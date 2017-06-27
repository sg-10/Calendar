from datetime import datetime


def create():
    check = True
    while check:
        st_date = raw_input("Start date and time ")
        try:
        	sd = datetime.strptime(st_date, '%d-%m-%Y %H:%M')
        except Exception as e:
        	print "Wrong format"
        	continue
        if sd < datetime.now():
            print "Start date is in the past. Please enter again"
            continue
        en_date = raw_input("End date and time ")
        ed = datetime.strptime(en_date, '%d-%m-%Y %H:%M')
        if sd > ed:
            print "End date is wrong. Please enter again"
            continue
        check = False
    desc = raw_input("Description ")
    file_data = open('details.txt', 'a')
    file_data.write(str(st_date+" "+en_date+" "+desc + "\n"))
    file_data.close()
    print "Event Created"
    return


def search():
	lines = list()
	with open('details.txt','r') as f:
		for line in f:
			t = line.rstrip('\n')
			t = str(t)
			lines.append(t)
	f.close()
	del_eve = raw_input("Search for event ")
	del_eve = del_eve.lower()
	events = list()
	for line in lines:
		if del_eve in line.lower():
			events.append(line)
	return lines, events

def read():
    # file_data = open('details.txt', 'r').read()
    lines, events = search()
    print "Calendar Details:"
    # print file_data
    # print type(file_data)
    for event in events:
    	print event
    return


def update():
	ret = delete(True)
	if ret:
		create()
	return


def delete(update=False):
	# f = open("details.txt", 'r')
	# lines = f.readlines()
	# print lines
	# f.close()
	# lines = list()
	# with open('details.txt','r') as f:
	# 	for line in f:
	# 		t = line.rstrip('\n')
	# 		t = str(t)
	# 		lines.append(t)
	# f.close()
	# del_eve = raw_input("Search for event ")
	# del_eve = del_eve.lower()
	# events = list()
	# for line in lines:
	# 	if del_eve in line.lower():
	# 		events.append(line)
	lines, events = search()
	length = len(events)
	if length:
		for i,event in enumerate(events):
			print i, ':', event
		if not update:
			print  length, ": All"
		to_del = input("Choose event ")
		if to_del == length and not update:
			f = open("details.txt",'w')
			for line in lines:
				if line not in events:
					f.write(line)
					f.write('\n')
			f.close()
		else:
			if to_del < length:
				f = open("details.txt",'w')
				for line in lines:
					if line != events[to_del]:
						f.write(line)
						f.write("\n")
				f.close()
				return True
			else:
				# print to_del, length
				print "Number not listed\n"
				return False
	else:
		print "No event found\n"
		return False


def choose(option):
    value = {1: create, 2: read, 3: update, 4: delete, 5: exit}
    ret = value.get(option, None)
    if ret:
        ret()
    else:
        print "Try Again"

while 1:
    x = input("Choose\n1: Create 2: Read 3: Update 4: Delete 5: Exit\n")
    choose(x)
