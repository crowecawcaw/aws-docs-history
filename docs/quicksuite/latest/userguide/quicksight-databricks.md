# Using Databricks in Quick Sight

Use this section to learn how to connect from Quick Sight to Databricks.

###### To connect to Databricks

1. Begin by creating a new dataset. Choose **Data** from the
   navigation pane at left.
2. Choose **Create** then **New
   Dataset**.
3. Choose the **Databricks** data source card.
4. For **Data source name**, enter a descriptive name for your
   Databricks data source connection, for example `Databricks CS`.
   Because you can create many datasets from a connection to Databricks, it's
   best to keep the name simple.
5. For **Connection type**, select the type of network you're
   using.
   - Public network – if your data is
     shared publicly.
   - VPC – if your data is inside a
     VPC.

###### Note

If you're using VPC, and you don't see it listed, check with your
administrator. 6. For **Database server**, enter the **Hostname of
workspace** specified in your Databricks connection details. 7. For **HTTP Path**, enter the **Partial URL for the
spark instance** specified in your Databricks connection
details. 8. For **Port**, enter the **port** specified
in your Databricks connection details. 9. For **Username** and **Password**, enter
your connection credentials. 10. To verify the connection is working, click **Validate
connection**. 11. To finish and create the data source, click **Create data
source**.

## Adding a new Quick Sight

dataset for Databricks

After you have an existing data source connection for Databricks data, you can
create Databricks datasets to use for analysis.

###### To create a dataset using Databricks

1. Choose **Data** at left, then scroll down to find the
   data source card for your Databricks connection. If you have many data
   sources, you can use the search bar at the top of the page to find your data
   source with a partial match on the name.
2. Choose the **Databricks** data source card, and then
   choose **Create data set**.
3. To specify the table you want to connect to, first select the Catalog and
   Schema you want to use. Then, for **Tables**, select the
   table that you want to use. If you prefer to use your own SQL statement,
   select **Use custom SQL**.
4. Choose **Edit/Preview**.
5. (Optional) To add more data, use the following steps:
   1. Choose **Add data** at top right.
   2. To connect to different data, choose **Switch data
      source**, and choose a different dataset.
   3. Follow the UI prompts to finish adding data.
   4. After adding new data to the same dataset, choose
      **Configure this join** (the two red dots). Set
      up a join for each additional table.
   5. If you want to add calculated fields, choose **Add
      calculated field**.
   6. To add a model from SageMaker AI, choose **Augment with
      SageMaker**. This option is only available in
      Quick Suite Enterprise edition.
   7. Clear the check box for any fields that you want to omit.
   8. Update any data types that you want to change.

6. When you are done, choose **Save** to save and close the
   dataset.

## Quick Sight

Administrator's guide to connecting Databricks

You can use Amazon Quick Sight to connect to Databricks on AWS. You can
connect to Databricks on AWS whether you signed up for through AWS Marketplace
or through the Databricks website.

Before you can connect to Databricks, your create or identify existing resources
that the connection requires. Use this section to help you gather the resources you
need to connect from Quick Sight to Databricks.

- To learn how to obtain your Databricks connection details, see [Databricks ODBC and JDBC connections](https://docs.databricks.com/integrations/jdbc-odbc-bi.html#get-server-hostname-port-http-path-and-jdbc-url "https://docs.databricks.com/integrations/jdbc-odbc-bi.html#get-server-hostname-port-http-path-and-jdbc-url")..
- To learn how to obtain your Databricks credentials—personal access
  token or user name and password—for authentication, see [Authentication requirements](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#authentication-requirements "https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#authentication-requirements") in the [Databricks
  documentation](https://docs.databricks.com/index.html "https://docs.databricks.com/index.html").

To connect to a Databricks cluster, you need `Can Attach To`
and `Can Restart` permissions. These permissions are managed in
Databricks. For more information, see [Permission Requirements](https://docs.databricks.com/integrations/jdbc-odbc-bi.html#permission-requirements "https://docs.databricks.com/integrations/jdbc-odbc-bi.html#permission-requirements") in the [Databricks
documentation](https://docs.databricks.com/index.html "https://docs.databricks.com/index.html")..

- If you are setting up a private connection for Databricks, you can learn
  more about how to configure a VPC for use with Quick Sight, see [Connecting to a
  VPC with Amazon Quick Sight](../../../quicksight/latest/user/working-with-aws-vpc.md "../../../quicksight/latest/user/working-with-aws-vpc.md") in the Quick Sight documentation. If the
  connection isnt' visible, verify with a system administrator that the
  network has open [inbound endpoints for
  Amazon Route 53](../../../quicksight/latest/user/vpc-route-53.md "../../../quicksight/latest/user/vpc-route-53.md"). the hostname of a Databricks workspace uses a
  public IP , there needs to be DNS TCP
  and DNS UDP inbound and outbound rules to allow traffic on DNS port 53, for
  the Route 53 security group. An administrator needs to create a security
  group with 2 inbound rules: one for DNS(TCP) on port 53 to the VPC CIDR and
  one for DNS(UDP) for port 53 to the VPC CIDR.

For Databricks-related details if you are using PrivateLink instead of a
public connection, see [Enable AWS PrivateLink](https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html "https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html") in the [Databricks
documentation](https://docs.databricks.com/index.html "https://docs.databricks.com/index.html").
