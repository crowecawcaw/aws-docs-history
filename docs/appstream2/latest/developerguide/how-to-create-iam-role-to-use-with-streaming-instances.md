# How to Create an IAM Role to Use With AppStream 2.0 Streaming Instances

This topic describes how to create a new IAM role so that you can use it with image builders and fleet streaming instances.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, and then choose **Create role**.
3. For **Select type of trusted entity**, choose **AWS service**.
4. From the list of AWS services, choose **AppStream 2.0**.
5. Under **Select your use case**, **AppStream 2.0 — Allows AppStream 2.0 instances to call AWS services on your behalf** is already selected. Choose **Next: Permissions**.
6. If possible, select the policy to use for the permissions policy or choose **Create policy** to open a new browser tab and create a new policy from scratch. For more information, see step 4 in the procedure [Creating IAM Policies (Console)](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start") in the _IAM User Guide_.

After you create the policy, close that tab and return to your original tab. Select the check box next to the permissions policies that you want AppStream 2.0 to have. 7. (Optional) Set a permissions boundary. This is an advanced feature that is available for service roles, but not service-linked roles. For more information, see [Permissions Boundaries for IAM Entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_. 8. Choose **Next: Tags**. You can optionally attach tags as key-value pairs. For more information, see [Tagging IAM Users and Roles](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 9. Choose **Next: Review**. 10. For **Role name**, type a role name that is unique within your Amazon Web Services account. Because other AWS resources might reference the role, you can't edit the name of the role after it has been created. 11. For **Role description**, keep the default role description or type a new one. 12. Review the role, and then choose **Create role**.
