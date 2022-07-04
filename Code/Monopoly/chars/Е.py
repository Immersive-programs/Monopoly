class char:
    def draw(buf,x,y,index,col):
        zero = x+8*index
        buf.line(zero,y,zero+6,y+6,col)
        buf.line(zero+6,y,zero,y+6,col)
        buf.line(zero+3,y,zero+3,y+6,col)
        buf.line(zero,y+1,zero+3,y+3,col)
        buf.line(zero,y+5,zero+3,y+3,col)
        buf.line(zero+6,y+1,zero+3,y+3,col)
        buf.line(zero+6,y+5,zero+3,y+3,col)
