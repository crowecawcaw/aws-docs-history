

# Entering system configuration settings
<a name="mkt-system-config"></a>

After you onboard an AWS seller account, you enter several system settings. Follow these steps.

1. In Salesforce, on the [Guided setup tab](use-guided-setup.md), expand **Step 2: Complete system configuration settings** and choose **Review.** 

1. On the **Custom Settings** page, locate the **AWS Marketplace Integration Settings**, and choose **Manage.** 

1. Choose **Edit** to add **Default Organization Level** **values**, and then enter the required values from the following table. 


<table>
<thead>
  <tr><th> <b>Setting name</b> </th><th> <b>Default value</b> </th><th> <b>Description</b> </th></tr>
</thead>
<tbody>
  <tr><td> <b>AWS Presigned URL Role Name</b> </td><td>NULL </td><td>The IAM role in the seller account used to presign the Amazon S3 URL for the custom EULA used with the AWS Marketplace catalog API. </td></tr>
  <tr><td> <b>Add seller account to buyer list</b> </td><td>FALSE </td><td>Enables the addition of the seller account to the buyer list so you can view the private offer in your account, similar to how a buyer would view it. </td></tr>
  <tr><td> <b>Amazon Simple Queue Service Queue Name</b> </td><td>NULL </td><td>Amazon SQS queue used to subscribe to the Amazon Simple Notification Service topic for retrieving notifications on the private offer.  The connector requires all onboarded AWS accounts to use the same SQS queue name.   </td></tr>
  <tr><td> <b>Are you in any partner programs</b> </td><td>FALSE </td><td></td></tr>
  <tr><td> <b>Log_All_Outbound_Requests</b> </td><td>FALSE </td><td>Enables logging on outbound API calls through the connector. </td></tr>
  <tr><td> <b>Log Level</b> </td><td>ERROR </td><td>Indicates the level of logging for outbound request logs. </td></tr>
  <tr><td> <b>Notification Retention</b> </td><td></td><td></td></tr>
  <tr><td> <b>SNS Topic ARN Prefix</b> </td><td></td><td></td></tr>
  <tr><td> <b>Sync log retention</b> </td><td>NULL </td><td>Configure sync log retention period in days. Recommended 10-90 days. </td></tr>
</tbody>
</table>


1. Choose **Save**. 