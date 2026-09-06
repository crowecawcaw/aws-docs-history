

# Using the X-Ray data source
<a name="xray-using"></a>

## Query editor
<a name="xray-query-editor"></a>

 The most important field in the editor is the query type. There are four query types: 
+  Trace List (Traces in AWS) 
+  Trace Statistics 
+  Trace Analytics (Analytics in AWS) 
+  Insights 

## Trace List
<a name="xray-trace-list"></a>

 The Trace List type allows you to search for traces, which are shown in a table. Choosing the trace ID in the first column opens the trace on the right side. Notice the query field in the editor. You can write queries, filter expressions, or you can insert a single trace ID that will be shown in a trace view. For more details about filter expressions, see the [AWS X-Ray documentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-filters.html). 

**Note**  
 The trace list will show only the first 1000 traces. 

## Trace Statistics
<a name="xray-trace-statistics"></a>

 In Trace Statistics, you can see a graph and a table showing information about error, fault, throttle, success, and total count. You can use the columns field in the query editor to see only specified columns. 

## Trace Analytics
<a name="xray-trace-analytics"></a>

 In Trace Analytics, you can visualize the following tables. 
+  Root Cause 
  +  Response Time 
    +  Root Cause Service (Last service in path) 
    +  Path (multiple paths) 
  +  Error 
    +  Root Cause Service (Last service in path) 
    +  Path 
    +  Error Message 
  +  Fault 
    +  Root Cause Service (Last service in path) 
    +  Path 
    +  Error Message 
+  End-user Impact 
+  URL 
+  HTTP Status Code 

## Insights
<a name="xray-insights"></a>

 In Insights, you can see the summary table for Insights. Choosing the InsightId will take you to AWS Management console. 

## Alerting
<a name="xray-alerting"></a>

 Because X-Ray queries can return numeric data, alerts are supported. For more information, see [Grafana alerting](alerts-overview.md). 