

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Link previews
<a name="dataretention-link-previews"></a>

When a user shares a link and has "Link Previews" enabled, Wickr generates an **edit** message with the preview content.

```
{
  "edit": {
    "originalmessageid": "11457fa08da211ea881baffab0b42745",
    "text": "https://example.com",
    "type": "text"
  },
  "message_id": "1163e5b08da211eab775a5032a0322ca",
  "msg_ts": "1588553780.000000",
  "msgtype": 9000,
  "sender": "user001",
  "sender_type": "normal",
  "time": "5/3/20 5:56 PM",
  "time_iso": "2020-05-03 17:56:20.000",
  "vgroupid": "S243f2ec645d3961bdd531f51f3244205d292b8d0fbd41802827746271d31d41"
}
```