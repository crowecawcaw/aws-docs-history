Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Usage metrics for autonomics operations

If you've enabled extra compute resources for automatic optimizations, you can see
information about your billed autonomics usage using the Amazon Redshift console.
For more information on autonomics metrics on the console for
serverless workgroups, see the resource management section in
[Amazon Redshift Serverless console](../mgmt/serverless-console.md "../mgmt/serverless-console.md") in the _Amazon Redshift Management Guide_.

The following system tables hold usage metrics about autonomics:

- [SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION](SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION.md "SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION.md") ‐
  Use SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION to see the amount of time that Amazon Redshift
  runs provisioned cluster autonomics operations in a given usage period.
- [SYS_AUTOMATIC_OPTIMIZATION](SYS_AUTOMATIC_OPTIMIZATION.md "SYS_AUTOMATIC_OPTIMIZATION.md") ‐
  Use SYS_AUTOMATIC_OPTIMIZATION to see detailed information on autonomics operations for both provisioned clusters and serverless workgroups.
- [SYS_SERVERLESS_USAGE](SYS_SERVERLESS_USAGE.md "SYS_SERVERLESS_USAGE.md") ‐
  Use SYS_SERVERLESS_USAGE to see the amount of time that Amazon Redshift runs serverless workgroup autonomics operations in a given usage period.
