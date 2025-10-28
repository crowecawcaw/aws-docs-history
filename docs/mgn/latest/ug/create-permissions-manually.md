NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Create permissions manually

To create permissions manually, you create the MGNConnectorInstallerRole to install the MGN Connector and the AWSApplicationMigrationConnectorManagementRole for the MGN Connector to assume.

## Create the MGNConnectorInstallerRole

The **MGNConnectorInstallerRole** role is used to install the Connector.
The user or identity that installs the Connector will require permission to assume this role.

To create the role:

1. Create a policy from the following JSON:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "mgn:TagResource"
 ],
 "Resource": "arn:aws:mgn:*:*:connector/*",
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "mgn:CreateAction": "CreateConnector"
 }
 }
 },
 {
 "Action": [
 "mgn:CreateConnector"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

2. Name the policy **MGNConnectorInstallerPolicy**.
3. Create a role with your account as the trusted entity.
   Alternatively use a custom trust policy that will grant the user or identity that will install the Connector, permission
   to assume this role.
4. Attach the **MGNConnectorInstallerPolicy** policy to the Permission policies.
5. Name the role **MGNConnectorInstallerRole**.

## AWSApplicationMigrationConnectorManagementRole

The **AWSApplicationMigrationConnectorManagementRole** role is the role that is initially assumed by the Connector.

To create the role:

1. After replacing **ACCOUNT-ID** with your account number,
   and **AWS_REGION** with the connector region,
   create a policy from the following JSON:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
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
 "Resource": "arn:aws:secretsmanager:*:*:secret:*",
 "Effect": "Allow"
 },
 {
 "Action": "s3:GetObject",
 "Resource":
 ["arn:aws:s3:::aws-application-migration-service-AWS_REGION/latest/source-automation-client/linux/ssaf-client/ssaf_client",
 "arn:aws:s3:::amazon-ssm-AWS_REGION/*"],
 "Effect": "Allow"
 }
 ]
}`

```

2. If you have created an S3 bucket for SSM logging, replace **LOGS-BUCKET** with the bucket name and append the following statements to the above policy:

```
{
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::LOGS-BUCKET/*",
    "Effect": "Allow"
}
```

3. In order for the MGN connector to send logs to CloudWatch, append the following statement to the above policy:

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

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

6. Attach the following policies:
   1. **AmazonSSMManagedInstanceCore**
   2. **MgnConnectorPolicy**

7. Name the role **AWSApplicationMigrationConnectorManagementRole**
