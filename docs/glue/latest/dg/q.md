# Amazon Q data integration in AWS Glue

Amazon Q data integration in AWS Glue is a new generative AI capability of AWS Glue that enables data engineers and ETL developers to build data integration jobs using natural language. Engineers and developers can ask Amazon Q to author jobs, troubleshoot issues, and answer questions about AWS Glue and data integration.

## What is Amazon Q?

###### Note

Powered by Amazon Bedrock: AWS implements [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md"). Because Amazon Q data integration is built on Amazon Bedrock, users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of artificial intelligence (AI).

Amazon Q is a generative artificial intelligence (AI) powered conversational assistant that can help you understand, build, extend, and operate AWS applications. The model that powers Amazon Q has been augmented with high quality AWS content to get you more complete, actionable, and referenced answers to accelerate your building on AWS. For more information, see [What is Amazon Q?](../../../amazonq/latest/aws-builder-use-ug/what-is.md "../../../amazonq/latest/aws-builder-use-ug/what-is.md")

## What is Amazon Q data integration in AWS Glue?

Amazon Q data integration in AWS Glue includes the following capabilities:

- **Chat** – Amazon Q data integration in AWS Glue can answer natural language questions in English about AWS Glue and data integration domains like AWS Glue source and destination connectors, AWS Glue ETL jobs, Data Catalog, crawlers and AWS Lake Formation, and other feature documentation, and best practices. Amazon Q data integration in AWS Glue responds with step-by-step instructions, and includes references to its information sources.
- **Data integration code generation** – Amazon Q data integration in AWS Glue can answer questions about AWS Glue ETL scripts, and generate new code given a natural language question in English.
- **Troubleshoot** – Amazon Q data integration in AWS Glue is purpose built to help you understand errors in AWS Glue jobs and provides step-by-step instructions, to root cause and resolve your issues.

###### Note

Amazon Q data integration in AWS Glue does not use the context of your conversation to inform future responses for the duration of your conversation. Each conversation with Amazon Q data integration in AWS Glue is independent of your prior or future conversations.

## Working with Amazon Q data integration in AWS Glue?

In the Amazon Q panel you can request Amazon Q generate code for an AWS Glue ETL script, or answer a question on AWS Glue features or troubleshooting an error. The response is an ETL script in PySpark with step-by-step instructions to customize the script, review and execute it. For questions, the response is generated based on the data integration knowledge base with a summary and source URL for references.

For example, you can ask Amazon Q to "_Please provide a Glue script that reads from Snowflake, renames the fields, and writes to Redshift_" and in response, Amazon Q data integration in AWS Glue will return an AWS Glue job script that can perform the requested action. You can review the generated code to ensure that it fulfills the requested intent. If satisfied, you can deploy it as an AWS Glue job in production. You can troubleshoot jobs by asking the integration to explain errors and failures, and to propose solutions. Amazon Q can answer questions about AWS Glue or data integration best practices.

![An example of using Amazon Q data integration in AWS Glue.](/images/glue/latest/dg/images/q-chat-experience-1.gif)

The following are example questions that demonstrate how Amazon Q data integration in AWS Glue can help you build on AWS Glue:

AWS Glue ETL code generation:

- Write an AWS Glue script that reads JSON from S3, transforms fields using apply mapping and writes to Amazon Redshift
- How do I write an AWS Glue script for reading from DynamoDB, applying the DropNullFields transform and writing to S3 as Parquet?
- Give me an AWS Glue script that reads from MySQL, drops some fields based on my business logic, and writes to Snowflake
- Write an AWS Glue job to read from DynamoDB and write to S3 as JSON
- Help me develop an AWS Glue script for AWS Glue Data Catalog to S3
- Write an AWS Glue job to read JSON from S3, drop nulls and write to Redshift

AWS Glue feature explanations:

- How do I use AWS Glue Data Quality?
- How to use AWS Glue job bookmarks?
- How do I enable AWS Glue autoscaling?
- What is the difference between AWS Glue dynamic frames and Spark data frames?
- What are the different types of connections supported by AWS Glue?

AWS Glue troubleshooting:

- How to troubleshoot Out Of Memory (OOM) errors on AWS Glue jobs?
- What are some error messages you may see when setting up AWS Glue Data Quality and how can you fix them?
- How do I fix an AWS Glue job with the error Amazon S3 access denied?
- How do I resolve issues with data shuffle on AWS Glue jobs?

## Best practices for interacting with Amazon Q data integration

The following are best practices for interacting with Amazon Q data integration:

- When interacting with Amazon Q data integration, ask specific questions, iterate when you have complex requests, and verify the answers for accuracy.
- When providing data integration prompts in natural language, be as specific as possible to help the assistant understand exactly what you need. Instead of asking "extract data from S3," provide more details like “write an AWS Glue script that extracts JSON files from S3.”
- Review the generated script before running it to ensure accuracy. If the generated script has errors or does not match your intent, provide instructions to the assistant on how to correct it.
- Generative AI technology is new and there can be mistakes, sometimes called hallucinations, in the responses. Test and review all code for errors and vulnerabilities before using it in your environment or workload.

## Amazon Q data integration in AWS Glue service improvement

To help Amazon Q data integration in AWS Glue provide the most relevant information about AWS services, we may use certain content from Amazon Q, such as questions that you ask Amazon Q and its responses, for service improvement.

For information about what content we use and how to opt out, see [Amazon Q Developer service improvement](../../../amazonq/latest/qdeveloper-ug/service-improvement.md "../../../amazonq/latest/qdeveloper-ug/service-improvement.md") in the _Amazon Q Developer User Guide_.

## Considerations

Consider the following items before you use Amazon Q data integration in AWS Glue:

- Currently, the code generation only works with PySpark kernel. The generated code is for AWS Glue jobs based on Python Spark.
- For information about the supported combinations of code generation abilities of Amazon Q data integration in AWS Glue, see [Supported code generation abilities](q-supported-actions.md "q-supported-actions.md").
