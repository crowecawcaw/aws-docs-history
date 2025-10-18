# Use your custom data source


 After you create a data source, you can use it to query and visualize data from that source, as well as to set alarms. 
 If you used a template to create your custom data source connector or you added the tag listed in [Step 3: Attach a resource tag to the Lambda function](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-tags "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-tags"), you can follow the steps in  [Creating a graph of metrics from
 another data source](graph_a_metric.md#create-metric-graph-multidatasource "graph_a_metric.md#create-metric-graph-multidatasource") to query it. 
 You can also use the metric math function `LAMBDA` to query it, as explained in the following section. 
 For information about creating alarms on metrics from your data source, see [Create an alarm based on a connected data
 source](Create_MultiSource_Alarm.md "Create_MultiSource_Alarm.md"). 
 This topic describes how to pass arguments to your Lambda function to your custom data source.
 


## 
 How to pass arguments to your Lambda function


The recommended way for you to pass arguments to your custom data source is to use the query 
 builder in the CloudWatch console when you query the data source.


You can also use your Lambda function to retrieve data from your data source
 by using the new `LAMBDA` expression in CloudWatch metric math.



```
LAMBDA("LambdaFunctionName" [, optional-arg]*)
```

`optional-arg` is up to 20 strings, numbers, or Booleans. For example,
 `param`, `3.14`, or `true`.


###### Note

Multi-line strings are not supported by the CloudWatch data source connectors. Every line feed is
 replaced with a space when the query is executed, or when you create an alarm or a
 dashboard widget with the query. In some cases, this might make your query not
 valid.


When you use the `LAMBDA` metric math function, you can provide the function
 name (`"MyFunction"`). If your resource policy allows, you can also use a specific version of the function
 (`"MyFunction:22"`), or a Lambda function alias
 (`"MyFunction:MyAlias"`). You can't use `*`


The following are some examples of calling the `LAMBDA` function.



```
LAMBDA("AmazonOpenSearchDataSource", "MyDomain", "some-query")
```


```
LAMBDA("MyCustomDataSource", true, "fuzzy", 99.9)
```

The `LAMBDA` metric math function returns a list of time series that can be returned 
 to the requester or combined with other metric math functions. The following is an example of combining 
 `LAMBDA` with other metric math functions.



```
FILL(LAMBDA("AmazonOpenSearchDataSource", "MyDomain", "some-query"), 0)
```
