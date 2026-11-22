

This guide provides documentation for Wickr IO Integrations. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Python Bot Development

To develop Wickr IO integrations in languages other than JavaScript such as Python, you will need to set up a Web REST API Interface integration on your machine and send HTTP/HTTPS requests to it. The following examples show how to do it in Python:

## Set up your Python app
<a name="python-setup"></a>

```python
import requests
import json

URL = "http://localhost:4001/WickrIO/V1/Apps/CLIENT_API_KEY"
PARAMS = {'Accept': '*/*', 'Content-Type': 'application/json',
          'Authorization': 'Basic AUTH_KEY'}
```

## Send 1-to-1 Message
<a name="python-send-1to1-message"></a>

```python
data = {
    "message": "Welcome to AWS Wickr! This message will self-destruct eventually.",
    "users": [
        {"name": "exampleuser@wickr.com"}
    ]
}
sendMessage = requests.post(URL + "/Messages",
                            headers=PARAMS,
                            data=json.dumps(data))
print(sendMessage.content)
```

## Add Room
<a name="python-add-room"></a>

```python
data = {
    "room": {
        "title": "Security Group room for Sports in Bot Testing Network",
        "description": "Security Group room for Sports in Bot Testing Network",
        "ttl": "25536000",
        "bor": "0",
        "members": [
            {"name": "wickruser1@wickr.com"},
            {"name": "wickruser2@wickr.com"}
        ],
        "masters": [
            {"name": "wickruser1@wickr.com"}
        ]
    }
}
AddRoom = requests.post(URL + "/Rooms",
                        headers=PARAMS,
                        data=json.dumps(data))
json_data = json.loads(AddRoom.text)
room = json_data['vgroupid']
print(room)
```

## Send Room message
<a name="python-send-room-message"></a>

```python
data = {
    "message": "Welcome to AWS Wickr! This message will self-destruct eventually.",
    "vgroupid": "examplevgroupid"
}
sendMessage = requests.post(URL + "/Messages",
                            headers=PARAMS,
                            data=json.dumps(data))
print(sendMessage.content)
```

## Get Statistics
<a name="python-get-statistics"></a>

```python
getStatistics = requests.get(URL + "/Statistics",
                             headers=PARAMS)
print(getStatistics.json())
```

## Delete Statistics
<a name="python-delete-statistics"></a>

```python
deleteStatistics = requests.delete(URL + "/Statistics",
                                   headers=PARAMS)
print(deleteStatistics.content)
```

## Get Room
<a name="python-get-room"></a>

```python
payload = {
    'vgroupid': room}
getRoom = requests.get(URL + "/Rooms/{0}".format(room),
                             headers=PARAMS)
print(getRoom.json())
```

## Modify Room
<a name="python-modify-room"></a>

```python
data = {
        "title": "Modified room",
        "description": "Testing ModifyRoom command",
        "ttl": "25536000",
        "bor": "0"
}
modifyRoom = requests.post(URL + "/Rooms/{0}".format(room),
                           headers=PARAMS,
                           data=json.dumps(data))
print(modifyRoom.content)
```

## Add Group Convo
<a name="python-add-group-convo"></a>

```python
data = {
    "groupconvo": {
        "members": [
            {"name": "exampleuser@wickr.com"},
            {"name": "exampleuser02@wickr.com"}
        ]
    }
}
AddGroupConvo = requests.post(URL + "/GroupConvo",
                              headers=PARAMS,
                              data=json.dumps(data))
print(AddGroupConvo.content)
response = json.loads(AddGroupConvo.text)
print(response['vgroupid'])
groupConvo = response['vgroupid']
print(groupConvo)
```

## Get Group Convos (All)
<a name="python-get-group-convos"></a>

```python
getGroupConvos = requests.get(URL + "/GroupConvo",
                              headers=PARAMS)
print(getGroupConvos.json())
```

## Get Group Convo (One)
<a name="python-get-group-convo"></a>

```python
getGroupConvo = requests.get(URL + "/GroupConvo/{0}".format(groupConvo),
                             headers=PARAMS)
print(getGroupConvo.json())
```

## Delete Group Convo (One)
<a name="python-delete-group-convo"></a>

```python
deleteGroupConvo = requests.delete(URL + "/GroupConvo/{0}".format(groupConvo),
                                   headers=PARAMS)
print(deleteGroupConvo.content)
```

## Get Message
<a name="python-get-message"></a>

```python
getMessage = requests.get(URL + "/Messages",
                          headers=PARAMS)
print(getMessage.json())
```

## Set MsgRecvCallback
<a name="python-set-msgrecvcallback"></a>

```python
payload = {'callbackurl': 'http://localhost:8080/apps/callback'}
setMsgRecvCallback = requests.post(URL + "/MsgRecvCallback",
                                   headers=PARAMS,
                                   params=payload)
print(setMsgRecvCallback.content)
```

## Get MsgRecvCallback
<a name="python-get-msgrecvcallback"></a>

```python
getMsgRecvCallback = requests.get(URL + "/MsgRecvCallback",
                                  headers=PARAMS)
print(getMsgRecvCallback.content)
```

## Delete MsgRecvCallback
<a name="python-delete-msgrecvcallback"></a>

```python
deleteMsgRecvCallback = requests.delete(URL + "/MsgRecvCallback",
                                        headers=PARAMS)
print(deleteMsgRecvCallback.content)
```

## Complete Python Bot Example
<a name="python-bot-development-example"></a>

```python
import requests
import json
import time

URL = "http://localhost:4001/WickrIO/V1/Apps/CLIENT_API_KEY"
PARAMS = {'Accept': '*/*', 'Content-Type': 'application/json',
          'Authorization': 'Basic AUTH_KEY'}

def get_messages():
    """Get new messages from Wickr"""
    try:
        response = requests.get(URL + "/Messages", headers=PARAMS)
        return response.json()
    except Exception as e:
        print(f"Error getting messages: {e}")
        return []

def process_message(message):
    """Process a message from Wickr"""
    try:
        # Extract message content and sender
        content = message.get('message', '')
        sender = message.get('sender', '')
        
        print(f"Received message from {sender}: {content}")
        
        # Simple echo response
        if content:
            reply = {
                "message": f"You said: {content}",
                "users": [{"name": sender}]
            }
            
            response = requests.post(URL + "/Messages",
                                    headers=PARAMS,
                                    data=json.dumps(reply))
            print(f"Reply sent: {response.status_code}")
    except Exception as e:
        print(f"Error processing message: {e}")

def main():
    """Main bot loop"""
    print("Starting Python Wickr bot...")
    
    while True:
        # Get and process new messages
        messages = get_messages()
        for message in messages:
            process_message(message)
        
        # Wait before checking for new messages again
        time.sleep(5)

if __name__ == "__main__":
    main()
```