# Enabling Automation

When you access the Automation section of the Compute Optimizer console for the first
time, you're asked to enable the feature using the account that you’re signed in with.
You can also opt in using the Compute Optimizer Automation API, AWS Command Line
Interface (AWSCLI), or SDKs.

By enabling this feature, you authorize Compute Optimizer to implement optimization
recommendations by managing AWS resources in your account. This includes creating Amazon
EBS snapshots, deleting EBS volumes, and modifying EBS volumes. In the future, AWS may
expand the types of optimization recommendations that AWS Compute Optimizer can implement and the AWS
resources it can manage.

To enable Automation, you need specific permissions to update the Automation
enrollment configuration and create the necessary service-linked role. For more
information on service-linked roles, see [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md "using-service-linked-roles.md").

###### To enable Automation

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. In the navigation pane, choose any page under the
   **Automation** section.
3. On the feature landing page, choose **Enable
   Automation**.
4. When prompted, review the note on service-linked role permissions and choose
   **Enable Automation**.
   To enable Automation using IAM policies, see Enabling Automation.

If you're enabling Automation for member accounts in your organization, the management account also needs permissions to associate and disassociate accounts. These permissions allow the management account to enable Automation for member accounts and configure whether the management account can implement optimizations on behalf of the member account. For more information, see [Enabling Automation for your organization](automation-org.md "automation-org.md").

## Policy to enable Automation for your

account

The following policy statement enables Automation for your account.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy",
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:UpdateEnrollmentConfiguration",
            "Resource": "*"
        }
    ]
}


```
