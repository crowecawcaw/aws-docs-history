This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Location messages

There are two types of location messages.

**Static location share**

```
{
  "location": {
    "latitude": 40.75017899435506,
    "longitude": -74.99449803034105
  },
  "message_id": "1f88fdc08bec11ea81b689d23fa72c7b",
  "msg_ts": "1588365684.000000",
  "msgtype": 8000,
  "receiver": "user001",
  "sender": "user002",
  "sender_type": "normal",
  "time": "5/1/20 1:41 PM",
  "time_iso": "2020-05-01 13:41:24.000",
  "vgroupid": "4ebf561eb2214c4e6f924d09e37bf80b6f9b85cb96b72badb03753d9ed26f7f4"
}
```

**Share location continuously**

The following example is when a user shares their location for a period of time. The
**edit** section shows the updated coordinates.

```
{
  "edit": {
    "type": "location",
    "shareexpiriation": "1780509208",
    "latitude": 40.755629888216255,
    "longitude": -73.9861171188826
  },
  "message_id": "2a99fdc08bec11ea81b689d23fa72c7b",
  "msg_ts": "1588365700.000000",
  "msgtype": 9000,
  "receiver": "user001",
  "sender": "user002",
  "sender_type": "normal",
  "time": "5/1/20 1:41 PM",
  "time_iso": "2020-05-01 13:41:40.000",
  "vgroupid": "4ebf561eb2214c4e6f924d09e37bf80b6f9b85cb96b72badb03753d9ed26f7f4"
}
```

###### Note

When **shareexpiriation** is set to "-1", the user has stopped
sharing their location. The field name **shareexpiriation** is
spelled as shown in the output.
