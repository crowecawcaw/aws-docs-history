AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Discovering a database server

Complete the following set of tasks to discover and add database servers on the
console.

###### To start the discovery of your database servers

1. On the **Database and analytics collector** page, choose
   **OS servers** under **Discovery** in
   the navigation pane.
2. Select the OS servers that include your database and analytics servers,
   then choose **Verify connection** on the
   **Actions** menu.
3. For servers that have the **Connectivity** status of
   **Failed**, edit the connection credentials.
   1. Select a single server or multiple servers when they have
      identical credentials, then choose **Edit** on the
      **Actions** menu. The **Edit OS
      server** page opens.
   2. For **Port**, enter the port number that is used
      for remote queries.
   3. For **Authentication type**, choose the
      authentication type that your OS server uses.
   4. For **User name**, enter the user name that you
      use to connect to your OS server.
   5. For **Password**, enter the password that you use
      to connect to your OS server.
   6. Choose **Verify connection** to make sure that
      you updated your OS server credentials correctly. Next, choose
      **Save**.

4. After you update credentials for all OS servers, select your OS servers
   and choose **Discover database servers**.
   The database and analytics data collection module connects to your OS servers and
   discovers the supported database and analytics servers. After the data collection
   module completes the discovery, you can see the list of discovered database and
   analytics servers by choosing **View database servers**.

Alternatively, you can add your database and analytics servers to inventory
manually. Also, you can import the list of servers from a CSV file. You can skip
this step if you already added all your database and analytics servers to the
inventory.

###### To add a database or analytics server manually

1. On the **Database and analytics collector** page, choose
   **Data collection** in the navigation pane.
2. Choose **Add database server**. The **Add
   database server** page opens.
3. Provide your database server credentials.
   1. For **Database engine**, choose the database
      engine of your server. For more information, see [Supported OS, database, and analytics servers](agentless-collector-gs-database-analytics-collection.md#agentless-collector-gs-database-analytics-collection-supported-servers "agentless-collector-gs-database-analytics-collection.md#agentless-collector-gs-database-analytics-collection-supported-servers").
   2. For **Hostname / IP**, enter the hostname or IP
      address of your database or analytics server.
   3. For **Port**, enter the port where your server
      runs.
   4. For **Authentication type**, choose the
      authentication type that your database or analytics server
      uses.
   5. For **User name**, enter the user name that you
      use to connect to your server.
   6. For **Password**, enter the password that you use
      to connect to your server.
   7. Choose **Verify** to make sure that you added
      your database or analytics server credentials correctly.

4. (Optional) Add multiple servers from a CSV file.
   1. Choose **Bulk import database servers from
      CSV**.
   2. Choose **Download template** to save a CSV file
      that includes a template that you can customize.
   3. Enter the connection credentials for your database and analytics
      servers into the file according to the template. The following
      example shows how you can provide database or analytics server
      connection credentials in a CSV file.

   ```
   Database engine,Hostname/IP,Port,Authentication type,Username,Password,Oracle service name,Database,Allow public key retrieval,Use SSL,Trust server certificate
   Oracle,192.0.2.1,1521,Login/Password authentication,USER-EXAMPLE,AKIAI44QH8DHBEXAMPLE,orcl,,,,
   PostgreSQL,198.51.100.1,1533,Login/Password authentication,USER2-EXAMPLE,bPxRfiCYEXAMPLE,,postgre,,TRUE,
   MSSQL,203.0.113.1,1433,Login/Password authentication,USER3-EXAMPLE,h3yCo8nvbEXAMPLE,,,,,TRUE
   MySQL,2001:db8:4006:812:ffff:200e,8080,Login/Password authentication,USER4-EXAMPLE,APKAEIVFHP46CEXAMPLE,,mysql,TRUE,TRUE,
   ```

   Save your CSV file after you add credentials for all your database
   and analytics servers. 4. Choose **Browse**, then choose your CSV
   file.

5. Choose **Add database server**.
6. After you add credentials for all OS servers, select your OS servers and
   choose **Discover database servers**.
   After you add all your database and analytics servers into the data collection
   module, add them to the inventory. The database and analytics data collection module
   can connect to the servers from the inventory and collects metadata and performance
   metrics.

###### To add your database and analytics servers to the inventory

1. On the **Database and analytics collector** page, choose
   **Database servers** under
   **Discovery** in the navigation pane.
2. Select the database and analytics servers, for which you want to collect
   metadata and performance metrics.
3. Choose **Add to inventory**.
   After you add all database and analytics servers to your inventory, you can start
   collecting metadata and performance metrics. For more information, see [Database and
   analytics data collection](agentless-collector-dashboard.md#using-collector-data-collect-database-analytics "agentless-collector-dashboard.md#using-collector-data-collect-database-analytics").
