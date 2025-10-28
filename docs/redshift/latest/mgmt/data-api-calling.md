Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Calling the Data API

You can call the Data API or the AWS CLI to run SQL statements on your cluster or
serverless workgroup. The primary operations to run SQL statements are [`ExecuteStatement`](../../../redshift-data/latest/APIReference/API_ExecuteStatement.md "../../../redshift-data/latest/APIReference/API_ExecuteStatement.md") and [`BatchExecuteStatement`](../../../redshift-data/latest/APIReference/API_BatchExecuteStatement.md "../../../redshift-data/latest/APIReference/API_BatchExecuteStatement.md") in the _Amazon Redshift Data API
Reference_. The Data API supports the programming languages that are
supported by the AWS SDK. For more information on these, see [Tools to Build on AWS](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").

To see code examples of calling the Data API, see [Getting Started with Redshift Data API](https://github.com/aws-samples/getting-started-with-amazon-redshift-data-api#getting-started-with-redshift-data-api "https://github.com/aws-samples/getting-started-with-amazon-redshift-data-api#getting-started-with-redshift-data-api") in _GitHub_. This
repository has examples of using AWS Lambda to access Amazon Redshift data from Amazon EC2, AWS Glue Data Catalog,
and Amazon SageMaker Runtime. Example programming languages include Python, Go, Java, and
Javascript.

You can call the Data API using the AWS CLI.

The following examples use the AWS CLI to call the Data API. To run the examples,
edit the parameter values to match your environment. In many of the examples a
`cluster-identifier` is provided to run against a cluster. When you run
against a serverless workgroup, you provide a `workgroup-name` instead. These
examples demonstrate a few of the Data API operations. For more information, see
the _AWS CLI Command Reference_.

Commands in the following examples have been split and formatted for readability. Not
all parameters and responses are shown in all examples. For
the API definition of the complete request syntax, request parameters, response
syntax, and response elements, see the [Amazon Redshift Data API
Reference](../../../redshift-data/latest/APIReference.md "../../../redshift-data/latest/APIReference.md").
