# IAM credentials

You can use your IAM credentials with the JDBC driver to connect to Amazon Athena by
setting the following connection parameters.

## User

Your AWS access key ID. For information about access keys, see [AWS
security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md") in the
_IAM User Guide_.

| Parameter name | Alias       | Parameter type | Default value |
| -------------- | ----------- | -------------- | ------------- |
| User           | AccessKeyId | Required       | none          |

## Password

Your AWS secret key ID. For information about access keys, see [AWS
security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md") in the
_IAM User Guide_.

| Parameter name | Alias           | Parameter type | Default value |
| -------------- | --------------- | -------------- | ------------- |
| Password       | SecretAccessKey | Optional       | none          |

## Session token

If you use temporary AWS credentials, you must specify a session token. For
information about temporary credentials, see [Temporary security
credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") in the
_IAM User Guide_.

| Parameter name | Alias | Parameter type | Default value |
| -------------- | ----- | -------------- | ------------- |
| SessionToken   | none  | Optional       | none          |
