# Using offline mode in AWS Schema Conversion Tool

You can run AWS Schema Conversion Tool in an offline mode. Following, you can learn how to work with
an existing AWS SCT project when disconnected from your source database.

AWS SCT doesn't require a connection to your source database to run the following operations:

- Add mapping rules.
- Create database migration assessment reports.
- Convert database schemas and code.
- Edit your source and converted code.
- Save your source and converted code as SQL scripts in a text file.
  Before you use AWS SCT in an offline mode, connect to your source database, load
  metadata, and save your project. Open this project or disconnect from the source
  database server to use AWS SCT in an offline mode.

###### To run AWS SCT in an offline mode

1. Start the AWS Schema Conversion Tool and create a new project. For more information, see [Starting and managing Projects in AWS SCT](CHAP_UserInterface.md "CHAP_UserInterface.md").
2. Add a source database server and connect to your source database. For more information,
   see [Adding servers to project in AWS SCT](CHAP_UserInterface.md "CHAP_UserInterface.md").
3. Add a target database server or use a virtual target database platform. For more information,
   see [Mapping to virtual targets in the AWS Schema Conversion Tool](CHAP_Mapping.md "CHAP_Mapping.md").
4. Create a mapping rule to define the target database platform for your source database.
   For more information, see [Mapping data types in the AWS Schema Conversion Tool](CHAP_Mapping.md "CHAP_Mapping.md").
5. Choose **View**, and then choose **Main view**.
6. In the left panel that displays the objects of your source database, choose your source
   database schemas. Open the context (right-click) menu for the object, and then choose
   **Load schema**. This operation loads all source schema metadata into your
   AWS SCT project.

The **Create report** and **Convert schema** operations
also load all source schema metadata into your AWS SCT project.
If you ran one of these operations from the context menu, skip the
**Load schema** operation. 7. On the **File** menu, choose **Save project** to save the
source database metadata in your project. 8. Choose **Disconnect from the server** to disconnect from your source database.
Now you can use AWS SCT in the offline mode.
