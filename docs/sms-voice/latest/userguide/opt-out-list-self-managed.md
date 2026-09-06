

# Self managed opt-outs
<a name="opt-out-list-self-managed"></a>

By default, when a customer sends a message that begins with *HELP* or *STOP* to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message. In the case of incoming STOP messages, AWS End User Messaging SMS also opts the customer out of receiving future SMS messages. If you prefer to manage HELP and STOP responses by using a service other than AWS End User Messaging SMS, you can enable self-managed opt-outs. 

When you enable this feature, there are three changes to the way that AWS End User Messaging SMS handles incoming messages that your customers sends. First, it stops sending automatic responses to incoming HELP and STOP messages. Second, AWS End User Messaging SMS stops automatically opting your customers out of receiving future SMS and MMS messages when they send a STOP message. And finally, it routes incoming HELP and STOP messages to the Amazon SNS topic that you use to receive two-way SMS messages, rather than responding to the sender automatically. 

If you enable this feature, you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.

**Important**  
Many countries, regions, and jurisdictions impose severe penalties for sending unwanted SMS messages. If you enable this feature, make sure you have systems and processes in place for capturing and managing opt-out requests.

**Note**  
To enable self-managed opt-outs for a pool or phone number, you must first enable two-way SMS messaging. Self-managed opt-outs are supported when using Connect Customer for two-way SMS. For more information on using Connect Customer with two-way SMS messaging, see [Set up SMS messaging](https://docs.aws.amazon.com/connect/latest/adminguide/setup-sms-messaging.html) in the *Connect Customer administrator guide*.