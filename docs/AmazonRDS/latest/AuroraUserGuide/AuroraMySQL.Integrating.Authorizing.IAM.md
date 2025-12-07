# Creating an IAM policy to access AWS Lambda resources

You can create an IAM policy that provides the minimum
required permissions for Aurora to invoke an AWS Lambda function on your behalf.

The following policy adds the permissions required by Aurora to invoke an
AWS Lambda function on your behalf.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAuroraToExampleFunction",
 "Effect": "Allow",
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:`us-east-1`:`123456789012`:function:`example_function`"
 }
 ]
}`

```

You can use the following steps to create an IAM policy that provides the minimum
required permissions for Aurora to invoke an AWS Lambda function on your behalf. To
allow Aurora to invoke all of your AWS Lambda functions, you can skip these steps and
use the predefined `AWSLambdaRole` policy instead of creating your
own.

###### To create an IAM policy to grant invoke to your AWS Lambda

functions

1. Open the [IAM
   console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. On the **Visual editor** tab, choose **Choose a service**,
   and then choose **Lambda**.
5. For **Actions**, choose **Expand all**, and then choose the
   AWS Lambda permissions needed for the IAM policy.

Ensure that `InvokeFunction` is selected. It is the minimum required permission to enable Amazon Aurora to
invoke an AWS Lambda function. 6. Choose **Resources** and choose **Add ARN** for **function**. 7. In the **Add ARN(s)** dialog box, provide the details
about your resource.

Specify the Lambda function to allow access to. For instance, if you want to allow Aurora
to access a Lambda function named `example_function`, then set the
ARN value to `arn:aws:lambda:::function:example_function`.

For more information on how to define an access policy for AWS Lambda, see
[Authentication and access control for AWS Lambda](../../../lambda/latest/dg/lambda-auth-and-access-control.md "../../../lambda/latest/dg/lambda-auth-and-access-control.md"). 8. Optionally, choose **Add additional permissions** to add another AWS Lambda function
to the policy, and repeat the previous steps for the function.

###### Note

You can repeat this to add corresponding
function permission statements to your policy for each AWS Lambda function
that you want Aurora to access. 9. Choose **Review policy**. 10. Set **Name** to a name for your IAM policy, for
example `AllowAuroraToExampleFunction`. You use this name when you
create an IAM role to associate with your Aurora DB cluster. You can also add
an optional **Description** value. 11. Choose **Create policy**. 12. Complete the steps in [Creating an
IAM role to allow Amazon Aurora to access AWS services](AuroraMySQL.Integrating.Authorizing.IAM.md "AuroraMySQL.Integrating.Authorizing.IAM.md").
