

# Step 4: Create a subscription filter
<a name="CreateSubscriptionFilterFirehose"></a>

Switch to the sending account, which is 111111111111 in this example. You will now create the subscription filter in the sending account. In this example, the filter is associated with a log group containing AWS CloudTrail events so that every logged activity made by "Root" AWS credentials is delivered to the destination you previously created. For more information about how to send AWS CloudTrail events to CloudWatch Logs, see [Sending CloudTrail Events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html) in the *AWS CloudTrail User Guide*.

When you enter the following command, be sure you are signed in as the IAM user or using the IAM role that you added the policy for, in [Step 3: Add/validate IAM permissions for the cross-account destination](Subscription-Filter-CrossAccount-Permissions-Firehose.md).

**Note**  
If you are granting permissions for the subscription filter to an entire organization, use the ARN of the IAM role that you created in [(Only if using an organization) Create an IAM role](CreateSubscriptionFilterFirehose-IAMrole.md). Specify this ARN with the `--role-arn` parameter, as shown in the following example.  
Otherwise, the `PutSubscriptionFilter` call fails with an error stating that a role ARN is required when creating a subscription filter against a destination that has an organization access policy.

```
aws logs put-subscription-filter \
    --log-group-name "aws-cloudtrail-logs-111111111111-300a971e" \                   
    --filter-name "firehose_test" \
    --filter-pattern "{$.userIdentity.type = AssumedRole}" \
    --destination-arn "arn:aws:logs:us-east-1:222222222222:destination:testFirehoseDestination" \
    --role-arn "arn:aws:iam::111111111111:role/CWLtoSubscriptionFilterRole"
```

The log group and the destination must be in the same AWS Region. However, the destination can point to an AWS resource such as a Firehose stream that is located in a different Region.