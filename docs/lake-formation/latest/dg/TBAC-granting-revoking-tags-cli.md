# Managing LF-Tag

permissions using the AWS CLI

You can grant, revoke, and list permissions on LF-Tags by using the AWS Command Line Interface
(AWS CLI).

###### To list LF-Tag permissions (AWS CLI)

- Enter a `list-permissions` command. You must be the LF-Tag creator, a data
  lake administrator, or have the `Drop`, `Alter`, `Describe`, `Associate`, `Grant with LF-Tag permissions` permission
  on a LF-Tag to see it.

The following command requests all LF-Tags that you have permissions on.

```
aws lakeformation list-permissions --resource-type LF_TAG
```

The following is sample output for a data lake administrator, who sees all LF-Tags
granted to all principals. Non-administrative users see only LF-Tags granted to them.
LF-Tag permissions granted from an external account appear on a separate results page.
To see them, repeat the command and supply the `--next-token` argument with the
token returned from the previous command run.

```
{
    "PrincipalResourcePermissions": [
        {
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/datalake_admin"
            },
            "Resource": {
                "LFTag": {
                    "CatalogId": "111122223333",
                    "TagKey": "environment",
                    "TagValues": [
                        "*"
                    ]
                }
            },
            "Permissions": [
                "ASSOCIATE"
            ],
            "PermissionsWithGrantOption": [
                "ASSOCIATE"
            ]
        },
        {
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/datalake_user1"
            },
            "Resource": {
                "LFTag": {
                    "CatalogId": "111122223333",
                    "TagKey": "module",
                    "TagValues": [
                        "Orders",
                        "Sales"
                    ]
                }
            },
            "Permissions": [
                "DESCRIBE"
            ],
            "PermissionsWithGrantOption": []
        },
...
    ],
    "NextToken": "eyJzaG91bGRRdWVy...Wlzc2lvbnMiOnRydWV9"
}


```

You can list all grants for a specific LF-Tag key. The following command returns all
permissions granted on the LF-Tag `module`.

```
aws lakeformation list-permissions --resource-type LF_TAG --resource '{ "LFTag": {"CatalogId":"111122223333","TagKey":"module","TagValues":["*"]}}'
```

You can also list LF-Tag values granted to a specific principal for a specific
LF-Tag. When supplying the `--principal` argument, you must supply the
`--resource` argument. Therefore, the command can only effectively request
the values granted to a specific principal for a specific LF-Tag key. The following
command shows how to do this for the principal `datalake_user1` and the
LF-Tag key `module`.

```
aws lakeformation list-permissions --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:user/datalake_user1 --resource-type LF_TAG --resource '{ "LFTag": {"CatalogId":"111122223333","TagKey":"module","TagValues":["*"]}}'
```

The following is sample output.

```
{
    "PrincipalResourcePermissions": [
        {
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/datalake_user1"
            },
            "Resource": {
                "LFTag": {
                    "CatalogId": "111122223333",
                    "TagKey": "module",
                    "TagValues": [
                        "Orders",
                        "Sales"
                    ]
                }
            },
            "Permissions": [
                "ASSOCIATE"
            ],
            "PermissionsWithGrantOption": []
        }
    ]
}
```

###### To grant permissions on LF-Tags (AWS CLI)

1. Enter a command similar to the following. This example grants to user
   `datalake_user1` the `Associate` permission on the LF-Tag with
   the key `module`. It grants permissions to view and assign all values for that
   key, as indicated by the asterisk (\*).

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:user/datalake_user1 --permissions "ASSOCIATE" --resource '{ "LFTag": {"CatalogId":"111122223333","TagKey":"module","TagValues":["*"]}}'
```

Granting the `Associate` permission implicitly grants the
`Describe` permission.

The next example grants `Associate` to the external AWS account
1234-5678-9012 on the LF-Tag with the key `module`, with the grant
option. It grants permissions to view and assign only the values `sales` and
`orders`.

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=123456789012 --permissions "ASSOCIATE" --permissions-with-grant-option "ASSOCIATE" --resource '{ "LFTag": {"CatalogId":"111122223333","TagKey":"module","TagValues":["sales", "orders"]}}'
```

2. Granting the `GrantWithLFTagExpression` permission implicitly grants the
   `Describe` permission.

The next example grants `GrantWithLFTagExpression` to a user on the LF-Tag with the key `module`, with the grant
option. It grants permissions to view and grant permissions on Data Catalog resources using only the values `sales` and
`orders`.

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=111122223333 --permissions "GrantWithLFTagExpression" --permissions-with-grant-option "GrantWithLFTagExpression" --resource '{ "LFTag": {"CatalogId":"111122223333","TagKey":"module","TagValues":["sales", "orders"]}}'
```

3. The next example grants `Drop` permissions to a user on the LF-Tag with
   the key `module`, with the grant option. It grants permissions to delete the LF-Tag. To delete a LF-Tag, you need permissions on all values for that key.

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=111122223333 --permissions "DROP" --permissions-with-grant-option "DROP" --resource '{ "LFTag": {"CatalogId":"111122223333","TagKey":"module","TagValues":["*"]}}'
```

4. The next example grants `Alter` permissions to the user on the LF-Tag with
   the key `module`, with the grant option. It grants permissions to delete the LF-Tag. To update a LF-Tag, you need permissions on all values for that key.

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=111122223333 --permissions "ALTER" --permissions-with-grant-option "ALTER" --resource '{ "LFTag": {"CatalogId":"111122223333","TagKey":"module","TagValues":["*"]}}'
```

###### To revoke permissions on LF-Tags (AWS CLI)

- Enter a command similar to the following. This example revokes the
  `Associate` permission on the LF-Tag with the key `module` from
  user `datalake_user1`.

```
aws lakeformation revoke-permissions --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:user/datalake_user1 --permissions "ASSOCIATE" --resource '{ "LFTag": {"CatalogId":"111122223333","TagKey":"module","TagValues":["*"]}}'
```
