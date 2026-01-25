# Get started with AWS Systems Manager for SAP

To get started with using AWS Systems Manager for SAP, ensure that you complete the following prerequisites for setup. You must run these steps on all Amazon EC2 instances in your setup.

###### Topics

- [Attach Systems Manager for SAP permissions to Amazon EC2 instance running SAP HANA database](#ec2-permissions "#ec2-permissions")
- [Amazon EC2 tag](#ec2-tag "#ec2-tag")
- [Identify or create SAP HANA user](#identify-create-hana-user "#identify-create-hana-user")
- [Register SAP HANA database credentials in AWS Secrets Manager](#register-secrets "#register-secrets")
- [Verify AWS Systems Manager Agent (SSM Agent) is running](#verify-ssm-agent "#verify-ssm-agent")
- [Verify setup before registering your SAP HANA database](#verification "#verification")
- [Backup and restore – optional](#backup-restore "#backup-restore")

## Attach Systems Manager for SAP permissions to Amazon EC2 instance running SAP HANA database

AWS Systems Manager for SAP communicates with the Amazon EC2 instance where your SAP HANA database running via policies. Attach the following IAM policies to the IAM role used by your Amazon EC2 instance.

- `AmazonSSMManagedInstanceCore` – this Amazon managed policy allows an instance to use Systems Manager service core functionality. For more information, see [About policies for a Systems Manager instance profile](../../../systems-manager/latest/userguide/setup-instance-profile.md#instance-profile-policies-overview "../../../systems-manager/latest/userguide/setup-instance-profile.md#instance-profile-policies-overview").
- `AWSSystemsManagerForSAPFullAccess` – this Amazon managed policy grants full access to AWS Systems Manager for SAP. For more information, see [AWS managed policy: AWSSystemsManagerForSAPFullAccess](iam-policies.md#security-iam-awsmanpol-AWSSystemsManagerForSAPFullAccess "iam-policies.md#security-iam-awsmanpol-AWSSystemsManagerForSAPFullAccess").

## Amazon EC2 tag

`SSMForSAPManaged` – add this tag on your Amazon EC2 instance to enable AWS Systems Manager for SAP to access your Amazon EC2 instance.

|       |                    |
| ----- | ------------------ |
| Key   | `SSMForSAPManaged` |
| Value | `True`             |

## Identify or create SAP HANA user

The SAP HANA database user credentials that you provide to AWS Systems Manager for SAP must have specific privileges based on the operations you intend to perform.

You must provide credentials for the SYSTEM_DB user, which requires [SAP HANA system privileges](https://help.sap.com/docs/SAP_BW4HANA/900e6cdd1edb48448d0a25075eae9ac0/a20457c7784948928e4c320c33d77948.html?locale=en-US "https://help.sap.com/docs/SAP_BW4HANA/900e6cdd1edb48448d0a25075eae9ac0/a20457c7784948928e4c320c33d77948.html?locale=en-US"). The following table shows the required privileges for different operations:

| Operation                              | Required Privileges        |
| -------------------------------------- | -------------------------- |
| Application registration and discovery | CATALOG READ               |
| Backup operations with AWS Backup      | BACKUP ADMIN, INFILE ADMIN |

You can use an existing SYSTEM_DB user with the required privileges, or create a new dedicated user for AWS Systems Manager for SAP operations. Optionally, you can also provide credentials for individual tenant database users.

When creating or identifying the SAP HANA user, ensure that the password does not contain the following special characters:

- angle brackets (<>)
- backslashes (/)
- double quotes (")
- pipelines (|)
- question marks (?)
- semicolons (;)

## Register SAP HANA database credentials in AWS Secrets Manager

You must create a secret with the username and password of the SAP HANA users identified or created in the previous section. A separate secret is required for each user of your databases running on an Amazon EC2 instance.

Use the following steps to register your SAP HANA database credentials in AWS Secrets Manager.

1. Sign in to https://console.aws.amazon.com/secretsmanager/.
2. On the AWS Secrets Manager page, select **Store a new secret**.
3. For Secret type, select **Other type of secret** and create the following key value pairs.

|          |                                  |
| -------- | -------------------------------- |
| Key      | Value                            |
| username | `<example_SAP_HANA_db_username>` |
| password | `<example_SAP_HANA_db_password>` |

4. Select **Next** and enter a Secret name. Note this Secret name for use while following the steps in [Register your SAP HANA databases with Systems Manager for SAP](register-database.md "register-database.md").
5. In the **Resource permissions** container, choose **Edit permissions**, and paste the following policy with your Amazon Resource Name for the Amazon EC2 instance role.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456789012:role/EC2RoleToAccessSecrets"
                ]
            },
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "*"
        }
    ]
}
```

This policy enables the IAM role used by your Amazon EC2 instance access to this secret. For more details, see [Attach a permissions policy to an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md "../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md").

###### Note

You must attach this policy to each secret that you create for your SAP HANA database credentials. 6. Select **Next** and then, select **Store**.

## Verify AWS Systems Manager Agent (SSM Agent) is running

Use the following command to verify the status of the SSM Agent on your instance.

```
$ sudo systemctl status amazon-ssm-agent
```

Your output should display _active (running)_ as seen here.

```
amazon-ssm-agent.service - amazon-ssm-agent
     Loaded: loaded (/usr/lib/systemd/system/amazon-ssm-agent.service; enabled; vendor preset: disabled)
     Active: active (running) since Tue 2022-02-15 18:56:26 UTC; 12s ago
     ^^^^^^^^^^^^^^^^^^^^^^^^ You should expect to see "active (running)".
   Main PID: 16061 (amazon-ssm-agen)
      Tasks: 36
     CGroup: /system.slice/amazon-ssm-agent.service
             ├─16061 /usr/sbin/amazon-ssm-agent
             └─16069 /usr/sbin/ssm-agent-worker
```

AWS Systems Manager Agent (SSM Agent) is pre-installed in several Amazon Machine Images (AMIs) provided by AWS. For more information, see [Working with SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").

## Verify setup before registering your SAP HANA database

- Ensure that you are running SAP HANA 2.x.
- Ensure that your Amazon EC2 instance has `/run` mount point mounted on `tmpfs`. Use the `df | grep tmpfs` command for verification.
- Ensure that your EC2 instance has Python 3.5 or later installed. SSM-SAP automatically uses the latest Python version available on your system. For custom-built or compiled Python installations, ensure that the \_lzma module is included in the build and available within your Python environment.
- Ensure that the `hdbcli` Python library is installed in the `/opt/aws/ssm-sap/` directory on your Amazon EC2 instance, if the revision of your SAP HANA 2.0 server is below 056.00.
- Ensure that the boto3 version is higher than 1.7.0 if boto3 is installed.

To register your database, see [Register your SAP HANA database with AWS Systems Manager for SAP](register-database.md "register-database.md").

## Backup and restore – _optional_

After registering your database, you can optionally choose to complete the prerequisites required to backup and restore your database. You must run these steps on all Amazon EC2 instances in your setup.

###### Topics

- [Set up required permissions for Amazon EC2 instance for backup and restore of SAP HANA database](#backup-permissions "#backup-permissions")
- [Install AWS Backint Agent for SAP HANA with AWS Systems Manager Agent (SSM Agent) on your SAP application server](#install-agents "#install-agents")

### Set up required permissions for Amazon EC2 instance for backup and restore of SAP HANA database

To backup and restore your SAP HANA databases running on Amazon EC2 instance, attach the following IAM policies to the IAM role used by your Amazon EC2 instance.

- `AWSBackupDataTransferAccess` – this Amazon managed policy must be attached to the IAM role of Amazon EC2 instance where AWS Backint Agent for SAP HANA is located. AWS Backint Agent uses this IAM role to transfer data for backup and restore. For more information about the policy, see [Managed policies for AWS Backup](../../../aws-backup/latest/devguide/security-iam-awsmanpol.md#aws-managed-policies "../../../aws-backup/latest/devguide/security-iam-awsmanpol.md#aws-managed-policies").
- `AWSBackupRestoreAccessForSAPHANA` – this Amazon managed policy enables access to restore your SAP HANA database using AWS Backup.
  - If you are going to use AWS Backup console for the restore process, attach this policy to the IAM role using the console.
  - If you are going to use AWS API for the restore process, attach this policy to the IAM role performing the API call.
  - Follow the recommended best practice of granting least privilege necessary for each role by attaching the `AWSBackupRestoreAccessForSAPHANA` policy only to the SAP HANA resource owner.

- `AWSBackupServiceRolePolicyForBackup` – this Amazon managed policy must be attached to the role that will passed to `StartBackupJob` or `DefaultRole`. For more information, see [Service-linked role permissions for AWS Backup](../../../aws-backup/latest/devguide/using-service-linked-roles-AWSServiceRoleForBackup.md#service-linked-role-permissions-AWSServiceRoleForBackup "../../../aws-backup/latest/devguide/using-service-linked-roles-AWSServiceRoleForBackup.md#service-linked-role-permissions-AWSServiceRoleForBackup"). The policy must contain the following trust relation.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "backup.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

### Install AWS Backint Agent for SAP HANA with AWS Systems Manager Agent (SSM Agent) on your SAP application server

Follow along the steps described in AWS Backint Agent for SAP HANA documentation. For more information, see [Install and configure AWS Backint Agent for SAP HANA](../../../sap/latest/sap-hana/aws-backint-agent-backup.md#backint-backup-install "../../../sap/latest/sap-hana/aws-backint-agent-backup.md#backint-backup-install").
