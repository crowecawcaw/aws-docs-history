

# Troubleshooting an integration

The following topics explain how to create a support case and troubleshoot common onboarding and integration errors.

**Topics**
+ [Raising support cases](#raising-support-cases)
+ [Onboarding error messages](#troubleshooting-during-crm-integration-onboarding)

## Raising support cases
<a name="raising-support-cases"></a>

If you still have difficulties integrating your CRM with AWS, follow these steps to raise a support case. 

1. Open the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console.

1. Choose **Get support**.

1. In the support chat, describe your CRM integration issue, including errors and the troubleshooting steps you tried.

1. Answer the chat's questions. If your issue needs a support case, the chat displays a case form with the details filled in.

1. Review the case form, and attach sync logs and screenshots.

1. Choose **Submit**. The chat displays your case ID.

For more information, see [Create a support case](https://docs.aws.amazon.com/partner-central/latest/getting-started/getting-support.html#how-support-chat-works).

## Onboarding error messages
<a name="troubleshooting-during-crm-integration-onboarding"></a>

The following table lists and describes some common error messages and their resolutions.


| Error message  | Error condition  | Resolution steps  | 
| --- | --- | --- | 
| Only Alliance Lead contact can make this request.  | When anyone other than an Alliance Lead (ACE eligible) tries to: update request status, access request details, abandon request, create new request.  | For internal users: Verify that the partner account is ACE eligible.  | 
| Failed to mark implementation as complete. Please try again.  | When you try to mark a request as implementation complete but there an error occurred during the update.  | Contact the support team.  | 
| No Request received.  | When you try to abandon a request and there are no requests to abandon.  |  | 
| Your request could not be taken at this time because of an internal error. Check again after some time.  | Occurs when internal errors occur when abandoning a request, or during request processing.  | Contact the support team.  | 
| Please provide ARN Details for the IAM User/Role to provision bucket for …  | Occurs when you don't provide an ARN for the beta or production IAM user.  | IAM details cannot be empty.  | 
| Duplicate Request: Bucket ARN details already created and provisioned for this IAM User/Role.  | Occurs when another request is created for the same partner with the same IAM details and the request is not abandoned.  | Abandon the existing request.  | 
| Please update the IAM ARN details in the existing request.  | Occurs when the system tried to process the request and the request failed due to an error.  | Update the IAM ARN details and resubmit.  | 
| Your request could not be taken at this time because of an internal error. Check again after some time.  | After a request is submitted and something during the processing failed.  | Contact the support team.  | 