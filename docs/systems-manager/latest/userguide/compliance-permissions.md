

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Configuring permissions for Compliance
<a name="compliance-permissions"></a>

As a best practice, update the AWS Identity and Access Management (IAM) role used by your managed nodes with the following permissions. This restricts the node's ability to use the [PutComplianceItems](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutComplianceItems.html) API action, which registers a compliance type and other details on a resource such as a managed node.

If your node is an Amazon EC2 instance, you must update the IAM instance profile used by the instance with the following permissions. For more information about instance profiles for EC2 instance managed by Systems Manager, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md). For other types of managed nodes, update the IAM role used by the node with the following permissions. For more information, see [Update permissions for a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-permissions.html) in the *IAM User Guide*.

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
                "ssm:PutComplianceItems"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "ec2:SourceInstanceARN": "${ec2:SourceInstanceARN}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:PutComplianceItems"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "ssm:SourceInstanceARN": "${ssm:SourceInstanceARN}"
                }
            }
        }
    ]
}
```

------