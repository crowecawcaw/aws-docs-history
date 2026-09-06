

# Connect to Amazon DocumentDB from Tableau Desktop
<a name="connect-jdbc-tableau"></a>

**Topics**
+ [Adding the Amazon DocumentDB JDBC Driver](#connect-jdbc-tableau-adddriver)
+ [Connecting to Amazon DocumentDB using Tableau - SSH Tunnel](#connect-jdbc-tableau-ssh)

## Adding the Amazon DocumentDB JDBC Driver
<a name="connect-jdbc-tableau-adddriver"></a>

To connect to Amazon DocumentDB from Tableau Desktop you must download and install the Amazon DocumentDB JDBC driver and the DocumentDB Tableau connector.

1. Download the Amazon DocumentDB JDBC driver JAR file from the [Amazon DocumentDB JDBC Driver repository](https://github.com/aws/amazon-documentdb-jdbc-driver/releases) and copy it to one of these directories according to your operating system:
   + *Windows* - `C:\Program Files\Tableau\Drivers`
   + *MacOS* - `~/Library/Tableau/Drivers`

1. Download the DocumentDB Tableau connector (a TACO file) from the [Tableau Exchange website](https://exchange.tableau.com/products/821) and copy it to your *My Tableau Repository/Connectors directory*.
   + *Windows* - `C:\Users\[user]\Documents\My Tableau Repository\Connectors`
   + *MacOS* - `/Users/[user]/Documents/My Tableau Repository/Connectors`

For additional information, refer to the [Tableau documentation](https://tableau.github.io/connector-plugin-sdk/docs/run-taco).

**Note**  
If you are using newer CA certificates, make sure to upgrade your JDBC driver to v1.4.5 (available in this AWS [GitHub repository](https://github.com/aws/amazon-documentdb-jdbc-driver/releases/tag/v1.4.5).).

## Connecting to Amazon DocumentDB using Tableau - SSH Tunnel
<a name="connect-jdbc-tableau-ssh"></a>

To connect to Tableau from a client machine outside of the VPC of your DocumentDB cluster, you must setup an SSH tunnel before following the steps below:

1. Launch the Tableau Desktop application.

1. Navigate to **Connect** > **To A Server** > **More**. 

1.  Choose **Amazon DocumentDB by Amazon Web Services** under **Installed Connectors**.  
![The Connect interface on Tableau Desktop shows the More... submenu under the To a Server section. The Amazon DocumentDB option is highlighted in the Installed Connectors submenu.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/jdbc/tableau-choose-docdb.png)

**Connecting to Amazon DocumentDB using Tableau - external SSH tunnel**

1. Enter the required connection parameters **Hostname**, **Port**, **Database**, **Username** and **Password**. The connection parameters in the following example are equivalent to the JDBC connection string : 

   `jdbc:documentdb://localhost:27019/test? tls=true&tlsAllowInvalidHostnames=true&scanMethod=random&scanLimit=1000&loginTimeoutSec=0&readPreference=primary&retryReads=true&schemaName=_default` with the username and password parameters passed separately in a properties collection. For more information on connection string parameters, refer to the [Amazon DocumentDB JDBC Driver github documentation](https://github.com/aws/amazon-documentdb-jdbc-driver/blob/develop/src/markdown/setup/connection-string.md).   
![General tab in Amazon DocumentDB connector interface showing hostname, port, database, username, and password fields.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/jdbc/tableau-connect.png)

1. (Optional) More advanced options can be found on the **Advanced** tab.  
![Advanced tab in Amazon DocumentDB connector interface showing additional connection options.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/jdbc/tableau-advanced.png)

1. Choose **Sign in.**

**Connecting to Amazon DocumentDB using Tableau - internal SSH tunnel**
**Note**  
If you prefer to not setup the SSH tunnel using a terminal, you can use the Tableau GUI to specify your EC2 instance details which the JDBC driver will inherently use to create a SSH tunnel. 

1. On the **Advanced** tab, choose the **Enable SSH Tunnel option** to review further properties.  
![Advanced tab in Amazon DocumentDB connector interface with Enable SSH Tunnel selected and additional SSH input fields shown.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/jdbc/tableau-advanced-Enablessh.png)

1. Enter the **SSH User**, **SSH Hostname**, and **SSH Private Key File**. 

1. (Optional) You can disable the **SSH Strict Host Key Check** option which bypasses the host key check against a known hosts file.
**Note**  
Disabling this option is less secure as it can lead to a [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attack.  
![Advanced tab in Amazon DocumentDB connector interface with SSH Strict Host Key Check option disabled.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/jdbc/tableau-advanced-sshhostkeycheck.png)

1. Enter the required parameters; **Hostname**, **Port**, **Database**, **Username** and **Password**.
**Note**  
Make sure you use the DocumentDB cluster endpoint and not localhost when using the internal SSH tunnel option.  
![General tab in Amazon DocumentDB connector interface showing hostname, port, database, username, and password fields.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/jdbc/tableau-hostname.png)

1. Choose **Sign In**.