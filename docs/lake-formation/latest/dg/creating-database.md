# Creating a database

Metadata tables in the Data Catalog are stored within databases. You can create as many databases
as you need, and you can grant different Lake Formation permissions on each database.

Databases can have an optional location property. This location is typically within an
Amazon Simple Storage Service (Amazon S3) location that is registered with Lake Formation. When you specify a location, principals
do not need data location permissions to create Data Catalog tables that point to locations within
the database location. For more information, see [Underlying data access control](access-control-underlying-data.md#data-location-permissions "access-control-underlying-data.md#data-location-permissions").

To create a database using the Lake Formation console, you must be signed in as a data lake
administrator or _database creator_. A database creator is a
principal who has been granted the Lake Formation `CREATE_DATABASE` permission. You can see a
list of database creators on the **Administrative roles and tasks** page of the
Lake Formation console. To view this list, you must have the `lakeformation:ListPermissions`
IAM permission and be signed in as a data lake administrator or as a database creator with the
grant option on the `CREATE_DATABASE` permission.

###### To create a database

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"), and sign in as a data lake
   administrator or database creator.
2. In the navigation pane, under **Data catalog**, choose
   **Databases**.
3. Choose **Create database**.
4. In the **Create database** dialog box, enter a database name, optional
   location, and optional description.
5. Optionally select **Use only IAM access control for new tables in this
   database**.

For information about this option, see [Changing the default settings for your data
lake](change-settings.md "change-settings.md"). 6. Choose **Create database**.
