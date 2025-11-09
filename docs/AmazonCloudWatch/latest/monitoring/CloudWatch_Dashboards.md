# Using Amazon CloudWatch dashboards

Amazon CloudWatch includes automatic pre-built dashboards and also enables you to create your own dashboards.
Dashboards help you to
monitor your resources in a single view, even those resources that are spread across
different Regions. You can use CloudWatch dashboards to create customized views of the telemetry data for your AWS resources.

With customizable dashboards, you can create the following:

- A single view for selected metrics and alarms to help you assess the health of
  your resources and applications across one or more Regions. You can select the color
  used for each metric on each graph, so that you can easily track the same metric across multiple
  graphs.
- An operational playbook that provides guidance for team members during operational
  events about how to respond to specific incidents.
- A common view of critical resource and application measurements that can be shared
  by team members for faster communication flow during operational events.
  If you have multiple AWS accounts, you can set up _CloudWatch cross-account observability_
  and then create
  rich cross-account dashboards
  in your monitoring accounts. You can seamlessly search, visualize, and analyze your metrics, logs, and traces
  without account boundaries.

With CloudWatch cross-account observability, you can do the following in a dashboard in a monitoring account:

- Search, view, and create graphs of metrics that reside in source accounts. A single graph
  can include metrics
  from multiple accounts.
- Create alarms in the monitoring account that watch metrics in source accounts.
- View the log events from log groups located in source accounts, and run CloudWatch Logs Insights queries of
  log groups in
  source accounts. A single CloudWatch Logs Insights query in a monitoring account
  can query multiple log groups in multiple source accounts at once.
- View nodes from source accounts in a trace map in X-Ray. You can
  then filter the map to specific source accounts.
  When you are signed in to a monitoring account, a blue **Monitoring account** badge
  appears at the top right of every page that supports CloudWatch cross-account observability functionality.

For more information about setting up CloudWatch cross-account observability, see
[CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

You can create dashboards
from the console
or using the AWS CLI or `PutDashboard` API operation.
You can add dashboards
to a favorites list,
where you can access not only your favorite dashboards, but also your recently visited dashboards.
For more information,
see [Add a dashboard to your favorites list](add-dashboard-to-favorites.md "add-dashboard-to-favorites.md").

To access CloudWatch dashboards, you need one of the following:

- The
  `AdministratorAccess`
  policy
- The
  `CloudWatchFullAccess`
  policy
- A custom policy that includes one or more of these specific permissions:
  - `cloudwatch:GetDashboard` and `cloudwatch:ListDashboards` to be able to view dashboards

  - `cloudwatch:PutDashboard` to be able to create or modify dashboards

  - `cloudwatch:DeleteDashboards` to be able to delete dashboards

###### Topics

- [Getting started with automatic dashboards](GettingStarted.md "GettingStarted.md")
- [Creating a customized dashboard](create_dashboard.md "create_dashboard.md")
- [Creating a cross-account cross-Region dashboard with the console](create_xaxr_dashboard.md "create_xaxr_dashboard.md")
- [Create a cross-account cross-Region dashboard
  programmatically](#create_xaxr_dashboard_API "#create_xaxr_dashboard_API")
- [Creating a graph with metrics from different accounts and Regions](#create-graph-xaxr-dashboard "#create-graph-xaxr-dashboard")
- [Adding an alarm from a different account to a cross-account dashboard](create-alarm-xaxr-dashboard.md "create-alarm-xaxr-dashboard.md")
- [Creating dashboards with variables](cloudwatch_dashboard_variables.md "cloudwatch_dashboard_variables.md")
- [Using widgets on dashboards](create-and-work-with-widgets.md "create-and-work-with-widgets.md")
- [Sharing dashboards](cloudwatch-dashboard-sharing.md "cloudwatch-dashboard-sharing.md")
- [Using live data](cloudwatch-live-data.md "cloudwatch-live-data.md")
- [Viewing an animated dashboard](cloudwatch-animated-dashboard.md "cloudwatch-animated-dashboard.md")
- [Add a dashboard
  to your favorites list](add-dashboard-to-favorites.md "add-dashboard-to-favorites.md")
- [Changing the period override setting or refresh interval](change_dashboard_refresh_interval.md "change_dashboard_refresh_interval.md")
- [Changing the time range or time zone format](change_dashboard_time_format.md "change_dashboard_time_format.md")

## Create a cross-account cross-Region dashboard

programmatically

You can use the AWS APIs and SDKs to create dashboards programmatically. For more information,
see [PutDashboard](../APIReference/API_PutDashboard.md "../APIReference/API_PutDashboard.md").

To enable cross-account cross-Region dashboards, we have added new parameters
to the dashboard body structure, as shown in the following table
and examples. For more information about overall dashboard body structure, see
[Dashboard Body Structure and Syntax](../APIReference/CloudWatch-Dashboard-Body-Structure.md "../APIReference/CloudWatch-Dashboard-Body-Structure.md").

| Parameter   | Use                                                                        | Scope            | Default                                |
| ----------- | -------------------------------------------------------------------------- | ---------------- | -------------------------------------- |
| `accountId` | Specifies the ID of the account where the widget or the metric is located. | Widget or metric | Account that is currently logged in    |
| `region`    | Specifies the Region of the metric.                                        | Widget or metric | Current Region selected in the console |

The following examples illustrate the JSON source for widgets in a cross-account cross-Region dashboard.

This example sets the `accountId` field to the ID of the sharing account at the widget
level. This specifies that all metrics in this widget will come from that sharing account and Region.

```

{
  "widgets": [
    {
          ...
          "properties": {
        "metrics": [
                   …
        ],
        "accountId": "111122223333",
        "region": "us-east-1"
      }
    }
  ]
}


```

This example sets the `accountId` field differently at the level of each metric. In this example,
the
different metrics in this metric math expression come from different sharing accounts and different Regions.

```

{
  "widgets": [
    {
          ...
          "properties": {
        "metrics": [
          [
            {
              "expression": "SUM(METRICS())",
              "label": "[avg: ${AVG}] Expression1",
              "id": "e1",
              "stat": "Sum"
            }
          ],
          [
            "AWS/EC2",
            "CPUUtilization",
            {
              "id": "m2",
              "accountId": "5555666677778888",
              "region": "us-east-1",
              "label": "[avg: ${AVG}] ApplicationALabel "
            }
          ],
          [
            ".",
            ".",
            {
              "id": "m1",
              "accountId": "9999000011112222",
              "region": "eu-west-1",
              "label": "[avg: ${AVG}] ApplicationBLabel"
            }
          ]
        ],
        "view": "timeSeries",
        "region": "us-east-1", ---> home region of the metric. Not present in above example
              "stacked": false,
        "stat": "Sum",
        "period": 300,
        "title": "Cross account example"
      }
    }
  ]
}


```

This example shows an alarm widget.

```

{
  "type": "metric",
  "x": 6,
  "y": 0,
  "width": 6,
  "height": 6,
  "properties": {
    "accountID": "111122223333",
    "title": "over50",
    "annotations": {
      "alarms": [
        "arn:aws:cloudwatch:us-east-1:379642911888:alarm:over50"
      ]
    },
    "view": "timeSeries",
    "stacked": false
  }
}


```

This example is for a CloudWatch Logs Insights widget.

```

{
  "type": "log",
  "x": 0,
  "y": 6,
  "width": 24,
  "height": 6,
  "properties": {
    "query": "SOURCE 'route53test' | fields @timestamp, @message\n| sort @timestamp desc\n| limit 20",
    "accountId": "111122223333",
    "region": "us-east-1",
    "stacked": false,
    "view": "table"
  }
}


```

Another way to create dashboards programmatically is to first create one in the AWS Management Console, and then copy the JSON source of this
dashboard. To do so, load the dashboard and choose **Actions**, **View/edit source**. You can then
copy this dashboard JSON to use as a template to create similar dashboards.

## Creating a graph with metrics from different accounts and Regions in a CloudWatch dashboard

1. Sign in to the monitoring account.
2. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the navigation pane, choose **Metrics**, and then choose **All metrics**.
4. Select the account and Region
   that you want
   to add metrics
   from.
   You can select your account and Region
   from the account and Region dropdown menus
   near the top-right
   of the screen.
5. Add the metrics you want to the graph. For more information, see [Graphing metrics](graph_metrics.md "graph_metrics.md").
6. Repeat steps 4-5 to add metrics from other accounts and Regions.
7. (Optional) Choose the **Graphed metrics** tab and add
   a metric math function that uses the metrics that you have chosen. For more
   information, see [Using math expressions with CloudWatch metrics](using-metric-math.md "using-metric-math.md").

You can also set up a single graph to include multiple
`SEARCH` functions. Each search can refer to a different
account or Region. 8. When you are finished with the graph, choose **Actions**, **Add to dashboard**.

Select your cross-account dashboard, and choose **Add to dashboard**.
