def rotate(string,comp):
  newstr=comp
  if(len(string)==len(comp)):
    if(string==comp):
      return True
    else:
      for i in range(len(string)):
        newstr=newstr[1:]+newstr[0]
        if(string==newstr):
          return True
      return False
  else:
    return False

if __name__ == "__main__":
  ans = rotate('ABCD','DACB')
  print(ans)
