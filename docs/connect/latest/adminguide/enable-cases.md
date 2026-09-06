

# Enable Cases using the Connect Customer console
<a name="enable-cases"></a>

This topic explains how to enable Connect Customer Cases using the Connect Customer console. To use the API, see [Connect Customer Cases API Reference](https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html).

**Tip**  
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
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. On the left navigation menu, choose **Cases** under the **Applications** section. If you don't see this option, it might not be available in your Region. For information about where Cases is available, see [Cases availability by Region](regions.md#cases_region). 

1. Choose **Enable cases** to get started.

1. On the **Cases** page, choose **Add domain**. 

1. On the **Add domain** page, enter a unique, friendly name that's meaningful to you, such as your organization name.

1. Choose **Add domain**. The domain is created.

   If the domain is not created, choose **Try again**. If that doesn't work, contact Support.

**Tip**  
To delete a Cases domain, use the [DeleteDomain](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteDomain.html) API. 

## Next steps
<a name="enable-cases-next-steps"></a>

After your cases domain is created, do the following:

1. [Assign security profile permissions](assign-security-profile-cases.md) to agents and call center managers.

1. [Create case fields](case-fields.md). Fields are the building blocks of your case templates.

1. [Create case templates](case-templates.md). Case templates are forms that agents complete and reference in the agent application. Templates ensure the right information is collected and referenced for different types of customer issues.

1. Optionally, [enable attachments](enable-attachments.md) across your Connect Customer instance. This step allows your agents to upload files to cases. For more information on the Files API, see the [StartAttachedFileUpload](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartAttachedFileUpload.html) API documentation.
**Note**  
Make sure that you have the `cases:CreateRelatedItem ` permission for your IAM entity. For more information on Cases permissions, see [Actions, resources, and condition keys for Connect Customer Cases](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnectcases.html).

1. Optionally, add the [Cases](cases-block.md) block to your flows. With this block, you can get, update, or create cases automatically.

1. Optionally, set up [case event streams](case-event-streams.md) to get near real-time updates when cases are created or modified.

1. Optionally, set up a [AI agents domain](ai-agent-initial-setup.md) and [Configure your flow](ai-agent-initial-setup.md#enable-ai-agents-step4) to generate AI-powered Case Summaries in the agent workspace

1. Optionally, [set up tag-based access controls for cases](cases-tag-based-access-control.md).