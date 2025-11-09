This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Wickr message formats

This section describes the format of the Wickr messages utilized by the Wickr IO addon
APIs and the Wickr IO Web Interface REST messaging APIs. It explains the various types of
Wickr messages you can encounter. Each message type includes a "msgtype" field and the
following table lists the values associated with this field.

| Message Type                    | msgtype |
| ------------------------------- | ------- |
| Text message                    | 1000    |
| Verification messages           | 3000    |
| File transfer                   | 6000    |
| Calling messages                | 7000    |
| Location message                | 8000    |
| Edit message                    | 9000    |
| Edit reaction message           | 9100    |
| Create room                     | 4001    |
| Modify room members             | 4002    |
| Leave room                      | 4003    |
| Modify room parameters          | 4004    |
| Delete room                     | 4005    |
| Delete message                  | 4011    |
| Message attributes message      | 4012    |
| Message attributes sync request | 4013    |
| Modify private property         | 4014    |

All of the messages are represented using JSON. The following table describes the possible
fields that are contained in the message JSON.

###### Note

The edit messages are only seen by the compliance bot installations (Wickr Enterprise) or
by the data retention bot (AWS Wickr).

| Field       | Description                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------- |
| control     | JSON object that defines the control message information. Contents described<br>below.        |
| file        | JSON object that defines the details of a file transfer message. Contents described<br>below. |
| id          | Unique identifier for the message                                                             |
| message_id  | The text associated with a text message                                                       |
| msgtype     | Type of message, values defined in table above.                                               |
| msg_ts      | The time the message was sent, accurate to the microsecond.                                   |
| receiver    | Wickr ID of the receiver, for 1-to-1 messages.                                                |
| sender      | Wickr ID of the sending client.                                                               |
| sender_type | Indicates if this is a guest user or normal user.                                             |
| time        | Displayable time message was sent.                                                            |
| time_iso    | The time in ISO format (YYYY-MM-DD hh:mm:ss.xxx)                                              |
| vgroupid    | The unique vGroupID of the conversation.                                                      |
