import os

from dotenv import load_dotenv, find_dotenv
from speechkit.stt import AudioProcessingType

from speechkit import (
    creds,
    configure_credentials,
    model_repository,
)


load_dotenv(find_dotenv())


configure_credentials(
    yandex_credentials=creds.YandexCredentials(
        api_key=os.getenv('API_KEY'),
    ),
)


model = model_repository.recognition_model()
model.model = 'general'
model.language = 'ru-RU'
model.audio_processing_type = AudioProcessingType.Full

filename = str(input('Enter filename: '))
path = os.path.abspath(f'audio/{filename}')
result = model.transcribe_file(audio_path=path)

for c, res in enumerate(result):
    print(res.normalized_text)
