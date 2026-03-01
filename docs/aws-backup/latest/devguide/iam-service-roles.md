# IAM service roles

An AWS Identity and Access Management (IAM) role is similar to a user, in that it is an AWS identity with
permissions policies that determine what the identity can and cannot do in AWS. However,
instead of being uniquely associated with one person, a role is intended to be assumable by
anyone who needs it. A service role is a role that an AWS service assumes to perform
actions on your behalf. As a service that performs backup operations on your behalf, AWS Backup
requires that you pass it a role to assume when performing backup operations on your behalf.
For more information about IAM roles, see [IAM
Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _IAM User Guide_.

The role that you pass to AWS Backup must have an IAM policy with the permissions that
enable AWS Backup to perform actions associated with backup operations, such as creating,
restoring, or expiring backups. Different permissions are required for each of the AWS
services that AWS Backup supports. The role must also have AWS Backup listed as a trusted entity,
which enables AWS Backup to assume the role.

When you assign resources to a backup plan, or if you perform an on-demand backup, copy,
or restore, you must pass a service role that has access to perform the underlying
operations on the specified resources. AWS Backup uses this role to create, tag, and delete
resources in your account.

## Using AWS roles to control access to backups

You can use roles to control access to your backups by defining narrowly scoped roles
and by specifying who can pass that role to AWS Backup. For example, you could create a role
that only grants permissions to back up Amazon Relational Database Service (Amazon RDS) databases and only grant Amazon RDS
database owners permission to pass that role to AWS Backup. AWS Backup provides several predefined
managed policies for each of the supported services. You can attach these managed policies
to roles that you create. This makes it easier to create service-specific roles that have
the correct permissions that AWS Backup needs.

For more information about AWS managed policies for AWS Backup, see [Managed policies for AWS Backup](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Default service role for AWS Backup

When using the AWS Backup console for the first time, you can choose to have AWS Backup create a
default service role for you. This role has the permissions that AWS Backup needs to create
and restore backups on your behalf.

###### Note

The default role is automatically created when you use the AWS Management Console.
You can create the default role using the AWS Command Line Interface (AWS CLI), but it must be done
manually.

If you prefer to use custom roles, such as separate roles for different resource
types, you can also do that and pass your custom roles to AWS Backup. To view examples of roles
that enable backup and restore for individual resource types, see the [Customer managed policies](security-iam-awsmanpol.md#customer-managed-policies "security-iam-awsmanpol.md#customer-managed-policies")
table.

The default service role is named `AWSBackupDefaultServiceRole`. This service role
contains two managed policies, [AWSBackupServiceRolePolicyForBackup](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.md")
and [AWSBackupServiceRolePolicyForRestores](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md").

`AWSBackupServiceRolePolicyForBackup` includes an IAM policy that grants
AWS Backup permissions to describe the resource being backed up, the ability to create, delete,
describe, or add tags to a backup regardless of the AWS KMS key with which it is encrypted.

`AWSBackupServiceRolePolicyForRestores` includes an IAM policy that
grants AWS Backup permissions to create, delete, or describe the new resource being created
from a backup, regardless of the AWS KMS key with which it is encrypted.
It also includes permissions to tag the newly created resource.

To restore an Amazon EC2 instance, you must launch a new instance.

## Creating the default service role in the console

Specific actions you take in the AWS Backup Console create the AWS Backup default service role.

###### To create the AWS Backup default service role in your AWS account

1.  Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2.  To create the role for your account, either assign resources to a backup plan or
    create an on-demand backup.
    1. Create a backup plan and assign resources to the backup. See [Create a backup
       plan](creating-a-backup-plan.md "creating-a-backup-plan.md").
    2. Alternatively, create an on-demand backup. See [Create an
       on-demand backup](create-on-demand-backup.md "create-on-demand-backup.md").

3.  Verify that you have created the `AWSBackupDefaultServiceRole` in your
    account by following these steps:
    1. Wait a few minutes. For more information, see [Changes that I make are not always immediately visible](../../../IAM/latest/UserGuide/troubleshoot_general.md#troubleshoot_general_eventual-consistency "../../../IAM/latest/UserGuide/troubleshoot_general.md#troubleshoot_general_eventual-consistency") in the
       _AWS Identity and Access Management User Guide._
    2. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    3. In the left navigation menu, choose **Roles**.
    4. In the search bar, type `AWSBackupDefaultServiceRole`. If this
       selection exists, you have created the AWS Backup default role and completed this
       procedure.
    5. If `AWSBackupDefaultServiceRole` still does not appear, add the
       following permissions to either the IAM user or IAM role you use to access the
       console.

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement":[
     {
     "Effect":"Allow",
     "Action":[
     "iam:CreateRole",
     "iam:AttachRolePolicy",
     "iam:PassRole"
     ],
     "Resource":"arn:`aws`:iam::*:role/service-role/AWSBackupDefaultServiceRole"
     },
     {
     "Effect":"Allow",
     "Action":[
     "iam:ListRoles"
     ],
     "Resource":"*"
     }
     ]
    }`

    ```

    For China Regions, replace `aws` with
    `aws-cn`. For AWS GovCloud (US) Regions, replace
    `aws` with
    `aws-us-gov`. 6. If you cannot add permissions to your IAM user or IAM role, ask your
    administrator to manually create a role with a name _other
    than_
    `AWSBackupDefaultServiceRole` and attach that role to these managed
    policies:

        * `AWSBackupServiceRolePolicyForBackup`
        * `AWSBackupServiceRolePolicyForRestores`
