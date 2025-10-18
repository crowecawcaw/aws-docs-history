# Dashboard Body Structure and Syntax

###### Contents

* [Overall Structure](#Dashboard-Body-Overall-Structure "#Dashboard-Body-Overall-Structure")
* [Widgets Array Structure](#CloudWatch-Dashboard-Properties-Widgets-Structure "#CloudWatch-Dashboard-Properties-Widgets-Structure")
* [Variables Array Structure](#CloudWatch-Dashboard-Properties-Variables-Structure "#CloudWatch-Dashboard-Properties-Variables-Structure")
* [Properties of a Log Widget Object](#CloudWatch-Dashboard-Properties-Log-Widget-Object "#CloudWatch-Dashboard-Properties-Log-Widget-Object")
* [Properties of a Metric Widget Object](#CloudWatch-Dashboard-Properties-Metric-Widget-Object "#CloudWatch-Dashboard-Properties-Metric-Widget-Object")
* [Metric Widget: Format for Each Metric in the Array](#CloudWatch-Dashboard-Properties-Metrics-Array-Format "#CloudWatch-Dashboard-Properties-Metrics-Array-Format")
* [Properties of a Metrics Explorer Widget Object](#CloudWatch-Dashboard-Properties-Metric-Explorer-Object "#CloudWatch-Dashboard-Properties-Metric-Explorer-Object")
* [Properties of an Alarm Status Widget Object](#CloudWatch-Dashboard-Properties-Alarm-Widget-Object "#CloudWatch-Dashboard-Properties-Alarm-Widget-Object")
## Overall Structure


A `DashboardBody` is a string in JSON format. It can include an array of
 between 0 and 500 widget objects, as well as a few other parameters. The dashboard must include
 a `widgets` array, but that array can be empty.


The following is an example of this structure with one metric widget and one text widget, a time range starting six hours before the current time, 
 and each graph's period setting always being obeyed.



```
{
   "start": "-PT6H",
   "periodOverride": "inherit",
   "widgets": [
      {
         "type":"metric",
         "x":0,
         "y":0,
         "width":12,
         "height":6,
         "properties":{
            "metrics":[
               [
                  "AWS/EC2",
                  "CPUUtilization",
                  "InstanceId",
                  "i-012345"
               ]
            ],
            "period":300,
            "stat":"Average",
            "region":"us-east-1",
            "title":"EC2 Instance CPU",
            "liveData": false,
            "legend": {
                "position": "right"
              }
         }
      },
      {
         "type":"text",
         "x":0,
         "y":7,
         "width":3,
         "height":3,
         "properties":{
            "markdown":"Hello world"
         }
      }
   ]
}
```

The next example displays three Lambda per-function metrics, and uses a dashboard variable so that dashboard users
 can switch between different Lambda function names and see all three metrics for each function. This helps you create a single flexible
 dashboard that can display key metrics for different resources. In this example the functions are discovered by a metric
 search query, so the dashboard automatically discovers new Lambda functions when they are created.



```
{
    "widgets": [{
            "height": 6,
            "width": 6,
            "y": 0,
            "x": 0,
            "type": "metric",
            "properties": {
                "view": "timeSeries",
                "stacked": false,
                "metrics": ["AWS/Lambda", "Invocations", "FunctionName", "my-function-name"],

                "region": "us-east-1",
                "liveData": true
            }
        },
        {
            "height": 12,
            "width": 12,
            "y": 0,
            "x": 6,
            "type": "metric",
            "properties": {
                "view": "timeSeries",
                "stacked": false,
                "metrics": ["AWS/Lambda", "Errors", "FunctionName", "my-function-name"],

                "region": "us-east-1",
                "liveData": true
            }
        },

        {
            "height": 3,
            "width": 6,
            "y": 0,
            "x": 18,
            "type": "metric",
            "properties": {
                "view": "timeSeries",
                "stacked": false,
                "metrics": ["AWS/Lambda", "Duration", "FunctionName", "my-function-name"],

                "region": "us-east-1",
                "liveData": true
            }
        }
    ],
    "variables": [{
        "type": "property",
        "property": "FunctionName",
        "inputType": "select",
        "id": "LambdaFunction_Variable",
        "label": "Function",
        "visible": true,
        "search": "{AWS/Lambda,FunctionName} MetricName=\"Duration\"",
        "populateFrom": "FunctionName"
    }]
}
```

The next example has two widgets. The first includes two metrics and a math expression that sums their total. The second widget
 is a search expression that displays the `CPUUtilization` for all EC2 instances in the Region.



```

{
   "start": "-PT9H",
   "periodOverride": "inherit",
   "widgets": [
      {
         "type":"metric",
         "x":0,
         "y":0,
         "width":12,
         "height":6,
         "properties":{
            "metrics":[
               [ "AWS/EC2", "DiskReadBytes", "InstanceId", "i-123",{ "id": "m1" } ],
               [ ".", ".", ".", "i-abc", { "id": "m2" } ],
               [ { "expression": "SUM(METRICS())", "label": "Sum of DiskReadbytes", "id": "e3" } ]
            ],
            "view": "timeSeries",
            "stacked": false,
            "period":300,
            "stat":"Average",
            "region":"us-east-1",
            "title":"EC2 Instance CPU"
         }
      },
      {
         "type":"metric",
         "x":0,
         "y":0,
         "width":18,
         "height":9,
         "properties":{
            "metrics":[
               [ { "expression": "SEARCH('{AWS/EC2,InstanceId} MetricName=\"CPUUtilization\"', 'Average', 300)", "id": "e1" } ]
            ],
            "view": "timeSeries",
            "stacked": false,
            "region":"us-east-1",
            "title":"EC2 Instance CPU"
         }
      }
   ]
}
    
```

The rest of this section includes examples illustrating each part of the `DashboardBody` syntax. For more examples showing
 the entire command syntax, see [PutDashboard](API_PutDashboard.md "API_PutDashboard.md")
 in the Amazon CloudWatch API Reference.


The top level of the JSON object can include the following properties.




**widgets**

The list of widgets in the dashboard. For more information, see 
 [Widgets Array Structure](#CloudWatch-Dashboard-Properties-Widgets-Structure "#CloudWatch-Dashboard-Properties-Widgets-Structure").


Required: Yes



**variables**

The array of dashboard variable objects used in the dashboard. For more information about the fields that you
 can use in each dashboard variable object, see 
[Variables Array Structure](#CloudWatch-Dashboard-Properties-Variables-Structure "#CloudWatch-Dashboard-Properties-Variables-Structure").


For more information about dashboard variables, see 
 [Create flexible dashboards with dashboard variables](../monitoring/cloudwatch_dashboard_variables.md "../monitoring/cloudwatch_dashboard_variables.md").


If you include a `variables` array, it can contain between 0 and 25 variable objects.


Required: No



**end**

The end of the time range to use for each widget on the dashboard when the dashboard loads. If you specify a value for `end`, you must also
 specify a value for `start`. For each of these values, specify an absolute time in the ISO 8601 format. For example, 
 `2018-12-17T06:00:00.000Z`.


Type: String


Required: No



**start**

The start of the time range to use for each widget on the dashboard.


You can specify `start` without specifying `end`
 to specify a relative time range that ends with the current time. In this case, the value of `start` must begin with `-PT`
 if you specify a time range in minutes or hours, and must begin with `-P` if you specify a time range in days, weeks, or months.
 You can then use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, 
 `-PT5M` shows the last 5 minutes, `-PT8H` shows the last 8 hours, and `-P3M` shows the last three months.


You can also use `start` along with an `end` field, to specify an absolute time range. When specifying
 an absolute time range, use the ISO 8601 format. For example, 
 `2018-12-17T06:00:00.000Z`.


If you omit `start`, the dashboard shows the default time range when it loads.


Type: String


Required: No



**periodOverride**

Use this field to specify the period for the graphs when the dashboard loads. Specifying `auto` causes the period of 
 all graphs on the dashboard to automatically adapt to the time range of the dashboard. Specifying `inherit` ensures that
 the period set for each graph is always obeyed.


Valid Values: auto | inherit


Type: String


Required: No




## Widgets Array Structure


Each widget of any type can have the following properties.




**type**

The type of widget.


Valid Values: `metric` | `text` | `log` | `alarm` | `explorer`


Type: String


Required: Yes



**x**

The horizontal position of the widget on the 24-column dashboard grid. The default is the next available position.


Valid Values: 0–23


Type: Integer


Required: Yes, if `y` is specified. Otherwise not required.



**y**

The vertical position of the widget on the 24-column dashboard grid. The default is the next available position.


Valid Values: Any integer, 0 or higher.


Type: Integer


Required: Yes, if `x` is specified. Otherwise not required.



**width**

The width of the widget in grid units (in a 24-column grid). The default is 6.


Valid Values: 1–24


Type: Integer


Required: No



**height**

The height of the widget in grid units. The default is 6.


Valid Values: 1–1000


Type: Integer


Required: No



**properties**

The detailed properties of the widget, which differ depending on the widget type. For more 
 information about the format of `properties`, see 
 [Properties of a Metric Widget Object](#CloudWatch-Dashboard-Properties-Metric-Widget-Object "#CloudWatch-Dashboard-Properties-Metric-Widget-Object")
 or [Properties of a Text Widget Object](#CloudWatch-Dashboard-Properties-Text-Widget-Object "#CloudWatch-Dashboard-Properties-Text-Widget-Object").


Type: Object


Required: Yes




## Variables Array Structure


Each dashboard variable in the array can have the following properties.




**type**

The type of dashboard variable. CloudWatch supports two types, *property variables*
 and *pattern variables*.


Property variables change the values of all instances of a property in all widgets in the dashboard. 
 A property can be either of the following:



* Any JSON property in the widget definitions, such as `region`.
* Any dimension name for a metric, such as `InstanceId`
 or `FunctionName`.

A pattern variable changes a regular expression pattern across the dashboard JSON. Use it
 when you need to change just part of a JSON property value, or even a JSON property.


Property variables apply to most use cases and are less complex to set up.


Valid Values: `property` | `pattern`


Type: String


Required: Yes



**inputType**

Determines how the dashboard user inputs the value for the variable.



* Specify `input` to use a text box that the user can enter values into.
* Specify `select` to use a dropdown set of values that you define, or a dropdown list of 
 values found by a metric search query.
* Specify `radio` to use a set of radio buttons, with values that you 
 define or that you find with a metric search query.

Valid Values: `input` | `select` | `radio`


Type: String


Required: Yes



**values**

If your `inputType` is `select` or `radio` and you want to define
 the possible variable values instead of using a metric query search, specify those values here.


`values` is an array where each object in the array contains a required *value*
 and an optional *label*. Each *value* can be a string, number, or Boolean, 
 and each label must be a string. Each of these values and labels can be as many as 255 characters.


If you specify a `values` array it must include at least one item, and can include
 as many as 500.


For example, the following creates a list of three possible Regions to use as the values for 
 a variable.



```
"values": [
    { "label": "US East (IAD)", "value": "us-east-1" },
    { "label": "US West (SFO)", "value": "us-west-1" },
    { "label": "EU (DUB)", "value": "eu-west-1" }
]
```

Type: Array


Required: Yes if `inputType` is `select` or `radio` and you are
 not using a metric search query to populate the values.



**id**

An Id for this variable. It can be up to 32 characters, and valid characters 
 are `0-9A-Za-z-_`


Type: String


Required: Yes



**label**

A label to display for the input field. It can have as many as 30 characters.


If you omit this field for a property variable,
 the property name is displayed as the label. If you omit it for a pattern variable, then 
 ``pattern_1`, `pattern_2`, ...`
 is used for the label.


Type: String


Required: No



**defaultValue**

The default value for the variable, when the dashboard is first opened.



* If `inputType` is `input`, you specify
 the `defaultValue` here manually and use as many as 255 characters
* If `inputType` is `select` or `radio`, you must specify
 a valid possible value that you specified in the `values` array or that was retrieved
 in the metric query search.

Valid Values: Any valid value for this variable


Type: String, Number, or Boolean, depending on the type value for this variable


Required: No



**search**

Specify this field to populate your `select` or `radio` input field by using 
 a metric search expression. For the value for this field, specify a namespace, dimension name, and a metric 
 name. The dimension that you specify must be valid for that metric. CloudWatch finds all 
 resources that publish that metric and dimension, and populates the list
 with them.


For example, specify `"search": "{AWS/EC2,InstanceId} MetricName=\"CPUUtilization\""` to 
 search for Amazon EC2 instances in the account, or specify `"search": "{AWS/Lambda,FunctionName} MetricName=\"Duration\"",`
 to return the Lambda functions in the account


The `search` string that you specify can be as many as 2048 characters.


###### Note

If you're using a search expression and you also want to specify a default value,
 the default that you specify in `defaultValue` is used as long as that default is one or the resources
 that was retrieved by the search. When using a search expression to populate your input field, 
 you can also specify the special value `__FIRST` for `defaultValue`, to have 
 the default value be the first value returned from the search. (The special value includes two underscores
 and then FIRST) Values returned by the search 
 are always sorted alphabetically.


Type: String


Required: Yes if `inputType` is `select` or `radio` and you are
 not specifying `values`.



**populateFrom**

If you are using the `search` field to populate your input field by using a search expression,
 specify this field with the name of a dimension that the search will retrieve.


For example, if your `search` value is 
 `"search": "{AWS/EC2,InstanceId} MetricName=\"CPUUtilization\""`, then you can specify
 `InstanceId` for `populateFrom`.


Type: String


Required: Yes if `inputType` is `select` or `radio` and you are
 not specifying `values`.



**visible**

Specified whether the input label and field are visible on the dashboard. If you omit this, 
 the default of `true` is used.


Using `false` saves some room on the dashboard, but requires the user to 
 change the dashboard URL to change the variable values.


Type: Boolean


Required: No




### Variable examples


The following example uses a property variable for changing the Region of all widgets, using a text 
 input field. When the dashboard is first opened, the default value of `us-east-1` is used 
 for the variable.



```
"variables": [
     {
        "type": "property", 
        "property": "region",
        "inputType": "input",
        "id": "region",
        "label": "Region",
        "defaultValue": "us-east-1",
        "visible": true
    } 
],
```

The following example uses a pattern variable for changing the Region of all widgets, in the case
 where sometimes the Region is set in the middle of a string such as an ARN.



```
"variables": [
    {
        "type": "pattern",
        "pattern": "us-east-1",
        "inputType": "input",
        "id": "region",
        "label": "Region",
        "defaultValue": "us-east-1",
        "visible": true
    }
],
```

The following example generates a Lambda function variable, with a radio button for each function. Functions
 are discovered by a metric query search.



```
"variables": [
    {
        "type": "pattern",
        "pattern": "originalFuncNameInDashboard",
        "inputType": "radio",
        "id": "functionName",
        "label": "Function",
        "visible": true,
        "search": "{AWS/Lambda,FunctionName} MetricName=\"Duration\"",
        "populateFrom": "FunctionName",
        "defaultValue": "__FIRST"
    }
],
```

The following sample displays how to specify multiple variables in a dashboard, and demonstrates several 
 types of variables.



```
"variables": [{
        "type": "property",
        "property": "region",
        "inputType": "select",
        "id": "unique_id_1",
        "label": "Region",
        "defaultValue": "us-east-1",
        "visible": true,
        "values": [{
                "label": "IAD",
                "value": "us-east-1"
            },
            {
                "label": "CMH",
                "value": "us-east-2"
            },
            {
                "label": "NRT",
                "value": "ap-northeast-1"
            }
        ]
    },
    {
        "type": "property",
        "property": "FunctionName",
        "inputType": "select",
        "id": "unique_id_2",
        "label": "Function",
        "visible": true,
        "values": [{
                "value": "my-FunctionName-1"
            },
            {
                "value": "my-FunctionName-2"
            },
            {
                "value": "my-FunctionName-3"
            }
        ]
    },
    {
        "type": "property",
        "property": "accountId",
        "inputType": "radio",
        "id": "unique_id_3",
        "defaultValue": "111122223333",
        "visible": true,
        "values": [{
                "label": "IAD Account",
                "value": "111122223333"
            },
            {
                "label": "CMH Account",
                "value": "123456789012"
            },
            {
                "label": "NRT Account",
                "value": "000000000000"
            }
        ]
    }
]
```

### Properties of a Text Widget Object


A widget of type `text` can have one or two parameters in the `properties` section. The `markdown` field is required,
 and the `transparent` field is optional.


For more information about the style of markdown supported in CloudWatch text widgets, see 
 [Using Markdown in the Console](https://docs.aws.amazon.com/general/latest/gr/aws-markdown.html "https://docs.aws.amazon.com/general/latest/gr/aws-markdown.html").




**markdown**

The text to be displayed by the widget. Use this parameter only for text widgets.


Type: String


Required: Yes (when the widget `type` is `text`).



**background**

Specifies whether the text widget has a solid or transparent background. The value `transparent` makes the widget transparent. The value `solid` is the default.


Type: String


Required: No





```
{
   "widgets":[
      {
         "type":"text",
         "x":0,
         "y":7,
         "width":3,
         "height":3,
         "properties":{
            "markdown":"Hello world",
            "background": "transparent"
         }
      }
   ]
}
```

## Properties of a Log Widget Object


A widget of type `log` represents the results of a CloudWatch Logs Insights query. For more information, see
 [Analyzing Log Data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html").


A `log` widget can include the 
 following fields in its `properties` field.




**accountId**

The account ID of the AWS account containing the logs, if this is a cross-account query.


Type: String


Required: No



**region**

The Region of the logs query.


Type: String


Required: Yes



**title**

The title text to be displayed by the widget.


Type: String


Required: No



**query**

Contains the CloudWatch Logs Insights query function.


Type: String


Required: Yes (when the widget `type` is `log`).


The `query` string starts with the names of the log groups that are to be queried. You must pre-pend each 
 log group name with `SOURCE`. Separate
 multiple log groups with a pipe character (|).


Add another pipe character after the list of log groups, and then specify the query syntax. Separate each line in the query
 syntax with `\n|`


For example, the following line represents a query of two log groups, `service_log1` and `service_log2`. The query
 displays 
 canaries that have faults.



```
"query": "SOURCE 'service_log1' | SOURCE 'service_log2' |filter Fault > 0\n| fields Fault.Message\n| stats count(*) by Canary.Name, Fault.Message"
```


**view**

Specifies how the query results are displayed. Specify `table` to view the results as a table. 
 Specify `timeSeries` to display this metric as a line graph. Specify `bar` to 
 display it as a bar graph. Specify `pie` to display it as a pie graph.


If you omit this parameter, the results are displayed as a table.


Type: String


Required: No (when the widget `type` is `log`).





```
{
    "widgets": [
        {
            "type": "log",
            "x": 12,
            "y": 24,
            "width": 12,
            "height": 6,
            "properties": {
                "region": "us-east-1",
                "title": "Errors (Application Log)",
                "query": "SOURCE 'application1.log' | SOURCE 'application2.log' | filter @message like \"[ERROR]\"\n| parse \"Error for [*] [*] due to: *\" canaryName1, canaryId1, cause1\n| parse \"Executor canary [*] *\" canaryName2, cause2\n| fields coalesce(cause1, cause2) as cause\n| fields coalesce(canaryName1, canaryName2) as canaryName\n| fields ispresent(cause) as isP\n| filter isP\n| stats count() as errCount by canaryName, substr(cause, 0, 130)\n| sort errCount DESC",
                "view": "table"
            }
        }
    ]
}
```

## Properties of a Metric Widget Object


A widget of type 
 `metric` can have the following fields within `properties`:




**accountId**

Specifies the AWS account ID where all metrics in this widget will come from. This is useful for cross-account dashboards
 that include widgets from multiple accounts. For more information, see
 [Cross-Account Cross-Region CloudWatch Console](../monitoring/Cross-Account-Cross-Region.md "../monitoring/Cross-Account-Cross-Region.md").


If you omit this, the current account is used as the default. Use this
 parameter only for metric widgets.


You can also use an `accountId` field within each metric in the array of `metrics` to create 
 a single widget which includes metrics from multiple accounts.


Type: String


Required: No



**annotations**

To include an alarm or annotation in the widget, specify an `annotations` array. For more 
 information about the format, see 
 [Dashboard Widget Object: Annotation Properties](#CloudWatch-Dashboard-Properties-Annotation-Format "#CloudWatch-Dashboard-Properties-Annotation-Format"). Use this
 parameter only for metric widgets.


Type: Object


Required: An alarm annotation is required only when the widget `type` is `metric` and `metrics` is not specified.
 A horizontal or vertical annotation is not required.



**liveData**

Specify `true` to display *live data* in the widget. Live
 data is data published within the last minute that has not been fully aggregated. For more
 information, see [Use Live Data](../monitoring/cloudwatch-live-data.md "../monitoring/cloudwatch-live-data.md").


Type: Boolean


Required: No



**legend**

Specify `legend` to determine where the legend for the lines
 on the graph is displayed. The `legend` field contains another 
 field called `position`. Possible values for `position`
 are `right`, `bottom`, and `hidden`.


For example, the following causes the legend to appear on the right
 in the graph.



```
"legend": {
     "position": "right"
}
```

Type: Object


Required: No



**metrics**

Specify a `metrics` array to include one or more metrics (without alarms), a Metrics Insights
 query, math expressions, or search expressions. 
 One `metrics` array can include
 0–500 metrics and expressions. Use this parameter only for metric widgets. For more
 information about the format of `metrics`, see [Metric Widget: Format for Each Metric in the Array](#CloudWatch-Dashboard-Properties-Metrics-Array-Format "#CloudWatch-Dashboard-Properties-Metrics-Array-Format").


One metrics array can include no more than one Metrics Insights query.


A single `expression` field can't include both a Metrics Insights query and
 a math expression, but you can use the returned results of a Metrics Insights query from one 
 expression as input in a math expression in a different expression in the array.


Type: Array of arrays


Required: Yes, when the widget `type` is `metric` and `annotations` is not specified.



**period**

The default period, in seconds, for all metrics in this widget. The period is the length of time represented by one
 data point on the graph. This default can be overridden within each metric definition.
 Use this parameter only for metric widgets. The default is 300.


Valid Values: Any multiple of 60, with 60 as the minimum.


Type: Integer


Required: No



**region**

The region of the metric.


Type: String


Required: Yes



**sparkline**


 Specify `true` 
 to display the sparkline feature
 under the number widget.
 Specify `false` 
 to display the number widget 
 by itself. 
 This parameter is ignored 
 if view is not `singleValue`. 
 Use this parameter only for metric widgets. 
 



 Type: Boolean
 



 Required: No
 



**stacked**

Specify `true` to display the graph as a stacked line, or `false` to 
 display as separate lines. This parameter is ignored if `view` is `singleValue`. Use 
 this parameter only for metric widgets. 


Type: Boolean


Required: No



**stat**

The default statistic to be displayed for each metric
 in the array. This 
 default can be overridden within the definition of each individual metric in 
 the `metrics` array. Use this parameter only for metric widgets.


Valid Values: `SampleCount` | `Average` | `Sum` | `Minimum` | `Maximum` | 
 `p`??``


Type: String that is a valid CloudWatch statistic.


Required: No



**table**

Include a `table` section to include data table-related changes in the widget. For more information about the 
 format, see [Dashboard Widget Object: Table Properties](#CloudWatch-Dashboard-Properties-Table "#CloudWatch-Dashboard-Properties-Table").


Type: Object


Required: No



**timezone**

The time zone to use for displaying the times in the graph. The format is
 + or - followed by four digits. The first two digits indicate the number of
 hours ahead or behind of UTC, and the final two digits are the number of
 minutes. For example, `+0130` indicates a time 1 hour and 30
 minutes ahead of UTC. The default is `+0000`.


Type: String


Required: No



**title**

The title to be displayed for the graph or number. Use 
 this parameter only for metric widgets.


Type: String


Required: No



**view**


 Specify `timeSeries` 
 to display this metric 
 as a line or stacked area graph.
 Specify `singleValue` 
 to display this metric
 as a number graph.
 Specify `gauge` 
 to display this metric
 as a gauge graph.
 Specify `bar` 
 to display this metric
 as a bar graph.
 Specify `pie` to display this metric
 as a pie graph.
 


###### Note


 If you specify `gauge`,
 you must set a value 
 for `min` and `max`
 on the left side 
 of `yAxis`.
 


Valid Values: `timeSeries` | `singleValue` | `gauge` | `bar` | `pie` | `table`


Type: String


Required: No



**yAxis**


 The minimum and maximum values 
 for the left and right side 
 of a graph's Y-axis.
 This property applies 
 to all graphed metrics, 
 except
 for specific metrics 
 that override this setting.
 For more information, 
 see [Dashboard Widget Object: yAxis Properties Format](#CloudWatch-Dashboard-Properties-YAxis-Properties-Format "#CloudWatch-Dashboard-Properties-YAxis-Properties-Format").
 


Type: yAxis object


Required: No




**Example: Stacked area and gauge widgets**



```
{
    "widgets": [
{
   "type":"metric",
   "x":0,
   "y":0,
   "width":12,
   "height":6,
   "properties":{
      "metrics":[
         [
            "AWS/EC2",
            "CPUUtilization",
            "InstanceId",
            "i-012345"
         ],
         [
            "AWS/EC2",
            "NetworkIn",
            "InstanceId",
            "i-012345",
            {
               "yAxis":"right",
               "label":"NetworkIn",
               "period":3600,
               "stat":"Maximum"
            }
         ]
      ],
      "period":300,
      "stat":"Average",
      "region":"us-east-1",
      "timezone":"+0300",
      "title":"EC2 Instance CPU",
      "stacked":true,
      "view":"timeSeries",
      "liveData":false,
      "yAxis":{
         "left":{
            "min":0,
            "max":100
         },
         "right":{
            "min":50
         }
      },
      "annotations":{
         "horizontal":[
            {
               "visible":true,
               "color":"#9467bd",
               "label":"Critical range",
               "value":20,
               "fill":"above",
               "yAxis":"right"
            }
         ]
      }
   },
{
   "type": metric, 
   "x": 18,
   "y"; 60,
   "width": 6, 
   "height": 6,
   "properties": {
      "metrics": [
         [ 
         "AWSLogsShrinkRay",
         "disk_inodes_used",
         "path", 
         "/dev/shm",
         "InstanceId",
         "i-012345",
         "AutoScalingGroupName",
         "ShrinkRayExecutorResourceStack-Gamma-us-east-1-ASGuseast1ac48xlargeASGB9B53974-VTYXJUZGUAHV",
         "InstanceType",
         "c4.8xlarge",
         "device",
         "tmpfs",
         "fstype",
         "tmpfs" 
         ]
         ],
      "view": "gauge", 
      "title": "Disk Inodes Used"
      "region": "us-east-1",
      "yAxis": {
         "left": {
            "min": 0, 
            "max": 100,
         }        
       }
     }
   }

```

## Metric Widget: Format for Each Metric in the Array


Each item in the `metrics` array is either a single metric or a math expression or search expression. Each single metric in the `metrics` array has the following format:



```
[ `Namespace`, `MetricName`, [{`DimensionName`,`DimensionValue`}...] {`Rendering Properties Object`} ]
```

Each expression in the `metrics` array has the following format:



```
[ {"expression" : "`expression`", ["label" : "`label`"] , ["id" : "`id`"] } ]
```



**accountId**

Specifies the AWS account ID where this metric comes from. This enables you to create a widget that 
 contains metrics from multiple accounts on a cross-account dashboard. For more information, see
 [Cross-Account Cross-Region CloudWatch Console](../monitoring/Cross-Account-Cross-Region.md "../monitoring/Cross-Account-Cross-Region.md").


If you omit this, the current account is used as the default. Use this
 parameter only for metric widgets.


Type: String


Required: No



**Namespace**

The AWS namespace containing the metric. If you have multiple entries in
 the `metrics` array, for each one after the first you may specify
 only `"."` to use the same namespace as the previous metric in
 the array.


Type: String


Required: Yes



**MetricName**

The name of the CloudWatch metric. If you have multiple entries in the
 `metrics` array, for each one after the first you may specify
 only `"."` to use the same metric name as the previous metric in
 the array.


Type: String


Required: Yes, for a single metric



**expression**

The Metrics Insights query, math expression, or search expression, if this is an expression 
 instead of a single metric.


In a search expression using double-quotes for an exact match, each double-quote mark must be escaped with a backslash.


For more information about Metrics Insights query syntax, 
 see 
[Metrics Insights query components and syntax](../monitoring/cloudwatch-metrics-insights-querylanguage.md "../monitoring/cloudwatch-metrics-insights-querylanguage.md").


For more information about math expressions or search expressions, see
 [Using Metric Math](../monitoring/using-metric-math.md "../monitoring/using-metric-math.md") or [Using Search Expressions in Graphs](../monitoring/using-search-expressions.md "../monitoring/using-search-expressions.md") in the Amazon CloudWatch User Guide.
 


Type: String


Required: Yes, for an expression


Example of an expression for a Metrics Insights query:



```
[ { "expression": "SELECT MAX(CPUUtilization) FROM SCHEMA(\"AWS/EC2\", InstanceId) GROUP BY InstanceId LIMIT 10", "label": "View the 10 max CPU Utilization", "id": "q1" } ]
```


**DimensionName**

The name of a dimension to further refine what data is shown. If you have
 multiple entries in the `metrics` array, for each one after the
 first you may specify only `"."` to use the same dimension name
 as in the corresponding dimension specified in the previous metric in the
 array. You may specify 0 dimensions for a metric, or up to as many
 dimensions as the metric support.


Type: String


Required: No



**DimensionValue**

The value to use for that dimension for the metric. Required if there is a corresponding dimension name.


Type: String


Required: No



**id**

The Id of this time series. This Id can be used as part of a math expression. The Id must start with a lowercase letter.


Type: String


Required: No



**label**

The label to display in the graph to represent this time series.


Type: String


Required: No



**region**

The region of the metric. Use this parameter only for metric widgets. If you omit this, the current Region is used
 as the default.


Type: String


Required: No



**Rendering Properties Object**

Specifies rendering properties to be used for this particular metric, overriding the 
 values specified for the overall widget. For more 
 information about the format, see 
 [Dashboard Widget Object: Rendering Properties Object Format](#CloudWatch-Dashboard-Properties-Rendering-Object-Format "#CloudWatch-Dashboard-Properties-Rendering-Object-Format"). 


Type: Metric Render Properties Object


Required: No





```
// The simplest example, a metric with no dimensions
        [ "AWS/EC2", "CPUUtilization" ]
        
 // A metric with a single dimension
        [ "AWS/EC2", "CPUUtilization", "InstanceId", "i-012345" ]
        
 // A metric with a single dimension and rendering properties
        [ "AWS/EC2", "DiskReadBytes", "InstanceId", "i-xyz", { "yAxis": "right"} ]
       
 // The following example graphs the `DiskReadBytes` metric for three instances.
        [ "AWS/EC2", "DiskReadBytes", "InstanceId", "i-xyz" ],
        [ ".", ".", ".", "i-abc" ],
        [ ".", ".", ".", "i-123" ]
       
 // The following example includes two metrics and a math expression to sum them.
        [ "AWS/EC2", "DiskReadBytes", "InstanceId", "i-123",{ "id": "m1" } ],
        [ ".", ".", ".", "i-abc", { "id": "m2" } ],
        [ { "expression": "SUM(METRICS())", "label": "Sum of DiskReadbytes", "id": "e3" } ]
       
  // The following example is a search expression showing the EC2 `CPUUtilization` for each instance in the Region.
        [ { "expression": "SEARCH('{AWS/EC2,InstanceId} MetricName=\"CPUUtilization\"', 'Average', 300)", "id": "e1" } ],

```

###### Topics

* [Dashboard Widget Object: Rendering Properties Object Format](#CloudWatch-Dashboard-Properties-Rendering-Object-Format "#CloudWatch-Dashboard-Properties-Rendering-Object-Format")
* [Dashboard Widget Object: Annotation Properties](#CloudWatch-Dashboard-Properties-Annotation-Format "#CloudWatch-Dashboard-Properties-Annotation-Format")
* [Dashboard Widget Object: yAxis Properties Format](#CloudWatch-Dashboard-Properties-YAxis-Properties-Format "#CloudWatch-Dashboard-Properties-YAxis-Properties-Format")
* [Dashboard Widget Object: Table Properties](#CloudWatch-Dashboard-Properties-Table "#CloudWatch-Dashboard-Properties-Table")

### Dashboard Widget Object: Rendering Properties Object Format


Each metric in the `metrics` array can optionally have custom rendering
 properties that override the default rendering properties specified in the
 `yAxis` parameter of the `widget` object. This section
 describes the format for those per-metric custom rendering properties.




**color**

The six-digit HTML hex color code to be used for this metric.


Type: String


Required: No



**label**

The label to display for this metric in the graph legend. If this is
 not specified, the metric is given an autogenerated label that
 distinguishes it from the other metrics in the widget.


Type: String


Required: No



**period**

The period for this metric, in seconds. The period is the length of time represented by one
 data point on the graph. 


Valid Values: A multiple of 60, with a minimum of 60.


Type: Integer


Required: No



**stat**

The statistic for this metric, if it is to be different than the statistic used for the 
 other metrics in the array. By default CloudWatch uses *Average* if you don't specify a statistic at array or at metric level.


Valid Values: `SampleCount` | `Average` | `Sum` | `Minimum` | `Maximum` |
 `p`??``


Type: String that is a valid CloudWatch statistic.


Required: No



**visible**

Set this to `true` to have the metric appear in the graph, or `false` to have it be hidden. The default
 is `true`.


Type: Boolean


Required: No



**yAxis**

Where on the graph to display the y-axis for this metric. The default is `left`.


Valid Values: `left` | `right`


Type: String


Required: No





```

       
 // The third metric has its own rendering properties, overriding those of the rest of the widget.
        [ "AWS/EC2", "DiskReadBytes", "InstanceId", "i-xyz" ],
        [ ".", ".", ".", "i-abc" ],
        [ ".", ".", ".", "i-123", { "label":"Instance i-123", "yAxis": "right"}  ]
```

### Dashboard Widget Object: Annotation Properties


Annotations include alarms, horizontal annotations, and vertical annotations. A single metric widget can
 have up to one alarm, or it can have one or more horizontal or vertical annotations. A single widget can't 
 have both an alarm and horizontal or vertical annotations.


#### Alarm Annotations


If you
 specify an alarm annotation, you cannot also specify a `metrics` array in the same widget.




**alarms**

The Amazon Resource Name (ARN) of the alarm.


Type: Array of strings. There can be 0–1 strings in the
 array.


Required: Only if no metrics are listed.





```
                
"annotations": {
   "alarms": [ "`arn1`" ]
}
            
```

#### Horizontal Annotations




**horizontal**

An array of horizontal annotations. Horizontal annotations have several options for fill shading, including shading above the
 annotation line, shading below the annotation line, and "band" shading that appears between two linked annotation lines
 as part of a single band annotation. Each horizontal annotation in the array that is a single annotation, instead
 of a band annotation, has the following format:



```
{`value`, `label`, `color`, `fill`, `yAxis`, `visible`}
```

Each horizontal annotation that is a band annotation has the following format:



```
[ {`value`, `label`, `color`, `yAxis`, `visible`}, {`value`, `label`} ]
```





**value**

The metric value in the graph where the horizontal annotation line is to appear. On a band shading annotation, the two values
 for Value define the upper and lower edges of the band.


On a graph with horizontal annotations, the graph is scaled so that all visible horizontal annotations appear on the graph. 


Type: Float


Required: Yes



**label**

A string that appears on the graph next to the annotation.


Type: String


Required: No



**color**

The six-digit HTML hex color code to be used for the annotation. This color is used for both the annotation line and the fill shading.


Type: String


Required: No



**fill**

How to use fill shading with the annotation. Valid values are
 `above` for shading above the annotation,
 `below` for shading below the annotation, and
 `none` for no shading. If `fill` is
 omitted, there is no shading.


The exception is an annotation with band shading. These annotations always have shading between the two values, and any value for `fill`
 is ignored.


Type: String


Required: No



**visible**

Set this to `true` to have the annotation appear in the graph, or `false` to have it be hidden. The default
 is `true`.


Type: Boolean


Required: No



**yAxis**

If the graph includes multiple metrics, specifies whether the numbers
 in `Value` refer to the metric associated with the left
 Y-axis or the right Y-axis, . Valid values are `right`
 and `left`.


Type: String


Required: No





```
// A single horizontal annotation with fill shading above the annotation line, based on the metric associated with the right Y-axis
                
"annotations": {
     "horizontal": [
         {
              "visible":true,
              "color":"#9467bd",
              "label":"Critical range",
              "value":20,
              "fill":"above",
              "yAxis":"right"
         }
    ]
}

// A band annotation. Each value has a label, but other parameters for the band are specified only with the first number

"annotations": {
    "horizontal": [
        [
            {
                "label": "Band top",
                "value": 200,
                "color": "#9467bd",
                "visible": true,
                "yAxis": "right"
            },
            {
                "value": 95.5,
                "label": "Band bottom"
            }
        ]
    ]
}

// Three annotations on a graph. The first one is a band annotation. The final one is hidden.

"annotations": {
    "horizontal": [
        [
            {
                "label": "Band top",
                "value": 200,
                "color": "#9467bd",
                "visible": true,
                "yAxis": "right"
            },
            {
                "value": 95.5,
                "label": "Band bottom"
            }
        ],
        {
            "visible": true,
            "color": "#9467bd",
            "label": "Label for this annotation",
            "value": 20,
            "fill": "below",
            "yAxis": "right"
        },
        {
            "visible": false,
            "color": "#aaa",
            "label": "Hidden annotation",
            "value": 150
        }
    ]
}

```

#### Vertical Annotations




**vertical**

An array of vertical annotations. For each vertical annotation, you can choose to have fill shading before
 the annotation, after it, or between two vertical lines that are linked as a 
 single band annotation. Each vertical annotation in the array that is a single annotation, instead
 of a band annotation, has the following format:



```
{`value`, `label`, `color`, `fill`, `visible`}
```

Each vertical annotation that is a band annotation has the following format:



```
[ {`value`, `label`, `color`, `visible`}, {`value`, `label`} ]
```





**value**

The date and time in the graph where the vertical annotation line is to appear. On a band shading annotation, the two values
 for Value define the beginning and ending edges of the band.


On a graph with vertical annotations, the graph is scaled so that all visible vertical annotations appear on the graph. 


This is defined as a string in ISO 8601 format. For more information, 
 see [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601").

Type: String


Required: Yes



**label**

A string that appears on the graph next to the annotation.


Type: String


Required: No



**color**

The six-digit HTML hex color code to be used for the annotation. This color is used for both the annotation line and the fill shading.


Type: String


Required: No



**fill**

How to use fill shading with the annotation. Valid values are
 `before` for shading before the annotation,
 `after` for shading after the annotation, and
 `none` for no shading. If `fill` is
 omitted, there is no shading.


The exception is an annotation with band shading. These annotations always have shading between the two values, and any value for `fill`
 is ignored.


Type: String


Required: No



**visible**

Set this to `true` to have the annotation appear in the graph, or `false` to have it be hidden. The default
 is `true`.


Type: Boolean


Required: No





```
// A single vertical annotation with fill shading after the annotation line
                    
"annotations": {
    "vertical": [
        {
            "visible": true,
            "color": "#9467bd",
            "label": "Bug fix deployed",
            "value": "2018-08-28T15:25:26Z",
            "fill": "after"
        }
    ]
}	


// A band vertical annotation. Each annotation line has a label, but other parameters for the band are specified only with the first value

"annotations": {
    "vertical": [
        [
            {
                "label": "Band start",
                "value": "2018-08-27T15:25:26Z",
                "color": "#9467bd",
                "visible": true
            },
            {
                "value": "2018-08-28T15:25:26Z",
                "label": "Band end"
            }
        ]
    ]
}


```

### Dashboard Widget Object: yAxis Properties Format


Defines the settings for the Y-axis of the graph. The settings include
 the maximum and minimum, a label for the axis, and whether the axis shows the units.
 Set this
 within the `widget` object to affect all metrics in the widget. To
 override the widget settings for a particular metric, set it for the metric in the
 `metrics` array.



```
{
  left: {
    min: 0,
    max: 100
  },
  right: {
    min: 0
  }
}

```



**left**

Optional settings for the left Y-axis.


Type: YAxis object


Required: No



**right**

Optional settings for the right Y-axis.


Type: YAxis object


Required: No




Each of the `left` and `right` objects can include the
 following parameters:




**label**

A label for this Y-axis


Type: String


Required: No



**min**

The minimum value for this Y-axis


Type: Float


Required: No



**max**

The maximum value for this Y-axis


Type: Float


Required: No



**showUnits**

Determines whether the units are shown for the metric
 associated with this axis. The default is true.


Type: Boolean


Required: No




### Dashboard Widget Object: Table Properties


If you specify `table` for a metric widget, you can include visualisations related to the visibility of summary columns, datapoint columns, and the table layout. 
 These properties take affect only when the widget view type is `table` and don't alter other view types if included. The `table` property is not required to use a table widget.




**layout**

Use this field to transform the table such that the data points extend vertically or horizontally. The default is `horizontal`.


Valid Values: `vertical` | `horizontal`


Type: String


Required: No



**stickySummary**

Set this to `true` to make the summary columns that you include in the table sticky, so you can explore the data
 columns while always having the summary columns in your viewport. The default is `false`.


The widget label is always sticky, no matter your choice in this field.


Valid Values: `true` | `false`


Type: Boolean


Required: No



**showTimeSeriesData**

Set this to `false` if you want only the label and summary columns to be displayed, hiding the other columns of data.


The default is `true`.


Valid Values: `true` | `false`


Type: Boolean


Required: No



**summaryColumns**

Summary columns are a new property introduced with the table widget. These columns are a specific subset of summaries of your current table. For example, the 
 `Sum` summary is a sum of all the rendered datapoints in its respective row. Summary columns are not that same concept as any CloudWatch metric statistic.


The default is `[“MIN“, "MAX","SUM", "AVG"]`


Valid Values: `"MIN"` | `"MAX"`| `"SUM"`| `"AVG"`


Type: Array


Required: No




For example, the following JSON creates a table displaying the minimum and maximum of each metric in the table.



```
"table": {
    "summaryColumns": ["MIN", "MAX"],
    "layout": "vertical",
    "stickySummary": true,
    "showTimeSeriesData": false,
    },
```

## 
 Properties of a Metrics Explorer Widget Object


A widget of type 
 `explorer` represents a metrics explorer widget. For more information, 
 see [Use Metrics Explorer to Monitor Resources by Their 
 Tags and Properties](../monitoring/CloudWatch-Metrics-Explorer.md "../monitoring/CloudWatch-Metrics-Explorer.md")



You can also add metrics explorer widgets to a dashboard using AWS CloudFormation. For
 more information, see [AWS::CloudWatch::Dashboard](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.md").


This widget type can have the following fields within the widget `properties`:




**aggregateBy**

An object that specifies how to aggregate metrics from multiple resources. The valid values 
 for the `key` field in this object are
 the keys of tags and resource properties. This object contains
 the following fields.



* **key**– The
 tag or resource property key to use for aggregating the metrics.
* **func**– The
 aggregation function to use. Valid values are 
 `AVG` |
 `MIN` |
 `MAX` |
 `STDDEV` |
 `SUM`

Type: Object


Required: No



**labels**

An array of the tags or the resource properties that are used to determine
 which metrics are displayed in the widget.
 


If you specify different keys, then only the resources that match all of
 the key/value pairs are displayed. If you specify multiple values for a single key, 
 then resources that match any of the values for that key are displayed.



* **key**– The
 tag or resource property to filter on.


For `key`, all tag keys are valid to be specified. The following
 EC2 and Lambda resource properties are also valid for `key`:




	+ EC2:
	
	
	`Architecture`, `Hypervisor`,
	 `CoreCount`, 
	 `ImageId`, 
	 `InstanceId`, 
	 `InstanceLifecycle`, 
	 `InstanceType`, 
	 `InstanceFamily`, 
	 `InstanceSize`, 
	 `Affinity`, 
	 `AvailabilityZone`, 
	 `Tenancy`, `Platform`, `RootDeviceType
	 `SecurityGroups`, 
	 `State`, 
	 `SubnetId`, 
	 `VirtualizationType`, and
	 `VpcId``
	+ Lambda:
	
	
	`FunctionName`, 
	 `Runtime`, 
	 `Language`, 
	 `MemorySize`, 
	 `Version`, 
	 `SecurityGroupIds`, 
	 `SubnetIds`, 
	 `SubnetIdCount`, 
	 `VpcId`, and
	 `Timeout`
* **value**– (Optional) The
 value of the tag or resource property to filter on. If this is omitted,
 metrics corresponding to all values of that tag or resource property are displayed.

Type: Object


Required: Yes



**metrics**

Specify a `metrics` array to include one or more metrics. 
 One `metrics` array can include
 1–100 metrics. Each object in the array must contain the following fields.



* **metricName**– The
 name of the metric.
* **resourceType**– The
 type of resource publishing the metric, described in the format
 used by AWS CloudFormation. For example, `AWS::EC2::Instance`
 or `AWS::Lambda::Function`.


You must use the same value for `resourceType` 
 for all metrics in the widget.


For a complete list of valid values, see
 [Valid 
 resourceType Values for a Metric Explorer Widget Object](#CloudWatch-Dashboard-Properties-Metric-Explorer-resourceType "#CloudWatch-Dashboard-Properties-Metric-Explorer-resourceType").
* **stat**– The statistic for this metric, if it is to be different than the statistic used for the 
 other metrics in the array. By default CloudWatch uses *Average* if you don't specify a statistic at array or at metric level.


Valid Values: `SampleCount` | `Average` | `Sum` | `Minimum` | `Maximum` |
 `p`??``

Type: Array of objects


Required: Yes



**period**

The default period, in seconds, for all metrics in this widget. The period is the length of time represented by one
 data point on the graph. The default is 300.


Valid Values: Any multiple of 60, with 60 as the minimum.


Type: Integer


Required: No



**splitBy**

Specifies how to split the metrics from multiple resources into
 different lines on a graph, or into different graphs. The valid values are
 the keys of tags, and the keys of resource properties.


Type: String


Required: No



**title**

The title to be displayed for the widget. The default is `Explorer`.


Type: String


Required: No



**widgetOptions**

An object that specifies how the widget appears on the dashboard. It can 
 contain the following fields.



* **legend**–


Determines where the legend for each graph is displayed. 
 The `legend` field contains another 
 field called `position`. Possible values for `position`
 are `right`, `bottom`, and `hidden`.


For example, the following causes the legend to appear on the right
 in the graph.



```
"legend": {
     "position": "right"
}
```
* **rowsPerPage**–


Specifies how many rows of graphs are displayed per page in the widget.
* **stacked**–

Specify 
 `true` to display the graph as a stacked area chart, or `false` to 
 display as separate lines.
* **view**–


Specifies how each graph is displayed. 
 Specify `timeSeries` to display this metric as a line graph. 
 Specify `bar` to 
 display it as a bar graph. 
 Specify `pie` to display it as a pie graph. The default
 is `timeSeries`.
* **widgetsPerRow**–


Specifies how many graphs are displayed in each row
 of the metrics explorer widget.

Type: Object


Required: No




**Example**


The following example displays three metrics for each of the account's running EC2 instances, with the 
 graphs in the widget split by availability zone. Within each graph, the metrics are aggregated 
 by instance type.



```
{
    "widgets": [
        {
            "type": "explorer",
            "width": 24,
            "height": 15,
            "x": 0,
            "y": 0,
            "properties": {
                "metrics": [
                    {
                        "metricName": "CPUUtilization",
                        "resourceType": "AWS::EC2::Instance",
                        "stat": "Average"
                    },
                    {
                        "metricName": "NetworkIn",
                        "resourceType": "AWS::EC2::Instance",
                        "stat": "Average"
                    },
                    {
                        "metricName": "NetworkOut",
                        "resourceType": "AWS::EC2::Instance",
                        "stat": "Average"
                    }
                ],
                "aggregateBy": {
                    "key": "InstanceType",
                    "func": "MAX"
                },
                "labels": [
                    {
                        "key": "State",
                        "value": "running"
                    }
                ],
                "widgetOptions": {
                    "legend": {
                        "position": "bottom"
                    },
                    "view": "timeSeries",
                    "rowsPerPage": 8,
                    "widgetsPerRow": 2
                },
                "period": 300,
                "splitBy": "AvailabilityZone",
                "title": "Running EC2 Instances by AZ"
            }
        }
    ]
}
```

### Valid 
 resourceType Values for a Metric Explorer Widget Object


The valid values for the `resourceType` field in the `metrics`
 section of a metrics explorer widget are as follows:



* `AWS::AmazonMQ::Broker`
* `AWS::ApiGateway::RestApi`
* `AWS::AppStream::Fleet`
* `AWS::AppSync::GraphQLApi`
* `AWS::CloudFront::Distribution`
* `AWS::CodeBuild::Project`
* `AWS::Datasync::Agent`
* `AWS::Datasync::Task`
* `AWS::DMS::ReplicationInstance`
* `AWS::DynamoDB::Table`
* `AWS::EC2::CapacityReservation`
* `AWS::EC2::Instance`
* `AWS::EC2::NatGateway`
* `AWS::EC2::TransitGateway`
* `AWS::EC2::Volume`
* `AWS::EC2::VPNConnection`
* `AWS::ECS::Cluster`
* `AWS::EFS::FileSystem`
* `AWS::ElastiCache::CacheCluster`
* `AWS::ElastiCache::ReplicationGroup`
* `AWS::ElasticBeanstalk::Environment`
* `AWS::ElasticLoadBalancing::LoadBalancer`
* `AWS::ElasticLoadBalancingV2::LoadBalancer/ApplicationELB`
* `AWS::ElasticLoadBalancingV2::LoadBalancer/GatewayELB`
* `AWS::ElasticLoadBalancingV2::LoadBalancer/NetworkELB`
* `AWS::ElasticLoadBalancingV2::TargetGroup`
* `AWS::EMR::Cluster`
* `AWS::Events::Rule`
* `AWS::FSx::FileSystem`
* `AWS::GameLift::Fleet`
* `AWS::GlobalAccelerator::Accelerator`
* `AWS::IoT::TopicRule`
* `AWS::IoT1Click::Device`
* `AWS::IoTAnalytics::Channel`
* `AWS::IoTAnalytics::Dataset`
* `AWS::IoTAnalytics::Datastore`
* `AWS::IoTAnalytics::Pipeline`
* `AWS::Kafka::Cluster`
* `AWS::Kinesis::Stream`
* `AWS::KinesisAnalytics::Application`
* `AWS::KinesisFirehose::DeliveryStream`
* `AWS::KinesisVideo::Stream`
* `AWS::KMS::Key`
* `AWS::Lambda::Function`
* `AWS::Logs::LogGroup`
* `AWS::MediaPackage::Channel`
* `AWS::MediaStore::Container`
* `AWS::OpsWorks::Instance`
* `AWS::OpsWorks::Layer`
* `AWS::OpsWorks::Stack`
* `AWS::QLDB::Ledger`
* `AWS::RDS::DBInstance`
* `AWS::Redshift::Cluster`
* `AWS::RoboMaker::SimulationJob`
* `AWS::Route53::HealthCheck`
* `AWS::Route53Resolver::ResolverEndpoint`
* `AWS::S3::Bucket`
* `AWS::SageMaker::Endpoint`
* `AWS::ServiceCatalog::CloudFormationProduct`
* `AWS::SES::ConfigurationSet`
* `AWS::SNS::Topic`
* `AWS::SQS::Queue`
* `AWS::StepFunctions::Activity`
* `AWS::StepFunctions::StateMachine`
* `AWS::StorageGateway::Gateway`
* `AWS::Synthetics::Canary`
* `AWS::Transfer::Server`
* `AWS::WorkMail::Organization`
* `AWS::WorkSpaces::Workspace`

## 
 Properties of an Alarm Status Widget Object


A widget of type `alarm` can have the following
 fields within `properties`.




**alarms**

An array of alarm ARNs to include in the widget. The array 
 can have 1-100 ARNs.


Type: Array of strings


Required: Yes (when the widget `type` is `alarm`).



**sortBy**

Specifies how to sort the alarms in the widget.


Choose `default`
 to sort them in alphabetical order by alarm name.


Choose `stateUpdatedTimestamp`
 to sort them first by alarm state, with alarms in ALARM state first, INSUFFICIENT\_DATA
 alarms next, and OK alarms last. Within each group, the alarms are sorted by 
 when they last changed state, with more recent state changes listed first.


Choose `timestamp`
 to sort them by the time when the alarms most recently changed state, no matter the
 current alarm state. The alarm that changed state most
 recently is listed first.


If you omit this field, the alarms are sorted in alphabetical order.


Type: String


Valid Values: default | stateUpdatedTimestamp | timestamp


Required: No



**states**

Use this field to filter the list of alarms displayed in the widget to only 
 those alarms currently in the specified states. You can specify one or more alarm states
 in the value for this field. The alarm states that you can specify are
 `ALARM`, `INSUFFICIENT_DATA`, and `OK`.


If you omit this field or specify an empty array, all the alarms
 specifed in `alarms` are displayed.


Type: Array of strings


Required: No



**title**

The title text to be displayed by the widget.


Type: String


Required: No




The following example is an alarm status widget that displays four alarms specified by
 name, no matter their current state:



```
{
    "type": "alarm",
    "x": 0,
    "y": 0,
    "width": 12,
    "height": 6,
    "properties": {
        "alarms": [
            "arn:aws:cloudwatch:us-east-1:012345678901:alarm:EC2FrontendCPU",
            "arn:aws:cloudwatch:us-east-1:012345678901:alarm:EC2BackendCPU",
            "arn:aws:cloudwatch:eu-west-1:987654321098:alarm:EC2FrontendCPU",
            "arn:aws:cloudwatch:eu-west-1:987654321098:alarm:EC2BackendCPU"
        ],
        "sortBy": "stateUpdatedTimestamp",
        "title": "All EC2 CPU alarms"
    }
}
```

The following example widget specifies the same four alarms, but the widget
 displays only the alarms that are
 currently in ALARM or INSUFFICIENT\_DATA state:



```
{
    "type": "alarm",
    "x": 0,
    "y": 0,
    "width": 12,
    "height": 6,
    "properties": {
        "alarms": [
            "arn:aws:cloudwatch:us-east-1:012345678901:alarm:EC2FrontendCPU",
            "arn:aws:cloudwatch:us-east-1:012345678901:alarm:EC2BackendCPU",
            "arn:aws:cloudwatch:eu-west-1:987654321098:alarm:EC2FrontendCPU",
            "arn:aws:cloudwatch:eu-west-1:987654321098:alarm:EC2BackendCPU"
        ],
        "sortBy": "stateUpdatedTimestamp",
        "states": [
            "ALARM",
            "INSUFFICIENT_DATA"
        ],
        "title": "EC2 alarms that are not currently OK"
    }
}
```
