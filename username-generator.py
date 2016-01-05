import argparse
import random
import string

parser = argparse.ArgumentParser(description='Generate fake data')
parser.add_argument("-f", help="Firstname")
parser.add_argument("-l", help="Lastname")
args = parser.parse_args()
first = args.f
last = args.l
char_set = string.ascii_uppercase + string.digits
randstring = ''.join(random.sample(char_set*6, 6))
replace_char = random.randint(1,10)
user_name_how = random.randint(1,11)
numbers = ['one','two','three','four','five','seven','eight','nine','ten']
if user_name_how == 1:
	user_name = first[0] + last
elif user_name_how == 2:
	user_name = first[0:2] + last[0:2]
elif user_name_how == 3:
	user_name = first[2:5] + last[0:5]
elif user_name_how == 4:
	user_name = first[1:2] + last
elif user_name_how == 5:
	user_name = first[0:2] + first[3:4]
elif user_name_how == 6:
	user_name = last[0:2] + last[1]
elif user_name_how == 7:
	user_name = first[2:4] + last[0:3]
elif user_name_how == 8:
	numbs = random.randint(10, 100)
	numbs = str(numbs)
	user_name = first[0] + last + " " + numbs
	user_name = user_name.replace(" ", "")
elif user_name_how == 9:
	user_name = first + randstring
elif user_name_how == 10:
	first = first[:1].upper() + first[1:]
	last = first[:1].upper() + last[1:]
	user_name = first + last
elif user_name_how == 11:
	first = first[:1].upper() + first[1:]
	last = first[:1].upper() + last[1:]
	user_name = first[0:2] + last[0:2]
elif user_name_how == 12:
	user_name = first + random.choice(numbers)
elif user_name_how == 13:
	username = last[3:6] + last[0:2]
else:
	print "user_name_how unexpected vaule"
if replace_char == 1:
	user_name = user_name.replace('i', '1')
	user_name = user_name.replace('a', '4')
	user_name = user_name.replace('e', '3')



print user_name
