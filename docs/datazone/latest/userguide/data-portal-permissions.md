# Configure the IAM permissions required to use the

Amazon DataZone data portal

Amazon DataZone data portal (outside the AWS Management Console) is a browser-based web
application where users can go to catalog, discover, govern, share, and analyze data in a
self-service fashion. The data portal authenticates users with IAM credentials or existing
credentials from your identity provider through AWS IAM Identity Center.

You must complete the following procedures in order to configure the required
permissions for any user, group or role that wants to use the Amazon DataZone data portal or
catalog:

###### Procedures to configure IAM permissions for using the data

portal

- [Attach required policy to a user,
  group, or role for Amazon DataZone data portal access](#data-portal-permissions-portal "#data-portal-permissions-portal")
- [Attach required policy to a user,
  group, or role for Amazon DataZone catalog access](#data-portal-permissions-catalog "#data-portal-permissions-catalog")
- [Attach optional policy to a user, group,
  or role for Amazon DataZone data portal or catalog access if your domain is encrypted with
  a customer-managed key from AWS Key Management Service (KMS)](#data-portal-permissions-kms "#data-portal-permissions-kms")

## Attach required policy to a user,

group, or role for Amazon DataZone data portal access

You can access the Amazon DataZone data portal by using either your AWS credentials or
your single sign-on (SSO) credentials. Follow the instructions in the section below to
set up the permissions required to access the data portal with your AWS credentials.
For more information about using Amazon DataZone with SSO, see [Setting up AWS IAM Identity Center for Amazon DataZone](sso-setup.md "sso-setup.md").

###### Note

Only IAM principals in your domain's AWS account can access the domain's data
portal. IAM principals from other AWS accounts cannot access the domain's data
portal.

Complete the following procedure to attach the required policy to a user, group, or a
role. For more information, see [AWS managed policies for Amazon DataZone](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users, User groups, or
   Roles**.
3. In the list, choose the name of the user, group, or role in which to embed a
   policy.
4. Choose the **Permissions** tab and, if necessary, expand the
   **Permissions policies** section.
5. Choose **Add permissions** and **Create inline
   policy** link.
6. On the **Create Policy** screen, in the Policy
   editor section, choose **JSON**. Create a policy
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
 "datazone:GetIamPortalLoginUrl"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

7. On the **Review policy** screen, enter a name for the policy.
   When you're satisfied with the policy, choose **Create policy**.
   Ensure that no errors appear in a red box at the top of the screen. Correct any
   that are reported.

## Attach required policy to a user,

group, or role for Amazon DataZone catalog access

###### Note

Only IAM principals in your domain's AWS account can access the domain's
catalog. IAM principals from other AWS accounts cannot access the domain's
catalog.

You can grant your IAM identities access to your Amazon DataZone domain’s catalog via
API and the SDK with the following procedure. If you want these IAM identities to also
have access to the Amazon DataZone data portal, then additionally follow the procedure
above to [Attach required policy to a user,
group, or role for Amazon DataZone data portal access](#data-portal-permissions-portal "#data-portal-permissions-portal"). For more information, see [AWS managed policies for Amazon DataZone](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, select the radio button next to the
   **AmazonDataZoneFullUserAccess** policy. You can use the
   **Filter** menu and the search box to filter the list of
   policies. For more information, see [AWS managed
   policy: AmazonDataZoneFullUserAccess](security-iam-awsmanpol-AmazonDataZoneFullUserAccess.md "security-iam-awsmanpol-AmazonDataZoneFullUserAccess.md")
4. Choose **Actions**, and then choose
   **Attach**.
5. Choose the user, group, or role to which you want to attach the policy by
   selecting the checkbox next to each principal. You can use the
   **Filter** menu and the search box to filter the list of
   principal entities. After choosing the user, group, or role, choose
   **Attach policy**.

## Attach optional policy to a user, group,

or role for Amazon DataZone data portal or catalog access if your domain is encrypted with
a customer-managed key from AWS Key Management Service (KMS)

If you create your Amazon DataZone domain with your own KMS key for data encryption, you
must also create an inline policy with the following permissions and attach it to your
IAM principals so they can access the Amazon DataZone data portal or catalog.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users, User groups, or
   Roles**.
3. In the list, choose the name of the user, group, or role in which to embed a
   policy.
4. Choose the **Permissions** tab and, if necessary, expand the
   **Permissions policies** section.
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
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 ]
 }
 ]
}`

```

7. On the **Review policy** screen, enter a name for the policy.
   When you're satisfied with the policy, choose **Create policy**.
   Ensure that no errors appear in a red box at the top of the screen. Correct any
   that are reported.
