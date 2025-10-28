# Removing principals and resources from hybrid access mode

Follow these steps to remove databases, tables, and principals from hybrid access mode.

Console

1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. Under **Permissions**, choose **Hybrid access mode**.
3. On the **Hybrid access mode** page, select the checkbox next to the database or table name and choose `Remove`.
4. A warning message prompts you to confirm the action. Choose **Remove**.

Lake Formation no longer enforces permissions for those resources, and access to this resource will be controlled using IAM and AWS Glue permissions.
This may cause the user to no longer have access to this resource if they don't have the appropriate IAM permissions.

AWS CLI

The following example shows how to remove resources from hybrid access mode.

```
aws lakeformation delete-lake-formation-opt-in --cli-input-json file://`file path`

json:
{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::`<123456789012>`:role/`role name`"
    },
    "Resource": {
        "Table": {
            "CatalogId": "`<123456789012>`",
            "DatabaseName": "`<database name>`",
            "Name": "`<table name>`"
          }
    }
}

```
