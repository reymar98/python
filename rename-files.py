# Pythono3 code to rename multiple 
# files in a directory or folder 
# G:\portable\Python\python.exe G:\hold\eclipse\links\python\10rename.py

# importing os module 
import os 
import datetime

# Function to rename multiple files 
def main(): 

	dir99 = "C:\\Users\\rdm99\\Documents\\zzdelete\\day3"

	dt10 = datetime.date.today()
	dt11 = dt10.strftime("%d%m%Y")
	ti10 = datetime.time.today()

	for count, filename in enumerate(os.listdir(dir99)): 

		z10 = filename.endswith(".pdf")

		if (z10){
			dt20 = datetime.datetime.now()
			dt21 = dt20.strftime("%X")
			dst = dt11 + dt21 + str(count) + ".pdf"
		 	src = filename 
			dst = dst.replace('.pdf','.jpg')
			os.rename(dir99 + "\\"+  src, dir99 + "\\" + dst) 
		}
		

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
