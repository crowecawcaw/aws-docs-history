Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a secret and an IAM role to use

federated queries

The following steps show how to create a secret and an IAM role to use with federated
queries.

## Prerequisites

Make sure that you have the following prerequisites to create a secret and an IAM
role to use with federated queries:

- An RDS PostgreSQL, Aurora PostgreSQL DB instance, RDS MySQL, or Aurora MySQL DB instance with user name and password
  authentication.
- An Amazon Redshift cluster with a cluster maintenance version that supports federated queries.

###### To create a secret (user name and password) with AWS Secrets Manager

1. Sign in to the Secrets Manager console with the account that owns your RDS or Aurora DB cluster instance.
2. Choose **Store a new secret**.
3. Choose the **Credentials for RDS database** tile. For **User
   name** and **Password**, enter values for your instance.
   Confirm or choose a value for **Encryption key**. Then choose the
   RDS database that your secret will access.

###### Note

We recommend using the default encryption key (`DefaultEncryptionKey`).
If you use a custom encryption key, the IAM role that is used to access the secret must be added as a key user. 4. Enter a name for the secret, continue with the creation steps with the default choices, and
then choose **Store**. 5. View your secret and note the **Secret ARN** value that you created to
identify the secret.

###### To create a security policy using the secret

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Create a policy with JSON similar to the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessSecret",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecretVersionIds"
 ],
 "Resource": "arn:aws:secretsmanager:`us-west-2`:`123456789012`:secret:my-rds-secret-VNenFy"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetRandomPassword",
 "secretsmanager:ListSecrets"
 ],
 "Resource": "*"
 }
 ]
}`

```

To retrieve the secret, you need list and read actions. We recommend that you
restrict the resource to the specific secret that you created. To do this, use the
Amazon Resource Name (ARN) of the secret to limit the resource. You can also specify
the permissions and resources using the visual editor on the IAM console. 3. Give the policy a name and finish creating it. 4. Navigate to **IAM roles**. 5. Create an IAM role for **Redshift - Customizable**. 6. Either attach the IAM policy you just created to an existing IAM role, or create a new IAM
role and attach the policy. 7. On the **Trust relationships** tab of your IAM role, confirm that the role
contains the trust entity `redshift.amazonaws.com`. 8. Note the **Role ARN** you created. This ARN has access to the secret.

###### To attach the IAM role to your Amazon Redshift cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**. The clusters for your account in
   the current AWS Region are listed.
3. Choose the cluster name in the list to view more details about a cluster.
4. For **Actions**, choose **Manage IAM roles**. The
   **Manage IAM roles** page appears.
5. Add your IAM role to the cluster.
