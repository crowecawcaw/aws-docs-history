This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Location messages

The **msgtype** for all location type messages is 8000. This message is
sent when a user sends their location in a conversation. The location will contain the user's
latitude and longitude.

## One-to-one messages

The following shows the format of a location type message in 1:1 conversations:

```

     {
     "location":{
     "latitude":45.75017899435506,
     "longitude":-74.99449803034105
     },
     "message_id":"1f88fdc08bec11ea81b689d23fa72c7b",
     "msg_ts":"1588365684.583407",
     "msgtype":8000,
     "receiver":"user003",
     "sender":"user100",
     "sender_type": "normal",
     "time": "7/11/23 5:33 PM",
     "time_iso": "2023-07-11 17:33:24.394",
     "ttl": "7/10/24 5:33 PM",
     "vgroupid":"4ebf561eb2214c4e6f924d09e37bf80b6f9b85cb96b72badb03753d9ed26f7f4"
     }

```

## Group and Room conversation

messages

The following shows the format of location type message in group or room conversation
conversations:

```

     {
     "location":{
     "latitude":45.75017899435506,
     "longitude":-74.99449803034105
     },
     "message_id":"1f88fdc08bec11ea81b689d23fa72c7b",
     "msg_ts":"1588365684.583407",
     "msgtype":8000,
     "sender":"user100",
     "sender_type": "normal",
     "time": "7/11/23 5:33 PM",
     "time_iso": "2023-07-11 17:33:24.394",
     "ttl": "7/10/24 5:33 PM",
     "vgroupid":"Sebf561eb2214c4e6f924d09e37bf80b6f9b85cb96b72badb03753d9ed26f7f4"
     }

```
