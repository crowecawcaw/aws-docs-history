# Grant Amazon SNS permissions to a CodePipeline

service role

If you plan to use Amazon SNS to publish notifications to topics when approval actions
require review, the service role you use in your CodePipeline operations must be granted
permission to access the Amazon SNS resources. You can use the IAM console to add this
permission to your service role.

In the policy below, specify the policy for publishing with SNS. For the following
policy, you can name it `SNSPublish`. Use the following policy by attaching
it to your service role.

###### Important

Make sure you are signed in to the AWS Management Console with the same account information you
used in [Getting started with CodePipeline](getting-started-codepipeline.md "getting-started-codepipeline.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sns:Publish",
 "Resource": "*"
 }
 ]
}`

```

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter or paste a JSON policy document. For details about the IAM policy language, see
[IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md"). 6. Resolve any security warnings, errors, or general warnings generated during [policy validation](../../../IAM/latest/UserGuide/access_policies_policy-validator.md "../../../IAM/latest/UserGuide/access_policies_policy-validator.md"), and then choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. (Optional) When you create or edit a policy in the AWS Management Console, you can generate a JSON
or YAML policy template that you can use in CloudFormation templates.

To do this, in the **Policy editor** choose
**Actions**, and then choose **Generate CloudFormation
template**. To learn more about CloudFormation, see [AWS Identity and Access Management resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the
_AWS CloudFormation User Guide_. 8. When you are finished adding permissions to the policy, choose
**Next**. 9. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 10. (Optional) Add metadata to the policy by attaching tags as key-value pairs. For more
information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 11. Choose **Create policy** to save your new policy.
