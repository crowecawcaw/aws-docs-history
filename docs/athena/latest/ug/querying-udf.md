# Query with user defined functions

User Defined Functions (UDF) in Amazon Athena allow you to create custom functions to process
records or groups of records. A UDF accepts parameters, performs work, and then returns a
result.

To use a UDF in Athena, you write a `USING EXTERNAL FUNCTION` clause before a
`SELECT` statement in a SQL query. The `SELECT` statement
references the UDF and defines the variables that are passed to the UDF when the query runs.
The SQL query invokes a Lambda function using the Java runtime when it calls the UDF. UDFs
are defined within the Lambda function as methods in a Java deployment package. Multiple UDFs
can be defined in the same Java deployment package for a Lambda function. You also specify
the name of the Lambda function in the `USING EXTERNAL FUNCTION` clause.

You have two options for deploying a Lambda function for Athena UDFs. You can deploy the
function directly using Lambda, or you can use the AWS Serverless Application Repository. To find existing Lambda functions
for UDFs, you can search the public AWS Serverless Application Repository or your private repository and then deploy to
Lambda. You can also create or modify Java source code, package it into a JAR file, and
deploy it using Lambda or the AWS Serverless Application Repository. For example Java source code and packages to get you
started, see [Create and deploy a UDF using Lambda](udf-creating-and-deploying.md "udf-creating-and-deploying.md"). For more information about Lambda, see
[AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md"). For more information about AWS Serverless Application Repository, see the [AWS Serverless Application Repository Developer Guide](../../../serverlessrepo/latest/devguide.md "../../../serverlessrepo/latest/devguide.md").

For an example that uses UDFs with Athena to translate and analyze
text, see the AWS Machine Learning Blog article [Translate and analyze text using SQL functions with Amazon Athena, Amazon Translate, and
Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/translate-and-analyze-text-using-sql-functions-with-amazon-athena-amazon-translate-and-amazon-comprehend/ "https://aws.amazon.com/blogs/machine-learning/translate-and-analyze-text-using-sql-functions-with-amazon-athena-amazon-translate-and-amazon-comprehend/"), or watch the [video](udf-videos.md#udf-videos-xlate "udf-videos.md#udf-videos-xlate").

For an example of using UDFs to extend geospatial queries in Amazon Athena, see [Extend geospatial queries in Amazon Athena with UDFs and AWS Lambda](https://aws.amazon.com/blogs/big-data/extend-geospatial-queries-in-amazon-athena-with-udfs-and-aws-lambda/ "https://aws.amazon.com/blogs/big-data/extend-geospatial-queries-in-amazon-athena-with-udfs-and-aws-lambda/") in the
_AWS Big Data Blog_.

###### Topics

- [Videos on UDFs in Athena](udf-videos.md "udf-videos.md")
- [Considerations and limitations](udf-considerations-limitations.md "udf-considerations-limitations.md")
- [Query using UDF query syntax](udf-query-syntax.md "udf-query-syntax.md")
- [Create and deploy a UDF using Lambda](udf-creating-and-deploying.md "udf-creating-and-deploying.md")
