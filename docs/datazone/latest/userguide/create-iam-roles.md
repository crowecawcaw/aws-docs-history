# Configure the IAM permissions required to use the

Amazon DataZone management console

In order to access and conﬁgure your Amazon DataZone domains, blueprints, and users, and
to create the Amazon DataZone data portal, you must use the Amazon DataZone management
console.

You must complete the following procedures in order to configure the required and/or
optional permissions for any user, group or role that wants to use the Amazon DataZone
management console.

###### Procedures to set up IAM permissions to use the management

console

- [Attach required and optional policies to a user, group,
  or role for Amazon DataZone console access](#attach-managed "#attach-managed")
- [Create a custom policy for IAM
  permissions to enable the Amazon DataZone service console simplified role creation](#create-custom-to-manage-EZCRZ "#create-custom-to-manage-EZCRZ")
- [Create a custom policy for
  permissions to manage an account associated with an Amazon DataZone domain](#create-custom-to-manage-associated-account "#create-custom-to-manage-associated-account")
- [(Optional) Create a custom
  policy for AWS Identity Center permissions to add and remove SSO user and SSO group
  access to Amazon DataZone domains](#create-custom-to-manage-add-remove-sso "#create-custom-to-manage-add-remove-sso")
- [(Optional) Add your IAM principal as a key
  user to create your Amazon DataZone domain with a customer-managed key from AWS Key
  Management Service (KMS)](#create-custom-to-manage-kms "#create-custom-to-manage-kms")

## Attach required and optional policies to a user, group,

or role for Amazon DataZone console access

Complete the following procedure to attach the required and optional custom policies
to a user, group, or a role. For more information, see [AWS managed policies for Amazon DataZone](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose the following policies to attach to your user, group, or a role.
   - In the list of policies, select the check box next to the
     **AmazonDataZoneFullAccess**. You can use the
     **Filter** menu and the search box to filter the list of
     policies. For more information, see [AWS managed
     policy: AmazonDataZoneFullAccess](security-iam-awsmanpol-AmazonDataZoneFullAccess.md "security-iam-awsmanpol-AmazonDataZoneFullAccess.md").
   - [(Optional) Create a custom
     policy for IAM permissions to enable the Amazon DataZone service console
     simplified role creation.](#create-custom-to-manage-EZCRZ "#create-custom-to-manage-EZCRZ")
   - [(Optional) Create
     a custom policy for AWS Identity Center permissions to add and remove
     SSO user and SSO group access to your Amazon DataZone domain.](#create-custom-to-manage-add-remove-sso "#create-custom-to-manage-add-remove-sso")

4. Choose **Actions**, and then choose
   **Attach**.
5. Choose the user, group, or role to which you want to attach the policy. You can
   use the **Filter** menu and the search box to filter the list of
   principal entities. After choosing the user, group, or role, choose
   **Attach policy**.

## Create a custom policy for IAM

permissions to enable the Amazon DataZone service console simplified role creation

Complete the following procedure to create a custom inline policy to have the
necessary permissions to enable Amazon DataZone to create the necessary roles in the AWS
management console on your behalf.

###### Note

For best practices information on configuring permissions to allow creation of
service roles, see [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** or **User
   groups**.
3. In the list, choose the name of the user or group to embed a policy in.
4. Choose the **Permissions** tab and, if necessary, expand the
   **Permissions policies** section.
5. Choose **Add permissions** and **Create inline
   policy** link.
6. On the **Create Policy** screen, in the **Policy
   editor** section, choose **JSON**.

Create a policy document with the following JSON statements, and then choose
**Next**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreatePolicy",
 "iam:CreateRole"
 ],
 "Resource": [
 "arn:aws:iam::*:policy/service-role/AmazonDataZone*",
 "arn:aws:iam::*:role/service-role/AmazonDataZone*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:AttachRolePolicy",
 "Resource": "arn:aws:iam::*:role/service-role/AmazonDataZone*",
 "Condition": {
 "ArnLike": {
 "iam:PolicyARN": [
 "arn:aws:iam::aws:policy/AmazonDataZone*",
 "arn:aws:iam::*:policy/service-role/AmazonDataZone*"
 ]
 }
 }
 }
 ]
}`

```

7. On the **Review policy** screen, enter a name for the policy.
   When you're satisfied with the policy, choose **Create policy**.
   Ensure that no errors appear in a red box at the top of the screen. Correct any
   that are reported.

## Create a custom policy for

permissions to manage an account associated with an Amazon DataZone domain

Complete the following procedure to create a custom inline policy to have the
necessary permissions in an associated AWS account to list, accept, and reject
resource shares of a domain, and then enable, configure, and disable environment
blueprints in the associated account. To enable the optional Amazon DataZone service console
simplified role creation available during blueprint configuration, you must also [Create a custom policy for IAM
permissions to enable the Amazon DataZone service console simplified role creation](#create-custom-to-manage-EZCRZ "#create-custom-to-manage-EZCRZ") .

###### Note

For best practices information on configuring permissions to allow creation of
service roles, see [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** or **User
   groups**.
3. In the list, choose the name of the user or group to embed a policy in.
4. Choose the **Permissions** tab and, if necessary, expand the
   P**ermissions policies** section.
5. Choose **Add permissions** and **Create inline
   policy** link.
6. On the **Create Policy** screen, in the **Policy
   editor** section, choose **JSON**. Create a policy
   document with the following JSON statements, and then choose
   **Next**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "datazone:ListEnvironmentBlueprintConfigurations",
 "datazone:PutEnvironmentBlueprintConfiguration",
 "datazone:GetDomain",
 "datazone:ListDomains",
 "datazone:GetEnvironmentBlueprintConfiguration",
 "datazone:ListEnvironmentBlueprints",
 "datazone:GetEnvironmentBlueprint",
 "datazone:ListAccountEnvironments",
 "datazone:DeleteEnvironmentBlueprintConfiguration"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::*:role/AmazonDataZone",
 "arn:aws:iam::*:role/service-role/AmazonDataZone*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:passedToService": "datazone.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:AttachRolePolicy",
 "Resource": "arn:aws:iam::*:role/service-role/AmazonDataZone*",
 "Condition": {
 "ArnLike": {
 "iam:PolicyARN": [
 "arn:aws:iam::aws:policy/AmazonDataZone*",
 "arn:aws:iam::*:policy/service-role/AmazonDataZone*"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreatePolicy",
 "iam:CreateRole"
 ],
 "Resource": [
 "arn:aws:iam::*:policy/service-role/AmazonDataZone*",
 "arn:aws:iam::*:role/service-role/AmazonDataZone*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ram:AcceptResourceShareInvitation",
 "ram:RejectResourceShareInvitation",
 "ram:GetResourceShareInvitations"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "s3:CreateBucket",
 "Resource": "arn:aws:s3:::amazon-datazone*"
 }
 ]
}`

```

7. On the **Review policy** screen, enter a name for the policy.
   When you're satisfied with the policy, choose **Create policy**.
   Ensure that no errors appear in a red box at the top of the screen. Correct any
   that are reported.

## (Optional) Create a custom

policy for AWS Identity Center permissions to add and remove SSO user and SSO group
access to Amazon DataZone domains

Complete the following procedure to create a custom inline policy to have the
necessary permissions to add and remove SSO user and SSO group access to your Amazon DataZone
domain.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** or **User
   groups**.
3. In the list, choose the name of the user or group to embed a policy in.
4. Choose the **Permissions** tab and, if necessary, expand the
   **Permissions policies** section.
5. Choose **Add permissions** and **Create inline
   policy**.
6. On the **Create Policy** screen, in the **Policy
   editor** section, choose **JSON**.

Create a policy document with the following JSON statements, and then choose
**Next**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso:GetManagedApplicationInstance",
 "sso:ListProfiles",
 "sso:AssociateProfile",
 "sso:DisassociateProfile",
 "sso:GetProfile"
 ],
 "Resource": "*"
 }
 ]
}`

```

7. On the **Review policy** screen, enter a name for the policy.
   When you're satisfied with the policy, choose **Create policy**.
   Ensure that no errors appear in a red box at the top of the screen. Correct any
   that are reported.

## (Optional) Add your IAM principal as a key

user to create your Amazon DataZone domain with a customer-managed key from AWS Key
Management Service (KMS)

Before you can optionally create your Amazon DataZone domain with a customer-managed key
(CMK) from the AWS Key Management Service (KMS), complete the following procedure to
make your IAM principal a user of your KMS key.

1. Sign in to the AWS Management Console and open the KMS console at [https://console.aws.amazon.com/kms/](https://console.aws.amazon.com/kms/ "https://console.aws.amazon.com/kms/").
2. To view the keys in your account that you create and manage, in the navigation
   pane choose **Customer managed keys**.
3. In the list of KMS keys, choose the alias or key ID of the KMS key that you
   want to examine.
4. To add or remove key users, and to allow or disallow external AWS accounts to
   use the KMS key, use the controls in the **Key users** section of
   the page. Key users can use the KMS key in cryptographic operations, such as
   encrypting, decrypting, re-encrypting, and generating data keys.
