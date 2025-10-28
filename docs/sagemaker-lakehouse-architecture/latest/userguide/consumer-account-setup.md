# Configure account B

To configure the receipient account, account B, the Lake Formation administrator accepts the AWS Resource Access Manager
(AWS RAM) shares, creates resource links that point to the shared catalog, database, and
tables, and configures permissions for the AWS Glue execution role
(`Glue-execution-role`).

## Accept and verify the shared resources

Lake Formation uses AWS RAM shares to enable cross-account sharing with Data Catalog resource policies.
To view and verify the shared resources from account A:

1. Log in to the AWS Management Console from account B and set the AWS Region to match the shared
   resource Region of account A.
2. Open the [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). You will see a message indicating there is a pending
   invite.
3. Follow the instructions to review and accept the pending invites on the AWS RAM console.
4. When the invite status changes to **Accepted**, choose **Shared resources** under **Shared with me** in the navigation pane.
5. Verify that the shared resources display correctly with ID of account A under the
   **Owner ID** column.

###### Note

You won't see an AWS RAM share invite for the catalog level on the Lake Formation console, because
catalog-level sharing isn’t possible. You can review the shared federated catalog and Amazon Redshift
managed catalog names on the AWS RAM console, or using the [AWS Command Line Interface](http://aws.amazon.com/cli "http://aws.amazon.com/cli") (AWS CLI) or SDK.

## Create a catalog link container and resource links

A catalog link container is a data catalog object that references a local or cross-account
federated database-level catalog from other AWS accounts. For more details, see [Accessing a shared federated catalog](../../../lake-formation/latest/dg/catalog-resource-link.md "../../../lake-formation/latest/dg/catalog-resource-link.md").

Create a catalog link container that points to federated catalog in account A:

1. On the Lake Formation console, under **Data Catalog** in the navigation pane, choose **Catalogs**.
2. Choose **Create catalog**.
3. Provide the following details for the catalog:
   1. Enter a name for the catalog.
   2. For **Type**, choose **Catalog Link
      container**.
   3. For **Source**, choose **Amazon Redshift**.
   4. For **Target Redshift Catalog**, enter the ARN of the federated
      catalog in account A.

   ```
   arn:aws:glue:`us-west-2`:`<<account A ID>>`:catalog/`redshiftserverless1-uswest2`/`ordersdb`
   ```

   5. Under **Access from engines**, select **Access
      this catalog from Apache Iceberg compatible engines**.
   6. For **IAM role**, provide the Redshift-S3 data transfer
      role that you had created in the prerequisites.
   7. Choose **Next**.

4. On the **Grant permissions – optional** page, choose
   **Add permissions**.
   1. Grant the `Admin` user **Super user** permissions for
      **Catalog permissions** and **Grantable
      permissions**.
   2. Choose **Add** and then choose **Next**.

5. Review the details on the **Review and create** page and
   then choose **Create catalog**.

Wait a few seconds for the catalog to show up. 6. In the navigation pane, choose **Catalogs** and verify that your
catalog is created.

## Create a database under the catalog link container

After creating the catalog link container, create a database under your catalog:

1. On the Lake Formation console, under **Data Catalog** in the navigation pane, choose **Databases**.
2. On the **Choose catalog** dropdown menu, choose your catalog link
   container.
3. Choose **Create database**.
4. Provide details for the database:
   1. Enter a name.
   2. For **Catalog**, choose select your catalog link container.
   3. Under **Default permissions for newly created tables**,
      clear the **Use only IAM access control for new tables in this
      database** box.
   4. Choose **Create database**.

5. Choose **Catalogs** in the navigation pane to verify that database is
   created under your catalog.

## Create a table resource link for the shared federated

catalog table

A resource link to a shared federated catalog table can reside only inside the database of
a catalog link container. A resource link for such tables will not work if created inside
the default catalog. For more details on resource links, see [Creating a resource link
to a shared Data Catalog table](../../../lake-formation/latest/dg/create-resource-link-table.md "../../../lake-formation/latest/dg/create-resource-link-table.md").

To create a table resource link:

1. On the Lake Formation console, under **Data Catalog** in the
   navigation pane, choose **Tables**.
2. On the **Create** dropdown menu, choose **Resource link**.
3. Provide details for the table resource link:
   1. For **Resource link name**, enter a name.
   2. For **Destination catalog**, choose catalog you created.
   3. For **Database**, choose your database.
   4. Choose a region for **Shared table’s region**.
   5. For **Shared table**, choose the table name.
   6. After you choose the **Shared table**, the **Shared table’s database** and **Shared table’s catalog
      ID** gets automatically populated.
   7. Choose **Create**.
   8. In the navigation pane, choose **Databases** to verify that table
      resource link is created under your database, inside the catalog you
      choose.

## Create a database resource link for the shared federated

catalog table

Create a database resource link in the default catalog to query the S3 based Iceberg table
shared from account A. For details on database resource links, refer [Creating a resource link to a shared Data Catalog database](../../../lake-formation/latest/dg/create-resource-link-database.md "../../../lake-formation/latest/dg/create-resource-link-database.md").

###### Note

A resource link is required to query from analytics engines, such as Athena, [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/"), and AWS Glue. When you use AWS Glue with
Lake Formation, the resource link name must be identical to the source account’s resource. For
additional details on using AWS Glue with Lake Formation, see [Considerations and
limitations](../../../lue/latest/dg/security-lf-enable-considerations.md "../../../lue/latest/dg/security-lf-enable-considerations.md").

To create a database resource link:

1. On the Lake Formation console, under **Data Catalog** in the
   navigation pane, choose **Databases**.
2. On the **Choose catalog** dropdown menu, choose the account
   ID to choose the default catalog.
3. Choose a darabase, and on the **Create** dropdown menu, choose
   **Resource link**.
4. Provide details for the resource link:
   1. For **Resource link name**, enter a name.

   The rest of the fields will automatically populate. 2. Choose **Create**.

5. In the navigation pane, choose **Databases** and verify that your
   database is created under the default catalog. Resource link names will show in
   italicized font.

## Verify access using Athena

Verify your access by running test queries in Athena:

1. Open the Athena console and ensure an Amazon S3 bucket is configured to store query results.
   For more information, see [Specify a query result location using the Athena console](../../../athena/latest/ug/query-results-specify-location-console.md "../../../athena/latest/ug/query-results-specify-location-console.md").
2. In the navigation pane, verify both the default catalog and federated catalog tables by
   previewing them.
3. Run a join query using the three-point notation for referring to tables from different
   catalogs as show in the following example:

```
SELECT
    `returns_tb.market` as Market,
    sum(`orders_tb`.quantity) as Total_Quantity
FROM `rl_link_container_ordersdb`.`public_db`.`rl_orderstbl as orders_tb`
JOIN awsdatacatalog.`customerdb`.`returnstbl_iceberg` as `returns_tb`
ON orders_tb.order_id = `returns_tb`.`order_id`
GROUP BY `returns_tb`.market;
```

## Grant permissions to the

`Glue-execution-role`

Set up Lake Formation permissions on the catalog link container, databases, tables, and resource
links for the AWS Glue job execution role
`Glue-execution-role` that you created in the
prerequisites:

1. On the Lake Formation console, choose **Data permissions** in the navigation pane.
2. Choose **Grant**.
3. Under **Principals**, select **IAM users and roles**
   and enter `Glue-execution-role`.
4. Under **LF-Tags or catalog resources**, select **Named Data
   Catalog resources**.
5. For **Catalogs**, choose your catalog and the account ID of
   account B, which indicates the default catalog.
6. Under **Catalog permissions**, select **Describe** for
   **Catalog permissions**.
7. Repeat these steps to grant additional permissions to
   `Glue-execution-role`.
