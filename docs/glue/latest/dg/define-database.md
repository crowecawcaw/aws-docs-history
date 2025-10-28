# Creating databases

Databases are used to organize metadata tables in the AWS Glue. When you define a table in
the AWS Glue Data Catalog, you add it to a database. A table can be in only one database.

Your database can contain tables that define data from many different data stores. This
data can include objects in Amazon Simple Storage Service (Amazon S3) and relational tables in Amazon Relational Database Service.

###### Note

When you delete a database from the AWS Glue Data Catalog, all the tables in the database are
also deleted.

To view the list of databases, sign in to the AWS Management Console and open the AWS Glue console at
[https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/"). Choose **Databases**, and then choose a database name
in the list to view the
details.

From the **Databases** tab in the AWS Glue console, you can add, edit, and
delete databases:

- To create a new database, choose **Add database** and provide a
  name and description. For compatibility with other metadata stores, such as Apache Hive,
  the name is folded to lowercase characters.

###### Note

If you plan to access the database from Amazon Athena, then provide a name with only alphanumeric
and underscore characters. For more information,
see
[Athena names](../../../athena/latest/ug/tables-databases-columns-names.md#ate-table-database-and-column-names-allow-only-underscore-special-characters "../../../athena/latest/ug/tables-databases-columns-names.md#ate-table-database-and-column-names-allow-only-underscore-special-characters").

- To edit the description for a database, select the check box next to the database
  name and choose **Edit**.
- To delete a database, select the check box next to the database name and choose
  **Remove**.
- To display the list of tables contained in the database, choose
  the database name and the database properties will display all tables in the database.
  To change the database that a crawler writes to, you must change the crawler definition.
  For more information, see [Using crawlers to populate the Data Catalog](add-crawler.md "add-crawler.md") .

## Database resource links

|                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The AWS Glue console was recently updated. The current version of the console does not support Database Resource Links. | The Data Catalog can also contain _resource links_ to databases. A database resource link is a link to a local or shared database. Currently, you can create resource links only in AWS Lake Formation. After you create a resource link to a database, you can use the resource link name wherever you would use the database name. Along with databases that you own or that are shared with you, database resource links are returned by `glue:GetDatabases()` and appear as entries on the **Databases** page of the AWS Glue console. The Data Catalog can also contain table resource links. For more information about resource links, see [Creating Resource Links](../../../lake-formation/latest/dg/creating-resource-links.md "../../../lake-formation/latest/dg/creating-resource-links.md") in the _AWS Lake Formation Developer Guide_. |
