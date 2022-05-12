import os


os.chdir('E:\Blender\Blend My NFT\Export\Blend_My_NFTs Output\Complete_Collection\Cardano_metaData')

print(os.getcwd())

listofcontents = []
i=0
for file in os.listdir():
    
    print("First file loop " + str(i))
       
    
    with open(file,"r") as reader:
        data = reader.readlines()
        
        cleanContent = [ d.replace("HouseLuxury_","HouseLuxury") for d in data ]           
        print("Content Replace Success")
            
        
        with open(file, "w") as file_writer:
            file_writer.writelines(cleanContent) 
            print("File Written Success")
    
    i = i + 1




   
        
            
         
      
      
    


 

  
