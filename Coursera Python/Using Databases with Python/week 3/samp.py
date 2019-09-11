import glob2
import datetime

filenames=glob2.glob("*.txt")
print(filenames)
file=open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w')
for filename in filenames:
    f=open(filename)
    file.write(f.read()+"\n")