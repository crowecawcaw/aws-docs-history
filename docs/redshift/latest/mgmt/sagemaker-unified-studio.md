Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using Amazon Sagemaker Unified Studio to query your databases in Amazon Redshift and the SageMaker lakehouse

Amazon SageMaker Unified Studio provides an off-console development environment and
supports SQL analytics on data in the SageMaker lakehouse, Amazon Redshift, and Amazon Athena for
SQL analytics. Navigate to Amazon SageMaker Unified Studio using the URL from your admin
and use your SSO or AWS credentials to log in. For more information about setting up
your first project, see [Getting
started](../../../sagemaker-unified-studio/latest/userguide/getting-started.md "../../../sagemaker-unified-studio/latest/userguide/getting-started.md") in the _Amazon SageMaker Unified Studio User
Guide_.

In Amazon SageMaker Unified Studio, you can perform [SQL
analytics](../../../sagemaker-unified-studio/latest/userguide/sql-query.md "../../../sagemaker-unified-studio/latest/userguide/sql-query.md") by running Amazon Redshift and Amazon Athena with the [query
editor](../../../sagemaker-unified-studio/latest/userguide/query-editor-navigate.md "../../../sagemaker-unified-studio/latest/userguide/query-editor-navigate.md"). Use the query editor to write and run queries, view results, and
share your work with your team. Run queries against your Redshift data warehouses
in your AWS accounts (within the same account and across your other
AWS accounts), build SQL queries for both Redshift and Athena using the same
interface and schedule the SQL queries using Amazon Managed Workflows for Apache Airflow. You can also use Amazon Q
generative SQL to generate SQL from natural language.
