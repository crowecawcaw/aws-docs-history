Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Getting authentication profiles

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
