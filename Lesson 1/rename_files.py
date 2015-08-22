import os

def rename_files () :
    #(1) get file names from folder
    file_list = os.listdir("/Users/Dcube/Google Drive/School/UDACITY/Programming_foundations_with_python/prank")
    print (file_list)
    saved_path = os.getcwd()
    print ("Saved Working Directory is: " + saved_path)
    os.chdir("/Users/Dcube/Google Drive/School/UDACITY/Programming_foundations_with_python/prank")
    new_path = os.getcwd()
    print ("Current working Directory is: " + new_path)
 

    # (2) for each file, rename filename
    for file_name in file_list:
          os.rename(file_name, file_name.translate(None, "0123456789"))                 
    os.chdir(saved_path)              
rename_files ()
