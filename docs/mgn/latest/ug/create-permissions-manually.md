NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Create roles manually

To create permissions manually, you create the **AWSApplicationMigrationConnectorManagementRole** needed to install and run the connector. The connector assumes the **AWSApplicationMigrationConnectorSharingRole\_management-account-id** role as needed, for example, to install the replication agent on a source server.

###### Note

The **MGNConnectorInstallerRole** is no longer required and does not need to be created. The permissions to register the connector (`mgn:CreateConnector` and `mgn:TagResource`) are included in the **MgnConnectorPolicy** below. The connector installer obtains the **AWSApplicationMigrationConnectorManagementRole** credentials from the AWS Systems Manager agent, which is registered using the SSM hybrid activation.

## AWSApplicationMigrationConnectorManagementRole

The **AWSApplicationMigrationConnectorManagementRole** role is the role that is assumed by the Connector. The connector installer uses this role's credentials, provided by the AWS Systems Manager agent, to register the connector with MGN.

To create the role:

1. After replacing **ACCOUNT-ID** with your account number, and **AWS\_REGION** with the connector region, create a policy from the following JSON:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "mgn:CreateConnector",
            "Resource": "arn:aws:mgn:AWS_REGION:ACCOUNT-ID:*",
            "Effect": "Allow"
        },
        {
            "Action": "mgn:TagResource",
            "Resource": "arn:aws:mgn:AWS_REGION:ACCOUNT-ID:connector/*",
            "Effect": "Allow",
            "Condition": {
                "StringEquals": {
                    "mgn:CreateAction": "CreateConnector"
                }
            }
        },
        {
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::*:role/AWSApplicationMigrationConnectorSharingRole_ACCOUNT-ID",
            "Effect": "Allow"
        },
        {
            "Condition": {
                "Null": {
                    "aws:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                }
            },
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "arn:aws:secretsmanager:AWS_REGION:ACCOUNT-ID:secret:*",
            "Effect": "Allow"
        },
        {
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::aws-application-migration-service-AWS_REGION/latest/source-automation-client/linux/ssaf-client/ssaf_client",
                "arn:aws:s3:::amazon-ssm-AWS_REGION/*"
            ],
            "Effect": "Allow"
        }
    ]
}
```

2. If you created an S3 bucket for SSM logging, replace **LOGS-BUCKET** with the bucket name and append the following to the policy:

```
{
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::LOGS-BUCKET/*",
    "Effect": "Allow"
}
```

3. In order for the MGN connector to send logs to CloudWatch, append this statement to the policy:

```
{
    "Effect": "Allow",
    "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams",
        "logs:PutLogEvents"
    ],
    "Resource": "*"
}
```

4. Name the policy **MgnConnectorPolicy**
5. Create a role with the following trust relationship:

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

6. Attach the following policies:

   1. **AmazonSSMManagedInstanceCore**
   2. **MgnConnectorPolicy**

7. Name the role **AWSApplicationMigrationConnectorManagementRole**

## AWSApplicationMigrationConnectorSharingRole\_management-account-id

The **AWSApplicationMigrationConnectorSharingRole\_management-account-id** role is assumed by the **AWSApplicationMigrationConnectorManagementRole** to perform actions on source servers in member accounts. The role name includes the ID of the account that owns the connector (the management account), which allows a single member account to hold sharing roles for multiple management accounts.

To create the role:

1. Create a policy from the following JSON:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "mgn:StartAgentless",
            "Resource": "arn:aws:mgn:*:*:source-server/*"
        }
    ]
}
```

2. Name the policy **AWSApplicationMigrationAgentInstallationPolicy**.
3. Create a role with the following trust relationship, where _management-account-id_ is the account in which the connector was created:

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

4. Attach the **AWSApplicationMigrationAgentInstallationPolicy** policy to the Permission policies.
5. Name the role **AWSApplicationMigrationConnectorSharingRole\_management-account-id**, replacing _management-account-id_ with the ID of the account in which the connector was created.
