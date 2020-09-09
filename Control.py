import CYDdatahandler
import CYDdonwload

Date1 = "2020-08-31"
Date2 = "2020-09-06"

date = CYDdonwload.DateGenerator(Date1, Date2)
if 1 == 2:
    CYDdonwload.DownCountryData(date)
    CYDdonwload.DownAttackData(date)
    CYDdonwload.DownForeignData(date)

else:
    CYDdatahandler.UpdateExcel(date)
