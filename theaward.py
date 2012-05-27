import datetime
import urllib
import httplib

class TheAward:
''' 

Class to Post Data to http://orb.theaward.com.au/ . See Readme.txt for more information

'''
    def __init__(self, sessionid, activityid):
        self.sessionid = sessionid
        self.activity = activityid


    def make_query_string(self, hours, activity_date):
        ''' Makes the data which is sent to the server. Due to the quirky way ORB is setup, we have to retrieve the form and the GUIDs for all the rows before submitting the data of that form '''
        u = urllib.urlopen('http://orb.theaward.com.au/webservice/xml.asp?S=' + self.sessionid + '&c=newfieldrow&e=' + self.activity + '&frt=F938BE03-F5C0-49E4-BDF2-6A8D5622DB19&output=xml&rand=856')
        u = u.readlines()[0]
        query = u[:361] + ' Value="' + hours + '"' + u[361:650] + ' Value="' + activity_date + '"' + u[650:775] + ' Value=""' + u[775:]
        return query

    def post_to_server(self, hours, activity_date):
        ''' Public interface to TheAward, posts one record as indicated '''
        data = urllib.urlencode({'uniDapXML': make_query_string(hours, activity_date, activity)})
        h = httplib.HTTPConnection('orb.theaward.com.au')
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        h.request('POST', '/webservice/xml.asp?S=' + self.sessionid + '&output=xml&c=writefieldcollection&bgpmode=212&rand=651', data, headers)
        r = h.getresponse() # see readme for why this is OK despite 'Save of Value 'x' failed'
        return 1
    

