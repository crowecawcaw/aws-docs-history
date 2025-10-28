# AWS managed policies for Amazon Verified Permissions

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

## AWS managed

policy: AmazonVerifiedPermissionsFullAccess

The `AmazonVerifiedPermissionsFullAccess` managed policy grants full access
to Verified Permissions. To work with Amazon Cognito-based identity sources, you'll need to attach a separate policy, such as the [AmazonCognitoReadOnly](../../../aws-managed-policy/latest/reference/AmazonCognitoReadOnly.md "../../../aws-managed-policy/latest/reference/AmazonCognitoReadOnly.md") policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccountLevelPermissions",
 "Effect": "Allow",
 "Action": [
 "verifiedpermissions:CreatePolicyStore",
 "verifiedpermissions:ListPolicyStores"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PolicyStoreLevelPermissions",
 "Effect": "Allow",
 "Action": [
 "verifiedpermissions:*"
 ],
 "Resource": [
 "arn:aws:verifiedpermissions::*:policy-store/*"
 ]
 }
 ]
}`

```

## AWS

managed policy: AmazonVerifiedPermissionsReadOnlyAccess

The `AmazonVerifiedPermissionsReadOnlyAccess` managed policy grants read-only
access to Verified Permissions.

This policy grants access to all read operations of Amazon Verified Permissions, including the
authorization query APIs `IsAuthorized` and
`IsAuthorizedWithToken`.

###### Note

Access to `BatchIsAuthorized` and `BatchIsAuthorizedWithToken`
are granted automatically when access is granted to `IsAuthorized` and
`IsAuthorizedWithToken`, respectively.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccountLevelPermissions",
 "Effect": "Allow",
 "Action": [
 "verifiedpermissions:ListPolicyStores"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PolicyStoreLevelPermissions",
 "Effect": "Allow",
 "Action": [
 "verifiedpermissions:GetIdentitySource",
 "verifiedpermissions:GetPolicy",
 "verifiedpermissions:GetPolicyStore",
 "verifiedpermissions:GetPolicyTemplate",
 "verifiedpermissions:GetSchema",
 "verifiedpermissions:IsAuthorized",
 "verifiedpermissions:IsAuthorizedWithToken",
 "verifiedpermissions:ListIdentitySources",
 "verifiedpermissions:ListPolicies",
 "verifiedpermissions:ListPolicyTemplates"
 ],
 "Resource": [
 "arn:aws:verifiedpermissions::*:policy-store/*"
 ]
 }
 ]
}`

```

## Verified Permissions updates to AWS managed

policies

View details about updates to AWS managed policies for Verified Permissions since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Verified Permissions Document history page.

| Change                                                                                                                                                                                    | Description                                                                                                                                                                                       | Date             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [AmazonVerifiedPermissionsFullAccess](#security-iam-awsmanpol-AmazonVerifiedPermissionsFullAccess "#security-iam-awsmanpol-AmazonVerifiedPermissionsFullAccess") – New policy             | Verified Permissions added a new policy to allow full access to Verified Permissions.                                                                                                             | October 11, 2024 |
| [AmazonVerifiedPermissionsReadOnlyAccess](#security-iam-awsmanpol-AmazonVerifiedPermissionsReadOnlyAccess "#security-iam-awsmanpol-AmazonVerifiedPermissionsReadOnlyAccess") – New policy | Verified Permissions added a new policy to allow access to all read operations of Amazon Verified Permissions, including the authorization query APIs `IsAuthorized` and `IsAuthorizedWithToken`. | October 11, 2024 |
| Verified Permissions started tracking changes                                                                                                                                             | Verified Permissions started tracking changes for its AWS managed policies.                                                                                                                       | October 11, 2024 |
