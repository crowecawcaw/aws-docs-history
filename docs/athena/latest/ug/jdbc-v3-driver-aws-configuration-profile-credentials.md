# AWS configuration profile credentials

You can use credentials stored in an AWS configuration profile by setting the
following connection parameters. AWS configuration profiles are typically stored in
files in the `~/.aws` directory). For information about AWS
configuration profiles, see [Use
profiles](../../../sdk-for-java/latest/developer-guide/credentials-profiles.md "../../../sdk-for-java/latest/developer-guide/credentials-profiles.md") in the _AWS SDK for Java Developer Guide_.

## Credentials provider

The credentials provider that will be used to authenticate requests to AWS. Set
the value of this parameter to `ProfileCredentials`.

| Parameter name      | Alias                                         | Parameter type | Default value | Value to use         |
| ------------------- | --------------------------------------------- | -------------- | ------------- | -------------------- |
| CredentialsProvider | _AWSCredentialsProviderClass<br>(deprecated)_ | Required       | none          | `ProfileCredentials` |

## Profile name

The name of the AWS configuration profile whose credentials should be used to
authenticate the request to Athena.

| Parameter name | Alias | Parameter type | Default value |
| -------------- | ----- | -------------- | ------------- |
| ProfileName    | none  | Required       | none          |

###### Note

The profile name can also be specified as the value of the
`CredentialsProviderArguments` parameter, although this use is
deprecated.

## Authenticating with an IAM Identity Center profile

Use an IAM Identity Center profile with the
`ProfileCredentials` provider to authenticate requests to AWS. This
approach uses SSO-managed credentials instead of long-term access keys. The
following example shows the required entries in the
`~/.aws/config` file.

```
[profile athena-idc]
sso_session = athena-idc-session
sso_account_id = 111122223333
sso_role_name = AthenaQueryRole
region = us-east-1

[sso-session athena-idc-session]
sso_start_url = https://example.awsapps.com/start
sso_region = us-east-1
sso_registration_scopes = sso:account:access
```

Before opening the JDBC connection, sign in to the profile. For example, use
`aws sso login --profile athena-idc`. Then configure the JDBC
connection with the following parameters.

```
CredentialsProvider=ProfileCredentials;
ProfileName=athena-idc;
```
