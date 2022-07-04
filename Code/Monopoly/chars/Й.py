class char:
    def draw(buf,x,y,index,col):
        zero = x+8*index
        buf.text('/', zero, y, col)
        buf.line(zero+1,y,zero+1,y+6,col)
        buf.line(zero+2,y,zero+2,y+6,col)
        buf.line(zero+6,y,zero+6,y+6,col)
        buf.line(zero+7,y,zero+7,y+6,col)
        buf.line(zero+3,y-1,zero+5,y-1,col)
