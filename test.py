
#!/usr/bin/python
import httplib, urllib
import json
deviceId = "DpwJPYEJ"
deviceKey = "1mOUe8ZVclT0CimZ"
def post_to_mcs(payload):  
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds
	conn.request("GET", "/mcs/v2/devices/" + deviceId + "/datapoints/LED_Control/datapoints", 
 headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close() 


