

# Resource sharing
<a name="nx-features-resource-sharing"></a>

AWS End User Messaging integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a service that enables you to share some AWS End User Messaging resources with other AWS accounts or through AWS Organizations. With AWS RAM, you share resources that you own by creating a *resource share*. A resource share specifies the resources to share, and the consumers with whom to share them. Consumers can include:
+ Specific AWS accounts inside or outside of its organization in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ Its entire organization in AWS Organizations
+ Other AWS services like Amazon Pinpoint or Amazon SNS

For more information about AWS RAM, see the *AWS RAM User Guide*.

This topic explains how to share resources that you own, and how to use resources that are shared with you.

**Important**  
Shared resources (phone numbers, sender IDs, pools, and opt-out lists) accessed via AWS RAM can only be used with the AWS End User Messaging API (for example, the [SendTextMessage](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-text-message.html) action). They are not supported with:  
Amazon SNS (`Publish` API for SMS)
Amazon Pinpoint (`SendMessages` API)
The AWS End User Messaging console
To send from a shared resource, use the AWS CLI or an SDK with the full Amazon Resource Name (ARN) of the resource in the `SendTextMessage` API call.

**Important**  
Sharing origination identities with other AWS accounts does not grant those accounts permission to send messages to China. Each AWS account must be individually allowlisted for sending to China, regardless of whether the origination identity is owned or shared via AWS RAM. If a consuming account attempts to send to China using a shared origination identity without its own China allowlisting, the request will fail with a `DESTINATION_COUNTRY_BLOCKED` validation error.  
To request China allowlisting for an account, open a case with AWS Support. For more information, see Getting support for AWS End User Messaging SMS.

**Topics**
+ [Prerequisites for sharing resources](#nx-sharing-prereqs)
+ [Sharing a resource](#nx-sharing-share)
+ [Unsharing a shared resource](#nx-sharing-unshare)
+ [Identifying a shared resource](#nx-sharing-identify)
+ [Responsibilities and permissions for shared resources](#nx-sharing-perms)
+ [Billing and metering](#nx-sharing-billing)
+ [Instance quotas](#nx-sharing-quotas)

## Prerequisites for sharing resources
<a name="nx-sharing-prereqs"></a>
+ To share a phone number, pool, opt-out list, or sender ID, you must own it in your AWS account. This means that the resource must be allocated or provisioned in your account. You cannot share a resource that has been shared with you.
+ To share a resource with your organization or an organizational unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

## Sharing a resource
<a name="nx-sharing-share"></a>

When you share a resource that you own with other AWS accounts, you enable them to do the following:
+ **Opt-out list** – Consumers with access to this resource can check the status of a phone number, remove a phone number, and add phone numbers to the opt-out list.
+ **Phone number** – Consumers with access to this resource can use the phone number to send messages.
+ **Pool** – Consumers with access to this resource can view the pool. Any resources contained in the pool must also be shared for other AWS accounts to be able to access them. You can have a mix of shared and unshared resources in a pool.
+ **Sender ID** – Consumers with access to this resource can use the sender ID to send messages.

To share a resource, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared. When you share a resource using the AWS End User Messaging console, you add it to an existing resource share. To add the resource to a new resource share, you must first create the resource share using the [AWS RAM console](https://console.aws.amazon.com/ram).

If you are part of an organization in AWS Organizations and sharing within your organization is enabled, consumers in your organization are automatically granted access to the shared resource. Otherwise, consumers receive an invitation to join the resource share and are granted access to the shared resource after accepting the invitation.

You can share a resource that you own using the AWS End User Messaging console, AWS RAM console, or the AWS CLI.

**Note**  
Shared resources can only be used through the AWS CLI or [AWS End User Messaging and Voice v2 API](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/Welcome.html). You must use the full Amazon Resource Name (ARN) of the shared resource. Sending via Amazon SNS, Amazon Pinpoint, or the AWS End User Messaging console is not supported for shared resources.  
To view resources shared with your account you must use the AWS CLI or the [AWS RAM console](https://console.aws.amazon.com/ram).

We recommend using the [AWS RAM console](https://console.aws.amazon.com/ram) to share resources.

**To share a resource that you own using the AWS End User Messaging console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose the resource type and then resource.

1. On the **Resource policy** tab, choose **Edit**.

1. You can edit the JSON resource based policy to change sharing permissions.

1. Choose **Save changes**.

**To share a resource that you own using the AWS RAM console**  
See [Creating a Resource Share](ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

**To share a resource that you own using the AWS CLI**  
Use the [create-resource-share](cli/latest/reference/ram/create-resource-share.html) command.

## Unsharing a shared resource
<a name="nx-sharing-unshare"></a>

When a resource owner stops sharing a resource with a consumer, the resource no longer appears in the consumer's AWS Management Console.

To unshare a shared resource that you own, you must remove it from the resource share. You can do this using the AWS End User Messaging console, AWS RAM console, or the AWS CLI.

**To unshare a shared resource that you own using the AWS RAM console**  
See [Updating a Resource Share](ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared resource that you own using the AWS CLI**  
Use the [disassociate-resource-share](cli/latest/reference/ram/disassociate-resource-share.html) command.

## Identifying a shared resource
<a name="nx-sharing-identify"></a>

Owners and consumers can identify shared resources using the AWS CLI.

**Note**  
Phone numbers, pools, opt-out list, and sender IDs are generally not identifiable as a shared resource in the AWS End User Messaging AWS Management Console.

**To identify a shared resource using the AWS CLI**  
Use the [describe-opt-out-lists](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.html), [describe-phone-numbers](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-phone-numbers.html), [describe-pools](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-pools.html), or [describe-sender-ids](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-sender-ids.html) command with the `Owner` parameter set to `SHARED`. The command returns the resources that are shared with you.

## Responsibilities and permissions for shared resources
<a name="nx-sharing-perms"></a>

### Permissions for owners
<a name="nx-perms-owner"></a>

Owners can update, view, share, stop sharing, and use resources.

### Permissions for consumers
<a name="nx-perms-consumer"></a>

Consumers can use and view resources.

## Billing and metering
<a name="nx-sharing-billing"></a>

The owner of the resource is billed for the resource. Consumers aren't billed for resources shared with them but are billed for using resources to send messages. There aren't extra costs associated with sharing a resource.

Consumers are billed for sending a message with [send-text-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-text-message.html), [send-media-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.html) or [send-voice-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-voice-message.html) and this counts against the consumers spending limits. For more information about pricing or spending limits, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/) and the production spend limit in Move out of the sandbox.

## Instance quotas
<a name="nx-sharing-quotas"></a>

Sharing a resource doesn't affect the limits of the resource in the owner's or consumer's account. Only the owner's account is used to calculate the limits of the resource.