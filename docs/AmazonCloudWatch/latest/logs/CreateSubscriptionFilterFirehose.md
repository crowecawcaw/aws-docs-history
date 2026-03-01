# Step 4: Create a subscription filter

Switch to the sending account, which is 111111111111 in this example. You will
now create the subscription filter in the sending account. In this example, the
filter is associated with a log group containing AWS CloudTrail events so that every
logged activity made by "Root" AWS credentials is delivered to the destination
you previously created. For more information about how to send AWS CloudTrail events
to CloudWatch Logs, see [Sending
CloudTrail Events to CloudWatch Logs](../../../awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.md") in the
_AWS CloudTrail User Guide_.

When you enter the following command, be sure you are signed in as the IAM
user or using the IAM role that you added the policy for, in [Step 3: Add/validate IAM permissions for the cross-account destination](Subscription-Filter-CrossAccount-Permissions-Firehose.md "Subscription-Filter-CrossAccount-Permissions-Firehose.md").

```
`aws logs put-subscription-filter \
 --log-group-name "aws-cloudtrail-logs-111111111111-300a971e" \
 --filter-name "firehose_test" \
 --filter-pattern "{$.userIdentity.type = AssumedRole}" \
 --destination-arn "arn:aws:logs:us-east-1:222222222222:destination:testFirehoseDestination"`
```

The log group and the destination must be in the same AWS Region. However,
the destination can point to an AWS resource such as a Firehose stream that is
located in a different Region.
