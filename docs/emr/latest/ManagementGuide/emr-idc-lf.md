# Configure Lake Formation for an IAM Identity Center enabled

EMR cluster

You can integrate [AWS Lake Formation](../../../lake-formation/latest/dg.md "../../../lake-formation/latest/dg.md")
with your AWS IAM Identity Center enabled EMR cluster.

First, be sure you have an Identity Center instance set up in the same Region as your
cluster. For more information, see [Create an Identity Center instance](emr-idc-start.md#emr-idc-start-instance "emr-idc-start.md#emr-idc-start-instance"). You can find the instance ARN in the
IAM Identity Center console when you view the instance details, or use the following command to
view details for all your instances from the CLI:

```
aws sso-admin list-instances
```

Then use the ARN and your AWS account ID with the following command to configure
Lake Formation to be compatible with IAM Identity Center:

```
aws lakeformation create-lake-formation-identity-center-configuration --cli-input-json file://create-lake-fromation-idc-config.json
json input:
{
    "CatalogId": "`account-id/org-account-id`",
    "InstanceArn": "`identity-center-instance-arn`"
}
```

Now, call `put-data-lake-settings` and enable
`AllowFullTableExternalDataAccess` with Lake Formation:

```
aws lakeformation put-data-lake-settings --cli-input-json file://put-data-lake-settings.json
json input:
{
    "DataLakeSettings": {
        "DataLakeAdmins": [
            {
                "DataLakePrincipalIdentifier": "`admin-ARN`"
            }
        ],
        "CreateDatabaseDefaultPermissions": `[...]`,
        "CreateTableDefaultPermissions": `[...]`,
        "AllowExternalDataFiltering": true,
        "AllowFullTableExternalDataAccess": true
    }
}
```

Finally, grant full table permissions to the identity ARN for the user that
accesses the EMR cluster. The ARN contains the user ID from Identity Center. Navigate
to Identity Center in the console, select **Users**, and then select the
user to view their **General information** settings.

Copy the User ID and paste it into the following ARN for
`user-id`:

```
arn:aws:identitystore:::user/`user-id`
```

###### Note

Queries on the EMR cluster only work if the IAM Identity Center identity has full table
access on the Lake Formation protected table. If the identity doesn't have full table
access, then the query will fail.

Use the following command to grant the user full table access:

```
aws lakeformation grant-permissions --cli-input-json file://grantpermissions.json
json input:
{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:identitystore:::user/`user-id`"
    },
    "Resource": {
        "Table": {
            "DatabaseName": "tip_db",
            "Name": "tip_table"
        }
    },
    "Permissions": [
        "ALL"
    ],
    "PermissionsWithGrantOption": [
        "ALL"
    ]
}
```

## Adding the application ARN to IDC for Lake Formation integration

In order to query Lake Formation enabled resources, the Application ARN of the IDC application needs
to be added. To do this, follow these steps:

1. On the console, choose **AWS Lake Formation**.
2. Select **IAM Identity Center integration** and **Lake Formation
   application integration** by matching the application ARN. The ARN will appear in the **Application ID**
   list.
