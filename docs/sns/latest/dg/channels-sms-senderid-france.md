

# Amazon SNS Sender ID requirements for France
<a name="channels-sms-senderid-france"></a>

This guide provides the steps and guidelines to create a dedicated Sender ID. French mobile carriers require this for sending SMS text messages to France.

**Topics**
+ [Setting up a dedicated Sender ID for France](#channels-sms-senderid-registration-france)
+ [Sender ID naming guidelines](#channels-sms-senderid-guidelines-france)

## Setting up a dedicated Sender ID for France
<a name="channels-sms-senderid-registration-france"></a>

You can use one of the following methods to set up a dedicated Sender ID. Amazon SNS uses the Sender ID for SMS messages published through the `Publish` API.
+ You can use the Amazon SNS console to configure the default Sender ID for all SMS messages published. To learn more, see [Setting SMS messaging preferences using the AWS Management Console](sms_preferences.md#sms_preferences_console).
+ You can use the `Publish` API to set the Sender ID using the `AWS.SNS.SMS.SenderID` message attribute when publishing an SMS message. To learn more, see [Sending a message (console)](sms_sending-overview.md#sms_publish_console).

## Sender ID naming guidelines
<a name="channels-sms-senderid-guidelines-france"></a>
+ The Sender ID name must be alphanumeric with a maximum of 11 characters.
+ The Sender ID name must not contain special characters or spaces.
+ We recommend using the same name for the Sender ID and the brand name of the company sending the SMS message.