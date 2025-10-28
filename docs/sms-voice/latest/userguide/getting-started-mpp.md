# Message part preview

A single SMS message can contain up to 140 bytes of information. When a message contains
more than the maximum number of characters, the message is split into multiple parts. Depending
on the recipient's mobile carrier and device, multiple messages might be displayed as a single
message, or as a sequence of separate messages.

If your message uses only characters in the GSM 03.38 character set, also known as the GSM
7-bit alphabet, it can contain up to 160 characters. If your message contains any characters that
are outside the GSM 03.38 character set, it can have up to 70 characters. When you send an SMS
message, AWS End User Messaging SMS automatically determines the most efficient encoding to use.

You are billed for each message part that is sent. Phone numbers have a limit on the number
of message parts they can send each second. If your message is split into two message parts, you
are billed for each message part. Use the message part preview before you send your SMS message
to see how many message parts it is. For more information about supported character sets, see
[SMS character limits](sms-limitations-character.md "sms-limitations-character.md"). For more
information about message size and throughput, see [What are the Message Parts per Second (MPS)
limits](sms-limitations-mps.md "sms-limitations-mps.md").

###### Using the message part preview

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Shortcuts**, choose **Message
   part preview**.
3. In the **SMS message** section, enter your SMS message. As you enter the
   message, the **Part preview** displays the encoding, number of characters, and
   SMS message parts.
