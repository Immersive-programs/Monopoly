class char:
    def draw(buf,x,y,index,col):
        zero = x+8*index
        buf.line(zero,y,zero,y+6,col)
        buf.line(zero+1,y,zero+1,y+6,col)
        buf.line(zero+6,y,zero+6,y+6,col)
        buf.line(zero+5,y,zero+5,y+6,col)
        buf.line(zero,y,zero+6,y,col)
