import argparse
import random
import string

user_name = ''

# Verbs and nouns for namegen
verbs = ['happy','sad','tall','short','malious','ravenous','smooth','loving','mean','weird','high','sober']
nouns = ['hacker','lumberjack','horse','unicorn','guy','girl','man','woman','male','female','men','women','duck','dog']
# Not Safe For Work verbs and nouns to be added in later
verbs_nfsw = ['drunk','shitfaced','rapie']
nouns_nfsw = ['rapist','fuck','pedophile']

starts = ["Touches_","Loves_","Hates_",'Licks_']
starts_nfsw = ["Gets_fucked_by_","Fucks_with_",'Humps_']

# The parser
parser = argparse.ArgumentParser(description='Generate a username')
parser.add_argument("-f", help="Firstname")
parser.add_argument("-l", help="Lastname")
parser.add_argument("-n", help="Use NFSW verbs and nouns")
args = parser.parse_args()

if args.n == 'yes':
	nouns = nouns + nouns_nfsw 
	starts = starts + starts_nfsw
elif args.n == 'only':
	nouns = nouns_nfsw
	starts = starts_nfsw

# Set first and last so I can reuse this code in namegen
first = args.f
last = args.l

# Random string generation
char_set = string.ascii_uppercase + string.digits
randstring = ''.join(random.sample(char_set*6, 6))

# Numbers that may be added to the username
numbers = ['one','two','three','four','five','seven','eight','nine','ten']

# Whats been done so far
# first letter + last name
# first 3 letters of first and all of last
# 2-5th of first and first 6 of last
# 1-2 of first and all of last
# first 3 of first and 3-4 of last
# first 3 of first and 1 of last
# 2-4 of first and 0-3 of last
# first 3 of first and 3-4 of last + numbers (spelled out)
# first + random string
# first + last but with first letter of first (john joe)
# first 3 + last 3 but with first letter of first (joh joe)

# How to generate the user name
user_name_how = random.randint(1,18)

# Code that generates username
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
	user_name = last[3:6] + last[0:2]
elif user_name_how == 14:
	user_name = random.choice(verbs) +'_'+ random.choice(nouns)
elif user_name_how == 15:
	user_name = first + random.choice(verbs) + random.choice(nouns) + last
elif user_name_how == 16:
	user_name = "The_one_and_only_" + first
elif user_name_how == 17:
	user_name = "The_one_and_only_" + first + "_the_" + random.choice(verbs) + "_" + last	
elif user_name_how == 18:
	how = random.randint(1,2)
	if how == 1:	
		user_name = random.choice(starts) + random.choice(verbs) + '_' + random.choice(nouns) + 's'
	elif how == 2:
		user_name = random.choice(starts) + random.choice(nouns) + 's'
else:
	print "user_name_how unexpected vaule\n" + str(user_name_how)

# If and how to repalce chars in the user name.
replace_char = random.randint(1,10)

# The code that replace chars in the user name
if replace_char == 1:
	user_name = user_name.replace('i', '1')
	user_name = user_name.replace('a', '4')
	user_name = user_name.replace('e', '3')
	user_name = user_name.replace('l','|')
elif replace_char == 2:
	user_name = user_name.replace('_', '-')
elif replace_char == 3:
	user_name = user_name.replace('_', '7')
elif replace_char == 4:
	user_name = user_name.replace('m','nn')
else:
	user_name = user_name

randstuff = random.randint(1,10)

# This codes adds random stuff to the end of a username so it's more unique
if randstuff == 1:
	user_name = user_name + randstring
else:
	user_name = user_name



print user_name