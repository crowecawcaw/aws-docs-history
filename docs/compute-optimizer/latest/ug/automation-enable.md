

# Enabling Automation

When you access the Automation section of the Compute Optimizer console for the first time, you're asked to enable the feature using the account that you’re signed in with. You can also opt in using the Compute Optimizer Automation API, AWS Command Line Interface (AWSCLI), or SDKs.

By enabling this feature, you authorize Compute Optimizer to implement optimization recommendations by managing AWS resources in your account. This includes creating Amazon EBS snapshots, deleting EBS volumes, and modifying EBS volumes. In the future, AWS may expand the types of optimization recommendations that AWS Compute Optimizer can implement and the AWS resources it can manage. 

To enable Automation, you need specific permissions to update the Automation enrollment configuration and create the necessary service-linked role. For more information on service-linked roles, see [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md).

**To enable Automation**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose any page under the **Automation** section.

1. On the feature landing page, choose **Enable Automation**.

1. When prompted, review the note on service-linked role permissions and choose **Enable Automation**.

After you enable Automation, the management account or a delegated administrator can create enrollment configurations on the **Account management** page to enable Automation for member accounts. For more information, see [Managing organization enrollment configurations](automation-org-ou-configure.md).

To enable Automation using IAM policies, see [Enabling Automation](automation-enable.md).

If you use AWS Organizations, you can enable Automation for member accounts from the management account or a delegated administrator account. Create an organization enrollment configuration on the root, an organizational unit (OU), or an account. The enrollment configuration enables Automation for every eligible account that it applies to. For more information, see [Enabling Automation for your organization](automation-org.md).

After you enable Automation, you can create automation rules with CloudFormation. For more information, see [Creating automation rules with CloudFormation](creating-automation-rules-with-cloudformation.md).

## Policy to enable Automation for your account
<a name="policy-automation-enable-coa"></a>

The following policy statement enables Automation for your account.

```JSON
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