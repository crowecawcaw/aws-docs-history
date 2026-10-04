

# How to get set up
<a name="nx-mms-get-set-up"></a>

This topic takes you from a new AWS account to sending your first MMS (multimedia) message with AWS End User Messaging. Complete the following steps.


**Setup steps**  

| Step | What you do | 
| --- | --- | 
| [Prerequisites](nx-mms-get-set-up-prerequisites.md) | Set up your AWS account, IAM permissions, and the AWS CLI. | 
| [Step 1: Get an MMS-capable phone number](nx-mms-get-set-up-identities.md) | Request an MMS-capable phone number for your destination country. | 
| [Step 2: Store your media in Amazon S3](nx-mms-gsu-media.md) | Store the image, audio, or video files you send in Amazon S3. | 
| [Step 3: Set up a phone pool](nx-mms-get-set-up-pool.md) | Create a phone pool with your number so that you send through one managed identity. | 

**Note**  
When you create a new AWS End User Messaging account, your SMS, MMS, and voice channels are placed in a sandbox until you request production access. In the sandbox you have access to all of the features of AWS End User Messaging, with restrictions on the volume and destinations of the messages you can send. For more information about the sandbox and how to move to production, see [Move out of the sandbox](nx-mms-scale-sandbox.md).