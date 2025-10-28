Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting

authentication profiles

To list existing authentication profiles, call the following command.

```
describe-authentication-profiles --authentication-profile-name <value: String>
```

The following example shows two retrieved profiles. All profiles are returned if
you don't specify a profile name.

`{ "AuthenticationProfiles": [ { "AuthenticationProfileName":
 "testProfile1", "AuthenticationProfileContent":
 "{\"AllowDBUserOverride\":\"1\",\"Client_ID\":\"ExampleClientID\",\"App_ID\":\"ExampleAppID\",\"AutoCreate\":false,\"enableFetchRingBuffer\":true,\"databaseMetadataCurrentDbOnly\":true}"
 }, { "AuthenticationProfileName": "testProfile2",
 "AuthenticationProfileContent":
 "{\"AllowDBUserOverride\":\"1\",\"Client_ID\":\"ExampleClientID\",\"App_ID\":\"ExampleAppID\",\"AutoCreate\":false,\"enableFetchRingBuffer\":true,\"databaseMetadataCurrentDbOnly\":true}"
 } ] }`
