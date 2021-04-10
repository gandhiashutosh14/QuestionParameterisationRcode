# from azure.storage.blob import BlockBlobService
# import pandas as pd
# import tables
#
# STORAGEACCOUNTNAME= devintrods5822393039
# STORAGEACCOUNTKEY= /+zVpuxkr4VxmaOzF0AUucvOXYMk8E4SHcSY2FaZn4Hpa3QPg4GT4TKrZpaa/ofFpCjvjEbEPi7Wn9qyyl4nJA==
# LOCALFILENAME= C:\Users\DN Gandhi\Desktop\New folder
# CONTAINERNAME= testrinputcsv
# BLOBNAME= ques_input_file.csv
#
# #download from blob
# t1=time.time()
# blob_service=BlockBlobService(account_name=STORAGEACCOUNTNAME,account_key=STORAGEACCOUNTKEY)
# blob_service.get_blob_to_path(CONTAINERNAME,BLOBNAME,LOCALFILENAME)
# t2=time.time()
# print(("It takes %s seconds to download "+blobname) % (t2 - t1))
#
# # LOCALFILE is the file path
# dataframe_blobdata = pd.read_csv(LOCALFILENAME)
import rpy2.robjects as robjects
r = robjects.r
r.source(r'C:\Users\DN Gandhi\Downloads\IRT\IRT\Code\ques_param.R') 
