Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# max_concurrency_scaling_clusters

## Values (default in

bold)

**1**, 0 to 10

## Description

Sets the maximum number of concurrency scaling clusters allowed when concurrency scaling is enabled.
Increase this value if more concurrency scaling is required. Decrease this value to reduce the usage of concurrency scaling clusters and the resulting billing charges.

The maximum number of concurrency scaling clusters is an adjustable quota.
For more information, see [Amazon Redshift quotas](../mgmt/amazon-redshift-limits.md#amazon-redshift-limits-quota "../mgmt/amazon-redshift-limits.md#amazon-redshift-limits-quota") in the
_Amazon Redshift Management Guide_.
