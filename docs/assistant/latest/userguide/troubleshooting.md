

# Troubleshooting access, permission, and response errors in the AWS assistant
<a name="troubleshooting"></a>

Use the following information to diagnose and fix common problems with the AWS assistant. If a problem continues, see [Contacting AWS Support with the AWS assistant](support.md).

## The AWS assistant icon appears, but you can't use it
<a name="assistant-not-available"></a>

Possible causes:
+ An IAM policy denies `q` actions for your identity.
+ A service control policy (SCP) in your organization denies `q` actions.
+ Your identity doesn't have the permissions that the AWS assistant requires.

**To resolve these issues**

1. Ask your administrator to check whether an IAM policy or SCP denies `q` actions. A policy that denies access to the AWS assistant doesn't hide the AWS assistant icon or chat panel.

1. Ask your administrator to give you the permissions that you need.

To prevent this problem, review deny statements for `q` actions when you change IAM policies or SCPs.

For example policies, see [Identity-based policy examples for the AWS assistant](security-iam-examples.md).

## Response reports insufficient permissions
<a name="assistant-access-denied"></a>

Possible causes:
+ You don't have permission to use the AWS assistant.
+ You don't have permission for the service API or resource in your request.
+ A permissions boundary, session policy, or organization policy denies the action.

**To resolve these issues**

1. Note the action that the response reports as denied.

1. Ask your administrator to review the denied action against your IAM, permissions boundary, session, and organization policies.

1. After your administrator updates your permissions, ask your question again.

To prevent this problem, give your users permissions for the services that they ask about, in addition to the permissions for the AWS assistant.

For more information, see [Identity and access management](security.md#security-iam).

## The AWS assistant can't find a resource
<a name="assistant-resource-missing"></a>

Possible causes:
+ Your prompt doesn't include the resource name, ARN, or Region.
+ The resource doesn't exist, or your identity can't access it.
+ The service doesn't support the required get, list, or describe operation.

**To resolve these issues**

1. Include the resource name or ARN and its Region in your prompt.

1. Verify that the resource exists and that your identity can access it.

1. For resource troubleshooting, enter your prompt in English.

To prevent this problem, specify the Region in prompts about Regional resources.

For more information, see [Chatting about your AWS resources](resources.md).

## Conversation or message is missing
<a name="assistant-conversation-missing"></a>

Possible causes:
+ You didn't ask a new question in the conversation for 90 days.
+ The message is older than 90 days.
+ Your administrator changed the customer managed AWS Key Management Service (AWS KMS) key that encrypts chat data.

**To resolve these issues**

1. Check the age of the conversation or message. You can't recover conversations or messages after the 90-day retention period.

1. If your administrator changed the key, ask your administrator to restore the previous key to access conversations encrypted with it.

To keep a conversation, ask a new question in it within 90 days.

For more information, see [Quotas for the AWS assistant](quotas.md) and [Key management](data-protection.md#key-management).

## Error related to AWS KMS grants
<a name="assistant-kms-grant-error"></a>

Possible causes:
+ The AWS assistant doesn't have permission to create grants for the customer managed AWS KMS key.

**To resolve these issues**

1. Ask your administrator to open the Amazon Q Developer console.

1. In the permissions banner, your administrator chooses **Update permissions**.

To prevent this problem, make sure that your users have the permissions in [Allow the AWS assistant to access customer managed keys](security-iam-examples.md#iam-example-kms).

For more information, see [Key management](data-protection.md#key-management).

## Response is incomplete or incorrect
<a name="assistant-response-problem"></a>

Possible causes:
+ The prompt doesn't include enough detail, such as resource identifiers, Regions, or time ranges.
+ The AWS assistant doesn't have access to the data that the question requires.

**To resolve these issues**

1. Add resource identifiers, Regions, time ranges, and the expected outcome to your prompt.

1. Review the source links and API details before you act on a response.

1. To report a problem, choose the thumbs-down icon.

To prevent this problem, start complex questions with the resource, Region, and time range that you want.

If the issue remains unresolved, see [Contacting AWS Support with the AWS assistant](support.md).