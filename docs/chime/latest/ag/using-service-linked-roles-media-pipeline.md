**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Using roles with Amazon Chime SDK media

pipelines

The information in the following sections explains how to create and manage a service-linked role for Amazon Chime
SDK Media Pipelines.

###### Topics

- [Service-linked role permissions for Amazon Chime SDK media pipelines](#slr-permissions "#slr-permissions")
- [Creating a service-linked role for Amazon Chime SDK media pipelines](#create-slr "#create-slr")
- [Editing a service-linked role for Amazon Chime SDK media pipelines](#edit-slr "#edit-slr")
- [Deleting a service-linked role for Amazon Chime SDK media pipelines](#delete-slr "#delete-slr")
- [Supported Regions for Amazon Chime SDK media pipelines service-linked roles](#slr-regions "#slr-regions")

## Service-linked role permissions for Amazon Chime SDK media pipelines

Amazon Chime uses the service-linked role named **AWSServiceRoleForAmazonChimeSDKMediaPipelines** –
Allows Amazon Chime SDK media pipelines to access Amazon Chime SDK meetings on your behalf.

The AWSServiceRoleForAmazonChimeSDKMediaPipelines service-linked role trusts the following services to assume the
role:

- `mediapipelines.chime.amazonaws.com`

The role allows Amazon Chime to complete the following actions on the specified resources:

- Action: `chime:CreateAttendee` on `all AWS resources`
- Action: `chime:DeleteAttendee` on `all AWS resources`
- Action: `chime:GetMeeting` on `all AWS resources`

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for Amazon Chime SDK media pipelines

You use the IAM console to create a service-linked role with the **Amazon Chime SDK Media Pipelines\*** use case.

###### Note

You must have IAM administrative permissions to complete these steps. If you don't, contact a system administrator.

###### To create the role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**, then choose **Create role**.
3. Choose the **AWS Service** role type, then choose **Chime**, then choose **Chime SDK Media Pipelines**.
4. Choose **Next**.
5. Choose **Next**.
6. Edit the description as needed, then choose **Create role**.

You can also use the AWS CLI or the AWS API to create a service-linked role named mediapipelines.chime.amazonaws.com.

In the AWS CLI, run this command: `aws iam create-service-linked-role --aws-service-name mediapipelines.chime.amazonaws.com`.

For more information, see [Creating a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for Amazon Chime SDK media pipelines

Amazon Chime does not allow you to edit the AWSServiceRoleForAmazonChimeSDKMediaPipelines service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Amazon Chime SDK media pipelines

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonChimeSDKMediaPipelines
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Amazon Chime SDK media pipelines service-linked roles

Amazon Chime SDK supports using service-linked roles in all of the AWS Regions where the service is available.
For more information, see [Amazon Chime endpoints and quotas](../../../general/latest/gr/chime.md#chime_region "../../../general/latest/gr/chime.md#chime_region").
