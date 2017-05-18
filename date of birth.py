print('this program prints the day of ur birth')
#NAME:TAYEBWA.LINARD
#REG.NO.16/U/11855/PS
#STUDENTNO:216012445
import calendar
dy=int(input('please insert the date you were born:'))
mth=int(input('please insert the month you were born:'))
yr=int(input(' please enter your year of birth:'))
lin=calendar.weekday(yr,mth,dy)
d={0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
print('WOW!,Your day of birth is',d[lin])

