# SMS and MMS limits and restrictions

The SMS protocol is subject to several limitations and restrictions. For example, there are
technical limitations that limit the length of each SMS message and MMS has limitations on the
size of the media file and length of the message body. There are also restrictions on the type of
content that you can send using SMS and MMS. This topic discusses several of these limitations and
restrictions.

When you're setting up SMS and MMS messaging in AWS End User Messaging SMS, you must consider these limitations
and restrictions. As a best practice, you should also implement the techniques discussed in [SMS and MMS best practices](best-practices.md#best-practices-sms "best-practices.md#best-practices-sms").

###### Topics

- [SMS character limits](sms-limitations-character.md "sms-limitations-character.md")
- [MMS file types, size and character limits](mms-limitations-character.md "mms-limitations-character.md")
- [Message Parts per Second (MPS)
  limits](sms-limitations-mps.md "sms-limitations-mps.md")
- [Message routes](#channels-sms-limitations-routes "#channels-sms-limitations-routes")

## Differences between message type and message routes

Messages sent through AWS End User Messaging SMS can either be promotional or transactional. A
promotional message type is typically comprised of marketing or sales-related messages. Some
countries or regions have quiet time hours when you're not permitted to send promotional
messages. A transactional message type is for more time-sensitive messages, such as password
resets or one-time passwords.

You pass the message type as an optional parameter using the [SendTextMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md") operation of the AWS End User Messaging SMS and voice v2 API. In
some cases you might use a sender ID as the originator, or you might have a shared pool of
numbers. If you have both transactional and promotional numbers associated with your account
for the destination country, AWS End User Messaging SMS chooses a transactional number by default. Delivery
receipts and the Delivery dashboard show the route as either promotional or transactional,
based on the chosen number.
