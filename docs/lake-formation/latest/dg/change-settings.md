# Changing the default settings for your data

lake

To maintain backward compatibility with AWS Glue, AWS Lake Formation has the following initial security
settings:

- The `Super` permission is granted to the group
  `IAMAllowedPrincipals` on all existing AWS Glue Data Catalog resources.
- "Use only IAM access control" settings are enabled for new Data Catalog resources.
  These settings effectively cause access to Data Catalog resources and Amazon S3 locations to be
  controlled solely by AWS Identity and Access Management (IAM) policies. Individual Lake Formation permissions are not in
  effect.

The `IAMAllowedPrincipals` group includes any IAM users and roles that are
allowed access to your Data Catalog resources by your IAM policies. The `Super`
permission enables a principal to perform every supported Lake Formation operation on the database or
table on which it is granted.

To change security settings so that access to Data Catalog resources (databases and tables) is
managed by Lake Formation permissions, do the following:

1. Change the default security settings for new resources. For instructions, see [Change the default permission model or use
   hybrid access mode](initial-lf-config.md#setup-change-cat-settings "initial-lf-config.md#setup-change-cat-settings").
2. Change the settings for existing Data Catalog resources. For instructions, see [Upgrading AWS Glue data permissions to
   the AWS Lake Formation model](upgrade-glue-lake-formation.md "upgrade-glue-lake-formation.md").

###### Changing the default security settings using the Lake Formation `PutDataLakeSettings`

API operation

You can also change default security settings by using the Lake Formation [PutDataLakeSettings](../APIReference/API_PutDataLakeSettings.md "../APIReference/API_PutDataLakeSettings.md") API operation.
This action takes as arguments an optional catalog ID and a [DataLakeSettings](../APIReference/API_DataLakeSettings.md "../APIReference/API_DataLakeSettings.md") structure.

To enforce metadata and underlying data access control by Lake Formation on new databases and
tables, code the `DataLakeSettings` structure as follows.

###### Note

Replace `<AccountID>` with a valid AWS account ID and
`<Username>` with a valid IAM user name. You can specify
more than one user as a data lake administrator.

```
{
    "DataLakeSettings": {
        "DataLakeAdmins": [
            {
                "DataLakePrincipalIdentifier": "arn:aws:iam::`<AccountId>`:user/`<Username>`"
            }
        ],
        "CreateDatabaseDefaultPermissions": [],
        "CreateTableDefaultPermissions": []
    }
}
```

You can also code the structure as follows. Omitting the
`CreateDatabaseDefaultPermissions` or `CreateTableDefaultPermissions`
parameter is equivalent to passing an empty list.

```
{
    "DataLakeSettings": {
        "DataLakeAdmins": [
            {
                "DataLakePrincipalIdentifier": "arn:aws:iam::`<AccountId>`:user/`<Username>`"
            }
        ]
    }
}
```

This action effectively revokes all Lake Formation permissions from the
`IAMAllowedPrincipals` group on new databases and tables. When you create a
database, you can override this setting.

To enforce metadata and underlying data access control only by IAM on new databases and
tables, code the `DataLakeSettings` structure as follows.

```
{
    "DataLakeSettings": {
        "DataLakeAdmins": [
            {
                "DataLakePrincipalIdentifier": "arn:aws:iam::`<AccountId>`:user/`<Username>`"
            }
        ],
        "CreateDatabaseDefaultPermissions": [
            {
                "Principal": {
                    "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                },
                "Permissions": [
                    "ALL"
                ]
            }
        ],
        "CreateTableDefaultPermissions": [
            {
                "Principal": {
                    "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                },
                "Permissions": [
                    "ALL"
                ]
            }
        ]
    }
}
```

This grants the `Super` Lake Formation permission to the
`IAMAllowedPrincipals` group on new databases and tables. When you create a
database, you can override this setting.

###### Note

In the preceding `DataLakeSettings` structure, the only permitted value for
`DataLakePrincipalIdentifier` is `IAM_ALLOWED_PRINCIPALS`, and the
only permitted value for `Permissions` is `ALL`.
