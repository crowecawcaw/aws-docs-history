# Tutorial: Use AWS Lambda with Amazon Kinesis Data Streams

In this tutorial, you create a Lambda function to consume events from a Kinesis data stream.
In this example scenario, a custom application writes records to a Kinesis data stream.
AWS Lambda then polls this data stream and, when it detects new data records, invokes your
Lambda function. AWS Lambda then executes the Lambda function by assuming the execution role
that you specified when you created the Lambda function.

For the detailed step by step instructions, see [Tutorial:
Using AWS Lambda with Amazon Kinesis](../../../lambda/latest/dg/with-kinesis-example.md "../../../lambda/latest/dg/with-kinesis-example.md").

###### Note

This tutorial assumes that you have some knowledge of basic Lambda operations and the
AWS Lambda console. If you haven't already, follow the instructions in [Getting
Started with AWS Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") to create your first Lambda function.
