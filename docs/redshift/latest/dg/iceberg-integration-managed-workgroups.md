Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managed workgroups

When you register a provisioned cluster or serverless namespace to the AWS Glue Data Catalog and create a catalog from it, AWS Glue
creates a managed workgroup to provide compute resources for any SQL query engine that accesses that catalog.
For example, an Amazon Athena user querying a table in a catalog would have their compute
requirements fulfilled by the managed workgroup’s Amazon Redshift compute resources. Managed workgroups use
Amazon Redshift compute resources, but are managed in AWS Glue.

Managed workgroups count toward the Amazon Redshift Serverless workgroup quota, which by default is 25. For more information, see
[Quotas and limits in Amazon Redshift](../mgmt/amazon-redshift-limits.md "../mgmt/amazon-redshift-limits.md")
in the _Amazon Redshift Management Guide_.

You can view general information, performance metrics, and query information for your managed workgroups in
the Amazon Redshift Serverless console. For more information, see
[Viewing properties for a workgroup](../mgmt/serverless-console-workgroups.md "../mgmt/serverless-console-workgroups.md")
in the _Amazon Redshift Management Guide_.
