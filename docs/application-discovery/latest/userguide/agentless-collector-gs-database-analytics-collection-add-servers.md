AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Adding your LDAP and OS servers

The database and analytics data collection module uses LDAP in Microsoft Active
Directory to gather information about the OS, database, and analytics servers in your
network. _Lightweight Directory Access Protocol (LDAP)_ is an open
standard application protocol. You can use this protocol to access and maintain
distributed directory information services over your IP network.

You can add an existing LDAP server into your database and analytics data collection
module to automatically discover OS servers in your network. If you don't use LDAP, you
can add OS servers manually.

###### To add an LDAP server to your database and analytics data collection

module

1. Open the Agentless Collector console. For more information, see [Accessing the
   collector console](agentless-collector-gs-access-console.md "agentless-collector-gs-access-console.md").
2. Choose **View Database and analytics collector**, then choose
   **LDAP servers** under **Discovery** in
   the navigation pane.
3. Choose **Add LDAP server**. The **Add LDAP
   server** page opens.
4. For **Hostname**, enter the hostname of your LDAP
   server.
5. For **Port**, enter the port number that is used for LDAP
   requests.
6. For **User name**, enter the user name that you use to
   connect to your LDAP server.
7. For **Password**, enter the password that you use to connect
   to your LDAP server.
8. (Optional) Choose **Verify connection** to make sure that you
   added your LDAP server credentials correctly. Alternatively, you can verify your
   LDAP server connection credentials later, from the list on the **LDAP
   servers** page.
9. Choose **Add LDAP server**.
10. On the **LDAP servers** page, select your LDAP server from
    the list and choose **Discover OS servers**.

###### Important

For OS discovery, the data collection module needs credentials for the domain
server to run requests using the LDAP protocol.

The database and analytics data collection module connects to your LDAP server and
discovers your OS servers. After the data collection module completes the OS servers
discovery, you can see the list of discovered OS servers by choosing **View OS
servers**.

Alternatively, you can add your OS servers manually or import the list of servers from
a comma-separated values (CSV) file. Also, you can use the VMware vCenter Agentless
Collector data collection module to discover your OS servers. For more information, see
[Using the VMware data
collection module](agentless-collector-gs-data-collection-vcenter.md "agentless-collector-gs-data-collection-vcenter.md").

###### To add an OS server to your database and analytics data collection module

1. On the **Database and analytics collector** page, choose
   **OS servers** under **Discovery** in the
   navigation pane.
2. Choose **Add OS server**. The **Add OS
   server** page opens.
3. Provide your OS server credentials.
   1. For **OS type**, choose the operating system of your
      server.
   2. For **Hostname / IP**, enter the hostname or IP
      address of your OS server.
   3. For **Port**, enter the port number that is used for
      remote queries.
   4. For **Authentication type**, choose the
      authentication type that your OS server uses.
   5. For **User name**, enter the user name that you use
      to connect to your OS server.
   6. For **Password**, enter the password that you use to
      connect to your OS server.
   7. Choose **Verify** to make sure that you added your OS
      server credentials correctly.

4. (Optional) Add multiple OS servers from a CSV file.
   1. Choose **Bulk import OS servers from CSV**.
   2. Choose **Download template** to save a CSV file that
      includes a template that you can customize.
   3. Enter the connection credentials for your OS servers into the file
      according to the template. The following example shows how you can
      provide OS server connection credentials in a CSV file.

   ```
   OS type,Hostname/IP,Port,Authentication type,Username,Password
   Linux,192.0.2.0,22,Key-based authentication,USER-EXAMPLE,ANPAJ2UCCR6DPCEXAMPLE
   Windows,203.0.113.0,,NTLM,USER2-EXAMPLE,AKIAIOSFODNN7EXAMPLE
   ```

   Save your CSV file after you add credentials for all your OS
   servers. 4. Choose **Browse**, then choose your CSV file.

5. Choose **Add OS server**.
6. After you add credentials for all OS servers, select your OS servers and
   choose **Discover database servers**.
