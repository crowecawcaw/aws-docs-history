

# Security profiles do not affect agent authorization for viewing an email thread
<a name="email-security-profiles1"></a>

Any user with the following permission in their security profile has access to read emails that they handle or emails that are part of a thread where they are a participant: **Contact Control Panel (CCP)** - **Access Contact Control Panel** - **Access**.

![The Access Contact Control Panel option on the Security profiles page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/access-ccp-perm.png)


This authorization behavior is enabled by default. It does not require setting up any additional permission or configuration.

This behavior is driven by the following context keys:

1. `connect:UserArn`: Represents the user that has access to an individual contact.

1. `connect:ContactAssociationId`: Represents the contact association the user has access to. For the email channel, a contact association always represents an email thread.

1. `connect:Channel`: Represents the contact channel the user has access to. For the email channel, this contextKey is always `EMAIL`.

We don't recommend using `connect:ContactAssociationId` in the same policy as `connect:UserArn` because it might result in a no-op. Because the `connect:UserArn` condition key is more restrictive, it will `Deny` access for all contacts not handled by the corresponding user, regardless of the access they have to email threads.

You can use `connect:Channel` in isolation to restrict access to specific channels. Accepted values are: `VOICE`, `CHAT`, `TASK`, or `EMAIL`. See the [Contact](https://docs.aws.amazon.com/connect/latest/APIReference/API_Contact.html) API.

Following are the contact-related APIs that support these context keys:

1. [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html)

1. [UpdateContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContact.html)

1. [ListContactReferences](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactReferences.html)

1. [TagContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_TagContact.html)

1. [UntagContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_UntagContact.html)

1. [UpdateContactRoutingData](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactRoutingData.html)

1. [GetContactAttributes](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetContactAttributes.html) 

1. [UpdateContactAttributes](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactAttributes.html) 

1.  [StopContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContact.html) 

1. [StartContactRecording](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactRecording.html) 

1.  [StopContactRecording](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContactRecording.html) 

1. [ResumeContactRecording](https://docs.aws.amazon.com/connect/latest/APIReference/API_ResumeContactRecording.html) 

1. [SuspendContactRecording](https://docs.aws.amazon.com/connect/latest/APIReference/API_SuspendContactRecording.html) 

1. [UpdateContactSchedule](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactSchedule.html) 

1. [TransferContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_TransferContact.html) 

1. [StartScreenSharing](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartScreenSharing.html) 