

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Create roles using the MGN console
<a name="create-permissions-console"></a>

When you add an MGN connector using the MGN console, MGN can create the required IAM roles for you. On the **MGN connectors** page, choose **Add connector**, and then select **Create IAM Roles**. MGN creates the following roles:
+ **AWSApplicationMigrationConnectorManagementRole** - created in the current account. This is the role that is assumed by the connector.
+ **AWSApplicationMigrationConnectorSharingRole\_management-account-id** - created in the current account, where *management-account-id* is the ID of the account in which the connector is created. This role is assumed by the connector and by the MGN service to perform actions on source servers, for example, to install the AWS Replication Agent. MGN supports cross-account scenarios: this role must exist in *every* account that contains source servers on which the connector installs agents. If you choose to deploy to all member accounts, the console also creates this role in every member account of your AWS Organization.

**Note**  
The **MGNConnectorInstallerRole** that was previously required to install the connector has been removed and is no longer needed. Its permissions (`mgn:CreateConnector` and `mgn:TagResource`) are now included in the **AWSApplicationMigrationConnectorManagementRole**. When the connector installer runs on the connector machine, it retrieves the **AWSApplicationMigrationConnectorManagementRole** credentials from the AWS Systems Manager agent, which is registered using the SSM hybrid activation, and uses them to register the connector with MGN.

## How MGN creates the roles
<a name="console-how-mgn-creates-roles"></a>

MGN creates the roles using AWS CloudFormation, with the credentials of the currently signed-in user:
+ **Individual account:** MGN creates a CloudFormation stack named **MGNConnectorRoles** in the same AWS Region where you are creating the connector. The stack creates both roles in the current account. IAM roles are global, so the connector can be used in any Region.
+ **Multiple accounts (AWS Organizations):** If you are signed in to the organization's management account, or to a delegated administrator account for CloudFormation StackSets, the console displays an **IAM roles deployment scope** option:
  + **This account only** - Create the IAM roles in this account only.
  + **This account and all member accounts** - In addition to the **MGNConnectorRoles** stack in the current account, MGN creates a service-managed CloudFormation StackSet named **MGNConnectorSharingRoles** that deploys the **AWSApplicationMigrationConnectorSharingRole\_management-account-id** role to all member accounts in your organization. Automatic deployment is enabled, so accounts that later join the organization automatically receive the role. When you run this from the management account, MGN also enables trusted access between AWS Organizations and CloudFormation StackSets if it is not already enabled.

**Note**  
If deployment to some member accounts fails, role creation in the current account is not rolled back. The console displays a warning with a link to the StackSet operation in the CloudFormation console, where you can review and retry the operation on the failed accounts.

## Required permissions
<a name="console-required-permissions"></a>

To have MGN create the roles for you, the signed-in user must have permissions to:
+ Create CloudFormation stacks with named IAM resources (CAPABILITY\_NAMED\_IAM), and create IAM roles and attach policies to them.
+ For deployment to all member accounts: manage CloudFormation StackSets (create/update StackSets and stack instances), call `organizations:ListRoots`, and, from the management account, enable trusted access for CloudFormation StackSets (`organizations:EnableAWSServiceAccess`).

## AWSApplicationMigrationConnectorManagementRole
<a name="console-mgn-connector-management-role"></a>

The **AWSApplicationMigrationConnectorManagementRole** role is the role that is assumed by the connector. The console creates an AWS Systems Manager hybrid activation for this role, and the connector machine registers with Systems Manager as a hybrid managed instance using that activation. From that point, the SSM agent on the connector machine provides the role's credentials to the connector, first to the installer, which registers the connector with MGN (`mgn:CreateConnector`), and then to the connector software for its ongoing operation.

The role is created with the following trust relationship:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

The following policies are attached to the role:

1. **AmazonSSMManagedInstanceCore** (AWS managed policy)

1. **MgnConnectorPolicy** (inline policy)

The **MgnConnectorPolicy** inline policy contains the following permissions, where *ACCOUNT-ID* is the account in which the role is created and *AWS\_REGION* is the Region in which you added the connector:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "mgn:CreateConnector",
            "Resource": "arn:aws:mgn:AWS_REGION:ACCOUNT-ID:*"
        },
        {
            "Effect": "Allow",
            "Action": "mgn:TagResource",
            "Resource": "arn:aws:mgn:AWS_REGION:ACCOUNT-ID:connector/*",
            "Condition": {
                "StringEquals": {
                    "mgn:CreateAction": "CreateConnector"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::*:role/AWSApplicationMigrationConnectorSharingRole_ACCOUNT-ID"
        },
        {
            "Effect": "Allow",
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "arn:aws:secretsmanager:AWS_REGION:ACCOUNT-ID:secret:*",
            "Condition": {
                "Null": {
                    "aws:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::aws-application-migration-service-AWS_REGION/latest/source-automation-client/linux/ssaf-client/ssaf_client",
                "arn:aws:s3:::amazon-ssm-AWS_REGION/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:AWS_REGION:ACCOUNT-ID:log-group:/aws/ssm/*",
                "arn:aws:logs:AWS_REGION:ACCOUNT-ID:log-stream:*"
            ]
        }
    ]
}
```

These permissions allow the connector to:
+ Register itself with MGN (`mgn:CreateConnector`) and tag the connector resource during registration (`mgn:TagResource`). These permissions were previously part of the separate **MGNConnectorInstallerRole**, which is no longer used.
+ Assume the **AWSApplicationMigrationConnectorSharingRole\_ACCOUNT-ID** role in any account in which the role exists, to perform actions on source servers such as installing the AWS Replication Agent.
+ Read source server credentials from AWS Secrets Manager. Access is limited to secrets that are tagged with the `AWSApplicationMigrationServiceManaged` tag.
+ Download the source server automation client and the AWS Systems Manager agent from the AWS owned Amazon S3 buckets.
+ Send connector logs to Amazon CloudWatch Logs, in log groups under the `/aws/ssm/` prefix.

**Note**  
The console-created policy scopes its resources to the connector's account and Region.

## AWSApplicationMigrationConnectorSharingRole\_management-account-id
<a name="console-sharing-role"></a>

The **AWSApplicationMigrationConnectorSharingRole\_management-account-id** role is assumed by the **AWSApplicationMigrationConnectorManagementRole** role and by the MGN service in order to perform actions on source servers in the account, for example, to install the AWS Replication Agent. The role name includes the ID of the account that owns the connector (the management account), which allows a single member account to hold sharing roles for multiple management accounts.

MGN supports cross-account scenarios: the role must exist in *every* account that contains source servers on which the connector installs agents. The console creates the role in the current account, and can deploy it to all member accounts of your AWS Organization. To create the role in an account that the console does not deploy to, for example, an account that is not part of your organization, or when you selected **This account only**, download the Member Account Template and deploy it in that account, as described in [Download the CloudFormation templates](#download-cloudformation-templates).

The role is created with the following trust relationship, where *management-account-id* is the account in which the connector was added:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "mgn.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "management-account-id"
                },
                "StringLike": {
                    "aws:SourceArn": "arn:aws:mgn:*:management-account-id:*"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::management-account-id:role/AWSApplicationMigrationConnectorManagementRole"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

The `aws:SourceAccount` and `aws:SourceArn` conditions limit the MGN service to assuming the role only on behalf of resources in the management account, which protects against the confused deputy problem.

The following policy is attached to the role:

1. **AWSApplicationMigrationAgentInstallationPolicy** (AWS managed policy)

## Download the CloudFormation templates
<a name="download-cloudformation-templates"></a>

If you prefer to review the roles or deploy them in your own workflow, expand **View or deploy roles yourself** in the **IAM Roles** section of the **Add connector** page, and download the CloudFormation templates:
+ **Management Account Template** (`mgn-connector-management-roles.json`), creates both the **AWSApplicationMigrationConnectorManagementRole** and the **AWSApplicationMigrationConnectorSharingRole\_management-account-id** roles. Deploy this template in the account that owns the connector.
+ **Member Account Template** (`mgn-connector-sharing-role.json`), creates only the **AWSApplicationMigrationConnectorSharingRole\_management-account-id** role. Deploy this template in every member account whose source servers the connector manages, for example by using a CloudFormation StackSet.

If you deploy the templates yourself, clear the **Create IAM Roles** check box before you continue.