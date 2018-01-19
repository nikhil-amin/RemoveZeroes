#Nikhil Amin -:- https://github.com/nikhilamin073
#Python Script to delete the Product row which has 0 quantity.

import csv, os							#importing required modules

os.getcwd()							
print "\nYou are in " + os.getcwd()				#prints your current working directory
 	
directory = raw_input("\nEnter your file's directory: ")
type(directory)							#enter your directory path from the current working directory

try:
	os.chdir(directory)					#changes the path to working file's directory location
	path = os.getcwd()
except:
	print "\nInvalid Path!"
	quit()							#If Invalid directory, Terminate the Script

print "You are in " + path

fname = raw_input("\nEnter your CSV filename (without extension) : ")
type(fname) 							#Enter the source CSV fileName
my_file = fname + '.csv'					#Adding .csv extention

if os.path.isfile(my_file) == False:
	print "File " + my_file + " does not exists."
	quit()							#If Invalid File, Terminate the Script

x = input("Enter Quantity Column Number: ") 			#Input the Quantity coloumn number	
type(x)
x -= 1

oname = raw_input("Enter your Output CSV filename (without extension) : ")
type(oname)							#Enter the output CSV fileName (any)
out_file = oname + '.csv' 					#Adding .csv extention

ofile  = open(out_file, "wb")					#opens output file in 'read' mode
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	
if os.path.isfile(my_file) == True:				#checks if source file is present or not
	with open(my_file, 'rb') as csvfile:			#opens source file in 'read' mode
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

		for col in csvreader:
			if col[x] == "0":			
				continue;			#Ignores the row having value 0 in the csv column
			else:				
				writer.writerow(col)		#writes pointing row of source file into output file 

print "\nSuccess! \nCheck your output file '"+ out_file + "' at '" + path + "'"
