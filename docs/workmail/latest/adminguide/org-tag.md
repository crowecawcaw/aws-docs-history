# Tagging an organization

Tagging an Amazon WorkMail organization resource allows you to:

- Differentiate between organizations in the AWS Billing and Cost Management console.
- Control access to Amazon WorkMail organization resources by adding them to the
  `Resource` element of AWS Identity and Access Management (IAM) permission policy
  statements.
  For more information about Amazon WorkMail resource-level permissions, see [Resources](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources"). For
  more information about controlling access based on tags, see [Authorization based on
  Amazon WorkMail tags](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").

Amazon WorkMail administrators can tag organizations using the Amazon WorkMail console.

###### To add tags to an Amazon WorkMail organization

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the console
window, open the **Select a Region** list and choose a Region.
For more information, see [Regions and
endpoints](../../../general/latest/gr/index.md "../../../general/latest/gr/index.md") in the _Amazon Web Services General Reference_. 2. In the navigation pane, choose **Organizations**, and then
choose the name of your organization. 3. Choose **Tags**. 4. For **Organization tags**, choose **Add new
tag**. 5. For **Key**, enter a name that identifies the tag. 6. (Optional) For **Value**, enter a value for the tag. 7. (Optional) Repeat steps 4-6 to add more tags to your organization. You can add
up to 50 tags. 8. Choose **Save** to save your changes.
You can view your organization tags in the Amazon WorkMail console.

Developers can also tag organizations using the AWS SDK or AWS Command Line Interface (AWS CLI). For
more information, see the `TagResource`, `ListTagsForResource`,
and `UntagResource` commands in the [Amazon WorkMail API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md") or the
[AWS CLI
Command Reference](../../../cli/latest/reference/workmail/index.md "../../../cli/latest/reference/workmail/index.md").

You can remove tags from an organization at any time, using the Amazon WorkMail console.

###### To remove tags from an Amazon WorkMail organization

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the console
window, open the **Select a Region** list and choose a Region.
For more information, see [Regions and
endpoints](../../../general/latest/gr/index.md "../../../general/latest/gr/index.md") in the _Amazon Web Services General Reference_. 2. In the navigation pane, choose **Organizations**, and then
choose the name of your organization. 3. Choose **Tags**. 4. For **Organization tags**, choose **Remove**
next to the tag to remove. 5. Choose **Submit** to save your changes.
