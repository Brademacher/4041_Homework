import numpy as np

class Frame:
    def __init__(self, frame, frame_array):
        self.frame = frame
        self.frame_array = frame_array

    def __lt__(self, other):
        self.frame_array.comps = self.frame_array.comps + 1
        return self.frame[0,0][0] < other.frame[0,0][0]

    def __le__(self, other):
        self.frame_array.comps = self.frame_array.comps + 1
        return self.frame[0,0][0] <= other.frame[0,0][0]

    def __gt__(self, other):
        self.frame_array.comps = self.frame_array.comps + 1
        return self.frame[0,0][0] > other.frame[0,0][0]

    def __ge__(self, other):
        self.frame_array.comps = self.frame_array.comps + 1
        return self.frame[0,0][0] >= other.frame[0,0][0]

class FrameArray:
    def __init__(self, frames):
        self.frames = frames
        self.swaps = 0
        self.comps = 0

    def __getitem__(self, index):
        return self.frames[index]

    def __setitem__(self, index, val):
        self.swaps = self.swaps + 1
        self.frames[index] = val

    def __len__(self):
        return len(self.frames)
    