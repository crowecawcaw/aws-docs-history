

# Get started
<a name="manager-assist-getting-started"></a>

Before you can use manager assist, assign the required permissions and verify access.

## Assign permissions
<a name="manager-assist-permissions"></a>

Assign users the following security profile permissions so that they can open the assistant and view performance metrics for users, queues, routing profiles, flows, cases, self-service, AI agents, evaluation forms, and test cases.
+ **Workspace Applications, Connect assistant, **View**** – grants access to the assistant. For information about assigning permissions, see [Security profiles](connect-security-profiles.md).  
![The Workspace Applications section of a security profile, with the View permission selected for Connect assistant.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-permissions.png)
+ **Resource-specific view permissions** – viewing metric data through manager assist requires the same permissions that are required to view that data elsewhere in Connect Customer. For example, to view flows data, you need the **Flows - View** permission, and to view users data, you need the **Users - View** permission. For the full list, see [List of security profile permissions](security-profile-list.md).
+ **Access control tags and agent hierarchies** – you can use resource tags, agent hierarchies, and access control tags to apply granular access to the metric data that is returned. For more information, see [Apply tag-based access control](dashboard-tag-based-access-control.md) and [Apply hierarchy-based access control](dashboard-access-control.md).

## Ask your first question
<a name="manager-assist-ask-first-question"></a>

**To ask a question**

1. In the Connect Customer admin website, choose the assistant icon in the right panel.  
![The assistant panel, with suggested prompts for monitoring the contact center, checking queue performance, and tracking agent availability.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-welcome.png)

1. Type a question, or choose one of the suggested prompts. For example, **How is my contact center performing over the last week?**  
![A question in the chat, and a processing indicator that is displayed while the response is generated.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-processing.png)

1. Review the response, and then ask a follow-up question to drill into your data or to view historical trends. You can also choose from the suggested follow-up prompts. For more information about the types of questions that you can ask, see [Capabilities overview](manager-assist-capabilities.md).  
![A response that includes recommended actions, followed by three suggested follow-up prompts.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-follow-up-prompts.png)