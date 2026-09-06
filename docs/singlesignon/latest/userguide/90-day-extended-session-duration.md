

# Extended sessions for Kiro
<a name="90-day-extended-session-duration"></a>

If your developers use Kiro as part of an integrated development environment (IDE), you can set the session duration for Kiro to 90 days. Depending on when you enabled IAM Identity Center, extended session duration for Kiro might be enabled by default. This extended session doesn't affect the session duration of the AWS access portal or other AWS managed applications.

For considerations such as how IAM Identity Center identity sources might affect the extended session duration, see [Session duration considerations for using identity sources, the AWS CLI, and AWS SDKs](user-session-duration-prereqs-considerations.md).

**Note**  
Kiro is accessible from consoles set to commercial AWS Regions that are enabled by default. If your IAM Identity Center instance is located in a Region where Kiro isn't currently accessible, enabling 90 day extended session duration won't override the default setting. This means that your session duration remains unchanged, whether you enable 90 day extended session duration or not. For information, [Supported AWS Regions for Kiro](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/regions.html).

**To extend a session for Kiro**

1. Open the IAM Identity Center console.

1. Choose **Settings**.

1. On the **Settings** page, choose the **Authentication** tab.

1. Under **Authentication**, next to **Session duration**, choose **Configure**. A **Configure session duration** dialog box appears.

1. In the **Configure session duration** dialog box, select the **Enable extended sessions for Kiro** check box. Clear the check box to disable extended session sessions for Kiro.

1. Choose **Save** to return to the **Settings** page.