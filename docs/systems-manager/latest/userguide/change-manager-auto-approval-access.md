

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Controlling access to auto-approval runbook workflows
<a name="change-manager-auto-approval-access"></a>

**Change Manager availability change**  
AWS Systems Manager Change Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Change Manager, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html). 

In each change template created for your organization or account, you can specify whether change requests created from that template can run as auto-approved change requests, meaning that they run automatically without a review step (with the exception of change freeze events).

However, you might want to prevent certain users, groups, or AWS Identity and Access Management (IAM) roles from running auto-approved change requests even if a change template allows it. You can do this through the use of the `ssm:AutoApprove` condition key for the `StartChangeRequestExecution` operation in an IAM policy assigned to the user, group, or IAM role. 

You can add the following policy as an inline policy, where the condition is specified as `false`, to prevent users from running auto-approvable change requests.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
            {
            "Effect": "Allow",
            "Action": "ssm:StartChangeRequestExecution",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "ssm:AutoApprove": "false"
                }
            }
        }
    ]
}
```

------

For information about specifying inline policies, see [Inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#inline-policies) and [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

For more information about condition keys for Systems Manager policies, see [Condition keys for Systems Manager](security_iam_service-with-iam.md#policy-conditions).