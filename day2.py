#📢 Day 2 – Daily Python Challenge 🐍 

#🚀 Challenge: Aisa Python program likhna hai jo user se ek sentence le aur usme jitne words hain, count kare! 🔢💡  

#🔥 Example:  
#📌 Input: "Python is amazing!"  
#📌 Output: Total words: 3  

#💡 Hint: 
#- split() function ka use karke sentence ko words me tod sakte ho.  
#- len() function se words ki total count nikal sakte ho.

# take input from user
Sent = input ("Enter a sentence:")

# breaking the sent into words using split() function
words = Sent.split()

# Counting the total number of words
total_words = len(words)

# Displaying the result
print(f"Total words: {total_words}")