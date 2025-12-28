# Monitoring Oracle GoldenGate

When you use Oracle GoldenGate for replication, make sure that the Oracle GoldenGate process is up and running and
the source and target databases are synchronized. You can use the following monitoring
tools:

- [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") is a monitoring service that is used in
  this pattern to monitor GoldenGate error logs.
- [Amazon SNS](../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md "../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md") is a message notification service that is
  used in this pattern to send email notifications.
  For detailed instructions, see [Monitor Oracle GoldenGate logs by using Amazon CloudWatch](../../../prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.md "../../../prescriptive-guidance/latest/patterns/monitor-oracle-goldengate-logs-by-using-amazon-cloudwatch.md").
