This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# AWS managed policies for AWS Wickr

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

## AWS managed policy:

AWSWickrFullAccess

You can attach the `AWSWickrFullAccess` policy to your IAM identities. This
policy grants full administrative permission to the Wickr service, including the
AWS Management Console for Wickr in the AWS Management Console. For more information about attaching policies to an
identity, see [Adding and removing
IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User
Guide_.

**Permissions details**

This policy includes the following permissions.

- `wickr` – Grants full administrative permission to the Wickr
  service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "wickr:*",
 "Resource": "*"
 }
 ]
}`

```

## Wickr updates to AWS managed

policies

View details about updates to AWS managed policies for Wickr since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Wickr Document history page.

| Change                                                                                                                     | Description                                                                                                                                                              | Date              |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [AWSWickrFullAccess](#security-iam-awsmanpol-AWSWickrFullAccess "#security-iam-awsmanpol-AWSWickrFullAccess") – New policy | Wickr added a new policy that grants full administrative permission to<br>the Wickr service, including the Wickr administrator console in the<br>AWS Management Console. | November 28, 2022 |
| Wickr started tracking changes                                                                                             | Wickr started tracking changes for its AWS managed policies.                                                                                                             | November 28, 2022 |
