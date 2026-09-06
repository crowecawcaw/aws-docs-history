

# Building API operations
<a name="workbench.querybuilder.operationbuilder.api"></a>

To use NoSQL Workbench to build DynamoDB CRUD APIs, select **Operation builder** from the left of the NoSQL Workbench user interface.

Then select **Open** and choose a connection.

You can perform the following operations in the operation builder.
+ [Delete Table](#workbench.querybuilder.operationbuilder.DeleteTable)
+ [Create Table](#workbench.querybuilder.operationbuilder.CreateTable)
+ [Update Table](#workbench.querybuilder.operationbuilder.UpdateTable)
+ [Put Item](#workbench.querybuilder.operationbuilder.Put)
+ [Update Item](#workbench.querybuilder.operationbuilder.update)
+ [Delete Item](#workbench.querybuilder.operationbuilder.Delete)
+ [Query](#workbench.querybuilder.operationbuilder.Query)
+ [Scan](#workbench.querybuilder.operationbuilder.scan)
+ [Transact Get Items](#workbench.querybuilder.operationbuilder.transactget)
+ [Transact Write Items](#workbench.querybuilder.operationbuilder.transactwrite)

## Delete table
<a name="workbench.querybuilder.operationbuilder.DeleteTable"></a>

To run a `Delete Table` operation, do the following.

1. Find the table you want to delete from the **Tables** section.

1. Select **Delete Table** from the horizontal ellipsis menu.

1. Confirm you want to delete the table by entering the **Table name**.

1. Select **Delete**.

For more information about this operation, see [Delete table](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html) in the *Amazon DynamoDB API Reference*. 

## Delete GSI
<a name="workbench.querybuilder.operationbuilder.DeleteGSI"></a>

To run a `Delete GSI` operation, do the following.

1. Find the GSI of a table you want to delete from the **Tables** section.

1. Select **Delete GSI** from the horizontal ellipsis menu.

1. Confirm you want to delete the GSI by entering the **GSI name**.

1. Select **Delete**.

For more information about this operation, see [Delete table](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html) in the *Amazon DynamoDB API Reference*. 

## Create table
<a name="workbench.querybuilder.operationbuilder.CreateTable"></a>

To run a `Create Table` operation, do the following.

1. Choose the **\+** icon next to the **Tables** section.

1. Enter the table name desired.

1. Create a partition key.

1. Optional: create a sort key.

1. To customize capacity settings, and uncheck the box next to **Use default capacity settings**.
   + You can now select either **Provisioned** or **On-demand capacity.**

     With Provisioned selected, you can set minimum and maximum read and write capacity units. You can also enable or disable auto scaling.
   + If the table is currently set to On-demand, you will be unable to specify a provisioned throughput.
   + If you switch from On-demand to Provisioned throughput, then Autoscaling will automatically be applied to all GSIs with: min: 1, max: 10; target: 70%.

1. Select **Skip GSIs and create** to create this table without a GSI. Optionally, you can select **Next** to create a GSI with this new table.

For more information about this operation, see [Create table](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html) in the *Amazon DynamoDB API Reference*. 

## Create GSI
<a name="workbench.querybuilder.operationbuilder.CreateGSI"></a>

To run a `Create GSI` operation, do the following.

1. Find a table that you want to add a GSI to.

1. From the horizontal ellipsis menu, select **Create GSI**.

1. Name your GSI under **Index name**.

1. Create a partition key.

1. Optional: create a sort key.

1. Choose a projection type option from the dropdown.

1. Select **Create GSI**.

For more information about this operation, see [Create table](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html) in the *Amazon DynamoDB API Reference*. 

## Update table
<a name="workbench.querybuilder.operationbuilder.UpdateTable"></a>

To update capacity settings for a table with an `Update Table` operation, do the following.

1. Find the table you want to update capacity settings for.

1. From the horizontal ellipsis menu, select **Update capacity settings**.

1. Select either **Provisioned** or **On-demand capacity.**

   With **Provisioned** selected, you can set minimum and maximum read and write capacity units. You can also enable or disable auto scaling.

1. Select **Update**.

For more information about this operation, see [Update table](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html) in the *Amazon DynamoDB API Reference*.

## Update GSI
<a name="workbench.querybuilder.operationbuilder.UpdateGSI"></a>

To update capacity settings for a GSI with an `Update Table` operation, do the following.

**Note**  
By default, global secondary indexes inherit the capacity settings of the base table. Global secondary indexes can have a different capacity mode only when the base table is in provisioned capacity mode. When you create a global secondary index on a provisioned mode table, you must specify read and write capacity units for the expected workload on that index. For more information, see [Provisioned throughput considerations for Global Secondary Indexes](GSI.md#GSI.ThroughputConsiderations).

1. Find the GSI you want to update capacity settings for.

1. From the horizontal ellipsis menu, select **Update capacity settings**.

1. You can now select either **Provisioned** or **On-demand capacity.**

   With **Provisioned** selected, you can set minimum and maximum read and write capacity units. You can also enable or disable auto scaling.

1. Select **Update**.

For more information about this operation, see [Update table](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html) in the *Amazon DynamoDB API Reference*.

## Put item
<a name="workbench.querybuilder.operationbuilder.Put"></a>

You create an item by using the `Put Item` operation. To run or generate code for a `Put Item` operation, do the following.

1. Find the table you want to create an item in.

1. From the **Actions** dropdown, select **Create item**.

1. Enter the partition key value.

1. Enter the sort key value, if one exists.

1. If you want to add non-key attributes, do the following:

   1. Select **\+ Add other attributes**.

   1. Specify the **Attribute name**, **Type**, and **Value**. 

1. If a condition expression must be satisfied for the `Put Item` operation to succeed, do the following:

   1. Choose **Condition**.

   1. Specify the attribute name, comparison operator, attribute type, and attribute value.

   1. If other conditions are needed, choose **Condition** again.

   For more information, see [DynamoDB condition expression CLI example](Expressions.ConditionExpressions.md).

1. If you want to generate code, choose **Generate code**.

   Select your desired language from the displayed tabs. You can now copy this code and use it in your application.

1. If you want the operation to be run immediately, choose **Run**.

1. If you want to save this operation for later use, choose **Save operation**, then enter a name for your operation and choose **Save**.

For more information about this operation, see [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) in the *Amazon DynamoDB API Reference*. 

## Update item
<a name="workbench.querybuilder.operationbuilder.update"></a>

To run or generate code for an `Update Item` operation, do the following:

1. Find the table you want to update an item in.

1. Select the item.

1. Enter the attribute name and attribute value for the selected expression.

1. If you want to add more expressions, choose another expression in the **Update Expression** dropdown list, and then select the **\+** icon.

1. If a condition expression must be satisfied for the `Update Item` operation to succeed, do the following:

   1. Choose **Condition**.

   1. Specify the attribute name, comparison operator, attribute type, and attribute value.

   1. If other conditions are needed, choose **Condition** again.

   For more information, see [DynamoDB condition expression CLI example](Expressions.ConditionExpressions.md).

1. If you want to generate code, choose **Generate code**.

   Choose the tab for the language that you want. You can now copy this code and use it in your application.

1. If you want the operation to be run immediately, choose **Run**.

1. If you want to save this operation for later use, choose **Save operation**, then enter a name for your operation and choose **Save**.

For more information about this operation, see [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html) in the *Amazon DynamoDB API Reference*. 

## Delete item
<a name="workbench.querybuilder.operationbuilder.Delete"></a>

To run a `Delete Item` operation, do the following.

1. Find the table you want to delete an item in. 

1. Select the item.

1. From the **Actions** dropdown, select **Delete item**.

1. Confirm you want to delete the item by selecting **Delete**.

For more information about this operation, see [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html) in the *Amazon DynamoDB API Reference*.

## Duplicate item
<a name="workbench.querybuilder.operationbuilder.Duplicate"></a>

You can duplicate an item by creating a new item with the same attributes. To duplicate an item, do the following.

1. Find the table you want to duplicate an item in.

1. Select the item.

1. From the **Actions** dropdown, select **Duplicate item**.

1. Specify a new partition key.

1. Specify a new sort key (if necessary).

1. Select **Run**.

For more information about this operation, see [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html) in the *Amazon DynamoDB API Reference*.

## Query
<a name="workbench.querybuilder.operationbuilder.Query"></a>

To run or generate code for a `Query` operation, do the following.

1. Select **Query** from the top of the NoSQL Workbench UI.

1. Specify the partition key value.

1. If a sort key is needed for the `Query` operation:

   1. Select **Sort key**.

   1. Specify the comparison operator, and attribute value.

1. Select **Query** to run this query operation. If more options are needed, check the **More options** checkbox and continue on with the following steps.

1. If not all the attributes should be returned with the operation result, select **Projection expression**.

1. Choose the **\+** icon.

1. Enter the attribute to return with the query result.

1. If more attributes are needed, choose the **\+ **.

1. If a condition expression must be satisfied for the `Query` operation to succeed, do the following:

   1. Choose **Condition**.

   1. Specify the attribute name, comparison operator, attribute type, and attribute value.

   1. If other conditions are needed, choose **Condition** again.

   For more information, see [DynamoDB condition expression CLI example](Expressions.ConditionExpressions.md).

1. If you want to generate code, choose **Generate code**.

   Choose the tab for the language that you want. You can now copy this code and use it in your application.

1. If you want the operation to be run immediately, choose **Run**.

1. If you want to save this operation for later use, choose **Save operation**, then enter a name for your operation and choose **Save**.

For more information about this operation, see [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) in the *Amazon DynamoDB API Reference*. 

## Scan
<a name="workbench.querybuilder.operationbuilder.scan"></a>

To run or generate code for a `Scan` operation, do the following.

1. Select **Scan** from the top of the NoSQL Workbench UI.

1. Select the **Scan** button to perform this basic scan operation. If more options are needed, check the **More options** checkbox and continue on with the following steps.

1. Specify an attribute name to filter your scan results.

1. If not all the attributes should be returned with the operation result, select **Projection expression**.

1. If a condition expression must be satisfied for the scan operation to succeed, do the following:

   1. Choose **Condition**.

   1. Specify the attribute name, comparison operator, attribute type, and attribute value.

   1. If other conditions are needed, choose **Condition** again. 

   For more information, see [DynamoDB condition expression CLI example](Expressions.ConditionExpressions.md).

1. If you want to generate code, choose **Generate code**.

   Choose the tab for the language that you want. You can now copy this code and use it in your application.

1. If you want the operation to be run immediately, choose **Run**.

1. If you want to save this operation for later use, choose **Save operation**, then enter a name for your operation and choose **Save**.

## TransactGetItems
<a name="workbench.querybuilder.operationbuilder.transactget"></a>

To run or generate code for a `TransactGetItems` operation, do the following.

1. From the **More operations** dropdown at the top of the NoSQL Workbench UI, choose **TransactGetItems**.

1. Choose the **\+** icon near **TransactGetItem**.

1. Specify a partition key.

1. Specify a sort key (if necessary).

1. Select **Run** to perform the operation, **Save operation** to save it, or **Generate code** to generate code for it.

For more information about transactions, see [Amazon DynamoDB transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html).

## TransactWriteItems
<a name="workbench.querybuilder.operationbuilder.transactwrite"></a>

To run or generate code for a `TransactWriteItems` operation, do the following.

1. From the **More operations** dropdown at the top of the NoSQL Workbench UI, choose **TransactWriteItems**.

1. Choose an operation from the **Actions** dropdown.

1. Choose the **\+** icon near **TransactWriteItem**.

1. In the **Actions** dropdown, choose the operation that you want to perform.
   + For `DeleteItem`, follow the instructions for the [Delete item](#workbench.querybuilder.operationbuilder.Delete) operation. 
   + For `PutItem`, follow the instructions for the [Put item](#workbench.querybuilder.operationbuilder.Put) operation. 
   + For `UpdateItem`, follow the instructions for the [Update item](#workbench.querybuilder.operationbuilder.update) operation.

   To change the order of actions, choose an action in the list on the left side, and then choose the up or down arrows to move it up or down in the list. 

   To delete an action, choose the action in the list, and then choose the **Delete** (trash can) icon. 

1. Select **Run** to perform the operation, **Save operation** to save it, or **Generate code** to generate code for it.

For more information about transactions, see [Amazon DynamoDB transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html).