This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Text message

The following is a text message in a one-to-one (DM) conversation.

```
{
  "message": "test message",
  "message_id": "a526085032fa11ee9a74053bb1017859",
  "msg_ts": "1691176258.000000",
  "msgtype": 1000,
  "receiver": "user001@example.com",
  "sender": "user002@example.com",
  "sender_type": "normal",
  "time": "8/4/23 7:10 PM",
  "time_iso": "2023-08-04 19:10:58.000",
  "vgroupid": "7ad65d17b945d7672190ecab6902fdd06eff162b91adfcda23df3b2ff95875e8"
}
```

The following shows a text message for a secure room conversation.

###### Note

The **vgroupid** for a secure room conversation starts with the
**S** letter and begins with the **G** letter
for group conversations.

```
{
  "message": "test message in a secure room",
  "message_id": "e2c5115032fb11ee9a74053bb1017859",
  "msg_ts": "1691176791.000000",
  "msgtype": 1000,
  "sender": "user002@example.com",
  "sender_type": "normal",
  "time": "8/4/23 7:19 PM",
  "time_iso": "2023-08-04 19:19:51.000",
  "vgroupid": "S19a8782d9a0441d5e13f15b6789f00bc2f9b8231aa364a2eb3a8269dce2ac21"
}
```
