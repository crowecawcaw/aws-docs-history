

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with business plans

A business plan describes your priorities for your AWS partnership for one plan year. A plan has a narrative, items such as goals, key performance indicators (KPIs), initiatives, and activities, and optional attachments. When the plan is ready, you submit it for review by AWS.

Business plan operations are part of the AWS Partner Central Account API. They use the same endpoint (`partnercentral-account.us-east-1.api.aws`), the same signing name (`partnercentral-account`), and the same `Catalog` parameter as the other Account API operations. Business plans are available only in the US East (N. Virginia) Region (`us-east-1`).

To call these operations, your AWS account must be registered as an AWS Partner in the catalog that you request. Otherwise, the call fails with an `AccessDeniedException` with the reason `INCOMPATIBLE_BENEFIT_AWS_PARTNER_STATE`.

## Business plan resources
<a name="business-plan-api-resources"></a>

The business plan API works with the following resources:

Business plan  
The plan itself. Each plan has an ID such as `bp-a1b2c3d4e5f6g` and an Amazon Resource Name (ARN). To build a plan's ARN, replace `{{my-account-id}}` with the ID of your AWS account, `{{my-catalog}}` with `AWS` or `Sandbox`, and `{{my-plan-id}}` with the plan ID in the following format:  

```
arn:aws:partnercentral:us-east-1:{{my-account-id}}:catalog/{{my-catalog}}/business-plan/{{my-plan-id}}
```
Operations that take a `PlanIdentifier` or `Identifier` accept either the plan ID or the plan ARN. If you pass an ARN, its catalog must match the `Catalog` parameter.

Plan item  
A goal, key performance indicator (KPI), initiative, or activity in a plan. Items have IDs such as `bpitem-a1b2c3d4e5f6g`, and you address them by plan and item ID. Plans that AWS migrated to AWS Partner Central can also have `PARTNERSHIP_GOAL` and `STRATEGIC_GOAL` items. You can't create items of these types.

Attachment  
A file attached to a plan. A file name identifies the attachment within its plan.

Task  
An asynchronous request for a plan. Submission tasks submit a plan for review, and attachment import tasks add a file to a plan. Task IDs look like `bptask-a1b2c3d4e5f6g`.

Association  
A link between a plan item and a AWS Partner Central opportunity or a campaign.

Settings  
Your business plan settings for a catalog, such as whether AWS can make changes to your plans.

## Business plan statuses
<a name="business-plan-api-statuses"></a>

The following table lists the business plan statuses and whether you can edit a plan in each status.


| Status | Description | Can you edit the plan? | 
| --- | --- | --- | 
| DRAFT | The plan is new, or it returned from review. CreateBusinessPlan creates plans in this status. | Yes | 
| IN\_REVIEW | You submitted the plan, and AWS is reviewing it. | No | 
| ACTIVE | AWS approved the plan. | Yes | 
| CANCELED | You canceled the plan with CancelBusinessPlan, or AWS canceled it. This status is final. | No | 
| COMPLETED | The plan's end date passed while the plan was ACTIVE. This status is final. | No | 

You can read a plan and its items, attachments, and history in every status. Plans are never deleted.

## Creating and submitting a business plan
<a name="business-plan-api-workflow"></a>

These steps take a new plan through its first review. Before you begin, make sure that your AWS account is registered as an AWS Partner in the catalog that you plan to use. For more information about the resources that the steps create, see [Business plan resources](#business-plan-api-resources). After AWS approves a plan, you can keep it current as described in [Updating a business plan](#business-plan-api-updating).

**To create a business plan and submit it for review**

1. To create the plan, call `CreateBusinessPlan` with the plan's `Catalog`, `Name`, `EndedAt`, and `Location`.

1. To get the rules for the plan's items, call `GetBusinessPlanItemSchema`. Use the schema in the response to build the `Detail` of each item.

1. To add the plan's goals, key performance indicators (KPIs), initiatives, and activities, call `CreateBusinessPlanItem` once for each item.

1. (Optional) To attach a file, call `StartBusinessPlanAttachmentImportTask` with the file's `FileUrl`.

1. (Optional) To confirm that AWS Partner Central added the file, call `GetBusinessPlanAttachmentImportTask` until the task status is `SUCCEEDED` or `FAILED`.

1. To submit the plan for review, call `StartBusinessPlanSubmissionTask`.

1. To check the result of the review, call `GetBusinessPlanSubmissionTask`.

A `GetBusinessPlan` response shows the result in the plan status, and you can receive the result as an event. For more information about business plan events, see [Notifications for the AWS Partner Central Account API](account-api-events.md).

When AWS finishes the review, the result is one of the following:
+ AWS approved the plan. The task status is `SUCCEEDED`, and the plan status is `ACTIVE`.
+ AWS asked for changes. The task status is `FAILED` with the error code `REWORK_NEEDED`, and the plan returns to `DRAFT`. Update the plan, and then submit it again.

To withdraw a plan from review, call `CancelBusinessPlanSubmissionTask` with the ID of the open task. The plan returns to `DRAFT`.

When you call `CreateBusinessPlan`, the plan year is the UTC year of the end date, and it must be the current year or the next year. Plan names must be unique in your account for each catalog. If you don't provide an `AnalysisDocument`, the plan starts with a narrative template. The narrative is Markdown text.

The `GetBusinessPlanItemSchema` response contains the JSON Schema (draft-07) that the plan's items must follow.

To link items to each other, add goals and key performance indicators (KPIs) first, then initiatives, and then activities. Goals, KPIs, and initiatives belong directly to the plan. An activity belongs to an initiative, so its `CreateBusinessPlanItem` request needs the initiative's ID in `ParentItemId`. An initiative or activity can list the goals and KPIs that it contributes to in `ContributesToItemIds`.

In a `StartBusinessPlanAttachmentImportTask` request, the `FileUrl` can be an HTTPS URL that AWS Partner Central can download without credentials, such as a presigned Amazon S3 URL. AWS Partner Central scans and copies the file asynchronously. If the file name matches an existing attachment, the new file replaces it.

Before you call `StartBusinessPlanSubmissionTask`, make sure that the plan is in `DRAFT` status and contains the content that its item schema requires. A plan can have only one open submission task. After the call succeeds, the plan status is `IN_REVIEW`, and the task status is `IN_PROGRESS`.

## Updating a business plan
<a name="business-plan-api-updating"></a>

You can update a plan and its items when the plan is in `DRAFT` or `ACTIVE` status. Updates to a plan in `IN_REVIEW`, `CANCELED`, or `COMPLETED` status fail with a `ConflictException` and the reason `INCOMPATIBLE_BUSINESS_PLAN_STATE`.
+ To change the plan's name, end date, location, or narrative, call `UpdateBusinessPlan`. Fields that you omit keep their current values.
+ To change an item, call `UpdateBusinessPlanItem`. To stop working on an item without removing it, set its `Status` to `DROPPED`. You can change it back later.
+ To remove an item permanently, call `DeleteBusinessPlanItem`. You can delete items only from a plan in `DRAFT` status, and only when the item has no child activities, contribution links, or associations.
+ To remove an attachment, call `DeleteBusinessPlanAttachment`.
+ To cancel a plan that you no longer need, call `CancelBusinessPlan`. This also cancels any open submission task. You can't undo this action.

To see what changed in a plan and its items, and whether you or AWS made each change, call `ListBusinessPlanHistory`.

## Letting AWS make changes to your plans
<a name="business-plan-api-aws-engagement"></a>

Your assigned AWS team can help you build your business plans. For your AWS team to make changes, you need both of the following:
+ The `AWSServiceRoleForPartnerCentralAccount` service-linked role in your AWS account. For more information, see [Managing service-linked roles for business plans](https://docs.aws.amazon.com/partner-central/latest/getting-started/using-roles-for-partner-central-account.html) in the *AWS Partner Central Getting Started Guide*.
+ AWS engagement turned on for the catalog. Call `PutBusinessPlanSettings` with `AllowAwsEngagement` set to `ENABLED`. To check the current setting, call `GetBusinessPlanSettings`.

The setting applies to every plan in the catalog. It controls only changes, so it doesn't affect AWS access to view your plans.

## Choosing a business plan API operation
<a name="business-plan-api-summary"></a>

Every business plan operation requires the `Catalog` parameter. The following table lists the business plan operations and what each one does.


| Operation | Description | 
| --- | --- | 
| CreateBusinessPlan | Creates a plan in DRAFT status. | 
| GetBusinessPlan | Returns a plan. | 
| ListBusinessPlans | Lists your plans. You can filter by status, name, location, and end date. | 
| UpdateBusinessPlan | Updates a plan's name, end date, location, or narrative. | 
| CancelBusinessPlan | Cancels a plan. | 
| ListBusinessPlanHistory | Lists the changes to a plan and its items, newest first. | 
| GetBusinessPlanItemSchema | Returns the JSON Schema that a plan's items must follow. | 
| CreateBusinessPlanItem | Creates a goal, KPI, initiative, or activity. | 
| GetBusinessPlanItem | Returns an item. | 
| ListBusinessPlanItems | Lists items in one plan or across your plans. | 
| UpdateBusinessPlanItem | Updates an item. | 
| DeleteBusinessPlanItem | Deletes an item from a plan in DRAFT status. | 
| StartBusinessPlanAttachmentImportTask | Starts adding a file to a plan. | 
| GetBusinessPlanAttachmentImportTask | Returns an attachment import task. | 
| ListBusinessPlanAttachmentImportTasks | Lists a plan's attachment import tasks, newest first. | 
| GetBusinessPlanAttachment | Returns an attachment's details and a presigned URL to download it. | 
| ListBusinessPlanAttachments | Lists a plan's attachments. | 
| DeleteBusinessPlanAttachment | Deletes an attachment. | 
| StartBusinessPlanSubmissionTask | Submits a plan for review by AWS. | 
| GetBusinessPlanSubmissionTask | Returns a submission task. | 
| ListBusinessPlanSubmissionTasks | Lists a plan's submission tasks, newest first. | 
| CancelBusinessPlanSubmissionTask | Withdraws a plan from review. | 
| AssociateBusinessPlan | Links a plan item to an opportunity or a campaign. | 
| DisassociateBusinessPlan | Removes a link between a plan item and an opportunity or a campaign. | 
| ListBusinessPlanAssociations | Lists links between plan items and opportunities or campaigns. | 
| GetBusinessPlanSettings | Returns your business plan settings for a catalog. | 
| PutBusinessPlanSettings | Turns AWS engagement on or off for a catalog. | 

To add, remove, or list tags on a business plan, use the `TagResource`, `UntagResource`, and `ListTagsForResource` operations with the plan ARN. Plan responses don't include tags.