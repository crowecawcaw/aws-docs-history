This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Appendix A: Compliance message

description

The following table contains a list of JSON fields that will be found in the messages that
the compliance bot streams to the received messages file.

| Field                                      | Description                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| bor                                        | The burn-on-read time if one is set for the conversation.                                  |
| control                                    | JSON object that defines the control message information. Contents described below.        |
| file                                       | JSON object that defines the details of a file transfer message. Contents described below. |
| id                                         | A unique identifier for each message.                                                      |
| links                                      | JSON list of link strings for text messages.                                               |
| message                                    | The text associated with a text message.                                                   |
| msg_ts                                     | Timestamp in microseconds based on server time.                                            |
| msgtype                                    | Identifies the type of message, values defined in the table below.                         |
| receiver                                   | The Wickr ID of the recipient.                                                             |
| sender                                     | The Wickr ID of the sender.                                                                |
| sender_type                                | Indicates if this is a guest user or a normal user.                                        |
| time                                       | Human readable time the message was sent.                                                  |
| time_iso                                   | The time in ISO format (YYYY-MM-DD hh:mm:ss.xxx).                                          |
| ttl                                        | The time to live date for the message.                                                     |
| vgroupid                                   | Identifies the conversation the message was sent in.                                       | The following **msgtype** value will describe the type of message being sent. |
| Message Type                               | msgtype value                                                                              |
| ---                                        | ---                                                                                        |
| Text message                               | 1000                                                                                       |
| File transfer                              | 6000                                                                                       |
| Verification message                       | 3000                                                                                       |
| Calling message                            | 7000                                                                                       |
| Location                                   | 8000                                                                                       |
| Edit message                               | 9000                                                                                       |
| Create room                                | 4001                                                                                       |
| Modify room members                        | 4002                                                                                       |
| Leave room                                 | 4003                                                                                       |
| Modify room parameters                     | 4004                                                                                       |
| Delete room                                | 4005                                                                                       |
| Delete message                             | 4011                                                                                       |
| Message attributes msg (message starred)   | 4012                                                                                       |
| Message attributes sync request (not used) | 4013                                                                                       |
| Modify private property (message pinned)   | 4014                                                                                       |
