TheAward
=========

Class to Post Data to http://orb.theaward.com.au/ , a website for submitting Duke Of Edinburgh Award logs online (the Online Record Book). The site isn't really made for entering data so after ten minutes of slaving away, I hacked together this script to enter my logs programatically, as seen in the example. 

#Usage: 
TheAward(sessionid, activityid)

Where SessionID is found at the GET key 'S' in all DoE pages and the activity is found at the GET key 'activity' on the activity page.

IE: if the page for my Physical Rec/Fitness activity is:

http://orb.theaward.com.au/participant/award/add-record.asp?S=ABC123ABC123&E=xxx-xxx&activity=ABC-123-ABC-123,

Then I should call:

t = TheAward('ABC123ABC123', 'ABC-123-ABC-123')

Then, call TheAward.post_to_server(hours, activity_date)

Where activity_date is in the python date format: "%d/%m/%Y" (dd/mm/yyyy)
and Hours is a string with two decimal points (ie: for 1 and a half hours, hours="1.50")

For an example of usage, see example.py

#Note on Save Fail:

When you read the value of h.getresponse, you may notice that the service returns a response saying that the setting of value 'x' failed. This is the case on the actual service itself. However, the value stores just fine. Obviously, some misconfiguration on the uniDap server that ORB uses.
