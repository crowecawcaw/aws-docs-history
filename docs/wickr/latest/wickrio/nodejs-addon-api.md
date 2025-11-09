This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Node.js Addon API

This section describes the Wickr IO Node.js addon and how to use it with several
examples. The APIs provided by the Wickr IO Node.js addon are low-level APIs, using the
APIs provided by the Wickr IO Bot API provide a higher-level approach to some of the main
aspects of an Wickr IO integration interfacing with a Wickr IO client. You will still
need to use the Wickr IO Node.js addon to perform most interactions with the Wickr IO
client. The APIs supported by the Wickr IO Node.js addon allow you to access all of the
necessary functionality from the Wickr IO client to communicate with other Wickr users
within the Wickr network.

The Wickr IO Node.js addon is published to the default NPM registry. The name of the
published module is `wickrio_addon`. It supports a specific set of functions
consistent with the Wickr IO REST API.

When using the Wickr IO Node.js addon you will have access to one Wickr IO client at a
time. It is not currently possible for an integration to communicate with more than one
Wickr IO client at the same time via the addon. Interaction with the Node.js is as
follows:

1. Initialize the Wickr IO Node.js addon interface. This is done by calling the
   clientInit() API, and supplying the user name of the Wickr IO client that is going
   to be used. The start() API provided by the Wickr IO Bot API uses the clientInit()
   API to initiate a connection to the Wickr IO client. We recommend using that API
   instead.
2. Interact with the Wickr IO client by calling the appropriate APIs.
3. When your program is complete then call the closeClient() API to gracefully stop
   processing. The close() API, provided by the Wickr IO Bot API, uses the
   closeClient() API to shut down the connection to the Wickr IO client.
   The addon APIs are described in detail in the following sections.

## Startup and Shutdown APIs

This section describes the APIs used to start and stop the connection between the
Wickr IO integration and the Wickr IO client.

The interface between the Wickr IO integration and the Wickr IO client needs to be
initialized. Initialization includes identifying the Wickr IO client and making sure
the Wickr IO client is in the appropriate state, for example running and logged into
the Wickr network. Once the interface between the client and the integration has been
initialized you can start using the other Wickr IO Node.js addon APIs. Also, the
interface should be gracefully shutdown when you are done using the APIs.

###### Note

Using the Wickr IO Bot API provides a higher-level API (start()) that will call
the appropriate APIs in this addon.

**clientInit(string
_clientName_)**

Before accessing any of the Wickr IO Node.js addon APIs you will need to run the
"clientInit(_clientName_)". The only argument is the user name
associated with the Wickr IO client.

###### Note

If you use the Wickr IO Bot API, the call to the start() API will call the
clientInit() API.

**closeClient()**

This API will close the currently open client object(s). This should be called when
done interacting with the client set in the "clientInit()" API.

###### Note

If you use the Wickr IO Bot API, the call to the close() API will call the
closeClient() API.

**isConnected(int _seconds_)**

The isConnect() API checks if there is a valid connection from the calling Wickr IO
integration to the Wickr IO client. The call will wait the input number of seconds for
a connection. The API returns true if a response was received from the client within the
amount of seconds input, otherwise it will return false.

###### Warning

If true is returned it does not mean the client is prepared to handle other
requests yet. Use the `getClientState()` API to make sure the client is
in the appropriate state. For most APIs the client should be in the RUNNING
state.

###### Note

The Wickr IO Bot API's start() API uses this API to make sure the connection to
the client exists.

**getClientState()**

This API retrieves the current state of the Wickr IO client the integration is
connected with. The value returned is one of the following possible values:

- LOGGINGIN
- NOTRUNNINNG
- RUNNING
- SHUTTINGDOWN
- STARTING
- UNINITIALIZED

It is important to make sure the Wickr IO client is in the RUNNING state before
performing any API calls that require access to the Wickr network. Doing so before
then may have unpredictable results.

###### Note

The Wickr IO Bot API's start() API uses this API repetitively to make sure the
client is in the RUNNING state before returning.

## Configuration API

The configuration API is used by the integration to configure specific Wickr IO
client modes of operation. Since the Wickr IO client is a separate software module
this API will provide a method to modify how the client operates. Typically, the use of
these APIs is done after the interface to the Wickr IO client has been
initialized.

**cmdSetControl(string _configKey_, string
_configValue_)**

This API will tell the Wickr IO client to set the specific
_configKey_ to the input _configValue_. You
will have to make a call to cmdSetControl() for each _configKey_
value that is being set. The following is a list of _configKey_
values that can be set:

| Config Key        | Description                                                                                                                                                                                                                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| attachLifeMinutes | This is a number that represents the number of minutes an attachment<br>(file) will remain on the Wickr IO client. After that amount of time<br>the attachment will be removed. A value of 0 will keep attachments on<br>the system indefinitely, this is the default value. It is highly<br>recommended that this value is set to something other than 0. |
| doreceive         | If set to 'false' the Wickr IO client will NOT forward incoming<br>Wickr messages to the integration software. This is useful for<br>transmit only integrations. The default value is 'true'.                                                                                                                                                              |
| duration          | This value is used to make the Wickr IO client and integration to<br>perform a restart after a number of seconds. A value of 0 will not<br>perform a restart. This value is helpful for testing, or if you wish to<br>perform periodic restarts. The default value is '0'.                                                                                 |

## Statistics APIs

APIs are provided to retrieve messaging statistics that are maintained by the Wickr
IO client. You can get and clear the retrieved statistics.

**cmdGetStatistics()**

This API will return a list of messaging and error statistics, for example.

```

{
    "statistics": {
        "message_count": 5,
        "pending_messages": 0,
        "sent": 7,
        "received": 3,
        "sent_errors": 1,
        "recv_errors": 1
    }
}

```

The following table describes each of the statistics that can be returned by this
API:

| Statistics                | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| message_count             | The number of received messages that are currently queued to a<br>conversation on the Wickr IO client. These queues feed into the main<br>receive queue that is used by the message callback and retrieval<br>APIs.                                                                                                                                                                                                          |
| outbox_sync               | The number of outbox sync messages received. Outbox sync messages are<br>messages that were sent by another device for this Wickr IO client.<br>This is only valid when there are multiple devices configured for a<br>Wickr IO client, which is not typical.                                                                                                                                                                |
| pending_callback_messages | The number of messages on the callback message queue. These are<br>messages received by the Wickr IO client, that are waiting to be sent<br>to a callback process. This number will be decremented for each message<br>that is retrieved from the Wickr IO client using the<br>cmdGetReceivedMessage() API or received by the integration software<br>successfully via the asynchronous message handling (i.e.<br>callback). |
| pending_messages          | The number of messages that are currently queued to be sent from the<br>Wickr IO client to Wickr clients on the Wickr network.                                                                                                                                                                                                                                                                                               |
| received                  | The number of messages that the Wickr IO client has<br>received.                                                                                                                                                                                                                                                                                                                                                             |
| recv_errors               | The number of errors that occurred while receiving messages.                                                                                                                                                                                                                                                                                                                                                                 |
| sent                      | The number of messages that have been sent by the Wickr IO<br>client.                                                                                                                                                                                                                                                                                                                                                        |
| sent_errors               | The number of errors that have occurred while trying to send<br>messages.                                                                                                                                                                                                                                                                                                                                                    |

**cmdClearStatistics()**

This API will clear the current statistics that are saved in the client.

## Wickr Client APIs

This section describes APIs that provide information about Wickr Clients. You can
use these APIs to get information about a Wickr client that the bot can communicate
with.

**cmdGetUserInfo(string users[])**

This API returns information about the each of the users from the input array of
Wickr user IDs. The value returned is a JSON object with two arrays, one for the
Wickr users that exist and one for the Wickr users that do not exist. The following
is an example of the JSON returned:

```

{
    "users" : [
        { "name" : "bobsmith@company.com", "full_name" : "Bob Smith", "is_bot", false" },
        { "name" : "joebrown@companuy.com", "full_name" : "Joe Brown", "is_bot", false" }
        ],
    "failed" : [ "failedUser1", "failedUser2" ]
}

```

###### Warning

This API requires interaction with the Wickr server, so keep the number of users
on the input list small so the response does not take too long.

**cmdGetClientInfo()**

This API will retrieve the bot client information. The values are returned in a JSON
list of objects.

```

{
    "version" : "<bot client's version>",
    "organization" : "Wickr, Inc."
}

```

This API can be used to verify the version of the client.

**cmdSetVerificationMode(string mode)**

This API is used to set the verification mode that the bot client will operate under.
The possible values for the input mode are "automatic" or "manual", all other values
will return an error. If the verification mode is set to "automatic" then any client the
bot client interacts with becomes unverified, the bot client will automatically put that
client into the verified state. If the verification mode is set to "manual" then it is
up to the bot integration to peridically get the verification list, using the
"cmdGetVerificationList" API and then calling the "cmdVerifyUsers" or
"cmdVerifyAllUsers" APIs.

**cmdGetVerificationList(string mode)**

This API will return a list of users that have become unverified. The mode argument is
optional. Normally, this API will return users that have a failed verification status.
When you call this function with a mode value of "all" then this API will return users
that are not verified, meaning they can have a verification status of failed, unverified
or pending. The value returned will be a JSON string with a list of users and their
verification status. These verification functions are necessary when verification is
done manually but the bot integration.

The following is a sample response:

```

{
    "users" : [
        { "user": "wickrID1", "reason": "failed" },
        { "user": "wickrID2", "reason": "unverified" },
        { "user": "wickrID3", "reason": "pending" }
    ]
}

```

**cmdVerifyUsers(string users[])**

This API will verify all of the users in the input users array. The verification
status for each of these users will be changed to verified. You will only need to use
this API if your bot was setup to do verification manually.

**cmdVerifyAll()**

This API will verify all users that are in the unverified or failed verification
state. This will only be necessary if the bot is doing verification manually.

## Secure Room Conversation APIs

This section describes the APIs that perform operations on Wickr secure rooms. The
operations you can perform include adding, modifying, deleting and retrieving secure
rooms. For APIs where you are dealing with a specific secure room, you will need to have
the _VGroupID_ that is associated with that room.

**cmdAddRoom(string members[], string moderators[], string title,
string desc, string ttl, string bor)**

This API creates a new secure room. The arguments of this request will contain the
information associated with the room.

The members and moderators arguments are arrays of strings, that are Wickr IDs. The
members array is the complete list of members of the secure room. The moderators array
is a list of the moderators of the secure room. The moderators must also be in the
members list. There must be at least one moderator in the room.

The ttl is the time to live value. The bor is the burn on read value. These values are
strings but the contents of the string is a number. The ttl and bor values are optional.
If the bor value is included then the ttl value must also be included.

```

{
    "vgroupid": "S0b503ae14cc896aad758ce48f63ac5fae0adccd78ef18cde82563c63b2c7761"
}

```

The response will either be an error with a description of that error or a successful
response with the vGroupId of the newly created room.

**cmdDeleteRoom(string vgroupid)**

In order to delete a secure room, you will need to have the vGroupID associated with
that room. You can use the get rooms API to get the list of rooms known by the Wickr
IO client, then determine which room to delete. Also, saving the vGroupID returned from
the add room API can be used as well.

**cmdGetRoom(string
_vgroupid_)**

This API will return details of a specific secure room conversation. The Wickr IO
client will respond with a JSON structure containing information for the specified
conversation.

```

{
    "rooms": [
        {
            "description": "Room description",
            "masters": [
                { "name" : "username001" }
            ],
            "members": [
                { "name" : "username001" },
                { "name" : "username002" }
            ],
            "title": "Room Title",
            "ttl": "-1",
            "vgroupid": "S00bf0ca3169bb9e7c3eba13b767bd10fcc8f41a3e34e5c54dab8bflkjdfde"
        }
    ]
}

```

**cmdGetRooms()**

This API will return a list of secure rooms that are known by the Wickr IO client.
The Wickr IO client will respond with a JSON array of the secure rooms that the
Wickr IO client is a member of. The following is an example of what the JSON returned
from this API:

```

{
    "rooms": [
        {
            "description": "Room description",
            "masters": [
                { "name" : "username001" }
            ],
            "members": [
                { "name" : "username001" },
                { "name" : "username002" }
            ],
            "title": "Room Title",
            "ttl": "7776000",
            "bor": "0",
            "vgroupid": "S00bf0ca3169bb9e7c3eba13b767bd10fcc8f41a3e34e5c54dab8bflkjdfde"
        }
    ]
}

```

**cmdLeaveRoom(string vgroupid)**

This API will instruct the Wickr IO client to leave the secure room identified by
the input vGroupID. In order to leave a secure room, you will need to have the vGroupID
associated with that room. You can use the get rooms API to get the list of rooms known
by the Wickr IO client, then determine which room to leave. Also, saving the vGroupID
returned from the create room API can be used as well.

**cmdModifyRoom(string vgroupid, string members[], string
moderators[], string title, string description, string ttl, string
bor)**

This API is used to modify some of the settings associated with a room. The following
room attributes can be modified using this API:

- TTL
- BOR
- Description
- Title
- Members
- Moderators

The Wickr IO client must be a moderator for the room identified by the input
vGroupID, otherwise the request will fail.

## Group Conversation APIs

This section describes the APIs associated with group conversations. Using these APIs,
you can create, get or delete group conversations that the Wickr IO client is a part
of.

**cmdAddGroupConvo(string members[], string ttl, string
bor)**

This API will create a new group conversation. The members argument is required, and
the ttl and bor values are optional. The response will either be an error with a
description of that error or a successful response with the vGroupID of the newly
created group conversation.

```

{
    "vgroupid": "G0b503ae14cc896aad758ce48f63ac5fae0adccd78ef18cde82563c63b2c7761"
}

```

**cmdDeleteGroupConvo(string vgroupid)**

This API will instruct the Wickr IO client to leave a group conversation. You can
only actually delete a group conversation if the client is the last member of the group
conversation.

In order to delete a group conversation, you will need to have the vGroupID associated
with that conversation. You can use the get group conversations API to get the list of
conversations known by the Wickr IO client, then determine which conversation to
delete. Also, saving the vGroupID returned from the create group conversation API can be
used as well. The group conversation with the same vGroupID will be deleted.

**cmdGetGroupConvos()**

This API will return a list of group conversations that are known by the Wickr IO
client. The Wickr IO client will respond with a JSON array of the group
conversations.

```

{
    "groupconvos": [
        {
            "members": [
                { "name" : "username001" },
                { "name" : "username002" }
            ],
            "ttl": "7776000",
            "bor": "0",
            "vgroupid": "G00bf0ca3169bb9e7c3eba13b767bd10fcc8f41a3e34e5c54dab8bflkjdfde"
        }
    ]
}

```

**cmdGetGroupConvo(string vgroupid)**

This API will return details of a specific group conversation. The Wickr IO will
respond with a JSON structure containing information for the specified
conversation.

```

{
    "rooms": [
        {
            "members": [
                { "name" : "username001" },
                { "name" : "username002" }
            ],
            "vgroupid": "G00bf0ca3169bb9e7c3eba13b767bd10fcc8f41a3e34e5c54dab8bflkjdfde"
        }
    ]
}

```

## Receive Message APIs

These messaging APIs are used to retrieve Wickr messages received by the Wickr IO
client. Messages received by the Wickr IO client can be retrieved using one of the
following methods:

- Explicitly polling for the received messages
- Asynchronously receiving messages
- Setting a URL where received messages will be posted to.

The Wickr IO APIs will only support one receive message method at a time. When a
message has successfully been transferred from the Wickr IO client to the integration
software that message will be removed from the Wickr IO client queue. The Wickr IO
client will not save messages after completion of the transfer.

The format of the messages received is described in the message format section.

**cmdGetReceivedMessage()**

This API will retrieve the next message waiting to be read. Each call to this API will
return just one message if any are waiting to be read. After the message is retrieved it
will be removed from the Wickr IO client database.

**cmdStartAsyncRecvMessages(function
callback(string))**

This API will initiate the asynchronous reception of received messages. The input
callback argument will be called when a message is received by the associated
client.

Any implementation that uses this API must make sure events can be handled so that the
message callback may be called.

**cmdStopAsyncRecvMessages()**

This API will stop the asynchronous reception of received messages.

**cmdSetMsgCallback(string url)**

Use this API to set a URL that will be used by the client to send received messages
to. Any messages received after this API is performed will be sent to the defined URL.
When using this method of receiving messages be careful to make sure the software
running on the Wickr IO Docker image can access the URL.

**cmdGetMsgCallback()**

Use this API to get the currently set message callback URL. If there is a URL callback
defined the following is the format of the body.

```

{
    "callback": "https://localhost:4008"
}

```

**cmdDeleteMsgCallback()**

If the URL callback is no longer needed or you need to switch to receive messages
asynchronously then delete the existing message URL callback. This API will delete the
current message callback.

## Transmit Message Arguments

There are several arguments to the transmit APIs that need more detailed
descriptions.

**Message Meta Arguments**

New to the 5.81 version of WickrIO, is the support for button and table GUI widgets.
These GUI widgets are only supported in text messages, file messages do not support
them. The transmit APIs have been modified to support an optional argument (messagemeta)
that identifies these buttons or tables. The messagemeta argument is a JSON string that
identifies the GUI elements associated with the message being transmitted. The following
figure shows the JSON associated with two buttons, one is a normal message button and
the other is a location button:

```

{
    "buttons" : [
        {
            "type": "message",
            "text": "Button Text",
            "message": "/action"
        },
        {
            "type": "getlocation",
            "text": "Send Location"
        }
    ]
}

```

The "type" object identifies the type of the button, and the "text" identifies the
text that will be displayed on the button to the user. The "message" object of the
message button is what the client will send back to the bot when the button is selected.
The "getlocation" type of button, when selected the client will send the client's
location to the bot.

The table GUI widget is used to display a selectable list of information on the
client. The messagemeta JSON string can contain a "table" object and a "textcut" object.
The "textcut" object is optional. The "table" object contains all the details of the
table to be shown. The "textcut" object contains a list of values that indicate which
characters in the message text should be cut if the client supports the table GUI
widget. Normally, if a client does not support the table GUI widgets it will just
display the message text. If the client does support the table GUI widgets it will
display the message text, minus the text referenced by the "textcut" values, and then
the list GUI. The following is a sample.

```

{
    "table" : {
        "name": "Table heading",
        "firstcolname": "Column 1",
        "secondcolname": "Column 2",
        "actioncolname": "Action",
        "rows": [
            {
                "firstcolvalue": "123",
                "secondcolvalue": "Hello",
                "response": "1"
            },
            {
                "firstcolvalue": "2838",
                "secondcolvalue": "There",
                "response": "2"
            }
        ]
    },
    "textcut" : [
        { "startindex": 0, "endindex": 75 }
    ]
}

```

The sample above shows all of the possible objects associated with the "table" and
"textcut" objects. The "textcut" array is optional. The "secondcolname" and
"secondcolvalue" objects are optional. The table can have one or two columns.

To include buttons or lists in your text messages you will create a JSON string and
that wil be the messagemeta argument to the message sending APIs (shown below). The
following is an example of the Javascript code for creating the messagemeta string for
some buttons. When the button is selected the 'message' value will be sent to the
bot.

```
const messagemeta = {
    buttons: [
        {
            type: 'message',
            text: 'yes',
            message: 'yes',
        },
        {
            type: 'message',
            text: 'no',
            message: 'no',
        }
    ],
}
const messagemetastring = JSON.stringify(messagemeta)
```

The following is an example Javascript for creating the message meta string for a
list. The action column contains the value that will be returned to the bot when that
item is selected. In this case it will be the number '1', '2' or '3'.

```
const users = [ 'user1@somewhere.com', 'user2@somewhere.com', 'user3@somewhere.com' ]

let messagemeta = {
    table: {
        name: 'List of Users',
        firstcolname: 'User',
        actioncolname: 'Select',
        rows: [],
    },
    textcut: [
        {
            startindex: 0,
            endindex: entriesString.length - 1,
        },
    ],
}

for (let i = 0; i < users.length; i++) {
    const response = i + 1
    const row = {
        firstcolvalue: users[i],
        response: response.toString(),
    }
    messagemeta.table.rows.push(row)
}

const messagemetastring = JSON.stringify(messagemeta)
```

**Message ID Arguments**

The messageID argument for the transmit functions is used to track the status of
transmits. Bot integrations like the broadcast bot use the messageID values to track the
process of a broadcast. The messageID can be used later to retrieve the status of the
transmission of all messages associated with that messageID value.

**Flags Arguments**

The flags arguments to the transmit functions is not fully defined. It will be defined
in a future document.

## Transmit Message APIs

The transmit message APIs support transmitting normal messages as well as files.
Messages and files will be transmitted to specific 1-on-1, secure room, or group
conversations on the Wickr network via the Wickr IO client. For secure rooms and
group conversations you will need to have the vGroupID associated with the specific
conversation.

Some of the arguments to these functions are optional. Required arguments will always
be listed first in the function definitions. The order of the arguments must follow the
defined function signature. If you are going to use an optional argument that is after
one you are not going to use then you will have to pass an appropriate value for the
optional argument you are not using (i.e. "" for string arguments, [] for array
arguments).

**cmdSend1to1Message(string users[], string message, string ttl,
string bor, string messageID, string flags[], string messagemeta)**

This API is used to send a message to one or more Wickr clients. The "users" field
may contain an array of 1 or more users to send the message to. The message will be sent
to each user on a separate 1-to-1 conversation. So, if the API request "users" field
contains 5 users then 5 messages will be sent, using the text from the "message"
field.

The users array and message arguments are required, the remaining arguments are
optional.

**cmdSendRoomMessage(string vgroupid, string message, string ttl,
string bor, string messageID, string flags[], string messagemeta)**

This API is used to send a message to a secure room or group conversation. If you want
to send a message to a secure room or a group conversation you will need to get the
vGroupID associated with that conversation. To do that the vGroupID will be returned
when you create the room/conversation using the appropriate API. Also, the get rooms API
will return a list of known rooms that you can send to, the vGroupID is contained in the
response.

The vgroupid and message arguments are required, the remaining arguments are
optional.

**cmdSend1to1Attachment(string users[], string filename, string
displayname, string ttl, string bor, string messagemeta)**

This API is used to send a file to one or more users. The file will be sent to each of
the users in the input users list, via individual 1-to-1 conversations. The filename
identifies a file that is located on the client system or a URL that identifies a
remotely accessible file. If this is a local file, the file must be located in a
location on the client that is accessible by the bot's client software running on the
Wickr IO Docker image. The displayname field will be sent in the file transfer
message.

The users array and filename arguments are required, the remaining arguments are
optional.

**cmdSendRoomAttachment(string vgroupid, string filename, string
displayname, string ttl, string bor, string messagemeta)**

This API is used to send a file to a secure room or group conversation. The file will
be sent to the conversation associated with the input vgroupid. The filename identifies
a file that is located on the client system or a URL that identifies a remotely
accessible file. If this is a local file, the file must be located in a location on the
client that is accessible by the bot's client software running on the Wickr IO Docker
image. The displayname field will be sent in the file transfer message.

The vgroupid and filename arguments are required, the remaining arguments are
optional.

**cmdSendMessageUserNameFile(string fileName, string message,
string ttl, string bor, string messageID, string flags[], string
messagemeta)**

This API is used to send a message to a list of Wickr clients contained in the input
file. The "fileName" contains the full pathname of a file that is readable by the
Wickr IO bot. The file contains a list of Wickr users, one per line in the file. The
input message will be sent to each user on a separate 1-to-1 conversation. So, if the
API request "fileName" file contains 5 users then 5 messages will be sent, using the
text from the "message" field.

The fileName and message arguments are required, the remaining arguments are
optional.

**cmdSendAttachmentUserNameFile(string fileName, string
attachment, string displayname, string ttl, string bor, string messageID, string
messagemeta)**

This API is used to send a file to a list of Wickr clients contained in the input
file. The "fileName" contains the full pathname of a file that is readable by the
Wickr IO bot. The file contains a list of Wickr users, one per line in the file. The
input file identified by the "attachment" will be sent to each user on a separate 1-to-1
conversation. So, if the API request "fileName" file contains 5 users then 5 messages
will be sent, using the file from the "attachment" field.

The fileName and attachment arguments are required, the remaining arguments are
optional.

## Network and Security Group Message APIs

These APIs are used to send messages and files to the users in a Wickr network or
security group. Since Wickr bots can only transmit to clients in the same network, the
Wickr network is the network that the bot is in. The Wickr bot can transmit to any
of the security groups that are associated with the network it is associated
with.

**cmdSendNetworkMessage(string message, string ttl, string bor,
string messageID, string flags[], string messagemeta)**

This API is used to send a message to all of the Wickr clients in the bot client's
Wickr network. The message will be sent to each user on a separate 1-to-1
conversation. So, if the associated network contains 100 users then 100 messages will be
sent, using the text from the "message" field.

The message argument is required, the remaining arguments are optional.

**cmdSendNetworkAttachment(string filename, string displayname,
string ttl, string bor, string messageID, string message, string
messagemeta)**

This API is used to send a file to all of the Wickr clients in the bot client's
Wickr network. The file will be sent to each of the users in the Wickr network via
individual 1-to-1 conversations. The filename identifies a file that is located on the
client system or a URL that identifies a remotely accessible file. If this is a local
file, the file must be located in a location on the client that is accessible by the
bot's client software running on the Wickr IO Docker image. The displayname field will
be sent in the file transfer message.

The message field is used to also transmit a message, in addition to sending the
attachment.

The filename argument is required, the remaining arguments are optional.

**cmdSendNetworkVoiceMemo(string filename, string displayname,
string ttl, string bor, string messageID, string message, string
messagemeta)**

This API is used to send a voice memo to all of the Wickr clients in the bot
client's Wickr network. The voice memo will be sent to each of the users in the
Wickr network via individual 1-to-1 conversations. The filename identifies a voice
memo file that is located on the client system, this file must be located in a location
on the client that is accessible by the bot's client software running on the Wickr IO
Docker image. The displayname field will be sent in the file transfer message.

The message field is used to also transmit a message, in addition to sending the
attachment.

The filename argument is required, the remaining arguments are optional.

**cmdGetSecurityGroups(string page, string size)**

This API will return a list of information for the Security Groups that are associated
with the Wickr network the bot client is in. The page and size values are used to
iterate through a large list of security groups. The page identifies which page of
security groups to retrieve, where each page contains size number of entries. The page
and size input values are optional but if specified they both have to be
specified.

The value returned is a JSON array containing the following entries:

```

{
  "size" : <size of security group>,
  "name" : "<security group name>",
  "id" : "<security group ID>"
}

```

The "size" value is the number of users that are in the security group. The "name" is
the actual name of the security group. The "id" is a unique identifier for the security
group. The "id" value is used in the following APIs to send to security groups
users.

**cmdSendSecurityGroupMessage(string message, string groupids[],
string ttl, string bor, string messageID, string flags[], string
messagemeta)**

This API is used to send a message to all of the Wickr clients in the security
groups identified by the groupids value. The message will be sent to each user on a
separate 1-to-1 conversation. So, if the associated security groups contain 100 users
then 100 messages will be sent, using the text from the "message" field.

The message and groupids arguments are required, the remaining arguments are
optional.

**cmdSendSecurityGroupAttachment(string groupids[], string
fileName, string displayname, string ttl, string bor, string messageID, string
message, string messagemeta)**

This API is used to send a file to all of the Wickr clients in the security groups
identified by the groupids value. The file will be sent to each of the users via
individual 1-to-1 conversations. The filename identifies a file that is located on the
client system or a URL that identifies a remotely accessible file. If this is a local
file, the file must be located in a location on the client that is accessible by the
bot's client software running on the Wickr IO Docker image. The displayname field will
be sent in the file transfer message.

The message field is used to also transmit a message, in addition to sending the
attachment.

The groupids and fileName arguments are required, the remaining arguments are
optional.

**cmdSendSecurityGroupVoiceMemo(string groupids[], string
fileName, string displayname, string ttl, string bor, string messageID, string
message, string messagemeta)**

This API is used to send a voice memo to all of the Wickr clients in the security
groups identified by the groupids value. The voice memo will be sent to each of the
users via individual 1-to-1 conversations. The filename identifies a voice memo file
that is located on the client system, this file must be located in a location on the
client that is accessible by the bot's client software running on the Wickr IO Docker
image. The displayname field will be sent in the file transfer message.

The message field is used to also transmit a message, in addition to sending the
attachment.

The groupids and fileName arguments are required, the remaining arguments are
optional.

## Message Status APIs

These APIs are available to the bulk send APIs of the Wickr IO bot (i.e. network and
security sending, file name list sending). The APIs will provide the ability to track
the number of messages sent and remaining to be sent as well as if errors have occured
during the sending of any of the messages. Errors will be identified on a per user basis
as well, which can help determine if there was a problem sending to specific Wickr
users.

**cmdAddMessageID(string messageid, string sender, string target,
string datesent, string message)**

Before sending a message that you want to track you will need to call this API to add
the message ID information to the Wickr IO client. This API is used to add a message
ID entry to the Wickr IO clients database. The key part of this API is the message ID,
it MUST be unique. The other values are determined by the integration using this
API.

The messageid value should uniquely identify the message being sent.

The sender is a string that should be used to identify the sender of the message. The
contents of this value is up to the integration using it. It can be used to restrict
access to the message ID information, so that users interacting with your integration
cannot see message information for other users.

The target is a string that should be used to identify who the message(s) are being
sent to. The contents of this value is up to the integration using it. The intent is to
determine what type of message was being sent.

The datesent is used to identify the date and time when the message was sent. The
contents of this value is up to the integration using it.

The message value is used to save the actual message or a string that identifies to
the users the message that was sent.

**cmdDeleteMessageID(string messageid)**

This API will delete all entries in the Wickr bot's client database associated with
the input message ID value.

**cmdGetMessageIDEntry(string messageid)**

This API will retrieve the information associated with the input message ID value. The
value returned is a JSON object with the following format:

```

{
  "message_id" : "<message ID value>",
  "sender"     : "<sender value>",
  "target"     : "<target value>",
  "when_sent"  : "<when sent value>",
  "message"    : "<message value>"
}

```

**cmdGetMessageIDTable(string page, string size)**

This API is used to retrieve all of the message ID entries from the Wickr bot
client's database. Since this table can get very large over time you will need to limit
the number of entries retrieved by using the page and size values. The page is a 0
relative value used to identify which page to retrieve, where each page contains a
number of entries equal to the size value. If the table is large enough you will need to
iterate through each page until the number of entries is less than the size value. The
return value from this API is a JSON array of the message ID objects, as shown in the
cmdGetMessageIDEntry() API above.

**cmdCancelMessageID(string messageID)**

This API is used to cancel the transmit associated with the input messageID value. The
bot client will attempt to stop the transmission. There is no guarantee that the
transmit will be fully cancelled, but any subsequent transmits associated with the
messageID should not occur.

**cmdGetMessageStatus(string messageid, string type, string page,
string size)**

This API is used to retrieve the status of a specific message, identified by the input
messageid value. The type value identifies what type of information should be returned.
There are two types of message status values that can be returned:

- "full" for a full status for all users that the message is being sent
  to
- "summary" for a summary of the transmission for the associate message being
  sent.

The type value is optional, if not specified the default is to return a "summary"
status of the associated message transmission. If the status to be returned is a
"summary" then the following JSON object will be returned:

```

{
  "num2send" : <number of users to send to>,
  "pending"  : <number pending to send>,
  "sent"     : <number sent>,
  "failed"   : <number failed to send>,
  "acked"    : <number acked by receiver>
}

```

The values returned are all numbers. The "acked" value is the number of users that
have responded to the bot. NOTE: a user sending a message to the bot will acknowledge
all message ID entries associated with that user. This behavior will change in future
versions.

If the type value is "full" then an array of values is returned, one for each user
that the message is targeted to. The JSON array returned will contain objects with the
following format:

```

{
  "user"           : "<user ID>",
  "status"         : <status of message to user>,
  "status_message" : "<error status if any>"
}

```

The "user" value is the user name that the message will be sent to. The "status" value
is a number value that identifies the status of the message that is being sent to the
"user". The "status" can have a value of one of the following:

- 0 means the message is pending to be sent to the associated user
- 1 means the message has been sent to the associated user
- 2 means the message failed to be sent to the associated user, see the
  "status_message" for details
- 3 means the message was sent and acknowledged by the associated user

If the "status" value returned for a user is a failed (3) then the "status_message"
value will also be returned, otherwise the "status_message" value will not be
returned.

The page and size input values are optional but should be used if the number of users
the message is sent to is large. The page is a 0 relative value used to identify which
page to retrieve, where each page contains a number of entries equal to the size value.
If the table is large enough you will need to iterate through each page until the number
of entries is less than the size value.

**cmdSetMessageStatus(string messageid, string user, string
status, string statusmessage)**

This API can be used to modify the status and status message associated with a
specific user's message status. The statusmessage value is optional. The messageid and
user value will uniquely identify a message ID entry in the Wickr bot client's
database. If there is no entry for the associated message ID and user then an entry will
be created in the database.

The messageid value can have an empty string value (i.e. ""), which can be used to
update ALL message ID entries for the specified user. This can be used for example to
acknowledge all messages sent to that user. If the messageid value is empty and there
are NO user entries for the user then nothing will be added to the database.

## Key-Value APIs

These APIs provide the ability to save and retrieve values to/from a persistent
encrypted storage location. The values will be stored in an encrypted database, that is
associated with the Wickr IO client. Currently, only string values can be saved using
these APIs.

These APIs do not have any relationship to the Wickr messaging, they are supplied
for use by the Wickr IO integrations to have a way to save persistent data.

###### Warning

Since these values are stored in the Wickr IO client database, the values will
be lost if the Wickr IO client database is reset. Also, the values are not
accessible until the Wickr IO client is in the logged in state.

**cmdAddKeyValue(string key, string value)**

This API is used to save, or update the value associated with the input key.

**cmdGetKeyValue(string key)**

This API will return the string value associated with the input key.

**cmdDeleteKeyValue(string key)**

This API will delete the key-value information associated with the input key.

**cmdClearAllKeyValues()**

This API will clear (delete) all key-value pairs from the persistent storage.
