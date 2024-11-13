from datetime import datetime

# Дата для газеты "The Moscow Times"
moscow_times_date = "Wednesday, October 2, 2002"
moscow_times_format = "%A, %B %d, %Y" 
moscow_times_datetime = datetime.strptime(moscow_times_date, moscow_times_format)

# Дата для газеты "The Guardian"
guardian_date = "Friday, 11.10.13"
guardian_format = "%A, %d.%m.%y" 
guardian_datetime = datetime.strptime(guardian_date, guardian_format)

# Дата для газеты "Daily News"
daily_news_date = "Thursday, 18 August 1977"
daily_news_format = "%A, %d %B %Y"  
daily_news_datetime = datetime.strptime(daily_news_date, daily_news_format)

print("The Moscow Times datetime:", moscow_times_datetime)
print("The Guardian datetime:", guardian_datetime)
print("Daily News datetime:", daily_news_datetime)