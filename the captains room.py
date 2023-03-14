https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
from collections import Counter 
if __name__=="__main__":
   n=int(input())
   a=Counter(list(map(int, input().split())))
   print(list(a.keys())[list(a.values()).index(1)])
