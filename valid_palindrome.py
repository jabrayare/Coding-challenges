import  re
def isPalindrome(s:str) -> bool:
  # removes white spaces, special characters, and converts all chars to lowercase.
  tmp = re.sub('[^A-Za-z0-9]', '', s).lower()
  first = 0
  last = len(tmp)-1
  while(first < last):
    # compare last and first chars
    if tmp[first] != tmp[last]:
      return False
    first += 1
    last -= 1
  return True

print(isPalindrome('Hello, world yea!'))
print(isPalindrome('ababa!'))
print(isPalindrome('aey dlrow olleh Hello, world yea!'))