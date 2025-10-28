# Edit IAM role from console

When you edit a Firehose stream, Firehose updates the corresponding permission policy
accordingly to reflect the configuration and permission changes.

For example, when you edit the Firehose stream and enable **Transform source
records with AWS Lambda** feature using the latest version of Lambda function
as `exampleLambdaFunction`, you get the following policy statement in the
permission policy.

```
{
  "Sid": "lambdaProcessing",
  "Effect": "Allow",
  "Action": [
    "lambda:InvokeFunction",
    "lambda:GetFunctionConfiguration"
  ],
  "Resource": "`arn:aws:`lambda:`us-east-1`:`123456789012`:function:exampleLambdaFunction:$LATEST"
}
```

###### Important

A console-managed IAM role is designed to be autonomous. We don't recommend that you
modify the permission policy or trust policy outside of the console.

1. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose **Firehose streams** and choose the name of a
   Firehose stream you want to update.
3. On the **Configuration** tab, in the **Server access**
   section, choose **Edit**.
4. Update the IAM role option.

###### Note

By default, the console always updates an IAM role with the pattern
_service-role_ in its ARN. When you choose the
existing IAM role option, make sure to select an IAM role without the
_service-role_ string in its ARN so that console
doesn’t make any changes to it. 5. Choose **Save changes**.
