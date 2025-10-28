# Analyze

After a security event is identified and reported, the next step is to analyze whether the reported event is a
false positive or a real incident. AMS uses automation and manual investigative techniques to handle security events.
The analysis includes investigation of logs from different detection sources such as network traffic logs, host
logs,CloudTrail events, AWS service logs and so on. The analysis also looks for patterns that show an anomalous behavior by correlation.

Your partnership is required to understand context specific to the account environment and to establish what is normal for your account and workloads. This helps AMS identify an anomaly faster and to an accelerated incident response.

## Handle communications from AMS about security events

AMS keeps you informed during the investigation by engaging your security contacts through an incident
ticket. Your AMS cloud service delivery manager (CSDM) and AMS cloud architect (CA) are the point
of contacts to reach out to for any communication during an active security investigation.

Communication includes automated notification when a security alert is generated, communication after event analysis,
establishing call bridges and the ongoing delivery of artifacts such as log files, snapshot of infected resources, and getting
investigation results to you during the security event.

Standard fields included in AMS security alert notifications are listed below. These fields provide
you with information so that you can route events to the appropriate teams within your organization for remediation.

- Finding Type
- Finding Identifier (Where relevant)
- Finding Severity
- Finding Description
- Finding created Date & Time
- AWS Account Id
- Region (Where relevant)
- AWS Resources (IAM user/role/policy, EC2, S3, EKS)

Additional fields are provided depending on the Finding Type, for example EKS Findings include Pod, Container, and Cluster details.
