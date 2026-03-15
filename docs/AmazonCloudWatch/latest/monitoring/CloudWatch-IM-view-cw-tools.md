# Exploring your data with CloudWatch tools and the Internet Monitor query interface

In addition to visualizing your performance and availability for your application with the Internet Monitor dashboard,
there are several methods that you can use to dive deeper into the data that Internet Monitor generates for you. These methods
include using CloudWatch tools with Internet Monitor data stored in CloudWatch Log files and using the Internet Monitor query interface. The tools
that you can use include CloudWatch Logs Insights, CloudWatch Metrics, CloudWatch Contributor Insights, and Amazon Athena. You can use some
or all these tools, as well as the dashboard, to explore Internet Monitor data, depending on your needs.

Internet Monitor aggregates CloudWatch metrics about traffic to your application and to each AWS Region, and includes
data such as total traffic impact, availability, and round-trip time. This data is published to CloudWatch Logs
and is also available to use with the Internet Monitor query interface. Details about geo-granularity and other aspects
of the information available to explore for each one varies.

Internet Monitor publishes data for your monitor at 5 minute intervals, and then makes the data available
in several ways. The following table lists scenarios for accessing Internet Monitor data, and describes features of
the data that is collected for each one.

| Feature                                            | CloudWatch Logs                                                                                                                                                      | Export to S3                                                                                                                               | Query interface                                                                                                                   | CloudWatch dashboard                                                                                                                      |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled by default                                 | Yes                                                                                                                                                                  | No                                                                                                                                         | Yes                                                                                                                               | Yes                                                                                                                                       |
| Number of city-networks that data is collected for | Top 500 (see note below)                                                                                                                                             | All                                                                                                                                        | All                                                                                                                               | All                                                                                                                                       |
| Data retention                                     | User controlled                                                                                                                                                      | User controlled                                                                                                                            | 30 days                                                                                                                           | 30 days                                                                                                                                   |
| Geo-granularities that data is collected for       | All (city-network, metro+network, subdivision+network, country+network)                                                                                              | City-network                                                                                                                               | All (city-network, metro+network, subdivision+network, country+network)                                                           | All (city-network, metro+network, subdivision+network, country+network)                                                                   |
| How to query and filter data                       | [Use CloudWatch Logs Insights to explore Internet Monitor measurements](CloudWatch-IM-view-cw-tools-logs-insights.md "CloudWatch-IM-view-cw-tools-logs-insights.md") | [Use Amazon Athena to query internet measurements in Amazon S3 log files](CloudWatch-IM-view-cw-tools.md "CloudWatch-IM-view-cw-tools.md") | [Use the Internet Monitor query interface](CloudWatch-IM-view-cw-tools-cwim-query.md "CloudWatch-IM-view-cw-tools-cwim-query.md") | [Monitor and optimize with the Internet Monitor dashboard](CloudWatch-IM-monitor-and-optimize.md "CloudWatch-IM-monitor-and-optimize.md") |

Note: Top 500 measurements are captured for city-networks; top 250 for metro+networks, top 100 for subdivision+networks, top 50 for country+networks.

This chapter describes how to query and explore your data by using CloudWatch tools or the Internet Monitor query interface,
together with examples for each method.

###### Contents

- [CloudWatch Logs Insights](CloudWatch-IM-view-cw-tools-logs-insights.md "CloudWatch-IM-view-cw-tools-logs-insights.md")
- [CloudWatch Contributor Insights](CloudWatch-IM-view-cw-tools-contributor-insights.md "CloudWatch-IM-view-cw-tools-contributor-insights.md")
- [CloudWatch Metrics](CloudWatch-IM-view-cw-tools-metrics-dashboard.md "CloudWatch-IM-view-cw-tools-metrics-dashboard.md")
- [Athena with S3 logs](CloudWatch-IM-view-cw-tools.md "CloudWatch-IM-view-cw-tools.md")
- [Internet Monitor query interface](CloudWatch-IM-view-cw-tools-cwim-query.md "CloudWatch-IM-view-cw-tools-cwim-query.md")
