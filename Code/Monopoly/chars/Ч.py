class char:
    def draw(buf,x,y,index,col):
        zero = x+8*index+1
        buf.line(zero+1,y,zero+1,y+3,col)
        buf.line(zero+2,y,zero+2,y+3,col)
        buf.line(zero+4,y,zero+4,y+6,col)
        buf.line(zero+5,y,zero+5,y+6,col)
        buf.line(zero+1,y+3,zero+5,y+3,col)
        buf.line(zero+1,y+4,zero+5,y+4,col)
