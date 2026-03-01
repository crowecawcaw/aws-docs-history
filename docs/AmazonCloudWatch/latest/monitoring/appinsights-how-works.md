# How Amazon CloudWatch Application Insights works

CloudWatch Application Insights provides monitoring of your application resources. The following information describes how Application Insights works.

###### Topics

- [How Application Insights monitors applications](#appinsights-how-works-sub "#appinsights-how-works-sub")
- [Data retention](#appinsights-retention "#appinsights-retention")
- [Quotas](#appinsights-limits "#appinsights-limits")
- [AWS Systems Manager (SSM) packages used by CloudWatch Application Insights](appinsights-ssm-packages.md "appinsights-ssm-packages.md")
- [AWS Systems Manager (SSM) Documents used by CloudWatch Application Insights](appinsights-ssm-documents.md "appinsights-ssm-documents.md")

## How Application Insights monitors applications

The following information describes how Application Insights monitors applications.

###### Application discovery and configuration

The first time an application is added to CloudWatch Application Insights it scans the application
components to recommend key metrics, logs, and other data sources to monitor for
your application. You can then configure your application based on these
recommendations.

###### Data preprocessing

CloudWatch Application Insights continuously analyzes the data sources being monitored across the
application resources to discover metric anomalies and log errors
(observations).

###### Intelligent problem detection

The CloudWatch Application Insights engine detects problems in your application by correlating
observations using classification algorithms and built-in rules. To assist in
troubleshooting, it creates automated CloudWatch dashboards, which include contextual
information about the problems.

###### Alert and action

When CloudWatch Application Insights detects a problem with your application, it generates CloudWatch Events to
notify you of the problem. See [Application Insights CloudWatch Events for detected problems](appinsights-cloudwatch-events.md "appinsights-cloudwatch-events.md") for more information about
how to set up these Events. Additionally, you can [configure Amazon SNS notifications](appinsights-problem-notifications.md "appinsights-problem-notifications.md") to receive alerts
for detected problems.

**Example scenario**

You have an ASP .NET application that is backed by a SQL Server database.
Suddenly, your database begins to malfunction because of high memory pressure. This
leads to application performance degradation and possibly HTTP 500 errors in your
web servers and load balancer.

With CloudWatch Application Insights and its intelligent analytics, you can identify the application layer
that is causing the problem by checking the dynamically created dashboard that shows
the related metrics and log file snippets. In this case, the problem might be at the
SQL database layer.

## Data retention

CloudWatch Application Insights retains problems for 55 days and observations for 60 days.

## Quotas

For default quotas for CloudWatch Application Insights, see [Amazon CloudWatch Application Insights endpoints and
quotas](../../../general/latest/gr/applicationinsights.md "../../../general/latest/gr/applicationinsights.md"). Unless otherwise noted, each quota is per AWS Region. Contact
[AWS Support](https://console.aws.amazon.com/support/home#/case/create?issueType=technical "https://console.aws.amazon.com/support/home#/case/create?issueType=technical") to request an increase in your service quota. Many
services contain quotas that cannot be changed. For more information about the
quotas for a specific service, see the documentation for that service.
