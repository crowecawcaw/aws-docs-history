# Best Practice 1.3 – Implement

application and database monitoring for SAP

Set up your application and database monitoring to provide information about its
internal state, status, and achievement of business outcomes. Some examples include
transaction response time, available work processes, queue depth, error and dump messages,
stalled batch jobs, and transaction throughput. Use this information to determine when a
corrective action is required.

**Suggestion 1.3.1 - Implement monitoring for databases supporting SAP
applications**

Continually monitor your SAP databases and establish alerts for common problems that
can affect SAP system availability and performance. Common monitoring items include the
following:

- Free space in data area
- Free space in logging area
- Excessive locking activity
- Cache utilization rates
- Average query response time
- Required security patches and hot fixes
- Top table sizes and growth
  Base alerting thresholds on healthy patterns of historical productive usage of your
  system. Continually review and adjust your alarm thresholds to prevent problems and to
  react to workload changes or growth.

For details on how to enable monitoring for your specific database, see your database
software provider installation and operational guides.

Consider Amazon CloudWatch Application Insights for SAP HANA databases to analyze metric patterns using historical
data to detect anomalies, and continuously track errors and exceptions from HANA, operating
system, and infrastructure logs.

- SAP on AWS Blog: [Set up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/")

**Suggestion 1.3.2 - Use SAP transactions and tools to understand the
SAP application**

Configure your SAP applications to provide information about their internal state,
status, and the achievement of business outcomes. Use this information to determine when a
response is required. Common monitoring items include the following:

- Availability of application (ASCS, PAS, AAS) and database services
- Number of active and concurrent users
- Availability of work processes for users
- Response time of user transactions
- Response time of batch and non-interactive transactions
- Error messages and dumps
- Failed jobs
- Full and slow queues
  Set up the SAP
  EarlyWatch Alert reporting system in SAP Solution Manager to create regular
  reports on the status of your SAP systems. Regularly review and remediate issues found in
  these reports to prevent problems and avoid interruptions to workload service.

- SAP Note: [2729186

* General Process of EWA Generation](https://launchpad.support.sap.com/#/notes/2729186 "https://launchpad.support.sap.com/#/notes/2729186") [Requires SAP Portal Access]

- SAP Documentation: [SAP Solution Manager 7.2 - Application Operations](http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html "http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html")
- SAP Lens [Performance efficiency]: [Best
  Practice 16.1 – Have data to evaluate performance](best-practice-16-1.md "best-practice-16-1.md")

**Suggestion 1.3.3 - Implement monitoring for your data recovery and
protection mechanisms**

Implement monitoring for mechanisms that safeguard your SAP data in the case of a
failure or disaster. Common monitoring items include:

- Alerts for regular database backups, for example, to Amazon S3 with the AWS
  Backint Agent
- Alerts for database replication, for example, HANA system replication failure or
  delays across Availability Zones
- Alerts for file storage backups, for example, an EBS snapshot, an Amazon EFS
  backup, or an Amazon FSx backup
- Alerts for recovery mechanisms which provide data resilience across Regions, for
  example, Amazon S3 buckets with cross-Region replication, Amazon S3 sync or
  CloudEndure Disaster Recovery
- Alerts for any recovery mechanisms which provide data resilience across accounts,
  for example, Amazon S3 buckets with same-Region replication to a WORM S3 bucket or
  logging account
  See the following links for further information:

- AWS Blog: [Monitor, Evaluate, and Demonstrate Backup Compliance with AWS Backup Audit
  Manager](https://aws.amazon.com/blogs/aws/monitor-evaluate-and-demonstrate-backup-compliance-with-aws-backup-audit-manager/ "https://aws.amazon.com/blogs/aws/monitor-evaluate-and-demonstrate-backup-compliance-with-aws-backup-audit-manager/")
- SAP Documentation: [SAP HANA System Replication Verification and Monitoring](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ba383103029f45fe92a98ecc1eef2f56.html?locale=en-US "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ba383103029f45fe92a98ecc1eef2f56.html?locale=en-US")

**Suggestion 1.3.4 - Expose SAP monitoring data outside of SAP tools
for independent observability**

SAP monitoring tools are limited to application and operating system level monitoring
and do not cover the wide range of supporting services that give an end-to-end view of SAP
service availability and health. Configure your SAP applications to provide metrics to a
more holistic, external monitoring and visualization tool of your choice.

Use the metrics collected in the previous best practices and externalize these
results such that you have an independent tool which can monitor, alert, and report on
trends. An independent tool allows observability, root cause analysis, historical and
trend reporting without being linked to the SAP system’s availability (that is, when SAP
is in a disaster or fault mode).

- SAP on AWS Blog: [Serverless Monitoring for SAP NetWeaver](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- SAP on AWS Blog: [Serverless Monitoring for SAP HANA](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- SAP on AWS Blog: [Set up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/")
- AWS Documentation: [Create a CloudWatch Custom Metric](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md")
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2 "https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2")
