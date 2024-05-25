import gspread


#Will get the last row in the worksheet
#credentialsfile.json
def next_available_row(worksheet,i):
    str_list = list(filter(None, worksheet.col_values(i)))
    return int(len(str_list)+1)

try:
    credentials = input("Enter the path of your Credentials File: ")
    sa = gspread.service_account(filename=credentials)
except:
    print("Failed opening the file")
    exit(1)

try:
    batchArchive = sa.open("Batch archive")
    batchArchiveWorkSheetName = str(input("Enter the sheet of batch archive name please: "))
    batchArchiveWorkSheet = batchArchive.worksheet(batchArchiveWorkSheetName)
    isValid = False
    while(not(isValid)):
        try:
            nextrow= int(input("Enter the next row: "))
            if(nextrow<0):
                print("this number is negative")
            else:
                isValid= True
        except ValueError:
            print("The number you entered is not an int") 
       

except gspread.exceptions.SpreadsheetNotFound:
    print("Could not open the Batch archive")
    exit(1)
except gspread.exceptions.WorksheetNotFound:
    print("WorkSheet int Batch Archive was not found")
    exit(1)
except Exception as e:
    print(f"Different error occured {e}")


try:
    isValid= False
    while(not(isValid)):
        try:
            numberOfSpreadSheets= int(input("Enter the number of SpreadSheets you have: "))
            if(numberOfSpreadSheets<0):
                print("The number has to be postive")
            else:
                isValid =True
        except ValueError:
            print("The number you entered is not an int")
        
    i = 0
    
    listOfInput = list()
    while(i<numberOfSpreadSheets):    
        spreadSheetName = str(input("Enter the SpreadSheetName: "))
        spreadSheet = sa.open(spreadSheetName)
        workSheet = spreadSheet.worksheet("Batch archieve section")
        nextAvailableRow = next_available_row(worksheet=workSheet, i= 1)
        listOfInput.append(workSheet.get(f"L2:U{nextAvailableRow}"))   
        i+=1
    
    dataFile = open("DATA.txt", "a")
    dataFile.write(str(listOfInput))
    dataFile.close()
    result = []
    for x in listOfInput:
        for y in x:
            result.append(y)
            
    
    batchArchiveWorkSheet.update(f'B{nextrow}:K{nextrow+len(result)-1}',result, raw=False)
    
    print("Done!")
    
    
except gspread.exceptions.SpreadsheetNotFound:
    print("Could not open the spreadsheet")
    exit(1)
except gspread.exceptions.WorksheetNotFound:
    print("WorkSheet was not found")
    exit(1)
except Exception as e:
    print(f"Different error occured {e}")



