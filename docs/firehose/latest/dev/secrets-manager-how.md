# Use the secret

We recommend that you use AWS Secrets Manager to store your credentials or keys to connect to
streaming destinations such as Amazon Redshift, HTTP endpoint, Snowflake, Splunk, Coralogix, Datadog,
Dynatrace, Elastic, Honeycomb, LogicMonitor, Logz.io, MongoDB Cloud, and New Relic.

You can configure authentication with Secrets Manager for these destinations through the AWS
Management Console at the time of Firehose stream creation. For more information, see [Configure destination settings](create-destination.md "create-destination.md"). Alternatively,
you can also use the [CreateDeliveryStream](../APIReference/API_CreateDeliveryStream.md "../APIReference/API_CreateDeliveryStream.md") and [UpdateDestination](../APIReference/API_UpdateDestination.md "../APIReference/API_UpdateDestination.md") API operations to configure authentication with
Secrets Manager.

Firehose caches the secrets with an encryption and uses them for every connection to
destinations. It refreshes the cache every 10 minutes to ensure that the latest
credentials are used.

You can choose to turn off the capability of retrieving secrets from Secrets Manager at any time
during the lifecycle of the stream. If you don’t want to use Secrets Manager to retrieve secrets,
you can use the username/password or API key instead.

###### Note

Although, there is no additional cost for this feature in Firehose, you are billed for access and
maintenance of Secrets Manager. For more information, see [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/pricing/ "https://aws.amazon.com/secrets-manager/pricing/") pricing page.

## Grant access to Firehose to retrieve the

secret

For Firehose to retrieve a secret from AWS Secrets Manager, you must provide Firehose the required
permissions to access the secret and the key that encrypts your secret.

When using AWS Secrets Manager to store and retrieve secrets, there are a few different
configuration options depending on where the secret is stored and how it is encrypted.

- If the secret is stored in the same AWS account as your IAM role and it's
  encrypted with the default AWS managed key (`aws/secretsmanager`),
  the IAM role that Firehose assumes only needs
  `secretsmanager:GetSecretValue` permission on the secret.

```
// secret role policy
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "`Secret ARN`"
        }
    ]
}
```

For more information on IAM policies, see [Permissions policy examples for AWS Secrets Manager](../../../secretsmanager/latest/userguide/auth-and-access_examples.md "../../../secretsmanager/latest/userguide/auth-and-access_examples.md").

- If the secret is stored in the same account as the role but encrypted with a [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") (CMK), the role needs both
  `secretsmanager:GetSecretValue` and `kms:Decrypt`
  permissions. The CMK policy also needs to allow the IAM role to perform
  `kms:Decrypt`.
- If the secret is stored in a different AWS account than your role, and it is encrypted with
  the default AWS managed key, this configuration is not possible as Secrets Manager does
  not allow cross-account access when secret is encrypted with AWS managed
  key.
- If the secret is stored in a different account and encrypted with a CMK, IAM
  role needs `secretsmanager:GetSecretValue` permission on the secret
  and `kms:Decrypt` permission on the CMK. The secret's resource policy
  and the CMK policy in the other account also need to allow the IAM role the
  necessary permissions. For more information, see [Cross-account access](../../../secretsmanager/latest/userguide/auth-and-access_examples_cross.md "../../../secretsmanager/latest/userguide/auth-and-access_examples_cross.md").
