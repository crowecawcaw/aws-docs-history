This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# User left room

Wickr generates this message when a user voluntarily leaves a room. The sender is the
user who left.

```
{
  "control": {
    "deletedusers": ["user003"],
    "msgtype": 4003
  },
  "message_id": "4d5e6f7a8b9c0d1e2f3a4b5c",
  "msg_ts": "1780503700.000000",
  "msgtype": 4003,
  "sender": "user003",
  "sender_type": "normal",
  "time": "6/3/26 4:21 PM",
  "time_iso": "2026-06-03 16:21:40.000",
  "vgroupid": "S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}
```
