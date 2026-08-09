# Provide call metadata for conversational analytics integration

In Connect Customer, each interaction with a customer is a Connect Customer contact. Each voice session
that comes through the conversational analytics connector creates a Connect Customer contact. The
connector creates a Connect Customer contact using the fields provided in the call metadata.
The call metadata includes the agent user ID and agent queue ID for the streamed
call in the call metadata.

You can provide the agent user ID and other call metadata to the
conversational analytics connector by using supported SIPREC metadata parameters
within the SIP INVITE of the audio stream session. The connector parses the
following call metadata fields and adds this information to the Connect Customer
contact.

| Call State Field  | SIPREC Metadata               | Value                          | If not provided                                                                                                                                                                                      |
| ----------------- | ----------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent user id     | `AmznConnectAgentUserId`      | Connect Customer agent user id | Required                                                                                                                                                                                             |
| Queue id          | `AmznConnectQueueId`          | Connect Customer queue id      | _Optional_. If not provided, the<br>default queue of the Connect Customer instance is used.                                                                                                          |
| Participant order | `AmznConnectParticipantOrder` | Valid values: `asc`, `desc`    | _Optional_. If not provided,<br>ascending order is used. Connect Customer sorts the SIPREC streams by using<br>labels. The first stream in label order is the agent and the second<br>is the caller. |

A contact must have a Connect Customer agent user ID. conversational analytics starts capturing
the streamed audio, and generating call recording and call analysis, only when the
agentId is provided.

If agentid is missing then the Connect Customer conversational analytics connector session is
terminated. If your SIPREC metadata was not parsed automatically by the Connect Customer
conversational analytics connector and agent user ID is not set, you can create a
flow lambda and access all the SIP and SIPREC metadata by using the following
fields:

| Attribute       | Description                                                                                                                                            | JSONPath Reference                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| SIPREC metadata | SIPREC metadata from the SIP event                                                                                                                     | $.Media.Sip.SiprecMetadata            |
| SIP header      | SIP header from the SIP event. {SIP header name} is the name of<br>the SIP header provided in the SIP event. For example, "To", "From",<br>and others. | $.Media.Sip.Headers.{SIP header name} |

For more information, see [Telephony call metadata attributes (call attributes)](connect-attrib-list.md#telephony-call-metadata-attributes "connect-attrib-list.md#telephony-call-metadata-attributes").

## How to use event metadata

Connect Customer publishes SIP, streaming, and contact events. These events include the
metadata gathered from the SIPREC SIP INVITE of the calls. The metadata includes
the SIPREC Metadata, SIP headers, fromNumber, toNumber, and others. Here are
some things you can do with this event metadata:

1. You can process the metadata in these events to determine your own
   unique identifier for the calls and correlate the calls with the your
   own system.
2. You can then add your unique identifier for the call into the call's
   contact attributes by using [Set contact
   attributes](set-contact-attributes.md "set-contact-attributes.md") block.
3. You can search by custom contact attributes in the Connect Customer admin website to find the
   contact for the third-party call in the two Connect Customer instances.

For information about how to create Connect Customer flow Lambda functions, see [Grant Connect Customer access to your AWS Lambda functions](connect-lambda-functions.md "connect-lambda-functions.md"). For a list of all the supported contact attributes that you can access in
your flow Lambda, see [List of available contact attributes in Connect Customer and their JSONPath references](connect-attrib-list.md "connect-attrib-list.md").
