

# Set up cross-account cross-region monitoring for CloudWatch Database Insights
<a name="Database-Insights-Cross-Account-Cross-Region"></a>

 CloudWatch Database Insights supports cross-account and cross-region database fleet monitoring, enabling centralized observability across your entire database AWS infrastructure. It allows you to monitor, troubleshoot, and optimize databases spanning multiple AWS accounts and regions from a single unified console experience. 

**Topics**
+ [Prerequisites](#Database-Insights-Cross-Account-Cross-Region-Prereq)
+ [Set-up your monitoring and source accounts for Database Insights cross-account access](#Database-Insights-Cross-Account-Cross-Region-MonitoringSourceAccountSetup)
+ [Set-up Database Insights for cross-account cross-region console](#Database-Insights-Cross-Account-Cross-Region-setup)
+ [Using Database Insights cross-account cross-region dashboards](#Database-Insights-Cross-Account-Cross-Region-Using)

## Prerequisites
<a name="Database-Insights-Cross-Account-Cross-Region-Prereq"></a>
+ Database Insights cross-account cross-region requires both **CloudWatch cross-account observability** and the **cross-account cross-region CloudWatch console** to be setup first. See instructions below on how to enable both.
+ If you have already enabled them, you might still need to configure additional data sharing for Database Insights to work across accounts and regions in your environment. See instructions below and make sure you have selected the right data sharing configuration.

## Set-up your monitoring and source accounts for Database Insights cross-account access
<a name="Database-Insights-Cross-Account-Cross-Region-MonitoringSourceAccountSetup"></a>

1. Follow the step-by-step guide in [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html). CloudFormation templates are provided for infrastructure as code deployments. 

1. In **Step 1: Set up a monitoring account** you need to at least select the following data types to share with your monitoring account for Database Insights to work across accounts and regions: **Logs**, **Metrics**, **Traces**, and **Application Signals - Services, Service Level Objectives (SLOs)**.

1. You need to do this process for **all regions** where you want to setup Database Insights with cross-account cross-region support.

## Set-up Database Insights for cross-account cross-region console
<a name="Database-Insights-Cross-Account-Cross-Region-setup"></a>

1. Follow the step-by-step guide in [Cross-account cross-Region CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html). 

1. In **Step 5: Permissions**, you need to at least select the following data types to share with your monitoring account: **Include CloudWatch automatic dashboards**, and **Include read-only access for Database Insights.** Otherwise, you can also opt for **Full read-only access to everything in your account**, which will include all data sources available. 

1.  CloudWatch cross-region console is a global setting, so you only need to do this step once and it will work for all regions. 

## Using Database Insights cross-account cross-region dashboards
<a name="Database-Insights-Cross-Account-Cross-Region-Using"></a>

 After you set up Database Insights for cross-account cross-region support, you can enable "Cross-account cross-region mode" in the **Filters** section of the left panel, right under **Database Views**. You will see a toggle button located on the top left corner, like in the screenshot below. 

![Filters panel with cross-account cross-region mode toggle, region selector, and account filters.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/database-insights-enable-cross-account-toggle.png)


 Once cross-account cross-region mode is enabled, new Filters are available, which allow you to select multiple regions and to filter by AWS Account IDs and labels, database resource types, and database resource identifiers. 

 By default, your current region and all accounts are selected. If you change your selection of regions and accounts, the Fleet Health Dashboard updates automatically to show resources that match the selected region and account filters. 

 From the Fleet Health Dashboard, you can easily navigate to the Database Instance Dashboard for instances that belong to other AWS accounts and regions. 

 There is a few aspects you must take into consideration when working with Database Insights cross-account cross-region monitoring: 
+  Alarms must be created in the monitoring account only. Alarms can be configured on metrics from source accounts, but they need to be created in the monitoring account. 
+  Fleet monitoring views must be defined and saved in the monitoring account only. 
+  Custom metrics dashboards in Database Insights Instance Dashboard must be customised in the monitoring account only. 
+  The maximum number of regions allowed in the Database Insights Fleet Health Dashboard at a given time is 3. 
+  Only read operations are allowed from the Monitoring account. This means you cannot create performance analysis reports from the Monitoring account. 
+  When cross-account cross-region mode is enabled in the Fleet Health Dashboard, filtering by AWS Resource Tags and resource properties is not available. 