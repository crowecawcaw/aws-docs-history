

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Usage metrics for autonomics operations
<a name="t_autonomics-usage-metrics"></a>

If you've enabled extra compute resources for automatic optimizations, you can see information about your billed autonomics usage using the Amazon Redshift console. For more information on autonomics metrics on the console for serverless workgroups, see the resource management section in [ Amazon Redshift Serverless console](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console.html) in the *Amazon Redshift Management Guide*.

The following system tables hold usage metrics about autonomics:
+ [SYS\_EXTRA\_COMPUTE\_FOR\_AUTOMATIC\_OPTIMIZATION](SYS_EXTRA_COMPUTE_FOR_AUTOMATIC_OPTIMIZATION.md) ‐ Use SYS\_EXTRA\_COMPUTE\_FOR\_AUTOMATIC\_OPTIMIZATION to see the amount of time that Amazon Redshift runs provisioned cluster autonomics operations in a given usage period.
+ [SYS\_AUTOMATIC\_OPTIMIZATION](SYS_AUTOMATIC_OPTIMIZATION.md) ‐ Use SYS\_AUTOMATIC\_OPTIMIZATION to see detailed information on autonomics operations for both provisioned clusters and serverless workgroups.
+ [SYS\_SERVERLESS\_USAGE](SYS_SERVERLESS_USAGE.md) ‐ Use SYS\_SERVERLESS\_USAGE to see the amount of time that Amazon Redshift runs serverless workgroup autonomics operations in a given usage period.