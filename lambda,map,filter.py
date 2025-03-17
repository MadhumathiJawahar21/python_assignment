#lamda
#add a num
add=lambda x,y,z:x+y+z
print(add(290,34,523))

#find even or odd
num=lambda x:"even" if x%2==0 else "odd"
print(num(10))

#multiply
mul=lambda x,y:x*y
print(mul(293,234))

#maximum num
max=lambda x,y:x if x>y else y
print(max(10,20))

#square a num
square=lambda x:x*x
print(square(8))


#Map
#convert a given list to uppercase
wordsz=["hello","world","python","course"]
uppercase_word=map(lambda i:i.upper(), wordsz)
print(list(uppercase_word))

#add 10 of each num
list1=[100,200,300,400]
add_num=map(lambda x:x+10,list1)
print(list(add_num))

#find the length of each word
word=["madhu","divi","deepu","bala"]
length=map(lambda x:len(x), word)
print(list(length))

#multiple corresponding elements of two list
num1=[20,34,56,78]
num2=[76,23,45,68]
multiply=map(lambda x,y:x*y, num1,num2)
print(list(multiply))

#squareroot of each num in a list
import math
numbers=[4,6,9,21,27]
sqroot=map(lambda x:math.sqrt(x), numbers)
print(list(sqroot))


#filter

#filter a word with more than five letter
wordz=["welcome","to","python","free","course"] 
choose=filter(lambda x:len(x)>5, wordz)
print(list(choose))

#filter positive number from a list
numz=[1,-3,5,0,4,-8,-5,3,6,87,99,-566,-3]
positive_num=filter(lambda x:x>0, numz)
print(list(positive_num))


#filter a strings starts with A
words=["academy","institute","association","organization","artist"]
letter=filter(lambda x:x[0]=='a', words)
print(list(letter))

#filter a palindrome from a list of words
wordss=["madam","hello","mam","level"]
palindrome=filter(lambda x:x== x[::-1], wordss)
print(list(palindrome))

#filter a string end with s
wordd=["girls","women","boys","men","kids"]
end=filter(lambda x:x[-1]=='s', wordd)
print(list(end))