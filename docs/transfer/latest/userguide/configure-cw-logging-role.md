# Configure CloudWatch logging role

To set access, you create a resource-based IAM policy and an IAM role that
provides that access information.

To enable Amazon CloudWatch logging, you start by creating an IAM policy that enables CloudWatch
logging. You then create an IAM role and attach the policy to it. You can do this when
you are [creating a server](getting-started.md#getting-started-server "getting-started.md#getting-started-server") or by [editing an existing server](edit-server-config.md "edit-server-config.md"). For more information
about CloudWatch, see [What is
Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") and [What is Amazon CloudWatch
logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") in the _Amazon CloudWatch User Guide_.

Use the following example IAM policies to allow CloudWatch logging.

Use a logging role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:DescribeLogStreams",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:log-group:/aws/transfer/*"
        }
    ]
}
```

Use structured logging

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogDelivery",
                "logs:GetLogDelivery",
                "logs:UpdateLogDelivery",
                "logs:DeleteLogDelivery",
                "logs:ListLogDeliveries",
                "logs:PutResourcePolicy",
                "logs:DescribeResourcePolicies",
                "logs:DescribeLogGroups"
            ],
            "Resource": "*"
        }
    ]
}
```

In the preceding example policy, for the `Resource`,
replace the `region-id` and
`AWS account` with your values. For example,
`"Resource":
 "arn:aws::logs:us-east-1:111122223333:log-group:/aws/transfer/*"`

You then create a role and attach the CloudWatch Logs policy that you created.

###### To create an IAM role and attach a policy

1. In the navigation pane, choose **Roles**, and then choose
   **Create role**.

On the **Create role** page, make sure that **AWS
service** is chosen. 2. Choose **Transfer** from the service list, and then choose
**Next: Permissions**. This establishes a trust
relationship between AWS Transfer Family and the IAM role. Additionally, add
`aws:SourceAccount` and `aws:SourceArn` condition keys
to protect yourself against the _confused deputy_ problem.
See the following documentation for more details:

    * Procedure for establishing a trust relationship with AWS Transfer Family: [To establish a trust relationship](requirements-roles.md#establish-trust-transfer "requirements-roles.md#establish-trust-transfer")
    * Description for confused deputy problem: [the confused deputy
     problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md")

3. In the **Attach permissions policies** section, locate and
   choose the CloudWatch Logs policy that you just created, and choose **Next:
   Tags**.
4. (Optional) Enter a key and value for a tag, and choose **Next:
   Review**.
5. On the **Review** page, enter a name and description for your
   new role, and then choose **Create role**.
6. To view the logs, choose the **Server ID** to open the server
   configuration page, and choose **View logs**. You are
   redirected to the CloudWatch console where you can see your log streams.
   On the CloudWatch page for your server, you can see records of user authentication (success
   and failure), data uploads (`PUT` operations), and data downloads
   (`GET` operations).
