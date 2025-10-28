This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Edit messages

###### Note

The edit messages are only seen by the compliance bot installations (Wickr Enterprise)
or by data retention bot (AWS Wickr).

There are currently two types of edit messages supported, the location and the text types.
The location type of edit message is sent when a user is sharing their location with someone
else.

```

    {
    "edit":{
    "type":"location",
    "shareexpiriation":"";
    "latitude":45.75017899435506,
    "longitude":-78.99449803034105
    },
    "message_id":"1f88fdc08bec11ea81b689d23fa72c7b",
    "msg_ts":"1588365684.583407",
    "msgtype":9000,
    "receiver":"user003",
    "sender":"user100",
    "sender_type": "normal",
    "time": "7/11/23 5:30 PM",
    "time_iso": "2023-07-11 17:30:15.103",
    "ttl": "7/10/24 5:30 PM",
    "vgroupid":"4ebf561eb2214c4e6f924d09e37bf80b6f9b85cb96b72badb03753d9ed26f7f4"
    }

```

The text type of edit message is sent when the user sends a message that includes links in
it. For example the user sends a message with the link https://howdoyoudo.com in it, the
following is what the edit message would look like:

```

    {
    "edit":{
    "originalmessageid":"11457fa08da211ea881baffab0b42745",
    "text":"https://howdoyoudo.com",
    "type":"text"
    },
    "message_id":"1163e5b08da211eab775a5032a0322ca",
    "msg_ts":"1588553780.419871",
    "msgtype":9000,
    "sender":"user001@amazon.com",
    "sender_type": "normal",
    "time": "7/11/23 5:30 PM",
    "time_iso": "2023-07-11 17:30:15.103",
    "ttl": "7/10/24 5:30 PM",
    "vgroupid":"S243f2ec645d3961bdd531f51f3244205d292b8d0fbd41802827746271d31d41"
    }

```

If you send a text message with a link and the security group has the "Send Link Preview"
option enabled, the edit message may contain an array of links information and link image meta
information. The following shows these additional fields:

```

    {
    "edit":{
    "linkimagemeta":{
    "domain":"userworld.com",
    "guid":"c43c71ef-4373-444e-a22d-dfce34d38a7a",
    "hash":"32bc71721bea8a456a06f364995012d3ebfc41aaaad0c2dd632b0f0bae4690f4bffcd5a4c23b4af16086fcfcd43d20058ca67ae10a7b38d74c2bffa21ea8de05",
    "key":"00a85d12214f596d4eac929d82287cccdead2a00c542f850322c1655494be2a40d"
    },
    "links":[
    {
    "faviconurl":"https://testdaily.com/favicon.ico",
    "imageurl":"https://testdaily.com/uploads/gallery/test-laughing.gif",
    "pagetitle":"Test laughing",
    "sitename":"Test Daily",
    "url":"https://testdaily.com/gallery/image/Test-laughing/"
    }
    ],
    "originalmessageid":"fb7d7d20b25d11eb9a2d77f565346d8b",
    "text":"https://twinsdaily.com/gallery/image/2234-burns-laughing/",
    "type":"text"
    },
    "message_id":"fe9c4950b25d11eb9a2d77f565346d8b",
    "msg_ts":"1620740233.829096",
    "msgtype":9000,
    "receiver":"bnuser02@userworld.com",
    "sender":"bnuser01@userworld.com",
    "sender_type": "normal",
    "time": "7/11/23 5:35 PM",
    "time_iso": "2023-07-11 17:35:41.411",
    "ttl": "7/10/24 5:35 PM",
    "vgroupid":"2c0ae523d2b1af3e43af80b5fafec05548fd2e33fee4c021c66033c6416bb6bb"
    }

```

## Edit content messages

Edit content messages are sent when a user edits the contents of a previously sent
message. The Edit Content message will contain the message ID associated with the original
message and the text of the updated message. The original message text will not be included.
This message type was introduced in the 5.92 version of the WickrIO software. The Edit Content
messages are used to identify when the text of a message is edited as well as when the links
contained in a message are edited.

The following is a basic example of an Edit Content message where the text is
edited:

```

      {
      "content_edited": true,
      "edit":{
      "type":"edit_content",
      "originalmessageid":"36028e2025dd11ec9cdafd3f2bfa110f",
      "text":"This is the edited message"
      },
      "message_id":"3fcef29025dd11ec9cdafd3f2bfa110f",
      "msg_ts":"1633439273.17562",
      "msgtype":9000,
      "receiver":"user001+comp9321_01@wickr.com",
      "sender":"user001+comp9321_02@wickr.com",
      "sender_type": "normal",
      "time": "7/11/23 5:35 PM",
      "time_iso": "2023-07-11 17:35:41.411",
      "ttl": "7/10/24 5:35 PM",
      "vgroupid":"56e3b0570daad62b2e2d14db8d33632f6175514022183a042660c7b8901dec79"
      }

```

The **type** value, within the **edit** group,
identifies this as an Edit Content message. The **originalmessageid**
identifies the message ID of the original message. The **text** field is the
new value of the message.

If the original message contains links, and the "Send Link Previews" option is set for the
security group, there will be two Edit Content messages sent. One of these messages is
associated with the text message changes and another that will contain the link image meta
information. The Edit Content message that contains the "content_edited" with a true value is
associated with the message text, as seen below:

```

      {
      "content_edited":true,
      "edit":{
      "type":"edit_content",
      "originalmessageid":"f4bddd80255e11ec8c960b356f9f1aad",
      "text":"This is a test with https://wickr.com",
      "links":[
      { "url":"https://wickr.com" }
      ],
      },
      "message_id":"b17cffb0264911ec9cdafd3f2bfa110f",
      "msg_ts":"1633485849.387294",
      "msgtype":9000,
      "receiver":"user001+comp9321_01@wickr.com",
      "sender":"user001+comp9321_02@wickr.com",
      "sender_type": "normal",
      "time": "7/11/23 5:35 PM",
      "time_iso": "2023-07-11 17:35:41.411",
      "ttl": "7/10/24 5:35 PM",
      "vgroupid":"56e3b0570daad62b2e2d14db8d33632f6175514022183a042660c7b8901dec79"
      }

```

The following edit content message is associated with the links that are in the
message:

```

      {
      "edit":{
      "type":"edit_content",
      "originalmessageid":"f4bddd80255e11ec8c960b356f9f1aad",
      "text":"This is a test with https://wickr.com",
      "linkimagemeta":{
      "domain":"wickr.com",
      "guid":"4747a757-32db-4748-8a59-f5fc02cf811b",
      "hash":"4848c43ba0ac0cca685cd3053076198f6d710ed02fa7adf4822ba752e48c5328b7bc947d6e0499bfca6d83c86bf805d3b2ed6a7adfa1b300d0be669a1a5e0d3c",
      "key":"0016c4902a79160966335053c07d96accd048ca5ce858f9def2364d11c36b7f345"
      },
      "links":[
      {
      "description":"Wickr provides end-to-end encrypted messaging, audio calling, video conferencing, file and location sharing, and more.",
      "faviconurl":"https://wickr.com/favicon.ico",
      "imageurl":"https://wickr.com/wp-content/uploads/2020/12/wickr-pro-screens-4-1.png",
      "pagetitle":"Home",
      "sitename":"Wickr",
      "url":"https://wickr.com"
      }
      ]
      },
      "message_id":"b270fca0264911ec9cdafd3f2bfa110f",
      "msg_ts":"1633485850.986206",
      "msgtype":9000,
      "receiver":"user001+comp9321_01@wickr.com",
      "sender":"user001+comp9321_02@wickr.com",
      "sender_type": "normal",
      "time": "7/11/23 5:35 PM",
      "time_iso": "2023-07-11 17:35:41.411",
      "ttl": "7/10/24 5:35 PM",
      "vgroupid":"56e3b0570daad62b2e2d14db8d33632f6175514022183a042660c7b8901dec79"
      }

```
