import os


path = ''

os.chdir(path)

print(os.getcwd())

listofcontents = []
i=0
for file in os.listdir():
    
    print("First file loop " + str(i))
       
    
    with open(file,"r") as reader:
        data = reader.readlines()
        
        cleanContent = [ d.replace("content_","content") for d in data ]           
        print("Content Replace Success")
            
        
        with open(file, "w") as file_writer:
            file_writer.writelines(cleanContent) 
            print("File Written Success")
    
    i = i + 1




   
        
            
         
      
      
    


 

  
