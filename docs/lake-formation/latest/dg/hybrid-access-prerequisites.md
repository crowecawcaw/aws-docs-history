# Prerequisites for setting up hybrid access mode

The following are the prerequisites for setting up hybrid access mode:

###### Note

We recommend that a Lake Formation administrator registers the Amazon S3 location in hybrid access mode, and opt in principals and resources.

1. Grant data location permission (`DATA_LOCATION_ACCESS`) to create Data Catalog
   resources that point to the Amazon S3 locations. Data location permissions control the
   ability to create Data Catalog catalogs, databases and tables that point to particular Amazon S3
   locations.
2. To share Data Catalog resources with another account in hybrid access mode (without
   removing `IAMAllowedPrincipals` group permissions from the resource), you need
   to update the **Cross account version settings** to Version 4. To update
   the version using Lake Formation console, choose **Version 4** under
   **Cross account version settings** on the **Data Catalog
   settings** page.

You can also use the `put-data-lake-settings` AWS CLI command to set the
`CROSS_ACCOUNT_VERSION` parameter to version 4:

```
aws lakeformation put-data-lake-settings --region us-east-1 --data-lake-settings file://settings
{
"DataLakeAdmins": [
        {
"DataLakePrincipalIdentifier": "arn:aws:iam::`<111122223333>`:user/`<user-name>`"
        }
    ],
    "CreateDatabaseDefaultPermissions": [],
    "CreateTableDefaultPermissions": [],
    "Parameters": {
"CROSS_ACCOUNT_VERSION": "4"
    }
}

```

3. To grant cross-account permissions in hybrid access mode, the grantor must have the required IAM permissions for AWS Glue and AWS RAM services. The AWS managed policy `AWSLakeFormationCrossAccountManager`
   grants the required permissions. 
   To enable cross-account data sharing in hybrid access mode, we’ve updated the `AWSLakeFormationCrossAccountManager` managed policy by adding two new IAM permissions:
   - ram:ListResourceSharePermissions
   - ram:AssociateResourceSharePermission

###### Note

If you are not using the AWS managed policy for the grantor role, add the above policies to your custom policies.

## Amazon S3 bucket location and user access

When you create a catalog, database or a table in the AWS Glue Data Catalog, you can specify the
Amazon S3 bucket location of the underlying data and register it with Lake Formation. The tables below
describe how permissions work for AWS Glue and Lake Formation users (principals) based on the Amazon S3 data
location of the table or database.

| Amazon S3 location registered with Lake Formation                                | Amazon S3 location of a database                                                                                                                   | AWS Glue users                                                                                     | Lake Formation users |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------- |
| Registered with Lake Formation (in hybrid access mode or in Lake Formation mode) | Have read/write access to the Amazon S3 data location by inheriting permissions<br>from the IAMAllowedPrincipals group (super access) permissions. | Inherit permissions to create tables from their granted CREATE TABLE<br>permission.                |
| No associated Amazon S3 location                                                 | Require explicit DATA LOCATION permission for running CREATE TABLE and<br>INSERT TABLE statements.                                                 | Require explicit DATA LOCATION permission for running CREATE TABLE and<br>INSERT TABLE statements. |

###### **IsRegisteredWithLakeFormation** table

property

The `IsRegisteredWithLakeFormation` property of a table indicates whether
the data location of the table is registered with Lake Formation for the requester. If the
permission mode of the location is registered as Lake Formation, then the
`IsRegisteredWithLakeFormation` property is `true` for all users
accessing the data location because all users are considered as opted in for that table.
If the location is registered in hybrid access mode, then the value is set to
`true` only for users who have opted in for that table.

| How `IsRegisteredWithLakeFormation` works | Permission mode | Users/Roles | `IsRegisteredWithLakeFormation`                                                                                                                                                                                                                                                                                        | Description |
| ----------------------------------------- | --------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Lake Formation                            | All             | True        | When a location is registered with Lake Formation, the `IsRegisteredWithLakeFormation`<br>property will be set to true for all users. This means that the permissions<br>defined in Lake Formation apply to the registered location. Credential vending will be<br>done by Lake Formation.                             |
| Hybrid access mode                        | Opted in        | True        | For users who have opted in to using Lake Formation for data access and governance for<br>a table, the `IsRegisteredWithLakeFormation` property will be set to<br>`true` for that table. They are subject to the permission policies<br>defined in Lake Formation for the registered location.                         |
| Hybrid access mode                        | Not opted in    | False       | For users who have not opted in to using Lake Formation permissions, the<br>`IsRegisteredWithLakeFormation` property is set to<br>`false`. They are not subject to the permission policies defined in<br>Lake Formation for the registered location. Instead, users will follow the Amazon S3<br>permissions policies. |
