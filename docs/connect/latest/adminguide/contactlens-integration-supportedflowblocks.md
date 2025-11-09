# Supported flow blocks

for Contact Lens integration

The following tables list the flow blocks that you can use to specify how Amazon Connect
processes the audio stream sessions.

**Set blocks**

| Flow block                  | Effect    | Description                                                                                          |
| --------------------------- | --------- | ---------------------------------------------------------------------------------------------------- |
| Set Working Queue           | No Effect | Sets Working Queue                                                                                   |
| Set Contact Attributes      | Supported | Stores key-value pairs as contact attributes. You set a value<br>that is later referenced in a flow. |
| Get Queue Metrics           | No Effect | Gets queue metrics                                                                                   |
| Change routing priority/age | No Effect | change routing prioroty of contact                                                                   |
| Set Hold Flow               | No Effect | Specifies the flow to invoke when a customer or agent is put on<br>hold.                             |
| Set Whisper Flow            | No Effect | Specifies the flow to invoke when a customer or agent joined in a<br>voice or chat conversation.     |
| Set callback Number         | No Effect | Specify the attribute to set the callback number.                                                    |
| Set Voice                   | No Effect | Sets the text-to-speech (TTS) language and voice to use for the<br>contact flow.                     |
| Set Customer Queue          | No Effect | Sets the customer queue for customer queue flow                                                      |
| Set Disconnect Flow         | No Effect | Sets disconnect flow for disconnect queue flow                                                       |
| Set event flow              | No Effect | Specifies which flow to run during a contact event.                                                  |
| Set routing criteria        | No Effect | Sets the routing criteria for the contact.                                                           |

**Analyze blocks**

| Flow block                           | Effect    | Description                                                         |
| ------------------------------------ | --------- | ------------------------------------------------------------------- |
| Set Recording and Analytics behavior | Supported | Sets options for recording and enables features in<br>Contact Lens. |
| Set logging behavior                 | Supported | Enable or disable flow logs                                         |

**Logic blocks**

| Flow block               | Effect    | Description                                           |
| ------------------------ | --------- | ----------------------------------------------------- |
| Distribute by percentage | Supported | Routes contacts randomly based on a percentage        |
| Loop                     | Supported | Executes looping branch for specified amount of times |

**Branch blocks**

| Flow block               | Effect    | Description                                                            |
| ------------------------ | --------- | ---------------------------------------------------------------------- |
| Check Queue Status       | No Effect | Checks Queue Status                                                    |
| Check Staffing           | No Effect | Checks staffing in queues                                              |
| Check hours of operation | Supported | Branches based on specified hours of operation.                        |
| Check Contact Attributes | Supported | Branches based on a comparison to the value of a contact<br>attribute. |

**Integrate blocks**

| Flow block        | Effect    | Description                                                                                |
| ----------------- | --------- | ------------------------------------------------------------------------------------------ |
| Create Task       | Supported | Creates a new task manually or by leveraging a task<br>template.                           |
| Customer profiles | Supported | Enables you to retrieve, create, and update a customer<br>profile.                         |
| Invoke AWS Lambda | Supported | Calls AWS Lambda, and optionally returns key-value pairs.                                  |
| Invoke module     | Supported | Calls a published module, which enables you create reusable<br>sections of a contact flow. |

**Terminate/Transfer blocks**

| Flow block        | Effect    | Description                                               |
| ----------------- | --------- | --------------------------------------------------------- |
| Disconnect/Hangup | Supported | Disconnects the contact and end the audio stream session. |
| End Flow          | Supported | Ends the current flow without disconnecting the contact.  |
