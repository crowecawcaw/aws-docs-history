# Query your CloudWatch metrics with
 CloudWatch Metrics Insights

CloudWatch Metrics Insights is a powerful high-performance SQL query engine that you can use to query your
 metrics at scale. You can identify trends and patterns within all of your CloudWatch metrics in real
 time, with access to up to two weeks of historical data for comprehensive trend analysis.

You can also set alarms on any Metrics Insights queries that return a single time series.
 This can be especially useful to create alarms that watch aggregated metrics across a fleet of
 your infrastructure or applications. Create the alarm once, and it dynamically adjusts as
 resources are added to or removed from the fleet.

 You can perform a CloudWatch Metrics Insights query in the console with the CloudWatch Metrics Insights query editor. You can also
 perform a CloudWatch Metrics Insights query with the AWS CLI or an AWS SDK by running `GetMetricData` or
 `PutDashboard`. There's no charge for queries that you run with the CloudWatch Metrics Insights query
 editor. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). 

 With the CloudWatch Metrics Insights query editor, you can choose from a variety of prebuilt sample queries and
 also create your own queries. As you create your queries, you can use a builder view to browse
 your existing metrics and dimensions. Alternatively, use an editor view to manually write
 queries. 

With Metrics Insights, you can run queries at scale. With the **GROUP
 BY** clause, you can group your metrics in real time into separate time series per
 specific dimension value. Because Metrics Insights queries include an **ORDER
 BY** ability, you can use Metrics Insights to make "Top N" type queries. For
 example, "Top N" type queries can scan millions of metrics in your account and return the 10
 instances that consume the most CPU. This can help you pinpoint and remedy latency issues in your applications. To use tags with alarms, opt in through CloudWatch Settings. After tags is enabled, you can also filter and group metrics using AWS resource tags, enabling you to query metrics aligned with your 
 organizational structure, such as by application, environment, or team.

###### Topics

* [Building your queries in
 CloudWatch Metrics Insights](cloudwatch-metrics-insights-buildquery.md "cloudwatch-metrics-insights-buildquery.md")
* [Query components and syntax in
 CloudWatch Metrics Insights](cloudwatch-metrics-insights-querylanguage.md "cloudwatch-metrics-insights-querylanguage.md")
* [Alarms on CloudWatch Metrics Insights queries in CloudWatch](cloudwatch-metrics-insights-alarms.md "cloudwatch-metrics-insights-alarms.md")
* [Use Metrics Insights queries with metric
 math](cloudwatch-metrics-insights-math.md "cloudwatch-metrics-insights-math.md")
* [Use natural language to generate
 and update CloudWatch Metrics Insights queries](cloudwatch-metrics-insights-query-assist.md "cloudwatch-metrics-insights-query-assist.md")
* [SQL inference](cloudwatch-metrics-insights-inference.md "cloudwatch-metrics-insights-inference.md")
* [Metrics Insights quotas](cloudwatch-metrics-insights-limits.md "cloudwatch-metrics-insights-limits.md")
* [Metrics Insights sample
 queries](cloudwatch-metrics-insights-queryexamples.md "cloudwatch-metrics-insights-queryexamples.md")
* [Metrics Insights glossary](cloudwatch-metrics-insights-glossary.md "cloudwatch-metrics-insights-glossary.md")
* [Troubleshooting Metrics
 Insights](cloudwatch-metrics-insights-troubleshooting.md "cloudwatch-metrics-insights-troubleshooting.md")
