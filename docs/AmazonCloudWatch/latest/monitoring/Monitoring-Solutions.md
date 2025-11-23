# CloudWatch observability solutions

CloudWatch observability solutions offer a catalog of readily available configurations to help you quickly implement monitoring for various AWS services and common workloads, such as Java Virtual Machines (JVM), Apache Kafka, Apache Tomcat, and NGINX. These solutions provide focused guidance on key monitoring tasks, including the installation and configuration of the CloudWatch agent, deployment of pre-defined custom dashboards, and setup of metric alarms. They are designed to assist developers and operations teams in leveraging AWS monitoring and observability tools more effectively.

The solutions include guidance on when to use specific observability features like Detailed Monitoring metrics for infrastructure, Container Insights for container monitoring, and Application Signals for application monitoring. By providing working examples and practical configurations, these solutions aim to simplify the initial setup process, allowing you to establish functional monitoring more quickly and customize as needed for their specific requirements.

To get started with observability solutions, visit the [observability solutions page](https://console.aws.amazon.com/cloudwatch/home?#settings:/observability-solutions "https://console.aws.amazon.com/cloudwatch/home?#settings:/observability-solutions") in the CloudWatch console.

For open-source solutions that work with Amazon Managed Grafana, see [Amazon Managed Grafana solutions](../../../grafana/latest/userguide/AMG_solutions.md "../../../grafana/latest/userguide/AMG_solutions.md")

Solutions that require CloudWatch agent are detailed below:

###### Topics

- [CloudWatch solution: JVM workload on Amazon EC2](Solution-JVM-On-EC2.md "Solution-JVM-On-EC2.md")
- [CloudWatch solution: NGINX workload on Amazon EC2](Solution-NGINX-On-EC2.md "Solution-NGINX-On-EC2.md")
- [CloudWatch solution: NVIDIA GPU workload on Amazon EC2](Solution-NVIDIA-GPU-On-EC2.md "Solution-NVIDIA-GPU-On-EC2.md")
- [CloudWatch solution: Kafka workload on Amazon EC2](Solution-Kafka-On-EC2.md "Solution-Kafka-On-EC2.md")
- [CloudWatch solution: Tomcat workload on Amazon EC2](Solution-Tomcat-On-EC2.md "Solution-Tomcat-On-EC2.md")
- [CloudWatch solution: Amazon EC2 health](Solution-EC2-Health.md "Solution-EC2-Health.md")

**How do solution dashboards work?**

The dashboards for CloudWatch solutions use search-powered variables (dropdowns) that allow you to explore and visualize different aspects of your workloads dynamically.

By combining the flexibility of search-powered variables with the pre-configured [metric widgets](create-and-work-with-widgets.md "create-and-work-with-widgets.md"), the dashboard provides deep insights into your workloads, enabling proactive monitoring,
troubleshooting, and optimization. This dynamic approach ensures that you can quickly adapt the dashboard to your specific monitoring needs, without the need for extensive customization or configuration.

**Do solutions support cross-Region observability?**

CloudWatch solution dashboards display metrics of the Region where the solution dashboard is created. However,
the solution dashboard doesn’t display metrics across multiple Regions. If you have a use case to view data
from multiple Regions in a single dashboard, you'll need to customize the dashboard JSON to add the Regions that you want to view.
To do this, use the `region` attribute of the metric format to query the metrics from different Regions.
For more information about modifying dashboard JSON, see
[Metric Widget: Format for Each Metric in the Array](../APIReference/CloudWatch-Dashboard-Body-Structure.md#CloudWatch-Dashboard-Properties-Metrics-Array-Format "../APIReference/CloudWatch-Dashboard-Body-Structure.md#CloudWatch-Dashboard-Properties-Metrics-Array-Format").

**Do solution dashboards support [Cross-account cross-Region CloudWatch console](Cross-Account-Cross-Region.md "Cross-Account-Cross-Region.md")?**

When using CloudWatch cross-account observability, solution dashboards in the central monitoring account display metrics from source accounts in the same Region. To differentiate metrics for similar workloads across accounts, provide unique grouping dimension values in agent configurations. For instance, assign distinct `ClusterName` values for Kafka brokers in different accounts for Kafka workload, enabling precise cluster selection and metric viewing in the dashboard.

**Do solution dashboards support [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md")?**

If you have enabled cross-account using Cross-account cross-Region CloudWatch console, you won't be able to use the solution dashboard created in the monitoring account to view metrics from source accounts. Instead, you'll need to create dashboards in the respective source accounts. However, you can create the dashboard in the source account and view it from the monitoring account by switching the account ID setting in the console.

**What are the limitations for a solution dashboard?**

Solution dashboards leverage Search expressions to filter and analyze metrics for the workloads. This enables dynamic views based on dropdown option selections. These search
expressions might return more than 500 time series, but each dashboard widget can't display more than 500 time series. If a metric search in the
solution dashboard results in more than 500 time series across all Amazon EC2; instances,
the graph displaying the top contributors might show inaccurate results. For more information about search expressions,
see [CloudWatch search expression syntax](search-expression-syntax.md "search-expression-syntax.md").

CloudWatch displays the metric information on the dashboards if you click the `i` icon on the dashboard widget. However,
this currently doesn’t work for dashboard widgets that use search expressions. The solution dashboards use search expressions,
so you won’t be able to see the metric description in the dashboard.

**Can I customize the agent configuration or the dashboard provided by a solution?**

You can customize the agent configuration and the dashboard. Be aware that if you
customize the agent configuration, you must update the dashboard accordingly or it will
display empty metric widgets. Also be aware that if CloudWatch releases a new version of a
solution, you might have to repeat your customizations if you apply the newer version of
the solution.

**How are solutions versioned?**

Each solution provides the most up-to-date instructions and resources. We always recommend using the latest version available. While the solutions themselves are not
versioned, the associated artifacts (such as CloudFormation templates for dashboards and agent installations) are versioned.

You can identify the version of a previously deployed artifact by checking the CloudFormation template's description field or the filename of the template you downloaded.
To determine if you're using the latest version, compare your deployed version with the one currently referenced in the solution documentation.
