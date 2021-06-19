#!/usr/local/bin/python
# save this as my_bio.py

class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.seq = sequence
        
    def gc_content(self):
        G = self.seq.count('G')
        C = self.seq.count('C')
        return (G+C)/len(self.seq)
    
    def __len__(self):
        return len(self.seq)
    

def gc_content(seq):
    G = seq.count('G')
    C = seq.count('C')
    return (G+C)/len(seq)