After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# AWS managed policies for Amazon FinSpace

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: AWSFinSpaceServiceRolePolicy

You can't attach AWSFinSpaceServiceRolePolicy to your IAM entities. This policy is attached to a
service-linked role that allows FinSpace to perform actions on your behalf. For more
information, see [Using service-linked roles for
FinSpace](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants FinSpace permissions to publish metrics.

**Permissions details**

This policy includes the following permission.

- `cloudwatch` – Allows principals access to publish metrics to
  the AWS/FinSpace and AWS/Usage namespace in the AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/FinSpace",
 "AWS/Usage"
 ]
 }
 },
 "Resource": "*"
 }
 ]
}`

```

## FinSpace updates to AWS managed

policies

View details about updates to AWS managed policies for FinSpace since this service
began tracking these changes.

| Change                                                                                                                                                       | Description                                                                                                    | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSFinSpaceServiceRolePolicy](#security-iam-awsmanpol-AWSFinSpaceServiceRolePolicy "#security-iam-awsmanpol-AWSFinSpaceServiceRolePolicy") – Updated policy | Updated the `AWSServiceRoleForFinSpace` policy to allow PutMetricData calls to AWS/Usage CloudWatch namespace. | November 17, 2023 |
| [AWSFinSpaceServiceRolePolicy](#security-iam-awsmanpol-AWSFinSpaceServiceRolePolicy "#security-iam-awsmanpol-AWSFinSpaceServiceRolePolicy") – New policy     | FinSpace added a new policy to enable access to AWS service and resources used or managed by Amazon FinSpace.  | June 5, 2023      |
| FinSpace started tracking changes                                                                                                                            | FinSpace started tracking changes for its AWS managed policies.                                                | June 5, 2023      |
