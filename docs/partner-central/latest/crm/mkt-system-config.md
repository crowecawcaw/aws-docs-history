# Entering system configuration settings

After you onboard an AWS seller account, you enter several system settings. Follow these
steps.

1. In Salesforce, on the [Guided setup tab](use-guided-setup.md "use-guided-setup.md"), expand **Step 2: Complete system configuration settings** and choose
   **Review.**
2. On the **Custom Settings** page, locate the **AWS Marketplace
   Integration Settings**, and choose **Manage.**
3. Choose **Edit** to add **Default Organization
   Level**
   **values**, and then enter the required values from the following table.

| **Setting name**                           | **Default value** | **Description**                                                                                                                                                                                                             |
| ------------------------------------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| **AWS Presigned URL Role Name**            | NULL              | The IAM role in the seller account used to presign the Amazon S3 URL for the custom EULA used with the AWS Marketplace catalog API.                                                                                         |
| **Add seller account to buyer list**       | FALSE             | Enables the addition of the seller account to the buyer list so you can view the private offer in your account, similar to how a buyer would view it.                                                                       |
| **Amazon Simple Queue Service Queue Name** | NULL              | Amazon SQS queue used to subscribe to the Amazon Simple Notification Service topic for retrieving notifications on the private offer. NoteThe connector requires all onboarded AWS accounts to use the same SQS queue name. |
| **Are you in any partner programs**        | FALSE             |                                                                                                                                                                                                                             |
| **Log_All_Outbound_Requests**              | FALSE             | Enables logging on outbound API calls through the connector.                                                                                                                                                                |
| **Log Level**                              | ERROR             | Indicates the level of logging for outbound request logs.                                                                                                                                                                   |
| **Notification Retention**                 |                   |                                                                                                                                                                                                                             |
| **SNS Topic ARN Prefix**                   |                   |                                                                                                                                                                                                                             |
| **Sync log retention**                     | NULL              | Configure sync log retention period in days. Recommended 10-90 days.                                                                                                                                                        | 4. Choose **Save**. |
