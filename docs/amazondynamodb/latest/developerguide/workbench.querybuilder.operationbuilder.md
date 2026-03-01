# Building API operations

To use NoSQL Workbench to build DynamoDB CRUD APIs, select **Operation
builder** from the left of the NoSQL Workbench user interface.

Then select **Open** and choose a connection.

You can perform the following operations in the operation builder.

- [Delete
  Table](#workbench.querybuilder.operationbuilder.DeleteTable "#workbench.querybuilder.operationbuilder.DeleteTable")
- [Create
  Table](#workbench.querybuilder.operationbuilder.CreateTable "#workbench.querybuilder.operationbuilder.CreateTable")
- [Update
  Table](#workbench.querybuilder.operationbuilder.UpdateTable "#workbench.querybuilder.operationbuilder.UpdateTable")

- [Put
  Item](#workbench.querybuilder.operationbuilder.Put "#workbench.querybuilder.operationbuilder.Put")
- [Update
  Item](#workbench.querybuilder.operationbuilder.update "#workbench.querybuilder.operationbuilder.update")
- [Delete
  Item](#workbench.querybuilder.operationbuilder.Delete "#workbench.querybuilder.operationbuilder.Delete")
- [Query](#workbench.querybuilder.operationbuilder.Query "#workbench.querybuilder.operationbuilder.Query")
- [Scan](#workbench.querybuilder.operationbuilder.scan "#workbench.querybuilder.operationbuilder.scan")
- [Transact Get Items](#workbench.querybuilder.operationbuilder.transactget "#workbench.querybuilder.operationbuilder.transactget")
- [Transact Write Items](#workbench.querybuilder.operationbuilder.transactwrite "#workbench.querybuilder.operationbuilder.transactwrite")

## Delete table

To run a `Delete Table` operation, do the following.

1. Find the table you want to delete from the **Tables** section.
2. Select **Delete Table** from the
   horizontal ellipsis menu.
3. Confirm you want to delete the table by entering the **Table name**.
4. Select **Delete**.

For more information about this operation, see [Delete
table](../APIReference/API_DeleteTable.md "../APIReference/API_DeleteTable.md") in the _Amazon DynamoDB API Reference_.

## Delete GSI

To run a `Delete GSI` operation, do the following.

1. Find the GSI of a table you want to delete from the **Tables** section.
2. Select **Delete GSI** from the horizontal
   ellipsis menu.
3. Confirm you want to delete the GSI by entering the **GSI name**.
4. Select **Delete**.

For more information about this operation, see [Delete
table](../APIReference/API_DeleteTable.md "../APIReference/API_DeleteTable.md") in the _Amazon DynamoDB API Reference_.

## Create table

To run a `Create Table` operation, do the following.

1. Choose the **+** icon next to the
   **Tables** section.
2. Enter the table name desired.
3. Create a partition key.
4. Optional: create a sort key.
5. To customize capacity settings, and uncheck the box next to **Use default capacity settings**.
   - You can now select either **Provisioned** or **On-demand
     capacity.**

   With Provisioned selected, you can set minimum and maximum
   read and write capacity units. You can also enable or disable
   auto scaling.
   - If the table is currently set to On-demand, you will be unable
     to specify a provisioned throughput.
   - If you switch from On-demand to Provisioned throughput, then
     Autoscaling will automatically be applied to all GSIs with: min:
     1, max: 10; target: 70%.

6. Select **Skip GSIs and create**
   to create this table without a GSI. Optionally, you can select
   **Next** to create a GSI with
   this new table.

For more information about this operation, see [Create
table](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md") in the _Amazon DynamoDB API Reference_.

## Create GSI

To run a `Create GSI` operation, do the following.

1. Find a table that you want to add a GSI to.
2. From the horizontal ellipsis menu, select **Create
   GSI**.
3. Name your GSI under **Index
   name**.
4. Create a partition key.
5. Optional: create a sort key.
6. Choose a projection type option from the dropdown.
7. Select **Create GSI**.

For more information about this operation, see [Create
table](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md") in the _Amazon DynamoDB API Reference_.

## Update table

To update capacity settings for a table with an `Update Table`
operation, do the following.

1. Find the table you want to update capacity settings for.
2. From the horizontal ellipsis menu, select **Update
   capacity settings**.
3. Select either **Provisioned** or
   **On-demand capacity.**

With **Provisioned** selected, you can
set minimum and maximum read and write capacity units. You can also
enable or disable auto scaling. 4. Select **Update**.

For more information about this operation, see [Update
table](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md") in the _Amazon DynamoDB API Reference_.

## Update GSI

To update capacity settings for a GSI with an `Update Table`
operation, do the following.

###### Note

By default, global secondary indexes inherit the capacity settings of the
base table. Global secondary indexes can have a different capacity mode only
when the base table is in provisioned capacity mode. When you create a
global secondary index on a provisioned mode table, you must specify read
and write capacity units for the expected workload on that index. For more
information, see [Provisioned throughput considerations for Global Secondary Indexes](GSI.md#GSI.ThroughputConsiderations "GSI.md#GSI.ThroughputConsiderations").

1. Find the GSI you want to update capacity settings for.
2. From the horizontal ellipsis menu, select **Update
   capacity settings**.
3. You can now select either **Provisioned**
   or **On-demand capacity.**

With **Provisioned** selected, you can
set minimum and maximum read and write capacity units. You can also
enable or disable auto scaling. 4. Select **Update**.

For more information about this operation, see [Update
table](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md") in the _Amazon DynamoDB API Reference_.

## Put item

You create an item by using the `Put Item` operation. To run or
generate code for a `Put Item` operation, do the following.

1. Find the table you want to create an item in.
2. From the **Actions** dropdown, select
   **Create item**.
3. Enter the partition key value.
4. Enter the sort key value, if one exists.
5. If you want to add non-key attributes, do the following:
   1. Select **+ Add other attributes**.
   2. Specify the **Attribute name**,
      **Type**, and **Value**.

6. If a condition expression must be satisfied for the `Put
Item` operation to succeed, do the following:
   1. Choose **Condition**.
   2. Specify the attribute name, comparison operator, attribute
      type, and attribute value.
   3. If other conditions are needed, choose
      **Condition** again.For more information, see [DynamoDB condition expression CLI example](Expressions.md "Expressions.md").

7. If you want to generate code, choose **Generate
   code**.

Select your desired language from the displayed tabs. You can now copy
this code and use it in your application. 8. If you want the operation to be run immediately, choose
**Run**. 9. If you want to save this operation for later use, choose
**Save operation**, then enter a name for your
operation and choose **Save**.

For more information about this operation, see [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md") in
the _Amazon DynamoDB API Reference_.

## Update item

To run or generate code for an `Update Item` operation, do the
following:

1. Find the table you want to update an item in.
2. Select the item.
3. Enter the attribute name and attribute value for the selected
   expression.
4. If you want to add more expressions, choose another expression in the
   **Update Expression** dropdown list, and then
   select the **+** icon.
5. If a condition expression must be satisfied for the `Update
Item` operation to succeed, do the following:
   1. Choose **Condition**.
   2. Specify the attribute name, comparison operator, attribute
      type, and attribute value.
   3. If other conditions are needed, choose
      **Condition** again.For more information, see [DynamoDB condition expression CLI example](Expressions.md "Expressions.md").

6. If you want to generate code, choose **Generate
   code**.

Choose the tab for the language that you want. You can now copy this
code and use it in your application. 7. If you want the operation to be run immediately, choose
**Run**. 8. If you want to save this operation for later use, choose
**Save operation**, then enter a name for your
operation and choose **Save**.

For more information about this operation, see [UpdateItem](../APIReference/API_UpdateItem.md "../APIReference/API_UpdateItem.md") in the _Amazon DynamoDB API Reference_.

## Delete item

To run a `Delete Item` operation, do the following.

1. Find the table you want to delete an item in.
2. Select the item.
3. From the **Actions** dropdown, select
   **Delete item**.
4. Confirm you want to delete the item by selecting **Delete**.

For more information about this operation, see [DeleteItem](../APIReference/API_DeleteItem.md "../APIReference/API_DeleteItem.md") in the _Amazon DynamoDB API Reference_.

## Duplicate item

You can duplicate an item by creating a new item with the same attributes. To
duplicate an item, do the following.

1. Find the table you want to duplicate an item in.
2. Select the item.
3. From the **Actions** dropdown, select
   **Duplicate item**.
4. Specify a new partition key.
5. Specify a new sort key (if necessary).
6. Select **Run**.

For more information about this operation, see [DeleteItem](../APIReference/API_DeleteItem.md "../APIReference/API_DeleteItem.md") in the _Amazon DynamoDB API Reference_.

## Query

To run or generate code for a `Query` operation, do the
following.

1. Select **Query** from the top of the
   NoSQL Workbench UI.
2. Specify the partition key value.
3. If a sort key is needed for the `Query` operation:
   1. Select **Sort key**.
   2. Specify the comparison operator, and attribute value.

4. Select **Query** to run this query
   operation. If more options are needed, check the **More options** checkbox and continue on with the following
   steps.
5. If not all the attributes should be returned with the operation
   result, select **Projection expression**.
6. Choose the **+** icon.
7. Enter the attribute to return with the query result.
8. If more attributes are needed, choose the **+** .
9. If a condition expression must be satisfied for the `Query`
   operation to succeed, do the following:
   1. Choose **Condition**.
   2. Specify the attribute name, comparison operator, attribute
      type, and attribute value.
   3. If other conditions are needed, choose
      **Condition** again.For more information, see [DynamoDB condition expression CLI example](Expressions.md "Expressions.md").

10. If you want to generate code, choose **Generate
    code**.

Choose the tab for the language that you want. You can now copy this
code and use it in your application. 11. If you want the operation to be run immediately, choose
**Run**. 12. If you want to save this operation for later use, choose
**Save operation**, then enter a name for your
operation and choose **Save**.

For more information about this operation, see [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") in the
_Amazon DynamoDB API Reference_.

## Scan

To run or generate code for a `Scan` operation, do the
following.

1. Select **Scan** from the top of the NoSQL
   Workbench UI.
2. Select the **Scan** button to perform
   this basic scan operation. If more options are needed, check the
   **More options** checkbox and continue
   on with the following steps.
3. Specify an attribute name to filter your scan results.
4. If not all the attributes should be returned with the operation
   result, select **Projection expression**.
5. If a condition expression must be satisfied for the scan operation to
   succeed, do the following:
   1. Choose **Condition**.
   2. Specify the attribute name, comparison operator, attribute
      type, and attribute value.
   3. If other conditions are needed, choose
      **Condition** again.For more information, see [DynamoDB condition expression CLI example](Expressions.md "Expressions.md").

6. If you want to generate code, choose **Generate
   code**.

Choose the tab for the language that you want. You can now copy this
code and use it in your application. 7. If you want the operation to be run immediately, choose
**Run**. 8. If you want to save this operation for later use, choose
**Save operation**, then enter a name for your
operation and choose **Save**.

## TransactGetItems

To run or generate code for a `TransactGetItems` operation, do the
following.

1. From the **More operations** dropdown at
   the top of the NoSQL Workbench UI, choose **TransactGetItems**.
2. Choose the **+** icon near **TransactGetItem**.
3. Specify a partition key.
4. Specify a sort key (if necessary).
5. Select **Run** to perform the operation,
   **Save operation** to save it, or
   **Generate code** to generate code for
   it.

For more information about transactions, see [Amazon DynamoDB
transactions](transactions.md "transactions.md").

## TransactWriteItems

To run or generate code for a `TransactWriteItems` operation, do
the following.

1.  From the **More operations** dropdown at
    the top of the NoSQL Workbench UI, choose **TransactWriteItems**.
2.  Choose an operation from the **Actions**
    dropdown.
3.  Choose the **+** icon near **TransactWriteItem**.
4.  In the **Actions** dropdown, choose the operation
    that you want to perform.

        * For `DeleteItem`, follow the instructions for the
         [Delete item](#workbench.querybuilder.operationbuilder.Delete "#workbench.querybuilder.operationbuilder.Delete") operation.
        * For `PutItem`, follow the instructions for the
         [Put item](#workbench.querybuilder.operationbuilder.Put "#workbench.querybuilder.operationbuilder.Put") operation.
        * For `UpdateItem`, follow the instructions for the
         [Update item](#workbench.querybuilder.operationbuilder.update "#workbench.querybuilder.operationbuilder.update") operation.

    To change the order of actions, choose an action in the list on the
    left side, and then choose the up or down arrows to move it up or down
    in the list.

To delete an action, choose the action in the list, and then choose
the **Delete** (trash can) icon. 5. Select **Run** to perform the operation,
**Save operation** to save it, or
**Generate code** to generate code for
it.

For more information about transactions, see [Amazon DynamoDB
transactions](transactions.md "transactions.md").
