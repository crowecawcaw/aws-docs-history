# Create a new IAM role from console

Alternatively, you could also use the Firehose console to create a new role on your behalf.

When Firehose creates an IAM role on your behalf, the role automatically includes all
permission and trust policies that grant the required permissions based on the
Firehose stream configuration.

For example, if you didn’t enable **Transform source records with
AWS Lambda** feature then console generates the following statement in the
permission policy.

```
{
  "Sid": "lambdaProcessing",
  "Effect": "Allow",
   "Action": [
     "lambda:InvokeFunction",
     "lambda:GetFunctionConfiguration"
   ],
   "Resource": "`arn:aws:`lambda:`us-east-1``123456789012`:function:%FIREHOSE_POLICY_TEMPLATE_PLACEHOLDER%"
}
```

###### Note

It's safe to ignore the policy statements that contain
`%FIREHOSE_POLICY_TEMPLATE_PLACEHOLDER%` as they don't grant permissions
on any resources.

The console create and edit Firehose stream workflows also create a trust policy and attach
it to the IAM role. The trust policy allows Firehose to assume the IAM role. Following is a
example of a trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "firehoseAssume",
 "Effect": "Allow",
 "Principal": {
 "Service": "firehose.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }]
}`

```

###### Important

- You should avoid using the same console-managed IAM role for multiple
  Firehose streams. Otherwise, the IAM role could become overly permissive or
  result in errors.
- To use different policy statements within a permission policy from a
  console-managed IAM role, you can create your own IAM role, and copy the
  policy statements to a permission policy attached to the new role. To attach
  the role to the Firehose stream, select the **Choose existing IAM
  role** option in the **Service
  access**.
- Console manages any IAM role that contains the string
  _service-role_ in its ARN. When you choose the
  existing IAM role option, make sure to select an IAM role without the
  _service-role_ string in its ARN so that console
  doesn’t make any changes to it.

1. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose **Create Firehose stream**.
3. Choose a source and destination. For more information, see [Tutorial: Create a Firehose stream from console](basic-create.md "basic-create.md").
4. Choose the destination settings. For more information, see [Configure destination settings](create-destination.md "create-destination.md").
5. Under [Advanced settings](create-configure-advanced.md "create-configure-advanced.md"),
   for **Service access**, choose **Create or update
   IAM role**.

###### Note

This is a default option. To use an existing role, select the
**Choose existing IAM role** option. Firehose console
won’t make any changes to your own role. 6. Choose **Create Firehose stream**.
