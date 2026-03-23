# Adding servers to project in AWS SCT

You can add multiple source and target database servers to an AWS Schema Conversion Tool project.

###### To add a server to your project

1. Start the AWS Schema Conversion Tool.
2. Create a new project or open an existing project.
3. Choose **Add source**
   from the menu to add a new source database.
4. Choose a database platform and specify database connection credentials.
   For more information on connecting to a source database, see [Connecting to source databases with the AWS Schema Conversion Tool](CHAP_Source.md "CHAP_Source.md").
   Use the following procedure to connect to your database.

###### To connect to your database

1. Open the context (right-click) menu for a database server, and then choose
   **Establish connection**.

You can also choose **Connect to the server** at the
top of your database schema tree. 2. Enter the password to connect to your source database server. 3. Choose **Test connection** to verify
that AWS SCT can connect to your source database. 4. Choose **Connect** to connect to your source database.
Use the following procedure to remove a database server from your AWS SCT project.

###### To remove a database server

1. Choose the database server to remove.
2. Open the context (right-click) menu, and then choose
   **Remove from project**.

AWS SCT removes the selected database server, all mapping rules, conversion
results, and other metadata related to this server.
