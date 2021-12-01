def func():
    pass
    return

if __name__ == '__main__':
   try:
      f = open('./testfile.txt','r')
      length = len(f.read())
      f.close()
      print(length)
      pass
   except Exception as e:
      pass
#fUn 분리
#callback 함수 만들기