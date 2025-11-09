# DynamoDB Streams and AWS Lambda triggers

Amazon DynamoDB is integrated with AWS Lambda so that you can create
_triggers_—pieces of code that automatically respond to events
in DynamoDB Streams. With triggers, you can build applications that react to data modifications in DynamoDB
tables.

###### Topics

- [Tutorial #1: Using filters to process all
  events with Amazon DynamoDB and AWS Lambda using the AWS CLI](Streams.Lambda.md "Streams.Lambda.md")
- [Tutorial #2: Using filters to process some
  events with DynamoDB and Lambda](Streams.Lambda.md "Streams.Lambda.md")
- [Best practices using DynamoDB Streams with
  Lambda](Streams.Lambda.md "Streams.Lambda.md")
  If you enable DynamoDB Streams on a table, you can associate the stream Amazon Resource Name (ARN)
  with an AWS Lambda function that you write. All mutation actions to that DynamoDB table can then
  be captured as an item on the stream. For example, you can set a trigger so that when an
  item in a table is modified a new record immediately appears in that table's stream.

###### Note

If you subscribe more than two Lambda functions to one DynamoDB stream, read throttling might occur.

The [AWS Lambda](../../../lambda/latest/dg/with-ddb.md "../../../lambda/latest/dg/with-ddb.md")
service polls the stream for new records four times per second. When new stream records are
available, your Lambda function is synchronously invoked. You can subscribe up to two Lambda
functions to the same DynamoDB stream. If you subscribe more than two Lambda functions to the same DynamoDB stream, read throttling might occur.

The Lambda function can send a notification, initiate a workflow, or perform many other
actions that you specify. You can write a Lambda function to simply copy each stream record
to persistent storage, such as Amazon S3 File Gateway (Amazon S3), and create a permanent audit trail of
write activity in your table. Or suppose that you have a mobile gaming app that writes to a
`GameScores` table. Whenever the `TopScore` attribute of the
`GameScores` table is updated, a corresponding stream record is written to
the table's stream. This event could then trigger a Lambda function that posts a
congratulatory message on a social media network. This function could also be written to
ignore any stream records that are not updates to `GameScores`, or that do not
modify the `TopScore` attribute.

If your function returns an error, Lambda retries the batch until it processes successfully
or the data expires. You can also configure Lambda to retry with a smaller batch, limit the
number of retries, discard records once they become too old, and other options.

As performance best practices, the Lambda function needs to be short lived. To avoid
introducing unnecessary processing delays, it also should not execute complex logic. For a
high velocity stream in particular, it is better to trigger an asynchronous post-processing
step function workflows than synchronous long running Lambdas.

You cannot use the same Lambda trigger across different AWS accounts.
Both the DynamoDB table and the Lambda functions must belong to the same AWS account.

For more information about AWS Lambda, see the [AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md").
