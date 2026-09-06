

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Managed workgroups
<a name="iceberg-integration-managed-workgroups"></a>

 When you register a provisioned cluster or serverless namespace to the AWS Glue Data Catalog and create a catalog from it, AWS Glue creates a managed workgroup to provide compute resources for any SQL query engine that accesses that catalog. For example, an Amazon Athena user querying a table in a catalog would have their compute requirements fulfilled by the managed workgroup’s Amazon Redshift compute resources. Managed workgroups use Amazon Redshift compute resources, but are managed in AWS Glue. 

Managed workgroups count toward the Amazon Redshift Serverless workgroup quota, which by default is 25. For more information, see [Quotas and limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Management Guide*.

 You can view general information, performance metrics, and query information for your managed workgroups in the Amazon Redshift Serverless console. For more information, see [ Viewing properties for a workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-workgroups.html) in the *Amazon Redshift Management Guide*. 