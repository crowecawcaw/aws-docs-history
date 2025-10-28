# Supported Lambda blueprints

These blueprints demonstrate how you can create and use AWS Lambda functions to
transform data in your Amazon Data Firehose data streams.

###### To see the blueprints that are available in the AWS Lambda console

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**, and then choose **Use a
   blueprint**.
3. In the **Blueprints** field, search for the keyword
   `firehose` to find the Amazon Data Firehose Lambda blueprints.
   List of blueprints:

- **Process records sent to Amazon Data Firehose stream
  (Node.js, Python)**

This blueprint shows a basic example of how to process data in your Firehose data stream using AWS Lambda.

_Latest release date:_ November, 2016.

_Release notes:_ none.

- **Process CloudWatch Logs sent to Firehose**

This blueprint is deprecated. Do not use this blueprint. It might incur high
charges when the decompressed CloudWatch Logs data is more than 6MB (Lambda limit). For
information on processing CloudWatch Logs sent to Firehose, see [Writing to Firehose
Using CloudWatch Logs](writing-with-cloudwatch-logs.md "writing-with-cloudwatch-logs.md").

- **Convert Amazon Data Firehose stream records in syslog format
  to JSON (Node.js)**

This blueprint shows how you can convert input records in RFC3164 Syslog
format to JSON.

_Latest release date:_ Nov, 2016.

_Release notes:_ none.

###### To see the blueprints that are available in the AWS Serverless Application Repository

1. Go to [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo "https://aws.amazon.com/serverless/serverlessrepo").
2. Choose **Browse all
   applications**.
3. In the **Applications** field, search for the keyword
   `firehose`.
   You can also create a Lambda function without using a blueprint. See [Getting
   Started with AWS Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md").
