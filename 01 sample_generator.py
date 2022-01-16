import time
import random
import os

print("Process start")
start_time = time.time()

N = 100
alphabets_and_numbers = "abcdefghijklmnopqrstuvwxyz1234567890"
first_name = "김이박최정강조윤장임"
middle_name = "민서예지도하주윤채현지"
last_name = "준윤우원호후서연아은진"

def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabets_and_numbers)
    return result

def random_name():
    result = ""
    result += random.choice(first_name)
    result += random.choice(middle_name)
    result += random.choice(last_name)
    return result

os.mkdir("personal_info")

for i in range(N):
    name = random_name()
    filename = "personal_info/" + str(i) + "_" + name + ".txt"
    outfile = open(filename, "w")
    outfile.write("name : "       + name                   + "\n")
    outfile.write("age : "        + str(time.time())[-2:]  + "\n")
    outfile.write("e-mail : "     + random_string(8)       + "@naver.com\n")
    outfile.write("division : "   + random_string(4)       + "\n")
    outfile.write("Mobile : 010-" + str(time.time())[-4:]  + "-" + str(time.time())[-6:-2] + "\n")
    outfile.write("Sex : " + random.choice(['male', 'female']))
    outfile.close()

print("Process done")
end_time = time.time()
print("The job took " + str(end_time - start_time) + " seconds.")
