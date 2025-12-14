# Viewing your Lambda Insights metrics

After you have installed the Lambda Insights extension on a Lambda function that has been invoked, you
can use the CloudWatch console to see your metrics. You can see a multi-function overview, or focus
on a single function. You can also view metrics for Lambda functions running on Managed Instances.

For a list of Lambda Insights metrics, see [Metrics collected by Lambda Insights](Lambda-Insights-metrics.md "Lambda-Insights-metrics.md").

###### To view the multi-function overview for your Lambda Insights metrics

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Insights**, **Lambda Insights**.
3. In the **Lambda Insights view** dropdown at the top of the page, select **Functions**.
4. Choose **Multi-function**.

The top part of the page displays graphs with aggregated metrics of all your Lambda functions
in the Region that have Lambda Insights enabled. Lower on the page is a table that lists the functions. 5. To filter by function name to reduce the number of functions displayed, type part of the
function name in the box near the top of the page. 6. To add this view to a dashboard as a widget, choose **Add to dashboard**.

###### To view metrics for a single function

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Insights**, **Lambda Insights**.
3. In the **Lambda Insights view** dropdown at the top of the page, select **Functions**.
4. Choose **Single function**.

The top part of the page displays graphs with metrics for
the selected function. 5. If you have X-Ray enabled, you can choose a single trace ID. This opens the X-Ray Trace Map page for
that invocation, and from there you can zoom out to see the distributed trace and the
other services involved in handling that specific transaction. For more information about
the X-Ray Trace Map, see [Using the
X-Ray Trace Map](../../../xray/latest/devguide/xray-console-servicemap.md "../../../xray/latest/devguide/xray-console-servicemap.md"). 6. To open CloudWatch Logs Insights and zoom in on a specific error,
choose **View logs** by the table at the bottom of the page. 7. To add this view to a dashboard as a widget, choose **Add to dashboard**.

###### To view metrics for Lambda functions running on Managed Instances

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Insights**, **Lambda Insights**.
3. In the **Lambda Insights view** dropdown at the top of the page, select **Managed Instances Functions**.

The page displays the Managed Instances view with metrics for your Lambda functions running on Managed Instances. 4. In the **Views** section, select a granularity level for viewing your metrics:

    * **Capacity Provider** – Displays aggregated metrics at the capacity provider level.
    * **Instance Type** – Displays aggregated metrics at the instance type level.
    * **Function** – Displays metrics at the individual function level. The top part of the page displays graphs with aggregated metrics of all your Lambda functions in the region that has Lambda Insights enabled. Lower on the page is a table that lists the functions. To filter by function name, type part of the function name in the box near the top of the page.

5. Use the **Filters** section to filter by capacity provider, instance type, or function.
6. To add this view to a dashboard as a widget, choose **Add to dashboard**.
