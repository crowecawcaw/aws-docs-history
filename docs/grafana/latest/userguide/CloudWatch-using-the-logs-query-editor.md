# Using the Amazon CloudWatch Logs

query editor

To query CloudWatch Logs, select the Region and up to 20 log groups that you want
to query. Use the main input area to write your query. For more information,
see [CloudWatch Logs Insights
query syntax](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md").

You can also write queries returning time series data by using the
`stats` command in CloudWatch Logs Insights. When making
`stats` queries in Explore, you have to make sure you are in
Metrics Explore mode.

To the right of the query input field is a CloudWatch Logs Insights link that opens
the CloudWatch Logs Insights console with your query. You can continue exploration
there if necessary.

## Using template

variables

As with several other data sources, the CloudWatch data source supports the
use of template variables in queries. For more information, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

## Deep linking from Grafana panels to the CloudWatch Logs console

If you want to view your query in the CloudWatch Logs Insights console, choose
the **CloudWatch Logs Insights** button next to the query editor.
If you’re not currently signed in to the CloudWatch console, the link forwards
you to the sign-in page. The provided link is valid for any
AWS account but only displays the correct metrics if you’re signed in
to the AWS account that corresponds to the selected data source in
Grafana.

## Alerting

Because CloudWatch Logs queries can return numeric data, for example, through
the use of the `stats` command, alerts are supported. For
more information, see [Grafana alerting](alerts-overview.md "alerts-overview.md").
