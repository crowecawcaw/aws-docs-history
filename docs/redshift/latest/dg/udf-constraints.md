Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Python UDF constraints

Within the constraints listed in this topic, you can use UDFs anywhere you use the
Amazon Redshift built-in scalar functions. For more information, see [SQL functions reference](c_SQL_functions.md "c_SQL_functions.md").

Amazon Redshift Python UDFs have the following constraints:

- Python UDFs cannot access the network or read or write to the file
  system.
- The total size of user-installed Python libraries cannot exceed 100 MB.
- Amazon Redshift can only run one Python UDF at a time for provisioned clusters using
  automatic workload management (WLM) and for serverless workgroups. If you try to run more than
  one UDF concurrently, Amazon Redshift queues the remaining Python UDFs to run in the workload
  management queues. SQL UDFs don’t have a concurrency limit when using automatic WLM.
- When using manual WLM for provisioned clusters, the number of Python UDFs that can run
  concurrently per cluster is limited to one-fourth of the cluster’s total concurrency
  level. For example, a provisioned cluster with a concurrency of 15 can run a
  maximum of three concurrent Python UDFs.
- When using Python UDFs, Amazon Redshift doesn't support the SUPER and HLLSKETCH data types.
