# AWS managed policies for zonal autoshift in ARC

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

## AWS managed policy: AWSZonalAutoshiftPracticeRunSLRPolicy

You can't attach `AWSZonalAutoshiftPracticeRunSLRPolicy` to your IAM entities.
This policy is attached to a service-linked role that allows Amazon Application Recovery Controller (ARC) to do the following for zonal autoshift:

- Monitor customer-provided Amazon CloudWatch alarms and customer AWS Health Dashboard events for practice runs
- Manage practice runs (practice zonal shifts)
- Manage balanced capacity checks for practice runs and autoshifts

For more information, see
[Using the service-linked role for zonal autoshift in ARC](using-service-linked-roles-zonal-autoshift.md "using-service-linked-roles-zonal-autoshift.md").

## Updates for AWS managed

policies for zonal autoshift

For details about updates to AWS managed policies for zonal autoshift in ARC since this service
began tracking these changes, see [Updates to AWS managed
policies for Amazon Application Recovery Controller (ARC)](security-iam-awsmanpol.md#security-iam-awsmanpol-arc-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-arc-updates"). For automatic alerts about changes to this page, subscribe to
the RSS feed on the ARC [Document history page](doc-history.md "doc-history.md").
