'''
Python program for copying the contents from one file to another file.
Developed by: SRIJITH R
RegisterNumber: 21004191
'''

def copy(fname,newfile):
  with open(fname,'r')as fp:
    with open(newfile,'w')as fp1:
      data1=fp.read()
      fp1.write(data1)
fname=input("Enter an existing file: ")
newfile=input("Enter a name for new file: ")
copy(fname,newfile)