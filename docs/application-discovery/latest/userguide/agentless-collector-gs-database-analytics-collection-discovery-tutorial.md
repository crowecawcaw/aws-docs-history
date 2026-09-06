

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Discovering a database server
<a name="agentless-collector-gs-database-analytics-collection-discovery-tutorial"></a>

Complete the following set of tasks to discover and add database servers on the console.

**To start the discovery of your database servers**

1. On the **Database and analytics collector** page, choose **OS servers** under **Discovery** in the navigation pane.

1. Select the OS servers that include your database and analytics servers, then choose **Verify connection** on the **Actions** menu.

1. For servers that have the **Connectivity** status of **Failed**, edit the connection credentials.

   1. Select a single server or multiple servers when they have identical credentials, then choose **Edit** on the **Actions** menu. The **Edit OS server** page opens.

   1. For **Port**, enter the port number that is used for remote queries.

   1. For **Authentication type**, choose the authentication type that your OS server uses.

   1. For **User name**, enter the user name that you use to connect to your OS server.

   1. For **Password**, enter the password that you use to connect to your OS server.

   1. Choose **Verify connection** to make sure that you updated your OS server credentials correctly. Next, choose **Save**.

1. After you update credentials for all OS servers, select your OS servers and choose **Discover database servers**.

The database and analytics data collection module connects to your OS servers and discovers the supported database and analytics servers. After the data collection module completes the discovery, you can see the list of discovered database and analytics servers by choosing **View database servers**.

Alternatively, you can add your database and analytics servers to inventory manually. Also, you can import the list of servers from a CSV file. You can skip this step if you already added all your database and analytics servers to the inventory.

**To add a database or analytics server manually**

1. On the **Database and analytics collector** page, choose **Data collection** in the navigation pane.

1. Choose **Add database server**. The **Add database server** page opens.

1. Provide your database server credentials.

   1. For **Database engine**, choose the database engine of your server. For more information, see [Supported OS, database, and analytics servers](agentless-collector-gs-database-analytics-collection.md#agentless-collector-gs-database-analytics-collection-supported-servers). 

   1. For **Hostname / IP**, enter the hostname or IP address of your database or analytics server.

   1. For **Port**, enter the port where your server runs.

   1. For **Authentication type**, choose the authentication type that your database or analytics server uses.

   1. For **User name**, enter the user name that you use to connect to your server.

   1. For **Password**, enter the password that you use to connect to your server.

   1. Choose **Verify** to make sure that you added your database or analytics server credentials correctly.

1. (Optional) Add multiple servers from a CSV file.

   1. Choose **Bulk import database servers from CSV**.

   1. Choose **Download template** to save a CSV file that includes a template that you can customize.

   1. Enter the connection credentials for your database and analytics servers into the file according to the template. The following example shows how you can provide database or analytics server connection credentials in a CSV file.

      ```
      Database engine,Hostname/IP,Port,Authentication type,Username,Password,Oracle service name,Database,Allow public key retrieval,Use SSL,Trust server certificate
      Oracle,192.0.2.1,1521,Login/Password authentication,USER-EXAMPLE,AKIAI44QH8DHBEXAMPLE,orcl,,,,
      PostgreSQL,198.51.100.1,1533,Login/Password authentication,USER2-EXAMPLE,bPxRfiCYEXAMPLE,,postgre,,TRUE,
      MSSQL,203.0.113.1,1433,Login/Password authentication,USER3-EXAMPLE,h3yCo8nvbEXAMPLE,,,,,TRUE
      MySQL,2001:db8:4006:812:ffff:200e,8080,Login/Password authentication,USER4-EXAMPLE,APKAEIVFHP46CEXAMPLE,,mysql,TRUE,TRUE,
      ```

      Save your CSV file after you add credentials for all your database and analytics servers.

   1. Choose **Browse**, then choose your CSV file.

1. Choose **Add database server**.

1. After you add credentials for all OS servers, select your OS servers and choose **Discover database servers**.

After you add all your database and analytics servers into the data collection module, add them to the inventory. The database and analytics data collection module can connect to the servers from the inventory and collects metadata and performance metrics.

**To add your database and analytics servers to the inventory**

1. On the **Database and analytics collector** page, choose **Database servers** under **Discovery** in the navigation pane.

1. Select the database and analytics servers, for which you want to collect metadata and performance metrics.

1. Choose **Add to inventory**.

After you add all database and analytics servers to your inventory, you can start collecting metadata and performance metrics. For more information, see [Database and analytics data collection](agentless-collector-dashboard.md#using-collector-data-collect-database-analytics).