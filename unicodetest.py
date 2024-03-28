# unicode字符
from turtle import rt


def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value = "%s",name = "%s",value2 = "%s"' %(value,name,value2))

# unicode_test('A')
# unicode_test('$')
# unicode_test('\u00a2')

# 编码(utf-8)
snowman = '\u2603'
len(snowman)
ds = snowman.encode('utf-8')
len(ds)
# print(snowman)
# print(ds)
# 解码(utf-8)
place = 'caf\u00e9'
type(place)
place_bytes = place.encode('utf-8')
type(place_bytes)
place2 = place_bytes.decode('utf-8')
# print(place2)

# 字节/字节数组
blist = [1,2,3,255]
# 字节(不可变)
the_bytes = bytes(blist)
# print('bytes = %s' %(the_bytes))
# 字节数组（可变）
the_byte_array = bytearray(blist)
# print('the_byte_array = %s' %(the_byte_array))
the_byte_array[1] = 127
# print('the_byte_array = %s' %(the_byte_array))

# 文件输入/输出
# fileobj = open(filename,mode)

# write()
poem = '''
        There was a young lady named Bright,
        Whose speed was far faster than light;
        She started one day in a relative way.
        And returned on the previous night.
        '''
# lenpoem = len(poem)
# fout = open('relativity','wt')
# # len = fout.write(poem)
# print(poem,file = fout,sep = '',end = '')
# # print(len)
# fout.close()

fout = open('relativity','wt')
offset = 0;
chunk = 100;
size = len(poem)
while True:
    if offset > size:
        break
    len = fout.write(poem[offset:offset+chunk])
    offset += chunk
    # print(len)

# read()/readline()/readlines()
# fin = open('relativity','rt')
# poem = fin.read()
# fin.close()
# print(len(poem))

# readline:读取一行数据
poem = ''
fin = open('relativity','rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem = poem+line
    print(len(poem))
fin.close()



