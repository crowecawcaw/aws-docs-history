This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Edit reaction messages

###### Note

The edit messages are only seen by the compliance bot installations (Wickr Enterprise)
or by Data Retention bot (AWS Wickr).

The edit reaction messages are used to modify the reactions associated with a message. The
message layout is similar to the Edit message layout, but the **msgtype** value
is 9100. The **edit** object contains the following fields:

| Field Name        | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| originalmessageid | The message ID of the message that the reaction is associated                |
| reactAdded        | This is a boolean that is true if the reaction is added and false if removed |
| reaction          | This is the reaction to enable or disable                                    |
| type              | This is always the value **reaction**                                        |

The "sender" field will identify who is adding or removing a reaction. The client should
display the reaction and which users were associated with that reaction.

The following is a sample of adding a reaction to a message in 1:1 conversation:

```

{
    "edit":{
      "originalmessageid":"a1c00830ad3911ebaa04213b1ad0a9b2",
      "reactAdded":true,
      "reaction":"👍",
      "type":"reaction"
    },
    "message_id":"b6d3d1b0add011ebb00f1b2dbb810704",
    "msg_ts":"1620239749.707944",
    "msgtype":9100,
    "receiver":"bn0523_bcast_bot",
    "sender":"bnuser01@userworld.com",
    "sender_type": "normal",
    "time": "7/11/23 5:35 PM",
    "time_iso": "2023-07-11 17:35:41.411",
    "ttl": "7/10/24 5:35 PM",
    "vgroupid":"4b32d7c8c6c37cc9e9506e9ed98ce37f0a96e1e45fcd4ca6f6d00c9d435d82e3"
}

```

The following is a sample of removing a reaction to a message:

```

{
    "edit":{
      "originalmessageid":"a1c00830ad3911ebaa04213b1ad0a9b2",
      "reactAdded":false,
      "reaction":"👍",
      "type":"reaction"
    },
    "message_id":"68596ac0add211ebb00f1b2dbb810704",
    "msg_ts":"1620240477.36364",
    "msgtype":9100,
    "receiver":"bn0523_bcast_bot",
    "sender":"bnuser01@userworld.com",
    "sender_type": "normal",
    "time": "7/11/23 5:35 PM",
    "time_iso": "2023-07-11 17:35:41.411",
    "ttl": "7/10/24 5:35 PM",
    "vgroupid":"4b32d7c8c6c37cc9e9506e9ed98ce37f0a96e1e45fcd4ca6f6d00c9d435d82e3"
}

```
