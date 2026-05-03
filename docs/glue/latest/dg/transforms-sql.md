# Using a SQL query to transform data

You can use a **SQL** transform to write your own transform in the form
of a SQL query.

A SQL transform node can have multiple datasets as inputs, but produces only a single
dataset as output. In contains a text field, where you enter the Apache SparkSQL query. You
can assign aliases to each dataset used as input, to help simply the SQL query. For more
information about the SQL syntax, see the [Spark SQL
documentation](https://spark.apache.org/docs/latest/sql-ref.html "https://spark.apache.org/docs/latest/sql-ref.html").

###### Note

If you use a Spark SQL transform with a data source located in a VPC, add an
AWS Glue VPC endpoint to the VPC that contains the data source. For more
information about configuring development endpoints, see [Adding a Development
Endpoint](add-dev-endpoint.md "add-dev-endpoint.md"), [Setting Up Your Environment for Development Endpoints](start-development-endpoint.md "start-development-endpoint.md"), and
[Accessing
Your Development Endpoint](dev-endpoint-elastic-ip.md "dev-endpoint-elastic-ip.md") in the _AWS Glue Developer Guide_.

###### To use a SQL transform node in your job diagram

1. (Optional) Add a transform node to the job diagram, if needed. Choose
   **SQL Query** for the node type.

###### Note

If you use a data preview session and a custom SQL or custom code node,
the data preview session will execute the SQL or code block as-is for the entire dataset. 2. On the **Node properties** tab, enter a name for the node in
the job diagram. If a node parent is not already selected, or if you want multiple
inputs for the SQL transform, choose a node from the **Node parents**
list to use as the input source for the transform. Add additional parent nodes as
needed. 3. Choose the **Transform** tab in the node details panel. 4. The source datasets for the SQL query are identified by the names you specified in
the **Name** field for each node. If you do not want to use these
names, or if the names are not suitable for a SQL query, you can associate a name to
each dataset. The console provides default aliases, such as
`MyDataSource`.

For example, if a parent node for the SQL transform node is named `Rename Org
 PK field`, you might associate the name `org_table` with this
dataset. This alias can then be used in the SQL query in place of the node name. 5. In the text entry field under the heading **Code block**, paste or
enter the SQL query. The text field displays SQL syntax highlighting and keyword
suggestions. 6. With the SQL transform node selected, choose the **Output schema**
tab, and then choose **Edit**. Provide the columns and data types that
describe the output fields of the SQL query.

Specify the schema using the following actions in the **Output
schema** section of the page:

    * To rename a column, place the cursor in the **Key** text box
     for the column (also referred to as a *field* or
     *property key*) and enter the new name.
    * To change the data type for a column, select the new data type for the column
     from the drop-down list.
    * To add a new top-level column to the schema, choose the Overflow (
    ![A rectangle with an ellipsis (...) in the center](images/edit-schema-actions-button.png)
    ) button, and then choose **Add root key**. New
     columns are added at the top of the schema.
    * To remove a column from the schema, choose the delete icon (
    ![An outline of a trash can](images/delete-icon-black.png)
    ) to the far right of the Key name.

7. When you finish specifying the output schema, choose **Apply** to
   save your changes and exit the schema editor. If you do not want to save you changes,
   choose **Cancel** to edit the schema editor.
8. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.
