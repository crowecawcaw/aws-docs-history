

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Control messages
<a name="dataretention-control-messages"></a>

Control messages set up and configure secure rooms and group conversations. Wickr also requires these messages to reconstruct the list of users involved in specific secure rooms and group conversations.

Like verification messages, these messages contain additional metadata to describe their actions. The control object can include the following:
+ A **bor** field. This is the burn-on-read time in seconds.
+ A **ttl** field. This is the expiration time in seconds.
+ A **description** field. This is the conversation's description.
+ A **title** field. This is the title of the conversation.
+ A **changemask** field. This is a number value created by adding the following flag values.


| Setting | Flag value | 
| --- | --- | 
| Masters field (moderators) | 1 | 
| TTL (expiration) | 2 | 
| Title field (room name) | 4 | 
| Description | 8 | 
| Meeting ID key | 16 | 
| Burn on read | 32 | 
| Saved items (file vault) | 64 | 

In the following example, the **changemask** value of 47 is equal to the sum of Masters (1), TTL (2), Title (4), Description (8), and Burn on read (32).

```
{
  "control": {
    "bor": 0,
    "changemask": 47,
    "description": "",
    "masters": ["user001", "user002"],
    "members": ["user001", "user002", "user003"],
    "msgtype": 4001,
    "title": "Creating a room",
    "ttl": 2592000
  },
  "message_id": "be452b00f89711e883588d1e7a946847",
  "msg_ts": "1544019125.000000",
  "msgtype": 4001,
  "sender": "user002",
  "sender_type": "normal",
  "time": "12/5/18 2:52 PM",
  "time_iso": "2018-12-05 14:52:05.000",
  "vgroupid": "S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}
```