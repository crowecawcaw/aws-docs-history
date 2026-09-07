

# MSFTOPS01-BP01 Implement infrastructure monitoring for your Microsoft workload
<a name="msftops01-bp01"></a>

 The implementation of infrastructure monitoring for Microsoft workloads on AWS will provide comprehensive visibility into system performance, resource utilization, and application health. This monitoring solution will detect anomalies in real time, generate actionable alerts, and enable rapid troubleshooting of issues before they impact end users. Consider leveraging Microsoft Performance Counters to cover the basic infrastructure monitoring for your Microsoft workload servers. Besides operating system and performance metrics, the counters will be expanded according to the Microsoft product deployed, such as SQL Server, Internet Information Services (IIS), Active Directory Federation Services, and others. The Performance Counters can also be integrated with monitoring solutions, like Amazon CloudWatch, Amazon Managed Service for Prometheus, and Amazon Managed Grafana. 

 **Desired outcome:** Establish comprehensive infrastructure monitoring that provides real-time visibility into the health and performance of your Microsoft workload components, enabling proactive issue identification and resolution while leveraging both Microsoft-native monitoring capabilities and AWS monitoring services for optimal observability. 

 **Common anti-patterns:** 
+  Relying solely on basic system monitoring without leveraging Microsoft Performance Counters, missing critical application-specific metrics that could indicate performance issues or potential failures before they impact users. 
+  Implementing monitoring in silos without integrating Microsoft Performance Counters with centralized monitoring solutions, leading to fragmented visibility and delayed incident response across the Microsoft workload infrastructure. 
+  Monitoring only during business hours or reactive monitoring after issues occur, rather than establishing continuous, proactive monitoring that can predict and prevent problems before they affect workload availability. 

 **Benefits of establishing this best practice:** 
+  Enhanced visibility and proactive issue detection through comprehensive monitoring of both operating system metrics and Microsoft product-specific performance counters, enabling early identification of potential problems before they impact business operations. 
+  Improved operational efficiency by integrating Microsoft Performance Counters with AWS monitoring services like Amazon CloudWatch, providing centralized dashboards, automated alerting, and streamlined incident response processes. 
+  Better capacity planning and performance optimization through detailed metrics collection across all Microsoft workload components, enabling data-driven decisions for resource allocation and performance tuning. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing comprehensive infrastructure monitoring for Microsoft workloads requires a strategic approach that combines Microsoft-native monitoring capabilities with AWS services. Start by identifying the Microsoft products in your environment and their specific Performance Counters, then configure collection and integration with AWS monitoring services. This approach ensures you capture both standard system metrics and application-specific indicators that are crucial for maintaining optimal performance and availability of your Microsoft workloads. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Inventory your Microsoft workload components and identify relevant Performance Counters for each product (Windows Server, SQL Server, IIS, and Active Directory). 

1.  Install and configure the Amazon CloudWatch Agent on Windows instances to collect Performance Counters and system metrics. 

1.  Configure custom Performance Counter collection for Microsoft-specific applications and services running in your environment. 

1.  Set up Amazon CloudWatch dashboards to visualize key performance metrics and create a centralized monitoring view. 

1.  Establish Amazon CloudWatch alarms and notifications for critical performance thresholds and anomaly detection. 

1.  Integrate with Amazon Managed Service for Prometheus and Amazon Managed Grafana for advanced monitoring and visualization capabilities. 

1.  Implement automated response mechanisms using AWS Systems Manager Automation for common performance issues. 

1.  Establish regular review processes to evaluate monitoring effectiveness and adjust thresholds based on workload behavior. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Recommended metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/application-insights-recommended-metrics.html) 
+  [Monitoring Windows pods with Prometheus and Grafana](https://aws.amazon.com/blogs/containers/monitoring-windows-pods-with-prometheus-and-grafana/) 
+  [Use AWS Systems Manager to enable CloudWatch memory metrics for Windows Server Amazon EC2 instances](https://aws.amazon.com/blogs/modernizing-with-aws/use-aws-systems-manager-to-enable-cloudwatch-memory-metrics-for-windows-server-amazon-ec2-instances/) 

 **Related tools:** 
+  [Collect metrics, logs, and traces using the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) 
+  [Using Amazon CloudWatch Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 
+  [Amazon Managed Grafana - Grafana dashboards](https://aws.amazon.com/grafana/) 
+  [Prometheus Windows Exporter](https://github.com/prometheus-community/windows_exporter) 