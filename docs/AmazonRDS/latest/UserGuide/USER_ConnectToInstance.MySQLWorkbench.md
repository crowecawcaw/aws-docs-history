

# Connecting from MySQL Workbench
<a name="USER_ConnectToInstance.MySQLWorkbench"></a>

**To connect from MySQL Workbench**

1. Download and install MySQL Workbench at [Download MySQL Workbench](http://dev.mysql.com/downloads/workbench/).

1. Open MySQL Workbench.  
![The Welcome screen in MySQL Workbench.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/mysql-workbench-main.png)

1. From **Database**, choose **Manage Connections**.

1. In the **Manage Server Connections** window, choose **New**.

1. In the **Connect to Database** window, enter the following information:
   + **Stored Connection** – Enter a name for the connection, such as **MyDB**.
   + **Hostname** – Enter the DB instance endpoint.
   + **Port** – Enter the port used by the DB instance.
   + **Username** – Enter the user name of a valid database user, such as the master user.
   + **Password** – Optionally, choose **Store in Vault** and then enter and save the password for the user.

   The window looks similar to the following:  
![The Manage Server Connections window in MySQL Workbench.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/mysql-workbench-connect.png)

   You can use the features of MySQL Workbench to customize connections. For example, you can use the **SSL** tab to configure SSL/TLS connections. For information about using MySQL Workbench, see the [MySQL Workbench documentation](https://dev.mysql.com/doc/workbench/en/). Encrypting client connections to MySQL DB instances with SSL/TLS, see [Encrypting client connections with SSL/TLS to MySQL DB instances on Amazon RDS](mysql-ssl-connections.md).

1. Optionally, choose **Test Connection** to confirm that the connection to the DB instance is successful.

1. Choose **Close**.

1. From **Database**, choose **Connect to Database**.

1. From **Stored Connection**, choose your connection.

1. Choose **OK**.