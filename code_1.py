import os
import shutil
from_dir = "C:/Users/Public/Documents/python/Projects/P102/Downloads"
to_dir = "C:/Users/Public/Documents/python/Projects/P102/Document_Files"
list_of_files = os.listdir(from_dir)
print("List of files in the source path:")
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension=="":
        continue
    
    if extension.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"document_Files"
        path3=to_dir+"/"+"document_Files"+"/"+file_name
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:    
            os.makedirs(path2)
            shutil.move(path1, path3)