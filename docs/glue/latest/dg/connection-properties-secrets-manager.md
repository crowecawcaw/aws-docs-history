

# Storing connection credentials in AWS Secrets Manager
<a name="connection-properties-secrets-manager"></a>

We recommend that you use AWS Secrets Manager to supply connection credentials for your data store. Using Secrets Manager this way lets AWS Glue access your secret at runtime for ETL jobs and crawler runs, and helps keep your credentials secure.

**Prerequisites**

To use Secrets Manager with AWS Glue, you must grant your [IAM role for AWS Glue](create-an-iam-role.md) permission to retrieve secret values. The AWS managed policy `AWSGlueServiceRole` doesn't include AWS Secrets Manager permissions. For example IAM policies, see [Example: Permission to retrieve secret values](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_examples_read) in the *AWS Secrets Manager* *User Guide.*

Depending on your network setup, you might also need to create a VPC endpoint to establish a private connection between your VPC and Secrets Manager. For more information, see [Using an AWS Secrets Manager VPC endpoint](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html).

**To create a secret for AWS Glue**

1. Follow the instructions in [Create and manage secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets.html) in the *AWS Secrets Manager User Guide*. The following example JSON shows how to specify your credentials in the **Plaintext** tab when you create a secret for AWS Glue. 

   ```
   {
     "username": "EXAMPLE-USERNAME",
     "password": "EXAMPLE-PASSWORD"
   }
   ```

1. Associate your secret with a connection using the AWS Glue Studio interface. For detailed instructions, see [Creating connections for connectors](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html#creating-connections) in the *AWS Glue Studio User Guide.*