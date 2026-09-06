

# Save and re-run CloudWatch Logs Insights queries
<a name="CWL_Insights-Saving-Queries"></a>

After you create a query, you can save it, and run it again later. Queries are saved in a folder structure, so you can organize them. You can save as many as 1000 queries per region and per account.

Queries are saved on a Region-specific level, not a user-specific level. If you create and save a query, other users with access to CloudWatch Logs in the same Region can see all saved queries and their folder structures in the Region.

To save a query, you must be logged into a role that has the permission `logs:PutQueryDefinition`. To see a list of your saved queries, you must be logged into a role that has the permission`logs:DescribeQueryDefinitions`.

**Note**  
You can create and save queries with parameters — reusable templates with named placeholders. Instead of saving multiple variations of the same query with different values, create one template and provide different parameter values when you run it. This functionality is currently supported for queries using Logs Insights query language only. For more information, see [Using saved queries with parameters](#CWL_Insights-Parameterized-Queries).

------
#### [ Console ]

**To save a query**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Logs Insights**.

1. In the query editor, create a query.

1. Choose **Save**.

1. Enter a name for the query.

1. (Optional) Choose a folder where you want to save the query. Select **Create new** to create a folder. If you create a new folder, you can use slash (/) characters in the folder name to define a folder structure. For example, naming a new folder **folder-level-1/folder-level-2** creates a top-level folder called **folder-level-1**, with another folder called **folder-level-2** inside that folder. The query is saved in **folder-level-2**.

1. (Optional) Change the query's log groups or query text.

1. (Optional) To use parameters in your query, follow these additional steps:

   1. **Add parameters to your query.** Replace static values with placeholders using the `{{parameter}}` syntax (double braces before and after the parameter name).

      Example: Original query with static values:

      ```
      fields @timestamp, @message
      | filter level = "Error"
      | filter applicationName = "OrderService"
      ```

      Updated query with parameters:

      ```
      fields @timestamp, @message
      | filter level = {{logLevel}}
      | filter applicationName = {{applicationName}}
      ```

   1. **Define the parameters used in your query.** For each placeholder parameter, specify:
      + **Name**: Must exactly match the placeholder name (for example, `logLevel`, `applicationName`).
      + **Default value** (optional): The value to use if no parameter value is provided.
      + **Description** (optional): Explains the parameter's purpose.

   1. Queries with parameters can be run by using the query name with a `$` prefix and passing the parameter names as key-value pairs. See **To run a saved query** for details.

1. Choose **Save**.

------
#### [ AWS CLI ]

**To save a query**, use `put-query-definition`:

```
aws logs put-query-definition \
  --name "ErrorsByLevel" \
  --query-string "fields @timestamp, @message | filter level = \"ERROR\"" \
  --log-group-names "/aws/lambda/my-function" \
  --region us-east-1
```

(Optional) To save a query with parameters, add the `--parameters` option and use `{{parameterName}}` placeholders in the query string:

```
aws logs put-query-definition \
  --name "ErrorsByLevel" \
  --query-string "fields @timestamp, @message | filter level = {{logLevel}} | filter applicationName = {{applicationName}}" \
  --parameters '[{"name":"logLevel","defaultValue":"ERROR","description":"Log level to filter"},{"name":"applicationName","defaultValue":"OrderService","description":"Application name to filter"}]' \
  --log-group-names "/aws/lambda/my-function" \
  --region us-east-1
```

To save a query in a folder, prefix the query name with the folder path:

```
aws logs put-query-definition \
  --name "my-folder/ErrorsByLevel" \
  --query-string "fields @timestamp, @message | filter level = {{logLevel}}" \
  --parameters '[{"name":"logLevel","defaultValue":"ERROR","description":"Log level to filter"}]' \
  --log-group-names "/aws/lambda/my-function" \
  --region us-east-1
```

------
#### [ API ]

**To save a query**, call [PutQueryDefinition](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.html):

```
{
  "name": "ErrorsByLevel",
  "queryString": "fields @timestamp, @message | filter level = \"ERROR\"",
  "logGroupNames": ["/aws/lambda/my-function"]
}
```

(Optional) To save a query with parameters, include the `parameters` field and use `{{parameterName}}` placeholders in the query string:

```
{
  "name": "ErrorsByLevel",
  "queryString": "fields @timestamp, @message | filter level = {{logLevel}} | filter applicationName = {{applicationName}}",
  "logGroupNames": ["/aws/lambda/my-function"],
  "parameters": [
    {
      "name": "logLevel",
      "defaultValue": "ERROR",
      "description": "Log level to filter"
    },
    {
      "name": "applicationName",
      "defaultValue": "OrderService",
      "description": "Application name to filter"
    }
  ]
}
```

------

**Tip**  
 You can create a folder for saved queries with `PutQueryDefinition`. To create a folder for your saved queries, use a forward slash (/) to prefix your desired query name with your desired folder name: `<{{folder-name}}>/<{{query-name}}>`. For more information about this action, see [PutQueryDefinition](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.html). 

------
#### [ Console ]

**To run a saved query**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Logs Insights**.

1. On the right, choose **Queries**.

1. Select your query from the **Saved queries** list. The query text appears in the query editor.

1. (Optional) To use a query with parameters:

   1. Choose the **\+** icon next to the query name in the **Saved queries** side panel.

   1. The query with parameters appears in the query editor. For example, if you choose the **\+** icon next to `ErrorsByLevel`, the query editor is populated with: `$ErrorsByLevel(level=, applicationName=)`

   1. Provide the values for the parameters (level, applicationName) and run the query. For example: `$ErrorsByLevel(level= "ERROR", applicationName= "OrderService")`

1. Choose **Run**.

------
#### [ AWS CLI ]

**To run a saved query with parameters**

Use `start-query` with the `$QueryName()` syntax:

```
aws logs start-query \
  --log-group-names "/aws/lambda/my-function" \
  --start-time 1707566400 --end-time 1707570000 \
  --query-string '$ErrorsByLevel(level= "ERROR", applicationName= "OrderService")' \
  --region us-east-1
```

------
#### [ API ]

**To run a saved query with parameters**

Call [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html) with the `$QueryName()` syntax in the `queryString` field:

```
{
  "logGroupNames": ["/aws/lambda/my-function"],
  "startTime": 1707566400,
  "endTime": 1707570000,
  "queryString": "$ErrorsByLevel(level=\"ERROR\", applicationName= \"OrderService\")"
}
```

------

**To save a new version of a saved query**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Logs Insights**.

1. On the right, choose **Queries**.

1. Select your query from **Saved queries** list. It appears in the query editor.

1. Modify the query. If you need to run it to check your work, choose **Run query**.

1. When you are ready to save the new version, choose **Actions**, **Save as**.

1. Enter a name for the query.

1. (Optional) Choose a folder where you want to save the query. Select **Create new** to create a folder. If you create a new folder, you can use slash (/) characters in the folder name to define a folder structure. For example, naming a new folder **folder-level-1/folder-level-2** creates a top-level folder called **folder-level-1**, with another folder called **folder-level-2** inside that folder. The query is saved in **folder-level-2**.

1. (Optional) Change the query's log groups or query text.

1. Choose **Save**.

To delete a query, you must be logged in to a role that has the `logs:DeleteQueryDefinition` permission.

**To edit or delete a saved query**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Logs Insights**.

1. On the right, choose **Queries**.

1. Select your query from **Saved queries** list. It appears in the query editor.

1. Choose **Actions**, **Edit** or **Actions**, **Delete**.

## Using saved queries with parameters
<a name="CWL_Insights-Parameterized-Queries"></a>

Saved queries with parameters are reusable query templates with named placeholders. Instead of maintaining multiple copies of nearly identical queries, you can save a template and supply different parameter values when running the query. Parameters are only supported in the CloudWatch Logs Insights query language.

 **How it works** 

When saving a query, placeholders identify the values which you can provide at query execution time. Placeholders use the `{{parameterName}}` syntax. The following is an example of a saved query named `ErrorsByLevel` with two parameters `logLevel` and `applicationName`.

```
fields @timestamp, @message
| filter level = {{logLevel}}
| filter applicationName = {{applicationName}}
```

To run a saved query, you can invoke it using the query name prefixed with `$` and passing the parameter values. The CloudWatch Logs Insights query engine replaces each placeholder. If a parameter contains default values, then those values are used if no other values are provided.

```
# Run query by using query name and passing parameter values explicitly
$ErrorsByLevel(logLevel = "WARN", applicationName = "OrderService")

# Run query without specifying parameter values - default values are used in this case.
$ErrorsByLevel()
```

Saved query names containing spaces or special characters need to be enclosed with backticks:

```
$`Errors By Level`(logLevel = "WARN")
```

### Sample saved queries with parameters
<a name="CWL_Insights-Parameterized-Queries-Examples"></a>

 **Adding a result limit as a parameter** 

Query name: `ErrorsByLevel` with parameters `logLevel` (default: `"ERROR"`), `applicationName` (default: `"OrderService"`), and `maxResults` (default: `50`)

```
fields @timestamp, @message, @logStream
| filter level = {{logLevel}}
| filter applicationName = {{applicationName}}
| sort @timestamp desc
| limit {{maxResults}}
```

```
# Run the query using the query name and passing parameter values
$ErrorsByLevel(logLevel = "WARN", applicationName = "OrderService", maxResults = 100)
```

 **Using multiple saved queries with parameters** 

 The example below uses `ErrorsByLevel` and a second saved query `RecentN` which is defined as `sort @timestamp desc | limit {{count}}` (with parameter `count`, default `20`). The CloudWatch Logs Insights query engine expands each query before running it.

```
# Using multiple queries with parameters in sequence
$ErrorsByLevel(logLevel = "WARN", applicationName = "OrderService")
| $RecentN(count = 10)

# Each of the queries is expanded, resulting in the following query when it is run.
fields @timestamp, @message
| filter level = "WARN"
| filter applicationName = "OrderService"
| sort @timestamp desc
| limit 10
```

### Quotas and error handling
<a name="CWL_Insights-Parameterized-Queries-Quotas"></a>

**Note**  
Each saved query can have a maximum of 20 parameters.

The expanded query string cannot exceed 10,000 characters. Parameter names must start with a letter or underscore. A saved query cannot reference another saved query (nested invocations are not supported).


**Common errors**  

| Error | Cause | 
| --- | --- | 
| Parameters are only supported for CWLI query language | Parameters are only supported in the CloudWatch Logs Insights query language. | 
| Required parameters not found in queryString | A parameter name in `--parameters` does not have a matching `{{placeholder}}` in the query string. | 
| Parameter count exceeds the maximum of 20 | Saved queries currently only support 20 parameters. | 
| Duplicate parameter name | The query definition has duplicate parameters in `parameters`. | 

**Note**  
To create or update a saved query with parameters, you need the `logs:PutQueryDefinition` permission. To run one, you need `logs:StartQuery` and `logs:DescribeQueryDefinitions`.