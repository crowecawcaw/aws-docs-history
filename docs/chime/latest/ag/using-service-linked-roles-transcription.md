# Using roles with live

transcription

The information in the following sections explains how to create and manage a service-linked
role for the Amazon Chime SDK live transcription. For more information about the live transcription
service, see [Using
Amazon Chime SDK live transcription](../dg/meeting-transcription.md "../dg/meeting-transcription.md").

###### Topics

- [Service-Linked Role
  Permissions for Nova Act](#service-linked-role-permissions-transcription "#service-linked-role-permissions-transcription")
- [Creating a Service-Linked Role for
  Nova Act](#create-service-linked-role-transcription "#create-service-linked-role-transcription")
- [Editing a Service-Linked Role for Nova Act](#edit-slr "#edit-slr")
- [Deleting a Service-Linked Role for Nova Act](#delete-slr "#delete-slr")
- [Supported Regions for Amazon Chime Service-Linked
  Roles](#slr-regions-transcription "#slr-regions-transcription")

## Service-Linked Role

Permissions for Nova Act

Nova Act uses a service-linked role named **AWSServiceRoleForAmazonChimeTranscription – Allows
the Amazon Chime SDK to access Amazon Transcribe and Amazon Transcribe Medical on your
behalf.**

The AWSServiceRoleForAmazonChimeTranscription service-linked role trusts the following services to assume
the role:

- `transcription.chime.amazonaws.com`

The role permissions policy allows the Amazon Chime SDK to complete the following actions on the
specified resources:

- Action: `transcribe:StartStreamTranscription` on
  `all AWS resources`
- Action: `transcribe:StartMedicalStreamTranscription` on
  `all AWS resources`

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a Service-Linked Role for

Nova Act

You use the IAM console to create a service-linked role with the
**Chime Transcription** use case.

###### Note

You must have IAM administrative permissions to complete these steps. If you don't,
contact a system administrator.

###### To create the role

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**, then
   choose **Create role**.
3. Choose the **AWS Service** role type, then choose **Chime
   Transcription**.

The IAM policy appears. 4. Select the checkbox next to the policy, then choose **Next:
Tags**. 5. Choose **Next: Review**. 6. Edit the description as needed, then choose **Create role**.

You can also use the AWS CLI or the AWS API to create a service-linked role named
transcription.chime.amazonaws.com.

In the CLI, run this command: `aws iam create-service-linked-role --aws-service-name
 transcription.chime.amazonaws.com`.

For more information, see [Creating a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a Service-Linked Role for Nova Act

The Amazon Chime SDK does not allow you to edit the AWSServiceRoleForAmazonChimeTranscription service-linked role.
After you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can use IAM to edit the role's description.
For more information, see [Editing
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a Service-Linked Role for Nova Act

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonChimeTranscription
service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Amazon Chime Service-Linked

Roles

The Amazon Chime SDK supports using service-linked roles in all of the regions where the service is
available. For more information, see [Amazon Chime endpoints and quotas](../../../general/latest/gr/chime.md#chime_region "../../../general/latest/gr/chime.md#chime_region"), and [Using Amazon Chime SDK media
Regions](../dg/chime-sdk-meetings-regions.md "../dg/chime-sdk-meetings-regions.md").
