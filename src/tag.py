from string import Template

"""
template_str = '''<audio controls>
    <source src="https://raw.githubusercontent.com/ytyaru/Audio.Sample.201708031714/master/20170803/ogg/CMajor.ogg">
    <source src="https://raw.githubusercontent.com/ytyaru/Audio.Sample.201708031714/master/20170803/wav/CMajor.wav">
</audio>
'''
"""

template_str = '''${scale_show}|<audio controls src="https://raw.githubusercontent.com/ytyaru/Python.Audio.Scale.201708031654/master/res/wav/${scale_name}.wav"></audio>|<audio controls src="https://raw.githubusercontent.com/ytyaru/Python.Audio.Scale.201708031654/master/res/ogg/${scale_name}.ogg"></audio>
'''

#['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
#['C','Cs','D','Ds','E','F','Fs','G','Gs','A','As','B']

template = Template(template_str)

table_body = ''
for scale in ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']:
    table_body += template.substitute(scale_show=scale+' Major', scale_name=scale.replace('#', 's')+'Major')
for scale in ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']:
    table_body += template.substitute(scale_show=scale+' Minor', scale_name=scale.replace('#', 's')+'Minor')

table = '''Scale|wav|ogg
-----|---|---
'''

print(table + table_body)
