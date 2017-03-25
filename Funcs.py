#Functions

def get_grid(x,y):
    return (int(x/32),int(y/32))



#takes direct string output from a .txt file and returns 3d array
def build_level(text):
    frames = []
    for i in range(len(text)-2):
        if "\n" in text[i]:
            if "\t" in text[i+1] and "\t" in text[i+2]:
                frames.append(text[i-1019:i])
                print i
    level = []
    for frame in frames:
        frame_out = []
        rows = frame.split("\n")
        for row in rows:
            cols = row.split("\t")
            cols.pop(len(cols)-1)
            cols = [int(x) for x in cols]
            frame_out.append(cols)
        level.append(frame_out)
    return level



