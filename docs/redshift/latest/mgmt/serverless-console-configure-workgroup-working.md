Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Workgroups

With Amazon Redshift Serverless, you can create and manage workgroups to isolate and
control compute resources for different workloads or users. Workgroups allow you to
set configuration options like memory and concurrency scaling limits, and prioritize
query execution across workloads. The compute-related workgroup groups together
compute resources like RPUs and VPC subnet groups.
