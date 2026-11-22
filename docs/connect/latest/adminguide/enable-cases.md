

# Enable Cases using the Connect Customer console

This topic explains how to enable Connect Customer Cases using the Connect Customer console. To use the API, see [Connect Customer Cases API Reference](https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html).

**Tip**  
When you create an instance, Cases is enabled by default on the **Data storage** step. For more information, see [Step 4: Data storage](amazon-connect-instances.md#get-started-data-storage). To enable Cases for an existing instance, use the following procedure.  
You must have Customer Profiles enabled. Make sure that you check your instance settings in the Connect Customer console, and if a Customer Profiles domain does not yet exist, see [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md).

## Requirements
<a name="cases-iam-requirements"></a>

If you're using custom IAM policies to manage access to the Connect Customer Cases, your users need the following IAM permissions to onboard to Cases using the Connect Customer console:
+ `connect:ListInstances`
+ `ds:DescribeDirectories`
+ `connect:ListIntegrationAssociations`
+ `cases:GetDomain`
+ `cases:CreateDomain`
+ `connect:CreateIntegrationAssociation`
+ `connect:DescribeInstance`
+ `iam:PutRolePolicy`

For more information, see [Required permissions for using custom IAM policies to manage Connect Customer Cases](required-permissions-iam-cases.md).

## How to enable Connect Customer Cases
<a name="how-to-enable-cases"></a>

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias.  
![The Connect Customer virtual contact center instances page, the instance alias.](https://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. On the left navigation menu, choose **Cases** under the **Applications** section. If you don't see this option, it might not be available in your Region. For information about where Cases is available, see [Cases availability by Region](regions.md#cases_region). 

1. Choose **Enable cases** to get started.

1. On the **Cases** page, choose **Add domain**. 

1. On the **Add domain** page, enter a unique, friendly name that's meaningful to you, such as your organization name.

1. Choose **Add domain**. The domain is created.

   If the domain is not created, choose **Try again**. If that doesn't work, contact Support.

**Tip**  
To delete a Cases domain, use the [DeleteDomain](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteDomain.html) API. 

## Enable Cases integrations
<a name="configure-cases-integrations"></a>

The **Cases** page for your instance has an **Integration status** section. It shows whether each Cases integration is set up. Choosing **Configure** completes the same steps as the matching CLI procedure.


| Integration | What it does | CLI procedure | 
| --- | --- | --- | 
| Case event configuration | Turns on case event streams, so an event is published to the default EventBridge event bus each time a case is created, updated, or deleted. | [Step 4: Enable case event streams and setup to receive events into an SQS queue](case-event-streams-enable.md#step4-case-event-streams-enable) | 
| Contact Lens rules | With this integration, you can run conversational analytics rules when a case is created or updated. | [Allow Connect Customer Cases to send updates to conversational analytics rules using the CLI](cases-rules-integration-onboarding.md) | 
| Customer Profiles | Streams case events to a dedicated event bus and uses Amazon AppIntegrations to forward them to Customer Profiles, so cases appear on customer profiles. | [Set up integration for Connect Customer Cases using the CLI](set-up-integration-for-amazon-connect-cases.md) | 

Each integration shows **Enabled**, **Disabled**, or **Unknown**. **Unknown** usually means that you don't have the permissions to read that integration's status.

The following image shows the **Integration status** section on the **Cases** page, where **Case event configuration** is **Enabled** and **Contact Lens rules** and **Customer Profiles** are **Disabled**, each with a **Configure** button.

![The Cases page, the Integration status section showing Case event configuration enabled, and Contact Lens rules and Customer Profiles disabled with Configure buttons.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-integration-status.png)


**To configure an integration**

1. On the **Cases** page, in **Integration status**, choose **Configure** next to the integration.

1. Review the resources that the console creates or reuses. Existing shared resources, including any that you created manually, are reused as is and aren't updated or deleted.

   The **Customer Profiles** integration creates or reuses a dedicated event bus, a forwarding rule on the default event bus, an EventBridge delivery role, a Customer Profiles event integration, and the Connect-case integration with your Customer Profiles domain. The following image shows these resources in the **Configure Customer Profiles integration** dialog box.  
![The Configure Customer Profiles integration dialog box, listing the dedicated event bus, forwarding rule, EventBridge delivery role, event integration, and Connect-case integration.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-configure-customer-profiles-integration.png)

1. Choose **Configure integration**.

Note the following:
+ The **Contact Lens rules** and **Customer Profiles** integrations require case event configuration. Configure **Case event configuration** first.
+ If case event configuration is already turned on but doesn't include all fields, choose **Configure** to update it to include all current and future case fields. Related item settings and other event configuration settings don't change.

  The following image shows the **Update fields included in case events** dialog box, with the fields currently included and the result after the update.  
![The Update fields included in case events dialog box, showing the fields currently included and the result after the update.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-update-event-fields.png)
+ The **Customer Profiles** integration requires a Customer Profiles domain for the instance. If none exists, create one first. For more information, see [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md).
+ If a step fails, resources created by earlier steps stay in place and are reused when you try again.
+ For the required IAM permissions, see [View and configure Cases integrations](required-permissions-iam-cases.md#configure-cases-integrations-iam).

## Next steps
<a name="enable-cases-next-steps"></a>

After your cases domain is created, do the following:

1. [Assign security profile permissions](assign-security-profile-cases.md) to agents and call center managers.

1. [Create case fields](case-fields.md). Fields are the building blocks of your case templates.

1. [Create case templates](case-templates.md). Case templates are forms that agents complete and reference in the agent workspace. Templates ensure the right information is collected and referenced for different types of customer issues.

1. Optionally, [enable attachments](enable-attachments.md) across your Connect Customer instance. This step allows your agents to upload files to cases. For more information on the Files API, see the [StartAttachedFileUpload](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartAttachedFileUpload.html) API documentation.
**Note**  
Make sure that you have the `cases:CreateRelatedItem ` permission for your IAM entity. For more information on Cases permissions, see [Actions, resources, and condition keys for Connect Customer Cases](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnectcases.html).

1. Optionally, add the [Cases](cases-block.md) block to your flows. With this block, you can get, update, or create cases automatically.

1. Optionally, set up [case event streams](case-event-streams.md) to get near real-time updates when cases are created or modified. If you selected **Enable Cases event streams** when you created the instance, or configured **Case event configuration** in **Integration status**, case event streams are already turned on.

1. Optionally, set up a [AI agents domain](ai-agent-initial-setup.md) and [Configure your flow](ai-agent-initial-setup.md#enable-ai-agents-step4) to generate AI-powered Case Summaries in the agent workspace

1. Optionally, [set up tag-based access controls for cases](cases-tag-based-access-control.md).