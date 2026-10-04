

# How to get set up
<a name="nx-sms-get-set-up"></a>

This topic takes you from a new AWS account to sending your first SMS message with AWS End User Messaging. Complete the following steps.


**Setup steps**  

| Step | What you do | 
| --- | --- | 
| [Prerequisites](nx-sms-get-set-up-prerequisites.md) | Set up your AWS account, IAM permissions, and the AWS CLI. | 
| [Step 1: Get a phone number](nx-sms-get-set-up-identities.md) | Request an origination identity, such as a phone number or sender ID, for your destination country. | 
| [Step 2: Set up a phone pool](nx-sms-get-set-up-pool.md) | Create a phone pool with your number so that you send through one managed identity. | 

**Note**  
When you create a new AWS End User Messaging account, your SMS, MMS, and voice channels are placed in a sandbox until you request production access. In the sandbox you have access to all of the features of AWS End User Messaging, with restrictions on the volume and destinations of the messages you can send. For more information about the sandbox and how to move to production, see [Move out of the sandbox](nx-sms-scale-sandbox.md).

**Tip**  
If you want to send one-time passwords or verification messages without managing your own phone numbers, you can use Notify. Notify lets you send templated messages using AWS-managed origination identities.