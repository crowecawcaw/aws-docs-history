This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Text message meta data

As of the 5.81 release of WickrIO, support was added to record the text message meta data
fields. These fields are used to define GUI widgets specific to the text message being
transmitted. Specific GUI widgets include buttons and list items. If you are interested in
creating bots with buttons or lists, refer to the transmit message arguments section of the
Node.js Addon APIs.

## Text message table meta data

The following text message is a broadcast bots response to a /report command. This sample
message contains two meta objects, the "tablemeta" object and the "textcutmeta" object. The
"tablemeta" object contains information used to display the list on the Wickr client. The
column name objects define the headers for the table. The "items" array contains the entries for
the table. The "textcutmeta" array contains information used to remove parts of the "message"
value when displaying the message to the user. This is done because the text of the "message"
may be redundant to the information contained in the "tablemeta" object. This will allow Wickr
clients that do not yet support the "tablemeta" protocol yet.

```

{
   "message":"Here are the past 5 broadcast message(s):\n(1) this is a broadcast\n(2) Send to one user\n(3) This is the 3rd broadcast\n(4) Hello World!\n(5) Test one\nTo get started, select the broadcast for which you would like to generate a report",
   "message_id":"80cff660a75a11eb986e31ce44694ab3",
   "msg_ts":"1619529271.494966",
   "msgtype":1000,
   "receiver":"bnuser01@userworld.com",
   "sender":"bn0523_bcast_bot",
   "tablemeta":{
      "actioncolumnname":"Select",
      "firstcolumnname":"Message",
      "items":[
         {
            "firstcolumnvalue":"this is a broadcast",
            "response":"1"
         },
         {
            "firstcolumnvalue":"Send to one user",
            "response":"2"
         },
         {
            "firstcolumnvalue":"This is the 3rd broadcast",
            "response":"3"
         },
         {
            "firstcolumnvalue":"Hello World!",
            "response":"4"
         },
         {
            "firstcolumnvalue":"Test one",
            "response":"5"
         }
      ],
      "name":"List of Sent Broadcasts"
   },
   "textcutmeta":[
      {
         "end":146,
         "start":0
      }
   ],
   "sender_type": "normal",
   "time": "7/11/23 6:07 PM",
   "time_iso": "2023-07-11 18:07:21.981",
   "ttl": "7/10/24 6:07 PM",
   "vgroupid":"4b32d7c8c6c37cc9e9506e9ed98ce37f0a96e1e45fcd4ca6f6d00c9d435d82e3"
}

```

The text message above is a sample, and does not include all of the optional fields for the
meta data you may see in a message. The "tablemeta" object can contain the following
objects:

| Name             | Description                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| name             | This object is a string that is the name of the table.                                           |
| firstcolumnname  | This object is a string that is the name of the first column of the table.                       |
| secondcolumnname | This object is a string that is the name of the second column of the table. This is<br>optional. |
| actioncolumnname | This object is a string that is the name of the action column of the table. This is<br>optional. |
| items            | This is an array of entries for the table.                                                       |

The items is an array and can contain 0 or more entries for the table. Each entry in this
table will contain the following objects:

| Name              | Description                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| firstcolumnvalue  | This object is a string that is the value for the first column.                                                     |
| secondcolumnvalue | This object is a string that is the value for the second column. This is<br>optional.                               |
| response          | This object is a string that is the value to be returned to the bot when the list is<br>selected. This is optional. |

The "textcutmeta" is used to maintain some backwards compatability with Wickr clients
that do not support lists. The "textcutmeta" is a list that identifies text characters that will
be removed from the message text when the client supports table meta data. Typically the text
that is removed is when the list information is in the message text, see the example above. The
fields of the each of the "textcutmeta" entries identifies the starting index and ending index
of what characters to cut from the message text. These values are 0 relative for the first
character in the message text.

## Text message button meta data

As of the 5.81 release of WickrIO, support was added for buttons. Wickr clients that
support these buttons will display the buttons when the message is received from the bot. There
are several types of buttons, but selecting a button will perform a specific operation,
including sending a message to the bot or sending your location to the bot. The following is an
example of a text message with button meta data:

```

{
   "buttonmeta":[
      {
         "msgbutton":{
            "message":"/ack",
            "text":"/Ack"
         }
      },
      {
         "locationbutton":{
            "locationtype":0,
            "text":"/Ack with Location"
         }
      }
   ],
   "message":"this is a broadcast\n\nBroadcast message sent by: bnuser01@userworld.com\n\nPlease acknowledge message by replying with /ack",
   "message_id":"744dc0c0a75a11eb986e31ce44694ab3",
   "msg_ts":"1619529250.508240",
   "msgtype":1000,
   "receiver":"bnuser01@userworld.com",
   "sender":"bn0523_bcast_bot",
   "sender_type": "normal",
   "time": "7/11/23 6:07 PM",
   "time_iso": "2023-07-11 18:07:21.981",
   "ttl": "7/10/24 6:07 PM",
   "vgroupid":"4b32d7c8c6c37cc9e9506e9ed98ce37f0a96e1e45fcd4ca6f6d00c9d435d82e3"
}

```

The "buttonmeta" array contains all of the buttons associated with this text message. There
are three types of buttons supported:

| Name           | Description                                                                                                                                                                                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| msgbutton      | This is a normal button type that contains the text of the button and the message to<br>be sent to the bot when the button is selected.                                                                                                                                                    |
| locationbutton | This is a location button that will perform a location based operation. Currently, the<br>"locationtype" value of 0 means the client will send the location of the device to the bot<br>when the button is selected. There will be other location type buttons supported in the<br>future. |

The "msgbutton" object will have the following objects:

| Name    | Description                                                              |
| ------- | ------------------------------------------------------------------------ |
| text    | This is the text of the button to be displayed                           |
| message | This is the message that is sent to the bot when the button is selected. |

The "locationbutton" type performs a location type of operation. The "locationbutton"
object has the following objects:

| Name | Description                                                                                                                                                                                                                                           |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| text | This is the text of the button to be displayed                                                                                                                                                                                                        |
| type | The type of location operation to perform. Value of 0 is to have the client send the<br>location to the bot when the button is selected. Other location button types will have the<br>option to start and stop location sharing, not implemented yet. |
