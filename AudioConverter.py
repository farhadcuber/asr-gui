import os

def AudioConverter(file):
    if '/' in file:
        _, out = tuple(file.rsplit('/', 1))
    else:
        out = file

    os.system('ffmpeg -y -i %s -acodec pcm_s16le -ac 1 -ar 16000 recordings/%s.tmp.wav' % (file, out))
    return 'recordings/%s.tmp.wav' % out