# Connecting to your DB instance using Oracle SQL

developer

In this procedure, you connect to your DB instance by using Oracle SQL Developer. To download a standalone
version of this utility, see the [Oracle SQL developer downloads page](https://www.oracle.com/tools/downloads/sqldev-downloads.html "https://www.oracle.com/tools/downloads/sqldev-downloads.html").

To connect to your DB instance, you need its DNS name and port number. For information about finding the DNS
name and port number for a DB instance, see [Finding the endpoint of your RDS for Oracle DB instance](USER_Endpoint.md "USER_Endpoint.md").

###### To connect to a DB instance using SQL developer

1. Start Oracle SQL Developer.
2. On the **Connections** tab, choose the **add (+)** icon.

![Oracle SQL Developer with add icon highlighted](images/oracle-sqldev-plus.png) 3. In the **New/Select Database Connection** dialog box, provide the information for your
DB instance:

    * For **Connection Name**, enter a name that describes the connection, such as
     `Oracle-RDS`.
    * For **Username**, enter the name of the database administrator for the DB
     instance.
    * For **Password**, enter the password for the database administrator.
    * For **Hostname**, enter the DNS name of the DB instance.
    * For **Port**, enter the port number.
    * For **SID**, enter the DB name. You can find the DB
     name on the **Configuration** tab of your database
     details page.

The completed dialog box should look similar to the following.

![Creating a new connection in Oracle SQL Developer](images/oracle-sqldev-newcon.png) 4. Choose **Connect**. 5. You can now start creating your own databases and running queries against your DB instance and
databases as usual. To run a test query against your DB instance, do the following:

    1. In the **Worksheet** tab for your connection, enter the following SQL
     query.



    ```
    SELECT NAME FROM V$DATABASE;
    ```
    2. Choose the **execute** icon to run the query.



    ![Running a query in Oracle SQL Developer using the execute icon](images/oracle-sqldev-run.png)

    SQL Developer returns the database name.



    ![Query results in Oracle SQL Developer](images/oracle-sqldev-results.png)
