

# Using AWS Secrets Manager secrets instead of database credentials in Quick


|  | 
| --- |
|    Intended audience:  AWS Quick Administrators and AWS Quick developers  | 

AWS Secrets Manager is a secret storage service that you can use to protect database credentials, API keys, and other secret information. Using a key helps you ensure that the secret can't be compromised by someone examining your code, because the secret isn't stored in the code. For an overview, see the [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide).

Quick administrators can grant AWS Quick read-only access to secrets they create in Secrets Manager. These secrets can be used in place of database credentials when creating and editing data sources using the Quick API.

Quick supports using secrets with data source types that support credential pair authentication. Jira and ServiceNow are not currently supported.

**Note**  
If you use AWS Secrets Manager with Quick, you are billed for access and maintenance as described in the [AWS Secrets Manager Pricing page](https://aws.amazon.com/secrets-manager/pricing). In your billing statement, the costs are itemized under Secrets Manager and not under AWS Quick.

Use the procedures described in the following sections to integrate Secrets Manager with AWS Quick.

**Topics**
+ [Granting AWS Quick access to Secrets Manager and selected secrets](#secrets-manager-integration-select-secrets)
+ [Creating or updating a data source with secret credentials using the AWS Quick API](#secrets-manager-integration-api)
+ [What's in the secret](#secrets-manager-integration-whats-in-secret)
+ [Modify a secret](#secrets-manager-integration-modifying)

## Granting AWS Quick access to Secrets Manager and selected secrets
<a name="secrets-manager-integration-select-secrets"></a>

If you're an administrator and you have secrets in Secrets Manager, you can grant AWS Quick read-only access to selected secrets. 

**To grant AWS Quick access to Secrets Manager and selected secrets**

1. In AWS Quick, choose your user icon on the upper right, and then choose **Manage Quick**.

1. Choose **Security & permissions** on the left.

1. Choose **Manage** in **AWS Quick access to AWS resources**.

1. In **Allow access and autodiscovery for these resources**, choose **AWS Secrets Manager**, **Select secrets**. 

   The **AWS Secrets Manager secrets** page opens. 

1. Select the secrets that you want to grant AWS Quick read-only access to.

   Secrets in your AWS Quick sign-up Region are shown automatically. To select secrets outside your home Region, choose **Secrets in Other AWS Regions**, and then enter the Amazon Resource Names (ARNs) for those secrets.

1. When you're done, choose **Finish**. 

   AWS Quick creates an IAM role called `aws-quicksight-secretsmanager-role-v0` in your account. It grants users in the account read-only access to the specified secrets and looks similar to the following:

   When AWS Quick users create analyses from or view dashboards that use a data source with secrets, AWS Quick assumes this Secrets Manager IAM role. For more information about secret permissions policies, see [Authentication and access control for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html) in the *AWS Secrets Manager User Guide*.

   The specified secret in the AWS Quick IAM role may have an additional resource policy that denies access. For more information, see [Attach a permissions policy to a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   If you're using an AWS managed AWS KMS key to encrypt your secret, AWS Quick doesn't require any additional permissions setup in Secrets Manager.

   If you're using a customer managed key to encrypt your secret, ensure that the AWS Quick IAM role, `aws-quicksight-secretsmanager-role-v0` has `kms:Decrypt` permissions. For more information, see [Permissions for the KMS key](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html#security-encryption-authz) in the *AWS Secrets Manager User Guide*.

   For more information about the types of keys used in AWS Key Management Service, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) in the *AWS Key Management Service guide*.

## Creating or updating a data source with secret credentials using the AWS Quick API
<a name="secrets-manager-integration-api"></a>

After the AWS Quick administrator has granted AWS Quick read-only access to Secrets Manager, you can create and update data sources in the API using a secret the administrator selected as credentials.

Following is an example API call to create a data source in AWS Quick. This example uses the `create-data-source` API operation. You can also use the `update-data-source` operation. For more information, see [CreateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSource.html) and [UpdateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSource.html) in the *AWS Quick API Reference*.

The user specified in the permissions in the following API call example can delete, view, and edit data sources for the specified MySQL data source in AWS Quick. They can also view and update the data source permissions. Instead of a AWS Quick username and password, a secret ARN is used as credentials for the data source.

```
aws quicksight create-data-source 
    --aws-account-id {{AWSACCOUNTID}} \ 
    --data-source-id {{DATASOURCEID}} \
    --name {{NAME}} \
    --type {{MYSQL}} \
    --permissions '[{"Principal": "arn:aws:quicksight:{{region}}:{{accountID}}:user/namespace/{{username}}", "Actions": ["quicksight:DeleteDataSource", "quicksight:DescribeDataSource", "quicksight:DescribeDataSourcePermissions", "quicksight:PassDataSource", "quicksight:UpdateDataSource", "quicksight:UpdateDataSourcePermissions"]}]' \
    --data-source-parameters='{"MySQLParameters":{"Database": "{{database}}", "Host":"{{hostURL}}", "Port":"{{port}}"}}' \
    --credentials='{"SecretArn":"arn:aws:secretsmanager:{{region}}:{{accountID}}:secret:{{secretname}}"}' \
    --region {{us-west-2}}
```

In this call, AWS Quick authorizes `secretsmanager:GetSecretValue` access to the secret based on the API caller's IAM policy, not the IAM service role's policy. The IAM service role acts on the account level and is used when an analysis or dashboard is viewed by a user. It cannot be used to authorize secret access when a user creates or updates the data source. 

When they edit a data source in the AWS Quick UI, users can view the secret ARN for data sources that use AWS Secrets Manager as the credential type. However, they can't edit the secret, or select a different secret. If they need to make changes, for example to the database server or port, users first need to choose **Credential pair** and enter their AWS Quick account username and password.

Secrets are automatically removed from a data source when the data source is altered in the UI. To restore the secret to the data source, use the `update-data-source` API operation.

## What's in the secret
<a name="secrets-manager-integration-whats-in-secret"></a>

AWS Quick requires the following JSON format to access your secret:

```JSON
{
  "username": "{{username}}",
  "password": "{{password}}"
}
```

The `username` and `password` fields are required for AWS Quick to access secrets. All other fields are optional and are ignored by AWS Quick.

The JSON format may vary depending on the type of database. For more information, see [JSON structure of AWS Secrets Manager database credential secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_secret_json_structure.html) in the *AWS Secrets Manager User Guide*.

## Modify a secret
<a name="secrets-manager-integration-modifying"></a>

To modify a secret, you use Secrets Manager. After you make changes to a secret, the updates become available the next time AWS Quick requests access to the secret.