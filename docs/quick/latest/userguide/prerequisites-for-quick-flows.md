

# Prerequisites for Quick Flows
<a name="prerequisites-for-quick-flows"></a>

 Before you can create and use Amazon Quick Flows, you need to ensure that your Amazon Quick administrator has completed the following prerequisites. 

## Administrator setup requirements
<a name="admin-setup-requirements"></a>

Your Quick administrator must complete the following tasks before you can create and use Quick Flows:
+ Set up and configure Quick for your organization. For more information, see [Setting up and signing into Amazon Quick](setting-up.md).
+ (Optional) Restrict access to flows for specific users using custom permissions.

For browser and region requirements, see [Supported browsers](supported-browsers.md).

## Required permissions
<a name="required-permissions-quick-flows"></a>

Permissions to create, run, share, and govern flows are determined by user subscriptions and any configured custom permissions. For more information, see [Managing Quick subscriptions](managing-subscriptions.md) and [Managing user access inside Amazon Quick](managing-users.md).

## Amazon Bedrock model access
<a name="bedrock-model-access"></a>

Quick Flows uses Amazon Bedrock models for AI reasoning in the General knowledge step. Your administrator must enable access in custom permissions for output refinement in flows using Bedrock models. For more information, see [General knowledge](ai-response-steps.md#general-knowledge-step).

## Next steps
<a name="next-steps-prereq"></a>

After ensuring that all prerequisites are met, you can:
+ Learn about key concepts in Quick Flows. See [Terminology and key concepts](terminology-and-key-concepts.md).
+ Create your first flow. See [Creating flows](creating-flows.md).