# Creating an Amazon Redshift connection

## Permissions needed

Additional permissions are need to use Amazon Redshift clusters and Amazon Redshift serverless environments.
For more information on how to add permissions to ETL jobs, see
[Review IAM permissions needed for ETL jobs](../ug/setting-up.md#getting-started-min-privs-job "../ug/setting-up.md#getting-started-min-privs-job").

- redshift:DescribeClusters
- redshift-serverless:ListWorkgroups
- redshift-serverless:ListNamespaces

## Overview

When adding an Amazon Redshift connection, you can choose an existing Amazon Redshift connection or
create a new connection when adding a **Data source - Redshift** node in AWS Glue Studio.

AWS Glue supports both Amazon Redshift clusters and Amazon Redshift serverless environments.
When you create a connection, Amazon Redshift serverless environments display the **serverless** label
next to the connection option.

For more information on how to create a Amazon Redshift connection, see
[Moving data to and from Amazon Redshift](aws-glue-programming-etl-redshift.md#aws-glue-programming-etl-redshift-using "aws-glue-programming-etl-redshift.md#aws-glue-programming-etl-redshift-using").
