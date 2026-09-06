

# IAM service roles
<a name="iam-service-roles"></a>

An AWS Identity and Access Management (IAM) role is similar to a user, in that it is an AWS identity with permissions policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. A service role is a role that an AWS service assumes to perform actions on your behalf. As a service that performs backup operations on your behalf, AWS Backup requires that you pass it a role to assume when performing backup operations on your behalf. For more information about IAM roles, see [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide*. 

The role that you pass to AWS Backup must have an IAM policy with the permissions that enable AWS Backup to perform actions associated with backup operations, such as creating, restoring, or expiring backups. Different permissions are required for each of the AWS services that AWS Backup supports. The role must also have AWS Backup listed as a trusted entity, which enables AWS Backup to assume the role. 

When you assign resources to a backup plan, or if you perform an on-demand backup, copy, or restore, you must pass a service role that has access to perform the underlying operations on the specified resources. AWS Backup uses this role to create, tag, and delete resources in your account.

## Using AWS roles to control access to backups
<a name="using-roles-to-control-access"></a>

You can use roles to control access to your backups by defining narrowly scoped roles and by specifying who can pass that role to AWS Backup. For example, you could create a role that only grants permissions to back up Amazon Relational Database Service (Amazon RDS) databases and only grant Amazon RDS database owners permission to pass that role to AWS Backup. AWS Backup provides several predefined managed policies for each of the supported services. You can attach these managed policies to roles that you create. This makes it easier to create service-specific roles that have the correct permissions that AWS Backup needs. 

For more information about AWS managed policies for AWS Backup, see [Managed policies for AWS Backup](security-iam-awsmanpol.md).

## Default service role for AWS Backup
<a name="default-service-roles"></a>

When using the AWS Backup console for the first time, you can choose to have AWS Backup create a default service role for you. This role has the permissions that AWS Backup needs to create and restore backups on your behalf.

**Note**  
The default role is automatically created when you use the AWS Management Console. You can create the default role using the AWS Command Line Interface (AWS CLI), but it must be done manually.

If you prefer to use custom roles, such as separate roles for different resource types, you can also do that and pass your custom roles to AWS Backup. To view examples of roles that enable backup and restore for individual resource types, see the [Customer managed policies](security-iam-awsmanpol.md#customer-managed-policies) table.

The default service role is named `AWSBackupDefaultServiceRole`. This service role contains two managed policies, [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html) and [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html).

`AWSBackupServiceRolePolicyForBackup` includes an IAM policy that grants AWS Backup permissions to describe the resource being backed up, the ability to create, delete, describe, or add tags to a backup regardless of the AWS KMS key with which it is encrypted. 

`AWSBackupServiceRolePolicyForRestores` includes an IAM policy that grants AWS Backup permissions to create, delete, or describe the new resource being created from a backup, regardless of the AWS KMS key with which it is encrypted. It also includes permissions to tag the newly created resource.

To restore an Amazon EC2 instance, you must launch a new instance. 

## Creating the default service role in the console
<a name="creating-default-service-role-console"></a>

 Specific actions you take in the AWS Backup Console create the AWS Backup default service role. 

**To create the AWS Backup default service role in your AWS account**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. To create the role for your account, either assign resources to a backup plan or create an on-demand backup.

   1. Create a backup plan and assign resources to the backup. See [Create a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html).

   1. Alternatively, create an on-demand backup. See [Create an on-demand backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-on-demand-backup.html).

1.  Verify that you have created the `AWSBackupDefaultServiceRole` in your account by following these steps: 

   1. Wait a few minutes. For more information, see [Changes that I make are not always immediately visible](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the *AWS Identity and Access Management User Guide.*

   1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

   1. In the left navigation menu, choose **Roles**.

   1. In the search bar, type `AWSBackupDefaultServiceRole`. If this selection exists, you have created the AWS Backup default role and completed this procedure.

   1. If `AWSBackupDefaultServiceRole` still does not appear, add the following permissions to either the IAM user or IAM role you use to access the console.

------
#### [ JSON ]

****  

      ```
      {
        "Version":"2012-10-17",		 	 	 
        "Statement":[
          {
            "Effect":"Allow",
            "Action":[
              "iam:CreateRole",
              "iam:AttachRolePolicy",
              "iam:PassRole"
            ],
            "Resource":"arn:{{aws}}:iam::*:role/service-role/AWSBackupDefaultServiceRole"
          },
          {
            "Effect":"Allow",
            "Action":[
              "iam:ListRoles"
            ],
            "Resource":"*"
          }
        ]
      }
      ```

------

      For China Regions, replace {{aws}} with {{aws-cn}}. For AWS GovCloud (US) Regions, replace {{aws}} with {{aws-us-gov}}.

   1. If you cannot add permissions to your IAM user or IAM role, ask your administrator to manually create a role with a name *other than* `AWSBackupDefaultServiceRole` and attach that role to these managed policies:
      + `AWSBackupServiceRolePolicyForBackup`
      + `AWSBackupServiceRolePolicyForRestores`