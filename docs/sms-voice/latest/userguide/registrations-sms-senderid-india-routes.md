

# Understanding international and local routes for India
<a name="registrations-sms-senderid-india-routes"></a>

**International routes (ILDO)**

By default, when you send messages to recipients in India, AWS End User Messaging SMS uses International Long-Distance Operator (ILDO) routes to transmit those messages. When recipients see a message sent over an ILDO connection, it appears to be sent from a random shared short code (unless you purchase a dedicated short code). International SMS to India is delivered via short codes rather than alphabetic sender IDs.

International routes are *not* subject to any AWS Region restriction. You can send messages to India over international routes—whether using a shared or dedicated short code—from any AWS Region where AWS End User Messaging SMS is available.

**Local routes (DLT-registered sender IDs)**

Companies that are registered in India can also use dedicated alphabetic sender IDs to send their messages. If you prefer to use a sender ID, you must send those messages over local routes rather than ILDO routes. Local routes require you to complete the DLT registration process described on this page.

**Important**  
AWS End User Messaging SMS only supports local India routes through AWS regions AP-SOUTH-1 Asia Pacific (Mumbai) and AP-SOUTH-2 Asia Pacific (Hyderabad). This restriction applies to local routes that use DLT-registered sender IDs. It does not apply to international routes or short codes, which can be used from any AWS Region.

**Cost comparison**

**Note**  
The price for sending messages using international (ILDO) routes is significantly higher than the price for sending messages through local routes. For current pricing for both route types, see the [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/) page.