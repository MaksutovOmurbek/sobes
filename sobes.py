# import random

# def to_file(lst, sobes):
#     random_value = random.choice(lst)
    
  
#     with open(sobes, 'w') as file:
#         file.write(random_value)

   
#     return random_value

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

# selected_language = to_file(language, "language.txt")
# print(selected_language)

 
# def print_zero_rows():
#     for i in range(5):
#         print(f"{i+1}: {'0'}")

# print_zero_rows()

names = ["azat", "zina", "kuma", "anna", "sas"]
user = filter(lambda x: x == x[::-1], names)
print(list(user))


