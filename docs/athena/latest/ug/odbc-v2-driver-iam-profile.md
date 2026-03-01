# IAM profile

You can configure a named profile to connect to Amazon Athena using the ODBC driver. To
use the credentials available in your hosting Amazon EC2 instance profile, set the
`credential_source` parameter to `Ec2InstanceMetadata`. If you
want to use a custom credentials provider in a named profile, specify a value for the
`plugin_name` parameter in your profile configuration.

## Authentication type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**     |
| -------------------------- | ------------------ | ----------------- | --------------------------------- |
| AuthenticationType         | Required           | `IAM Credentials` | `AuthenticationType=IAM Profile;` |

## AWS profile

The profile name to use for your ODBC connection. For more information about
profiles, see [Using named profiles](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles") in the _AWS Command Line Interface User Guide_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| AWSProfile                 | Required           | `none`            | `AWSProfile=default;`         |

## Preferred role

The Amazon Resource Name (ARN) of the role to assume. The preferred role parameter
is used when the custom credentials provider is specified by the
`plugin_name` parameter in your profile configuration. For more
information about ARN roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the
_AWS Security Token Service API Reference_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                        |
| -------------------------- | ------------------ | ----------------- | ---------------------------------------------------- |
| preferred_role             | Optional           | `none`            | `preferred_role=arn:aws:IAM::123456789012:id/user1;` |

## Session duration

The duration, in seconds, of the role session. For more information about session
duration, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the
_AWS Security Token Service API Reference_. The session duration
parameter is used when the custom credentials provider is specified by the
`plugin_name` parameter in your profile configuration.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| duration                   | Optional           | `900`             | `duration=900;`               |

## Plugin name

Specifies the name of a custom credentials provider used in a named profile. This
parameter can take the same values as those in the **Authentication
Type** field of the ODBC Data Source Administrator, but is used only by
`AWSProfile` configuration.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| plugin_name                | Optional           | `none`            | `plugin_name=AzureAD;`        |
