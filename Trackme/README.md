# --Features
1- File Tracking Using watchdog (complex)
2- File Moving
3- File Deleting
4- File Renaming
# --Memory Optimization
1- Using file system watcher APIs instead of polling (e.g. inotify on Linux)
2- Using text-based icons to reduce GUI overhead

# --Guide: 
track option: just select a directory you want to track then open dev.log (the file will be created after choosing directory) and all the changes that will happen in that directory will be logged there.

delete option: select the file you want to delete (ex:file.txt) and it will be deleted directly after choosing it.

move option: select the current path of the file (ex:C:\Users\someone\file.txt) then choose the directory you want to move the file to (ex: C:\Users\another\) and done.

rename option: select the directory of the file you want to rename (ex:C:\Users\directory\) then the full path (ex:C:\Users\directory\file.txt) and finally write the new name of the file with its format (ex:newfile.md).





Note for optimize reviewer: hackatime tracked this project under 2 names (Optimize-1, Trackme)
Cause: changed the folder name.

Notes for users:
1- you cannot select multiple directiories to track changes in
2- you can not choose multiple files to delete
3- click the empty button to remove unneccessary files (for example, sys32.exe).