# CloudWatch pipelines extensions

CloudWatch pipelines extensions provide additional functionality to the pipeline. You can use the AWS Secrets Manager
integration for credential management.

## AWS Secrets Manager extension

Configures access to AWS Secrets Manager for retrieving credentials and
sensitive configuration values. This extension is only supported for
third-party sources that require authentication credentials.

###### Configuration

Configure the AWS Secrets Manager extension with the following
parameters:

```
extension:
  aws:
    secrets:
      <secret-name>:
        secret_id: "<secret arn>"
        region: "<secret region>"
        sts_role_arn: "arn:aws:iam::123456789012:role/Example-Role"
        refresh_interval: PT1H
        disable_refresh: false
```

###### Parameters

`aws.secrets.<secret-name>.secret_id`
(required)

The ARN of the AWS Secrets Manager secret containing the
credentials.

`aws.secrets.<secret-name>.region`
(required)

The AWS region where the secret is stored.

`aws.secrets.<secret-name>.sts_role_arn`
(required)

The ARN of the IAM role to assume for accessing the AWS
Secrets Manager secret.

`aws.secrets.<secret-name>.refresh_interval`
(optional)

How often to refresh the secret from AWS Secrets Manager.
Uses ISO 8601 duration format. Defaults to PT1H (1 hour).

`aws.secrets.<secret-name>.disable_refresh`
(optional)

Whether to disable automatic secret refresh. Defaults to
false.

### Secret reference syntax

Reference secrets in your pipeline configuration using the following
syntax:

```
${{aws_secrets:<secret-name>:<key>}}
```

For example, to reference a client ID and secret:

```
source:
  microsoft_office365:
    authentication:
      oauth2:
        client_id: "${{aws_secrets:office365-creds:client_id}}"
        client_secret: "${{aws_secrets:office365-creds:client_secret}}"
```

### Requirements and limitations

Secret format

Secrets must be stored as JSON key-value pairs in AWS
Secrets Manager.

Cross-Region access

Secrets can be accessed from any Region where AWS
Secrets Manager is available.

Refresh interval limits

Minimum refresh interval is 5 minutes (PT5M). Maximum is
24 hours (PT24H).

Maximum secrets

A pipeline can reference up to 10 different
secrets.

###### Important

Consider the following when using secrets:

- Ensure the IAM role has appropriate permissions to access
  the secrets
- Monitor secret access using AWS CloudTrail
- Use separate secrets for different environments
  (development, production)
