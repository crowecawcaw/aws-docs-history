This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Wickr control messages

Wickr control messages are used to setup and configure the Wickr group and secure room
conversations. These control messages will also be passed on to the integration software. You
can use these control messages to construct and maintain the list of users that are part of
group and secure conversations. The **control** JSON object contains the
specific control message fields, as described in this table:

| Field       | Description                                                                                                                                    |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| bor         | The burn on read time in seconds.                                                                                                              |
| changemask  | A number that is the sum of values associated with which fields are being changed by<br>the control message. Table below defines these values. |
| description | The description of the secure room conversation.                                                                                               |
| masters     | Array of Wickr IDs that are moderators for the secure room conversation. In group<br>conversations all members should be moderators.           |
| members     | Array of Wickr IDs that are members of the group or secure room conversation.                                                                  |
| title       | The title of the secure room conversation                                                                                                      |
| ttl         | The title of the secure room conversation                                                                                                      |

The `changemask` value is a number value that is created by adding the following
flag values, based on what fields are contained in the **control**
object:

| Field           | Value |
| --------------- | ----- |
| Masters field   | 1     |
| Time to live    | 2     |
| Time filed      | 4     |
| Description     | 8     |
| Meeting ID key  | 16    |
| Burn on read    | 32    |
| File vault info | 64    |

The following sections contain examples of control messages, note the values of the
`changemask` fields.

## Create room control message

The create room control message is used to create a group or secure room conversation. The
following depicts a typical create room control message:

```

{
    "control":{
        "bor":0,
        "changemask":47,
        "description":"",
        "masters":["user001", "user002"],
        "members":["user001", "user002", "user003"],
        "msgtype":4001,
        "title":"Creating a room",
        "ttl":2592000
    },
    "message_id":"be452b00f89711e883588d1e7a946847",
    "msg_ts":"1544019125.75323",
    "msgtype":4001,
    "sender":"user002",
    "sender_type": "normal",
    "time": "7/11/23 5:12 PM",
    "time_iso": "2023-07-11 17:12:45.168",
    "ttl": "7/10/24 5:12 PM",
    "vgroupid":"S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}

```

In the example above you will see the `changemask` value 47 which is equal to
the sum of the "burn on read" (32), "masters field" (1), "time to live" (2), "title field" (4)
and the "description" (8). The changemask values are used in other control messages as
well.

## Modify room members control message

The modify room member control message is used to modify the list of users associated with
a group or secure room conversation. Members can be added or removed from the conversation
using this control message.

```

{
    "control":{
        "addedusers":[],
        "deletedusers":["testbot"],
        "msgtype":4002
    },
    "message_id":"d34058a0f89711e88760d7c8037ea946",
    "msg_ts":"1544019160.275884",
    "msgtype":4002,
    "sender":"user002",
    "sender_type": "normal",
    "time": "7/11/23 5:15 PM",
    "time_iso": "2023-07-11 17:15:49.079",
    "ttl": "7/10/24 5:15 PM",
    "vgroupid":"S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}

```

The `addedusers` field identifies the list of users that were added to the
conversation. The `deletedusers` field identifies the list of users that were
removed from the conversation.

###### Note

This control message has a fixed set of fields and does not require the
`changemask` field.

## Leave room control message

The leave room control message is sent when a user is leaving a secure room or group
conversation. The sender is the user leaving the conversation:

```

{
    "message_id":"f660fe80f89711e887d86d198d2ef374",
    "msg_ts":"1544019219.210107",
    "msgtype":4003,
    "sender":"user002",
    "sender_type": "normal",
    "time": "7/11/23 5:54 PM",
    "time_iso": "2023-07-11 17:54:31.688",
    "ttl": "7/10/24 5:54 PM",
    "vgroupid":"S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}

```

This control message is a simple control message and does not contain the "control" JSON
object. The `msgtype` fields identifies the leave room action.

## Modify room parameters control message

The modify room parameters control message is used to modify one or more fields associated
with a group or secure room conversation.

```

{
    "control":{
        "bor":0,
        "changemask":47,
        "description":"change description",
        "masters":["user001", "user002"],
        "members":["user002","user002"],
        "msgtype":4004,
        "title":"Creating a room",
        "ttl":2592000
    },
    "message_id":"db805750f89711e8a01ab328ac0b2f04",
    "msg_ts":"1544019174.117057",
    "msgtype":4004,
    "sender":"user002",
    "sender_type": "normal",
    "time": "7/11/23 5:59 PM",
    "time_iso": "2023-07-11 17:59:57.473",
    "ttl": "7/10/24 5:59 PM",
    "vgroupid":"S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}

```

This message is similar to the create room control message. The `changemask`
field has the same definition as well.

## Delete room control message

The delete room control message is used to delete a specific group or secure room
conversation.

```

{
    "message_id":"06364710f89811e899418b6723464a0c",
    "msg_ts":"1544019245.773676",
    "msgtype":4005,
    "sender":"user002",
    "sender_type": "normal",
    "time": "7/11/23 6:03 PM",
    "time_iso": "2023-07-11 18:03:01.100",
    "ttl": "7/12/23 6:03 PM",
    "vgroupid":"S7879eb406958d83b991a5f2acb29e5ad8565a4faa41e1c5cbd7004c5586ddd5"
}

```

This control message does not have a "control" JSON object. The `msgtype`
identifies that action to be performed.

## Delete message

Here is the delete control message that will delete a message from all of the specified
sender's devices. The sender is the sender of the control message, not the original sender of
the message being deleted. The message will not be deleted from other users devices: The
message to delete is identified by the id value in the control group.

```

{
    "control":
    {
        "message_id":"a59a3520ca2f11e7a14cd1c8bf2a1be8",
        "isrecall":false,
        "msgtype":4011
    },
    "message_id":"aa4a3580ca2f11e7a156a34c720bab3d",
    "msg_ts":"1510769172.735225",
    "msgtype":4011,
    "sender":"user003",
    "time":"11/15/17 1:06 PM",
    "vgroupid":"Sb0e9297f2208dc86b63b288df8c226882e1052b65022edb9edb9ecf6e77db08"
}

```

Here is the delete control message that will recall the message from all users the message
was sent to:

```

{
    "control":
    {
        "isrecall":true,
        "message_id":"c2855a10ca2f11e7afa15b0943d8c736",
        "msgtype":4011
    },
    "message_id":"c5bce5e0ca2f11e78946112c51861afa",
    "msg_ts":"1510769218.785332",
    "msgtype":4011,
    "sender":"user003",
    "time": "7/11/23 6:04 PM",
    "time_iso": "2023-07-11 18:04:03.772",
    "ttl": "7/10/24 6:04 PM",
    "vgroupid":"Sb0e9297f2208dc86b63b288df8c226882e1052b65022edb9edb9ecf6e77db08"
}

```

## Modify private property

This message identifies when a conversation is pinned or un-pinned. The "pinned" value
will be true when the conversation is pinned, and "false" when it is being un-pinned.

```

{
    "control":
    {
        "pinned":true,
        "msgtype":4014
    },
    "message_id":"c5bce5e0ca2f11e78946112c51861afa",
    "msg_ts":"1510769218.785332",
    "msgtype":4014,
    "sender":"user003",
    "sender_type": "normal",
    "time": "7/11/23 6:07 PM",
    "time_iso": "2023-07-11 18:07:21.981",
    "ttl": "7/10/24 6:07 PM",
    "vgroupid":"Sb0e9297f2208dc86b63b288df8c226882e1052b65022edb9edb9ecf6e77db08"
}

```

This message identifies when a message is starred:

```

{
    "control": {
      "attributes": [
        {
          "isstarred": true,
          "msgid": "74f16f3011d511ee9456414dec7866b3"
        }
      ],
      "msgtype": 4012
    },
    "message_id": "7a38aa00201511eeb723c79384d92c63",
    "msg_ts": "1689098711.200122",
    "msgtype": 4012,
    "sender": "cn0623_01@amazon.com",
    "sender_type": "normal",
    "time": "7/11/23 6:05 PM",
    "time_iso": "2023-07-11 18:05:11.200",
    "ttl": "7/10/24 6:05 PM",
    "vgroupid": "S5d76ccc43c2bb3bc93e7273798ce8f4b89bfa8429b33888fbcd454e5d233a19"
}

```
