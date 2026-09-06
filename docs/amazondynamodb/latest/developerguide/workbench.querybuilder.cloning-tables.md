

# Cloning tables with NoSQL Workbench
<a name="workbench.querybuilder.cloning-tables"></a>

Cloning tables will copy a table’s key schema (and optionally GSI schema and items) between your development environments. You can clone a table between DynamoDB local to an Amazon DynamoDB account, and even clone a table from one account to another in different Regions for faster experimentation.

**To clone a table**

1. In the **Operation Builder**, select your connection and Region (Region selection is not available for DynamoDB local).

1. After you are connected to DynamoDB, browse your tables and select the table you want to clone.

1. From the horizontal ellipsis menu, select the **Clone** option.

1. Input your clone destination details:

   1. Select a connection.

   1. Select a Region (Region is not available for DynamoDB local).

   1. Enter a new table name.

   1. Choose a clone option:

      1. **Key schema** is selected by default and cannot be unselected. By default, cloning a table will copy your primary key and sort key if they are available.

      1. **GSI schema** is selected by default if your table to be cloned has a GSI. Cloning a table will copy your GSI primary key and sort key if they are available. You have the option to deselect GSI schema to skip cloning the GSI schema. Cloning a table will copy your base table’s capacity settings as the GSI’s capacity settings. You can use the `UpdateTable` operation in Operation Builder to update the table’s GSI capacity setting after cloning is complete.

1. Enter the number of items to clone. To only clone the key schema and optionally the GSI schema, you can keep the **Items to clone** value at 0. The maximum number of items that can be cloned is 5000.

1. Choose a capacity mode:

   1. **On-demand mode** is selected by default. DynamoDB on-demand offers pay-per-request pricing for read and write requests so that you pay only for what you use. To learn more, see [DynamoDB On-demand mode](capacity-mode.md#capacity-mode-on-demand) .

   1. **Provisioned mode** lets you specify the number of reads and writes per second that you require for your application. You can use auto scaling to adjust your table’s provisioned capacity automatically in response to traffic changes. To learn more, see [DynamoDB Provisioned mode](provisioned-capacity-mode.md).

1. Select **Clone** to begin cloning.

1. The cloning process will run in the background. The **Operation builder** tab will show a notification when there is a change in the cloning table status. You can access this status by selecting the **Operation builder** tab and then selecting the arrow button. The arrow button is located on the cloning table status widget located near the bottom of the menu sidebar.