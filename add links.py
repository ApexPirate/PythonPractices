#Python 檔案讀寫

file = open(r"G:\Desktop\tw.txt", 'r')  #開檔案    #r 唯讀
filenew = open(r"G:\Desktop\twNew.txt", 'w')    #w 清除檔案內容並重新寫入，若無指定的檔案，自動新建一個

"""contents = file.readlines()  #分行讀出存至list
for content in contents:
    print(content)"""

for line in file:   #也是每行讀取
    filenew.write("<a href=\"" + line.strip() + "\">" + line.strip() + "</a><br>\n")    #.strip() 清除字串前後空白

file.close()    #關檔案
filenew.close()