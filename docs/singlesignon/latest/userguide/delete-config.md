# Delete your IAM Identity Center instance

When an IAM Identity Center instance is deleted, all the data in that instance is deleted and cannot be
 recovered. The following table describes what data is deleted based on the directory type
 that is configured in IAM Identity Center.



| What data gets deleted | Connected directory - AWS Managed Microsoft AD, AD Connector, or external identity provider | IAM Identity Center identity store |
| --- | --- | --- |
| All permission sets you have configured for AWS accounts | Yes | Yes |
| All applications you have configured in IAM Identity Center | Yes | Yes |
| All user assignments you have configured for AWS accounts and applications | Yes | Yes |
| All users and groups in the directory or store | **N/A** | Yes | Use the following procedure to delete your IAM Identity Center instance. ###### To delete your IAM Identity Center instance 1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon"). 2. In the left navigation pane, choose **Settings**. 3. On the **Settings** page, choose the **Management** tab. 4. In the **Delete IAM Identity Center configuration** section, choose **Delete**. 5. In the **Delete IAM Identity Center configuration** dialog, select each checkbox to acknowledge you understand that your data will be deleted. Type your IAM Identity Center instance in the text box, and then choose **Confirm**.
