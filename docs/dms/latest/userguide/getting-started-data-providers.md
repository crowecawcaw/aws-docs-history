# Configure your data providers for

DMS Schema Conversion

Next, you create data providers that describe your source and target databases. For
each data provider, you specify a data store type and location information. You don't
store your database credentials in a data provider.

###### To create a data provider for an on-premises database

1. Sign in to the AWS Management Console, and open the AWS DMS console.
2. In the navigation pane, choose **Data providers**, and then choose **Create data provider**.
3. For **Name**, enter a unique name for your source data provider. For example, enter `sc-dp`.
4. For **Purpose**, select **Schema Conversion**.
5. For **Engine type**, choose the type of database engine for your data provider.
6. Turn on **Virtual mode** if you want to use schema conversion without connecting to a target database. For more information, see [Virtual data provider](virtual-data-provider.md "virtual-data-provider.md").
7. If **Virtual Mode** is turned on, connection information will be preset automatically using defaults. Note that a virtual data provider can only be used as a target in a migration project or in schema conversion. For more information on virtual mode, see [Virtual data provider](virtual-data-provider.md "virtual-data-provider.md").

If **Virtual mode** is off, provide your connection information for the source database. The connection parameters depend on your database engine. For more information, see [Creating data providers](../../../data-providers-create.md "../../../data-providers-create.md"). 8. Select **Engine configuration**. Then select
**Enter manually**. Provide your connection information
for the source database. The connection parameters depend on your source
database engine. For more information, see [Creating data providers](../../../data-providers-create.md "../../../data-providers-create.md"). 9. For **Secure Socket Layer (SSL) mode**, choose the type of SSL enforcement. 10. Choose **Create data provider**.

###### To create a data provider for an Amazon RDS database

1. Sign in to the AWS Management Console, and open the AWS DMS console.
2. In the navigation pane, choose **Data providers**, and then choose **Create data provider**.
3. For **Name**, enter a unique name for your source data provider. For example, enter `sc-dp`.
4. For **Purpose**, select **Schema Conversion**.
5. For **Engine type**, choose the type of database engine for your data provider.
6. Turn **Virtual Mode** on, if you intend to use this data provider for schema conversion without connecting to a target database. For more information on virtual mode, see [Virtual data provider](virtual-data-provider.md "virtual-data-provider.md").
7. Select **Engine configuration**. Select **Choose RDS database instance from list**.
8. For **Database from RDS**, choose **Browse**, and choose your database. DMS Schema Conversion automatically retrieves the information about the engine type, server name, and port.
9. For **Database name**, enter the name of your database.
10. For **Secure Socket Layer (SSL) mode**, choose the type of SSL enforcement.
11. Choose **Create data provider**.
