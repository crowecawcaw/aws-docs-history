# Extended sessions for Amazon Q Developer

If your developers use Amazon Q Developer as part of an integrated development environment (IDE), you can set the session duration for Amazon Q Developer to 90 days. Depending on when you enabled IAM Identity Center, extended session duration for Amazon Q Developer might be enabled by default. This extended session doesn't affect the session duration of the AWS access portal or other AWS managed applications.

###### Note

Amazon Q Developer is accessible from consoles set to commercial AWS Regions that are enabled by default. If your IAM Identity Center instance is located in a Region where Amazon Q Developer isn't currently accessible, enabling 90 day extended session duration won't override the default setting. This means that your session duration remains unchanged, whether you enable 90 day extended session duration or not. For information, [Supported AWS Regions for Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/regions.html "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/regions.html").

###### To extend a session for Amazon Q Developer

1. Open the IAM Identity Center console.
2. Choose **Settings**.
3. On the **Settings** page, choose the **Authentication** tab.
4. Under **Authentication**, next to **Session duration**, choose **Configure**. A **Configure session duration** dialog box appears.
5. In the **Configure session duration** dialog box, select the **Enable extended sessions for Amazon Q Developer** check box. Clear the check box to disable extended session sessions for Amazon Q Developer.
6. Choose **Save** to return to the **Settings** page.
