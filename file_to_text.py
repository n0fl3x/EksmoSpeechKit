import os
import grpc._channel as grpch

from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from speechkit.stt import AudioProcessingType

from speechkit import (
    creds,
    configure_credentials,
    model_repository,
)


load_dotenv(find_dotenv())


def file_to_text(filename: str = None) -> None or dict:
    """Функция транскрипизации готового аудиофайла в текст."""

    if type(filename) != str or not filename:
        print('Incorrect or empty filename.')
        return

    configure_credentials(
        yandex_credentials=creds.YandexCredentials(
            api_key=os.getenv('API_KEY'),
        ),
    )

    model = model_repository.recognition_model()
    model.model = 'general'
    model.language = 'ru-RU'
    model.audio_processing_type = AudioProcessingType.Full

    path = str(Path(__file__).parent.resolve()) + f'/audio/{filename}'

    try:
        result = model.transcribe_file(audio_path=path)
        line = result[0]
        res_dict = {
            'raw_text': line.raw_text,
            'normalized_text': line.normalized_text,
        }
        print('Raw text:\n', res_dict.get('raw_text'))
        print('Normalized text:\n', res_dict.get('normalized_text'))

    except grpch._Rendezvous:
        print('Incorrect API-key.')
        return
    except FileNotFoundError as er:
        print('File not found: %s' % er)
        return
    except Exception as ex:
        print(ex)
        return
    
    return res_dict


if __name__ == '__main__':
    file_to_text(input('Enter filename: '))
