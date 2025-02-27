#📢 Day 3 – Daily Python Challenge 🐍
#🚀 Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi! 🔢💡

num = int(input("Enter Your Number:"))
if num < 1:
    print("No, Its Not A Prime Number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
         is_prime = False
        break
    if is_prime:
        print("Yes, Its A Prime Number")
    else:
        print("No, Its Not A Prime Number")