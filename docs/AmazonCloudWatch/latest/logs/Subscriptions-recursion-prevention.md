# Log recursion prevention

There is a risk of causing an infinite log recursion with subscription filters that
can lead to a large increase in ingestion billing in both CloudWatch Logs and your destination, if
not prevented. This can occur when a subscription filter is associated with a log group
that receives log events as a result of your subscription delivery workflow. The logs
ingested into the log group will be delivered to the destination, causing the log group
to ingest more logs which will then be forwarded again to the destination, creating a
recursion loop.

For example, consider a subscription filter with the destination as Firehose, which
delivers log events to Amazon S3. Additionally, there is also a Lambda function that processes
new events delivered to Amazon S3 and produces some logs itself. If the subscription filter
is applied to the Lambda function’s log group, then the log events produced by the
function will get forwarded to Firehose and Amazon S3 at the destination, which will then invoke
the function again, causing more logs to be produced and forwarded to Firehose and Amazon S3,
causing another invocation of the function and so on. This will occur in an infinite
loop, leading to an unexpected billing increase on log ingestion, Firehose, and
Amazon S3.

If the Lambda function is attached to a VPC with flow logs enabled for CloudWatch Logs, then the
VPC’s log group can cause a log recursion as well.

We recommend that you don't apply subscription filters to log groups that are a part
of your subscription delivery workflow. For account-level subscription filters, use the
`selectionCriteria` parameter in the `PutAccountPolicy` API to
exclude these log groups from the policy.

When excluding log groups, consider the following AWS services that produce logs and
may be a part of your subscription delivery workflows:

- Amazon EC2 with Fargate
- Lambda
- AWS Step Functions
- Amazon VPC flow logs that are enabled for CloudWatch Logs

###### Note

Log events produced by a Lambda destination’s log group will not be forwarded back
to the Lambda function for an account-level subscription filter policy. In this case,
excluding the destination Lambda function’s log group using
`selectionCriteria` is not required for account subscription
policies.
