

# Adding an analysis rule to a configured table
<a name="add-analysis-rule"></a>

The following sections describe how to add an analysis rule to your configured table. By deﬁning the analysis rules, you can authorize the member who can query to run queries that match a speciﬁc analysis rule supported by AWS Clean Rooms.

AWS Clean Rooms supports the following types of analysis rules:
+ [Aggregation analysis rule](analysis-rules-aggregation.md)
+ [List analysis rule](analysis-rules-list.md)
+ [Custom analysis rule in AWS Clean Rooms](analysis-rules-custom.md)

There can be only one analysis rule per configured table. You can configure the analysis rule any time before you associate your configured tables with the collaboration.

**Important**  
If you are using Cryptographic Computing for Clean Rooms and have encrypted data tables in the collaboration, the analysis rule you add to the encrypted configured table should be consistent with how the data was encrypted. For example, if you encrypted the data for SELECT (aggregation analysis rule), you shouldn't add the analysis rule for JOIN (list analysis rule).

**Topics**
+ [Adding an aggregation analysis rule to a table (guided flow)](#add-agg-analysis-rule-console-wizard)
+ [Adding a list analysis rule to a table (guided flow)](#add-list-analysis-rule-console-wizard)
+ [Adding a custom analysis rule to a table (guided flow)](#add-custom-analysis-rule-wizard)
+ [Adding analysis rule to a table (JSON editor)](#add-analysis-rule-console-json-editor)
+ [Next steps](#add-analysis-rule-next-step)

## Adding an aggregation analysis rule to a table (guided flow)
<a name="add-agg-analysis-rule-console-wizard"></a>

The *aggregation analysis rule* allows queries that aggregate statistics without revealing row-level information using COUNT, SUM, and AVG functions along optional dimensions.

This procedure describes the process of adding an aggregation analysis rule to your configured table by using the **Guided flow** option in the AWS Clean Rooms console.

**Note**  
Configured tables using non-S3 data sources only support [custom analysis rules](#add-custom-analysis-rule-wizard).

**To add the aggregation analysis rule to a table (guided flow)**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Tables**.

1. Choose the configured table.

1. On the configured table detail page, choose **Configure analysis rule**.

1. Under **Step 1: Choose analysis rule type**, under **Analysis rule type**, choose the **Aggregation** option.

1. Under **Creation method**, select **Guided flow**, and then choose **Next**. 

1. Under **Step 2: Specify query controls**, for **Aggregate functions**:

   1. Choose an **Aggregate function** from the dropdown:
      + **COUNT**
      + **COUNT DISTINCT**
      + **SUM**
      + **SUM DISTINCT**
      + **AVG**

   1. Choose which columns can be used in the **Aggregate function** from the **Columns** dropdown.

   1. (Optional) Choose **Add another function** to add another aggregate function and associate one or more columns to that function.
**Note**  
At least one aggregate function is required.

   1. (Optional) Choose **Remove** to remove an aggregate function.

1. For **Join controls**, 

   1. Choose one option for **Allow table to be queried by itself**:


<table>
<thead>
  <tr><th>If you choose...</th><th>Then ...</th></tr>
</thead>
<tbody>
  <tr><td><b>No, only overlap can be queried</b></td><td>The table can be queried only when joined to a table owned by the member who can query. </td></tr>
  <tr><td><b>Yes</b></td><td>The table can be queried by itself or when joined to other tables.</td></tr>
</tbody>
</table>


   1. Under **Specify join columns**, choose the columns that you want to allow to be used in the INNER JOIN statement.

      This is *optional* if you have selected **Yes** in the previous step.

   1. Under **Specify allowed operators for matching**, choose which, if any, operators can be used for matching on multiple join columns. If you select two or more JOIN columns, one of these operators is required.


<table>
<thead>
  <tr><th>If you choose...</th><th>Then ...</th></tr>
</thead>
<tbody>
  <tr><td><b>AND</b></td><td>You can include <code>AND</code> in the <code>INNER JOIN</code> match conditions to join one column to another column between tables.</td></tr>
  <tr><td><b>OR</b></td><td>You can include <code>OR</code> in the <code>INNER JOIN</code> match conditions to combine multiple column matches between tables. This logical operator is useful for obtaining a higher match rate.</td></tr>
</tbody>
</table>


1. *(Optional)* For **Dimension controls**, in the **Specify dimension columns** dropdown, choose which columns you want to allow to be used in the SELECT statement, and the WHERE, GROUP BY, and ORDER BY parts of the query.
**Note**  
Aggregate function or join columns can’t be used as **Dimension** columns.

1. For **Scalar functions**, choose one option for **Which scalar functions do you want to allow?**


<table>
<thead>
  <tr><th>If you choose...</th><th>Then ...</th></tr>
</thead>
<tbody>
  <tr><td><b>All currently supported by AWS Clean Rooms</b></td><td>You allow all scalar functions currently supported by AWS Clean Rooms.<ul><li> You can choose <b>View list</b> to see the entire list of <b>Scalar functions supported in AWS Clean Rooms</b>. </li></ul></td></tr>
  <tr><td><b>A custom list</b></td><td>You can customize which scalar functions to allow.<ul><li> Choose one or more options from the <b>Specify allowed scalar functions</b> dropdown. </li></ul></td></tr>
  <tr><td><b>None</b></td><td>You don't want to allow any scalar functions.</td></tr>
</tbody>
</table>


   For more information, see [Scalar functions](analysis-rules-aggregation.md#scalar-functions).

1. Choose **Next**.

1. Under **Step 3: Specify query results controls**, for **Aggregation constraints**:

   1. Select the dropdown list for each **Column name**.

   1. Select the dropdown list for each **Minimum number of distinct values** that must be met for each output row to be returned, after the COUNT DISTINCT function is applied to it.

   1. Choose **Add constraint** to add more aggregation constraints.

   1. (Optional) Choose **Remove** to remove an aggregation constraint.

1. For **Additional analyses applied to output**, select an option based on your goal. 


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Allow only direct queries on this table. Deny additional analyses from being run on query results. The table can only be used for direct querying.</td><td><b>Not allowed</b></td></tr>
  <tr><td>Allow but don’t require both direct queries and additional analyses on this table.</td><td><b>Allowed</b></td></tr>
  <tr><td>Require that the table can only be used in direct queries that are processed with one of the required additional analyses. Direct queries on this table must be further processed before they can be returned.</td><td><b>Required</b></td></tr>
</tbody>
</table>


1. Choose **Next**.

1. Under **Step 4: Review and configure**, review the selections you’ve made for the previous steps, edit if necessary, and then choose **Configure analysis rule**.

You see a confirmation message that you’ve successfully configured an aggregation analysis rule to the table.

## Adding a list analysis rule to a table (guided flow)
<a name="add-list-analysis-rule-console-wizard"></a>

The *list analysis rule* allows queries that output row-level lists of the overlap between the associated table and a table of the member who can query.

This procedure describes the process of adding the list analysis rule to your configured table using the **Guided flow** option in the AWS Clean Rooms console. 

**Note**  
Configured tables using non-S3 data sources only support [custom analysis rules](#add-custom-analysis-rule-wizard).

**To add a list analysis rule to a table (guided flow)**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Tables**.

1. Choose the configured table.

1. On the configured table detail page, choose **Configure analysis rule**.

1. Under **Step 1: Choose analysis rule type**, under **Analysis rule type**, choose the **List** option.

1. Under **Creation method**, select **Guided flow**, and then choose **Next**. 

1. Under **Step 2: Specify query controls**, for **Join controls**:

   1. Under **Specify join columns**, choose the columns that you want to allow to be used in the INNER JOIN statement.

   1. Under **Specify allowed operators for matching**, choose which, if any, operators can be used for matching on multiple join columns. If you select two or more JOIN columns, one of these operators is required.


<table>
<thead>
  <tr><th>If you choose...</th><th>Then ...</th></tr>
</thead>
<tbody>
  <tr><td><b>AND</b></td><td>You can include <code>AND</code> in the <code>INNER JOIN</code> match conditions to join one column to another column between tables.</td></tr>
  <tr><td><b>OR</b></td><td>You can include <code>OR</code> in the <code>INNER JOIN</code> match conditions to combine multiple column matches between tables. This logical operator is useful for obtaining a higher match rate.</td></tr>
</tbody>
</table>


1. *(Optional)* For **List controls**, in the **Specify list columns** dropdown, choose which columns you want to allow to be used in the query output (that is, used in the SELECT statement), or used to filter results (that is, the WHERE statement).

1. Choose **Next**.

1. Under **Step 3: Specify query results controls**, for **Additional analyses applied to output**, select an option based on your goal. 


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Allow only direct queries on this table. Deny additional analyses from being run on query results. The table can only be used for direct querying.</td><td><b>Not allowed</b></td></tr>
  <tr><td>Allow but don’t require both direct queries and additional analyses on this table.</td><td><b>Allowed</b></td></tr>
  <tr><td>Require that the table can only be used in direct queries that are processed with one of the required additional analyses. Direct queries on this table must be further processed before they can be returned.</td><td><b>Required</b></td></tr>
</tbody>
</table>


1. Under **Step 4: Review and configure**, review the selections you’ve made for the previous steps, edit if necessary, and then choose **Configure analysis rule**.

You see a confirmation message that you’ve successfully configured a list analysis rule for the table.

## Adding a custom analysis rule to a table (guided flow)
<a name="add-custom-analysis-rule-wizard"></a>

The custom analysis rule enables custom SQL queries or PySpark jobs on a configured table. The custom analysis rule is required if you're using:
+ [Analysis templates](create-analysis-template.md) to allow a specific set of pre-approved SQL queries or PySpark jobs or a specific set of accounts that can provide queries that use your data.
+ [AWS Clean Rooms Differential Privacy](differential-privacy.md) to protect against user-identification attempts.
+ Non-S3 data sources, such as Amazon Athena or Snowflake.

This procedure describes the process of adding the custom analysis rule to your configured table using the **Guided flow** option in the AWS Clean Rooms console. 

**To add a custom analysis rule to a table (guided flow)**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Tables**.

1. Choose the configured table.

1. On the configured table detail page, choose **Configure analysis rule**.

1. Under **Step 1: Choose analysis rule type**, under **Analysis rule type**, choose the **Custom** option.

1. Under **Creation method**, select **Guided flow**, and then choose **Next**. 

1. Under **Step 2: Specify analysis controls**, for **Direct analysis controls**, choose an option based on your goal.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended action</th></tr>
</thead>
<tbody>
  <tr><td>Review each new analysis before it is allowed to be run on this configured table</td><td> <ol><li> Under <b>Analysis templates allowed to be run</b>, choose <b>Add analysis template</b>. </li><li> Choose the appropriate <b>Collaboration</b> and the <b>Analysis template</b> from the dropdown lists. </li><li> Choose <b>Next</b>.  </li></ol> </td></tr>
  <tr><td>Allow specific collaborators to run any analyses of a chosen type without review on this table</td><td> <ol><li> Under <b>Analysis type</b>, <ol><li> Choose <b>Any query</b> to allow any query created by the AWS account you specify. </li><li> Choose <b>Any query</b> to allow any job created by the AWS account you specify. </li></ol> </li><li> Under <b>AWS accounts allowed to create any analysis</b>, choose <b>Add AWS account</b>. </li><li> Enter an AWS account or choose the an <b>AWS account ID</b>. from the dropdown list. </li><li> (Optional) Choose <b>Add another AWS account</b> to add another AWS account. </li><li> Choose <b>Next</b>.  </li></ol> </td></tr>
</tbody>
</table>


1. Under **Step 3: Specify analysis results controls**, 

   1. For **Job results controls**, note that no additional results controls are supported.

   1. Under **Query results controls**, for **Columns not allowed in output**, choose the columns you want to be allowed in the query output, based on your goal.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended action</th></tr>
</thead>
<tbody>
  <tr><td>Allow all columns to be returned in query outputs</td><td> <ol><li> Choose <b>None</b> </li><li> Proceed to <b>Additional analyses applied to output</b>. </li></ol> </td></tr>
  <tr><td>Disallow certain columns from being returned in query outputs</td><td> <ol><li> Choose <b>Custom list</b> </li><li> Under <b>Specify disallowed columns</b>, choose the columns that you want removed from query outputs. </li></ol> </td></tr>
</tbody>
</table>


   1. For **Additional analyses applied to output** choose whether additional analyses can be applied to the query output, based on your goal.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td> <ul><li> Allow only direct queries on this table.  </li><li> Deny additional analyses from being run on query results.  </li><li> The table can only be used for direct querying. </li></ul> </td><td><b>Not allowed</b></td></tr>
  <tr><td>Allow but don’t require both direct queries and additional analyses on this table.</td><td><b>Allow</b></td></tr>
  <tr><td> <ul><li> Require that the table can only be used in direct queries that are processed with one of the required additional analyses.  </li><li> Direct queries on this table must be further processed before they can be returned. </li></ul> </td><td><b>Required</b></td></tr>
</tbody>
</table>


   1. Choose **Next**.

1. (Optional) Under **Step 4: Set differential privacy**, determine whether you want differential privacy turned on or off. 

   Differential privacy is a mathematically-proven technique to protect your data from re-identification attacks. 
**Note**  
AWS Clean Rooms Differential Privacy is only available for collaborations where the data is stored in Amazon S3.

   For **Differential privacy**, choose whether to turn differential privacy on or off, based on your goal.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended action</th></tr>
</thead>
<tbody>
  <tr><td> <ul><li> You don't require protection against re-identification attempts  </li><li> Your table doesn't have user-level data  </li></ul> </td><td> <ol><li> Choose <b>Turn off</b>. </li><li> Choose <b>Next</b>. </li></ol> </td></tr>
  <tr><td> <ul><li> You require protection against re-identification attempts </li><li> Your table has user-level data  </li></ul> </td><td> <ol><li> Choose <b>Turn on</b>. </li><li> Select the <b>User identifier column</b> that contains the unique identifier of your users, such as the <code>user_id</code> column, whose privacy you want to protect.  <br />To turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the <b>User identifier column</b> in both analysis rules to maintain a consistent definition of users across tables. In case of a misconfiguration, the member who can query receives an error message that there are two columns to choose from in order to compute the number of user contributions (for example, the number of ad impressions made by a user) while running the query. </li><li> Choose <b>Next</b>. </li></ol> </td></tr>
</tbody>
</table>


1. Under **Step 5: Review and configure**, review the selections you’ve made for the previous steps, edit if necessary, and then choose **Configure analysis rule**.

You see a confirmation message that you’ve successfully configured a custom analysis rule for the table.

## Adding analysis rule to a table (JSON editor)
<a name="add-analysis-rule-console-json-editor"></a>

The following procedure shows how to add an analysis rule to a table using the **JSON editor** option in the AWS Clean Rooms console.

**Note**  
Configured tables using non-S3 data sources only support [custom analysis rules](#add-custom-analysis-rule-wizard).

**To add an aggregation, list, or custom analysis rule to a table (JSON editor)**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Tables**.

1. Choose the configured table.

1. On the configured table detail page, choose **Configure analysis rule**.

1. Under **Step 1: Choose analysis rule type**, under **Analysis rule type**, choose either the **Aggregation**, **List**, or **Custom** option.

1. Under **Creation method**, select **JSON editor**, and then choose **Next**. 

1. Under **Step 2: Specify controls**, you can choose to insert a query structure (**Insert template**) or insert a file (**Import from file**).


<table>
<thead>
  <tr><th>If you choose...</th><th>Then ...</th></tr>
</thead>
<tbody>
  <tr><td><b>Insert template</b></td><td><ol><li> Specify the parameters for the selected analysis rule in the <b>Analysis rule definition</b>.  </li><li> You can press <b>Ctrl</b> + <b>Spacebar</b> to enable auto-complete. </li></ol>For more information about aggregation analysis rule parameters, see <a href="analysis-rules-aggregation.md#agg-query-controls">Aggregation analysis rule - query controls</a>.<br />For more information about list analysis rule parameters, see <a href="analysis-rules-list.md#parameters-list-query-controls">List analysis rule - query controls</a>.</td></tr>
  <tr><td><b>Import from file</b></td><td> <ol><li> Select your JSON file from your local drive. </li><li> Choose <b>Open</b>. <br />The <b>Analysis rule definition</b> displays the analysis rule from the uploaded file. </li></ol> </td></tr>
</tbody>
</table>


1. Choose **Next**.

1. Under **Step 3: Review and configure**, review the selections you’ve made for the previous steps, edit if necessary, and then choose **Configure analysis rule**.

You receive a confirmation message that you’ve successfully configured an analysis rule for the table.

## Next steps
<a name="add-analysis-rule-next-step"></a>

Now that you configured an analysis rule to your configured table, you are ready to: 
+ [Associate a configured table to a collaboration](associate-configured-table.md)
+ [Query the data tables](running-sql-queries.md) (as a member who can query)