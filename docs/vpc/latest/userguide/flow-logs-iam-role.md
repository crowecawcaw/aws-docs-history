

# IAM role for publishing flow logs to CloudWatch Logs
<a name="flow-logs-iam-role"></a>

The IAM role that's associated with your flow log must have sufficient permissions to publish flow logs to the specified log group in CloudWatch Logs. The IAM role must belong to your AWS account.

The IAM policy that's attached to your IAM role must include at least the following permissions.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
      ],
      "Resource": "*"
    }
  ]
}
```

------

Ensure that your role has the following trust policy, which allows the flow logs service to assume the role.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "vpc-flow-logs.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

We recommend that you use the `aws:SourceAccount` and `aws:SourceArn` condition keys to protect yourself against [the confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html). For example, you could add the following condition block to the previous trust policy. The source account is the owner of the flow log and the source ARN is the flow log ARN. If you don't know the flow log ID, you can replace that portion of the ARN with a wildcard (\*) and then update the policy after you create the flow log.

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "{{account_id}}"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:ec2:{{region}}:{{account_id}}:vpc-flow-log/{{flow-log-id}}"
    }
}
```

## Create an IAM role for flow logs
<a name="create-flow-logs-role"></a>

You can update an existing role as described above. Alternatively, you can use the following procedure to create a new role for use with flow logs. You'll specify this role when you create the flow log.

**To create an IAM role for flow logs**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. On the **Create policy** page, do the following:

   1. Choose **JSON**.

   1. Replace the contents of this window with the permissions policy at the start of this section.

   1. Choose **Next**.

   1. Enter a name for your policy and an optional description and tags, and then choose **Create policy**.

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. For **Trusted entity type**, choose **Custom trust policy**. For **Custom trust policy**, replace `"Principal": {},` with the following, then and choose **Next**.

   ```
   "Principal": {
      "Service": "vpc-flow-logs.amazonaws.com"
   },
   ```

1. On the **Add permissions** page, select the checkbox for the policy that you created earlier in this procedure, and then choose **Next**.

1. Enter a name for your role and optionally provide a description.

1. Choose **Create role**.