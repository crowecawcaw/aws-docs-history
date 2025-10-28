Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Use case examples for user-defined functions (UDFs)

###### Note

Starting November 1, 2025,
Amazon Redshift will no longer support the creation of new Python UDFs.
Existing Python UDFs will continue to function until June 30, 2026.
Starting July 1, 2026, Amazon Redshift will no longer support Python
UDFs. We recommend that you migrate your existing Python UDFs to Lambda UDFs before November 1, 2025.
For information on creating and using Lambda UDFs, see [Scalar Lambda UDFs](udf-creating-a-lambda-sql-udf.md "udf-creating-a-lambda-sql-udf.md").
For information on converting existing Python UDFs to
Lambda UDFs, see the [blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

You can use user-defined functions to solve business problems by integrating Amazon Redshift with other components.
Following are some examples of how others have used UDFs for their use cases:

- [Accessing external components using Amazon Redshift Lambda UDFs](https://aws.amazon.com/blogs/big-data/accessing-external-components-using-amazon-redshift-lambda-udfs/ "https://aws.amazon.com/blogs/big-data/accessing-external-components-using-amazon-redshift-lambda-udfs/") –
  describes how Amazon Redshift Lambda UDFs work and walks through creating a Lambda UDF.
- [Translate and analyze text using SQL functions with Amazon Redshift, Amazon Translate, and Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/translate-and-analyze-text-using-sql-functions-with-amazon-redshift-amazon-translate-and-amazon-comprehend/ "https://aws.amazon.com/blogs/machine-learning/translate-and-analyze-text-using-sql-functions-with-amazon-redshift-amazon-translate-and-amazon-comprehend/") –
  provides prebuilt Amazon Redshift Lambda UDFs that you can install with a few clicks to translate, redact, and analyze text fields.
- [Access Amazon Location Service from Amazon Redshift](https://aws.amazon.com/blogs/big-data/access-amazon-location-service-from-amazon-redshift/ "https://aws.amazon.com/blogs/big-data/access-amazon-location-service-from-amazon-redshift/") –
  describes how to use Amazon Redshift Lambda UDFs to integrate with Amazon Location Service.
- [Data Tokenization with Amazon Redshift and Protegrity](https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/ "https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/") –
  describes how to integrate Amazon Redshift Lambda UDFs with the Protegrity Serverless product.
- [Amazon Redshift UDFs](https://github.com/aws-samples/amazon-redshift-udfs "https://github.com/aws-samples/amazon-redshift-udfs") –
  a collection of Amazon Redshift SQL, Lambda, and Python UDFs.
