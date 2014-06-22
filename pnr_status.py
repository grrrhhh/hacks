from bs4 import BeautifulSoup
import urllib
import urllib2


PNR_STATUS_ENQUIRY_URL = "http://www.indianrail.gov.in/cgi_bin/inet_pnstat_cgi_10521.cgi" #this keeps changing.
#its static. Seems like every time, they do a bug fix, they screw up the endpoint.
#http://www.indianrail.gov.in/cgi_bin/inet_pnrstat_cgi.cgi

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)' + \
             'Ubuntu Chromium/32.0.1700.102 Chrome/32.0.1700.102 Safari/537.36'
headers = { 'Referer': 'http://www.indianrail.gov.in/pnr_Enq.html',
            'User-Agent' : user_agent }

form_data = {}
form_data = {
    'lccp_cap_val' : 95237,
    'lccp_capinp_val' : 95237,
    'submit' : 'Wait For PNR Enquiry!'
}

form_data['lccp_pnrno1'] = 1234567899 # 10-digit PNR number

form_data = urllib.urlencode(form_data)
req = urllib2.Request(PNR_STATUS_ENQUIRY_URL, form_data, headers) # (url, data, headers)
response = urllib2.urlopen(req)
response = response.read()

indianRailwayMessySoup = BeautifulSoup(response)
print "-------------"
print indianRailwayMessySoup.find('h2').get_text()
print "-------------"
print indianRailwayMessySoup.find('h3').get_text()
