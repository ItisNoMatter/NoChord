import threading
import readchar
import sys
import time
import pygame 
import music21 as m21
from enum import Enum

class KeyType(Enum):
    NONE   = -1
    UPPER  = 0
    MIDDLE = 1
    LOWER  = 2

class KeyConfig:
    def __init__(self,func,keytype):
        self.func = func
        self.keytype = keytype


class NotesPlayer:
    def __init__(self,str_notes):
        self.keyconfig = {#きれいじゃないのであとでKeyConfigクラスを実装する
            "f":KeyConfig(self._play_chord,KeyType.UPPER), 
            "r":KeyConfig(self._play_chord,KeyType.MIDDLE),
            "j":KeyConfig(self._play_root,KeyType.MIDDLE),
            "u":KeyConfig(self._play_root,KeyType.UPPER),
            "k":KeyConfig(self._play_third,KeyType.MIDDLE),
            "i":KeyConfig(self._play_third,KeyType.UPPER),
            "l":KeyConfig(self._play_fifth,KeyType.MIDDLE),
        }
        self.chord = m21.chord.Chord(str_notes)

        n_root = m21.note.Note(self.chord.root())#StreamオブジェクトにNoteオブジェクト他を渡してもうまく動かなかったので、事前にChordオブジェクトに変換してやる。
        self.root = m21.chord.Chord([n_root])

        n_third = m21.note.Note(self.chord.third)
        self.third = m21.chord.Chord([n_third])

        n_fifth = m21.note.Note(self.chord.fifth)
        self.fifth = m21.chord.Chord([n_fifth])
        self.i_arpeggio = 0
        self.arpeggio = [self.root,self.third,self.fifth]
    """ 
    TODO
    以下は動くか検証するのに時間かけたくなかったので未実装、__init__内での,self.rootやself.fifthなどの冗長な定義を共通化する。
    m21.chord.root()はPitchオブジェクトを返すが、Chordクラスの生成は引数にPitchオブジェクトを取れないのでNoteオブジェクトに変換している

    def _into_chord(method):
        n = m21.note.Note(self.chord.method())
    """
    def _play_chord(self):
        s = m21.stream.Stream(self.chord)
        sp = m21.midi.realtime.StreamPlayer(s)
        sp.play()
    
    def _play_arpeggio(self):
        s = m21.stream.Stream(self.arpeggio[self.i_arpeggio])
        self.i_arpeggio += 1
        sp = m21.midi.realtime.StreamPlayer(s)
        sp.play()
    def _play_root(self):
        s = m21.stream.Stream(self.root)
        sp = m21.midi.realtime.StreamPlayer(s)
        sp.play()
    def _play_third(self):
        s = m21.stream.Stream(self.third)
        sp = m21.midi.realtime.StreamPlayer(s)
        sp.play()
    def _play_fifth(self):
        s = m21.stream.Stream(self.fifth)
        sp = m21.midi.realtime.StreamPlayer(s)
        sp.play()
    def play(self,key):
        func = self.keyconfig[key].func #KeyConfigクラスの実装によってここが変わる
        func()

def _start_thread(target,args):
    t = threading.Thread(target=target,args=args)
    t.start()

def play(chordlist):
    current_keytype = KeyType.UPPER
    for i in range(len(chordlist)):#くそみたいな実装　早くリファクタリングするべき
        np = NotesPlayer(chordlist[i])
        while 1:
            kb = readchar.readchar()
            
            sys.stdout.flush()#enter押さずに入力受け取れるおまじない
            if kb != "":
                should_go_next = current_keytype != np.keyconfig[kb].keytype
                current_keytype = np.keyconfig[kb].keytype#ここも気持ち悪い　やはりkeyconfigは外部で持つべき
                if should_go_next:
                    try:
                        next_np = NotesPlayer(chordlist[i+1])
                        _start_thread(target=next_np.play,args=(kb,))
                        print(chordlist[i+1])
                        break
                    except IndexError:
                        print("finish")
                        exit()
                _start_thread(target=np.play,args=(kb,))
                print(chordlist[i])