# Connecting to your Amazon RDS for Db2 DB instance with IBM Db2 Data Management Console

You can connect to your Amazon RDS for Db2 DB instance with IBM Db2 Data Management Console. IBM Db2 Data Management Console can administer and
monitor several RDS for Db2 DB instances.

###### Note

You must have an Amazon EC2 Linux or Windows machine that is on the same VPC and security
group as your RDS for Db2 DB instance. The VPC and security group controls the connection
to your DB instance through the internal network.

IBM Db2 Data Management Console requires a repository Db2 database to store metadata and performance metrics but
can't automatically create a repository database for RDS for Db2. Instead, you must first
create a repository database to monitor one or more RDS for Db2 DB instances. Then you can
install IBM Db2 Data Management Console and connect to your RDS for Db2 DB instance with IBM Db2 Data Management Console.

###### Topics

- [Step 1: Creating a repository database to monitor DB instances](#db2-creating-repo-db-monitoring-dmc "#db2-creating-repo-db-monitoring-dmc")
- [Step 2: Installing and setting up IBM Db2 Data Management Console](#db2-install-setup-dmc "#db2-install-setup-dmc")
- [Step 3: Configuring the repository database and connecting to RDS for Db2 DB instances](#db2-connecting-db-instances-with-dmc "#db2-connecting-db-instances-with-dmc")
- [Using IBM Db2 Data Management Console](#db2-using-dmc "#db2-using-dmc")

## Step 1: Creating a repository database to monitor DB instances

You can use an existing properly sized RDS for Db2 DB instance as a repository for IBM Db2 Data Management Console
to monitor other RDS for Db2 DB instances. However, because the admin user doesn't have
`SYSCTRL` authority to create buffer pools and tablespaces, using IBM Db2 Data Management Console
repository creation to create a repository database fails. Instead, you must create a
repository database. This repository database monitors your RDS for Db2 DB instances.

You can create a repository database in two different ways. You can create an RDS for Db2
database and then manually create a buffer pool, a user tablespace, and a system
temporary tablespace. Or, you can create a separate Amazon EC2 instance to host an IBM Db2 Data Management Console
repository database.

###### Topics

- [Manually creating a buffer pool, a user tablespace, and a system temporary tablespace](#db2-manually-creating-dmc "#db2-manually-creating-dmc")
- [Creating an Amazon EC2 instance to host an IBM Db2 Data Management Console repository](#db2-creating-ec2-dmc "#db2-creating-ec2-dmc")

### Manually creating a buffer pool, a user tablespace, and a system temporary tablespace

###### To create a buffer pool, a user tablespace, and a system temporary tablespace

1. Connect to the `rdsadmin` database. In the following example,
   replace `master_username` and
   `master_password` with your own
   information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Create a buffer pool for IBM Db2 Data Management Console. In the following example, replace
   `database_name` with the name of the repository
   you created for IBM Db2 Data Management Console to monitor your RDS for Db2 DB instances.

```
db2 "call rdsadmin.create_bufferpool('`database_name`',
     'BP4CONSOLE', 1000, 'Y', 'Y', 32768)"
```

3. Create a user tablespace for IBM Db2 Data Management Console. In the following example, replace
   `database_name` with the name of the repository
   you created for IBM Db2 Data Management Console to monitor your RDS for Db2 DB instances.

```
db2 "call rdsadmin.create_tablespace('`database_name`',
     'TS4CONSOLE', 'BP4CONSOLE', 32768)"
```

4. Create a system temporary tablespace for IBM Db2 Data Management Console. In the following example,
   replace `database_name` with the name of the
   repository you created for IBM Db2 Data Management Console to monitor your RDS for Db2 DB instances.

```
db2 "call rdsadmin.create_tablespace('`database_name`',
    'TS4CONSOLE_TEMP', 'BP4CONSOLE', 32768, 0, 0, 'S')"
```

You are now ready to install IBM Db2 Data Management Console. For more information about installation and
setup, see [Step 2: Installing and setting up IBM Db2 Data Management Console](#db2-install-setup-dmc "#db2-install-setup-dmc").

### Creating an Amazon EC2 instance to host an IBM Db2 Data Management Console repository

You can create a separate Amazon Elastic Compute Cloud (Amazon EC2) instance to host an IBM Db2 Data Management Console repository.
For information about creating an Amazon EC2 instance, see [Tutorial: Get started with Amazon EC2 Linux instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the
_Amazon EC2 User Guide_.

## Step 2: Installing and setting up IBM Db2 Data Management Console

After you create a buffer pool, a user tablespace, and a system temporary tablespace,
you are ready to install and set up IBM Db2 Data Management Console.

###### Important

You must have an Amazon EC2 Linux or Windows machine that is on the same VPC and
security group as your RDS for Db2 DB instance. The VPC and security group controls the
connection to your DB instance through the internal network. Also, you must have
already [created a repository
database](#db2-creating-repo-db-monitoring-dmc "#db2-creating-repo-db-monitoring-dmc") for IBM Db2 Data Management Console.

###### To install and set up IBM Db2 Data Management Console

1. Download IBM Db2 Data Management Console from [IBM Db2 Data Management Console Version 3.1x releases](https://www.ibm.com/support/pages/ibm-db2-data-management-console-version-31x-releases-new-features-and-enhancements "https://www.ibm.com/support/pages/ibm-db2-data-management-console-version-31x-releases-new-features-and-enhancements") on the IBM Support website.
2. Install IBM Db2 Data Management Console.
3. Open IBM Db2 Data Management Console and use the IP address of your Amazon EC2 machine and the port number
   you used for the HTTP or HTTPS connection to your Amazon EC2 instance. For example,
   use `http://`xx.xx.xx.xx`:11080` or
   `https://`xx.xx.xx.xx`.11081`.
   Replace `xx.xx.xx.xx` with the IP address
   of your Amazon EC2 machine. `11080` and `11081` are the default
   ports for HTTP and HTTPS connections.
4. (Optional) If you want to use port 80 or 443 on your Amazon EC2 instance, you can
   use either Apache httpd or a Nginx HTTP server to proxy the IBM Db2 Data Management Console port to either
   port 80 or 443. For more information, see [Apache HTTP Server Project](https://httpd.apache.org "https://httpd.apache.org") and [the nginx website](https://nginx.org/en/ "https://nginx.org/en/").

To allow connection to IBM Db2 Data Management Console, you must edit the inbound rules in your security
group. If you use a proxy, change the TCP/IP port 80 or 443 to redirect to the
IBM Db2 Data Management Console ports. If you aren't using a proxy, change the TCP/IP port 80 or 443 to
the default ports 11080 (HTTP) or 11081 (HTTPS).

You are now ready to log in to IBM Db2 Data Management Console to configure the repository database and to
connect to your RDS for Db2 DB instances. For more information, see [Configuring the
repository database and connecting to DB instances](#db2-connecting-db-instances-with-dmc "#db2-connecting-db-instances-with-dmc").

## Step 3: Configuring the repository database and connecting to RDS for Db2 DB instances

When you connect to the repository database for the first time, IBM Db2 Data Management Console automatically
configures the repository. After the repository database is configured, you can add
database connections to IBM Db2 Data Management Console.

To connect to your RDS for Db2 DB instance, you need its DNS name and port number. For
information about finding them, see [Finding the endpoint](db2-finding-instance-endpoint.md "db2-finding-instance-endpoint.md"). You also need to know the
database name, master username, and master password that you defined when you created
your RDS for Db2 DB instance. For more information about finding them, see [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating"). If you are connecting over the
internet, allow traffic to the database port. For more information, see [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").

###### To connect to RDS for Db2 DB instances with IBM Db2 Data Management Console

1.  Log in to IBM Db2 Data Management Console with the credentials you set during installation.
2.  Configure the repository.
    1. In the **Connection and database** section, enter the
       following information for your RDS for Db2 DB instance:
       - For **Host**, enter the DNS name of the DB
         instance.
       - For **Port**, enter the port number for the
         DB instance.
       - For **Database**, enter the name of the
         database.

    ![The Connection and database section in IBM Db2 Data Management Console with Host, Port, and Database fields.](images/ibm-dmc-connection-database.png) 2. In the **Security and credential** section, enter the
    following information for your RDS for Db2 DB instance:

        * For **Security type**, choose
         **Encrypted user and password**.
        * For **Username**, enter the name of the
         database administrator for the DB instance.
        * For **Password**, enter the password of the
         database administrator for the DB instance.

    3. Choose **Test connection**.

    ###### Note

    If the connection is unsuccessful, confirm that the database port
    is open through the inbound rules in your security group. For more
    information, see [Considerations for security groups with Amazon RDS for Db2](db2-security-groups-considerations.md "db2-security-groups-considerations.md").

    If you didn't [manually
    create a buffer pool, a user tablespace, and a system temporary
    tablespace](#db2-manually-creating-dmc "#db2-manually-creating-dmc") in RDS for Db2, you might see the following error
    message:

    ![Error message about not having permissions to perform operations.](images/ibm-dmc-error-message.png)

    Make sure that you created a buffer table, a tablespace, and objects
    for an IBM Db2 Data Management Console repository to monitor your RDS for Db2 DB instance. Or, you
    can use an Amazon EC2 Db2 DB instance to host an IBM Db2 Data Management Console repository to monitor
    your RDS for Db2 DB instance. For more information, see [Step 1: Creating a repository database to monitor DB instances](#db2-creating-repo-db-monitoring-dmc "#db2-creating-repo-db-monitoring-dmc"). 4. After you successfully test your connection, choose
    **Next**.

    ![The Security and credential section in IBM Db2 Data Management Console.](images/ibm-dmc-security-credential.png)If IBM Db2 Data Management Console finds the buffer pool, the user tablespace, and the system temporary
    tablespace in the RDS for Db2 DB instance, then IBM Db2 Data Management Console automatically configures the
    repository database. If you use your Db2 instance on your Amazon EC2 instance as the
    repository database, then IBM Db2 Data Management Console automatically creates the buffer pool and other
    objects.

3.  In the **Set statistics event monitor opt-in** window, choose
    **Next**.
4.  (Optional) Add new connection. If you want to use a different RDS for Db2 DB
    instance for administration and monitoring, then add a connection to a
    non-repository RDS for Db2 DB instance.

        1. In the **Connection and database** section, enter the
         following information for the RDS for Db2 DB instance to use for
         administration and monitoring:




        	* For **Connection name**, enter the Db2
        	 database identifier.
        	* For **Host**, enter the DNS name of the DB
        	 instance.
        	* For **Port**, enter the port number for the
        	 DB instance.
        	* For **Database**, enter the name of the
        	 database.

        ![The Connection and database section for a new connection in IBM Db2 Data Management Console with Host, Port, and Database fields.](images/ibm-dmc-new-connection-database.png)
        2. In the **Security and credential**section, select **Enable monitoring
         data collection**.
        3. Enter the following information for your RDS for Db2 DB instance:




        	* For **Username**, enter the name of the
        	 database administrator for the DB instance.
        	* For **Password**, enter the password of the
        	 database administrator for the DB instance.
        4. Choose **Test connection**.
        5. After you successfully test your connection, choose
         **Save**.

    ![The Security and credential section for a new connection in IBM Db2 Data Management Console.](images/ibm-dmc-new-security-credential.png)

After the connection is added, a window similar to the following appears. This
window indicates that your database was successfully configured.

![The window indicating that the database was successfully configured in IBM Db2 Data Management Console.](images/ibm-dmc-configuration-success.png) 5. Choose **Go to Databases**. A Databases window similar to the
following appears. This window is a dashboard that shows metrics, statuses, and
connections.

![The Databases overview window in IBM Db2 Data Management Console.](images/ibm-dmc-database-view.png)

You can now start using IBM Db2 Data Management Console.

## Using IBM Db2 Data Management Console

You can use IBM Db2 Data Management Console to do the following types of tasks:

- Manage multiple RDS for Db2 DB instances.
- Run SQL commands.
- Explore, create, or change data and database objects.
- Create `EXPLAIN PLAN` statements in SQL.
- Tune queries.

###### To run SQL commands and view the results

1. In the left navigation bar, choose **SQL**.
2. Enter a SQL command.
3. Choose **Run all**.
4. To view the results, choose the **Results** tab.

![The Database window showing how to run a SQL command and view the results in IBM Db2 Data Management Console.](images/ibm-dmc-sql-run-example.png)
