

# MSFTREL02-BP01 Implement comprehensive monitoring for potential failures across the application, AWS infrastructure, and network connectivity
<a name="msftrel02-bp01"></a>

 Monitoring your Microsoft application, AWS resources, and network connectivity enables prompt responses to both actual and potential failures, enhancing overall system reliability. 

 **Desired outcome:** Comprehensive monitoring across the Microsoft application, AWS infrastructure, and network components will enable early detection of issues and prompt response to potential failures, optimizing system reliability and performance. 

 **Common anti-patterns:** 
+  Only responding to issues after they cause significant disruptions, rather than proactively monitoring for potential problems. 
+  Monitoring individual components in isolation without considering the interconnected nature of the application, infrastructure, and network. 
+  Focusing monitoring efforts solely on the application layer while neglecting AWS infrastructure and network connectivity monitoring. 

 **Benefits of establishing this best practice:** 
+  Comprehensive monitoring enables quick identification and resolution of issues, reducing downtime and enhancing overall system stability. 
+  Continuous monitoring provides valuable insights into system behavior, allowing for data-driven optimizations and resource allocation. 
+  Proactive monitoring reduces the time and resources spent on troubleshooting, allowing IT teams to focus on strategic initiatives rather than firefighting. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Begin by identifying critical monitoring metrics across each layer (application, infrastructure, and network) and implement a primary monitoring solution like Amazon CloudWatch. Set up custom metrics and dashboards for Microsoft application-specific monitoring, configure detailed AWS resource monitoring, and establish network connectivity checks. 

 Set up automated alerting and aggregate logs. Define clear thresholds and escalation procedures, and implement automated responses where appropriate. 

 Regularly review and refine your monitoring parameters to maintain the effectiveness of the monitoring strategy. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Define and configure essential metrics and alarms for Microsoft workloads with thresholds appropriate to your specific environment and SLA requirements, including: 

   1.  SQL Server performance monitoring (CPU utilization, memory availability, deadlock detection, backup status) 

   1.  Active Directory health checks (authentication failures, replication status, SYSVOL synchronization) 

   1.  IIS or .NET application monitoring (application pool health, HTTP error rates, worker process status) 

   1.  Windows system alerts (disk space, memory utilization, critical service status) 

   1.  AWS infrastructure monitoring for underlying EC2, EBS, and network components 

1.  Create consolidated dashboards for unified visibility across your monitored components. 

1.  Set up topics and subscription endpoints for automated alerting based on predefined thresholds. 

1.  Implement centralized logging and configure log metric filters. 

1.  Establish automated remediation actions in response to specific alarm conditions. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Monitor workload resources](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/monitor-workload-resources.html) 
+  [Designing and implementing logging and monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html) 

 **Related tools:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Simple Notification Service](https://aws.amazon.com/sns/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 