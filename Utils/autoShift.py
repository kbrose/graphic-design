import sys
import os

def autoShift(txt):
    xshift = []
    yshift = []
    out = ''
    for line in txt.split('\n'):
        line = line.rstrip()
        if '\\begin{scope}' in line:
            curr_xshift = 0.0
            curr_yshift = 0.0
            # if 'xshift' in line:
            #     x = line.find('xshift')
            #     x2 = line[x:].find('=')
            #     if 'c' not in line[(x+x2):]:
            #         print 'Error in line "' + line + '", missing "cm" unit'
            #         quit()
            #     x3 = line[(x+x2):].find('c')
            #     curr_xshift += float(line[x+x2+1:x3-1])
            #     if ',' in line[x+x2:]:
            #         x4 = line[x+x2:].find(',')+1
            #     else:
            #         x4 = line[x+x2:].find(']')
            #     line = line[0:x] + line[x+x2+x4]
            # if 'yshift' in line:
            #     x = line.find('yshift')
            #     x2 = line[x:].find('=')
            #     if 'c' not in line[(x+x2):]:
            #         print 'Error in line "' + line + '", missing "cm" unit'
            #         quit()
            #     x3 = line[(x+x2):].find('c')
            #     curr_yshift += float(line[x+x2+1:x3-1])
            #     if ',' in line[x+x2:]:
            #         x4 = line[x+x2:].find(',')+1
            #     else:
            #         x4 = line[x+x2:].find(']')
            #     line = line[0:x] + line[x+x2+x4]
            if 'shift' in line:
                x1 = line.find('shift')
                x2 = line[x1:].find('{') + x1
                x3 = line[x2:].find('(') + x2
                x4 = line[x2:].find(',') + x2
                x5 = line[x2:].find(')') + x2
                x6 = line[x2:].find('}') + x2
                curr_xshift += float(line[x3+1:x4])
                curr_yshift += float(line[x4+1:x5])
                if ',' in line[x6:]:
                    x6 = line[x6:].find(',')
                else:
                    x1 = line.find('[')
                    x6 = line.find(']')
                print line
                line = line[0:x1] + line[x6 + 1:]
            xshift = xshift + [curr_xshift]
            yshift = yshift + [curr_yshift]
            print xshift
            print yshift
        elif '\\end{scope}' in line:
            xshift = xshift[:-1]
            yshift = yshift[:-1]
            print line
            print xshift
            print yshift
        else:
            line2 = ''
            i = 0
            while '(' in line[i:]:
                x1 = i + line[i:].find('(')
                x2 = i + line[i:].find(')')
                x3 = line[x1:x2].find(',')
                if x3 == -1:
                    line2 = line2 + line[i:x2+1]
                    i = x2+1
                    continue
                x_coord = float(line[x1+1:x1+x3])
                y_coord = float(line[x1+x3+1:x2])
                x_coord = x_coord + sum(xshift)
                y_coord = y_coord + sum(yshift)
                line2 = line2 + line[i:x1] + '(' + str(x_coord) + ', ' + str(y_coord) + ')'
                i = x2 + 1
            line2 = line2 + line[i:]
            line = line2
        out = out + line + os.linesep
    return out


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Error, at least one file input required.'
        quit()

    f1 = sys.argv[1]
    f1 = open(f1, 'r')
    textIn = f1.read()

    if len(sys.argv) > 2:
        f2 = sys.argv[2]
        f2 = open(f2, 'w')
        f2.write(autoShift(textIn))
    else:
        print autoShift(textIn)
