import pandas as pd
import html5lib
from openpyxl import load_workbook
dfs=pd.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')

currency = dfs[0]
currency=currency.ix[:,0:5]

currency.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出'] #[u'欄位名稱']將欄位設成unicode
#清除幣別欄重複字元
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)') #幣別值有重複字 利用正規式取英文代號
#currency.to_excel(r'C:\Users\User\Desktop\testExcel.xlsx')
#-----------------------------------


#將爬下來的資料存成excel檔
try:
    currency.drop([0, 18])
    writer = pd.ExcelWriter(r'C:\Users\User\Desktop\writeInExcel\currency.xlsx', engine = 'openpyxl')
    writer.book = load_workbook(r'C:\Users\User\Desktop\writeInExcel\currency.xlsx')
    currency.to_excel(writer, sheet_name = 'Sheet 2')
    writer.save()
    writer.close()
except Exception as e:
    print(e)
    currency.drop([0, 18])
    writer = pd.ExcelWriter(r'C:\Users\User\Desktop\writeInExcel\currency.xlsx', engine = 'openpyxl')
    currency.to_excel(writer, sheet_name = 'Sheet 1')
    writer.save()
    writer.close()