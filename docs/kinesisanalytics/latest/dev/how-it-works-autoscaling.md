After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Automatically Scaling Applications to Increase

Throughput

Amazon Kinesis Data Analytics elastically scales your application to accommodate the data throughput of your
source stream and your query complexity for most scenarios. Kinesis Data Analytics provisions capacity in the
form of Kinesis Processing Units (KPU). A single KPU provides you with the memory (4 GB) and
corresponding computing and networking.

The default limit for KPUs for your application is 64. For instructions on how to request an increase to this limit, see
**To request a limit increase** in [Amazon Service Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").
