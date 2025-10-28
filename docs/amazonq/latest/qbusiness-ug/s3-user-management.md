# How Amazon Q Business connector

crawls Amazon S3 ACLs

You add access control information to a document in an Amazon S3 data source using
a metadata file associated with the document. You specify the file using the console or as
the `aclConfigurationFilePath` parameter when you call the
`CreateDataSource` or `UpdateDataSource` API and use the
`configuration` parameter.

###### Note

The ACL file and data should be stored in the same Amazon S3 bucket.

The configuration file contains a JSON structure that identifies an Amazon S3
prefix and lists the access settings for the prefix. The prefix can be a path, or it can be
an individual file. If the prefix is a path, the access settings apply to all of the files
in that path.

You provide three pieces of information in the file:

- The access that the entity should have. You can use `ALLOW` or
  `DENY`.
- The type of entity. You can use `USER` or `GROUP`.
- The name of the entity.

###### Important

The system grants ALL users access to prefixes that do NOT appear in the ACL file.

The JSON structure for the configuration file must be in the following format:

```
[
    {
        "keyPrefix": "s3://BUCKETNAME/prefix1/",
        "aclEntries": [
            {
                "Name": "user1@example.com",
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
        "keyPrefix": "s3://BUCKETNAME/prefix2/",
        "aclEntries": [
            {
                "Name": "user2@example.com",
                "Type": "USER",
                "Access": "ALLOW"
            },
            {
                "Name": "user1@example.com",
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

For more
information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
