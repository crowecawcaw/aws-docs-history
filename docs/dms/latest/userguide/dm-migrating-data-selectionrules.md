# Selection rules for homogeneous data migrations

You can use selection rules to choose the schema, tables, or both that you want to include in your replication.

When creating data migration task, choose **Add selection rule**.

For the rule settings, provide the following values:

- **Schema**: Choose **Enter a schema**.
- **Schema name**: Provide the name of the schema you want to replicate,
  or use `%` as a wildcard.
- **Table name**: : Provide the name of the table you want to replicate,
  or use `%` as a wildcard.
  By default, the only rule-action that DMS supports is `Include`, and the
  only wildcard character that DMS supports is `%`.

###### Note

The support for selection rules AWS DMS for homogeneous data migrations varies based on the combination of the source
database engine and the migration type chosen. PostgreSQL and MongoDB-compatible sources allow selection rules for all migration
types, while MySQL sources only support selection rules for the Full Load migration type.

###### Example Migrate all tables in a schema

The following example migrates all tables from a schema named `dmsst` in your source to your target endpoint.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-action": "include",
            "object-locator": {
                "schema-name": "dmsst",
                "table-name": "%"
            },
            "filters": [],
            "rule-id": "1",
            "rule-name": "1"
        }
    ]
}
```

###### Example Migrate some tables in a schema

The following example migrates all tables with a name starting with `collectionTest`,
from a schema named `dmsst` in your source to your target endpoint.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-action": "include",
            "object-locator": {
                "schema-name": "dmsst",
                "table-name": "collectionTest%"
            },
            "filters": [],
            "rule-id": "1",
            "rule-name": "1"
        }
    ]
}
```

###### Example Migrate specific tables from multiple schemas

The following example migrates some of the tables from multiple schemas
named `dmsst` and `Test` in your source to your target
endpoint.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-action": "include",
            "object-locator": {
                "schema-name": "dmsst",
                "table-name": "collectionTest1"
            },
            "filters": [],
            "rule-id": "1",
            "rule-name": "1"
        },
        {
            "rule-type": "selection",
            "rule-action": "include",
            "object-locator": {
                "schema-name": "Test",
                "table-name": "products"
            },
            "filters": [],
            "rule-id": "2",
            "rule-name": "2"
        }
    ]
}
```
