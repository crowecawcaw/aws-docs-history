

# Saving projects in AWS SCT
<a name="CHAP_UserInterface.SaveProject"></a>

Use the following procedure to save an AWS Schema Conversion Tool project.

**To save your project**

1. Start the AWS Schema Conversion Tool.

1. On the **File** menu, choose **Save project**. 

    AWS SCT saves the project in the folder, which you specified when you created the project. 

Use the following procedure to open an existing AWS Schema Conversion Tool project.

**To open your project**

1. On the **File** menu, choose **Open project**. The **Open** dialog box appears. 

1.  Choose the project folder and then choose the Windows Script Component (\*.sct) file. 

1. AWS SCT opens your project but doesn't automatically connect to your source and target databases. Choose **Connect to the server** at the top of your database schema trees to connect to your source and target databases.

If you open a project saved in AWS SCT version 1.0.655 or before, AWS SCT automatically creates mapping rules for all source database schemas to the target database platform. To add other target database platforms, delete existing mapping rules and then create new mapping rules. For more information on creating mapping rules, see [Mapping data types in the AWS Schema Conversion Tool](CHAP_Mapping.md). 