import hashlib
import sys

paths = []
if sys.argv[1:] != []:
    paths = sys.argv[1:] # DDされた全ファイルをpathsに格納

hashs = []

if(paths==[]):
    print('元ファイルをD&Dしてください')
    paths.append(input(': '))
    print('検証したいファイルをD&Dしてください')
    paths.append(input(': '))

for i, path in enumerate(paths):
        with open(path, 'rb') as f:
            f_data = f.read()
            hash = hashlib.sha256(f_data).hexdigest() # sha256
            hashs.append(hash)
            if(i==0): continue
            if(hashs[0] == hashs[i]):
                print(f'元ファイル: {paths[0]} と検証先ファイル: {paths[i]} は')
                print('同一ファイルです\n')
            else:
                print(f'元ファイル: {paths[0]} と検証先ファイル: {paths[i]} は')
                print('改ざんされています\n')

print('続行しますか？(Y/n)')
sentaku = input(': ')