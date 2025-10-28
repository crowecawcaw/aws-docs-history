# Setting up cross-account sharing for Amazon SageMaker AI

partner AI apps

Amazon SageMaker AI integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a service
that enables you to share some Amazon SageMaker AI resources with other AWS accounts or through
AWS Organizations. With AWS RAM, you share resources that you own by creating a _resource
share_. A resource share specifies the resources to share, and the consumers with
whom to share them. Consumers can be specific AWS accounts inside or outside of its
organization in AWS Organizations.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

This topic explains how to share resources that you own, and how to use resources that are
shared with you.

###### Contents

- [Prerequisites for sharing an
  Amazon SageMaker Partner AI App](#partner-app-resource-sharing-ram-prereqs "#partner-app-resource-sharing-ram-prereqs")
- [Sharing an Amazon SageMaker Partner AI App](#partner-app-resource-sharing-share "#partner-app-resource-sharing-share")
- [Accepting resource share
  invitations](#partner-app-resource-sharing-responses "#partner-app-resource-sharing-responses")
- [Identifying a shared Amazon SageMaker Partner AI App](#sharing-identify "#sharing-identify")
- [Responsibilities and permissions for shared
  Amazon SageMaker Partner AI Apps](#sharing-perms "#sharing-perms")

## Prerequisites for sharing an

Amazon SageMaker Partner AI App

- To share an Amazon SageMaker Partner AI App, you must own it in your AWS account. This means that the
  resource must be allocated or provisioned in your account. You cannot share an Amazon SageMaker Partner AI App
  that has been shared with you.
- To share an Amazon SageMaker Partner AI App with your organization or an organizational unit in AWS Organizations,
  you must enable sharing with AWS Organizations. For more information, see [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.

## Sharing an Amazon SageMaker Partner AI App

To share an Amazon SageMaker Partner AI App, you must add it to a resource share. A resource share is an AWS RAM
resource that lets you share your resources across AWS accounts. A resource share specifies
the resources to share, and the consumers with whom they are shared. When you share an
Amazon SageMaker Partner AI App using the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker"), you
add it to an existing resource share. To add the Amazon SageMaker Partner AI App to a new resource share, you must
first create the resource share by using the [AWS RAM
console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").

You can share an Amazon SageMaker Partner AI App that you own using the Amazon SageMaker AI console, AWS RAM console, or
the AWS CLI.

###### To share an Amazon SageMaker Partner AI App that you own using the Amazon SageMaker AI console

1. Sign in to the AWS Management Console and open the AWS RAM console at [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. In the main pane, choose **Create a resource share**.
3. Enter a name for the resource share that you want to create.
4. In the **Resources** section, for **Resource type**
   select **SageMaker AI Partner Apps**. The partner apps that you can share appear
   in the table.
5. Select the partner apps that you want to share.
6. Optionally specify tags, and then choose **Next**.
7. Specify the AWS accounts with which you want to share your partner apps.
8. Review your resource share configuration and choose **Create resource
   share**. It might take the service a few minutes to finish creating the
   resource share.

###### To share an Amazon SageMaker Partner AI App that you own using the AWS RAM console

See [Creating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the _AWS RAM User Guide_.

###### To share an Amazon SageMaker Partner AI App that you own using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

## Accepting resource share

invitations

When a resource owner sets up a resource share, each consumer AWS account receives an
invitation to join the resource share. The consumer AWS accounts must accept the invitation
to gain access to any shared resources.

For more information on accepting a resource share invitation through AWS RAM, see [Using shared
AWS resources](../../../ram/latest/userguide/getting-started-shared.md "../../../ram/latest/userguide/getting-started-shared.md") in the _AWS Resource Access Manager User
Guide_.

## Identifying a shared Amazon SageMaker Partner AI App

Owners and consumers can identify shared Amazon SageMaker Partner AI Apps using the Amazon SageMaker AI console and
AWS CLI.

###### To identify a shared Amazon SageMaker Partner AI App by using the Amazon SageMaker AI console

See [Partner AI Apps in Studio](partner-apps-studio.md "partner-apps-studio.md").

###### To identify a shared Amazon SageMaker Partner AI App by using the AWS CLI

Use the [list-partner-apps](../../../cli/latest/reference/sagemaker/list-partner-apps.md "../../../cli/latest/reference/sagemaker/list-partner-apps.md")
command. The command returns the Amazon SageMaker Partner AI Apps that you own and Amazon SageMaker Partner AI Apps that are shared
with you. `OwnerId` shows the AWS account ID of the Amazon SageMaker Partner AI App owner.

## Responsibilities and permissions for shared

Amazon SageMaker Partner AI Apps

The account with which an Amazon SageMaker Partner AI App is shared needs to have the following AWS Identity and Access Management
policy.

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AmazonSageMakerPartnerListAppsPermission",
      "Effect" : "Allow",
      "Action" : "sagemaker:ListPartnerApps",
      "Resource" : "*"
    },
    {
      "Sid" : "AmazonSageMakerPartnerAppsPermission",
      "Effect" : "Allow",
      "Action" : [
        "sagemaker:CreatePartnerAppPresignedUrl",
        "sagemaker:DescribePartnerApp",
        "sagemaker:CallPartnerAppApi"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : [
                        "`App-owner AWS account-1`", "`App-owner AWS account-2`", ...
                    ]
        }
      },
      "Resource" : "arn:aws:sagemaker:*:*:partner-app/*"
    }
  ]
}
```
