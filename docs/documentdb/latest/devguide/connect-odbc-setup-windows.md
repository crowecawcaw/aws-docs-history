# Setting up the Amazon DocumentDB ODBC driver in Windows

Use the following procedure to set up the Amazon DocumentDB ODBC driver in Windows:

1. Open **Control Panel** in Windows and search for ODBC (or in the menu, select **Windows Tools** > **ODBC Data Sources (32-bit)** or **ODBC Data Sources (64-bit)**):

![Windows Control Panel interface showing setup links for ODBC 32-bit and 64-bit data sources.](images/odbc-control-panel-1.png) 2. Select the appropriate ODBC Driver Data Source Administrator: opt for the 32-bit version if it is installed, otherwise, choose the 64-bit version. 3. Select the Sytem DSN tab and then click **Add...** to add a new DSN:

![ODBC Data Source Administrator interface showing Add button.](images/odbc-add-dsn-1.png) 4. Choose **Amazon DocumentDB** from the data source driver list:

![The Create New Data Source interface with the Amazon DocumentDB driver option selected.](images/create-data-source-1.png) 5. In the **Configure Amazon DocumentDB DSN** dialog, complete the **Connection Settings**, **TLS** tab, and **Test Connection** fields, then click **Save**:

![The Configure Amazon DocumentDB DSN interface with Connection Settings, TLS, and Test Connection fields. The Save button is on the bottom.](images/config-docdb-dsn-1.png) 6. Ensure you complete the Windows form accurately, as connection details will differ depending on your chosen SSH tunneling method to the EC2 instance.
See SSH tunneling methods [here](https://github.com/aws/amazon-documentdb-odbc-driver/blob/develop/src/markdown/setup/setup.md#using-an-ssh-tunnel-to-connect-to-amazon-documentdb "https://github.com/aws/amazon-documentdb-odbc-driver/blob/develop/src/markdown/setup/setup.md#using-an-ssh-tunnel-to-connect-to-amazon-documentdb").
See [Connection String Syntax and Options](https://github.com/aws/amazon-documentdb-odbc-driver/blob/develop/src/markdown/setup/connection-string.md "https://github.com/aws/amazon-documentdb-odbc-driver/blob/develop/src/markdown/setup/connection-string.md") for more information about each property.

![The Configure Amazon DocumentDB DSN interface with SSH Tunnel fields completed.](images/config-docdb-dsn-ssh-1.png)
For more information about configuring the Amazon DocumentDB ODBC Driver on Windows, click [here](https://github.com/aws/amazon-documentdb-odbc-driver/blob/develop/src/markdown/setup/windows-dsn-configuration.md "https://github.com/aws/amazon-documentdb-odbc-driver/blob/develop/src/markdown/setup/windows-dsn-configuration.md").
