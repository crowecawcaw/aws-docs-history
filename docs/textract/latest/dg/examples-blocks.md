

# Tutorials

[Block](https://docs.aws.amazon.com/textract/latest/APIReference/API_Block.html) objects that are returned from Amazon Textract Core operations contain the results of text detection and text analysis operations, such as [AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/APIReference/API_AnalyzeDocument.html). The following Python tutorials show some of the different ways that you can use Block objects. For example, you can export table information to a comma-separated values (CSV) file.

The tutorials use synchronous Amazon Textract Core operations that return all results. If you want to use asynchronous operations such as [StartDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentAnalysis.html), you need to change the example code to accommodate multiple batches of returned `Block` objects. To make use of the asynchronous operations example, ensure that you have followed the instructions given at [Configuring Amazon Textract Core for asynchronous operations](api-async-roles.md).

For examples that show you other ways to use Amazon Textract Core, see [Additional code samples](other-examples.md).

**Topics**
+ [Prerequisites](#examples-prerequisites)
+ [Extracting key-value pairs from a form document](examples-extract-kvp.md)
+ [Exporting tables into a CSV file](examples-export-table-csv.md)
+ [Detecting text with an AWS Lambda function](lambda.md)
+ [Extracting and sending text to Amazon Comprehend for analysis](textract-to-comprehend.md)
+ [Additional code samples](other-examples.md)

## Prerequisites
<a name="examples-prerequisites"></a>

Before you can run the examples in this section, you have to configure your environment. 

**To configure your environment**

1. Give a user the `AmazonTextractFullAccess` permissions. For more information, see [Step 1: Set up an AWS account and create a user](setting-up.md).

1. Install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md).