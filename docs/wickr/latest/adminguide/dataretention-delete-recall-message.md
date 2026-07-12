This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Delete or recall message

The **isrecall** field shows whether the message was recalled
(visible to all participants) or only deleted locally.

```
{
  "control": {
    "isrecall": true,
    "msgid": "4ab537d0f85d11e88c2225680208f9ff",
    "msgtype": 4011
  },
  "message_id": "bea7ad10f89811e8822887c76561d99d",
  "msg_ts": "1544019555.000000",
  "msgtype": 4011,
  "sender": "user002",
  "sender_type": "normal",
  "time": "12/5/18 2:59 PM",
  "time_iso": "2018-12-05 14:59:15.000",
  "vgroupid": "3f13df0d8f267812d7e743a518fcfb6dacf6fd0824e16a83a4d2a06d32cf8d9c"
}
```
