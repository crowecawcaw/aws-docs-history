# Cascading cross-account permissions

Follow these steps to set up and test cross-account permission cascading:

1. Create an LF-Tag using the Lake Formation console:
   - **Tag Key**: `c175912681300719`
   - **Tag Values**: `[`all`, `public`]`

2. Associate a table with the tag and value:
   - **Key**: `c175912681300719`
   - **Value**: `all`

3. Grant cross-account tag policy permission. Grant `SELECT` permission on tag policy from account `111122223333` to account `444455556666`:

```

aws lakeformation grant-permissions \
  --cli-input-json '{
    "Principal": {
        "DataLakePrincipalIdentifier": "`444455556666`"
    },
    "Resource": {
        "LFTagPolicy": {
            "CatalogId": "`111122223333`",
            "ResourceType": "TABLE",
            "Expression": [{
                "TagKey": "`c175912681300719`",
                "TagValues": [
                    "`all`"
                ]
            }]
        }
    },
    "Permissions": [
        "SELECT"
    ]
}'

```

The consumer account (`444455556666`) admin can access tables tagged with the tag ``c175912681300719`:`all``. The consumer account can't cascade permission grants to other users with either of the tag values. 4. Grant `DESCRIBE` permission. The producer account admin grants `DESCRIBE` on the tag key and both values to the consumer account:

```

aws lakeformation grant-permissions \
  --cli-input-json '{
    "Principal": {
        "DataLakePrincipalIdentifier": "`444455556666`"
    },
    "Resource": {
       "LFTag": {
            "CatalogId": "`111122223333`",
            "TagKey": "`c175912681300719`",
             "TagValues": ["`all`","`public`"]
        }
    },
    "Permissions": [
        "DESCRIBE"
    ]
}'

```

The consumer account admin tries to cascade the permission to other users using the tag `c175912681300719` and value "`all`" (identical policy):

```

aws lakeformation grant-permissions --region us-east-1 --cli-input-json '{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::`444455556666`:role/`AccessAnalyzerTrustedService`"
    },
    "Resource": {
       "LFTagPolicy": {
            "CatalogId": "`111122223333`",
            "ResourceType": "TABLE",
            "Expression": [
                {
                    "TagKey": "`c175912681300719`",
                    "TagValues": [
                        "`all`"
                    ]
                }
            ]
        }
    },
    "Permissions": [
        "SELECT"
    ]
}'

```

**Result:** AccessDeniedException

The grant fails because Lake Formation detects that the LF-Tag policy is exactly the same as the LF-Tag policy used by the producer account to share resources with the consumer account, and only checks if the user has grantable permissions, not Rule #2 (DESCRIBE permissions).

Grant with multiple tag values:

```

aws lakeformation grant-permissions --region us-east-1 --cli-input-json '{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::`444455556666`:role/`AccessAnalyzerTrustedService`"
    },
    "Resource": {
       "LFTagPolicy": {
            "CatalogId": "`111122223333`",
            "ResourceType": "TABLE",
            "Expression": [
                {
                    "TagKey": "`c175912681300719`",
                    "TagValues": [
                        "`all`","`public`"
                    ]
                }
            ]
        }
    },
    "Permissions": [
        "SELECT"
    ]
}'

```

**Result** – Success – Policy is not identical, so Rule #2 applies and DESCRIBE permissions are sufficient.

Consumer attempts single `public` value – Succeeds:

```

aws lakeformation grant-permissions
--cli-input-json '{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::`444455556666`:role/`AccessAnalyzerTrustedService`"
    },
    "Resource": {
       "LFTagPolicy": {
            "CatalogId": "`111122223333`",
            "ResourceType": "TABLE",
            "Expression": [
                {
                    "TagKey": "`c175912681300719`",
                    "TagValues": [
                        "`public`"
                    ]
                }
            ]
        }
    },
    "Permissions": [
        "SELECT"
    ]
}'

```

Policy is not identical, so Rule #2 applies.
