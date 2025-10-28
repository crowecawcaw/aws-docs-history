# Step 3: Create an

account-level subscription filter policy

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
you created in [Step 2: (Only if
using an organization) Create an IAM role](CreateSubscriptionFilter-IAMrole-Account.md "CreateSubscriptionFilter-IAMrole-Account.md").

In the following example, an account-level subscription filter policy is
created in a sending account. the filter is associated with the sender
account `111111111111` so that every log event matching the
filter and selection criteria is delivered to the destination you previously
created. That destination encapsulates a stream called
"RecipientStream".

The `selection-criteria` field is optional, but is important
for excluding log groups that can cause an infinite log recursion from a
subscription filter. For more information about this issue and determining
which log groups to exclude, see [Log recursion prevention](Subscriptions-recursion-prevention.md "Subscriptions-recursion-prevention.md"). Currently, NOT IN
is the only supported operator for `selection-criteria`.

```
`aws logs put-account-policy \
 --policy-name "CrossAccountStreamsExamplePolicy" \
 --policy-type "SUBSCRIPTION_FILTER_POLICY" \
 --policy-document '{"DestinationArn":"arn:aws:logs:region:999999999999:destination:testDestination", "FilterPattern": "", "Distribution": "Random"}' \
 --selection-criteria 'LogGroupName NOT IN ["LogGroupToExclude1", "LogGroupToExclude2"]' \
 --scope "ALL"`
```

The sender account's log groups and the destination must be in the same
AWS Region. However, the destination can point to an AWS resource such
as a Kinesis Data Streams stream that is located in a different Region.
