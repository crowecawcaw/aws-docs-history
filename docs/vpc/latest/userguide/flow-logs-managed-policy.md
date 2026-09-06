

# AWS managed policies for VPC Flow Logs
<a name="flow-logs-managed-policy"></a>

If you are using VPC Flow Logs and you create a subscription with tag fields and the associated TagFieldSpecifications parameter, the **AWSVPCFlowLogsServiceRolePolicy** managed policy is automatically created in your IAM account and attached to the **AWSServiceRoleForVPCFlowLogs** [service-linked role](flow-logs-slr.md).

This managed policy enables VPC Flow Logs to do the following:
+ Create and manage EventBridge Managed Rules to send tag update events to the VPC Flow Logs service. 
+ Call APIs on behalf of customers to validate tag value freshness for log enrichment.

The following example shows the details of the managed policy that's created.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowPutRuleOnSpecificSourcesAndDetailTypes",
            "Effect": "Allow",
            "Action": "events:PutRule",
            "Resource": [
                "arn:aws:events:*:*:rule/VPCFlowLogsEC2TagsManagedRule",
                "arn:aws:events:*:*:rule/VPCFlowLogsASGTagsManagedRule"
            ],
            "Condition": {
                "ForAllValues:StringEquals": {
                    "events:source": [
                        "aws.tag",
                        "aws.autoscaling"
                    ],
                    "events:detail-type": [
                        "AWS API Call via CloudTrail",
                        "Tag Change on Resource"
                    ]
                },
                "Null": {
                    "events:source": "false",
                    "events:detail-type": "false"
                },
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "AllowOtherOperationsOnRulesManagedByVPCFlowLogs",
            "Effect": "Allow",
            "Action": [
                "events:DeleteRule",
                "events:DescribeRule",
                "events:PutTargets",
                "events:RemoveTargets"
            ],
            "Resource": [
                "arn:aws:events:*:*:rule/VPCFlowLogsEC2TagsManagedRule",
                "arn:aws:events:*:*:rule/VPCFlowLogsASGTagsManagedRule"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "AllowDescribeTagsOnAllEC2Resources",
            "Effect": "Allow",
            "Action": [
                "tag:GetResources",
                "autoscaling:DescribeTags"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The first statement in the preceding example enables VPC Flow Logs to create EventBridge Managed Rules in your AWS account for sources `aws.tag` and `aws.autoscaling` for detail-types related to tag change events.

The second statement in the preceding example enables VPC Flow Logs to control the lifecycle of the created Managed Rules in your AWS account for resources named `VPCFlowLogsEC2TagsManagedRule` and/or `VPCFlowLogsASGTagsManagedRule`.

The third statement in the preceding example enables VPC Flow Logs to call tag APIs on behalf of customers to validate tag value freshness for log enrichment.

## AWS managed policy: AWSVPCFlowLogsServiceRolePolicy
<a name="flow-logs-managed-policy-AWSVPCFlowLogsServiceRolePolicy"></a>

You can attach the `AWSVPCFlowLogsServiceRolePolicy` policy to your IAM identities. This policy grants permissions that enables VPC Flow Logs to create and manage EventBridge Managed Rules and call DescribeTag APIs on your behalf to automatically track updates to EC2 Tag values associated with resources under Flow Logs subscriptions that include tag fields.

To view the permissions for this policy, see [AWSVPCFlowLogsServiceRolePolicy ](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVPCFlowLogsServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Updates to the AWS managed policy
<a name="flow-logs-managed-policy-updates"></a>

View details about updates to AWS managed policies for VPC Flow Logs since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWS managed policy: AWSVPCFlowLogsServiceRolePolicy](#flow-logs-managed-policy-AWSVPCFlowLogsServiceRolePolicy) – New policy | New AWSVPCFlowLogsServiceRolePolicy policy enables VPC Flow Logs to create and manage EventBridge Managed Rules and call DescribeTag APIs on your behalf to automatically track updates to EC2 Tag values associated with resources under Flow Logs subscriptions that include tag fields. | March 31, 2026 | 
| VPC Flow Logs started tracking changes | VPC Flow Logs started tracking changes for its AWS managed policies. | March 31, 2026 | 