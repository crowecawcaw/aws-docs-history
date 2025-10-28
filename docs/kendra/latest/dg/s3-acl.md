# Access control for Amazon S3 data sources

You can control access to documents in an Amazon S3 data source using a
configuration file. You specify the file in the console or as the
`AccessControlListConfiguration` parameter when you call the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") or [UpdateDataSource](../APIReference/API_UpdateDataSource.md "../APIReference/API_UpdateDataSource.md")
API.

The configuration file contains a JSON structure that identifies an S3 prefix and
lists the access settings for the prefix. The prefix can be a path, or it can be an
individual file. If the prefix is a path, the access settings apply to all of the files
in that path. There is a maximum number of S3 prefixes in the JSON configuration file
and a default maximum file size. For more information, see
[Quotas for Amazon Kendra](quotas.md "quotas.md")

You can specify both users and groups in the access settings. When you query the
index, you specify user and group information. For more information, see [Filtering by user attribute](user-context-filter.md#context-filter-attribute "user-context-filter.md#context-filter-attribute").

The JSON structure for the configuration file must be in the following format:

```
[
    {
        "keyPrefix": "s3://BUCKETNAME/prefix1/",
        "aclEntries": [
            {
                "Name": "user1",
                "Type": "USER",
                "Access": "ALLOW"
            },
            {
                "Name": "group1",
                "Type": "GROUP",
                "Access": "DENY"
            }
        ]
    },
    {
        "keyPrefix": "s3://prefix2",
        "aclEntries": [
            {
                "Name": "user2",
                "Type": "USER",
                "Access": "ALLOW"
            },
            {
                "Name": "user1",
                "Type": "USER",
                "Access": "DENY"
            },
            {
                "Name": "group1",
                "Type": "GROUP",
                "Access": "DENY"
            }
        ]
    }
]
```
