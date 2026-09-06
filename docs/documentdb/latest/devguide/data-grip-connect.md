

# Connect to Amazon DocumentDB using DataGrip
<a name="data-grip-connect"></a>

[DataGrip](https://www.jetbrains.com/help/datagrip/documentdb.html) is a powerful integrated development environment (IDE) that supports various database systems, including Amazon DocumentDB. This section walks you through the steps to connect to your Amazon DocumentDB cluster using DataGrip, allowing you to easily manage and query your data using a graphical interface.

## Prerequisites
<a name="data-grip-prerequisites"></a>
+ DataGrip IDE installed on your machine. You can download it from [JetBrains](https://www.jetbrains.com/datagrip/download/#section=windows).
+ An Amazon EC2 instance running in the same VPC as your Amazon DocumentDB cluster. You’ll use this instance to establish a secure tunnel from your local machine to the Amazon DocumentDBcluster. Follow the instructions on how to [Connect using Amazon EC2](connect-ec2.md).
+ Alternative to an Amazon EC2 instance, a VPN connection, or if you are already accessing your AWS infrastructure using a secure VPN. If you prefer this option, follow the instructions to [securely access Amazon DocumentDB using AWS Client VPN](https://aws.amazon.com/blogs/database/securely-access-amazon-documentdb-with-mongodb-compatibility-locally-using-aws-client-vpn/).

## Connect using DataGrip
<a name="data-grip-connect-steps"></a>

1. Launch DataGrip on your computer and create a **New Project**.  
![DataGrip welcome screen with New Project option highlighted.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/welcome.png)

1. Add a new data source using one of the following ways:

   1. From the main menu, navigate to **File – New – Data Source** and select **DocumentDB**

   1. In the **Database Explorer**, choose the new icon (**\+**) in the toolbar. Navigate to **Data Source** and select **DocumentDB**.  
![The dropdown list for + shows the Data Source submenu. DocumentDB is selected from that submenu.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/explorer.png)

1. On the **Data Sources** page in the **General** tab, check if there is a **Download missing driver files** link at the bottom of the connection settings area. Choose this link to download drivers that are required to interact with a database. For a direct download link, refer to [JetBrains JDBC drivers](https://www.jetbrains.com/datagrip/jdbc-drivers/).  
![Data Sources and Drivers interface with Download missing driver files link highlighted.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/missing-driver.png)

1. In the **General** tab, specify the connection details:

   1. In the **Host** field, specify the Amazon DocumentDB cluster endpoint.

   1. **Port** is already set to 27017. Change it if your cluster was deployed on a different port.

   1. For **Authentication**, choose **User & Password**.

   1. Enter your user name and password information.

   1. The **Database** field is optional. You can specify the database to which you want to connect.

   1. The **URL** field auto-completes as you add the preceding details.  
![Host, port, authentication, database, and URL fields in the General tab on the Data Sources and Drivers interface.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/connection.png)

1. In the **SSH/SSL** tab, enable **Use SSH tunnel**, then choose the icon to open the **SSH Configuration** dialog. Enter the following information:

   1. in the **Host** field, enter the hostname of your Amazon EC2 instance.

   1. Enter the username and password for your Amazon EC2 instance.

   1. For **Authentication type**, choose **Key pair**.

   1. Enter your **Private key file**.
**Note**  
If you’re using the VPN option, there is no need to configure the SSH tunnel.  
![The SSH/SSL tab in the Data Sources and Drivers interface with Use SSH tunnel selected and the SSH configuration icon highlighted. The icon opens the displayed SSH Configurations interface.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/ssh-tunnel.png)

1. In the **SSH/SSL** tab, enable **Use SSL**. In the **CA file** field, enter the location to the `global-bundle.pem` file on your computer. For **Mode**, leave the option **Require**.
**Note**  
You can download the certificate from this location or with this command: wget [https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem](https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem)
**Note**  
If you are connecting to Amazon DocumentDB elastic cluster, you don’t have to specify the CA file. Leave the **Use SSL** option checked and all the other options at their default values.  
![SSH/SSL tab in the Data Sources and Drivers interface with SSL settings enabled.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/use-ssl.png)

1. In the **Schemas** tab, choose **All databases** or enter the filter “\*:\*” in the **Schema pattern** field. Choose **Test Connection** to test the connection.  
![The Schemas tab in the Data Sources and Drivers interface with the All databases option selected. A Succeeded message appears above the Test Connection link.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/schemas.png)

1. Once the connection is successfully tested, choose **OK** to save the data source configuration.

## DataGrip features
<a name="data-grip-features"></a>

DataGrip provides various features to help you work with Amazon DocumentDB efficiently:
+ **SQL Editor** — Write and execute SQL-like queries on your DocumentDB collections using the SQL editor in DataGrip.
+ **Visual Query Builder** — Use the visual query builder to create queries graphically without writing SQL code.
+ **Schema Management** — Easily manage your database schema, including creating, altering, and dropping collections.
+ **Data Visualization** — View and analyze your data using various visualization tools available in DataGrip.
+ **Export and Import Data** — Transfer data between Amazon DocumentDB and other databases using DataGrip's export and import features.

Refer to the official [DataGrip documentation](https://www.jetbrains.com/datagrip/features/) for more advanced features and tips on working with Amazon DocumentDB and other database systems.