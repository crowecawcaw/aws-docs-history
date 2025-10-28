Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data tokenization

_Tokenization_ is the process of replacing actual values
with opaque values for data security purposes. Security-sensitive applications use
tokenization to replace sensitive data such as personally identifiable information (PII)
or protected health information (PHI) with tokens to reduce the security risks.
_Detokenization_ reverses tokens with actual values
for authorized users with appropriate security policies.

For integration with third-party tokenization services, you can use Amazon Redshift user-defined functions
(UDFs) that you create using [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/"). For more information, see [Lambda user-defined functions](../dg/udf-creating-a-lambda-sql-udf.md "../dg/udf-creating-a-lambda-sql-udf.md") in the _Amazon Redshift Database Developer Guide_. For example, see [Protegrity](https://www.protegrity.com/how-we-work/partners/aws-data-protection "https://www.protegrity.com/how-we-work/partners/aws-data-protection").

Amazon Redshift sends tokenization requests to a tokenization server accessed through a REST API or
predefined endpoint. Two or more complimentary Lambda functions process the tokenization
and detokenization requests. For this processing, you can use Lambda functions provided
by a third-party tokenization provider. You can also use Lambda functions that you
register as Lambda UDFs in Amazon Redshift.

For example, suppose that a query is submitted that invokes a tokenization or detokenization
UDF on a column. The Amazon Redshift cluster spools the applicable rows of arguments and sends
those rows in batches to the Lambda function in parallel. The data transfers between the
Amazon Redshift compute nodes and Lambda in a separate, isolated network connection that's not
accessible to clients. The Lambda function passes the data to the tokenization server
endpoint. The tokenization server tokenizes or detokenizes the data as necessary and
returns it. The Lambda functions then transmit the results to the Amazon Redshift cluster for
further processing, if necessary, and then return the query results.
