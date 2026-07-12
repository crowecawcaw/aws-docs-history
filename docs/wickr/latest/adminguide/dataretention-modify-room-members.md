This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Modify room members message

The **addedusers** and **deletedusers** arrays show
who was added and removed.

**Member added**

```
{
  "control": {
    "addedusers": ["user003"],
    "msgtype": 4002
  },
  "message_id": "d34058a0f89711e88760d7c8037ea946",
  "msg_ts": "1544019160.000000",
  "msgtype": 4002,
  "sender": "user002",
  "sender_type": "normal",
  "time": "12/5/18 2:52 PM",
  "time_iso": "2018-12-05 14:52:40.000",
  "vgroupid": "S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}
```

**Member removed**

```
{
  "control": {
    "deletedusers": ["user003"],
    "msgtype": 4002
  },
  "message_id": "e5f1a9c0f89711e88760d7c8037ea946",
  "msg_ts": "1544019175.000000",
  "msgtype": 4002,
  "sender": "user002",
  "sender_type": "normal",
  "time": "12/5/18 2:52 PM",
  "time_iso": "2018-12-05 14:52:55.000",
  "vgroupid": "S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}
```
