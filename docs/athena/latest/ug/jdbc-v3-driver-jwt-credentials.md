# JWT credentials

With this authentication type, you can use a JSON web token (JWT) obtained from an
external identity provider as a connection parameter to authenticate with Athena. The
external credentials provider must already be federated with AWS.

## Credentials provider

The credentials provider that will be used to authenticate requests to AWS. Set
the value of this parameter to `JWT`.

| Parameter name      | Alias                                    | Parameter type | Default value | Value to use |
| ------------------- | ---------------------------------------- | -------------- | ------------- | ------------ |
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required       | none          | `JWT`        |

## JWT web identity token

The JWT token obtained from an external federated identity provider. This token
will be used to authenticate with Athena.

| Parameter name      | Alias                           | Parameter type | Default value |
| ------------------- | ------------------------------- | -------------- | ------------- |
| JwtWebIdentityToken | web_identity_token (deprecated) | Required       | none          |

## JWT role ARN

The Amazon Resource Name (ARN) of the role to assume. For information about
assuming roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the
_AWS Security Token Service API Reference_.

| Parameter name | Alias                 | Parameter type | Default value |
| -------------- | --------------------- | -------------- | ------------- |
| JwtRoleArn     | role_arn (deprecated) | Required       | none          |

## JWT role session name

The name of the session when you use JWT credentials for authentication. The name
can be any name that you choose.

| Parameter name     | Alias                          | Parameter type | Default value |
| ------------------ | ------------------------------ | -------------- | ------------- |
| JwtRoleSessionName | role_session_name (deprecated) | Required       | none          |

## Role session duration

The duration, in seconds, of the role session. For more information, see [AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md") in the
_AWS Security Token Service API Reference_.

| Parameter name      | Alias                 | Parameter type | Default value |
| ------------------- | --------------------- | -------------- | ------------- |
| RoleSessionDuration | Duration (deprecated) | Optional       | 3600          |
