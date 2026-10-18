

# AWS Systems Manager Run Command execution block sample policy
<a name="security_iam_region_switch_ssm"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for AWS Systems Manager Run Command. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:DescribeDocument"
      ],
      "Resource": "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:document/{{document-name}}"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:SendCommand"
      ],
      "Resource": [
        "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:document/{{document-name}}",
        "arn:aws:ec2:{{us-east-1}}:*:instance/*",
        "arn:aws:ssm:{{us-east-1}}:*:managed-instance/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:DescribeInstanceInformation",
        "ssm:ListCommandInvocations",
        "ssm:CancelCommand"
      ],
      "Resource": "*"
    }
  ]
}
```

 `ssm:SendCommand` is scoped to the AWS Systems Manager documents and to the managed nodes in the plan's Regions. The node ARNs use a wildcard account and ID because Region switch resolves the command's target managed nodes dynamically at runtime from the targets that you configure. When a step targets nodes by instance ID, you can replace the `instance/*` and `managed-instance/*` wildcards with the specific node ARNs. The `ssm:DescribeInstanceInformation`, `ssm:ListCommandInvocations`, and `ssm:CancelCommand` actions require the wildcard resource because they don't support resource-level permissions for this use. 