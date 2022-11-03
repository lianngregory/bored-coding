#list of letters and morse code translation!
words = {"a" : "*-", "b" : "-***", "c" : "-*-*", "d" : "-**", "e" : "*", "f" : "**-*", "g" : "--*", "h" : "****", "i" : "**", "j" : "*---", "k" : "-*-", "l" : "*-**" , "m" : "--", "n" : "-*", "o" : "---", "p" : "*--*", "q" : "--*-", "r" : "*-*", "s" : "***", "t" : "-", "u" : "**-", "v" : "***-", "w" : "*--", "x" : "-**-", "y" : "-*--", "z" : "--**"}

#blank list to append later with translated phrase
translate = []

#taking in user input
userEnter = input("Please type a sentence or phrase, and I will translate it to morse code for you!")

userEnter = userEnter.lower() #lowercases everything!

letters = [x for x in userEnter] #splits words into individual characters to then translate

#for each word, translate it if its in the dict!
for w in letters:
    if w in words:
        translate.append(words[w])
    else:
        translate.append(w)

#print the snazzy phrase!!
print(*translate)