# Adding and validating access patterns

You can use NoSQL Workbench for Amazon DynamoDB to create, store, and validate _access patterns_.

###### Note

See [Identify your data access patterns](../../../prescriptive-guidance/latest/dynamodb-data-modeling/step3.md "../../../prescriptive-guidance/latest/dynamodb-data-modeling/step3.md") for more details on identifying the right access patterns.

###### To create an access pattern

1. Open NoSQL Workbench, and on the main screen, choose the name of the model that you want to add access patterns to.
2. On the left side, choose the **Access patterns** tab, and choose the **+** icon.
3. On the next screen, provide a **Name**, an optional **Description**, the **Type** of the access pattern, and the **Table** or **Global Secondary Index** to test the access pattern against.

###### Note

NoSQL Workbench currently supports the following operations for access patterns:
`Scan`, `Query`, `GetItem`, `PutItem`, `UpdateItem`, `DeleteItem`. Amazon DynamoDB supports a broader list of operations. 4. After you create an access pattern, you can switch to the **Validate** tab to verify that your data model is designed to return expected results for the access pattern.
See [Adding sample data to a data model](workbench.Modeler.AddData.md "workbench.Modeler.AddData.md") for details on how to auto-generate sample data for your tables. Different types of access patterns support different input parameters.

###### Note

To validate access patterns, NoSQL Workbench starts a separate DynamoDB local database on port `8001` (by default) with tables and indexes stored in memory.

    * NoSQL Workbench automatically adds the sample data from your model to the temporary tables.
    * If you edit the sample data or the data model itself, NoSQL Workbench updates the temporary tables.
    * This temporary database is erased when you close the application.

###### To edit your access patterns

1. Open NoSQL Workbench, and on the main screen, choose the name of the model that you want to edit access patterns for.
2. On the left side, choose the **Access patterns** tab.
3. To edit an access pattern, choose it from the list on the left.
4. In the top bar, choose **Edit**.
