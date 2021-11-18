"""
fagelsang.py

The Birds, translated for birds.

Copyright 2021 Nathan Mifsud <nathan@mifsud.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import time
from numpy import random
from nltk.tokenize import word_tokenize, SyllableTokenizer

cast = {
    'EUELPIDES': 'euel',
    'PISTHETAERUS': 'pist',
    'EPOPS': 'epop',
    'TROCHILUS': 'troc',
    'PHOENICOPTERUS': 'phoe',
    'HERALD': 'hera',
    'PRIEST': 'prie',
    'A POET': 'apoe',
    'POET': 'poet',
    'A PROPHET': 'apro',
    'PROPHET': 'prop',
    'METON': 'meto',
    'AN INSPECTOR': 'ansp',
    'INSPECTOR': 'insp',
    'A DEALER IN DECREES': 'adea',
    'DEALER IN DECREES': 'deal',
    'IRIS': 'iris',
    'A PARRICIDE': 'apar',
    'PARRICIDE': 'parr',
    'CINESIAS': 'cine',
    'AN INFORMER': 'anin',
    'INFORMER': 'info',
    'PROMETHEUS': 'prom',
    'POSIDON': 'posi',
    'TRIBALLUS': 'trib',
    'HERACLES': 'hera',
    'MESSENGER': 'mess',
    'A MESSENGER': 'ames',
    'SECOND MESSENGER': 'smes',
    'CHORUS': 'chor',
    'A SERVANT': 'aser'
}

vowel_sounds = ['ee','ye','eh','e','wi','hi','ri','i','ra','ah',
                'aw','ar','ua','a','uo','hu','u','ho','oo','o']

variant_endings = ['r','rhk','rk','k','m']

consonant_pairs = {
    'b': ['r','p','k'],
    'c': ['k','r','p','ppity'],
    'd': ['t','ee'],
    'f': ['i','e','ee'],
    'g': ['w'],
    'h': ['h','nk','oo'],
    'j': ['a','aa','rrr'],
    'k': ['r','k','rk','p','tchu','wk','sh','eep'],
    'l': ['i','nk','oo'],
    'm': ['i','e'],
    'n': ['p','rk'],
    'p': ['p','t','k','r','rr','rrp','rt','eet','ee'],
    'q': ['k','ck','ip','ir','ark'],
    'r': ['aah','i','e','ee','rrr'],
    's': ['k','ou','e','ee','eep'],
    't': ['t','k','nk','p','ee','eek','oo'],
    'v': ['it','e','ee','eer'],
    'w': ['p','t','k','w','hoo','oo','ah','chity'],
    'x': [''],
    'y': ['k','aa','owk'],
    'z': ['t','ee']
}


def has_punct(s):
    return any(p in s for p in ".,;:!?'…-—")


def get_pair(s):
    c = s[0].lower()
    if c in 'aeiou' and random.rand() < .5:
        p = random.choice(variant_endings)
    else:
        p = consonant_pairs.get(c)
        p = random.choice(p) if type(p) is list else ''
    return p


def extend_vowel(s):
    for l in s:
        if l in 'aeio':
            m = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,4])
            s = s.replace(l, l*m, 1)
            break
    return s


def repeat_sound(s):
    # how many repetitions (and how to separate them)
    if len(s) > 2:
        r = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,4])
        sep = ' ' if random.rand() < .8 else '-'
    else: # more likely to repeat shorter sounds
        r = random.choice([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,4,5,6])
        if random.rand() < .6:
            sep = '-'
        elif random.rand() < 3 and not s.isupper():
            sep = ''
        else:
            sep = ' '

    # handle capitalisation
    if len(s) > 1 and r > 1:
        l = s.lower()
    elif r > 1:
        l = s # prevents turning 'I' lowercase
    else:
        l, sep = '', ''

    # build series of repetitions
    middle = '' if r == 1 else sep
    for _ in range(r-2): # to vary the vowel length per repeat
        middle += extend_vowel(l) + sep
    s = extend_vowel(s) + middle + extend_vowel(l)
    return s


def tokenize(speech):
    # see https://www.nltk.org/api/nltk.tokenize.sonority_sequencing.html
    SSP = SyllableTokenizer()
    tokens = [SSP.tokenize(t) for t in word_tokenize(speech)]
    tokens = [t for l in tokens for t in l] # flattens list of lists
    return tokens


def birdify(speech):
    birdified = ['']
    bird_sound = ''

    for token in tokenize(speech):
        # define separator
        if len(birdified) == 1:
            sep = '' # don't prepend separator to first sound
        elif random.rand() > .8 \
            and has_punct(birdified[-1]) == False:
            sep = '-' # occasionally hyphenate adjacent sounds
        else:
            sep = ' '

        # handle punctuation
        punct = ''
        if has_punct(token):
            if token in ["'",'-']:
                continue # strip hyphens and apostrophes
            elif len(token) == 1:
                punct = token # but retain periods, commas, etc
            else:
                token = token.replace("'", '', 1) # strip leftovers (e.g. 'twas)

        # birdify the word
        for sound in vowel_sounds:
            if sound in token \
                and not token.startswith(sound): # skip cases like 'a' and 'wi[th]'
                opening = token.split(sound,1)[0]
                bird_sound = opening + sound + get_pair(opening)
                break # no need to look for other sounds
            elif len(token) == 1 \
                and not token in ['a','I']: # for lonely letters (e.g. t from 'tis)
                bird_sound = token + random.choice(vowel_sounds)
            elif token[-1] == 'y':
                token = token.replace('y', random.choice(vowel_sounds), 1)
            elif punct == '':
                bird_sound = token

        speech = sep + repeat_sound(bird_sound) if punct == '' else ''
        birdified += speech + punct

    birdified = ''.join(birdified)

    return(birdified)


def translate(play):
    script = []

    for line in play:
        for c in cast:
            if line.startswith(c):
                line = line.split(c,1)[1].lstrip()

                if '(' not in line:
                    speech, action, more_speech = '', '', ''
                    for _ in range(random.choice([1,1,1,2,2,3,4])):
                        speech += line # adds higher-order repetition

                else: # handle stage directions
                    if line.startswith('('):
                        speech      = ''
                        action      = line.split(')',1)[0][1:]
                        more_speech = line.split(')',1)[1]
                    elif line.endswith(')'):
                        speech      = line.split('(',1)[0]
                        action      = line.split('(',1)[1]
                        more_speech = ''
                    else: # action in middle of dialogue
                        speech      = line.split('(',1)[0]
                        action      = line.split('(')[1].split(')')[0]
                        more_speech = line.split(')',1)[1]

                    action = ' \\direct{' + action + '} '

                speaker  = '\n\\' + cast[c] + 'speaks\n'
                dialogue = birdify(speech) + action + birdify(more_speech)
                script  += speaker + dialogue

    script = ''.join(script)

    return(script)


def publish(script):
    with open('template.tex') as f:
        doc = f.read().replace('script', script)

    filename = 'fagelsang-' + time.strftime('%y%m%d-%H%M%S') + '.tex'
    with open(filename, 'w') as f:
        f.write(doc)

    wc = str(len(script.split()))
    print('Generated ' + filename + ' (' + wc + ' words)')


if __name__ == '__main__':
    with open('the-birds.txt') as f:
        play = f.readlines()

    if len(sys.argv) == 1:
        publish(translate(play))
    else: # compare translation of given line
        line_num = int(sys.argv[1]) - 1
        line = play[line_num]
        print('\n' + line + translate([line]))