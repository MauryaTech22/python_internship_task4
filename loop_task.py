print("===== TASK 4: LOOPS & ITERATIONS =====\n")

# 1. Print numbers from 1 to 100 using for loop
print("1. Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n\n")

# 2. Countdown timer using while loop
print("2. Countdown Timer:")
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Countdown Finished!\n")

# 3. break and continue example
print("3. Break and Continue Example:")
for i in range(1, 11):
    if i == 5:
        print("Skipping number 5")
        continue
    if i == 8:
        print("Breaking loop at 8")
        break
    print(i)
print()

# 4. Iterate over string characters
print("4. Iterating over string:")
name = "Python"
for char in name:
    print(char)
print()

# 5. Multiplication table of a number
print("5. Multiplication Table of 5:")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# 6. range() with steps
print("6. range() with steps (Even numbers 2 to 20):")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# 7. Loop with condition (Check even/odd)
print("7. Even or Odd Check:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
print()

# 8. Real-world example: Password attempts
print("8. Real-world Example: Password Attempts")
correct_password = "admin123"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)
else:
    print("Account Locked!")

print("\n===== TASK COMPLETED SUCCESSFULLY =====")
