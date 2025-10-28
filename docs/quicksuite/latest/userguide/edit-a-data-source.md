# Editing a data source

You can edit an existing database data source to update the connection
information, such as the server name or the user credentials. You can also edit an
existing Amazon Athena data source to update the data source name. You can't edit Amazon S3
or Salesforce data sources.

## Editing a database data

source

Use the following procedure to edit a database data source.

1. From the Quick Suite start page, choose
   **Data** at left. Choose
   **Create** and then choose **New
   dataset**.
2. Choose a database data source.
3. Choose **Edit Data Source**.
4. Modify the data source information:
   - If you are editing an autodiscovered database data source, you
     can modify any of the following settings:
     - For **Data source name**, enter a
       name for the data source.
     - For **Instance ID**, choose the name
       of the instance or cluster that you want to connect to
       from the list provided.
     - **Database name** shows the default
       database for the **Instance ID**
       cluster or instance. If you want to use a different
       database on that cluster or instance, enter its
       name.
     - For **UserName**, enter the user name
       of a user account that has permissions to do the
       following:
       - Access the target database.
       - Read (perform a `SELECT` statement
         on) any tables in that database that you want to
         use.

     - For **Password**, enter the password
       for the account that you entered.

   - If you are editing an external database data source, you can
     modify any of the following settings:
     - For **Data source name**, enter a
       name for the data source.
     - For **Database server**, enter one of
       the following values:
       - For an Amazon Redshift cluster, enter the endpoint of the
         cluster without the port number. For example, if
         the endpoint value is
         `clustername.1234abcd.us-west-2.redshift.amazonaws.com:1234`,
         then enter
         `clustername.1234abcd.us-west-2.redshift.amazonaws.com`.
         You can get the endpoint value from the
         **Endpoint** field on the cluster
         detail page on the Amazon Redshift console.
       - For an Amazon EC2 instance of PostgreSQL, MySQL, or
         SQL Server, enter the public DNS address. You can
         get the public DNS value from the **Public
         DNS** field on the instance detail pane
         in the EC2 console.
       - For a non–Amazon EC2 instance of PostgreSQL,
         MySQL, or SQL Server, enter the hostname or public
         IP address of the database server.

     - For **Port**, enter the port that the
       cluster or instance uses for connections.
     - For **Database name**, enter the name
       of the database that you want to use.
     - For **UserName**, enter the user name
       of a user account that has permissions to do the
       following:
       - Access the target database.
       - Read (perform a `SELECT` statement
         on) any tables in that database that you want to
         use.

     - For **Password**, enter the password
       for the account that you entered.

5. Choose **Validate connection**.
6. If the connection validates, choose **Update data
   source**. If not, correct the connection information and
   try validating again.
7. If you want to create a new dataset using the updated data source,
   proceed with the instructions at [Creating a dataset from a
   database](create-a-database-data-set.md "create-a-database-data-set.md"). Otherwise, close the
   **Choose your table** dialog box.

## Editing an Athena data

source

Use the following procedure to edit an Athena data source.

1. From the Quick Suite start page, choose
   **Data** at left. Choose
   **Create** and then choose **New
   dataset**.
2. Choose an Athena data source.
3. Choose **Edit Data Source**.
4. For **Data source name**, enter a new name.
5. The **Manage data source sharing** screen appears. On
   the **Users** tab, locate the user that you want to
   remove.
6. If you want to create a new dataset using the updated data source,
   proceed with the instructions at [Creating a dataset using Amazon Athena
   data](create-a-data-set-athena.md "create-a-data-set-athena.md"). Otherwise, close the
   **Choose your table** dialog box.
