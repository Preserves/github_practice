def read_file(filename):

    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    new = []
    word_count1 = 0
    word_count2 = 0
    sticker_count1 = 0
    sticker_count2 = 0
    image_count1 = 0
    image_count2 = 0
    for line in lines:
        s = line.split()
        #time = s[0]
        name = s[1]
        if name == '劉育誠':
            if s[2] == '貼圖':
                sticker_count1 += 1
            elif s[2] == '圖片':
                image_count += 1
            else:    
                for m in s[2:]:
                    word_count1 += len(m)
        elif name == '惠芬luckymerry':
            if s[2] == '貼圖':
                sticker_count2 += 1
            elif s[2] == '圖片':
                image_count2 += 1
            else:
                for m in s[2:]:
                    word_count2 += len(m)
    print('劉育誠傳了', word_count1, '個字', end = ' ')
    print(sticker_count1, '個貼圖', end = ' ')
    print(image_count1, '次圖片')
    
    print('惠芬luckymerry說了', word_count2, '個字', end = ' ')
    print(sticker_count2, '個貼圖', end = ' ')
    print(image_count2, '次圖片')
    return new


#def write_file(filename, lines):
 #   with open(filename, 'w', encoding='utf-8') as f:
  #      for line in lines:
   #         f.write(line + '\n')


def main():
    lines = read_file('[LINE]mother.txt')
    lines = convert(lines)
    #write_file('output[LINE].txt', lines)
    

main()