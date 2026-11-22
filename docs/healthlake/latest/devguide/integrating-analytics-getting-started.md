

# Getting started with HealthLake analytics

Complete the following steps to query HealthLake data with any analytics engine. Steps 1 and 2 apply to every engine. Step 3 applies to Apache Spark on Amazon EMR, Databricks, and Snowflake. Step 4 sends you to the page for your engine.


**Steps for each analytics engine**  

| Step | Amazon Athena and Amazon Redshift Spectrum | Spark on Amazon EMR | Databricks | Snowflake | 
| --- | --- | --- | --- | --- | 
| 1. Find the resource links | Required | Required | Required | Required | 
| 2. Grant Lake Formation permissions | Required. Principal: the IAM user or role that runs queries. Tables: all or named. | Required. Principal: the Amazon EMR Serverless runtime role. Tables: all or named. | Required. Principal: the HealthLake OpenSharing server's IAM role. Tables: all tables. | Required. Principal: the Snowflake integration's IAM role. Tables: named tables. | 
| 3. Turn on full table access | Not needed | Required | Required | Required | 
| 4. Set up your engine | [Using AWS analytics services](integrating-analytics-aws.md) | [Setting up Apache Spark on Amazon EMR](integrating-spark.md) | [Setting up the Databricks integration](integrating-databricks-setting-up.md) | [Setting up the Snowflake integration](integrating-snowflake-setting-up.md) | 

![Your IAM user or role queries a Glue resource link in your AWS account, named for the data store and ending in _healthlake_view. The resource link points to a target database in the HealthLake service account that holds one table for each FHIR resource type. You grant DESCRIBE on the resource link, and SELECT and DESCRIBE on the tables in the target database.](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-analytics-resource-link.png)


Before you begin, make sure that you have an IAM user or role that is a data lake administrator in Lake Formation. The user or role must be in the same AWS account and Region as the data store. For more information, see [Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin) in the *AWS Lake Formation Developer Guide*.

## Step 1: Find the resource links
<a name="integrating-analytics-granting-find"></a>

Each data store appears in the Lake Formation console as two entries: a *resource link* and the data store in the HealthLake service account. To learn more about resource links, see [How resource links work in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/resource-links-about.html) in the *AWS Lake Formation Developer Guide*.

------
#### [ Console ]

**To find the resource links (console)**

1. Open the [Lake Formation console](https://console.aws.amazon.com/lakeformation).

1. In the navigation pane, choose **Databases**.

1. Find the resource links. Their names appear in *italics* and end in `_healthlake_view`. Each resource link shows the HealthLake service account as the owner of its shared resource.

------
#### [ AWS CLI ]

**To list the HealthLake resource links (AWS CLI)**
+ List every HealthLake resource link with its target database and catalog ID.

  ```bash
  aws glue get-databases \
      --region {{us-east-1}} \
      --query "DatabaseList[?ends_with(Name, '_healthlake_view')].[Name, TargetDatabase.CatalogId, TargetDatabase.DatabaseName]" \
      --output table
  ```

  The output looks like the following:

  ```
  -------------------------------------------------------------------------------------------------------
  |                                             GetDatabases                                            |
  +----------------------------------------------------+--------------------------+---------------------+
  |  {{healthlake-demo_a1b2c3d4e5f6_healthlake_view}}   |  {{444455556666}}   |  {{target-database-name}}  |
  +----------------------------------------------------+--------------------------+---------------------+
  ```

  The command returns three columns for each data store:
  + The resource link name ({{resource-link-name}}).
  + The HealthLake service account that owns the target database ({{444455556666}}).
  + The target database name ({{target-database-name}}).

  You use these values when you grant access.

  If a data store has no row, HealthLake hasn't created a resource link for it.

**Note**  
The HealthLake service account can differ for each data store.

------

**Note**  
To inspect a table, use `aws glue get-table` (singular). The `get-tables` command reports `IsRegisteredWithLakeFormation: false` for these tables even though they're registered with Lake Formation.

**Result:** You have the resource link name, catalog ID, and target database name for each data store that you want to query.

## Step 2: Grant Lake Formation permissions
<a name="integrating-analytics-getting-started-grant"></a>

Grant the same Lake Formation permissions to the principal for your engine: `DESCRIBE` on the resource link, and `SELECT` and `DESCRIBE` on the tables in the target database. For Amazon Athena and Amazon Redshift Spectrum, the principal is the IAM user or role that runs queries. For Spark on Amazon EMR, it's the Amazon EMR Serverless runtime role. For Databricks, it's the OpenSharing server's IAM role. For Snowflake, it's the Snowflake integration's IAM role. Spark on Amazon EMR, Databricks, and Snowflake create this IAM role during engine setup in Step 4, so return to this step after you create it.

------
#### [ Console ]

For a user, group, or role to query the data, you must grant **Describe** permission on the resource link database. Then, you must grant **Select** and **Describe** on the tables.

**To grant DESCRIBE on the resource link (console)**

1. Open the [Lake Formation console](https://console.aws.amazon.com/lakeformation).

1. In the primary navigation bar, choose **Databases**.

1. On the **Databases** page, choose the radio button next to the name of the data store that is in italics.

1. Choose **Actions (▼)**.

1. Choose **Grant**.

1. On the **Grant data permissions** page, under **Principals**, choose **IAM users or roles**.

1. Under **IAM users or roles**, use the **down arrow (▼)**, or search for the IAM user, role, or group that you want to grant access to.

1. Under the **LF-Tags or catalog resources** card, choose the **Named data catalog resources** option.

1. Under **Databases**, use the **down arrow (▼)** to choose the HealthLake data store database that you want to share access to.

1. In the **Resource link permissions** card, under **Resource link permissions**, choose **Describe**.

When the grant is successful, the **Grant permission success** banner appears. To view the permission you just granted, choose **Data lake permissions**. Find the user, group, or role in the table. Under the **Permissions** column, you see **Describe** listed.

Now use **Grant on target** to grant **Select** and **Describe** on the tables in the database.

**To grant SELECT and DESCRIBE on the tables (console)**

1. Open the [Lake Formation console](https://console.aws.amazon.com/lakeformation).

1. In the primary navigation bar, choose **Databases**.

1. On the **Databases** page, choose the radio button next to the name of the data store that is in italics.

1. Choose **Actions (▼)**.

1. Choose **Grant on target**.

1. On the **Grant data permissions** page, under **Principals**, choose **IAM users or roles**.

1. Under **IAM users or roles**, use the **down arrow (▼)** or search for the IAM user, group, or role that you want to grant access to.

1. Under the **LF-Tags or catalog resources** card, choose the **Named data catalog resources** option.

1. Under **Databases**, use the **down arrow (▼)** to choose the HealthLake data store database that you want to grant access to.

1. Under **Tables**, choose **All tables** to share every table. To grant named tables only, choose the tables instead of **All tables**.

1. In the **Table permissions** card, under **Table permissions**, choose **Describe** and **Select**.

1. Choose **Grant**.

After you choose **Grant**, a **Grant permissions success** banner appears. The specified principal can now query the HealthLake data store.

------
#### [ AWS CLI ]

Grant the same permissions with the AWS CLI. Replace {{role-name}} with the IAM user or role that queries, or the engine's IAM role.

**To grant access with the AWS CLI**

1. Grant `DESCRIBE` on the data store resource link.

   ```bash
   aws lakeformation grant-permissions \
       --region {{us-east-1}} \
       --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/{{role-name}} \
       --resource '{"Database":{"Name":"{{resource-link-name}}"}}' \
       --permissions DESCRIBE
   ```

1. Grant `SELECT` and `DESCRIBE` on the tables in the target database. Choose one of the following options:
   + **All tables.** Grant on every table in the target database with `TableWildcard`.

     ```bash
     aws lakeformation grant-permissions \
         --region {{us-east-1}} \
         --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/{{role-name}} \
         --resource '{"Table":{"CatalogId":"{{444455556666}}","DatabaseName":"{{target-database-name}}","TableWildcard":{}}}' \
         --permissions SELECT DESCRIBE
     ```
   + **Named tables (recommended for least privilege).** Grant on one table by replacing `TableWildcard` with the table name. Repeat for each table.

     ```bash
     aws lakeformation grant-permissions \
         --region {{us-east-1}} \
         --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/{{role-name}} \
         --resource '{"Table":{"CatalogId":"{{444455556666}}","DatabaseName":"{{target-database-name}}","Name":"{{table-name}}"}}' \
         --permissions SELECT DESCRIBE
     ```

1. Verify the grants on the principal. The `list-permissions` command requires `--resource`, so run it once for the resource link and once for the tables.

   ```bash
   aws lakeformation list-permissions \
       --region {{us-east-1}} \
       --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/{{role-name}} \
       --resource '{"Database":{"Name":"{{resource-link-name}}"}}'
   
   aws lakeformation list-permissions \
       --region {{us-east-1}} \
       --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/{{role-name}} \
       --resource '{"Table":{"CatalogId":"{{444455556666}}","DatabaseName":"{{target-database-name}}","TableWildcard":{}}}'
   ```

   The first command lists `DESCRIBE` on the resource link. The second lists `SELECT` and `DESCRIBE` on the target tables. For named tables, replace `"TableWildcard":{}` with `"Name":"{{table-name}}"`.

   The resource link check can also list `ALL` when the `IAMAllowedPrincipals` group holds it on the link.

Repeat for each data store. For more information, see [Granting permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html) in the *AWS Lake Formation Developer Guide*.

------

**Result:** The principal for your engine can request Lake Formation credentials and read the HealthLake tables that you granted.

## Step 3: Turn on full table access (Spark on Amazon EMR, Databricks, and Snowflake)
<a name="integrating-analytics-full-table-access"></a>

Skip this step if you use only Amazon Athena or Amazon Redshift Spectrum. Spark on Amazon EMR, Databricks, and Snowflake need full table access; Amazon Athena and Amazon Redshift Spectrum don't.

Full table access lets external engines request Lake Formation credentials for tables on which they have full table access. This setting applies to the entire AWS account and Region. For more information, see [Allow external engines to access data with full table access](https://docs.aws.amazon.com/lake-formation/latest/dg/full-table-credential-vending.html) in the *AWS Lake Formation Developer Guide*.

Before you turn it on, record whether it's already on. Review the other external engines in the account and Region to confirm that full table access is compatible with their authorization model. The setting doesn't grant access to any table by itself. The IAM policies and Lake Formation grants must also authorize each request.

------
#### [ Console ]

**To allow full table access for external engines (console)**

1. Open the [AWS Lake Formation console](https://console.aws.amazon.com/lakeformation).

1. In the navigation pane, expand **Administration**, and then choose **Application integration settings**.

1. Choose **Allow external engines to access data in Amazon S3 locations with full table access**.

1. Choose **Save**.

------
#### [ AWS CLI ]

**Important**  
`put-data-lake-settings` replaces all data lake settings, including your data lake administrators. Always start from the current settings.

**To allow full table access for external engines (AWS CLI)**

1. Read your current data lake settings, set `AllowFullTableExternalDataAccess` to `true`, and write the result to a file. This command requires `jq`. Without it, edit the saved file manually and change only this value.

   ```bash
   aws lakeformation get-data-lake-settings --region {{us-east-1}} \
     | jq '.DataLakeSettings.AllowFullTableExternalDataAccess = true' > data-lake-settings.json
   ```

1. Apply the updated settings.

   ```bash
   aws lakeformation put-data-lake-settings --region {{us-east-1}} \
       --cli-input-json file://data-lake-settings.json
   ```

**To confirm full table access**
+ Confirm that full table access is on.

  ```bash
  aws lakeformation get-data-lake-settings \
      --region {{us-east-1}} \
      --query DataLakeSettings.AllowFullTableExternalDataAccess
  ```

  The output is `true`.

------

**Turning it off:** Turn off full table access only if it was off before you turned it on and no other engine depends on it. Repeat the preceding console or AWS CLI procedure with the value set to `false`.

**Important**  
Other engines that use Lake Formation credential vending stop working if you turn off full table access.

**Result:** External engines, such as Spark on Amazon EMR, Databricks, and Snowflake, can request Lake Formation credentials for tables on which they have full table access.

## Step 4: Set up your analytics engine
<a name="integrating-analytics-getting-started-engine"></a>

Set up the engine that you query with. Each page covers the engine-specific connection and configuration:
+ [Using AWS analytics services](integrating-analytics-aws.md)
+ [Setting up the Databricks integration](integrating-databricks-setting-up.md)
+ [Setting up the Snowflake integration](integrating-snowflake-setting-up.md)

**Result:** You're on your engine's setup page, ready to connect and query HealthLake data.

## Revoking access
<a name="integrating-analytics-granting-revoke"></a>

To revoke access, run the following commands for each data store, with the engine's principal. If you granted named tables, replace `TableWildcard` with the table name and repeat for each table.

```bash
aws lakeformation revoke-permissions \
    --region {{us-east-1}} \
    --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/{{role-name}} \
    --resource '{"Database":{"Name":"{{resource-link-name}}"}}' \
    --permissions DESCRIBE

aws lakeformation revoke-permissions \
    --region {{us-east-1}} \
    --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/{{role-name}} \
    --resource '{"Table":{"CatalogId":"{{444455556666}}","DatabaseName":"{{target-database-name}}","TableWildcard":{}}}' \
    --permissions SELECT DESCRIBE
```

**Note**  
Revoking a grant blocks new Lake Formation credentials under that grant, but it doesn't invalidate credentials or AWS STS sessions that were already issued. Running queries and sessions can continue until their credentials expire.