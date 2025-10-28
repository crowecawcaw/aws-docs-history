# Set up Partner AI Apps

The following topics describe the permissions needed to start using Amazon SageMaker Partner AI Apps. The
permissions required are split into two parts, depending on the user permissions level:

- **Administrative permissions** – Permissions for
  administrators setting up data scientist and machine learning (ML) developer
  environments.
  - AWS Marketplace
  - Partner AI Apps management
  - AWS License Manager

- **User permissions** – Permissions for data scientists
  and machine learning developers.
  - User authorization
  - Identity propagation
  - SDK access

## Prerequisites

Admins can complete the following prerequisites to set up Partner AI Apps.

- (Optional) Onboard to a SageMaker AI domain. Partner AI Apps can be accessed directly from a SageMaker AI
  domain. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
  - If using Partner AI Apps in a SageMaker AI domain in VPC-only mode, admins must create an endpoint
    with the following format to connect to the Partner AI Apps. For more information about using
    Studio in VPC-only mode, see [Connect Amazon SageMaker Studio
    in a VPC to External Resources](studio-updated-and-internet-access.md "studio-updated-and-internet-access.md").

  ```
  aws.sagemaker.`region`.partner-app
  ```

- (Optional) If admins are interacting with the domain using the AWS CLI, they must also
  complete the following prerequisites.
  1.  Update the AWS CLI by following the steps in [Installing the
      current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
  2.  From the local machine, run `aws configure` and provide AWS
      credentials. For information about AWS credentials, see [Understanding and getting your AWS
      credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md").

## Administrative permissions

The administrator must add the following permissions to enable Partner AI Apps in SageMaker AI.

- Permission to complete AWS Marketplace subscription for Partner AI Apps
- Set up Partner AI App execution role

### AWS Marketplace subscription for Partner AI Apps

Admins must complete the following steps to add permissions for AWS Marketplace. For information
about using AWS Marketplace, see [Getting started as a buyer
using AWS Marketplace](../../../marketplace/latest/buyerguide/buyer-getting-started.md "../../../marketplace/latest/buyerguide/buyer-getting-started.md").

1. Grant permissions for AWS Marketplace. Partner AI Apps administrators require these permissions to
   purchase subscriptions to Partner AI Apps from AWS Marketplace. To get access to AWS Marketplace, admins must attach
   the `AWSMarketplaceManageSubscriptions` managed policy to the IAM role
   that they're using to access the SageMaker AI console and purchase the app. For details about
   the `AWSMarketplaceManageSubscriptions` managed policy, see [AWS managed policies for AWS Marketplace buyers](../../../marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsmarketplacemanagesubscriptions "../../../marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsmarketplacemanagesubscriptions"). For information about attaching
   managed policies, see [Adding and
   removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").
2. Grant permissions for SageMaker AI to run operations on the admins behalf using other
   AWS services. Admins must grant SageMaker AI permissions to use these services and the
   resources that they act upon. The following policy definition demonstrates how to grant
   the required Partner AI Apps permissions. These permissions are needed in addition to the
   existing permissions for the admin role. For more information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePartnerApp",
 "sagemaker:DeletePartnerApp",
 "sagemaker:UpdatePartnerApp",
 "sagemaker:DescribePartnerApp",
 "sagemaker:ListPartnerApps",
 "sagemaker:CreatePartnerAppPresignedUrl",
 "sagemaker:CreatePartnerApp",
 "sagemaker:AddTags",
 "sagemaker:ListTags",
 "sagemaker:DeleteTags"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Set up Partner AI App execution role

1. Partner AI Apps require an execution role to interact with resources in the AWS account.
   Admins can create this execution role using the AWS CLI. The Partner AI App uses this role to
   complete actions related to Partner AI App functionality.

```
aws iam create-role --role-name PartnerAiAppExecutionRole --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "sagemaker.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'
```

2. Create the AWS License Manager service-linked role by following the steps in [Create a service-linked role for License Manager](../../../license-manager/latest/userguide/license-manager-role-core.md#create-slr-core "../../../license-manager/latest/userguide/license-manager-role-core.md#create-slr-core").
3. Grant permissions for the Partner AI App to access License Manager using the AWS CLI. These permissions
   are required to access the licenses for Partner AI App. This allows the Partner AI App to verify access
   to the Partner AI App license.

```
aws iam put-role-policy --role-name PartnerAiAppExecutionRole --policy-name LicenseManagerPolicy --policy-document '{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Action": [
      "license-manager:CheckoutLicense",
      "license-manager:CheckInLicense",
      "license-manager:ExtendLicenseConsumption",
      "license-manager:GetLicense",
      "license-manager:GetLicenseUsage"
    ],
    "Resource": "*"
  }
}'
```

4. If the Partner AI App requires access to an Amazon S3 bucket, then add Amazon S3 permissions to the
   execution role. For more information, see [Required permissions
   for Amazon S3 API operations](../../../AmazonS3/latest/userguide/using-with-s3-policy-actions.md "../../../AmazonS3/latest/userguide/using-with-s3-policy-actions.md").

### Configure Amazon Bedrock integration

Partner AI applications such as Deepchecks support integration with Amazon Bedrock to enable LLM-based evaluation features.
When configuring a Partner AI App with Amazon Bedrock support, administrators can specify which foundation models
and inference profiles are available for use within the application. If you need to increase the quota limit for your Amazon Bedrock models, see
[Request an increase for Amazon Bedrock quotas](../../../bedrock/latest/userguide/quotas-increase.md "../../../bedrock/latest/userguide/quotas-increase.md").

1. Ensure the Partner AI App execution role has the required Amazon Bedrock permissions. Add the following
   permissions to enable Amazon Bedrock model access:

```
aws iam put-role-policy --role-name PartnerAiAppExecutionRole --policy-name BedrockInferencePolicy --policy-document '{
	   "Version": "2012-10-17",
	   "Statement": {
	     "Effect": "Allow",
	     "Action": [
	       "bedrock:InvokeModel",
	       "bedrock:GetFoundationModel",
	       "bedrock:GetInferenceProfile"
	     ],
	     "Resource": "*"
	   }
	 }'
```

2. Identify the Amazon Bedrock models that your organization wants to make available to the Partner AI App.
   You can view available models in your region using the Amazon Bedrock console. For information about
   model availability across regions, see [Model support by AWS Region](../../../bedrock/latest/userguide/models-regions.md "../../../bedrock/latest/userguide/models-regions.md").
3. (Optional) Create customer-managed inference profiles for cost tracking and model management.
   Inference profiles allow you to track Amazon Bedrock usage specifically for the Partner AI App and can enable
   cross-region inference when models are not available in your current region. For more information,
   see [Using inference profiles in Amazon Bedrock](../../../bedrock/latest/userguide/inference-profiles.md "../../../bedrock/latest/userguide/inference-profiles.md").
4. When creating or updating the Partner AI App, specify the allowed models and inference profiles
   using the `CreatePartnerApp` or `UpdatePartnerApp` API. The Partner AI App
   will only be able to access the models and inference profiles that you explicitly configure.

###### Important

Amazon Bedrock usage through Partner AI Apps is billed directly to your AWS account using your existing
Amazon Bedrock pricing. The Partner AI App infrastructure costs are separate from Amazon Bedrock model inference costs.

#### Deepchecks Amazon Bedrock integration

Deepchecks supports Amazon Bedrock integration for LLM-based evaluation capabilities, including:

- _LLM as a judge evaluations_ - Use foundation models to automatically
  evaluate model outputs for quality, relevance, and other criteria
- _Automated annotation_ - Generate labels and annotations for datasets
  using foundation models
- _Content analysis_ - Analyze text data for bias, toxicity, and other
  quality metrics using LLM capabilities

For detailed information about Deepchecks Amazon Bedrock features and configuration, see the
Deepchecks documentation within the application.

## User permissions

After admins have completed the administrative permissions settings, they must make sure
that users have the permissions needed to access the Partner AI Apps.

1. Grant permissions for SageMaker AI to run operations on your behalf using other
   AWS services. Admins must grant SageMaker AI permissions to use these services and the resources
   that they act upon. Admins grant SageMaker AI these permissions using an IAM execution role. For
   more information about IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md"). The following policy
   definition demonstrates how to grant the required Partner AI Apps permissions. This policy can be
   added to the execution role of the user profile.  For more information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribePartnerApp",
 "sagemaker:ListPartnerApps",
 "sagemaker:CreatePartnerAppPresignedUrl"
 ],
 "Resource": "arn:aws:sagemaker:*:*:partner-app/app-*"
 }
 ]
}`

```

2. (Optional) If launching Partner AI Apps from Studio, add the `sts:TagSession`
   trust policy to the role used to launch Studio or the Partner AI Apps directly as follows.
   This makes sure that the identity can be propagated properly.

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "sagemaker.amazonaws.com"
    },
    "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
             ]
}
```

3. (Optional) If using the SDK of a Partner AI App to access functionality in SageMaker AI, add
   the following `CallPartnerAppApi` permission to the role used to run the SDK
   code. If running the SDK code from Studio, add the permission to the Studio
   execution role. If running the code from anywhere other than Studio, add the
   permission to the IAM role used with the notebook. This gives the user access the Partner AI App
   functionality from the Partner AI App’s SDK.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CallPartnerAppApi"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`111122223333`:partner-app/`app`"
 ]
 }
 ]
}`

```

### Manage user authorization and

authentication

To provide access to Partner AI Apps to members of their team, admins must make sure that the
identity of their users is propagated to the Partner AI Apps. This propagation makes sure users can
properly access the Partner AI Apps' UI and perform authorized Partner AI App actions.

Partner AI Apps support the following identity sources:

- AWS IAM Identity Center
- External identity providers (IdPs)
- IAM Session-based identity

The following sections gives information about the identity sources that Partner AI Apps
support, as well as important details related to that identity source.

If a user is authenticated into Studio using IAM Identity Center and launches an application
from Studio, the IAM Identity Center `UserName` is automatically propagated as the
user identity for a Partner AI App. This is not the case if the user launches the Partner AI App
directly using the `CreatePartnerAppPresignedUrl` API.

If using SAML for AWS account federation, admins have two options to carry over
the IdP identity as the user identity for a Partner AI App. For information about setting up
AWS account federation, see [How to Configure SAML 2.0 for AWS account Federation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Amazon-Web-Service "https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Amazon-Web-Service"). 

- **Principal Tag** – Admins can configure
  the IdP-specific IAM Identity Center application to pass identity information from the landing
  session using the AWS session `PrincipalTag` with the following
  `Name` attribute. When using SAML, the landing role session uses an
  IAM role. To use the `PrincipalTag`, admins must add the
  `sts:TagSession` permission to this landing role, as well as the
  Studio execution role. For more information about `PrincipalTag`,
  see [Configure SAML assertions for the authentication response](../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md#saml_role-session-tags "../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md#saml_role-session-tags").

```
https://aws.amazon.com/SAML/Attributes/PrincipalTag:SageMakerPartnerAppUser
```

- **Landing session name** – Admins can
  propagate the landing session name as the identity for the Partner AI App. To do this, they
  must set the `EnableIamSessionBasedIdentity` opt-in flag for each Partner AI App.
  For more information, see [EnableIamSessionBasedIdentity](#partner-app-onboard-user-iam-session "#partner-app-onboard-user-iam-session").

###### Important

We do not recommend using this method for production accounts. For production
accounts, use an identity provider for increased security.

SageMaker AI supports the following options for identity propagation when using an IAM
session-based identity. All of the options, except using a session tag with AWS STS,
require setting the `EnableIamSessionBasedIdentity` opt-in flag for each
application. For more information, see [EnableIamSessionBasedIdentity](#partner-app-onboard-user-iam-session "#partner-app-onboard-user-iam-session").

When propagating identities, SageMaker AI verifies whether an AWS STS Session tag is being
used. If one is not used, then SageMaker AI propagates the IAM username or AWS STS session name.

- **AWS STS Session tag** – Admins can set a
  `SageMakerPartnerAppUser` session tag for the launcher IAM session.
  When admins launch a Partner AI App using the SageMaker AI console or the AWS CLI,
  the `SageMakerPartnerAppUser` session tag is automatically passed as
  the user identity for the Partner AI App. The following example shows how to set the
  `SageMakerPartnerAppUser` session tag using the AWS CLI. The value of the
  key is added as a principal tag.

```
aws sts assume-role \
    --role-arn arn:aws:iam::`account`:role/`iam-role-used-to-launch-partner-ai-app` \
    --role-session-name session_name \
    --tags Key=SageMakerPartnerAppUser,Value=`user-name`
```

When giving users access to a Partner AI App using
`CreatePartnerAppPresignedUrl`, we recommend verifying the value for
the `SageMakerPartnerAppUser` key. This helps to prevent unintended
access to Partner AI App resources. The following trust policy verifies that the session tag
exactly matches the associated IAM user. Admins can use any principal tag for this
purpose. It should be configured on the role that is launching Studio or the
Partner AI App.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RoleTrustPolicyRequireUsernameForSessionName",
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession"
 ],
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Condition": {
 "StringLike": {
 "aws:RequestTag/SageMakerPartnerAppUser": "prefix${aws:username}"
 }
 }
 }
 ]
}`

```

- **Authenticated IAM user** – The username of
  the user is automatically propagated as the Partner AI App user.
- **AWS STS session name** – If no
  `SageMakerPartnerAppUser` session tag is configured when using AWS STS,
  SageMaker AI returns an error when users launch a Partner AI App. To avoid this error, admins must
  set the `EnableIamSessionBasedIdentity` opt-in flag for each Partner AI App. For
  more information, see [EnableIamSessionBasedIdentity](#partner-app-onboard-user-iam-session "#partner-app-onboard-user-iam-session").

When the `EnableIamSessionBasedIdentity` opt-in flag is enabled, use
the [IAM role trust policy](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_rolesessionname "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_rolesessionname") to make sure that the IAM session name is or
contains the IAM username. This makes sure that users don't gain access by
impersonating other users. The following trust policy verifies that the session name
exactly matches the associated IAM user. Admins can use any principal tag for this
purpose. It should be configured on the role that is launching Studio or the
Partner AI App.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RoleTrustPolicyRequireUsernameForSessionName",
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Condition": {
 "StringEquals": {
 "sts:RoleSessionName": "${aws:username}"
 }
 }
 }
 ]
}`

```

Admins must also add the `sts:TagSession` trust policy to the role
that is launching Studio or the Partner AI App. This makes sure that the identity can
be propagated properly.

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "sagemaker.amazonaws.com"
    },
    "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
             ]
}
```

After setting the credentials, admins can give their users access to Studio or
the Partner AI App from the AWS CLI using either the `CreatePresignedDomainUrl` or
`CreatePartnerAppPresignedUrl` API calls, respectively.

Users can also then launch Studio from the SageMaker AI console, and launch Partner AI Apps
from Studio.

### `EnableIamSessionBasedIdentity`

`EnableIamSessionBasedIdentity` is an opt-in flag. When
the `EnableIamSessionBasedIdentity` flag is set, SageMaker AI passes IAM session
information as the Partner AI App user identity. For more information about AWS STS sessions, see
[Use temporary
credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md").

### Access control

To control access to Partner AI Apps, use an IAM policy attached to the user profile’s
execution role. To launch a Partner AI App directly from Studio or using the AWS CLI, the user
profile’s execution role must have a policy that gives permissions for
the `CreatePartnerAppPresignedUrl` API. Remove this permission from the user
profile’s execution role to make sure they can't launch Partner AI Apps.

### Root admin users

The Comet and Fiddler Partner AI Apps require at least one root
admin user. Root admin users have permissions to add both normal and admin users and manage
resources. The usernames provided as root admin users must be consistent with the usernames
from the identity source.

While root admin users are persisted in SageMaker AI, normal admin users are not and exist only
within the Partner AI App until the Partner AI App is terminated.

Admins can update root admin users using the `UpdatePartnerApp` API call.
When root admin users are updated, the updated list of root admin users is passed to the
Partner AI App. The Partner AI App makes sure that all usernames in the list are granted root admin
privileges. If a root admin user is removed from the list, the user still retains normal
admin permissions until either:

- The user is removed from the application.
- Another admin user revokes admin permissions for the user.

###### Note

Fiddler doesn't support updating admin users. Only Comet
supports updates to root admin users. 

To delete a root admin user, you must first update the list of root admin users using
the `UpdatePartnerApp` API. Then, remove or revoke the admin permissions
through the Partner AI App's UI.

If you remove a root admin user from the Partner AI App's UI without updating the list of root
admin users with the `UpdatePartnerApp` API, the change is temporary. When SageMaker AI
sends the next Partner AI App update request, SageMaker AI sends the root admin list that still includes the
user to the Partner AI App. This overrides the deletion completed from the Partner AI App UI.
