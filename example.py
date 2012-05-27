''' Example Displaying usage of TheAward. It submits 1.5 hrs of activity on Tuesdays and Thursdays and 1 hr on Saturday for the amount of weeks specified with weeks. '''
from theaward import TheAward

a = TheAward('Sess_id', 'Act_id')
hours = "1.50"
day = 'THU'
activity_date = datetime.date(2012, 4, 31)
addition = 2
weeks = 10
for x in range(0,weeks*3):
    post_to_server(hours, activity_date.strftime("%d/%m/%Y"))
    activity_date += datetime.timedelta(days=addition)

    if day == 'SAT':
        hours = "1.50"
        addition = 2
        day = 'TUE'

    elif day == 'TUE':
        hours = "1.50"
        addition = 2
        day = 'THU'

    else:
        hours = "1.00"
        addition = 3
        day = "SAT"
