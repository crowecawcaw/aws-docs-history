Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Storing database credentials in AWS Secrets Manager

When you call the Data API, you can pass credentials for the cluster or
serverless workgroup by using a secret in AWS Secrets Manager. To pass credentials in this
way, you specify the name of the secret or the Amazon Resource Name (ARN) of the
secret.

To store credentials with Secrets Manager, you need `SecretManagerReadWrite`
managed policy permission. For more information about the minimum permissions, see
[Creating and Managing Secrets
with AWS Secrets Manager](../../../secretsmanager/latest/userguide/managing-secrets.md "../../../secretsmanager/latest/userguide/managing-secrets.md") in the _AWS Secrets Manager User Guide_.

###### To store your credentials in a secret for an Amazon Redshift cluster

1.  Use the AWS Secrets Manager console to create a secret that contains credentials for
    your cluster:

        * When you choose **Store a new secret**, choose
         **Credentials for Redshift cluster**.
        * Store your values for **User name** (database
         user), **Password**, and **DB cluster** (cluster identifier) in your secret.
        * Tag the secret with the key `RedshiftDataFullAccess`.
         The AWS managed policy `AmazonRedshiftDataFullAccess`
         only allows the action `secretsmanager:GetSecretValue`
         for secrets tagged with the key `RedshiftDataFullAccess`.

    For instructions, see [Creating a Basic
    Secret](../../../secretsmanager/latest/userguide/manage_create-basic-secret.md "../../../secretsmanager/latest/userguide/manage_create-basic-secret.md") in the _AWS Secrets Manager User Guide_.

2.  Use the AWS Secrets Manager console to view the details for the secret you created,
    or run the `aws secretsmanager describe-secret` AWS CLI
    command.

Note the name and ARN of the secret. You can use these in calls to the
Data API.

###### To store your credentials in a secret for a serverless workgroup

1.  Use AWS Secrets Manager AWS CLI commands to store a secret that contains credentials
    for your serverless workgroup:

        * Create your secret in a file, for example a JSON file named
         `mycreds.json`. Provide the values for
         **User name** (database user) and
         **Password** in the file.



        ```
        {
              "username": "myusername",
              "password": "mypassword"
        }
        ```
        * Store your values in your secret and tag the secret with the key
         `RedshiftDataFullAccess`.



        ```
        aws secretsmanager create-secret --name MyRedshiftSecret  --tags Key="RedshiftDataFullAccess",Value="serverless" --secret-string file://mycreds.json
        ```

        The following shows the output.



        ```
        {
            "ARN": "arn:aws:secretsmanager:`region`:`accountId`:secret:MyRedshiftSecret-`mvLHxf`",
            "Name": "MyRedshiftSecret",
            "VersionId": "a1603925-e8ea-4739-9ae9-e509eEXAMPLE"
        }
        ```

    For more information, see [Creating a Basic Secret with AWS CLI](../../../secretsmanager/latest/userguide/manage_create-basic-secret.md#proc-create-api "../../../secretsmanager/latest/userguide/manage_create-basic-secret.md#proc-create-api") in the
    _AWS Secrets Manager User Guide_.

2.  Use the AWS Secrets Manager console to view the details for the secret you created,
    or run the `aws secretsmanager describe-secret` AWS CLI
    command.

Note the name and ARN of the secret. You can use these in calls to the
Data API.
