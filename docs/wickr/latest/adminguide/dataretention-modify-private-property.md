This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Modify private property

This message identifies when a conversation is pinned or unpinned. The
**pinned** value is true when the conversation is pinned, and false
when it is being unpinned.

```
{
  "control": {
    "pinned": true,
    "msgtype": 4014
  },
  "message_id": "c5bce5e0ca2f11e78946112c51861afa",
  "msg_ts": "1510769218.000000",
  "msgtype": 4014,
  "sender": "user003",
  "sender_type": "normal",
  "time": "11/15/17 5:06 PM",
  "time_iso": "2017-11-15 17:06:58.000",
  "vgroupid": "Sb0e9297f2208dc86b63b288df8c226882e1052b65022edb9edb9ecf6e77db08"
}
```
