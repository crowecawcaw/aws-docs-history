# Best Practice 9.1 – Understand your

strategy for SAP application and database security event analysis

Without keeping security logs at the appropriate levels of granularity, vital data
required for incident response, forensic security analysis, and threat modeling can be
lost. SAP security staff must be able to evaluate potential security incidents affecting
SAP systems in alignment with your business security requirements. For SAP workloads
running on AWS, the AWS services described in the Well-Architected Framework Security
Pillar are a helpful starting point in conjunction with the following suggestions.

- Well-Architected Framework [Security]: [Detection – Configure](../security-pillar/configure.md "../security-pillar/configure.md")

**Suggestion 9.1.1 – Determine which logs are required to detect
security events**

For individual SAP software and supported databases refer to the SAP NetWeaver Guide
Finder as well as the SAP NetWeaver Security Guide for what logs might be applicable (for
example, [read access logging](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/631dfbf00a604784b69fc30570bfb69d.html "https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/631dfbf00a604784b69fc30570bfb69d.html")). In addition, review the SAP advisory on [security logging](https://help.sap.com/viewer/1a93b7a44ac146b5ad9b6fd95c1223cc/LATEST/en-US/182e167819f6405792686e94c177b9eb.html "https://help.sap.com/viewer/1a93b7a44ac146b5ad9b6fd95c1223cc/LATEST/en-US/182e167819f6405792686e94c177b9eb.html") and related topics surrounding best practices for your
development activities.

- SAP Documentation: [SAP
  NetWeaver Guide Finder](https://help.sap.com/viewer/nwguidefinder "https://help.sap.com/viewer/nwguidefinder")
- SAP Documentation: [ABAP Platform Security Guide](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4aaf6fd65e233893e10000000a42189c.html "https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4aaf6fd65e233893e10000000a42189c.html")
- SAP Documentation: [Security Logging](https://help.sap.com/viewer/1a93b7a44ac146b5ad9b6fd95c1223cc/LATEST/en-US/182e167819f6405792686e94c177b9eb.html "https://help.sap.com/viewer/1a93b7a44ac146b5ad9b6fd95c1223cc/LATEST/en-US/182e167819f6405792686e94c177b9eb.html")

**Suggestion 9.1.2 – Develop mechanisms for storing and analyzing
logs**

Having relevant data regarding potential security events is necessary for any secure
SAP installation, but it is equally important to store that data securely and have the
necessary tools for searching and analyzing the data in an efficient and timely manner. One
option within AWS includes using the [CloudWatch Agent](../../../systems-manager/latest/userguide/monitoring-cloudwatch-agent.md "../../../systems-manager/latest/userguide/monitoring-cloudwatch-agent.md") to store instance logs and SAP application logs relevant to
security in an [Amazon CloudWatch log group](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md"). Such logs could also be [exported to
Amazon S3](../../../AmazonCloudWatch/latest/logs/S3Export.md "../../../AmazonCloudWatch/latest/logs/S3Export.md") for holistic log analysis and for integration with [third-party log
analytics solutions](https://aws.amazon.com/marketplace/solutions/control-tower/siem "https://aws.amazon.com/marketplace/solutions/control-tower/siem").

Refer to the following for help with assembling, combining, and analyzing your SAP on
AWS security logs:

- SAP Lens [Security]: [Suggestion 7.4.4 -
  Consolidate user and authorization events in a Security Information and Event
  Management (SIEM) system for analysis](best-practice-7-4.md "best-practice-7-4.md")
- SAP on AWS Blog: [Set up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/")
- SAP on AWS Blog: [SAP HANA monitoring: A serverless approach using Amazon CloudWatch](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- SAP on AWS Blog: [SAP Monitoring: A serverless approach using Amazon CloudWatch](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/")

**Suggestion 9.1.3 – Use machine learning to analyse and determine
events of importance**

Consider applying pattern recognition, anomaly detection, or both to security logs to
assist in determining potential threats and events of importance to your SAP workload. AWS
managed services, such as [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") and [Amazon
GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/"), can help, combined with third-party security solutions from the AWS
Marketplace.

- AWS Video: [An Overview
  of AWS Security Hub CSPM](https://www.youtube.com/watch?v=oBac-GAoZJ8 "https://www.youtube.com/watch?v=oBac-GAoZJ8")
- AWS Documentation: [Getting started with GuardDuty](../../../guardduty/latest/ug/guardduty_settingup.md "../../../guardduty/latest/ug/guardduty_settingup.md")
