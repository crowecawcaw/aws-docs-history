This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Text message

The msgtype for all text-based messages is 1000. Text-based messages can be sent either
directly to the Wickr bot or in secure Room/Group conversations.

## One-to-one messages

The following shows a one-to-one text message format:

```

     {
     "message_id":"3960e020ca4211e799802f2894564caa",
     "message":"This is a typical 1:1 message",
     "msg_ts":"1510777143.738976",
     "msgtype":1000,
     "receiver":"user001",
     "sender_type": "normal",
     "sender":"user003",
     "time": "7/11/23 5:19 PM",
     "time_iso": "2023-07-11 17:19:58.781",
     "ttl": "7/10/24 5:19 PM",
     "vgroupid":"fb6e21630c05fde50ae39113c3626018712cf2c374b4a80eba4d28ced9419c07"
     }

```

## Text messages with links

If you send a text message that contains links, and the security group settings have the
"Send Link Preview" option enabled, the text message will contain a list of the URLs for those
links:

```

     {
     "links":[
     {
     "url":"https://testdaily.com/image/test-laughing/"
     }
     ],
     "message":"Check out this link https://testdaily.com/image/test-laughing/",
     "message_id":"fb7d7d20b25d11eb9a2d77f565346d8b",
     "msg_ts":"1620740228.594362",
     "msgtype":1000,
     "receiver":"bnuser02@userworld.com",
     "sender":"bnuser01@userworld.com",
     "time":"5/11/21 1:37 PM",
     "ttl":"6/10/21 1:37 PM",
     "vgroupid":"2c0ae523d2b1af3e43af80b5fafec05548fd2e33fee4c021c66033c6416bb6bb"
     }

```

## Group and Room conversation messages

The following shows a normal group or secure room conversation text message format:

```

     {
     "message_id":"3960e020ca4211e799802f2894564caa",
     "message":"This is a typical 1:1 message",
     "msg_ts":"1510777143.738976",
     "msgtype":1000,
     "sender_type": "normal",
     "sender":"user003",
     "time": "7/11/23 5:19 PM",
     "time_iso": "2023-07-11 17:19:58.781",
     "ttl": "7/10/24 5:19 PM",
     "vgroupid":"Sa6783e427e164d37f2e8177874ee192523e6cc9520416bf96850ca01730bf07"
     }

```

###### Note

In some cases, the Wickr IO client does not track the list of clients associated with
group conversations, so the list of destination clients will not be included. You can use the
supplied Wickr IO APIs to retrieve the members associated with a secure room or group
conversation vGroupID.
