import os

def main():
  # prompt user for directory
  directory = input("Enter dicrectory to save file: ")
# directory defaults to current directory if user presses enter key
  if directory == "":
    directory = "."
# checks that path is valid
  assert os.path.exists(directory), "Path does not exist."



# prompt user for filename

filename = input("Please enter the filename: ")



# # prompt for user details
directory = input("What is the directory that you would like to save the file : ")
name = input("Please enter name: ")
address = input("Please enter address: ")
phone = input("Please enter phone number: ")

 #checking if the directory exists
if os.path.isdir(directory):
    #createing and opening the file to write
    writeFile = open(os.path.join(directory,filename),'w')
    #writing the data by comma seperated
    writeFile.write(name+','+address+','+phone_number+'\n')
    #close the file after writing is done
    writeFile.close()

    print("File contents:")
    #reading the file for proof of storing
    readFile = open(os.path.join(directory,filename),'r')
    for line in readFile:
      print(line)
    readFile.close()
else:
    print("Sorry but that directory does not exist...")
main()