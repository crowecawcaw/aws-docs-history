

# Grant Amazon SNS permissions to a CodePipeline service role
<a name="approvals-service-role-permissions"></a>

If you plan to use Amazon SNS to publish notifications to topics when approval actions require review, the service role you use in your CodePipeline operations must be granted permission to access the Amazon SNS resources. You can use the IAM console to add this permission to your service role.

In the policy below, specify the policy for publishing with SNS. For the following policy, you can name it `SNSPublish`. Use the following policy by attaching it to your service role.

**Important**  
Make sure you are signed in to the AWS Management Console with the same account information you used in [Getting started with CodePipeline](getting-started-codepipeline.md).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "*"
        }
    ]
}
```

------

**To use the JSON policy editor to create a policy**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane on the left, choose **Policies**. 

   If this is your first time choosing **Policies**, the **Welcome to Managed Policies** page appears. Choose **Get Started**.

1. At the top of the page, choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Enter or paste a JSON policy document. For details about the IAM policy language, see [IAM JSON policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html).

1. Resolve any security warnings, errors, or general warnings generated during [policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html), and then choose **Next**. 
**Note**  
You can switch between the **Visual** and **JSON** editor options anytime. However, if you make changes or choose **Next** in the **Visual** editor, IAM might restructure your policy to optimize it for the visual editor. For more information, see [Policy restructuring](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html#troubleshoot_viseditor-restructure) in the *IAM User Guide*.

1. (Optional) When you create or edit a policy in the AWS Management Console, you can generate a JSON or YAML policy template that you can use in CloudFormation templates.

   To do this, in the **Policy editor** choose **Actions**, and then choose **Generate CloudFormation template**. To learn more about CloudFormation, see [AWS Identity and Access Management resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IAM.html) in the *AWS CloudFormation User Guide*.

1. When you are finished adding permissions to the policy, choose **Next**.

1. On the **Review and create** page, enter a **Policy name** and a **Description** (optional) for the policy that you are creating. Review **Permissions defined in this policy** to see the permissions that are granted by your policy.

1. (Optional) Add metadata to the policy by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

1. Choose **Create policy** to save your new policy.