class char:
    def draw(buf,x,y,index,col):
        zero = x+8*index
        buf.line(zero+1,y+6,zero+4,y+6,col)
        buf.line(zero+1,y,zero+4,y,col)
        buf.line(zero+5,y+1,zero+5,y+2,col)
        buf.line(zero+6,y+1,zero+6,y+2,col)
        buf.line(zero+5,y+5,zero+5,y+4,col)
        buf.line(zero+6,y+5,zero+6,y+4,col)
        buf.line(zero+2,y+3,zero+4,y+3,col)
