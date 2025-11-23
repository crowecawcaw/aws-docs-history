# Prerequisites for enrollment

_This section describes how to
enroll an existing AWS account into AWS Control Tower if you have not selected the optional
auto-enroll feature on the landing zone **Settings** page, or if you are
operating with a landing zone version previous to 3.1._

These prerequisites are required before you can enroll an existing AWS account in
AWS Control Tower:

###### Note

The prerequisite to add the `AWSControlTowerExecution` role is not
required if you have activated the AWS Control Tower auto-enroll capability in the landing zone
**Settings** page, or if you are enrolling the account as part
of a **Register OU** process. However, in all cases, the account to
be enrolled may not have existing AWS Config resources. See [Enroll
accounts that have existing AWS Config resources](existing-config-resources.md "existing-config-resources.md")

1. To enroll an existing AWS account, the `AWSControlTowerExecution`
   role must be present in the account you are enrolling. You can review [Enroll
   an account](quick-account-provisioning.md "quick-account-provisioning.md") for details and instructions.
2. In addition to the `AWSControlTowerExecution` role, the existing
   AWS account you want to enroll must have the following permissions and trust
   relationships in place. Otherwise, enrollment will fail.

Role Permission: `AdministratorAccess` (AWS managed
policy)

**Role Trust Relationship:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::``111122223333``:root"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

3. We recommend that the account should not have an AWS Config configuration
   recorder or delivery channel. These may be deleted or modified through the AWS CLI
   before you can enroll an account. Otherwise, review [Enroll
   accounts that have existing AWS Config resources](existing-config-resources.md "existing-config-resources.md") for instructions on how
   you can modify your existing resources.
4. The account that you wish to enroll must exist in the same AWS Organizations
   organization as the AWS Control Tower management account. The account that exists can be
   enrolled _only_ into the same organization as
   the AWS Control Tower management account, in an OU that already is registered with
   AWS Control Tower.
   To check other prerequisites for enrollment, see [Getting
   Started with AWS Control Tower](getting-started-with-control-tower.md "getting-started-with-control-tower.md").

###### Note

When you enroll an account into AWS Control Tower, your account is governed by the AWS CloudTrail
trail for the AWS Control Tower organization. If you have an existing deployment of a CloudTrail
trail, you may see duplicate charges unless you delete the existing trail for the
account before you enroll it in AWS Control Tower.

**About trusted access with the `AWSControTowerExecution` role**

Before you can enroll an existing AWS account into AWS Control Tower you must give permission for
AWS Control Tower to manage, or _govern_, the account. Specifically,
AWS Control Tower requires permission to establish trusted access between AWS CloudFormation and AWS Organizations on
your behalf, so that CloudFormation can deploy your stack automatically to the accounts in your
selected organization. With this trusted access, the `AWSControlTowerExecution`
role conducts activities required to manage each account. That's why you must add this role
to each account before you enroll it.

When trusted access is enabled, CloudFormation can create, update, or delete stacks across
multiple accounts and AWS Regions with a single operation. AWS Control Tower relies on this trust
capability so it can apply roles and permissions to existing accounts before it moves them
into a registered organizational unit, and thereby brings them under governance.

To learn more about trusted access and AWS CloudFormation StackSets, see [AWS CloudFormationStackSets and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudformation.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudformation.md").
