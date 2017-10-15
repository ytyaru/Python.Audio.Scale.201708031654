# このソフトウェアについて

音階（スケール）を算出し、wavファイルに出力する。

メジャーとマイナーの各スケールにて、全キーの場合の音を鳴らす。

* スケールは2種(メジャー,マイナー)
* キーは12種(C,C#,D,D#,E,F,F#,G,G#,A,A#,B)
* 計24スケール
* 1スケール7音

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)

# 実行

```sh
$ python main.py
```

```sh
$ python main.py 
ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave
ALSA lib pcm.c:2239:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2239:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2239:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
bt_audio_service_open: connect() failed: Connection refused (111)
bt_audio_service_open: connect() failed: Connection refused (111)
bt_audio_service_open: connect() failed: Connection refused (111)
bt_audio_service_open: connect() failed: Connection refused (111)
ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave
---------- メジャー・スケール ----------
C メジャー・スケール
C   0   4 261.625565
D   2   4 293.664768
E   4   4 329.627557
F   5   4 349.228231
G   7   4 391.995436
A   9   4 440.000000
B  11   4 493.883301
C   0   5 261.625565
C+ メジャー・スケール
C#  1   4 277.182631
D#  3   4 311.126984
F   5   4 349.228231
F#  6   4 369.994423
G#  8   4 415.304698
A# 10   4 466.163762
C   0   5 261.625565
C#  1   5 277.182631
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
D メジャー・スケール
D   2   4 293.664768
E   4   4 329.627557
F#  6   4 369.994423
G   7   4 391.995436
A   9   4 440.000000
B  11   4 493.883301
C#  1   5 277.182631
D   2   5 293.664768
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
D+ メジャー・スケール
D#  3   4 311.126984
F   5   4 349.228231
G   7   4 391.995436
G#  8   4 415.304698
A# 10   4 466.163762
C   0   5 261.625565
D   2   5 293.664768
D#  3   5 311.126984
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
E メジャー・スケール
E   4   4 329.627557
F#  6   4 369.994423
G#  8   4 415.304698
A   9   4 440.000000
B  11   4 493.883301
C#  1   5 277.182631
D#  3   5 311.126984
E   4   5 329.627557
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
F メジャー・スケール
F   5   4 349.228231
G   7   4 391.995436
A   9   4 440.000000
A# 10   4 466.163762
C   0   5 261.625565
D   2   5 293.664768
E   4   5 329.627557
F   5   5 349.228231
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
F+ メジャー・スケール
F#  6   4 369.994423
G#  8   4 415.304698
A# 10   4 466.163762
B  11   4 493.883301
C#  1   5 277.182631
D#  3   5 311.126984
F   5   5 349.228231
F#  6   5 369.994423
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
G メジャー・スケール
G   7   4 391.995436
A   9   4 440.000000
B  11   4 493.883301
C   0   5 261.625565
D   2   5 293.664768
E   4   5 329.627557
F#  6   5 369.994423
G   7   5 391.995436
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
G+ メジャー・スケール
G#  8   4 415.304698
A# 10   4 466.163762
C   0   5 261.625565
C#  1   5 277.182631
D#  3   5 311.126984
F   5   5 349.228231
G   7   5 391.995436
G#  8   5 415.304698
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
A メジャー・スケール
A   9   4 440.000000
B  11   4 493.883301
C#  1   5 277.182631
D   2   5 293.664768
E   4   5 329.627557
F#  6   5 369.994423
G#  8   5 415.304698
A   9   5 440.000000
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
A+ メジャー・スケール
A# 10   4 466.163762
C   0   5 261.625565
D   2   5 293.664768
D#  3   5 311.126984
F   5   5 349.228231
G   7   5 391.995436
A   9   5 440.000000
A# 10   5 466.163762
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
B メジャー・スケール
B  11   4 493.883301
C#  1   5 277.182631
D#  3   5 311.126984
E   4   5 329.627557
F#  6   5 369.994423
G#  8   5 415.304698
A# 10   5 466.163762
B  11   5 493.883301
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
---------- マイナー・スケール ----------
C マイナー・スケール
C   0   4 261.625565
D   2   4 293.664768
D#  3   4 311.126984
F   5   4 349.228231
G   7   4 391.995436
G#  8   4 415.304698
A# 10   4 466.163762
C   0   5 261.625565
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
C+ マイナー・スケール
C#  1   4 277.182631
D#  3   4 311.126984
E   4   4 329.627557
F#  6   4 369.994423
G#  8   4 415.304698
A   9   4 440.000000
B  11   4 493.883301
C#  1   5 277.182631
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
D マイナー・スケール
D   2   4 293.664768
E   4   4 329.627557
F   5   4 349.228231
G   7   4 391.995436
A   9   4 440.000000
A# 10   4 466.163762
C   0   5 261.625565
D   2   5 293.664768
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
D+ マイナー・スケール
D#  3   4 311.126984
F   5   4 349.228231
F#  6   4 369.994423
G#  8   4 415.304698
A# 10   4 466.163762
B  11   4 493.883301
C#  1   5 277.182631
D#  3   5 311.126984
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
E マイナー・スケール
E   4   4 329.627557
F#  6   4 369.994423
G   7   4 391.995436
A   9   4 440.000000
B  11   4 493.883301
C   0   5 261.625565
D   2   5 293.664768
E   4   5 329.627557
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
F マイナー・スケール
F   5   4 349.228231
G   7   4 391.995436
G#  8   4 415.304698
A# 10   4 466.163762
C   0   5 261.625565
C#  1   5 277.182631
D#  3   5 311.126984
F   5   5 349.228231
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
F+ マイナー・スケール
F#  6   4 369.994423
G#  8   4 415.304698
A   9   4 440.000000
B  11   4 493.883301
C#  1   5 277.182631
D   2   5 293.664768
E   4   5 329.627557
F#  6   5 369.994423
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
G マイナー・スケール
G   7   4 391.995436
A   9   4 440.000000
A# 10   4 466.163762
C   0   5 261.625565
D   2   5 293.664768
D#  3   5 311.126984
F   5   5 349.228231
G   7   5 391.995436
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
G+ マイナー・スケール
G#  8   4 415.304698
A# 10   4 466.163762
B  11   4 493.883301
C#  1   5 277.182631
D#  3   5 311.126984
E   4   5 329.627557
F#  6   5 369.994423
G#  8   5 415.304698
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
A マイナー・スケール
A   9   4 440.000000
B  11   4 493.883301
C   0   5 261.625565
D   2   5 293.664768
E   4   5 329.627557
F   5   5 349.228231
G   7   5 391.995436
A   9   5 440.000000
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
A+ マイナー・スケール
A# 10   4 466.163762
C   0   5 261.625565
C#  1   5 277.182631
D#  3   5 311.126984
F   5   5 349.228231
F#  6   5 369.994423
G#  8   5 415.304698
A# 10   5 466.163762
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
B マイナー・スケール
B  11   4 493.883301
C#  1   5 277.182631
D   2   5 293.664768
E   4   5 329.627557
F#  6   5 369.994423
G   7   5 391.995436
A   9   5 440.000000
B  11   5 493.883301
ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred
```

## wavファイル作成

```sh
$ cd src/
$ python WaveFile.py
```

oggファイルはGUIツールのSoundConverterで生成した。pythonの標準ライブラリでは不可。

# 参考

音名。

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

ほぼ丸パクリした。感謝。

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

