# Check communication status

## Description

Use this block to verify whether an outbound message or voice call succeeded before proceeding. You can add up to 5 conditions.

**Example use cases**

- Follow up only after an SMS or email is delivered.
- Retry or route to an agent if a call fails or reaches voicemail.

## How to configure this block

You can configure the **Check communication status** block in the admin website or using the CheckCommunicationStatus action in Flow language.

## Supported status

| Channel  | Status                              | Description                                                                                                                                                                                            |
| -------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| WhatsApp | Failed                              | The WhatsApp message could not be delivered to the recipient.                                                                                                                                          |
|          | Delivered                           | The WhatsApp message was successfully delivered to the recipient.                                                                                                                                      |
|          | Sent                                | The WhatsApp message was sent to the recipient.                                                                                                                                                        |
|          | Read                                | The recipient opened and read the WhatsApp message.                                                                                                                                                    |
| SMS      | Text invalid                        | The destination phone number is not valid.                                                                                                                                                             |
|          | Text blocked                        | The recipient's device or carrier is blocking SMS messages.                                                                                                                                            |
|          | Text delivered                      | The message is delivered to the specified location.                                                                                                                                                    |
|          | Text successful                     | The recipient's carrier successfully accepted the message.                                                                                                                                             |
|          | Text queued                         | The message is queued and ready to be delivered to the recipient.                                                                                                                                      |
|          | Text pending                        | The message hasn't yet been delivered.                                                                                                                                                                 |
|          | Text TTL expired                    | The SMS message couldn't be delivered within the specified time frame.                                                                                                                                 |
|          | Text carrier unreachable            | An issue with the mobile network prevented the message from being delivered. This error is usually temporary.                                                                                          |
|          | Text invalid message                | The body of the SMS message is invalid. For example, the message doesn't meet the content or format requirements and can't be delivered.                                                               |
|          | Text carrier blocked                | The carrier has blocked delivery of this message. This often occurs when the carrier identifies the contents of the message as unsolicited or malicious.                                               |
|          | Text spam                           | The mobile carrier identified the contents of the message as spam and blocked delivery.                                                                                                                |
|          | Text unknown                        | An error occurred that prevented the delivery of the message. This error is usually temporary.                                                                                                         |
| Voice    | Voicemail beep                      | The number dialed was answered by voicemail with a beep.                                                                                                                                               |
|          | Voicemail no beep                   | The number dialed was answered by voicemail with no beep.                                                                                                                                              |
|          | AMD unanswered                      | The number dialed kept ringing, but no one answered.                                                                                                                                                   |
|          | Sit tone busy                       | The number dialed was busy.                                                                                                                                                                            |
|          | Sit tone invalid number             | The number dialed was not a valid number.                                                                                                                                                              |
|          | Human answered                      | The number dialed was answered by a person.                                                                                                                                                            |
|          | AMD unresolved                      | The number dialed connected, but answering machine detection could not determine whether a person or voicemail answered.                                                                               |
|          | AMD unresolved\_silence             | The number dialed was connected but the answering machine detection observed silence.                                                                                                                  |
|          | AMD not applicable                  | The call disconnected before ringing, and there was no media to detect.                                                                                                                                |
|          | Sit tone detected                   | A special information tone (SIT) was detected.                                                                                                                                                         |
|          | Fax machine detected                | A fax machine was detected.                                                                                                                                                                            |
|          | AMD error                           | The number dialed was connected, but there was an error in answering machine detection.                                                                                                                |
|          | Outbound destination endpoint error | Current configurations do not allow this destination to be dialed (for example, calling an endpoint destination from an ineligible instance).                                                          |
|          | Outbound resource error             | The instance has insufficient permissions to make outbound calls, or the necessary resources were not found.                                                                                           |
|          | Outbound attempt failed             | There was an unknown error, invalid parameter, or insufficient permissions to call the API.                                                                                                            |
|          | Outbound preview discarded          | No contact was made. The recipient was removed from the list. The system does not automatically retry.                                                                                                 |
|          | AMD disabled                        | Answering machine detection is disabled.                                                                                                                                                               |
|          | Initiated                           | An outbound call was initiated or transferred.                                                                                                                                                         |
|          | Connected to System                 | The contact established media—for example, a person or voicemail answered. Amazon Connect generates this event for any of the AnsweringMachineDetectionStatus codes.                                   |
|          | Contact data updated                | One or more contact properties were updated on an outbound call. Updated properties can include user-defined attributes and tags, routing criteria updates, or conversational analytics configuration. |
|          | Queued                              | An outbound call is queued to be assigned to an agent.                                                                                                                                                 |
|          | Connected to agent                  | An outbound call is connected to an agent.                                                                                                                                                             |
|          | Disconnected                        | The voice call disconnected. Possible reasons include a failed dial attempt, an unanswered call, or a detected SIT tone.                                                                               |
|          | Completed                           | The contact has fully ended, including After Contact Work (ACW) if applicable.                                                                                                                         |
| Email    | Bounce                              | An issue related to the email or server prevented delivery of the message.                                                                                                                             |
|          | Complaint                           | The message was received but the recipient marked it as spam.                                                                                                                                          |
|          | Delivery                            | The message is delivered.                                                                                                                                                                              |
|          | Send                                | Amazon Connect accepted the message and attempted to deliver it.                                                                                                                                       |
|          | Reject                              | Amazon Connect detected malware and rejected the message.                                                                                                                                              |
|          | Open                                | The message was received and the recipient opened it.                                                                                                                                                  |
|          | Click                               | The message was received and the recipient clicked a link in it.                                                                                                                                       |
|          | Rendering Failure                   | The email wasn't sent because of a template rendering issue.                                                                                                                                           |
|          | DeliveryDelay                       | A temporary error occurred that delayed delivery of the message. Amazon Connect systematically reattempts message delivery.                                                                            |
|          | Subscription                        | The email was successfully delivered, but the recipient updated the subscription preferences.                                                                                                          |
