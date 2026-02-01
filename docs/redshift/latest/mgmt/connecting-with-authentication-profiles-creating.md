Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating an

authentication profile

Using the AWS CLI, you create an authentication profile with the
`create-authentication-profile` command. This assumes that you have
an existing Amazon Redshift cluster and an existing database. Your credentials must have
permission to connect to the Amazon Redshift database and rights to fetch the authentication
profile. You provide the configuration options as a JSON string, or reference a file
containing your JSON string.

```
create-authentication-profile --authentication-profile-name<value: String> --authentication-profile-content<value: String>
```

The following example creates a profile called `ExampleProfileName`.
Here, you can add keys and values that define your cluster name and other option
settings, as a JSON string.

```
create-authentication-profile --authentication-profile-name "ExampleProfileName" --authentication-profile-content "{\"AllowDBUserOverride\":\"1\",\"Client_ID\":\"ExampleClientID\",\"App_ID\":\"ExampleAppID\",\"AutoCreate\":false,\"enableFetchRingBuffer\":true,\"databaseMetadataCurrentDbOnly\":true}"
}
```

This command creates the profile with the specified JSON settings. The following
is returned, which indicates that the profile is created.

`{"`AuthenticationProfileName`":
 "`ExampleProfileName`",
 `"AuthenticationProfileContent"`:
 "{\"`AllowDBUserOverride`\":\"1\",\"`Client_ID`\":\`"ExampleClientID`\",\"`App_ID`\":\"`ExampleAppID`\",\"`AutoCreate`\":false,\"`enableFetchRingBuffer`\":true,\"`databaseMetadataCurrentDbOnly`\":true}"
 }`

## Limitations and quotas for creating an authentication profile

Each customer has a quota of ten (10) authentication profiles.

Certain errors can occur with authentication profiles. Examples are if you
create a new profile with an existing name, or if you exceed your profile quota.
For more information, see [CreateAuthenticationProfile](../APIReference/redshift-api.md#API_CreateAuthenticationProfile "../APIReference/redshift-api.md#API_CreateAuthenticationProfile").

You can't store certain option keys and values for JDBC, ODBC, and Python
connection strings in the authentication profile store:

- `AccessKeyID`
- `access_key_id`
- `SecretAccessKey`
- `secret_access_key_id`
- `PWD`
- `Password`
- `password`

You can't store the key or value `AuthProfile` in the profile
store, for JDBC or ODBC connection strings. For Python connections, you can’t
store `auth_profile`.

Authentication profiles are stored in Amazon DynamoDB and managed by AWS.
