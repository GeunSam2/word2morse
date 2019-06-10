import sys
import math
from Morse2 import Morse
from make_wave import waveFile

def make_sin_wave(sample_rate,frequency,duration,amplitude):
    data=[]
    samples_num=int(duration*sample_rate)
    volume=amplitude*32767
    for i in range(samples_num):
        value=math.sin(2*math.pi*i*frequency/sample_rate)
        data.append(int(value*volume))
    return data


def convert_text_to_morse_wave(text,filename):
    convert_text=Morse().convert(text)
    convert_exact_text=Morse('=','===').convert_exact(text)
    print(convert_text)

    sample_rate=8000 # 8000hz
    frequency=600 # 600hz
    dot_dur=0.05 # 50ms
    volume=0.8 # 80%

    wave=waveFile(sample_rate)
    wave_duration=0
    wave_data=[]
    for i in convert_exact_text:
        wave_duration=wave_duration+dot_dur
        if i !=' ':
            wave_data = wave_data + make_sin_wave(sample_rate,frequency,dot_dur,volume)
        else:
            wave_data = wave_data + make_sin_wave(sample_rate, frequency, dot_dur, 0)

    wave.add_data_subchunk(wave_duration,wave_data)
    wave.save(filename)

#메인 실행
if __name__ == '__main__':
    if len(sys.argv) == 3:
        convert_text_to_morse_wave(sys.argv[1], sys.argv[2])
    else:
        print("Error!! please retry input")

