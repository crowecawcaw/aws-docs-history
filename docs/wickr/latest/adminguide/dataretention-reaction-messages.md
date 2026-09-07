

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Reaction messages
<a name="dataretention-reaction-messages"></a>

When a user adds or removes an emoji reaction on a message, Wickr generates a reaction edit message. The **reactAdded** field indicates whether the reaction was added (true) or removed (false).

```
{
  "edit": {
    "originalmessageid": "73117f005f6811f19b07b1408476c2f4",
    "reactAdded": true,
    "reaction": "(thumbs up)",
    "type": "reaction"
  },
  "message_id": "8f9a0b1c2d3e4f5a6b7c8d9e",
  "msg_ts": "1780503777.000000",
  "msgtype": 9100,
  "sender": "user001@example.com",
  "sender_type": "normal",
  "time": "6/3/26 4:22 PM",
  "time_iso": "2026-06-03 16:22:57.000",
  "vgroupid": "S3f8a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9"
}
```