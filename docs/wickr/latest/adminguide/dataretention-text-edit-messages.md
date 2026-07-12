This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Text edit messages

When a user edits a previously sent message, the **edit** object
contains the updated text and a reference to the original message.

```
{
  "edit": {
    "originalmessageid": "84da42d05f6811f19b07b1408476c2f4",
    "text": "corrected message text",
    "type": "text"
  },
  "message_id": "5c6d7e8f9a0b1c2d3e4f5a6b",
  "msg_ts": "1780503802.000000",
  "msgtype": 9000,
  "sender": "user001@example.com",
  "sender_type": "normal",
  "time": "6/3/26 4:23 PM",
  "time_iso": "2026-06-03 16:23:22.000",
  "vgroupid": "S3f8a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9"
}
```
