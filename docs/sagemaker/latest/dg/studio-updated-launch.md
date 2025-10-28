# Launch Amazon SageMaker Studio

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

This page's topics demonstrate how to launch Amazon SageMaker Studio from the Amazon SageMaker AI console
and the AWS Command Line Interface (AWS CLI).

###### Topics

- [Prerequisites](#studio-updated-launch-prereq "#studio-updated-launch-prereq")
- [Launch from the Amazon SageMaker AI console](#studio-updated-launch-console "#studio-updated-launch-console")
- [Launch using the AWS CLI](#studio-updated-launch-cli "#studio-updated-launch-cli")

## Prerequisites

Before you begin, complete the following prerequisites:

- Onboard to a SageMaker AI domain with Studio access. If you don't have
  permissions to set Studio as the default experience for your domain,
  contact your administrator. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- Update the AWS CLI by following the steps in [Installing the current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- From your local machine, run `aws configure` and provide your AWS
  credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").

## Launch from the Amazon SageMaker AI console

Complete the following procedure to launch Studio from the Amazon SageMaker AI
console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. From the left navigation pane, choose Studio.
3. From the Studio landing page, select the domain and user profile for
   launching Studio.
4. Choose **Open Studio**.
5. To launch Studio, choose **Launch personal Studio**.

## Launch using the AWS CLI

This section demonstrates how to launch Studio using the AWS CLI. The procedure to
access Studio using the AWS CLI depends if the domain uses AWS Identity and Access Management (IAM)
authentication or AWS IAM Identity Center authentication. You can use the AWS CLI to launch Studio
by creating a presigned domain URL when your domain uses IAM authentication. For
information about launching Studio with IAM Identity Center authentication, see [Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md").

The following code snippet demonstrates how to launch Studio from the
AWS CLI using a presigned domain URL if Studio is the default experience. For
more information, see [create-presigned-domain-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-presigned-domain-url.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-presigned-domain-url.html").

```
aws sagemaker create-presigned-domain-url \
--region `region` \
--domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--session-expiration-duration-in-seconds 43200
```

The following code snippet demonstrates how to launch Studio from the
AWS CLI using a presigned domain URL if Studio Classic is the default experience. For
more information, see [create-presigned-domain-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-presigned-domain-url.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-presigned-domain-url.html").

```
aws sagemaker create-presigned-domain-url \
--region `region` \
--domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--session-expiration-duration-in-seconds 43200 \
--landing-uri studio::
```
