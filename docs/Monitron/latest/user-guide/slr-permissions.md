Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Service-linked role permissions for

Amazon Monitron

Amazon Monitron uses the service-linked role named
**AWSServiceRoleForMonitron[\_{SUFFIX}]** – Amazon Monitron uses AWSServiceRoleForMonitron to access other AWS services, including Cloudwatch Logs, Kinesis Data Streams, KMS keys, and SSO. For more information about
the policy, see [AWSServiceRoleForMonitronPolicy](../../../aws-managed-policy/latest/reference/AWSServiceRoleForMonitronPolicy.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForMonitronPolicy.md") in the _AWS Managed
Policy Reference Guide_

The AWSServiceRoleForMonitron[\_{SUFFIX}] service-linked role trusts the following services to assume the
role:

- `monitron.amazonaws.com` or
  `core.monitron.amazonaws.com`
  The role permissions policy named MonitronServiceRolePolicy allows Amazon Monitron to
  complete the following actions on the specified resources:

- Action: Amazon CloudWatch Logs `logs:CreateLogGroup`,
  `logs:CreateLogStream` and `logs:PutLogEvents`
  on the CloudWatch log group, log stream, and log events under /aws/monitron/\*
  path
  The role permissions policy named
  MonitronServiceDataExport-KinesisDataStreamAccess allows Amazon Monitron to complete the
  following actions on the specified resources:

- Action: Amazon Kinesis `kinesis:PutRecord`,
  `kinesis:PutRecords`, and
  `kinesis:DescribeStream` on the Kinesis data stream
  specified for live data export.
- Action: Amazon AWS KMS `kms:GenerateDataKey` for the AWS KMS
  key used by the specified Kinesis data stream for live data
  export
- Action: Amazon IAM `iam:DeleteRole` to delete the
  service-linked role itself when not used
  The role permissions policy named AWSServiceRoleForMonitronPolicy allows Amazon Monitron
  to complete the following actions on the specified resources:

- Action: IAM Identity Center `sso:GetManagedApplicationInstance`,
  `sso:GetProfile`, `sso:ListProfiles`,
  `sso:AssociateProfile`,
  `sso:ListDirectoryAssociations`,
  `sso:ListProfileAssociations`,
  `sso-directory:DescribeUsers`,
  `sso-directory:SearchUsers`,
  `sso:CreateApplicationAssignment`, and
  `sso:ListApplicationAssignments` to access IAM Identity Center users
  associated with the project

###### Note

Add `sso:ListProfileAssociations` to allow Amazon Monitron to
list associations with the application instance underlying the Amazon Monitron
Project.

You must configure permissions to allow an IAM entity (such as a user,
group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.
