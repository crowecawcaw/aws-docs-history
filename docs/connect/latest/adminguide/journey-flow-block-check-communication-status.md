# Check communication status

## Description

Use this block to verify whether an outbound message or voice call succeeded before proceeding. You can add up to 5 conditions.

**Example use cases**

- Follow up only after an SMS or email is delivered.
- Retry or route to an agent if a call fails or reaches voicemail.

## How to configure this block

You can configure the **Check communication status** block in the admin website or using the CheckCommunicationStatus action in Flow language.

## Supported status

| Channel  | Status                              |
| -------- | ----------------------------------- |
| WhatsApp | Failed                              |
|          | Delivered                           |
|          | Sent                                |
|          | Read                                |
| SMS      | Text invalid                        |
|          | Text blocked                        |
|          | Text delivered                      |
|          | Text successful                     |
|          | Text queued                         |
|          | Text pending                        |
|          | Text TTL expired                    |
|          | Text carrier unreachable            |
|          | Text invalid message                |
|          | Text carrier blocked                |
|          | Text spam                           |
|          | Text unknown                        |
| Voice    | Voicemail beep                      |
|          | Voicemail no beep                   |
|          | AMD unanswered                      |
|          | Sit tone busy                       |
|          | Sit tone invalid number             |
|          | Human answered                      |
|          | AMD unresolved                      |
|          | AMD unresolved_silence              |
|          | AMD not applicable                  |
|          | Sit tone detected                   |
|          | Fax machine detected                |
|          | AMD error                           |
|          | Outbound destination endpoint error |
|          | Outbound resource error             |
|          | Outbound attempt failed             |
|          | Outbound preview discarded          |
|          | Expired                             |
|          | AMD disabled                        |
|          | Initiated                           |
|          | connected_to_system                 |
|          | Contact data updated                |
|          | Queued                              |
|          | Connected to agent                  |
|          | Disconnected                        |
|          | Completed                           |
| Email    | Bounce                              |
|          | Complaint                           |
|          | Delivery                            |
|          | Send                                |
|          | Reject                              |
|          | Open                                |
|          | Click                               |
|          | Rendering Failure                   |
|          | DeliveryDelay                       |
|          | Subscription                        |
