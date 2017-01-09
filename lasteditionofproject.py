__author__ = 'Perus'

import os
import shutil
import os.path

os.getcwd()
os.chdir("/Users/fissalalsharef/Desktop")
def print_pofm():
    try:
        choice = raw_input("Please choose what do you want to do from the list: \n 1)Create a file \n 2)Delete a file \n 3)Rename a file \n 4)Copy a file \n 5)Move a file from one directory to another \n 6)Modifying Txt files \n Get a number: ")
        choice = int(choice)
        #help = str("\h")

        if choice == 1:
            help_input = input("If you do not know how to create a file please enter number 1 and if you know that please enter number 0: ")
            if help_input == 1:
                print "If you want to create a file please use open built-in function function"
                input1 = raw_input("If you want to continue, please press enter .. ")
                new_file = raw_input("Please write the name of the file that you want to create: ")
                #p = open(new_file,"w")
                if os.path.exists(new_file):
                    print "This file does exist"
                else:
                    open(new_file, 'w')
                    with open(new_file, 'w') as f:
                        f.close()
                    print "Your file created successfully"

            elif help_input == 0:
                new_file = raw_input("Please write the name of the file that you want to create: ")
                if os.path.exists(new_file):
                    print "This file does exist"
                else:
                   open(new_file, 'w')
                   with open(new_file, 'w') as f:
                       f.close()
                   print "Your file created successfully"
            else:
                print "Please select 0 or 1"

        elif choice == 2:
                help_input = input("If you do not know how to delete please enter number 1 and if you know that please enter number 0: ")
                if help_input == 1:
                    print "To remove a file please use os.remove() built-function. If the file you want to remove is in a different place than your current working directory you should write in detail.For instance /Users/Username/Documents"
                    input1 = raw_input("If you want to continue, please press enter .. ")
                    the_file = raw_input("Please enter the file name that you want to delete: ")
                    if os.path.exists(the_file):
                        os.remove(the_file)
                    else:
                        print "This file does not exist"

                elif help_input == 0:
                    the_file = raw_input("Please enter the file name that you want to delete: ")
                    if os.path.exists(the_file):
                        os.remove(the_file)
                        print ("Your file deleted successfully")
                    else:
                        print "This file does not exist"
                else:
                  print "Please select 0 or 1"
                return("None")

        elif choice == 3:
            help_input = input("If you do not know how to create a file please enter number 1 and if you know that please enter number 0: ")
            if help_input == 1:
                print "To rename a file you should use rename(oldFile, newFile), which takes two inputs built-function. First you should write the file that you want to rename, after that you should write new name of file /n If your file is not in your current working directory please write like; /Users/Documents/file"
                input1 = raw_input("If you want to continue, please press enter .. ")
                the_file1 = raw_input("Please enter the file name that you want to rename: ")
                the_file2 = raw_input("Please enter the new file name: ")
                if os.path.exists(the_file1):
                    os.rename(the_file1, the_file2)
                    print "Name of the new file is %s" %(the_file2)
                else:
                    print "There is no such file in the path"
            elif help_input == 0:
                the_file1 = raw_input("Please enter the file name that you want to rename: ")
                the_file2 = raw_input("Please enter the new file name: ")
                if os.path.exists(the_file1):
                    os.rename(the_file1, the_file2)
                    print "Name of the new file is %s" %(the_file2)
                else:
                    print "There is no such file in the path"
            else:
                print "Please select 0 or 1"

        elif choice == 4:
             help_input = input("If you do not know how to write copying file location press 1 and if you know how to write copying file location press 0:")
             if help_input == 1:
              print("You should write the detailed current directories of both copied and current or new directory .For example, /Users/Perus/Desktop/peri.c is the filename you want to copy and Users/Perus/Documents is the current or new directory.")
              the_file3 = raw_input("Please enter the file name that you want to copy ")
              m = raw_input("Please enter the location you want to copy")
              try:
                 shutil.copy2(the_file3,m)
                 print "Your file copied successfully"
              except:
                  print("The address or file cannot find")
             elif help_input == 0:
              the_file3 = raw_input("Please enter the file name that you want to copy ")
              m = raw_input("Please enter the location you want to copy")
              try:
                 shutil.copy2(the_file3,m)
              except:
                 print("The address or file cannot find")
             else:
                print "Please select 0 or 1"

        elif choice == 5:
            help_input = input("If you do not know how to write location press 1 and if you know how to write location press 0:")
            if help_input == 1:
               print("You should write the detailed current directories of both file and new directory .For example, /Users/Perus/Desktop/peri.c is the filename you want to move and Users/Perus/Documents is the new directory.")
               print("To continue press enter...")
               the_file4 = raw_input("Please enter the file name that you want to move from one directory to another:")
               new_dir = raw_input("Please enter the new location:")
               try:
                shutil.move(the_file4,new_dir)
                print("The file moved successfully")
               except:
                   print ("The address cannot find")

            elif help_input == 0:
               the_file4 = raw_input("Please enter the file name that you want to move from one directory to another:")
               new_dir = raw_input("Please enter the new location:")
               try:
                shutil.move(the_file4,new_dir)
                print("The file moved successfully")
               except:
                   print ("The address cannot find")
            else:
                print "Please select 0 or 1"

        elif choice == 6:
            chs = input("\nTo do modifications within the file choose from the list down: \n 1)Append a txt to the end of the file \n 2)Insert a txt in a specific position \n 3)Remove all txt in a file \n 4)Show the content of the file \n Choose a number: ")
            if chs == 1:
                help = input("Press 1 for any help to understand what this step is for or press 0 if you do not.. ")
                if help == 1:
                    print "This step helps you to add any string you want to the end of the txt that you already have in your file.."
                    con = raw_input("press enter to continue the process.. ")
                    input2 = raw_input("Choose the file you want to modify.. ")
                    if os.path.exists(input2):
                        input3 = raw_input("what you want to be added to that file.. ")
                        with open(input2,'a') as f: f.write(input3)
                        f.close()
                    else:
                        print "This file does not exist"
                        #with open('test1','rb') as f: print "Recent modification you did: " + f.read()
                elif help == 0:
                    input2 = raw_input("Choose the file you want to modify.. ")
                    if os.path.exists(input2):
                        input3 = raw_input("What you want to be added to that file.. ")
                        with open(input2,'a') as f: f.write(input3)
                        f.close()
                    else:
                        print "This file does not exist"
                else:
                  print "Please select 0 or 1"

            elif chs == 2:
                help = input("Press 1 for any help in doing this step or press 0 if you do not.. ")
                if help == 1:
                    print "This function help you to insert anything you want at a specific index you want."
                    con = raw_input("Press enter to continue the process please.. ")
                    File_name = raw_input("Choose the file you want to insert a txt to..")
                    if os.path.exists(File_name):
                        input3 = raw_input("What you want to be added to your file.. ")
                        input4 = raw_input("Where you want you txt to be added: ")
                        if input4 == int:
                         with open(File_name, 'r') as f:
                            lines = f.readlines()
                            a = lines[0].split()
                            a.insert(input4, input3)
                            b = ' '.join(a)
                            with open(File_name, 'w') as ff:
                                ff.write(b)
                                ff.close()
                        else:
                              print "Please enter an integer"
                              raw_input("Please press enter to continue")
                              return print_pofm()


                    else:
                        print "This file does not exist"

                elif help == 0:
                    File_name = raw_input("Choose the file you want to insert a txt to..")
                    if os.path.exists(File_name):
                        input3 = raw_input("What you want to be added to your file.. ")
                        input4 = raw_input("Where you want you txt to be added: ")

                        if input4 == int :
                         with open(File_name, 'r+') as f:
                            lines = f.readlines()
                            a = lines[0].split()
                            a.insert(input4, input3)
                            b = ' '.join(a)
                         with open(File_name, 'w') as ff:
                            ff.write(b)
                            ff.close()
                        else:
                            print "Please enter an integer"
                            raw_input("Please press enter to continue")
                            return print_pofm()

                    else:
                        print "This file does not exist"
                else:
                  print "Please select 0 or 1"

            elif chs == 3:
                help = input("Press 1 for any help in doing this step or press 0 if you do not.. ")
                if help == 1:
                    print "This step helps you to remove all txt input from the file.."
                    con = raw_input("press enter to continue the process please.. ")
                    File_name = raw_input("Choose the file you want to remove a txt from..")
                    if os.path.exists(File_name):
                        with open(File_name, 'w') as f:
                            f.close()
                            pass
                    else:
                        print "This file does not exist"
                elif help == 0:
                    File_name = raw_input("Choose the file you want to remove a txt from..")
                    if os.path.exists(File_name):
                        with open(File_name, 'w') as f:
                            f.close()
                            pass
                    else:
                        print "This file does not exist"
                else:
                  print "Please select 0 or 1"

            elif chs == 4:
                help = input("Press 1 for any help in doing this step or press 0 if you do not.. ")
                if help == 1:
                    print ("Please choose the file name that you want to shown down.If you choose a file from other working directory from your current one, please enter full name of directory. For instance Users/Username/Desktop ")
                    input1 = raw_input("Please choose the file you want to be shown down: ")
                    input2 = raw_input("Please enter how many lines you want to be in a single page: ")
                    if input2 == int :
                     input3 = raw_input("Please press enter to complete with other pages:\n \n  ")
                     a = open(input1, 'r+')
                     for i in range(input2):
                       line = a.next().strip()
                       print line
                    else:
                        print "An error occured,please enter an integer"
                        raw_input("Please press enter to continue:")
                        return print_pofm()
                elif help == 0:
                   input1 = raw_input("Please choose the file you want to be shown down: ")
                   input2 = raw_input("Please enter how many lines you want to be in a single page: ")
                   if input2 == int:
                    input3 = raw_input("Please press enter to complete with other pages:\n \n  ")
                    a = open(input1, 'r+')
                    for i in range(input2):
                      line = a.next().strip()
                      print line
                   else:
                       print "An error occured,please enter an integer"
                       raw_input("Please press enter to continue:")
                       return print_pofm()

            else:
                    print "You should only pick up numbers that corresponds to the steps in the menu which are from 1-4"

        else:
            print "You should only pick up numbers that corresponds to the steps in the menu which are from 1-6"

        for chs in range(1,6):
             y = raw_input("If you want to continue press c, if not press e:")
             if y == "c":
              return print_pofm()
             elif y== "e":
              return ("None")
             else:
               print("Please choose to continue or not")
    except:
        print "There is something went wrong"



print_pofm()







