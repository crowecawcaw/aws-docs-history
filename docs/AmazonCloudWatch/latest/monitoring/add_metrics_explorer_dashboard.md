# 
 Add a metrics explorer widget 
 to a CloudWatch dashboard

The following steps explain how to add a metrics explorer widget to a 
 dashboard using the console. You can also add it programmatically or by
 using AWS CloudFormation. For more information, see 
[Metrics Explorer Widget Object Definition](../APIReference/CloudWatch-Dashboard-Body-Structure.md#CloudWatch-Dashboard-Properties-Metric-Explorer-Object "../APIReference/CloudWatch-Dashboard-Body-Structure.md#CloudWatch-Dashboard-Properties-Metric-Explorer-Object") and [AWS::CloudWatch::Dashboard](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.md").

###### To add a metrics explorer widget to a dashboard

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**.
3. Choose the name of the dashboard where you want to add the metrics
 explorer widget.
4. Choose the **+** symbol.
5. Choose **Explorer** and then choose **Next**.
 


###### Note

You must be opted in to the new dashboard view to be able to add a Metrics Explorer widget. To
 opt in, choose **Dashboards** in the navigation pane,
 then choose **try out the new interface** in the banner
 at the top of the page.
6. Do one of the following:


	* To use a template, choose **Pre-filled Explorer widget**
	 and then select a template to use.
	* To create a custom visualization, choose 
	 **Empty Explorer widget**.
7. Choose **Create**.


If you used a template, the widget appears on your dashboard with the selected
 metrics. If you're satisfied with the explorer widget and the dashboard,
 choose **Save dashboard**.


If you did not use a template, continue to the following steps.
8. In the new widget under **Explorer**, in the **Metrics**
 box, choose a single metric or all the available metrics from a
 service.


After you choose a metric, you can optionally repeat this step to add more
 metrics.
9. For each metric selected, CloudWatch displays the statistic that it will use immediately after the
 metric name. To change this, choose the statistic name and then choose the
 statistic that you want.
10. Under **From**, choose a tag or a resource property to 
 filter your results.


After you do this, you can optionally repeat this step to choose more tags
 or resource properties.


If you choose multiple values of the same property, such as two EC2
 instance types, the explorer displays all the resources that match either
 chosen property. It's treated as an OR operation.


If you choose
 different properties or tags, such as the `Production` 
 tag and the M5 instance type, only the resources
 that match all of these selections are displayed. This is treated as an AND operation.
11. (Optional) For **Aggregate by**, choose a statistic to 
 use to aggregate the metrics. Then, next to **for**, choose how to 
 aggregate the metric from the list. You can aggregate 
 together all the resources that are currently displayed, or aggregate 
 by a single tag or resource property.


Depending on how you choose to aggregate, the result may be a single time
 series or multiple time series.
12. Under **Split by**, you can choose to split a single graph with multiple time
 series into multiple graphs. The split can be made by a variety of criteria,
 which you choose under **Split by**.
13. Under **Graph options**, you can refine the graph by changing the period, 
 the type of graph, the legend placement, and the layout.
14. If you're satisfied with the explorer widget and the dashboard, choose **Save
 dashboard**.
