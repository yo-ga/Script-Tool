# -*- coding: utf-8 -*-
# python 3.6
import sys
import csv
from gtts import gTTS

if len(sys.argv) < 2:
    print ("please add your file")
    sys.exit(-1)

filename = sys.argv[1]
sentences = []
with open(filename, newline="") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['sentences',])
    for row in reader:
        sentences.append(row['sentences'])

print("[Start] Load audio data")
for itr in range(0, len(sentences)):
    print("[Audio] audio_{}.mp3 for {}".format(itr, sentences[itr]))
    tts = gTTS(text=sentences[itr], lang='zh-tw')
    tts.save("audio_{}.mp3".format(itr))
