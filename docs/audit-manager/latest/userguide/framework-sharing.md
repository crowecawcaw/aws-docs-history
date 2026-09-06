

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Sending request to share a custom framework in AWS Audit Manager
<a name="framework-sharing"></a>



This tutorial describes how to share your custom frameworks across AWS accounts and AWS Regions. 

When you share a custom framework, Audit Manager creates a snapshot of your framework and sends a share request to the recipient. The recipient has 120 days to accept the shared framework. When they accept, Audit Manager replicates the shared custom framework to their framework library in the specified AWS Region. If you want to replicate a custom framework to another Region under your own account, use the following tutorial and enter your own AWS account ID as the recipient account ID. 

## Prerequisites
<a name="framework-sharing-prerequisites"></a>

Before you start this tutorial, make sure that you first meet the following conditions:
+ You're familiar with Audit Manager [framework sharing concepts and terminology](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html). 
+ The custom framework that you want to share is [eligible for sharing](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html#eligibility) and exists in the framework library of your AWS Audit Manager environment. 
+ The recipient already enabled AWS Audit Manager in the AWS Region where you want to share the custom framework.
+ The recipient is not an AWS Organizations management account.
+ Your IAM identity has appropriate permissions to share a custom framework in AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

**Tip**  
Before you start, make a note of the AWS account ID that you want to share your custom framework with. This can be your own account ID, if your goal is to replicate the framework to another AWS Region under your account. You need this information for step 2 of the tutorial. 

## Procedure
<a name="deleting-shared-framework-requests-procedure"></a>

**Topics**
+ [Step 1: Identify the custom framework that you want to share](#framework-sharing-step-1)
+ [Step 2: Send a share request](#framework-sharing-step-2)
+ [Step 3: View your sent requests](#framework-sharing-step-3)
+ [Step 4 (Optional): Revoke the share request](#framework-sharing-step-4)

### Step 1: Identify the custom framework that you want to share
<a name="framework-sharing-step-1"></a>

Start by identifying the custom framework that you want to share. You can find a list of all available custom frameworks on the **Framework library** page in Audit Manager. 

**Important**  
Don’t share custom frameworks that contain sensitive data. This includes data found within the framework itself, its control sets, and any of the custom controls that comprise the custom framework. For more information, see [Framework eligibility](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html#eligibility).

**To view your available custom frameworks**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Framework library**.

1.  Choose the **Custom frameworks** tab. This displays a list of your available custom frameworks. You can choose any framework name to view the details of that custom framework.

### Step 2: Send a share request
<a name="framework-sharing-step-2"></a>

Next, specify a recipient and send them a share request for the custom framework. The recipient has 120 days to respond to the share request before it expires. 

**To send a share request**

1. From the **Custom frameworks** tab of the framework library, choose the name of a framework to open the detail page. From here, choose **Actions** and then choose **Share custom framework**.
   + Alternatively, select a custom framework from the list in the framework library, choose **Actions**, and then choose **Share custom framework**. Depending on the size of the custom framework, this method can take a few seconds while Audit Manager prepares the share request.

1. Review the notice that displays in the dialog box.
   + If you're unsure whether you can share your custom framework, review [Framework eligibility](https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html#eligibility) for further guidance. 
   + If your framework has controls that use custom AWS Config rules as a data source, we recommend that you contact the recipient to let them know. The recipient can then create and enable the same AWS Config rules in their instance of AWS Config. For more information, see [My shared framework has controls that use custom AWS Config rules as a data source. Can the recipient collect evidence for these controls?](framework-issues.md#framework-sharing-custom-config-rules). 

1. Enter **agree** and then choose **Agree** to proceed.

1. On the next screen, follow these steps:
   + Under **AWS account**, enter the recipient’s account ID. This can be your own account ID. 
   + Under **AWS Region**, select the recipient's Region from the dropdown list.
   + (Optional) Under **Message to recipient**, enter an optional comment about the custom framework that you're sharing.
   + Under **Custom framework details**, review the details to confirm that you want to share this framework.

1. Choose **Share**.

**Note**  
Keep in mind the following points:  
When you share a custom framework with another AWS account, the framework is replicated only to the specified AWS Region. After accepting the share request, the recipient can then replicate the framework across Regions as needed. 
When sharing custom frameworks across AWS Regions, it can take up to 10 minutes to process share request actions. After sending a cross-Region share request, we recommend that you check back later to confirm that your share request was sent successfully. 
When you send a share request, Audit Manager takes a snapshot of the custom framework at the time of the share request creation. If you update the custom framework after sending a share request, the request isn't automatically updated. To share the latest version of an updated framework, you can [resend the share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-resend). The expiration date of this new snapshot is 120 days from the re-share date.

### Step 3: View your sent requests
<a name="framework-sharing-step-3"></a>

You can select the **Sent requests** tab to see a list of all the share requests that you sent. You can filter this list as needed. For example, you can apply filters to display only requests that expire within the next 30 days. 

**To view and filter your sent requests**

1. From the navigation pane, choose **Share requests**.

1. Choose the **Sent requests** tab.

1. (Optional) Apply filters to fine-tune which sent requests are visible. You can do this by finding the **All statuses** dropdown list, and changing the filter to one of the following.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html)

**Note**  
It can take up to 15 minutes to process a share request. As a result, if an error occurred when sending your share request to the recipient, the *Failed* status might not display immediately. We recommend that you check back later to confirm that your share request was sent successfully. 

### Step 4 (Optional): Revoke the share request
<a name="framework-sharing-step-4"></a>

If you need to cancel an active share request before it’s due to expire, you can revoke the request at any time. This step is optional. If you take no action, the recipient loses the ability to accept the share request after the expiration date.

**To revoke a share request**

1. From the navigation pane, choose **Share requests**.

1. Choose the **Sent requests** tab.

1. Select the framework that you want to revoke and choose **Revoke request**.

1. In the pop-up window that appears, choose **Revoke**.

**Note**  
You can only revoke access to share requests that have a status of *Active* or *Expiring*. After a recipient accepts a share request, you can no longer revoke their access to that custom framework. This is because a copy of the custom framework now exists in the recipient’s framework library.   
When sharing frameworks across AWS Regions, it can take up to 10 minutes to process share request actions. After revoking a cross-Region share request, we recommend that you check back later to confirm that the share request was revoked successfully. 

## Next steps
<a name="deleting-shared-framework-requests-next-steps"></a>

### Resending a share request for an updated framework
<a name="framework-sharing-resend"></a>

You might send a share request for a custom framework and then update the same framework afterwards. If you do this, the share request isn't automatically updated to reflect the latest version of the framework. However, if its status is *active*, *shared*, or *expiring*, you can update an existing share request. To do this, you resend a new share request with the same set of details as the existing request. In the new share request, include the same custom framework ID, recipient account ID, and recipient AWS Region. You can also provide a new comment with the new share request.

Keep in mind the following when you resend a share request: 
+ For the update to be successful, the new request must be for the same custom framework ID. It must also specify the same recipient account ID and Region as the existing request.
+ If the name of the custom framework has changed, the updated share request displays the latest name. 
+ If you provide a new comment, the updated share request displays the latest comment. 
+ When you resend a share request, the expiration date is extended by six months. 

**To resend a share request for an updated framework**

1. From the **Custom frameworks** tab of the framework library, choose the name of the framework that you want to share. This opens the framework detail page. 

1. Choose **Actions** and then choose **Share custom framework**. 

1. Review the notice that displays in the dialog box, enter **agree**, and then choose **Agree** to proceed.

1. On the next screen, follow these steps:
   + Under **AWS account**, enter the same account ID that you specified in the existing share request. 
   + Under **AWS Region**, select the same Region that you specified in the existing share request.
   + (Optional) Under **Message to recipient**, enter an optional comment about the updated custom framework.
   + Under **Custom framework details**, review the details to confirm that you want to resend the share request.

1. Choose **Share** to resend and update the share request.

## Additional resources
<a name="deleting-shared-framework-requests-additional-resources"></a>

To find solutions to the issues that you might encounter when sharing a custom framework, see [Troubleshooting framework issues](framework-issues.md).