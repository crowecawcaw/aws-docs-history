Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Create and configure a target

Amazon Redshift data warehouse

In this step, you create and configure a target Amazon Redshift data warehouse, such as a Redshift Serverless
workgroup or a provisioned cluster. If you already have a Amazon Redshift data warehouse configured
for use with zero-ETL integrations, you can skip this step.

Your target data warehouse must have the following characteristics:

- Running Amazon Redshift Serverless or a provisioned cluster of an RA3 node type.
- Has case sensitivity (`enable_case_sensitive_identifier`) turned on. For
  more information, see [Turn on case sensitivity for your
  data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
- Encrypted, if your target data warehouse is an Amazon Redshift provisioned cluster. For more
  information, see [Amazon Redshift database encryption](working-with-db-encryption.md "working-with-db-encryption.md").
- Created in the same AWS Region as the integration source.
  To create your target data warehouse for your zero-ETL integrations, see one of the following
  topics depending on your deployment type:

- To create an Amazon Redshift provisioned cluster, see [Creating a cluster](create-cluster.md "create-cluster.md").
- To create an Amazon Redshift Serverless workgroup with a namespace, see [Creating
  a workgroup with a namespace](serverless-console-workgroups-create-workgroup-wizard.md "serverless-console-workgroups-create-workgroup-wizard.md").
  When you create a provisioned cluster, Amazon Redshift also creates a default parameter group.
  You can't edit the default parameter group. However, you can create a custom parameter
  group before creating a new cluster and then associate it with the cluster. Or, you can edit
  the parameter group that will be associated with the created cluster. You must also turn on
  case sensitivity for the parameter group either when creating the custom parameter group or
  when editing a current one to use zero-ETL integrations.

To create a custom parameter group using the Amazon Redshift console or the AWS CLI, see [Creating a
parameter group](parameter-group-create.md "parameter-group-create.md").
