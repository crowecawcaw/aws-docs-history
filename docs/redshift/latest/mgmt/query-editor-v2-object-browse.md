

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Browsing an Amazon Redshift database
<a name="query-editor-v2-object-browse"></a>

Within a database, you can manage schemas, tables, views, functions, and stored procedures in the tree-view panel. Each object in the view has actions associated with it in a context (right-click) menu.

The hierarchical tree-view panel displays database objects. To refresh the tree-view panel to display database objects that might have been created after the tree-view was last displayed, choose the ![Circular arrow icon representing a refresh or reload action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-refresh.png) icon. Open the context (right-click) menu for an object to see what actions you can perform.

![Tree-view icons](http://docs.aws.amazon.com/redshift/latest/mgmt/images/sqlworkbench-tree-view.png)

After you choose a table, you can do the following:
+ To start a query in the editor with a SELECT statement that queries all columns in the table, use **Select table**.
+ To see the attributes or a table, use **Show table definition**. Use this to see column names, column types, encoding, distribution keys, sort keys, and whether a column can contain null values. For more information about table attributes, see [CREATE TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html) in the *Amazon Redshift Database Developer Guide*.
+ To delete a table, use **Delete**. You can either use **Truncate table** to delete all rows from the table or **Drop table** to remove the table from the database. For more information, see [TRUNCATE](https://docs.aws.amazon.com/redshift/latest/dg/r_TRUNCATE.html) and [DROP TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_DROP_TABLE.html) in the *Amazon Redshift Database Developer Guide*. 

Choose a schema to **Refresh** or **Drop schema**. 

Choose a view to **Show view definition** or **Drop view**. 

Choose a function to **Show function definition** or **Drop function**. 

Choose a stored procedure to **Show procedure definition** or **Drop procedure**. 