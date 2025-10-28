# Analyze with Amazon OpenSearch Service

CloudWatch Logs integrates with Amazon OpenSearch Service to enable you to create automatic
curated dashboards that display key metrics that OpenSearch Service derives from logs vended from AWS
services. The following dashboards are available:

- An **Amazon VPC flow logs dashboard** captures network flow data for
  Amazon VPC. It helps you analyze network traffic, detect unusual patterns, and monitor
  resource usage. Key metrics displayed include the following:
  - Total flows and acceptance and rejection of these flows
  - Traffic patterns over time
  - A Sankey diagram that illustrates data flow between source and destination
    IPs (top talkers)
  - Top IPs by bytes and packets transferred

###### Note

Currently only VPC version 2 fields format is supported.

- An **AWS WAF logs dashboard** provides insights into web traffic
  being monitored by AWS WAF. This dashboard helps you identify traffic patterns,
  blocked requests, and potential threats from specific regions or IPs. Key metrics
  displayed include the following:
  - Total requests, including by “ALLOW” and “BLOCK” counts.
  - Request history over time, displaying allowed and blocked requests.
  - Breakdowns of requests by Web ACL name, blocked requests by terminating
    rule, and source IPs.
  - A geographic distribution of request origins.
  - Top client IPs and terminating rules by request count.

- A **CloudTrail logs** dashboard provides an overview of API activity
  within your AWS environment using CloudTrail logs. It’s useful for monitoring API
  activity, auditing actions, and identifying potential security or compliance issues.
  Key metrics displayed include the following:
  - Total event count and event history over time
  - A breakdown of events by account IDs, categories, and Regions.
  - Top APIs, services, and source IPs involved in generating events.
  - A table of the top users that are generating events, detailing user
    account information and event counts.

- An **AWS Network Firewall** dashboard provides enhanced visibility into network
  traffic, offering valuable insights for security monitoring and analysis. This
  dashboard offers a comprehensive view of various network metrics and patterns, to
  quickly identify potential security issues and optimize network configurations. Key
  metrics displayed include the following:

      + Top talkers and protocols
      + Insights into PrivateLink endpoints
      + Allowed and blocked TLS Server Name Indication traffic

  The metrics displayed in these curated dashboards are derived from
  Amazon OpenSearch Service analytics.

Before you can view these dashboards, you must create an IAM role and perform a one-time
integration of CloudWatch Logs with Amazon OpenSearch Service. This one-time integration
configures the Amazon OpenSearch Service resources needed to create and render the
dashboard. You will incur charges for the OpenSearch services used. For more information,
see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

You can create these curated dashboards only for log groups in the Standard Log
Class.

###### Important

Don't use [log
transformers](CloudWatch-Logs-Transformation.md "CloudWatch-Logs-Transformation.md") for any log groups that you want to create vended logs
dashboards for. Transforming log events will cause the dashboards to have empty
data.

###### Topics

- [Step 1: Create the integration with
  OpenSearch Service](OpenSearch-Dashboards-Integrate.md "OpenSearch-Dashboards-Integrate.md")
- [Step 2: Create vended logs
  dashboards](OpenSearch-Dashboards-Create.md "OpenSearch-Dashboards-Create.md")
- [View, edit, or delete vended logs
  dashboards](OpenSearch-Dashboards-Manage.md "OpenSearch-Dashboards-Manage.md")
- [IAM policies for users](OpenSearch-Dashboards-UserRoles.md "OpenSearch-Dashboards-UserRoles.md")
- [Permissions that the integration
  needs](OpenSearch-Dashboards-CreateRole.md "OpenSearch-Dashboards-CreateRole.md")
