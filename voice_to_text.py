import pyaudio
import wave

from datetime import datetime

from file_to_text import file_to_text


def record_to_text() -> str:
    """Функция записи аудиофайла."""

    duration = None
    while not duration or duration <= 0:
        try:
            duration = int(input('Enter duration of record in seconds: '))
            if duration <= 0:
                print('Duration cannot be less or equal to zero.')
                continue
        except ValueError:
            print('Invalid duration value.')
            continue

    cuts = 1024
    piece_format = pyaudio.paInt16
    channels = 2
    rate = 44100

    now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'audio/{now}.wav'
    res_filename = f'{now}.wav'

    port = pyaudio.PyAudio()
    print('Recording...')
    stream = port.open(
        format=piece_format,
        channels=channels,
        rate=rate,
        frames_per_buffer=cuts,
        input=True,
    )

    frames = []
    for i in range(0, int(rate / cuts * duration)):
        data = stream.read(cuts)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    port.terminate()
    print('Finished recording.')

    wavefile = wave.open(f=filename, mode='wb')
    wavefile.setnchannels(nchannels=channels)
    wavefile.setsampwidth(sampwidth=port.get_sample_size(piece_format))
    wavefile.setframerate(framerate=rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    return res_filename


if __name__ == '__main__':
    file_to_text(record_to_text())
