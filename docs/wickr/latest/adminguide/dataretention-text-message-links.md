This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Text messages with links

If you send a text message that contains links, and the security group settings have
the "Send Link Preview" option enabled, the text message contains a list of the URLs for
those links.

```
{
  "links": [
    {
      "url": "https://weather.com/weather/today"
    }
  ],
  "message": "Test message with a link: https://weather.com/weather/today",
  "message_id": "b7e4f2a032fa11ee9a74053bb1017859",
  "msg_ts": "1691176397.000000",
  "msgtype": 1000,
  "receiver": "user001@example.com",
  "sender": "user002@example.com",
  "sender_type": "normal",
  "time": "8/4/23 7:13 PM",
  "time_iso": "2023-08-04 19:13:17.000",
  "vgroupid": "7ad65d17b945d7672190ecab6902fdd06eff162b91adfcda23df3b2ff95875e8"
}
```
