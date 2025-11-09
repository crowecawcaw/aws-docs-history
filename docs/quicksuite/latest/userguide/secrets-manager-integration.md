# Using AWS Secrets Manager secrets instead of

database credentials in Quick Suite

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| Intended audience:<br>Amazon Quick Suite Administrators and Amazon Quick Suite developers |

AWS Secrets Manager is a secret storage service that you can use to protect database
credentials, API keys, and other secret information. Using a key helps you ensure that
the secret can't be compromised by someone examining your code, because the secret isn't
stored in the code. For an overview, see the [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide.md "../../../secretsmanager/latest/userguide.md").

Quick Suite administrators can grant Amazon Quick Suite read-only access to secrets
they create in Secrets Manager. These secrets can be used in place of database credentials when
creating and editing data sources using the Quick Suite API.

Quick Suite supports using secrets with data source types that support
credential pair authentication. Jira and ServiceNow are not currently supported.

###### Note

If you use AWS Secrets Manager with Quick Suite, you are billed for access and
maintenance as described in the [AWS Secrets Manager Pricing
page](https://aws.amazon.com/secrets-manager/pricing "https://aws.amazon.com/secrets-manager/pricing"). In your billing statement, the costs are itemized under Secrets Manager and not
under Amazon Quick Suite.

Use the procedures described in the following sections to integrate Secrets Manager with
Amazon Quick Suite.

###### Topics

- [Granting Amazon Quick Suite
  access to Secrets Manager and selected secrets](#secrets-manager-integration-select-secrets "#secrets-manager-integration-select-secrets")
- [Creating or updating a data source
  with secret credentials using the Amazon Quick Suite API](#secrets-manager-integration-api "#secrets-manager-integration-api")
- [What's in the
  secret](#secrets-manager-integration-whats-in-secret "#secrets-manager-integration-whats-in-secret")
- [Modify a secret](#secrets-manager-integration-modifying "#secrets-manager-integration-modifying")

## Granting Amazon Quick Suite

access to Secrets Manager and selected secrets

If you're an administrator and you have secrets in Secrets Manager, you can grant
Amazon Quick Suite read-only access to selected secrets.

###### To grant Amazon Quick Suite access to Secrets Manager and selected secrets

1. In Amazon Quick Suite, choose your user icon on the upper right, and then choose
   **Manage Quick Suite**.
2. Choose **Security & permissions** on the left.
3. Choose **Manage** in **Amazon Quick Suite access to
   AWS resources**.
4. In **Allow access and autodiscovery for these
   resources**, choose **AWS Secrets Manager**,
   **Select secrets**.

The **AWS Secrets Manager secrets** page opens. 5. Select the secrets that you want to grant Amazon Quick Suite read-only access
to.

Secrets in your Amazon Quick Suite sign-up Region are shown automatically. To
select secrets outside your home Region, choose **Secrets in Other
AWS Regions**, and then enter the Amazon Resource Names
(ARNs) for those secrets. 6. When you're done, choose **Finish**.

Amazon Quick Suite creates an IAM role called
`aws-quicksight-secretsmanager-role-v0` in your account. It
grants users in the account read-only access to the specified secrets and
looks similar to the following:

When Amazon Quick Suite users create analyses from or view dashboards that use a
data source with secrets, Amazon Quick Suite assumes this Secrets Manager IAM role. For
more information about secret permissions policies, see [Authentication and access control for AWS Secrets Manager](../../../secretsmanager/latest/userguide/auth-and-access.md "../../../secretsmanager/latest/userguide/auth-and-access.md") in the
_AWS Secrets Manager User Guide_.

The specified secret in the Amazon Quick Suite IAM role may have an additional
resource policy that denies access. For more information, see [Attach a permissions policy to a secret](../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md "../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md") in the
_AWS Secrets Manager User Guide_.

If you're using an AWS managed AWS KMS key to encrypt your secret,
Amazon Quick Suite doesn't require any additional permissions setup in
Secrets Manager.

If you're using a customer managed key to encrypt your secret, ensure that the
Amazon Quick Suite IAM role, `aws-quicksight-secretsmanager-role-v0`
has `kms:Decrypt` permissions. For more information, see [Permissions for the KMS key](../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz "../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz") in the
_AWS Secrets Manager User Guide_.

For more information about the types of keys used in AWS Key Management
Service, see [Customer keys and
AWS keys](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") in the _AWS Key Management Service
guide_.

## Creating or updating a data source

with secret credentials using the Amazon Quick Suite API

After the Amazon Quick Suite administrator has granted Amazon Quick Suite read-only access to
Secrets Manager, you can create and update data sources in the API using a secret the
administrator selected as credentials.

Following is an example API call to create a data source in Amazon Quick Suite. This
example uses the `create-data-source` API operation. You can also use the
`update-data-source` operation. For more information, see [CreateDataSource](../../../quicksight/latest/APIReference/API_CreateDataSource.md "../../../quicksight/latest/APIReference/API_CreateDataSource.md") and [UpdateDataSource](../../../quicksight/latest/APIReference/API_UpdateDataSource.md "../../../quicksight/latest/APIReference/API_UpdateDataSource.md") in the _Amazon Quick Suite API Reference_.

The user specified in the permissions in the following API call example can
delete, view, and edit data sources for the specified MySQL data source in
Amazon Quick Suite. They can also view and update the data source permissions. Instead of
a Amazon Quick Suite username and password, a secret ARN is used as credentials for the
data source.

```
aws quicksight create-data-source
    --aws-account-id `AWSACCOUNTID` \
    --data-source-id `DATASOURCEID` \
    --name `NAME` \
    --type `MYSQL` \
    --permissions '[{"Principal": "arn:aws:quicksight:`region`:`accountID`:user/namespace/`username`", "Actions": ["quicksight:DeleteDataSource", "quicksight:DescribeDataSource", "quicksight:DescribeDataSourcePermissions", "quicksight:PassDataSource", "quicksight:UpdateDataSource", "quicksight:UpdateDataSourcePermissions"]}]' \
    --data-source-parameters='{"MySQLParameters":{"Database": "`database`", "Host":"`hostURL`", "Port":"`port`"}}' \
    --credentials='{"SecretArn":"arn:aws:secretsmanager:`region`:`accountID`:secret:`secretname`"}' \
    --region `us-west-2`
```

In this call, Amazon Quick Suite authorizes `secretsmanager:GetSecretValue`
access to the secret based on the API caller's IAM policy, not the IAM service
role's policy. The IAM service role acts on the account level and is used when an
analysis or dashboard is viewed by a user. It cannot be used to authorize secret
access when a user creates or updates the data source.

When they edit a data source in the Amazon Quick Suite UI, users can view the secret ARN
for data sources that use AWS Secrets Manager as the credential type. However, they can't edit
the secret, or select a different secret. If they need to make changes, for example
to the database server or port, users first need to choose **Credential
pair** and enter their Amazon Quick Suite account username and
password.

Secrets are automatically removed from a data source when the data source is
altered in the UI. To restore the secret to the data source, use the
`update-data-source` API operation.

## What's in the

secret

Amazon Quick Suite requires the following JSON format to access your secret:

```
{
  "username": "`username`",
  "password": "`password`"
}
```

The `username` and `password` fields are required for
Amazon Quick Suite to access secrets. All other fields are optional and are ignored by
Amazon Quick Suite.

The JSON format may vary depending on the type of database. For more information,
see [JSON
structure of AWS Secrets Manager database credential secrets](../../../secretsmanager/latest/userguide/reference_secret_json_structure.md "../../../secretsmanager/latest/userguide/reference_secret_json_structure.md") in the
_AWS Secrets Manager User Guide_.

## Modify a secret

To modify a secret, you use Secrets Manager. After you make changes to a secret, the updates
become available the next time Amazon Quick Suite requests access to the secret.
