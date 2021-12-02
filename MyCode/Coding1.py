#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta


print("Output #1: I'm excited to learn Python.")
x = 4
y = 5
z=x+y
print("Output #2: Four plus five equals {0:d}.".format(z))

a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c= a+b
print("Output #3: {0}, {1}, {2}".format(a,b,c))

x = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))

print("Output #7: {0:3f}".format(8.3/2.7))
y = 2.5*4.8
print("Output #8: {0:1f}".format(y))
r = 8/float(3)
print("Output #9: {0:2f}".format(r))
print("Output #10: {0:4f}".format(8.0/3))

print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))


print("Output #14: {0:s}".format('I\'m enjoying learning Python.'))


print("Output #15: {0:s}".format("This is a long string.  Without the backslash \
it would run off of the page on the right in the text editor and be very \
difficult to read and edit.  By using the backslash you can split the long \
string into smaller strings on separate lines so that the whole string is easy \
to view in the text editor."))


print("Output #16: {0:s}".format('''You can use triple single quotes 
for full multi-line comment strings.'''))
print("Output #17: {0:s}".format("""You can use triple double quotes
for multi-line comment strings."""))


string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))
m = len(sentence)
print("Output #20: {0:d}".format(m))


string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
.format(string1_list2[0],string1_list2[1], string1_list2[2]))
string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1],string2_list[5],\
string2_list[-1]))
print("Output #25: {0}".format(','.join(string2_list)))

string3 = " Remove unwanted characters  from this string.\t\t    \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))


#制表符示例
print("学号\t姓名\t语文\t数学\t英语")
print("2017001\t曹操\t99\t\t88\t\t0")
print("2017002\t周瑜\t92\t\t45\t\t93")
print("2017008\t黄盖\t77\t\t82\t\t100")







string4 = "$$Here's another string that has unwanted vharacters.__---++"
print("Output #30: {0:s}".format(string4))
string4 = "$$The unwanted characters have been moved.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ","!@!")
print("Output #32(with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ",",")
print("Output #33(with commas): {0:s}".format(string5_replace))

string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's wHAT Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string5 = "Here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string7.capitalize()))
string5_list = string5.split()
print("Output #37(on each word):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))

string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
    	count += 1
print("Output #38: {0:d}".format(count))

string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)",re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))

string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {:s}".format(pattern.sub("a", string)))

today = date.today()
print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_daytime = datetime.today()
print("Output #45: {0!s}".format(current_daytime))

#Output #41: today: 2021-12-01; Output #42: 2021; Output #43: 12; Output #44: 1;Output #45: 2021-12-01 21:03:21.738656

one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))
#Output #45: 2021-12-01 21:07:19.128404; Output #46: yesterday: 2021-11-30; Output #47: -1 57600

date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))

print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))
#Output #50: 12/02/2021; Output #51: Dec 02 2021; Output #52: 2021-12-02; Output #53: December 02, 2021


date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))

print("Output #56: {!s}".format(datetime.date(datetime.strptime\
(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime\
(date4, '%B %d, %Y'))))
#注意换行 Output #54: 2021-12-02 00:00:00; Output #55: 2021-12-02 00:00:00; Output #56: 2021-12-02; Output #57: 2021-12-02






#1.4.5 列表
a_list = [1,2,3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle',9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements.".format\
(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))














































































