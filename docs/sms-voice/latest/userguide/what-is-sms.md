# How Short Message Service (SMS) works

[Short Message Service](https://aws.amazon.com/what-is/sms/ "https://aws.amazon.com/what-is/sms/"), commonly known as SMS, is a service that allows the exchange of
text messages between mobile devices. SMS messages are typically short, with a maximum
length of 160 characters, supported by virtually all mobile devices, and can be sent and
received on various mobile networks. SMS is widely used for personal and business
communication, providing a quick and convenient way to send concise messages to individuals
or groups of people.

###### How does application to person (A2P) SMS work?

SMS uses the infrastructure that's already in place for voice calls, operating
on the signaling channels of mobile networks. Here's a simplified overview
of how SMS works:

1. **Application initiates a message**. The
   application creates a text message and addresses the message to the
   recipient's phone number. AWS receives the message request,
   processes the message.
2. **AWS sends the message to the Short Message
   Service Center (SMSC)**. An SMSC is a centralized
   server responsible for handling SMS messages.

AWS selects the appropriate SMS message route to deliver the message
to the end user’s mobile device. The selected SMS route may be an
intermediary that then routes the SMS message to the SMSC or the SMS
can be routed directly to the SMSC. This results in the message
leaving the AWS boundary and being delivered to the correct SMSC. 3. **SMSC delivers the message**. The SMSC
uses a series of signaling messages to send the message to the
recipient's mobile network. 4. **Message is stored**. The recipient's
SMSC receives the message and temporarily stores it until the
recipient's device is available to receive it. 5. **Recipient's device gets notified**.
When the recipient's device is reachable, the recipient's SMSC sends
a notification message indicating that a new SMS is
available. 6. **Message is retrieved**: The recipient's
mobile device connects to the recipient's SMSC to retrieve the
message. 7. **Message displays**: The recipient's
mobile device receives the message and displays it to the
recipient. 8. **Possible delivery confirmation**. The
recipient's mobile device might send a delivery receipt (DLR)
confirmation back to the sender's SMSC, indicating that the message
was successfully received. This DLR is then relayed back to AWS
who then passes it along to application owner.
