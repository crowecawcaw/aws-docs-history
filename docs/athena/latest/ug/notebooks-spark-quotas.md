# Understand service quotas for Athena for

Spark

_Service quotas_, also known as _limits_, are the
maximum number of service resources or operations that your AWS account can use. For more
information about the service quotas for other AWS services that you can use with
Amazon Athena for Spark, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the
_Amazon Web Services General Reference_.

###### Note

New AWS accounts might have initial lower quotas that can increase over time.
Amazon Athena for Apache Spark monitors account usage within each AWS Region, and then
automatically increases the quotas based on your usage. If your requirements exceed the
stated limits, contact customer support.

The following table lists the service quotas for Amazon Athena for Apache Spark.

| Name                                 | Default | Adjustable | Description                                                                                                                                                                                                                                                                          |
| ------------------------------------ | ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Apache Spark DPU concurrency         | 160     | No         | The maximum number of data processing units (DPUs) that you can consume concurrently for Apache Spark calculations for a single account in the current AWS Region. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. |
| Apache Spark session DPU concurrency | 60      | No         | The maximum number of DPUs you can consume concurrently for an Apache Spark calculation within a session.                                                                                                                                                                            |
