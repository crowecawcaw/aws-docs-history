# AWS managed policies for Amazon WorkMail

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

## AWS managed policy: AmazonWorkMailFullAccess

You can attach the `AmazonWorkMailFullAccess` policy to your IAM identities.
This policy grants permissions that allow full access to Amazon WorkMail.

To view the permissions for this policy, see [AmazonWorkMailFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonWorkMailFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonWorkMailFullAccess") in the AWS Management Console.

## AWS managed policy: AmazonWorkMailReadOnlyAccess

You can attach the `AmazonWorkMailReadOnlyAccess` policy to your IAM identities.
This policy grants permissions that allow read-only access to Amazon WorkMail.

To view the permissions for this policy, see [AmazonWorkMailReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonWorkMailReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonWorkMailReadOnlyAccess") in the AWS Management Console.

## AWS managed policy: AmazonWorkMailEventsServiceRolePolicy

This policy is attached to the service-linked role named **AmazonWorkMailEvents**
to allow access to AWS services and resources used or managed by Amazon WorkMail events. For more information, see [Using service-linked roles for
Amazon WorkMail](using-service-linked-roles.md "using-service-linked-roles.md").

## Amazon WorkMail updates to AWS managed policies

View details about updates to AWS managed policies for Amazon WorkMail since this service
began tracking these changes.

| Change                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    | Date              |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| AWS managed policy updates - Update to an existing policy | The `AmazonWorkMailReadOnlyAccess` and `AmazonWorkMailFullAccess` permissions were updated for Amazon WorkMail to support _audit logging_. For more information on the updated permissions, see [Amazon WorkMail identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md") and for information on audit logging, see [Enabling audit logging](audit-logging.md "audit-logging.md"). | February 14, 2024 |
| Amazon WorkMail started tracking changes                  | Amazon WorkMail started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                         | March 1, 2021     |
