# Viewing principals and resources in hybrid access mode

Follow these steps to view databases, tables, and principals in hybrid access mode.

Console

1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. Under **Permissions**, choose **Hybrid access mode**.
3. The **Hybrid access mode** page shows the resources and principals that are currently in hybrid access mode..

AWS CLI

The following example shows how to list all opt in principals and resources that are in hybrid access mode.

```

aws lakeformation list-lake-formation-opt-ins

```

The following example shows how to list opt in for a specific principal-resource
pair.

```

aws lakeformation list-lake-formation-opt-ins --cli-input-json file://`file path`

json:
{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::`<account-id>`:role/`<role name>`"
    },
    "Resource": {
        "Table": {
            "CatalogId": "`<account-id>`",
            "DatabaseName": "`<database name>`",
            "Name": "`<table name>`"
          }
    }
}

```
