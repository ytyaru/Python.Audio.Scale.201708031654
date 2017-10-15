#http://qiita.com/mzmttks/items/7a7c8c4b42007e13812a
import wave
class WaveFile:
    @staticmethod
    def Write(data, bit=16, fs=8000, channels=1, filename='output.wav'):    
        wf = wave.open(filename, "w")
#        wf.setnchannels(channels)
#        wf.setsampwidth(bit / 8)
#        wf.setframerate(fs)
        wf.setparams((
            channels,                 # channel
            int(bit / 8),             # byte width
            fs,                       # sampling rate
            len(data),                # number of frames
            "NONE", "not compressed"  # no compression
        ))
        wf.writeframes(data)
        wf.close()

if __name__ == "__main__" :
    import Sampler
    import BaseWaveMaker
    import MusicTheory.EqualTemperament
    import MusicTheory.Scale
    wm = BaseWaveMaker.BaseWaveMaker()
    sampler = Sampler.Sampler()
    scale = MusicTheory.Scale.Scale()
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(key, 'メジャー・スケール')
        scale.Major(key=key)
        waves = []
        for f0 in scale.Frequencies:
            waves.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.25)))
#            p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.25)))
#            p.Play(sampler.Sampling(wm.Triangle(a=1, fs=8000, f0=f0, sec=0.25)))
        WaveFile.Write(b''.join(waves), filename=key.replace('+', 's') + 'Major' + '.wav')
        
        print(key, 'マイナー・スケール')
        scale.Minor(key=key)
        waves = []
        for f0 in scale.Frequencies:
            waves.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.25)))
        WaveFile.Write(b''.join(waves), filename=key.replace('+', 's') + 'Minor' + '.wav')

