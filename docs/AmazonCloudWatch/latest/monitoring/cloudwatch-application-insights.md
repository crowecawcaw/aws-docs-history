# Detect common application problems with CloudWatch Application Insights

You can use Amazon CloudWatch Application Insights to detect problems with your applications. CloudWatch Application Insights facilitates observability for your applications and underlying AWS resources.
It helps you set up the best monitors for your application resources to continuously analyze
data for signs of problems with your applications. Application Insights, which is powered by [SageMaker](../../../sagemaker/latest/dg/wahtis.md "../../../sagemaker/latest/dg/wahtis.md") and other AWS
technologies, provides automated dashboards that show potential problems with monitored
applications, which help you to quickly isolate ongoing issues with your applications and
infrastructure. The enhanced visibility into the health of your applications that Application Insights
provides helps reduce mean time to repair (MTTR) to troubleshoot your application
issues.

When you add your applications to Amazon CloudWatch Application Insights, it scans the resources in the applications and
recommends and configures metrics and logs on [CloudWatch](WhatIsCloudWatch.md "WhatIsCloudWatch.md") for application components. Example application components include SQL
Server backend databases and Microsoft IIS/Web tiers. Application Insights analyzes metric patterns
using historical data to detect anomalies, and continuously detects errors and exceptions
from your application, operating system, and infrastructure logs. It correlates these
observations using a combination of classification algorithms and built-in rules. Then, it
automatically creates dashboards that show the relevant observations and problem severity
information to help you prioritize your actions. For common problems in .NET and SQL
application stacks, such as application latency, SQL Server failed backups, memory leaks,
large HTTP requests, and canceled I/O operations, it provides additional insights that point
to a possible root cause and steps for resolution. Built-in integration with [AWS SSM
OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md") allows you to resolve issues by running the relevant Systems Manager
Automation document.

###### Sections

- [What is
  Amazon CloudWatch Application Insights?](appinsights-what-is.md "appinsights-what-is.md")
- [How Application Insights
  works](appinsights-how-works.md "appinsights-how-works.md")
- [Prerequisites, IAM policies, and permissions](appinsights-accessing.md "appinsights-accessing.md")
- [Set up application for monitoring](appinsights-setting-up.md "appinsights-setting-up.md")
- [Application Insights cross-account observability](appinsights-cross-account.md "appinsights-cross-account.md")
- [Work with component
  configurations](component-config.md "component-config.md")
- [Use CloudFormation
  templates](appinsights-cloudformation.md "appinsights-cloudformation.md")
- [Tutorial: Set up monitoring for SAP ASE](appinsights-tutorial-sap-ase.md "appinsights-tutorial-sap-ase.md")
- [Tutorial: Set up
  monitoring for SAP HANA](appinsights-tutorial-sap-hana.md "appinsights-tutorial-sap-hana.md")
- [Tutorial: Set up monitoring for SAP NetWeaver](appinsights-tutorial-sap-netweaver.md "appinsights-tutorial-sap-netweaver.md")
- [View and troubleshoot
  Application Insights](appinsights-troubleshooting.md "appinsights-troubleshooting.md")
- [Supported logs and
  metrics](appinsights-logs-and-metrics.md "appinsights-logs-and-metrics.md")
