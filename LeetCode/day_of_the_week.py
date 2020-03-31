from datetime import datetime 

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.strptime(str(day) + '-' + str(month) + '-' + str(year), '%d-%m-%Y').strftime('%A')
