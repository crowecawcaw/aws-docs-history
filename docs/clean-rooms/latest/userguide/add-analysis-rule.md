# Adding an analysis rule to a configured table

The following sections describe how to add an analysis rule to your configured table. By
deﬁning the analysis rules, you can authorize the member who can query to run queries that match
a speciﬁc analysis rule supported by AWS Clean Rooms.

AWS Clean Rooms supports the following types of analysis rules:

- [Aggregation analysis rule](analysis-rules-aggregation.md "analysis-rules-aggregation.md")
- [List analysis rule](analysis-rules-list.md "analysis-rules-list.md")
- [Custom analysis rule in AWS Clean Rooms](analysis-rules-custom.md "analysis-rules-custom.md")
  There can be only one analysis rule per configured table. You can configure the analysis
  rule any time before you associate your configured tables with the collaboration.

###### Important

If you are using Cryptographic Computing for Clean Rooms and have encrypted data tables in the collaboration, the
analysis rule you add to the encrypted configured table should be consistent with how the data
was encrypted. For example, if you encrypted the data for SELECT (aggregation
analysis rule), you shouldn't add the analysis rule for JOIN (list analysis
rule).

###### Topics

- [Adding an aggregation analysis rule to
  a table (guided flow)](#add-agg-analysis-rule-console-wizard "#add-agg-analysis-rule-console-wizard")
- [Adding a list analysis rule to a table
  (guided flow)](#add-list-analysis-rule-console-wizard "#add-list-analysis-rule-console-wizard")
- [Adding a custom analysis rule to a table
  (guided flow)](#add-custom-analysis-rule-wizard "#add-custom-analysis-rule-wizard")
- [Adding analysis rule to a table (JSON
  editor)](#add-analysis-rule-console-json-editor "#add-analysis-rule-console-json-editor")
- [Next steps](#add-analysis-rule-next-step "#add-analysis-rule-next-step")

## Adding an aggregation analysis rule to

a table (guided flow)

The _aggregation analysis rule_ allows queries that
aggregate statistics without revealing row-level information using COUNT,
SUM, and AVG functions along optional dimensions.

This procedure describes the process of adding an aggregation analysis rule to your
configured table by using the **Guided flow** option in the AWS Clean Rooms
console.

###### Note

Configured tables using non-S3 data sources only support [custom analysis rules](#add-custom-analysis-rule-wizard "#add-custom-analysis-rule-wizard").

###### To add the aggregation analysis rule to a table (guided flow)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Tables**.
3. Choose the configured table.
4. On the configured table detail page, choose **Configure analysis
   rule**.
5. Under **Step 1: Choose analysis rule type**, under **Analysis
   rule type**, choose the **Aggregation** option.
6. Under **Creation method**, select **Guided flow**,
   and then choose **Next**.
7. Under **Step 2: Specify query controls**, for **Aggregate
   functions**:
   1. Choose an **Aggregate function** from the dropdown:
      - **COUNT**
      - **COUNT DISTINCT**
      - **SUM**
      - **SUM DISTINCT**
      - **AVG**

   2. Choose which columns can be used in the **Aggregate function**
      from the **Columns** dropdown.
   3. (Optional) Choose **Add another function** to add another
      aggregate function and associate one or more columns to that function.

   ###### Note

   At least one aggregate function is required. 4. (Optional) Choose **Remove** to remove an aggregate
   function.

8. For **Join controls**,
   1. Choose one option for **Allow table to be queried by
      itself**:

   | If you choose...                    | Then ...                                                                                   |
   | ----------------------------------- | ------------------------------------------------------------------------------------------ |
   | **No, only overlap can be queried** | The table can be queried only when joined to a table owned by the member<br>who can query. |
   | **Yes**                             | The table can be queried by itself or when joined to other<br>tables.                      |
   2. Under **Specify join columns**, choose the columns that you want
      to allow to be used in the INNER
      JOIN statement.

   This is _optional_ if you have selected
   **Yes** in the previous step. 3. Under **Specify allowed operators for matching**, choose which,
   if any, operators can be used for matching on multiple join columns. If you select two
   or more JOIN columns, one of these operators is required.

   | If you choose... | Then ...                                                                                                                                                                              |
   | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **AND**          | You can include `AND` in the `INNER JOIN` match<br>conditions to join one column to another column between tables.                                                                    |
   | **OR**           | You can include `OR` in the `INNER JOIN` match<br>conditions to combine multiple column matches between tables. This logical<br>operator is useful for obtaining a higher match rate. |

9. _(Optional)_ For **Dimension
   controls**, in the **Specify dimension columns** dropdown,
   choose which columns you want to allow to be used in the SELECT statement, and the
   WHERE, GROUP
   BY, and ORDER
   BY parts of the query.

###### Note

Aggregate function or join columns can’t be used as **Dimension**
columns. 10. For **Scalar functions**, choose one option for **Which
scalar functions do you want to allow?**

| If you choose...                               | Then ...                                                                                                                                                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **All currently supported by AWS Clean Rooms** | You allow all scalar functions currently supported by AWS Clean Rooms.<br>• You can choose **View list** to see the entire list of<br>**Scalar functions supported in AWS Clean Rooms**. |
| **A custom list**                              | You can customize which scalar functions to allow.<br>• Choose one or more options from the \*_Specify allowed scalar<br>functions_<br>• dropdown.                                       |
| **None**                                       | You don't want to allow any scalar functions.                                                                                                                                            |

For more information, see [Scalar functions](analysis-rules-aggregation.md#scalar-functions "analysis-rules-aggregation.md#scalar-functions"). 11. Choose **Next**. 12. Under **Step 3: Specify query results controls**, for
**Aggregation constraints**:

    1. Select the dropdown list for each **Column name**.
    2. Select the dropdown list for each **Minimum number of distinct
     values** that must be met for each output row to be returned, after the
     COUNT DISTINCT function is applied to it.
    3. Choose **Add constraint** to add more aggregation
     constraints.
    4. (Optional) Choose **Remove** to remove an aggregation
     constraint.

13. For **Additional analyses applied to output**, select an option based
    on your goal.

| Your goal                                                                                                                                                                                                            | Recommended option |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Allow only direct queries on this table. Deny additional analyses from being<br>run on query results. The table can only be used for direct querying.                                                                | **Not allowed**    |
| Allow but don’t require both direct queries and additional analyses on this<br>table.                                                                                                                                | **Allowed**        |
| Require that the table can only be used in direct queries that are processed<br>with one of the required additional analyses. Direct queries on this table must be<br>further processed before they can be returned. | **Required**       |

14. Choose **Next**.
15. Under **Step 4: Review and configure**, review the selections you’ve
    made for the previous steps, edit if necessary, and then choose **Configure
    analysis rule**.

You see a confirmation message that you’ve successfully configured an aggregation analysis
rule to the table.

## Adding a list analysis rule to a table

(guided flow)

The _list analysis rule_ allows queries that output
row-level lists of the overlap between the associated table and a table of the member who can
query.

This procedure describes the process of adding the list analysis rule to your configured
table using the **Guided flow** option in the AWS Clean Rooms console.

###### Note

Configured tables using non-S3 data sources only support [custom analysis rules](#add-custom-analysis-rule-wizard "#add-custom-analysis-rule-wizard").

###### To add a list analysis rule to a table (guided flow)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Tables**.
3. Choose the configured table.
4. On the configured table detail page, choose **Configure analysis
   rule**.
5. Under **Step 1: Choose analysis rule type**, under **Analysis
   rule type**, choose the **List** option.
6. Under **Creation method**, select **Guided flow**,
   and then choose **Next**.
7. Under **Step 2: Specify query controls**, for **Join
   controls**:
   1. Under **Specify join columns**, choose the columns that you want
      to allow to be used in the INNER
      JOIN statement.
   2. Under **Specify allowed operators for matching**, choose which,
      if any, operators can be used for matching on multiple join columns. If you select two
      or more JOIN columns, one of these operators is required.

   | If you choose... | Then ...                                                                                                                                                                              |
   | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **AND**          | You can include `AND` in the `INNER JOIN` match<br>conditions to join one column to another column between tables.                                                                    |
   | **OR**           | You can include `OR` in the `INNER JOIN` match<br>conditions to combine multiple column matches between tables. This logical<br>operator is useful for obtaining a higher match rate. |

8. _(Optional)_ For **List controls**,
   in the **Specify list columns** dropdown, choose which columns you want
   to allow to be used in the query output (that is, used in the SELECT
   statement), or used to filter results (that is, the WHERE
   statement).
9. Choose **Next**.
10. Under **Step 3: Specify query results controls**, for
    **Additional analyses applied to output**, select an option based on
    your goal.

| Your goal                                                                                                                                                                                                            | Recommended option |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Allow only direct queries on this table. Deny additional analyses from being<br>run on query results. The table can only be used for direct querying.                                                                | **Not allowed**    |
| Allow but don’t require both direct queries and additional analyses on this<br>table.                                                                                                                                | **Allowed**        |
| Require that the table can only be used in direct queries that are processed<br>with one of the required additional analyses. Direct queries on this table must be<br>further processed before they can be returned. | **Required**       |

11. Under **Step 4: Review and configure**, review the selections you’ve
    made for the previous steps, edit if necessary, and then choose **Configure
    analysis rule**.

You see a confirmation message that you’ve successfully configured a list analysis rule
for the table.

## Adding a custom analysis rule to a table

(guided flow)

The custom analysis rule enables custom SQL queries or PySpark jobs on a configured table.
The custom analysis rule is required if you're using:

- [Analysis templates](create-analysis-template.md "create-analysis-template.md") to allow a specific
  set of pre-approved SQL queries or PySpark jobs or a specific set of accounts that can
  provide queries that use your data.
- [AWS Clean Rooms Differential Privacy](differential-privacy.md "differential-privacy.md") to protect against user-identification attempts.
- Non-S3 data sources, such as Amazon Athena or Snowflake.

This procedure describes the process of adding the custom analysis rule to your configured
table using the **Guided flow** option in the AWS Clean Rooms console.

###### To add a custom analysis rule to a table (guided flow)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Tables**.
3. Choose the configured table.
4. On the configured table detail page, choose **Configure analysis
   rule**.
5. Under **Step 1: Choose analysis rule type**, under **Analysis
   rule type**, choose the **Custom** option.
6. Under **Creation method**, select **Guided flow**,
   and then choose **Next**.
7. Under **Step 2: Specify analysis controls**, for **Direct
   analysis controls**, choose an option based on your goal.

| Your goal                                                                                         | Recommended action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Review each new analysis before it is allowed to be run on this configured<br>table               | 1. Under **Analysis templates allowed to be run**, choose<br>**Add analysis template**.<br>2. Choose the appropriate **Collaboration\*<br>• and the<br>**Analysis template\*<br>• from the dropdown lists.<br>3. Choose **Next**.                                                                                                                                                                                                                                                                                           |
| Allow specific collaborators to run any analyses of a chosen type without<br>review on this table | 1. Under **Analysis type**,<br>1. Choose **Any query\*<br>• to allow any query created by<br>the AWS account you specify.<br>2. Choose **Any query*<br>• to allow any job created by<br>the AWS account you specify.<br>2. Under **AWS accounts allowed to create any<br>analysis**, choose **Add AWS account**.<br>3. Enter an AWS account or choose the an **AWS account<br>ID**. from the dropdown list.<br>4. (Optional) Choose \*\*Add another AWS account*<br>• to add<br>another AWS account.<br>5. Choose **Next**. |

8. Under **Step 3: Specify analysis results controls**,
   1. For **Job results controls**, note that no additional results
      controls are supported.
   2. Under **Query results controls**, for **Columns not
      allowed in output**, choose the columns you want to be allowed in the query
      output, based on your goal.

   | Your goal                                                     | Recommended action                                                                                                                    |
   | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
   | Allow all columns to be returned in query outputs             | 1. Choose **None**<br>2. Proceed to **Additional analyses applied to<br>output**.                                                     |
   | Disallow certain columns from being returned in query outputs | 1. Choose **Custom list**<br>2. Under **Specify disallowed columns**, choose the<br>columns that you want removed from query outputs. |
   3. For **Additional analyses applied to output** choose whether
      additional analyses can be applied to the query output, based on your goal.

   | Your goal                                                                                                                                                                                                                   | Recommended option |
   | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
   | • Allow only direct queries on this table.<br>• Deny additional analyses from being run on query results.<br>• The table can only be used for direct querying.                                                              | **Not allowed**    |
   | Allow but don’t require both direct queries and additional analyses on<br>this table.                                                                                                                                       | **Allow**          |
   | • Require that the table can only be used in direct queries that are<br>processed with one of the required additional analyses.<br>• Direct queries on this table must be further processed before they<br>can be returned. | **Required**       |
   4. Choose **Next**.

9. (Optional) Under **Step 4: Set differential privacy**, determine
   whether you want differential privacy turned on or off.

Differential privacy is a mathematically-proven technique to protect your data from
re-identification attacks.

###### Note

AWS Clean Rooms Differential Privacy is only available for collaborations where the data is stored in Amazon S3.

For **Differential privacy**, choose whether to turn differential
privacy on or off, based on your goal.

| Your goal                                                                                                      | Recommended action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • You don't require protection against re-identification attempts<br>• Your table doesn't have user-level data | 1. Choose **Turn off**.<br>2. Choose **Next**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| • You require protection against re-identification attempts<br>• Your table has user-level data                | 1. Choose **Turn on**.<br>2. Select the **User identifier column\*<br>• that contains the<br>unique identifier of your users, such as the `user_id` column,<br>whose privacy you want to protect.<br>To turn on differential privacy for two or more tables in a<br>collaboration, you must configure the same column as the **User<br>identifier column\*<br>• in both analysis rules to maintain a<br>consistent definition of users across tables. In case of a misconfiguration,<br>the member who can query receives an error message that there are two<br>columns to choose from in order to compute the number of user contributions<br>(for example, the number of ad impressions made by a user) while running the<br>query.<br>3. Choose **Next**. |

10. Under **Step 5: Review and configure**, review the selections you’ve
    made for the previous steps, edit if necessary, and then choose **Configure
    analysis rule**.

You see a confirmation message that you’ve successfully configured a custom analysis rule
for the table.

## Adding analysis rule to a table (JSON

editor)

The following procedure shows how to add an analysis rule to a table using the
**JSON editor** option in the AWS Clean Rooms console.

###### Note

Configured tables using non-S3 data sources only support [custom analysis rules](#add-custom-analysis-rule-wizard "#add-custom-analysis-rule-wizard").

###### To add an aggregation, list, or custom analysis rule to a table (JSON editor)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Tables**.
3. Choose the configured table.
4. On the configured table detail page, choose **Configure analysis
   rule**.
5. Under **Step 1: Choose analysis rule type**, under **Analysis
   rule type**, choose either the **Aggregation**,
   **List**, or **Custom** option.
6. Under **Creation method**, select **JSON editor**,
   and then choose **Next**.
7. Under **Step 2: Specify controls**, you can choose to insert a query
   structure (**Insert template**) or insert a file (**Import from
   file**).

| If you choose...     | Then ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Insert template**  | 1. Specify the parameters for the selected analysis rule in the<br>**Analysis rule definition**.<br>2. You can press **Ctrl\*<br>• + **Spacebar\*\*<br>to enable auto-complete.<br>For more information about aggregation analysis rule parameters, see [Aggregation analysis rule<br>• query controls](analysis-rules-aggregation.md#agg-query-controls "analysis-rules-aggregation.md#agg-query-controls").<br>For more information about list analysis rule parameters, see [List analysis rule<br>• query controls](analysis-rules-list.md#parameters-list-query-controls "analysis-rules-list.md#parameters-list-query-controls"). |
| **Import from file** | 1. Select your JSON file from your local drive.<br>2. Choose **Open**.<br>The \*_Analysis rule definition_<br>• displays the analysis<br>rule from the uploaded file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

8. Choose **Next**.
9. Under **Step 3: Review and configure**, review the selections you’ve
   made for the previous steps, edit if necessary, and then choose **Configure
   analysis rule**.

You receive a confirmation message that you’ve successfully configured an analysis rule
for the table.

## Next steps

Now that you configured an analysis rule to your configured table, you are ready to:

- [Associate a configured table to a
  collaboration](associate-configured-table.md "associate-configured-table.md")
- [Query the data tables](running-sql-queries.md "running-sql-queries.md") (as a member who can
  query)
