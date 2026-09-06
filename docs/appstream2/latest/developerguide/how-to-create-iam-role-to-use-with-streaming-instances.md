

# How to Create an IAM Role to Use With WorkSpaces Applications Streaming Instances
<a name="how-to-create-iam-role-to-use-with-streaming-instances"></a>

This topic describes how to create a new IAM role so that you can use it with image builders and fleet streaming instances.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then choose **Create role**.

1. For **Select type of trusted entity**, choose **AWS service**.

1. From the list of AWS services, choose **WorkSpaces Applications**.

1. Under **Select your use case**, **WorkSpaces Applications — Allows WorkSpaces Applications instances to call AWS services on your behalf** is already selected. Choose **Next: Permissions**.

1. If possible, select the policy to use for the permissions policy or choose **Create policy** to open a new browser tab and create a new policy from scratch. For more information, see step 4 in the procedure [Creating IAM Policies (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-start) in the *IAM User Guide*.

   After you create the policy, close that tab and return to your original tab. Select the check box next to the permissions policies that you want WorkSpaces Applications to have.

1. (Optional) Set a permissions boundary. This is an advanced feature that is available for service roles, but not service-linked roles. For more information, see [Permissions Boundaries for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.

1. Choose **Next: Tags**. You can optionally attach tags as key-value pairs. For more information, see [Tagging IAM Users and Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

1. Choose **Next: Review**.

1. For **Role name**, type a role name that is unique within your Amazon Web Services account. Because other AWS resources might reference the role, you can't edit the name of the role after it has been created.

1. For **Role description**, keep the default role description or type a new one.

1. Review the role, and then choose **Create role**.