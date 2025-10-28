# Step 3: Create an

account-level subscription filter policy

Switch to the sending account, which is 111111111111 in this example. You will
now create the account-level subscription filter policy in the sending account.
In this example, the filter causes every log event containing the string
`ERROR` in all but two log groups to be delivered to the
destination you previously created.

```
aws logs put-account-policy \
    --policy-name "CrossAccountFirehoseExamplePolicy" \
    --policy-type "SUBSCRIPTION_FILTER_POLICY" \
    --policy-document '{"DestinationArn":"arn:aws:logs:us-east-1:222222222222:destination:testFirehoseDestination", "FilterPattern": "{$.userIdentity.type = AssumedRole}", "Distribution": "Random"}' \
    --selection-criteria 'LogGroupName NOT IN ["LogGroupToExclude1", "LogGroupToExclude2"]' \
    --scope "ALL"
```

The sending account's log groups and the destination must be in the same AWS
Region. However, the destination can point to an AWS resource such as a Firehose
stream that is located in a different Region.
