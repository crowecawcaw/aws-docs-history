# Troubleshooting an integration

The following topics explain how to create a support case and troubleshoot common
onboarding and integration errors.

###### Topics

- [Raising support cases](#raising-support-cases "#raising-support-cases")
- [Onboarding error messages](#troubleshooting-during-crm-integration-onboarding "#troubleshooting-during-crm-integration-onboarding")

## Raising support cases

If you still have difficulties integrating your CRM with AWS, follow these steps to
raise a support case.

1. Sign in to the [AWS Partner
   Central](https://partnercentral.awspartner.com "https://partnercentral.awspartner.com") with your AWS Partner Network credentials.
2. On the [Support Center for
   Partner Central](https://partnercentral.awspartner.com/support "https://partnercentral.awspartner.com/support"), choose **Open New Case** and
   complete the following fields:
   - **Type of Support Case** – AWS Partner
     Central.
   - **Question regarding** – Partner Central
     Tools or ACE leads and opportunities.
   - **Get Specific** – Select the most
     appropriate CRM integration case type.
   - **Subject** – Include a brief description
     of the request.
   - **Description** – Provide a detailed
     description of issues, questions, errors, and troubleshooting steps.
   - **Attachments** – Sync logs and
     screenshots, where applicable.

## Onboarding error messages

The following table lists and describes some common error messages and their
resolutions.

| Error message                                                                                              | Error condition                                                                                                                                         | Resolution steps                                                     |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Only Alliance Lead contact can make this request.                                                          | When anyone other than an Alliance Lead (ACE eligible) tries to: update request<br>status, access request details, abandon request, create new request. | For internal users: Verify that the partner account is ACE eligible. |
| Failed to mark implementation as complete. Please try again.                                               | When you try to mark a request as **implementation complete**<br>but there an error occurred during the update.                                         | Contact the support team.                                            |
| No Request received.                                                                                       | When you try to abandon a request and there are no requests to abandon.                                                                                 |                                                                      |
| Your request could not be taken at this time because of an internal error.<br>Check again after some time. | Occurs when internal errors occur when abandoning a request, or during request<br>processing.                                                           | Contact the support team.                                            |
| Please provide ARN Details for the IAM User/Role to provision bucket for …                                 | Occurs when you don't provide an ARN for the beta or production IAM user.                                                                               | IAM details cannot be empty.                                         |
| Duplicate Request: Bucket ARN details already created and provisioned for this<br>IAM User/Role.           | Occurs when another request is created for the same partner with the same IAM<br>details and the request is not abandoned.                              | Abandon the existing request.                                        |
| Please update the IAM ARN details in the existing request.                                                 | Occurs when the system tried to process the request and the request failed due<br>to an error.                                                          | Update the IAM ARN details and resubmit.                             |
| Your request could not be taken at this time because of an internal error.<br>Check again after some time. | After a request is submitted and something during the processing failed.                                                                                | Contact the support team.                                            |
