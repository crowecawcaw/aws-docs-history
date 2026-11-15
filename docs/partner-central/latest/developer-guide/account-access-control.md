

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Access for the Account API
<a name="account-access-control"></a>

Access control and permissions are managed by AWS Identity and Access Management (IAM). This section provides guidance for configuring the necessary permissions to interact with the Account API.

## Prerequisites
<a name="account-prerequisites"></a>

Before configuring permissions, ensure that your AWS account is linked to and that you created the necessary IAM roles and users. For more information, see [Setup and authentication](setup-authentication.md).

## Using AWS managed policies
<a name="account-using-aws-managed-policies"></a>

AWS provides managed policies that grant the required permissions to interact with the Account API. To provide the necessary access to manage account resources, attach the `AWSPartnerCentralFullAccess` policy to your IAM identities. For more information, see [AWS managed policies for users](https://docs.aws.amazon.com/partner-central/latest/getting-started/managed-policies.html).

## Assigning policies to IAM roles and users
<a name="account-assigning-policies"></a>

Follow these steps to assign policies to IAM roles and users:

1. Sign in to the AWS Management Console.

1. Navigate to the IAM service.

1. Select roles or users, and choose the IAM role or user to which you want to attach a policy.

1. Attach the `AWSPartnerCentralFullAccess` policy to the selected IAM role or user.

For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

## Managing permissions using condition keys
<a name="account-managing-permissions-with-condition-keys"></a>

Condition keys in IAM policies provide resource-level permissions for when to enforce statement policies. You can use condition keys to specify conditions that dictate when certain permissions are allowed or denied.

For more information, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html).

The following table lists the condition keys that you can use in policy statements for Account API actions. The keys are grouped by the operations that they apply to. The first row applies to all operations and the second row to verification. The other rows apply to business plans, and the last three of them are the tag condition keys.


**Condition keys overview**  

| Condition key | Description | Applicable actions | Valid values | 
| --- | --- | --- | --- | 
| partnercentral:Catalog | Filters access by the type of the associated catalog entity | All actions | AWS, Sandbox | 
| partnercentral:VerificationType | Filters access by the type of verification. | StartVerification and GetVerification | The valid values are BUSINESS\_VERIFICATION and REGISTRANT\_VERIFICATION. | 
| partnercentral:BusinessPlanItemType | Filters access by the type of the business plan item | CreateBusinessPlanItem, GetBusinessPlanItem, UpdateBusinessPlanItem, and DeleteBusinessPlanItem | GOAL, KPI, INITIATIVE, ACTIVITY, PARTNERSHIP\_GOAL, STRATEGIC\_GOAL | 
| partnercentral:BusinessPlanItemStage | Filters access by the stage of the business plan item | CreateBusinessPlanItem, GetBusinessPlanItem, UpdateBusinessPlanItem, and DeleteBusinessPlanItem | ONBOARD, BUILD, MARKET, SELL | 
| partnercentral:AllowAwsEngagement | Filters access by whether you allow AWS to make changes to your business plans | CreateBusinessPlan, UpdateBusinessPlan, CancelBusinessPlan, CreateBusinessPlanItem, UpdateBusinessPlanItem, DeleteBusinessPlanItem, StartBusinessPlanSubmissionTask, CancelBusinessPlanSubmissionTask, StartBusinessPlanAttachmentImportTask, and DeleteBusinessPlanAttachment | ENABLED, DISABLED | 
| aws:ResourceTag/${TagKey} | Filters access by the tags attached to the business plan | Business plan actions that name an existing plan | The tag value for the tag key | 
| aws:RequestTag/${TagKey} | Filters access by the tags in the request | CreateBusinessPlan, and TagResource when you create a plan with tags | The tag value for the tag key | 
| aws:TagKeys | Filters access by the tag keys in the request | CreateBusinessPlan, and TagResource when you create a plan with tags | Tag keys | 

For `CreateBusinessPlanItem`, the item type and stage come from the request. For the other item actions, they come from the stored item. When `UpdateBusinessPlanItem` changes the stage of an item, your policy must allow the request for both the current stage and the new stage.

If an item has no stage, the request doesn't include `partnercentral:BusinessPlanItemStage`. To allow requests for these items, use a condition operator that ends in `IfExists`, such as `StringEqualsIfExists`.

The value of `partnercentral:AllowAwsEngagement` is the `AllowAwsEngagement` business plan setting for the catalog. You set it with `PutBusinessPlanSettings`. If you haven't set it, the value is `DISABLED`.

## Summary of required permissions
<a name="account-summary-of-required-permissions"></a>

The following tables list the IAM action for each Account API operation and what the action lets you do, grouped by area. For more information about business plan actions, see [Business plan permissions](#account-business-plan-permissions).

The following table lists the actions for partner registration, partner profiles, and domain management.


| Action | What you can do | 
| --- | --- | 
| partnercentral:AssociateAwsTrainingCertificationEmailDomain | Associate AWS training certification email domains. | 
| partnercentral:CancelProfileUpdateTask | Cancel profile update tasks. | 
| partnercentral:CreatePartner | Create partners. | 
| partnercentral:DisassociateAwsTrainingCertificationEmailDomain | Disassociate AWS training certification email domains. | 
| partnercentral:GetAllianceLeadContact | Get alliance lead contact details. | 
| partnercentral:GetPartner | Get partner details. | 
| partnercentral:GetProfileUpdateTask | Get profile update task details. | 
| partnercentral:GetProfileVisibility | Get profile visibility settings. | 
| partnercentral:ListPartners | List partners. | 
| partnercentral:PutAllianceLeadContact | Update alliance lead contact details. | 
| partnercentral:PutProfileVisibility | Update profile visibility settings. | 
| partnercentral:SendEmailVerificationCode | Send email verification codes. | 
| partnercentral:StartProfileUpdateTask | Start profile update tasks. | 

The following table lists the actions for partner connections.


| Action | What you can do | 
| --- | --- | 
| partnercentral:AcceptConnectionInvitation | Accept connection invitations. | 
| partnercentral:CancelConnection | Cancel connections. | 
| partnercentral:CancelConnectionInvitation | Cancel connection invitations. | 
| partnercentral:CreateConnectionInvitation | Create connection invitations. | 
| partnercentral:GetConnection | Get connection details. | 
| partnercentral:GetConnectionInvitation | Get connection invitation details. | 
| partnercentral:GetConnectionPreferences | Get connection preferences. | 
| partnercentral:ListConnectionInvitations | List connection invitations. | 
| partnercentral:ListConnections | List connections. | 
| partnercentral:RejectConnectionInvitation | Reject connection invitations. | 
| partnercentral:UpdateConnectionPreferences | Update connection preferences. | 

The following table lists the actions for partner verification.


| Action | What you can do | 
| --- | --- | 
| partnercentral:GetVerification | Get verification details. | 
| partnercentral:StartVerification | Start verification processes. | 

## Business plan permissions
<a name="account-business-plan-permissions"></a>

Each business plan operation requires the IAM action with the same name, for example `partnercentral:CreateBusinessPlan` for `CreateBusinessPlan`. The `AWSPartnerCentralFullAccess` managed policy grants all of them. Their condition keys are in [Managing permissions using condition keys](#account-managing-permissions-with-condition-keys). For details about each operation, see [Working with business plans](working-with-business-plans-api.md).

The following table lists the business plan actions.


| Action | What you can do | 
| --- | --- | 
| partnercentral:AssociateBusinessPlan | Link business plan items to opportunities or campaigns. | 
| partnercentral:CancelBusinessPlan | Cancel business plans. | 
| partnercentral:CancelBusinessPlanSubmissionTask | Withdraw business plans from review. | 
| partnercentral:CreateBusinessPlan | Create business plans. | 
| partnercentral:CreateBusinessPlanItem | Create business plan items. | 
| partnercentral:DeleteBusinessPlanAttachment | Delete business plan attachments. | 
| partnercentral:DeleteBusinessPlanItem | Delete business plan items. | 
| partnercentral:DisassociateBusinessPlan | Remove links between business plan items and opportunities or campaigns. | 
| partnercentral:GetBusinessPlan | Get business plan details. | 
| partnercentral:GetBusinessPlanAttachment | Get business plan attachments. | 
| partnercentral:GetBusinessPlanAttachmentImportTask | Get attachment import task details. | 
| partnercentral:GetBusinessPlanItem | Get business plan item details. | 
| partnercentral:GetBusinessPlanItemSchema | Get the business plan item schema. | 
| partnercentral:GetBusinessPlanSettings | Get business plan settings. | 
| partnercentral:GetBusinessPlanSubmissionTask | Get submission task details. | 
| partnercentral:ListBusinessPlanAssociations | List links between business plan items and opportunities or campaigns. | 
| partnercentral:ListBusinessPlanAttachmentImportTasks | List attachment import tasks. | 
| partnercentral:ListBusinessPlanAttachments | List business plan attachments. | 
| partnercentral:ListBusinessPlanHistory | List business plan history. | 
| partnercentral:ListBusinessPlanItems | List business plan items. | 
| partnercentral:ListBusinessPlans | List business plans. | 
| partnercentral:ListBusinessPlanSubmissionTasks | List submission tasks. | 
| partnercentral:PutBusinessPlanSettings | Update business plan settings. | 
| partnercentral:StartBusinessPlanAttachmentImportTask | Add attachments to business plans. | 
| partnercentral:StartBusinessPlanSubmissionTask | Submit business plans for review. | 
| partnercentral:UpdateBusinessPlan | Update business plans. | 
| partnercentral:UpdateBusinessPlanItem | Update business plan items. | 

Operations that name a business plan check the action against that plan. In the `Resource` element of a policy statement, you identify a plan by its Amazon Resource Name (ARN). A business plan ARN contains the following values:

`{{my-account-id}}`  
The ID of your AWS account.

`{{my-catalog}}`  
`AWS` or `Sandbox`.

`{{my-plan-id}}`  
The ID of the plan, such as `bp-a1b2c3d4e5f6g`, or `*` to match every plan in the catalog.

To identify a plan in a policy statement, replace `{{my-account-id}}`, `{{my-catalog}}`, and `{{my-plan-id}}` in the following ARN with the values from the preceding list:

```
arn:aws:partnercentral:us-east-1:{{my-account-id}}:catalog/{{my-catalog}}/business-plan/{{my-plan-id}}
```

The account in the ARN is always your own account. You can't grant access to business plans in another AWS account.

The following operations don't name an existing plan. A statement must allow them on all resources (`"Resource": "*"`):
+ `CreateBusinessPlan`, `ListBusinessPlans`, and `GetBusinessPlanItemSchema`
+ `GetBusinessPlanSettings` and `PutBusinessPlanSettings`
+ `ListBusinessPlanItems` and `ListBusinessPlanAssociations`, when you call them without a `PlanIdentifier`

All other business plan operations act on a specific plan. So do `ListBusinessPlanItems` and `ListBusinessPlanAssociations` when you call them with a `PlanIdentifier`. Allow these operations on the plan's ARN, or use `*` as `{{my-plan-id}}` to cover every plan in the catalog.

To create a plan with tags, you also need `partnercentral:TagResource` on `arn:aws:partnercentral:us-east-1:{{my-account-id}}:catalog/{{my-catalog}}/business-plan/*`. Both permissions must allow the request.