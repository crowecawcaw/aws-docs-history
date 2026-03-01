# Configuring IAM authentication for RDS Proxy

To set up AWS Identity and Access Management (IAM) authentication for RDS Proxy in Amazon RDS, create and configure an
IAM policy that grants the necessary permissions.

This topic provides the steps to configure IAM authentication for RDS Proxy, including
creating the required IAM policy and attaching it to an IAM role.

###### Tip

This procedure is only necessary if you want to create your own IAM role. Otherwise,
RDS can automatically create the required role when you set up the proxy, so you can skip
these steps.

## Prerequisites

Before you set up IAM authentication for RDS Proxy, make sure that you have the
following:

- **AWS Secrets Manager** – At least one stored secret that
  contains database credentials. For instructions to create secrets, see [Setting up database credentials for RDS Proxy](rds-proxy-secrets-arns.md "rds-proxy-secrets-arns.md").

This is not required if you are using end-to-end IAM authentication.

- **IAM permissions** – An IAM role or user with
  permissions to create and manage IAM policies, roles, and secrets in
  AWS Secrets Manager.

## Creating an IAM policy for end-to-end IAM authentication

When using end-to-end IAM authentication, RDS Proxy connects to your database using IAM authentication
instead of retrieving credentials from Secrets Manager. This requires configuring your IAM role with
`rds-db:connect` permissions for the database accounts you want to use with the proxy.

To authenticate your RDS Proxy to the database using IAM, create an IAM role with a policy that grants the necessary database connection permissions.

###### To create a role for end-to-end IAM authentication with your proxy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Create a permissions policy for the role. For general steps, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md").

Paste this policy into the JSON editor and make the following changes:

    * Substitute your own account ID.
    * Substitute `us-east-2` with the where the proxy must reside.
    * Substitute the database resource IDs and user names with the ones you want to use.
     The resource ID format differs between RDS instances and Aurora clusters.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "rds-db:connect",
            "Resource": [
                "arn:aws:rds-db:us-east-2:`account_id`:dbuser:`db_instance_resource_id`/`db_user_name_1`",
                "arn:aws:rds-db:us-east-2:`account_id`:dbuser:`db_instance_resource_id`/`db_user_name_2`"
            ]
        }
    ]
}
```

3. Create the role and attach the permissions policy to it. For general steps, see
   [Create a role to
   delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

For the **Trusted entity type**, choose **AWS
service**. Under **Use case**, select
**RDS** and choose **RDS - Add Role to
Database** for the use case. 4. For **Permissions policies**, choose the policy that you
created. 5. For **Select trusted entities**, enter the following trust policy
for the role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "rds.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

To create the role using the AWS CLI, send the following request:

```
aws iam create-role \
  --role-name `my_e2e_iam_role_name` \

  --assume-role-policy-document '{"Version":"2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"Service":["rds.amazonaws.com"]},"Action":"sts:AssumeRole"}]}'
```

Then, attach the policy to the role:

```
aws iam put-role-policy \
  --role-name `my_e2e_iam_role_name` \
  --policy-name `e2e_iam_db_connect_policy` \
  --policy-document '{

    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "rds-db:connect",
            "Resource": [
                "arn:aws:rds-db:us-east-2:`account_id`:dbuser:`db_instance_resource_id`/`db_user_name_1`",
                "arn:aws:rds-db:us-east-2:`account_id`:dbuser:`db_instance_resource_id`/`db_user_name_2`"
            ]
        }
    ]
}'
```

With the IAM role and permissions configured for end-to-end IAM authentication, you can now create a proxy with `DefaultAuthScheme` set to `IAM_AUTH`.
This proxy directly authenticates to the database using IAM without requiring Secrets Manager secrets. For instructions, see [Creating a proxy for Amazon Aurora](rds-proxy-creating.md "rds-proxy-creating.md").

When using end-to-end IAM authentication, ensure that your database users are configured for IAM authentication as described in [Creating a database account using IAM authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md").

## Creating an IAM policy for Secrets Manager access

To allow RDS Proxy to retrieve database credentials from Secrets Manager, create an IAM role
with a policy that grants the necessary permissions.

###### To create a role to access your secrets for use with your proxy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Create a permissions policy for the role. For general steps, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md").

Paste this policy into the JSON editor and make the following changes:

    * Substitute your own account ID.
    * Substitute `us-east-2` with the Region where the proxy will
     reside.
    * Substitute the secret names with the ones you created. For more information, see
      [Specifying KMS keys in
     IAM policy statements](../../../kms/latest/developerguide/cmks-in-iam-policies.md "../../../kms/latest/developerguide/cmks-in-iam-policies.md").
    * Substitue the KMS key ID with the one you used to encrypt the Secrets Manager secrets,
     either the default key or your own key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": [
 "arn:aws:secretsmanager:us-east-2:`111122223333`:secret:`secret_name_1`",
 "arn:aws:secretsmanager:us-east-2:`111122223333`:secret:`secret_name_2`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:us-east-2:`111122223333`:key/`key_id`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "secretsmanager.us-east-2.amazonaws.com"
 }
 }
 }
 ]
}`

```

3. Create the role and attach the permissions policy to it. For general steps, see
   [Create a role to
   delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

For the **Trusted entity type**, choose **AWS
service**. Under **Use case**, select
**RDS** and choose **RDS - Add Role to
Database** for the use case. 4. For **Permissions policies**, choose the policy that you
created. 5. For **Select trusted entities**, enter the following trust policy
for the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "rds.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

To create the role using the AWS CLI, send the following request:

```
aws iam create-role \
  --role-name `my_role_name` \
  --assume-role-policy-document '{"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"Service":["rds.amazonaws.com"]},"Action":"sts:AssumeRole"}]}'
```

Then, attach the policy to the role:

```
aws iam put-role-policy \
  --role-name `my_role_name` \
  --policy-name `secret_reader_policy` \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "secretsmanager:GetSecretValue",
            "Resource": [
                "arn:aws:secretsmanager:us-east-2:`account_id`:secret:`secret_name_1`",
                "arn:aws:secretsmanager:us-east-2:`account_id`:secret:`secret_name_2`"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:us-east-2:`account_id`:key/`key_id`",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "secretsmanager.us-east-2.amazonaws.com"
                }
            }
        }
    ]
}'
```

With the IAM role and permissions configured, you can now create a proxy and
associate it with this role. This allows the proxy to retrieve database credentials
securely from AWS Secrets Manager and enable IAM authentication for your applications. For
instructions, see [Creating a proxy for Amazon Aurora](rds-proxy-creating.md "rds-proxy-creating.md").
