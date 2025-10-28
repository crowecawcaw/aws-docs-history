# Prerequisites for connecting the Data Catalog to external data sources

To connect the AWS Glue Data Catalog to external data sources, register the connection with Lake Formation, and set up federated catalogs, you
need to complete the following requirements:

###### Note

We recommend that a Lake Formation data lake administrator creates the AWS Glue connections to connect to
external data sources, and create the federated catalogs.

1.  ###### Create IAM roles.
    - Create a role that has the necessary permissions to deploy resources (Lambda function, Amazon S3 spill bucket, IAM role, and the AWS Glue connection) required to create a connection to the external data source.
    - Create a role that has the necessary minimum permissions to access the AWS Glue connection
      properties (the Lambda function and the Amazon S3 spill bucket). This is the role that
      you'll include when you register the connection with Lake Formation.

    To use Lake Formation to manage and secure the data in your data lake, you must
    register the AWS Glue connection with Lake Formation. By doing so, Lake Formation can vend credentials to
    Amazon Athena for querying the federated data sources.

    The role must have `Select` or `Describe` permissions on the Amazon S3 bucket and the Lambda function.

        + s3:ListBucket
        + s3:GetObject
        + lambda:InvokeFunction

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "s3:*"
     ],
     "Resource": [
     "arn:aws:s3:::amzn-s3-demo-bucket1/object/*",
     "arn:aws:s3:::amzn-s3-demo-bucket1/object"
     ]
     },
     {
     "Sid": "lambdainvoke",
     "Effect": "Allow",
     "Action": "lambda:InvokeFunction",
     "Resource": "arn:aws:lambda:us-east-1:123456789012:function:`example-lambda-function`"
     },
     {
     "Sid": "gluepolicy",
     "Effect": "Allow",
     "Action": "glue:*",
     "Resource": "*"
     }
     ]
    }`

    ```

    - Add the following trust policy to the IAM role that is used in registering the connection:

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Principal": {
     "Service": [
     "lakeformation.amazonaws.com"
     ]
     },
     "Action": "sts:AssumeRole"
     }
     ]
    }`

    ```

    - The data lake administrator who registers the connection must have the
      `iam:PassRole` permission on the role.

    The following is an inline policy that grants this permission. Replace
    `<account-id>` with a valid AWS account number,
    and replace `<role-name>` with the name of the
    role.

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "PassRolePermissions",
     "Effect": "Allow",
     "Action": [
     "iam:PassRole"
     ],
     "Resource": [
     "arn:aws:iam::`111122223333`:role/`example-role-name>`"
     ]
     }
     ]
    }`

    ```

    - To create federated catalogs in Data Catalog, make sure the IAM role you’re using is a Lake Formation data lake administrator by checking the data lake settings (`aws lakeformation get-data-lake-settings`).

    If you're not a data lake administrator, you need the Lake Formation `CREATE_CATALOG` permission to create a catalog.
    The following example shows how to grant the required permissions to create catalogs.

    ```
    aws lakeformation grant-permissions \
    --cli-input-json \
            '{
                "Principal": {
                 "DataLakePrincipalIdentifier":`"arn:aws:iam::123456789012:role/non-admin"`
                },
                "Resource": {
                    "Catalog": {
                    }
                },
                "Permissions": [
                    "CREATE_CATALOG",
                    "DESCRIBE"
                ]
            }'

    ```

2.  Add the following key policy to the AWS KMS key if you're using a customer managed key to
    encrypt the data in the data source. Replace the account number with a valid AWS account
    number, and specify role name. By default, the data is encrypted using an KMS key. Lake Formation
    provides an option to create your custom KMS key for encryption. If you're using a
    customer managed key, you must add specific key policies to the key.

For more information about managing the permissions of a customer managed key,
see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "`arn:aws:kms:us-east-1:123456789012:key/key-1`"
 }
 ]
}`

```
