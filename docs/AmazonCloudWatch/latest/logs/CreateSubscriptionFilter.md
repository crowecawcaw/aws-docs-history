# Step 4: Create a subscription

filter

After you create a destination, the log data recipient account can share
the destination ARN
(arn:aws:logs:us-east-1:999999999999:destination:testDestination) with other
AWS accounts so that they can send log events to the same destination.
These other sending accounts users then create a subscription filter on
their respective log groups against this destination. The subscription
filter immediately starts the flow of real-time log data from the chosen log
group to the specified destination.

###### Note

If you are granting permissions for the subscription filter to an
entire organization, you will need to use the ARN of the IAM role that
you created in [Step 2: (Only if using an
organization) Create an IAM role](CreateSubscriptionFilter-IAMrole.md "CreateSubscriptionFilter-IAMrole.md").

In the following example, a subscription filter is created in a sending
account. the filter is associated with a log group containing AWS CloudTrail
events so that every logged activity made by "Root" AWS credentials is
delivered to the destination you previously created. That destination
encapsulates a stream called "RecipientStream".

The rest of the steps in the following sections assume that you have
followed the directions in [Sending CloudTrail Events to CloudWatch Logs](../../../awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.md") in the
_AWS CloudTrail User Guide_ and created a log group that
contains your CloudTrail events. These steps assume that the name of this log
group is `CloudTrail/logs`.

When you enter the following command, be sure you are signed in as the
IAM user or using the IAM role that you added the policy for, in [Step 3:
Add/validate IAM permissions for the cross-account destination](Subscription-Filter-CrossAccount-Permissions.md "Subscription-Filter-CrossAccount-Permissions.md").

```
`aws logs put-subscription-filter \
 --log-group-name "CloudTrail/logs" \
 --filter-name "RecipientStream" \
 --filter-pattern "{$.userIdentity.type = Root}" \
 --destination-arn "arn:aws:logs:`region`:999999999999:destination:testDestination"`
```

The log group and the destination must be in the same AWS Region.
However, the destination can point to an AWS resource such as a Amazon Kinesis Data Streams
stream that is located in a different Region.
