# Grant CloudWatch permissions to a

CodeDeploy service role

Before you can use CloudWatch alarm monitoring with your deployments, the service role you use
in your CodeDeploy operations must be granted permission to access the CloudWatch resources.

###### To grant CloudWatch permissions to a service role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the IAM console, in the navigation pane, choose
   **Roles**.
3. Choose the name of the service role you use in your AWS CodeDeploy operations.
4. On the **Permissions** tab, in the **Inline
   Policies** area, choose **Create Role Policy**.

–or–

If the **Create Role Policy** button is not available, expand the
**Inline Policies** area, and then choose **click
here**. 5. On the **Set Permissions** page, choose **Custom
Policy**, and then choose **Select**. 6. On the **Review Policy** page, in the **Policy
Name** field, type a name to identify this policy, such as
`CWAlarms`. 7. Paste the following into the **Policy Document** field:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudwatch:DescribeAlarms",
 "Resource": "*"
 }
 ]
}`

```

8. Choose **Apply Policy**.
