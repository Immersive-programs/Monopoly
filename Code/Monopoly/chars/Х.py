class char:
    def draw(buf,x,y,index,col):
        zero = x+8*index
        buf.text('X', zero, y, col)
