

# Sender IDs in Amazon SNS
<a name="channels-sms-originating-identities-sender-ids"></a>

**Important**  
The Amazon SNS SMS Developer Guide has been updated. Amazon SNS has integrated with [AWS End User Messaging SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-service.html) for the delivery of SMS messages. This guide contains the latest information on how to create, configure, and manage your Amazon SNS SMS messages.

A sender ID is an alphabetic name that identifies the sender of an SMS message. When you send an SMS message using a sender ID, and the recipient is in an area where sender ID authentication is supported, your sender ID appears on the recipient’s device instead of a phone number. A sender ID provides SMS recipients with more information about the sender than a phone number, long code, or short code provides. For more information, see [Sender IDs](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id.html) in the *AWS End User Messaging SMS User Guide*.

Sender IDs are supported in several countries and regions around the world. In some places, if you're a business that sends SMS messages to individual customers, you must use a sender ID that's pre-registered with a regulatory agency or industry group. For a complete list of countries and regions that support or require sender IDs, see [Supported countries and regions for SMS messaging with AWS End User Messaging SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html) in the *AWS End User Messaging SMS User Guide*.

 For more information on sender IDs, see the following documentation in the *AWS End User Messaging SMS User Guide*:


| AWS End User Messaging SMS Topic | Description | 
| --- | --- | 
| [Manage sender IDs](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-request.html) | Before you request a sender ID verify that they are available, see [Supported countries and regions for SMS messaging with AWS End User Messaging SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html) in the *AWS End User Messaging SMS User Guide*. | 
| [Tags](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-tags-add.html) | Tags are pairs of keys and values that you can optionally apply to your AWS resources to control access or usage.  | 

**Topics**
+ [Amazon SNS Sender ID requirements for France](channels-sms-senderid-france.md)