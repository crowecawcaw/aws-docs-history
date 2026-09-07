

# MSFTREL03-BP03 Implement automated feedback loops
<a name="msftrel03-bp03"></a>

 Automated feedback loops are critical for Microsoft workloads due to their complex interdependencies and the need for continuous monitoring of performance patterns, security posture, and operational effectiveness. Microsoft environments require systematic approaches to identify trends, measure improvement initiatives, and translate monitoring investments into actionable insights for maintaining system reliability and security. 

 **Desired outcome:** The implementation of automated feedback loops establishes comprehensive monitoring and continuous improvement mechanisms through Amazon CloudWatch dashboards, automated vulnerability assessments, and metrics-driven compliance reporting, enabling data-driven decision-making and proactive risk management for Windows workloads on AWS. 

 **Common anti-patterns:** 
+  Relying solely on manual monitoring and reactive troubleshooting instead of implementing automated alerts and dashboards 
+  Conducting unplanned or inconsistent vulnerability assessments without a standardized schedule or automated scanning process 
+  Failing to maintain a prioritized improvement backlog, addressing issues randomly rather than based on quantifiable risk metrics and business impact 

 **Benefits of establishing this best practice:** 
+  Custom CloudWatch dashboards provide real-time insights into system performance and security patterns, enabling faster issue detection and resolution. 
+  Regular automated vulnerability assessments help identify and address potential threats before they can be exploited, improving overall security posture. 
+  A prioritized backlog based on risk and business impact allocates resources efficiently to address the most critical issues first. 
+  Automated compliance reporting using CloudWatch metrics and alarms streamlines the audit process and helps maintain ongoing regulatory adherence with less manual effort. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implement automated feedback loops by creating custom CloudWatch dashboards to monitor patterns and resolution times. Set up regular vulnerability assessments for EC2 instances running Windows workloads, and maintain a continuous improvement backlog prioritized by risk and business impact. Use CloudWatch metrics and alarms to monitor the effectiveness of implemented controls and automate compliance reporting. 

 Begin by creating custom dashboards that display key metrics for Windows workloads. Next, establish automated vulnerability scanning for EC2 instances on a regular schedule. Develop a process for maintaining and prioritizing a continuous improvement backlog based on identified risks and business impact. Finally, configure CloudWatch metrics and alarms to monitor control effectiveness and automate compliance reporting, verifying that each component works together in a cohesive feedback loop. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Set up specialized CloudWatch dashboards for Microsoft workloads including: 

   1.  SQL Server metrics (connection pools, deadlocks, wait statistics, backup status) 

   1.  IIS or .NET performance (request queues, application pool health, session state) 

   1.  Active Directory monitoring (authentication failures, replication status, LDAP queries) 

   1.  Windows system performance (memory usage, disk I/O, Event Logs) 

   1.  Exchange or SharePoint service health dashboards. 

1.  Focus on key Windows Performance Counters to drive continual improvement, such as: 

   1.  \\Memory\\Available MBytes 

   1.  \\Processor(\_Total)\\% Processor Time 

   1.  \\PhysicalDisk(\_Total)\\Avg. Disk Queue Length 

   1.  Critical Windows Event Log patterns (Security Event ID 4625 for failed logons, System Event ID 6008 for unexpected shutdowns) 

   1.  Application-specific metrics like \\SQLServer:General Statistics\\User Connections and \\Web Service(\_Total)\\Current Connections 

1.  Enable Amazon Inspector for automated vulnerability assessments on Windows EC2 instances, which automatically discovers supported Windows instances and performs continuous scanning every 6 hours by default. Configure custom scan schedules using SSM associations and use Inspector's integration with Systems Manager to assess operating system vulnerabilities, software packages, and network reachability for comprehensive security monitoring. 

1.  Create and maintain a centralized improvement backlog system with clear risk scoring and business impact criteria. 

1.  Implement alarms with appropriate thresholds for identified key performance and security metrics. 

1.  Establish automated compliance reporting workflows using metrics and AWS reporting tools. 

1.  Develop documentation and runbooks for responding to automated alerts and managing the continuous improvement process. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) 