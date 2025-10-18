# GetMetricWidgetImage: Metric Widget Structure and Syntax

`MetricWidget` is an input parameter for the [https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API\_GetMetricWidgetImage.html](API_GetMetricWidgetImage.md "API_GetMetricWidgetImage.md") API. It
 is a string in JSON format. 

###### Contents

* [Overall Structure](#Metric-Widget-Overall-Structure "#Metric-Widget-Overall-Structure")
* [Format for Each Metric in the Array of Metrics](#CloudWatch-Metric-Widget-Metrics-Array-Format "#CloudWatch-Metric-Widget-Metrics-Array-Format")
* [Annotation Properties Format](#CloudWatch-Metric-Widget-Annotations-Format "#CloudWatch-Metric-Widget-Annotations-Format")
* [yAxis Properties Format](#CloudWatch-Metric-Widget-YAxis-Properties-Format "#CloudWatch-Metric-Widget-YAxis-Properties-Format")
## Overall Structure


The `MetricWidget` string can include the following parameters:




**metrics**

The metrics to include in the graph, as a
 `metrics` array. This can include both raw metric and metric
 math expressions. One `metrics` array can include
 1–100 metrics and expressions. For more
 information about the format of `metrics`, see [Format for Each Metric in the Array of Metrics](#CloudWatch-Metric-Widget-Metrics-Array-Format "#CloudWatch-Metric-Widget-Metrics-Array-Format").


Type: Array of arrays


Required: Yes.



**annotations**

The horizontal and vertical annotations to add to the graph, as annotations arrays. For more information about the format, see 
 [Annotation Properties Format](#CloudWatch-Metric-Widget-Annotations-Format "#CloudWatch-Metric-Widget-Annotations-Format").


Required: No



**end**

The date and time for the end of the metrics shown in the graph. This can be expressed as either an absolute value, such as 
 **2018-04-25T12:00:00.000Z** or a relative value such as **-PID**.


If you don't specify `end`, the default of `-PT0H` (the current time) is used.


Type: String


Required: No



**height**

The height of the widget in pixels. The default is 400.


Valid Values: 1–2000


Type: Integer


Required: No, but you should set this if you also set a value for `width`.



**legend**

Specifies the location and visibility of the graph legend. `legend` contains one field, `position`. 
 The value of `position` can be `bottom`, `right`, or `hidden`. The default is
 `bottom`.


Type: String


Required: No



**liveData**

Specify `true` to display *live data* in the widget. Live
 data is data published within the last minute that has not been fully aggregated. For more
 information, see [Use Live Data](../monitoring/cloudwatch-live-data.md "../monitoring/cloudwatch-live-data.md").


Type: Boolean


Required: No



**period**

The default period, in seconds, for all metrics in this widget. This default can be overridden within each metric definition.
 The default is 300.


Valid Values: 1, 5, 10, 30, 60, and any multiple of 60. 1, 5, 10, and 30 are only for high-resolution metrics.


Type: Integer


Required: No



**region**

This parameter is optional. If you include it, it must specify the local Region.


Type: String


Required: No



**stacked**

Specify `true` to display the graph as a stacked line, or `false` to 
 display as separate lines. The default is false.


Type: Boolean


Required: No



**start**

The date and time for the start of the metrics shown in the graph. This can be expressed as either an absolute value, such as 
 **2018-04-25T12:00:00.000Z** or a relative value such as **-PID**.


If you don't specify `start`, the default of `-PT3H` (three hours ago) is used.


Type: String


Required: No



**stat**

The default statistic to be displayed for each metric
 in the array. This 
 default can be overridden within the definition of each individual metric in 
 the `metrics` array.


If you omit this, the default of `Average` is used.


Valid Values: `SampleCount` | `Average` |
 `Sum` | `Minimum` | `Maximum` |
 `p`??`` |
 `TM(`??`:`??`)`,
 `TC(`??`:`??`)`
| `TS(`??`:`??`)`
| `WM(`??`:`??`)`
| `PR(`??`:`??`)`
| `IQM` Type: String that is a valid CloudWatch statistic. Required: No **theme** The color palette used to style the graph. The default is `light`. Valid Values: `light | dark` Type: String Required: No **timezone** The time zone to use for displaying the times in the graph. The format is + or - followed by four digits. The first two digits indicate the number of hours ahead or behind of UTC, and the final two digits are the number of minutes. For example, `+0130` indicates a time 1 hour and 30 minutes ahead of UTC. The default is `+0000`. Type: String Required: No **title** The title to be displayed for the graph. Type: String Required: No **view** The display format. Specify `timeSeries` to display this metric as a line graph. Specify `bar` to display the metric as a bar graph. Specify `pie` to display the metric as a pie graph. The default is `timeSeries`. Valid Values: `timeSeries | bar | pie` Type: String Required: No **width** The width of the widget in pixels. The default is 600. Valid Values: 1–2000 Type: Integer Required: No, but you should set this if you also set a value for `width`. **yAxis** Limits for the minimums and maximums of the y-axis. This applies to every metric being graphed, unless specific metrics override it. For more information about the format, see [yAxis Properties Format](#CloudWatch-Metric-Widget-YAxis-Properties-Format "#CloudWatch-Metric-Widget-YAxis-Properties-Format"). Type: YAxis object Required: No ## Format for Each Metric in the Array of Metrics Each item in the `metrics` array is a CloudWatch metric to display in the graph, or to use as part of a math expression displayed in the graph. For more information about math expressions, see [Use Metric Math](../monitoring/using-metric-math.md "../monitoring/using-metric-math.md") in the Amazon CloudWatch User Guide. Each metric in the array has the following format: ``` [`Namespace`, `MetricName`, `Dimension1Name`, `Dimension1Value`, `Dimension2Name`, `Dimension2Value`... {`Options Object`}] ``` **Namespace** The AWS namespace containing the metric. To use the same namespace as the previous metric in the array, you may specify `"."` for each entry after the first. Type: String Required: Yes **MetricName** The name of the CloudWatch metric. To use the same name as the previous metric in the array, you may specify `"."` for each entry after the first. Type: String Required: Yes **DimensionName** The name of a dimension to further refine what data is shown. To use the same dimension name as the previous metric in the array, you may specify `"."` for each entry after the first. You may specify zero dimensions for a metric, or up to as many dimensions as the metric supports. Type: String Required: No **DimensionValue** The value to use for that dimension for the metric. Required if there is a corresponding dimension name. Type: String Required: No, unless there is a corresponding dimension name. **Options Object** Specifies either custom rendering properties to be used for the specified CloudWatch metric, or a math expression to display on the graph. For more information about the format, see [Options Object Format](#CloudWatch-Metric-Widget-Options-Object-Format "#CloudWatch-Metric-Widget-Options-Object-Format"). Type: Options Object Required: No *Examples* ``` // The simplest example, a metric with no dimensions [ "AWS/EC2", "CPUUtilization" ] // A metric with a single dimension [ "AWS/EC2", "CPUUtilization", "InstanceId", "i-01234567890123456" ] // A metric with a single dimension and rendering properties [ "AWS/EC2", "DiskReadBytes", "InstanceId", "i-01234567890123456", { yAxis: "right"} ] // The following example graphs the `DiskReadBytes` metric for three instances. [ "AWS/EC2", "DiskReadBytes", "InstanceId", "i-01234567890123456" ], [ ".", ".", ".", "i-abc" ], [ ".", ".", ".", "i-123" ] ``` ### Options Object Format Specifies either custom rendering properties to be used for the specified CloudWatch metric, or a math expression to display on the graph. If this object is specified as part of a CloudWatch metric in the `metrics` array, it sets custom rendering properties for this metric and overrides the defaults used for the whole graph. You can also specify this object to add a math expression to the graph. In this case, the other settings in this object specify the display options for the result of the math expression. This section describes the format of these options objects. **color** The six-digit HTML hex color code to be used for this metric or expression. Type: String Required: No **expression** A math expression to display. For more information about supported math expression functions and format, see [Metric Math Syntax and Functions](../monitoring/using-metric-math.md#metric-math-syntax "../monitoring/using-metric-math.md#metric-math-syntax") in the Amazon CloudWatch User Guide. Type: String that is a valid CloudWatch metric math expression. Required: Yes if this is an expression. **label** The label to display for this metric or expression in the graph legend. If this is not specified, the metric is given an auto-generated label that distinguishes it from the other metrics in the widget. Type: String Required: No **id** An identifier for this metric or expression, which must be unique within this widget. The id can be used as a variable to represent this metric or expression within math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Type: String Required: No **period** The period for this metric, in seconds. If specified, this overrides the default period used for other metrics in this graph. This parameter is not applicable for math expressions. Valid Values: 1, 5, 10, 30, 60, and any multiple of 60. 1, 5, 10, and 30 are only for high-resolution metrics. Type: Integer Required: No **stat** The statistic to be displayed for this metric, if it is to be different than the statistic used for the other metrics in the graph. This parameter is not applicable for math expressions. Valid Values: `SampleCount` | `Average` | `Sum` | `Minimum` | `Maximum` | `p`??`` Type: String that is a valid CloudWatch statistic. Required: No **visible** Specifies whether this metric or expression is shown on the graph. The default is `true`. Setting `visible` to `false` is useful if you want to hide the raw metrics that are used in math expressions, and show only the expression results on the graph. Type: Boolean Required: No **yAxis** Where on the graph to display the y-axis for this metric or expression. The default is `left`. Valid Values: `left` | `right` Type: String Required: No *Example* In the following example, CloudWatch retrieves a custom `apiLatency` metric. At the top, the p50 statistic is specified to show the median value. Next, for the same metric on the same instance (this is specified by the four fields that are just periods), the Average value is graphed. Next is an options object with a math expression, showing the halfway value of the two metrics. Finally, another expression shows the rate of change. To show only the results of the two expressions on the graph and hide the raw metrics, you could change the first two instances of `visible` to `false`. ``` { "metrics": [ [ "MyNamespace", "apiLatency", "InstanceId", "i-0987654321abcdef0", { "id": "m1", "stat": "p50", "label": "Median value", "visible": true, "color": "#dddddd", "yAxis": "left", "period": 300 } ], [ ".", ".", ".", ".", { "id": "m2", "stat": "Average", "label": "Average value", "visible": true, "color": "#cccccc", "yAxis": "left", "period": 300 } ], [ { "expression": "(m1+m2)/2", "id": "e1", "label": "Half way between average and median", "visible": true, "color": "#000000", "yAxis": "left" } ], [ { "expression": "RATE(e1)", "yAxis": "right", "label": "rate of change of the half way point" } ] ] } ``` ## Annotation Properties Format A single graph can have multiple horizontal and vertical annotations. All horizontal annotations are specified in one `horizontal` field, and all vertical annotations are specified in one `vertical` field. **horizontal** An array of horizontal annotations. Horizontal annotations have several options for fill shading, including shading above the annotation line, shading below the annotation line, and "band" shading that appears between two linked annotation lines as part of a single annotation. Each horizontal annotation in the array that does not have band shading has the following format: ``` {`value`, `label`, `color`, `fill`, `yAxis`, `visible`} ``` Each horizontal annotation that does have band shading has the following format: ``` [{`value`, `label`, `color`, `yAxis`, `visible`}, {`value`, `label`}] ``` **vertical** An array of vertical annotations. Vertical annotations have several options for fill shading, including shading before the annotation line, shading after the annotation line, and "band" shading that appears between two linked annotation lines as part of a single band annotation. Each vertical annotation in the array that does not have band shading has the following format: ``` {`value`, `label`, `color`, `fill`, `visible`} ``` Each vertical annotation that does have band shading has the following format: ``` [{`value`, `label`, `color`, `visible`}, {`value`, `label`}] ``` The `horizontal` array can include the following fields. **value** The metric value in the graph where the horizontal annotation line is to appear. On a band shading annotation, the two values for `Value` define the upper and lower edges of the band. On a graph with horizontal annotations, the graph is scaled so that all visible horizontal annotations appear on the graph. Type: Float Required: Yes, if horizontal annotations are used. **label** A string that appears on the graph next to the annotation. Type: String Required: No **color** The six-digit HTML hex color code to be used for the annotation. This color is used for both the annotation line and the fill shading. Type: String Required: No **fill** How to use fill shading with the annotation. Valid values are `above` for shading above the annotation, `below` for shading below the annotation, and `none` for no shading. If `fill` is omitted, there is no shading. The exception is an annotation with band shading. These annotations always have shading between the two values, and any value for `fill` is ignored. Type: String Required: No **visible** Set this to `true` to have the annotation appear in the graph, or `false` to have it be hidden. The default is `true`. Type: Boolean Required: No **yAxis** If the graph includes multiple metrics, specifies whether the numbers in `Value` refer to the metric associated with the left Y-axis or the right Y-axis. Valid values are `right` and `left`. Type: String Required: No The `vertical` array can include the following fields. **value** The time stamp where the vertical annotation line is to appear. This must be specified as an absolute time stamp, such as `2018-08-28T15:25:26Z`. On a band shading annotation, the two values for `Value` define the beginning and ending edges of the band. Type: String Required: Yes, if vertical annotations are used. **label** A descriptive string that appears on the graph next to the annotation. Type: String Required: No **color** The six-digit HTML hex color code to be used for the annotation. This color is used for both the annotation line and the fill shading. Type: String Required: No **fill** How to use fill shading with the annotation. Valid values are `before` for shading before the annotation, `after` for shading after the annotation, and `none` for no shading. If `fill` is omitted, there is no shading. The exception is an annotation with band shading. These annotations always have shading between the two values, and any value for `fill` is ignored. Type: String Required: No **visible** Set this to `true` to have the annotation appear in the graph, or `false` to have it be hidden. The default is `true`. Type: Boolean Required: No *Examples* ``` // A single horizontal annotation with fill shading above the annotation line, based on the metric associated with the right Y-axis "annotations": { "horizontal": [ { "visible":true, "color":"#9467bd", "label":"Critical range", "value":20, "fill":"above", "yAxis":"right" } ] } // A horizontal band annotation. Each value has a label, but other parameters for the band need to be specified only with the first number "annotations": { "horizontal": [ [ { "label":"Band top", "value":200, "color":"#9467bd", "visible":true, "yAxis":"right" }, { "value":95.5, "label":"Band bottom" } ] ] } // A single vertical annotation with fill shading after the annotation line "annotations": { "vertical": [ { "visible": true, "color": "#9467bd", "label": "Bug fix deployed", "value": "2018-08-28T15:25:26Z", "fill": "after" } ] } // A vertical band annotation. Each annotation line has a label, but other parameters for the band are specified only with the first value "annotations": { "vertical": [ [ { "label": "Band start", "value": "2018-08-27T15:25:26Z", "color": "#9467bd", "visible": true }, { "value": "2018-08-28T15:25:26Z", "label": "Band end" } ] ] } ``` ## yAxis Properties Format Defines the minimum and maximum values for the Y-axis of the graph. Set this within the `MetricWidget` object to affect all metrics in the widget. To override the widget settings for a particular metric, set it in the options object for that metric in the `metrics` array. **left** Optional `min` and `max` settings for the left Y-axis. Type: YAxis object Required: No **right** Optional `min` and `max` settings for the right Y-axis. Type: YAxis object Required: No Each of the `left` and `right` objects can include the following parameters: **min** The minimum value for this Y-axis. Type: Float Required: No **max** The maximum value for this Y-axis. Type: Float Required: No *Example* ``` { left: { min: 0, max: 100 }, right: { min: 0 } } ```
