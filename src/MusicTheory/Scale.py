#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#http://www.chaco2008.com/theory/1-3_majorscale.html
#http://www.chaco2008.com/theory/2-3_minorscale.html
#メジャー・スケール=全,全,半,全,全,全,半
#マイナー・スケール=全,半,全,全,半,全,全
#全音=2, 半音=1
#CMajor=C,D,E,F,G,A,B
#Cminor=C,D,D#,F,G,G#,A#
import MusicTheory.EqualTemperament
import MusicTheory.Key
class Scale:
    def __init__(self):
        self.__major = [2,2,1,2,2,2,1]
        self.__minor = [2,1,2,2,1,2,2]
        self.__scales = []
        self.__frequencies = []
        self.__key_pitch = 4 # キーの音の高さ(C4等)
        self.__et = MusicTheory.EqualTemperament.EqualTemperament()

    @property
    def Scales(self): return self.__scales
    @property
    def Key(self): return self.__scales[0]
    @property
    def Frequencies(self): return self.__frequencies
    
    # ドレミファソラシド(C,D,E,F,G,A,B)
    def Major(self, key='C', pitch=4): return self.__create_scales(self.__major, key, pitch)
    def Minor(self, key='C', pitch=4): return self.__create_scales(self.__minor, key, pitch)
    def __create_scales(self, scales, key, pitch):
        self.__scales.clear()
        self.__frequencies.clear()
        k = MusicTheory.Key.Key()
        v = k.Get(key)
        self.__scales.append(v)
        k.Get(MusicTheory.Key.Key.ValueToName(v))
        self.__frequencies.append(self.__et.FromKey(k, pitch))
        for interval in scales:
            #0-11
            #-1-->11
            #-2-->10
            #12-->0
            #13-->1
            v += interval
            if v < 0: v = len(self.__et.Keys) - abs(v)
            elif len(self.__et.Ids)-1 < v:
                pitch += 1
                v %= len(self.__et.Ids)
            self.__scales.append(v)
            k.Get(MusicTheory.Key.Key.ValueToName(v))
            self.__frequencies.append(self.__et.FromKey(k, pitch))
            
#        print('self.__scales:', self.__scales)
#        print('self.__frequencies:', self.__frequencies)
        return self.__scales


if __name__ == '__main__':
    s = Scale()
    print('---------- メジャー・スケール ----------')
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(key, 'メジャー・スケール')
        print(s.Major(key=key))
        print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
    print('---------- マイナー・スケール ----------')
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(s.Minor(key=key))
        print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
