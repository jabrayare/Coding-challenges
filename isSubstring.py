def isSubstring(str1, str2):
  if len(str1) < len(str2):
    return False
  first = 0
  second = 0
  while first < len(str1):
    if str1[first] == str2[second]:
      index = 0
      while second < len(str2):
        if str1[first] != str2[second]:
          break;
        else:
          index += 1
        second += 1
        first += 1
      if index == len(str2):
        return True
    first+=1
  return False

print(isSubstring("cat", "meow"))