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

user_name_how = random.randint(1, 9)
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
else:
	print "user_name_how unexpected vaule"
print user_name
