After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Examples: Transforming Data

There are times when your application code must preprocess incoming records before
performing any analytics in Amazon Kinesis Data Analytics. This can happen for various reasons, such as when
records don't conform to the supported record formats, resulting in unnormalized columns in
the in-application input streams.

This section provides examples of how to use the available string functions to normalize
data, how to extract information that you need from string columns, and so on. The section
also points to date time functions that you might find useful.

## Preprocessing Streams with Lambda

For information about preprocessing streams with AWS Lambda, see [Preprocessing Data Using a Lambda Function](lambda-preprocessing.md "lambda-preprocessing.md").

###### Topics

- [Examples: Transforming String Values](examples-transforming-strings.md "examples-transforming-strings.md")
- [Example: Transforming
  DateTime Values](app-string-datetime-manipulation.md "app-string-datetime-manipulation.md")
- [Example: Transforming Multiple Data Types](app-tworecordtypes.md "app-tworecordtypes.md")
