import hashlib
# import sys

# paths = []
# if sys.argv[1:] != []:
#     paths = sys.argv[1:] # DDされた全ファイルをpathsに格納

paths = ['hoge1.txt', 'hoge2.txt', 'hoge3.txt']

hashs = []

for i, path in enumerate(paths):
    with open(path, 'rb') as f:
        # print(path)
        f_data = f.read()
        #sha256
        hash = hashlib.sha256(f_data).hexdigest()
        # print('sha256:', hash)
        hashs.append(hash)
        if(i==0): continue
        if(hashs[0] == hashs[i]):
            print(f'元ファイル: {paths[0]} と検証先ファイル: {paths[i]} は')
            print('同一ファイルです\n')
        else:
            print(f'元ファイル: {paths[0]} と検証先ファイル: {paths[i]} は')
            print('改ざんされています\n')

