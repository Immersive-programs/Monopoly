class char:
    def draw(buf,x,y,index,col):
        zero = x+8*index+1
        buf.line(zero+5,y,zero+5,y+6,col)
        buf.line(zero+6,y,zero+6,y+6,col)
        buf.line(zero,y+6,zero+2,y,col)
        buf.line(zero+1,y+6,zero+3,y,col)
        buf.line(zero+4,y,zero+5,y,col)
        buf.line(zero+4,y+1,zero+5,y+1,col)
