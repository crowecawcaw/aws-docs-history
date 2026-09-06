

# Event types for SMS, MMS, and voice
<a name="configuration-sets-event-types"></a>

The easiest way to use event destinations is to send all SMS, MMS and voice events to a single destination. However, you can configure event destinations so that specific types of events are sent to different destinations. For example, you could send all delivery-related events to Firehose for storage, and all failure events to an Amazon SNS topic so that you can be notified when they occur. You can also send SMS events and voice events to different locations.

You can configure event destinations to send the following types of events:

**SMS, MMS, and Voice events**
+ **ALL** – Sends all SMS, MMS, and voice events to the specified destination.

**SMS events**
+ **TEXT\_ALL** – Sends all SMS events to the specified destination.
+ **TEXT\_DELIVERED (Delivered)** – Sends all SMS delivery events to the specified destination. Depending on the destination country the **TEXT\_DELIVERED** and **TEXT\_SUCCESSFUL** events may be used interchangeably.
+ **TEXT\_SUCCESSFUL (Successful)** – Success events occur when the message is accepted by the recipient's carrier. Depending on the destination country the **TEXT\_DELIVERED** and **TEXT\_SUCCESSFUL** events may be used interchangeably.
+ **TEXT\_QUEUED (Queued)** – Queued events occur when the message is queued for delivery, but not delivered yet.
+ **TEXT\_PENDING (Pending)** – Pending events occur when a message is in the process of being delivered, but hasn't been delivered (or failed to be delivered) yet.
+ **TEXT\_BLOCKED (Blocked)** – Blocked events occur when the recipient's device or carrier is blocking messages to that recipient.
+ **TEXT\_TTL\_EXPIRED (TTL expired)** – TTL Expired events occur when the time required to deliver the message exceeds the `TTL` value that you specified when you sent the message.
+ **TEXT\_CARRIER\_UNREACHABLE (Carrier unreachable)** – Carrier Unreachable events occur when a transient error occurs on the carrier network of the message recipient.
+ **TEXT\_INVALID (SMS invalid)** – Invalid events occur when the destination phone number is not valid.
+ **TEXT\_INVALID\_MESSAGE (Invalid message)** – Invalid message events occur when the body of the SMS message is invalid and can't be delivered.
+ **TEXT\_CARRIER\_BLOCKED (Carrier blocked)** – Carrier blocked events occur when the recipient's carrier blocks the delivery of the message. This typically occurs when the carrier identifies the message as malicious (for example, if the message contains information related to a phishing scam) or abusive (for example, if the message is suspected of being unsolicited or prohibited content).
+ **TEXT\_UNREACHABLE (Unreachable)** – Unreachable events occur when the recipient's device is unavailable. This might occur if the device is not connected to a mobile network, or is powered off.
+ **TEXT\_SPAM (Spam)** – Spam events occur when the recipient's carrier identifies the message as containing unsolicited commercial content and blocks the delivery of the message.
+ **TEXT\_UNKNOWN (Unknown)** – Unknown events occur when a message fails to be delivered for a reason that isn't covered by one of the other event types. Unknown errors might be transient or permanent.
+ **TEXT\_PROTECT\_BLOCKED (Protect Blocked)** – Message blocked by protect configuration.

**Voice events**
+ **VOICE\_ALL** – Sends all voice events to the specified destination.
+ **VOICE\_COMPLETED (Completed)** – Completed events occur when the audio message is played to the recipient. This status doesn't necessarily mean that the message was delivered to a human recipient. For example, it could indicate that the message was delivered to a voicemail system.
+ **VOICE\_ANSWERED (Answered)** – Answered events occur when the recipient answers the phone. 
+ **VOICE\_INITIATED (Initiated)** – Sends events to the specified destination each time a voice message is initiated.
+ **VOICE\_TTL\_EXPIRED (TTL expired)** – TTL Expired events occur when the time required to deliver the message exceeds the `TTL` value that you specified when you sent the message.
+ **VOICE\_BUSY (Busy)** – Busy events occur when the recipient's phone line is busy.
+ **VOICE\_NO\_ANSWER (No answer)** – No answer events occur after the call has been placed, but the recipient (or their voicemail system) never answer.
+ **VOICE\_RINGING (Ringing)** – Ringing events occur after the call has been placed, but before the recipient answers.
+ **VOICE\_FAILED (Failed)** – Failure events occur when the message fails to be delivered.

**MMS events**
+ **MEDIA\_ALL** – Sends all MMS events to the specified destination.
+ **MEDIA\_PENDING (Pending)** – Pending events occur when a message is in the process of being delivered, but hasn't been delivered (or failed to be delivered) yet.
+ **MEDIA\_QUEUED (Queue)** – Queued events occur when the message is queued for delivery, but not delivered yet.
+ **MEDIA\_SUCCESSFUL (Successful)** – Success events occur when the message is accepted by the recipient's carrier.
+ **MEDIA\_DELIVERED (Delivered)** – Sends all MMS delivery events to the specified destination.
+ **MEDIA\_INVALID (MMS invalid)** – Invalid events occur when the destination phone number is not valid.
+ **MEDIA\_INVALID\_MESSAGE (Invalid message)** – Invalid message events occur when the body of the MMS message is invalid and can't be delivered.
+ **MEDIA\_UNREACHABLE (Unreachable)** – Unreachable events occur when the recipient's device is unavailable. This might occur if the device is not connected to a mobile network, or is powered off.
+ **MEDIA\_CARRIER\_UNREACHABLE (Carrier unreachable)** – Carrier Unreachable events occur when a transient error occurs on the carrier network of the message recipient.
+ **MEDIA\_BLOCKED (Blocked)** – Blocked events occur when the recipient's device or carrier is blocking messages to that recipient.
+ **MEDIA\_CARRIER\_BLOCKED (Carrier blocked)** – Carrier blocked events occur when the recipient's carrier blocks the delivery of the message. This typically occurs when the carrier identifies the message as malicious (for example, if the message contains information related to a phishing scam) or abusive (for example, if the message is suspected of being unsolicited or prohibited content).
+ **MEDIA\_SPAM (Spam)** – Spam events occur when the recipient's carrier identifies the message as containing unsolicited commercial content and blocks the delivery of the message.
+ **MEDIA\_UNKNOWN (Unknown)** – Unknown events occur when a message fails to be delivered for a reason that isn't covered by one of the other event types. Unknown errors might be transient or permanent.
+ **MEDIA\_TTL\_EXPIRED (TTL expired)** – TTL Expired events occur when the time required to deliver the message exceeds the `TTL` value that you specified when you sent the message.
+ **MEDIA\_FILE\_TYPE\_UNSUPPORTED (File type unsupported)** – File type unsupported events occur when a media file is not in a supported format. For a list of supported file types, see [MMS file types, size and character limits](mms-limitations-character.md)
+ **MEDIA\_FILE\_SIZE\_EXCEEDED (File size)** – File size exceeded event occur when the media file is larger than 600 KB in size.
+ **MEDIA\_FILE\_INACCESSIBLE (File inaccessible)** – File inaccessible events occur when AWS End User Messaging SMS doesn't have permissions to access the file.