# AWS managed policies for Amazon Cognito

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### AWS managed IAM policies that grant access to Amazon Cognito

- `AmazonCognitoPowerUser` - Permissions for accessing and managing all
  aspects of your identity pools and user pools. To view the permissions for this policy,
  see [AmazonCognitoPowerUser](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonCognitoPowerUser "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonCognitoPowerUser").
- `AmazonCognitoReadOnly` - Permissions for read-only access to your
  identity pools and user pools. To view the permissions for this policy,
  see [AmazonCognitoReadOnly](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonCognitoReadOnly "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonCognitoReadOnly").
- `AmazonCognitoDeveloperAuthenticatedIdentities` - Permissions for your
  authentication system to integrate with Amazon Cognito. To view the permissions for this policy,
  see [AmazonCognitoDeveloperAuthenticatedIdentities](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonCognitoDeveloperAuthenticatedIdentities "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonCognitoDeveloperAuthenticatedIdentities").
  These policies are maintained by the Amazon Cognito team, so even as new APIs are added, your users
  continue to have the same level of access.

###### Note

When you create a new identity pool, you can automatically create new roles for
authenticated and guest user access. The administrator who creates your identity pool with
new IAM roles must also have IAM permissions to create roles.

Identity pools with unauthenticated guest access apply an additional AWS managed policy
as a [session policy](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") to
unauthenticated users. This AWS managed policy has no intended administrative use. Instead,
it limits the scope of permissions that you can apply to guest users in the identity pools
[enhanced authentication flow](authentication-flow.md "authentication-flow.md"). For more information, see [IAM roles](iam-roles.md "iam-roles.md").

###### AWS managed IAM policies that Amazon Cognito grants to guest users

- `AmazonCognitoUnAuthedIdentitiesSessionPolicy` - In combination with an
  inline session policy, limits the permissions that IAM administrators can grant to
  identity pool guest users. Amazon Cognito automatically applies this policy to guest sessions.
  For more information, see [The AWS managed session policy for
  guests](iam-roles.md#access-policies-managed-policy "iam-roles.md#access-policies-managed-policy").

## Amazon Cognito updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon Cognito since this service began
tracking these changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the Amazon Cognito [Document
history](cognito-document-history.md "cognito-document-history.md") page.

| Change                                                         | Description                                                                                                                                                                                                                                                                                                                                                           | Date              |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `AmazonCognitoPowerUser`–Change                                | Amazon Cognito added new actions to permit the use of the AWS End User Messaging SMS API operation<br>[DescribeAccountAttributes](../../../pinpoint/latest/apireference_smsvoicev2/API_DescribeAccountAttributes.md "../../../pinpoint/latest/apireference_smsvoicev2/API_DescribeAccountAttributes.md") for Amazon Cognito user pools administrative power<br>users. | February 27, 2025 |
| `AmazonCognitoUnAuthedIdentitiesSessionPolicy`–Change          | Amazon Cognito added new actions to permit the use of AWS Key Management Service for unauthenticated<br>(guest) users in identity pools.                                                                                                                                                                                                                              | October 30, 2024  |
| `AmazonCognitoUnAuthedIdentitiesSessionPolicy`–Change          | Amazon Cognito added new actions to permit the use of Amazon Location Service for unauthenticated<br>(guest) users in identity pools.                                                                                                                                                                                                                                 | August 9, 2024    |
| `AmazonCognitoUnAuthedIdentitiesSessionPolicy`–New<br>policy   | Added an AWS managed policy for privilege scope-down of guest users in<br>identity pools.                                                                                                                                                                                                                                                                             | July 14, 2023     |
| `AmazonCognitoPowerUser` and<br>`AmazonCognitoReadOnly`–Change | Added new permissions to allow power users to view and manage associations<br>of AWS WAF web ACLs to Amazon Cognito user pools.Added new permissions to allow read-only<br>users to view associations of AWS WAF web ACLs to Amazon Cognito user pools.                                                                                                               | July 19, 2022     |
| `AmazonCognitoPowerUser`–Change                                | Added a new permission to allow Amazon Cognito to call Amazon Simple Email Service<br>`PutIdentityPolicy` and `ListConfigurationSets`<br>operations.This change allows Amazon Cognito user pools to update Amazon SES sending<br>authorization policies and to apply Amazon SES configuration sets when you<br>configure email sending in your user pool.             | November 17, 2021 |
| `AmazonCognitoPowerUser`–Change                                | Added a new permission to allow Amazon Cognito to call Amazon Simple Notification Service's<br>`GetSMSSandboxAccountStatus` operation.<br>This change allows Amazon Cognito user pools to decide if you need to graduate out of the<br>Amazon Simple Notification Service sandbox in order to send messages to all end users through user<br>pools.                   | June 1, 2021      |
| Amazon Cognito started tracking changes                        | Amazon Cognito started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                 | March 1, 2021     |
