import os
import random
import send_mail

#opening test data csv file
with open('testdata.csv','r') as testdata:
    data = testdata.read()
split_list = data.splitlines()
rows = len(split_list)

old_data=split_list[0].split(',')
print("old_data: ",old_data)

#count=0

column=len(old_data)

with open('base.xml','r') as base_xml:
    read_data=base_xml.read()

folder_name='modifield_xmls_'+str(random.randint(1,9999))

os.mkdir(folder_name)
print('\nYour new xmls is in ' +folder_name+' folder')


for index in range(1,rows):

    filename='./'+folder_name+'/'+'modified_'+str(index)+'.xml'
    print('modified_'+str(index)+'.xml')
    final_data=split_list[index].split(',')
    with open(filename,'w+') as new_xml:
           new_xml.write(read_data)
    for count in range(0,column):
            with open(filename,'r') as new_xml:
                read_data1 =new_xml.read()
            with open(filename,'w+') as new_xml:
                new_xml.write(read_data1.replace(old_data[count],final_data[count]))
    #send_mail.send_email(filename)
	#uncomment and enable above line to send mail


