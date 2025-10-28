# Event types for SMS, MMS, and

voice

The easiest way to use event destinations is to send all SMS, MMS and voice events to
a single destination. However, you can configure event destinations so that specific
types of events are sent to different destinations. For example, you could send all
delivery-related events to Firehose for storage, and all failure events to an Amazon SNS topic
so that you can be notified when they occur. You can also send SMS events and voice
events to different locations.

You can configure event destinations to send the following types of events:

###### SMS, MMS, and Voice events

- **ALL** – Sends all SMS, MMS, and voice
  events to the specified destination.

###### SMS events

- **TEXT_ALL** – Sends all SMS events to the
  specified destination.
- **TEXT_DELIVERED (Delivered)** – Sends all
  SMS delivery events to the specified destination. Depending on the destination
  country the **TEXT_DELIVERED** and **TEXT_SUCCESSFUL** events may be used
  interchangeably.
- **TEXT_SUCCESSFUL (Successful)** – Success
  events occur when the message is accepted by the recipient's carrier. Depending
  on the destination country the **TEXT_DELIVERED**
  and **TEXT_SUCCESSFUL** events may be used
  interchangeably.
- **TEXT_QUEUED (Queued)** – Queued events
  occur when the message is queued for delivery, but not delivered yet.
- **TEXT_PENDING (Pending)** – Pending events
  occur when a message is in the process of being delivered, but hasn't been
  delivered (or failed to be delivered) yet.
- **TEXT_BLOCKED (Blocked)** – Blocked events
  occur when the recipient's device or carrier is blocking messages to that
  recipient.
- **TEXT_TTL_EXPIRED (TTL expired)** – TTL
  Expired events occur when the time required to deliver the message exceeds the
  `TTL` value that you specified when you sent the message.
- **TEXT_CARRIER_UNREACHABLE (Carrier
  unreachable)** – Carrier Unreachable events occur when a
  transient error occurs on the carrier network of the message recipient.
- **TEXT_INVALID (SMS invalid)** – Invalid
  events occur when the destination phone number is not valid.
- **TEXT_INVALID_MESSAGE (Invalid message)**
  – Invalid message events occur when the body of the SMS message is invalid
  and can't be delivered.
- **TEXT_CARRIER_BLOCKED (Carrier blocked)**
  – Carrier blocked events occur when the recipient's carrier blocks the
  delivery of the message. This typically occurs when the carrier identifies the
  message as malicious (for example, if the message contains information related
  to a phishing scam) or abusive (for example, if the message is suspected of
  being unsolicited or prohibited content).
- **TEXT_UNREACHABLE (Unreachable)** –
  Unreachable events occur when the recipient's device is unavailable. This might
  occur if the device is not connected to a mobile network, or is powered
  off.
- **TEXT_SPAM (Spam)** – Spam events occur
  when the recipient's carrier identifies the message as containing unsolicited
  commercial content and blocks the delivery of the message.
- **TEXT_UNKNOWN (Unknown)** – Unknown events
  occur when a message fails to be delivered for a reason that isn't covered by
  one of the other event types. Unknown errors might be transient or
  permanent.
- **TEXT_PROTECT_BLOCKED (Protect Blocked)**
  – Message blocked by protect configuration.

###### Voice events

- **VOICE_ALL** – Sends all voice events to
  the specified destination.
- **VOICE_COMPLETED (Completed)** – Completed
  events occur when the audio message is played to the recipient. This status
  doesn't necessarily mean that the message was delivered to a human recipient.
  For example, it could indicate that the message was delivered to a voicemail
  system.
- **VOICE_ANSWERED (Answered)** – Answered
  events occur when the recipient answers the phone.
- **VOICE_INITIATED (Initiated)** – Sends
  events to the specified destination each time a voice message is
  initiated.
- **VOICE_TTL_EXPIRED (TTL expired)** – TTL
  Expired events occur when the time required to deliver the message exceeds the
  `TTL` value that you specified when you sent the message.
- **VOICE_BUSY (Busy)** – Busy events occur
  when the recipient's phone line is busy.
- **VOICE_NO_ANSWER (No answer)** – No answer
  events occur after the call has been placed, but the recipient (or their
  voicemail system) never answer.
- **VOICE_RINGING (Ringing)** – Ringing
  events occur after the call has been placed, but before the recipient
  answers.
- **VOICE_FAILED (Failed)** – Failure events
  occur when the message fails to be delivered.

###### MMS events

- **MEDIA_ALL** – Sends all MMS events to the
  specified destination.
- **MEDIA_PENDING (Pending)** – Pending
  events occur when a message is in the process of being delivered, but hasn't
  been delivered (or failed to be delivered) yet.
- **MEDIA_QUEUED (Queue)** – Queued events
  occur when the message is queued for delivery, but not delivered yet.
- **MEDIA_SUCCESSFUL (Successful)** – Success
  events occur when the message is accepted by the recipient's carrier.
- **MEDIA_DELIVERED (Delivered)** – Sends all
  MMS delivery events to the specified destination.
- **MEDIA_INVALID (MMS invalid)** – Invalid
  events occur when the destination phone number is not valid.
- **MEDIA_INVALID_MESSAGE (Invalid message)**
  – Invalid message events occur when the body of the MMS message is invalid
  and can't be delivered.
- **MEDIA_UNREACHABLE (Unreachable)** –
  Unreachable events occur when the recipient's device is unavailable. This might
  occur if the device is not connected to a mobile network, or is powered
  off.
- **MEDIA_CARRIER_UNREACHABLE (Carrier
  unreachable)** – Carrier Unreachable events occur when a
  transient error occurs on the carrier network of the message recipient.
- **MEDIA_BLOCKED (Blocked)** – Blocked
  events occur when the recipient's device or carrier is blocking messages to that
  recipient.
- **MEDIA_CARRIER_BLOCKED (Carrier blocked)**
  – Carrier blocked events occur when the recipient's carrier blocks the
  delivery of the message. This typically occurs when the carrier identifies the
  message as malicious (for example, if the message contains information related
  to a phishing scam) or abusive (for example, if the message is suspected of
  being unsolicited or prohibited content).
- **MEDIA_SPAM (Spam)** – Spam events occur
  when the recipient's carrier identifies the message as containing unsolicited
  commercial content and blocks the delivery of the message.
- **MEDIA_UNKNOWN (Unknown)** – Unknown
  events occur when a message fails to be delivered for a reason that isn't
  covered by one of the other event types. Unknown errors might be transient or
  permanent.
- **MEDIA_TTL_EXPIRED (TTL expired)** – TTL
  Expired events occur when the time required to deliver the message exceeds the
  `TTL` value that you specified when you sent the message.
- **MEDIA_FILE_TYPE_UNSUPPORTED (File type
  unsupported)** – File type unsupported events occur when a
  media file is not in a supported format. For a list of supported file types, see
  [MMS file types, size and character limits](mms-limitations-character.md "mms-limitations-character.md")
- **MEDIA_FILE_SIZE_EXCEEDED (File size)** –
  File size exceeded event occur when the media file is larger than 600 KB in
  size.
- **MEDIA_FILE_INACCESSIBLE (File inaccessible)**
  – File inaccessible events occur when AWS End User Messaging SMS doesn't have permissions to
  access the file.
