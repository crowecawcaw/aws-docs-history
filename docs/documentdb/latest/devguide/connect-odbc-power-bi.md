

# Connect to Amazon DocumentDB from Microsoft Power BI Desktop
<a name="connect-odbc-power-bi"></a>

**Topics**
+ [Prerequisites](#odbc-power-bi-prerequisites)
+ [Adding Microsoft Power BI Desktop custom connector](#odbc-adding-power-bi)
+ [Connecting using the Amazon DocumentDB custom connector](#odbc-connect-custom-connector)
+ [Configuring Microsoft Power BI Gateway](#odbc-power-bi-gw)

## Prerequisites
<a name="odbc-power-bi-prerequisites"></a>

Before beginning, ensure that the Amazon DocumentDB ODBC driver is correctly installed.

## Adding Microsoft Power BI Desktop custom connector
<a name="odbc-adding-power-bi"></a>

Copy the `AmazonDocumentDBConnector.mez` file to the `<User>\Documents\Power BI Desktop\Custom Connectors\` folder (or to `<User>\OneDrive\Documents\Power BI Desktop\Custom Connectors` if using OneDrive). This will allow Power BI to access custom connector. You can get the connector to Power BI Desktop [here](https://github.com/aws/amazon-documentdb-odbc-driver/releases). Restart Power BI Desktop to make sure the connector is loaded.

**Note**  
The custom connector only supports Amazon DocumentDB username and password for authentication.

## Connecting using the Amazon DocumentDB custom connector
<a name="odbc-connect-custom-connector"></a>

1. Select Amazon DocumentDB (Beta) from **Get Data** and choose **Connect**. If you get a warning for using a third-party service, choose **Continue**.  
![The Get Data interface with Amazon DocumentDB (Beta) option highlighted.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/get-data-1.png)

1. Enter all necessary information to connect to your Amazon DocumentDB cluster, then choose **OK**:  
![Form with connection detail input fields for an Amazon DocumentDB cluster.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/docdb-form-1.png)
**Note**  
Depending on the configuration of your ODBC driver's Data Source Name (DSN), the SSH connection details screen may not be displayed if you have already provided the necessary information within the DSN settings.

1. Choose the data connectivity mode:
   + **Import** - loads all data and stores the information on disk. The data must be refreshed and reloaded to show data updates.
   + **Direct Query** - does not load data, but does live queries on the data. This means that data does not need to be refreshed and reloaded to show data updates.  
![Interface showing Data Connectivity mode options for DocumentDB.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/data-connectivity-1.png)
**Note**  
If you are using a very large dataset, importing all of the data may take a longer period of time.

1. If this is the first time connecting to this data source, select the authentication type and input your credentials when prompted. Then choose **Connect**:  
![Authentication interface showing input fields for username and password credentials.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/docdb-credentials-1.png)

1. In the **Navigator** dialog, select the database tables you want, then either choose **Load** to load the data or **Transform Data** to continue transforming the data.  
![Navigator interface showing list of database tables to choose from. The Load and Transform Data buttons are in the bottom right.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/navigator-1.png)
**Note**  
Your data source settings are saved once you connect. To modify them, select **Transform Data** > **Data Source Settings**.

## Configuring Microsoft Power BI Gateway
<a name="odbc-power-bi-gw"></a>

**Prerequisites**:
+ Enure that the custom connector will work with Power BI Gateway.
+ Make sure that the ODBC DSN is created in the ODBC data sources in the **System** tab on the machine where Power BI Gateway is installed.

If you are using the internal SSH tunnel feature, the file `known_hosts` needs to be located where the Power BI service account has access to it.

![The known_hosts properties interface showing permissions for the PBIEgwService.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/ssh-known-hosts-1.png)


**Note**  
This also applies to any file(s) that you might need to be able to establish a connection to your Amazon DocumentDB cluster, such as a certificate authority (CA) certificate file (pem file). 