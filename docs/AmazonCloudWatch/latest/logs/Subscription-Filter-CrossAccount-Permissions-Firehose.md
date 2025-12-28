# Step 3:

Add/validate IAM permissions for the cross-account destination

According to AWS cross-account policy evaluation logic, in order to access
any cross-account resource (such as an Kinesis or Firehose stream used as a
destination for a subscription filter) you must have an identity-based policy in
the sending account which provides explicit access to the cross-account
destination resource. For more information about policy evaluation logic, see
[Cross-account policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.md").

You can attach the identity-based policy to the IAM role or IAM user that
you are using to create the subscription filter. This policy must be present in
the sending account. If you are using the Administrator role to create the
subscription filter, you can skip this step and move on to [Step 4: Create a subscription
filter](CreateSubscriptionFilter.md "CreateSubscriptionFilter.md").

###### To add or validate the IAM permissions needed for cross-account

1. Enter the following command to check which IAM role or IAM user is
   being used to run AWS logs commands.

```
aws sts get-caller-identity
```

The command returns output similar to the following:

```
{
"UserId": "`User ID`",
"Account": "`sending account id`",
"Arn": "arn:aws:`sending account id`:role/user:`RoleName/UserName`"
}
```

Make note of the value represented by
`RoleName` or
`UserName`. 2. Sign into the AWS Management Console in the sending account and search for the
attached policies with the IAM role or IAM user returned in the
output of the command you entered in step 1. 3. Verify that the policies attached to this role or user provide
explicit permissions to call `logs:PutSubscriptionFilter` on
the cross-account destination resource.

The following policy provides permissions to create a subscription
filter on any destination resource only in a single AWS account,
account `999999999999`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSubscriptionFiltersOnAnyResourceInOneSpecificAccount",
 "Effect": "Allow",
 "Action": "logs:PutSubscriptionFilter",
 "Resource": [
 "arn:aws:logs:*:*:log-group:*",
 "arn:aws:logs:*:123456789012:destination:*"
 ]
 }
 ]
}`

```

The following policy provides permissions to create a subscription
filter only on a specific destination resource named
`sampleDestination` in single AWS account, account
`123456789012`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSubscriptionFiltersOnSpecificResource",
 "Effect": "Allow",
 "Action": "logs:PutSubscriptionFilter",
 "Resource": [
 "arn:aws:logs:*:*:log-group:*",
 "arn:aws:logs:*:`123456789012`:destination:`amzn-s3-demo-bucket`"
 ]
 }
 ]
}`

```
