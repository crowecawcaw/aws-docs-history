

# Working with shared resources in AWS End User Messaging SMS
<a name="shared-resources"></a>

AWS End User Messaging SMS integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a service that enables you to share some AWS End User Messaging SMS resources with other AWS accounts or through AWS Organizations. With AWS RAM, you share resources that you own by creating a *resource share*. A resource share specifies the resources to share, and the consumers with whom to share them. Consumers can include:
+ Specific AWS accounts inside or outside of its organization in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ Its entire organization in AWS Organizations
+ Other AWS Services like Amazon Pinpoint or Amazon SNS

For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)*.

This topic explains how to share resources that you own, and how to use resources that are shared with you.

**Important**  
Shared resources (phone numbers, sender IDs, pools, and opt-out lists) accessed via AWS RAM can only be used with the AWS End User Messaging SMS API (for example, the [SendTextMessage](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-text-message.html) action). They are not supported with:  
Amazon SNS (`Publish` API for SMS)
Amazon Pinpoint (`SendMessages` API)
The AWS End User Messaging SMS console
To send from a shared resource, use the AWS CLI or an with the full Amazon Resource Name (ARN) of the resource in the `SendTextMessage` API call.

**Important**  
Sharing origination identities with other AWS accounts does not grant those accounts permission to send messages to China. Each AWS account must be individually allowlisted for sending to China, regardless of whether the origination identity is owned or shared via AWS RAM. If a consuming account attempts to send to China using a shared origination identity without its own China allowlisting, the request will fail with a `DESTINATION_COUNTRY_BLOCKED` validation error.  
To request China allowlisting for an account, open a case with AWS Support. For more information, see [Requesting support for SMS, MMS, and voice messaging through Support](awssupport.md).

**Topics**
+ [Prerequisites for sharing phone number, pool, opt-out list, or sender IDs](#sharing-prereqs)
+ [Sharing a phone number, pool, opt-out list, or sender ID](#sharing-share)
+ [Unsharing a shared phone number, pool, opt-out list, or sender ID](#sharing-unshare)
+ [Identifying a shared phone number, pool, opt-out list, or sender ID](#sharing-identify)
+ [Responsibilities and permissions for shared phone number, pool, opt-out list, or sender IDs](#sharing-perms)
+ [Billing and metering](#sharing-billing)
+ [Instance quotas](#sharing-quotas)
+ [Example policies for sharing a sender ID or phone number with Amazon Pinpoint](#sharing-policy-example)
+ [Example policy for sharing a sender ID with Amazon Pinpoint and Amazon SNS](#sharing-policy-example-sender-id)
+ [Example policy for sharing a phone number with Amazon Pinpoint and Amazon SNS](#sharing-policy-example-phone-number)

## Prerequisites for sharing phone number, pool, opt-out list, or sender IDs
<a name="sharing-prereqs"></a>
+ To share a phone number, pool, opt-out list, or sender ID, you must own it in your AWS account. This means that the resource must be allocated or provisioned in your account. You cannot share a phone number, pool, opt-out list, or sender ID that has been shared with you.
+ To share a phone number, pool, opt-out list, or sender ID with your organization or an organizational unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

## Sharing a phone number, pool, opt-out list, or sender ID
<a name="sharing-share"></a>

When you share a resources that you own with other AWS accounts, you enable them to do the following: 
+ **Opt-Out List** – Consumers with access to this resource can check the status of a phone number, remove a phone number, and add phone numbers to the opt-out list.
+ **PhoneNumber** – Consumers with access to this resource can use the phone number to send messages.
+ **Pool** – Consumers with access to this resource can view the pool. Any resources contained in the pool must also be shared for other AWS accounts to be able to access them. You can have a mix of shared and unshared resources in a pool.
+ **Sender ID** – Consumers with access to this resource can use the Sender Id to send messages.

To share a phone number, pool, opt-out list, or sender ID, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared. When you share a phone number, pool, opt-out list, or sender ID using the AWS End User Messaging SMS console, you add it to an existing resource share. To add the phone number, pool, opt-out list, or sender ID to a new resource share, you must first create the resource share using the [AWS RAM console](https://console.aws.amazon.com/ram).

If you are part of an organization in AWS Organizations and sharing within your organization is enabled, consumers in your organization are automatically granted access to the shared phone number, pool, opt-out list, or sender ID. Otherwise, consumers receive an invitation to join the resource share and are granted access to the shared phone number, pool, opt-out list, or sender ID after accepting the invitation.

You can share a phone number, pool, opt-out list, or sender ID that you own using the AWS End User Messaging SMS console, AWS RAM console, or the AWS CLI.

**Note**  
Shared resources can only be used through the AWS CLI or [AWS End User Messaging SMS and Voice v2 API](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/Welcome.html). You must use the full Amazon Resource Name (ARN) of the shared resource. Sending via Amazon SNS, Amazon Pinpoint, or the AWS End User Messaging SMS console is not supported for shared resources.  
To view resources shared with your account you must use the AWS CLI or the [AWS RAM console](https://console.aws.amazon.com/ram).

We recommend using the [AWS RAM console](https://console.aws.amazon.com/ram) to share resources.

**To share a phone number, pool, opt-out list, or sender ID that you own using the AWS End User Messaging SMS console**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose the resource type and then resource.

1. On the **Resource policy** tab, choose **Edit**.

1. You can edit the JSON resource based policy to change sharing permissions.

1. Choose **Save changes**.

**To share a phone number, pool, opt-out list, or sender ID that you own using the AWS RAM console**  
See [Creating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

**To share a phone number, pool, opt-out list, or sender ID that you own using the AWS CLI**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command.

## Unsharing a shared phone number, pool, opt-out list, or sender ID
<a name="sharing-unshare"></a>

When a resource owner stops sharing a phone number, pool, opt-out list, or sender ID with a consumer, the resource no longer appears in the consumer's console.

To unshare a shared phone number, pool, opt-out list, or sender ID that you own, you must remove it from the resource share. You can do this using the AWS End User Messaging SMS console, AWS RAM console, or the AWS CLI.

**To unshare a shared phone number, pool, opt-out list, or sender ID that you own using the AWS RAM console**  
See [Updating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared phone number, pool, opt-out list, or sender ID that you own using the AWS CLI**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

## Identifying a shared phone number, pool, opt-out list, or sender ID
<a name="sharing-identify"></a>

Owners and consumers can identify shared phone number, pool, opt-out list, or sender IDs using the AWS CLI.

**Note**  
Phone numbers, pools, opt-out list, and sender IDs are generally not identifiable as a shared resource in the AWS End User Messaging SMS console. 

**To identify a shared phone number, pool, opt-out list, or sender ID using the AWS CLI**  
Use the [describe-opt-out-lists](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.html), [describe-phone-numbers](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-phone-numbers.html), [describe-pools](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-pools.html), or [describe-sender-ids](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-sender-ids.html) command with the `Owner` parameter set to `SHARED`. The command returns the phone number, pool, opt-out list, or sender IDs that are shared with you. 

## Responsibilities and permissions for shared phone number, pool, opt-out list, or sender IDs
<a name="sharing-perms"></a>

### Permissions for owners
<a name="perms-owner"></a>

Owners can update, view, share, stop sharing, and use phone number, pool, opt-out list, or sender IDs. 

### Permissions for consumers
<a name="perms-consumer"></a>

Consumers can use and view phone number, pool, opt-out list, or sender IDs. 

## Billing and metering
<a name="sharing-billing"></a>

The owner of the resource is billed for the resource. Consumers aren't billed for resources shared with them but are billed for using resources to send messages. There aren't extra costs associated with sharing a resource.

Consumers are billed for sending a message with [send-text-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-text-message.html), [send-media-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.html) or [send-voice-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-voice-message.html) and this counts against the consumers spending limits. For more information about pricing or spending limits, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/) and [Set an SMS, MMS or voice spending limit in AWS End User Messaging SMS](spend-limit.md).

## Instance quotas
<a name="sharing-quotas"></a>

Sharing a resource doesn't affect the limits of the resource in the owner's or consumer's account. Only the owner's account is used to calculate the limits of the resource.

## Example policies for sharing a sender ID or phone number with Amazon Pinpoint
<a name="sharing-policy-example"></a>

We recommend that you use the [AWS RAM console](https://console.aws.amazon.com/ram) to create and manage resource shares. 

The following example allows Amazon Pinpoint to send SMS or Voice messages with the specified phone number. 

**To share a phone number that you own using the AWS End User Messaging SMS console**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers** and then choose a phone number.

1. On the **Resource policy** tab, choose **Edit**.

1. You can edit the JSON resource based policy to change sharing permissions.

   In the following JSON, make the following changes and then paste the JSON to the **Resource policy**:
   + Replace {{Partition}} with the AWS partition the phone number is in.
   + Replace {{Region}} with the AWS Region the phone number is in.
   + Replace {{Account}} with the account number that owns the phone number.
   + Replace {{Phone-id}} with the identifier of the phone number.

1. Choose **Save changes**.

The following example allows Amazon Pinpoint to send SMS messages with the specified sender ID. 

**To share a Sender ID that you own using the AWS End User Messaging SMS console**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Sender IDs** and then choose a sender ID.

1. On the **Resource policy** tab, choose **Edit**.

1. You can edit the JSON resource based policy to change sharing permissions.

   In the following JSON, make the following changes and then paste the JSON to the **Resource policy**:
   + Replace {{Partition}} with the AWS partition the sender ID is in.
   + Replace {{Region}} with the AWS Region the sender ID is in.
   + Replace {{Account}} with the account number that owns the sender ID.
   + Replace {{Senderid}} with the identifier of the sender ID.
   + Replace {{Countrycode}} with the two-letter ISO-3166 alpha-2 code for the country of the sender ID.

1. Choose **Save changes**.

## Example policy for sharing a sender ID with Amazon Pinpoint and Amazon SNS
<a name="sharing-policy-example-sender-id"></a>

We recommend that you use the [AWS RAM console](https://console.aws.amazon.com/ram) to create and manage resource shares. 

The following example allows Amazon Pinpoint and Amazon SNS to send SMS messages with the specified sender ID. 

**To share a sender ID that you own using the AWS End User Messaging SMS console**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Sender IDs** and then choose a sender ID.

1. On the **Resource policy** tab, choose **Edit**.

1. You can edit the JSON resource based policy to change sharing permissions.

   In the following JSON, make the following changes and then paste the JSON to the **Resource policy**:
   + Replace {{Partition}} with the AWS partition the phone number is in.
   + Replace {{Region}} with the AWS Region the phone number is in.
   + Replace {{OwnersAccountID}} with the AWS account number that owns the sender ID.
   + Replace {{SenderID}} with the identifier of the sender ID.
   + Replace {{ISO}} with the two-letter ISO-3166 alpha-2 code for the country of the sender ID.
   + Replace {{ConsumersAccountID}} with the AWS account number to give access to.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "pinpoint.amazonaws.com"
               },
               "Action": [
                   "sms-voice:SendTextMessage",
                   "sms-voice:SendVoiceMessage"
               ],
               "Resource": "arn:aws:sms-voice:{{us-east-1}}:{{111122223333}}:sender-id/{{SenderID}}/{{ISO}}",
               "Condition": {
                   "StringEquals": {
                   "aws:SourceAccount": "{{111122223333}}"
                   }
               }
           },
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "sns.amazonaws.com"
               },
               "Action": "sms-voice:SendTextMessage",
               "Resource": "arn:aws:sms-voice:{{us-east-1}}:{{111122223333}}:sender-id/{{SenderID}}/{{ISO}}",
               "Condition": {
                   "StringEquals": {
                   "aws:SourceAccount": "{{111122223333}}"
                   }
               }
           },
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{111122223333}}:root"
               },
               "Action": "sms-voice:SendTextMessage",
               "Resource": "arn:aws:sms-voice:{{us-east-1}}:{{111122223333}}:sender-id/{{SenderID}}/{{ISO}}"
           }
       ]
   }
   ```

------

1. Choose **Save changes**.

## Example policy for sharing a phone number with Amazon Pinpoint and Amazon SNS
<a name="sharing-policy-example-phone-number"></a>

We recommend that you use the [AWS RAM console](https://console.aws.amazon.com/ram) to create and manage resource shares. 

The following example allows Amazon Pinpoint and Amazon SNS to send SMS messages with the specified phone number. 

**To share a phone number that you own using the AWS End User Messaging SMS console**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers** and then choose a phone number.

1. On the **Resource policy** tab, choose **Edit**.

1. You can edit the JSON resource based policy to change sharing permissions.

   In the following JSON, make the following changes and then paste the JSON to the **Resource policy**:
   + Replace {{Partition}} with the AWS partition the phone number is in.
   + Replace {{Region}} with the AWS Region the phone number is in.
   + Replace {{OwnersAccountID}} with the AWS account number that owns the phone number.
   + Replace {{PhoneNumberID}} with the identifier of the phone number.
   + Replace {{ConsumersAccountID}} with the AWS account number to give access to.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "pinpoint.amazonaws.com"
               },
               "Action": [
                   "sms-voice:SendTextMessage",
                   "sms-voice:SendVoiceMessage"
               ],
               "Resource": "arn:aws:sms-voice:{{us-east-1}}:{{111122223333}}:phone-number/{{PhoneNumberID}}",
               "Condition": {
                   "StringEquals": {
                   "aws:SourceAccount": "{{111122223333}}"
                   }
               }
           },
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "sns.amazonaws.com"
               },
               "Action": "sms-voice:SendTextMessage",
               "Resource": "arn:aws:sms-voice:{{us-east-1}}:{{111122223333}}:phone-number/{{PhoneNumberID}}",
               "Condition": {
                   "StringEquals": {
                   "aws:SourceAccount": "{{111122223333}}"
                   }
               }
           },
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{111122223333}}:root"
               },
               "Action": "sms-voice:SendTextMessage",
               "Resource": "arn:aws:sms-voice:{{us-east-1}}:{{111122223333}}:phone-number/{{PhoneNumberID}}"
           }
       ]
   }
   ```

------

1. Choose **Save changes**.