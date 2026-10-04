

# Setup MMS
<a name="nx-mms"></a>

MMS (Multimedia Messaging Service) extends SMS so you can send images, audio, video, and longer text to recipients in the United States and Canada. Common use cases include sending product images and promotional creative, delivery and appointment visuals, media-rich alerts, and any notification where a picture or short video communicates more than text alone.

You send MMS with the AWS End User Messaging SMS and Voice v2 API (the `sms-voice` namespace, which you call as `aws pinpoint-sms-voice-v2` on the AWS CLI). The main send operation is `SendMediaMessage`, which sends a media message to a single destination phone number and references your media files by their Amazon S3 locations.

**Key concepts**


| Concept | Description | 
| --- | --- | 
| Origination identity | The phone number that an MMS message is sent from. MMS uses the same origination identities as SMS, such as long codes, toll-free numbers, short codes, and 10DLC. | 
| Media files in Amazon S3 | The images, audio, or video you send. You upload each file to an Amazon S3 bucket, grant AWS End User Messaging read access, and reference the file by its S3 location in the send request. | 
| Phone pool | A collection of origination identities that share the same settings, so AWS End User Messaging can select an identity and fail over if one is unavailable. | 
| Configuration set | A set of rules applied to the messages you send, including where to send delivery and engagement events. | 
| Opt-out list | A list of destination numbers that have opted out. AWS End User Messaging does not send to a number while it is on an opt-out list. | 

**How this guide is organized**

Use the following table to find where to start.


| Section | What you'll do | Start here if | 
| --- | --- | --- | 
| [How to get set up](nx-mms-get-set-up.md) | Set up an origination identity, prepare your media in Amazon S3, and send a test MMS message. | You are new to MMS and want a working test send. | 
| [Send a message](nx-mms-send.md) | Send media messages from your application. | You have an origination identity and want to send from your own code. | 
| [Scale](nx-mms-scale.md) | Move out of the sandbox, monitor delivery, and manage spending and quotas. | You are sending in production and want to keep it healthy and grow. | 