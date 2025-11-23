# Configuring Athena for queries

###### Important

AWS HealthOmics variant stores and annotation stores are no longer open to new customers.
Existing customers can continue to use the service as normal.
For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

You can use Athena to query variants and annotations. Before you run any queries, perform the following
setup tasks:

###### Topics

- [Configure a query results location using the Athena console](#configure-athena-query "#configure-athena-query")
- [Configure a workgroup with Athena engine v3](#configure-athena-workgroup "#configure-athena-workgroup")

## Configure a query results location using the Athena console

To configure a query results location, follow these steps.

1. Open the Athena console: [Athena console](https://console.aws.amazon.com//athena "https://console.aws.amazon.com//athena")
2. In the primary navigation bar, choose **Query editor**.
3. In the query editor, choose the **Settings** tab, then choose
   **Manage**.
4. Enter an S3 prefix of a location to save the query result.

## Configure a workgroup with Athena engine v3

To configure a workgroup, follow these steps.

1. Open the Athena console: [Athena console](https://console.aws.amazon.com//athena "https://console.aws.amazon.com//athena")
2. In the primary navigation bar, choose **Workgroups**, then **Create workgroup**.
3. Enter a name for the workgroup.
4. Select **Athena SQL** as the type of engine.
5. Under **Upgrade query engine**, select **Manual**.
6. Under **Query version engine**, select **Athena version 3**.
7. Choose **Create workgroup**.
