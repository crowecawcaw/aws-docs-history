# Creating a dataset from a

database

The following procedures walk you through connecting to database data sources and
creating datasets. To create datasets from AWS data sources that your Amazon Quick Suite
account autodiscovered, use [Creating a dataset from an
autodiscovered Amazon Redshift cluster or Amazon RDS instance](#create-a-data-set-autodiscovered "#create-a-data-set-autodiscovered"). To create datasets from any
other database data sources, use [Creating a dataset using a database
that's not autodiscovered](#create-a-data-set-database "#create-a-data-set-database").

## Creating a dataset from an

autodiscovered Amazon Redshift cluster or Amazon RDS instance

Use the following procedure to create a connection to an autodiscovered AWS
data source.

###### To create a connection to an autodiscovered AWS data source

1. Check [Data source quotas](data-source-limits.md "data-source-limits.md") to make sure that your target
   table or query doesn't exceed data source quotas.
2. Confirm that the database credentials you plan to use have appropriate
   permissions as described in [Required permissions](required-permissions.md "required-permissions.md").
3. Make sure that you have configured the cluster or instance for Amazon Quick Suite
   access by following the instructions in [Network and database configuration requirements](configure-access.md "configure-access.md").
4. On the Amazon Quick Suite start page, choose **Data**.
5. Choose **Create** then choose **New
   dataset**.
6. Choose either the **RDS** or the **Redshift
   Auto-discovered** icon, depending on the AWS service that
   you want to connect to.
7. Enter the connection information for the data source, as
   follows:
   - For **Data source name**, enter a name for
     the data source.
   - For **Instance ID**, choose the name of the
     instance or cluster that you want to connect to.
   - **Database name** shows the default database
     for the **Instance ID** cluster or instance. To
     use a different database on that cluster or instance, enter its
     name.
   - For **UserName**, enter the user name of a
     user account that has permissions to do the following:
     - Access the target database.
     - Read (perform a `SELECT` statement on) any
       tables in that database that you want to use.

   - For **Password**, enter the password for the
     account that you entered.

8. Choose **Validate connection** to verify your
   connection information is correct.
9. If the connection validates, choose **Create data
   source**. If not, correct the connection information and
   try validating again.

###### Note

Amazon Quick Suite automatically secures connections to Amazon RDS instances and
Amazon Redshift clusters by using Secure Sockets Layer (SSL). You don't need to
do anything to enable this. 10. Choose one of the following:

    * **Custom SQL**


    On the next screen, you can choose to write a query with the
     **Use custom SQL** option. Doing this opens
     a screen named **Enter custom SQL query**,
     where you can enter a name for your query, and then enter the
     SQL. For best results, compose the query in a SQL editor, and
     then paste it into this window. After you name and enter the
     query, you can choose **Edit/Preview data** or
     **Confirm query**. Choose
     **Edit/Preview data** to immediately go to
     data preparation. Choose **Confirm query** to
     validate the SQL and make sure that there are no errors.
    * **Choose tables**


    To connect to specific tables, for **Schema: contain
     sets of tables**, choose
     **Select** and then choose a schema. In
     some cases where there is only a single schema in the database,
     that schema is automatically chosen, and the schema selection
     option isn't displayed.


    To prepare the data before creating an analysis, choose
     **Edit/Preview data** to open data
     preparation. Use this option if you want to join to more
     tables.


    Otherwise, after choosing a table, choose
     **Select**.

11. Choose one of the following options:
    - Prepare the data before creating an analysis. To do this,
      choose **Edit/Preview data** to open data
      preparation for the selected table. For more information about
      data preparation, see [Preparing dataset examples](preparing-data-sets.md "preparing-data-sets.md").
    - Create a dataset and analysis using the table data as-is and
      to import the dataset data into SPICE for
      improved performance (recommended). To do this, check the table
      size and the SPICE indicator to see if you have
      enough capacity.

    If you have enough SPICE capacity, choose
    **Import to SPICE for quicker
    analytics**, and then create an analysis by
    choosing **Visualize**.

    ###### Note

    If you want to use SPICE and you don't have
    enough space, choose **Edit/Preview data**.
    In data preparation, you can remove fields from the dataset
    to decrease its size. You can also apply a filter or write a
    SQL query that reduces the number of rows or columns
    returned. For more information about data preparation, see
    [Preparing dataset examples](preparing-data-sets.md "preparing-data-sets.md").
    - To create a dataset and an analysis using the table data
      as-is, and to have the data queried directly from the database,
      choose the **Directly query your data** option.
      Then create an analysis by choosing
      **Visualize**.

## Creating a dataset using a database

that's not autodiscovered

Use the following procedure to create a connection to any database other than
an autodiscovered Amazon Redshift cluster or Amazon RDS instance. Such databases include Amazon Redshift
clusters and Amazon RDS instances that are in a different AWS Region or are
associated with a different AWS account. They also include MariaDB, Microsoft
SQL Server, MySQL, Oracle, and PostgreSQL instances that are on-premises, in
Amazon EC2, or in some other accessible environment.

###### To create a connection to a database that isn't an autodiscovered

Amazon Redshift cluster or RDS instance

1. Check [Data source quotas](data-source-limits.md "data-source-limits.md") to make sure that your target
   table or query doesn't exceed data source quotas.
2. Confirm that the database credentials that you plan to use have
   appropriate permissions as described in [Required permissions](required-permissions.md "required-permissions.md").
3. Make sure that you have configured the cluster or instance for Amazon Quick Suite
   access by following the instructions in [Network and database configuration requirements](configure-access.md "configure-access.md").
4. On the Amazon Quick Suite start page, choose **Manage
   data**.
5. Choose **Create** then choose **New data
   set**.
6. Choose the **Redshift Manual connect** icon if you
   want to connect to an Amazon Redshift cluster in another AWS Region or associated
   with a different AWS account. Or choose the appropriate database
   management system icon to connect to an instance of Amazon Aurora, MariaDB,
   Microsoft SQL Server, MySQL, Oracle, or PostgreSQL.
7. Enter the connection information for the data source, as
   follows:
   - For **Data source name**, enter a name for
     the data source.
   - For **Database server**, enter one of the
     following values:
     - For an Amazon Redshift cluster or Amazon RDS instance, enter the
       endpoint of the cluster or instance without the port
       number. For example, if the endpoint value is
       `clustername.1234abcd.us-west-2.redshift.amazonaws.com:1234`,
       then enter
       `clustername.1234abcd.us-west-2.redshift.amazonaws.com`.
       You can get the endpoint value from the
       **Endpoint** field on the cluster
       or instance detail page in the AWS console.
     - For an Amazon EC2 instance of MariaDB, Microsoft SQL
       Server, MySQL, Oracle, or PostgreSQL, enter the public
       DNS address. You can get the public DNS value from the
       **Public DNS** field on the
       instance detail pane in the Amazon EC2 console.
     - For a non-Amazon EC2 instance of MariaDB, Microsoft SQL
       Server, MySQL, Oracle, or PostgreSQL, enter the hostname
       or public IP address of the database server. If you are
       using Secure Sockets Layer (SSL) for a secured
       connection (recommended), you likely need to provide the
       hostname to match the information required by the SSL
       certificate. For a list of accepted certificates see
       [Amazon Quick Suite SSL and CA certificates](configure-access.md#ca-certificates "configure-access.md#ca-certificates").

   - For **Port**, enter the port that the cluster
     or instance uses for connections.
   - For **Database name**, enter the name of the
     database that you want to use.
   - For **UserName**, enter the user name of a
     user account that has permissions to do the following:
     - Access the target database.
     - Read (perform a `SELECT` statement on) any
       tables in that database that you want to use.

   - For **Password**, enter the password
     associated with the account you entered.

8. (Optional) If you are connecting to anything other than an Amazon Redshift
   cluster and you _don't_ want a secured connection,
   make sure that **Enable SSL** is clear. _We
   strongly recommend leaving this checked_, because an
   unsecured connection can be open to tampering.

For more information on how the target instance uses SSL to secure
connections, see the documentation for the target database management
system. Amazon Quick Suite doesn't accept self-signed SSL certificates as valid. For
a list of accepted certificates, see [Amazon Quick Suite SSL and CA certificates](configure-access.md#ca-certificates "configure-access.md#ca-certificates").

Amazon Quick Suite automatically secures connections to Amazon Redshift clusters by using SSL.
You don't need to do anything to enable this.

Some databases, such as Presto and Apache Spark, must meet additional
requirements before Amazon Quick Suite can connect. For more information, see [Creating a data source using
Presto](create-a-data-source-presto.md "create-a-data-source-presto.md"), or [Creating a data source using Apache
Spark](create-a-data-source-spark.md "create-a-data-source-spark.md"). 9. (Optional) Choose **Validate connection** to verify
your connection information is correct. 10. If the connection validates, choose **Create data
source**. If not, correct the connection information and
try validating again. 11. Choose one of the following:

    * **Custom SQL**


    On the next screen, you can choose to write a query with the
     **Use custom SQL** option. Doing this opens
     a screen named **Enter custom SQL query**,
     where you can enter a name for your query, and then enter the
     SQL. For best results, compose the query in a SQL editor, and
     then paste it into this window. After you name and enter the
     query, you can choose **Edit/Preview data** or
     **Confirm query**. Choose
     **Edit/Preview data** to immediately go to
     data preparation. Choose **Confirm query** to
     validate the SQL and make sure that there are no errors.
    * **Choose tables**


    To connect to specific tables, for **Schema: contain
     sets of tables**, choose
     **Select** and then choose a schema. In
     some cases where there is only a single schema in the database,
     that schema is automatically chosen, and the schema selection
     option isn't displayed.


    To prepare the data before creating an analysis, choose
     **Edit/Preview data** to open data
     preparation. Use this option if you want to join to more
     tables.


    Otherwise, after choosing a table, choose
     **Select**.

12. Choose one of the following options:
    - Prepare the data before creating an analysis. To do this,
      choose **Edit/Preview data** to open data
      preparation for the selected table. For more information about
      data preparation, see [Preparing dataset examples](preparing-data-sets.md "preparing-data-sets.md").
    - Create a dataset and an analysis using the table data as-is
      and import the dataset data into SPICE for
      improved performance (recommended). To do this, check the table
      size and the SPICE indicator to see if you have
      enough space.

    If you have enough SPICE capacity, choose
    **Import to SPICE for quicker
    analytics**, and then create an analysis by
    choosing **Visualize**.

    ###### Note

    If you want to use SPICE and you don't have
    enough space, choose **Edit/Preview data**.
    In data preparation, you can remove fields from the dataset
    to decrease its size. You can also apply a filter or write a
    SQL query that reduces the number of rows or columns
    returned. For more information about data preparation, see
    [Preparing dataset examples](preparing-data-sets.md "preparing-data-sets.md").
    - Create a dataset and an analysis using the table data as-is
      and have the data queried directly from the database. To do
      this, choose the **Directly query your data**
      option. Then create an analysis by choosing
      **Visualize**.
