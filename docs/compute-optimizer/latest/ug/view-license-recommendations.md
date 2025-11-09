# Viewing commercial software license recommendations

AWS Compute Optimizer generates license recommendations for commercial software that run on Amazon EC2.
These recommendations are displayed on the following pages of the Compute Optimizer console.

The **Recommendations for commercial software licenses** page lists the
following information for each of your EC2 instances with licenses.

- Finding classifications
- Finding reasons
- Estimated monthly savings
- Savings opportunity
- On-Demand prices
- BYOL hourly license prices
  The recommendations from Compute Optimizer are listed next to each of your EC2 instances with commercial software licenses. The information
  that's provided includes recommended saving opportunities, EC2 instance On-Demand prices, and
  hourly bring your own license (BYOL) prices. This information can help you decide if you should
  down-size your license edition. For more information about how to view
  your license recommendations for commercial software, see [Accessing commercial software license recommendations and details](license-view-recommendations.md "license-view-recommendations.md").

###### Note

The recommendations are refreshed daily and they can take up to 24 hours to generate.
Keep in mind that Compute Optimizer requires 24 hours of metrics in the past 14 days to
generate license recommendations. For more information, see
[Commercial software license requirements](requirements.md#requirements-license "requirements.md#requirements-license").

The **License details** page provides the following
information for your license recommendation:

- Your current license settings and Compute Optimizer's recommended licence configurations.
  Use the table to compare your current license configurations, such as edition, model, and number of
  instance cores, with Compute Optimizer recommendations.
- Use the utilization graphs to access the utilization of the current license during the
  analysis period.
  For more information about how to view the details for your license recommendation,
  see [Accessing commercial software license details page](license-view-recommendations.md#license-viewing-details "license-view-recommendations.md#license-viewing-details").

###### Contents

- [Finding classifications](#license-recommendations-findings "#license-recommendations-findings")
- [Finding reasons](#license-finding-reasons "#license-finding-reasons")
- [Estimated monthly savings and savings
  opportunity](#license-savings-calculation "#license-savings-calculation")
- [Inferred workload types](#license-inferred-workload-types "#license-inferred-workload-types")
- [Compare current license edition with recommended license edition](#compare-license-table "#compare-license-table")
- [Utilization graphs](#license-utilization-graphs "#license-utilization-graphs")
- [Accessing commercial software license recommendations and details](license-view-recommendations.md "license-view-recommendations.md")

## Finding classifications

The **Findings** column on the **Commercial software license recommendations** page provides a summary of how each of your licenses performed during the analyzed period.

The following findings classifications apply to Microsoft SQL Server licenses.

| Classification       | Description                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Insufficient metrics | When Compute Optimizer detects that your CloudWatch Application Insights isn't enabled or is enabled with<br>insufficient permissions. Compute Optimizer displays a finding reason of `InvalidCloudwatchApplicationInsights`<br>or `CloudwatchApplicationInsightsError`.                                                                          |
| Not optimized        | When Compute Optimizer detects that your EC2 infrastructure isn't using any of the Microsoft SQL server license features<br>you're paying for, a license is considered not optimized. Compute Optimizer displays a finding reason of<br>`LicenseOverprovisioned`. A license that isn't optimized might result in unnecessary<br>additional costs. |
| Optimized            | When the license for your SQL server database meets your performance requirements, the license is<br>considered optimized.                                                                                                                                                                                                                        |

For more information about these finding classifications, see
[Finding reasons](#license-finding-reasons "#license-finding-reasons").

## Finding reasons

The **Finding reasons** column on the **EC2 instances
recommendations** and **EC2 instance details** pages shows which
specification of an instance is under-provisioned or over-provisioned.

The following finding reasons apply to Microsoft SQL server license recommendations.

| Finding reason                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LicenseOverprovisioned`               | A license is considered over-provisioned when any of the current license features<br>aren't in use. CloudWatch Application Insights analyzes the<br>`mssql_enterprise_features_used` metric to identify this.<br>If your license is over-provisioned, you can consider downgrading your Microsoft<br>SQL Server license. If you meet certain eligibility requirements you can downgrade<br>from SQL Server Enterprise edition to SQL Server Standard edition, or Developer<br>edition if it is a non-production workload. For more information, see<br>[Downgrade<br>your Microsoft SQL Server edition](../../../sql-server-ec2/latest/userguide/downgrade-sql-server-on-ec2.md "../../../sql-server-ec2/latest/userguide/downgrade-sql-server-on-ec2.md") in the _Microsoft SQL Server on<br>Amazon EC2 User Guide_. |
| `InvalidCloudwatchApplicationInsights` | The backend exporter of your CloudWatch Application Insights isn't configured properly. For more<br>information about how to configure CloudWatch Application Insights, see [Set up<br>Amazon CloudWatch Application Insights for monitoring](../../../AmazonCloudWatch/latest/monitoring/appinsights-setting-up.md "../../../AmazonCloudWatch/latest/monitoring/appinsights-setting-up.md") in the _Amazon CloudWatch User Guide_.                                                                                                                                                                                                                                                                                                                                                                                   |
| `CloudwatchApplicationInsightsError`   | You have configured CloudWatch Application Insights but it hasn't identified the number of<br>Enterprise edition features in use. It can take a few hours to identify the features.<br>If the features aren't identified after a few hours, contact Support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Estimated monthly savings and savings

opportunity

The **Estimated monthly savings (On-Demand)** column lists the approximate
monthly cost savings after you downgrade your license edition based on Compute Optimizer’s recommendations.
To calculate this, Compute Optimizer multiplies the savings per hour by the estimated monthly running hours.

The **Savings opportunity (%)** column lists the percentage difference between
your current Microsoft SQL server license and Compute Optimizer’s recommended license. The Bring Your Own
License (BYOL) savings calculation is based on the license price. The License Included savings calculation
is based on the On-Demand pricing.

###### Important

Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page.
That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings
estimates considering the price of existing resources, the price of recommended resources, and
historical usage data. Estimated monthly savings reflects the projected dollar savings
associated with each of the recommendations generated. For more information, see [Enabling
Cost Explorer](../../../cost-management/latest/userguide/ce-enable.md "../../../cost-management/latest/userguide/ce-enable.md") and [Optimizing your cost with
Rightsizing Recommendations](../../../cost-management/latest/userguide/ce-rightsizing.md "../../../cost-management/latest/userguide/ce-rightsizing.md") in the _Cost Management User
Guide_.

## Inferred workload types

The **Inferred workload types** column on the
**EC2 instances recommendations** page lists the applications that might be
running on the instance as inferred by Compute Optimizer. This column does this by analyzing the attributes of
your instances. These attributes include the instance name, tags, and configuration. Compute Optimizer can
currently infer if your instances are running Amazon EMR, Apache Cassandra,
Apache Hadoop, Memcached, NGINX,
PostgreSQL, Redis, Kafka, or
SQLServer. By inferring the applications that run on your instances, Compute Optimizer can
identify the effort to migrate your workloads from x86-based instance types to
Arm-based AWS Graviton instances types. For more information, see
[Migration effort](view-ec2-recommendations.md#ec2-migration-effort "view-ec2-recommendations.md#ec2-migration-effort") in the next section
of this guide.

###### Note

You can't infer the SQLServer application in the Middle East (Bahrain), Africa (Cape Town),
Asia Pacific (Hong Kong), Europe (Milan), and Asia Pacific (Jakarta) Regions.

## Compare current license edition with recommended license edition

On the **License details** page, compare the configurations of your current license edition
with Compute Optimizer’s recommended license edition. The following table provides a description for
each column section in the console.

| Column                    | Description                                                                                                                                                                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| License edition           | The current license edtion and the recommended license edition. For example, Enterprise,<br>Standard, and Free.                                                                                                                                                               |
| Instance On-Demand price  | The current and recommended On-Demand instance prices.                                                                                                                                                                                                                        |
| BYOL price (hourly)       | The current and recommended Bring your own license (BYOL) hourly price.                                                                                                                                                                                                       |
| Estimated monthly savings | The approximate monthly cost savings after you downgrade your license edition based<br>on Compute Optimizer’s recommendations. For more information, see [Estimated monthly savings and savings<br>opportunity](#license-savings-calculation "#license-savings-calculation"). |
| Savings opportunity (%)   | The percentage difference between your current Microsoft SQL server license and Compute Optimizer’s<br>recommended license. For more information, see [Estimated monthly savings and savings<br>opportunity](#license-savings-calculation "#license-savings-calculation").    |
| Instance cores            | The current and recommended number of physical cores for an instance. Number of instance<br>cores are used in licensing calculations.                                                                                                                                         |

## Utilization graphs

The **License details** page displays current resource utilization of the
current commercial software license. The graph only displays the number of Enterprise editon
features that were used data over the analysis period.

You can change the graphs to display data for the last 24 hours, three days, one week, or two
weeks.
