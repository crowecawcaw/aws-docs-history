

# Chat applications policies
<a name="orgs_manage_policies_chatbot"></a>

Chat applications policies in AWS Organizations enable you to control access to your organization's accounts from chat applications such as Slack and Microsoft Teams.

[Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) is an AWS service that enables DevOps and software development teams to use messaging program chat rooms to monitor and respond to operational events in their AWS Cloud. Amazon Q Developer in chat applications processes AWS service notifications from Amazon Simple Notification Service (Amazon SNS), and forwards them to chat rooms so teams can analyze and act on them immediately, regardless of location.

## How chat applications policies work
<a name="orgs_manage_policies_chatbot_how_work"></a>

Using chat applications policies, the management account or delegated administrator of an organization can do the following across an organization:
+ Enforce which supported chat applications (Amazon Chime, Microsoft Teams, and Slack) can be used.
+ Restrict chat client access to specific workspaces (Slack) and teams (Microsoft Teams).
+ Restrict Slack channel visibility to either public or private channels.
+ Set and enforce specific [role settings](https://docs.aws.amazon.com/chatbot/latest/adminguide/understanding-permissions.html#role-settings).

Chat applications policies restrict and take precedence over account level settings such as [role settings](https://docs.aws.amazon.com/chatbot/latest/adminguide/understanding-permissions.html#role-settings) and [channel guardrail policies](https://docs.aws.amazon.com/chatbot/latest/adminguide/understanding-permissions.html#channel-guardrails). You can access and modify chat applications policies from the Amazon Q Developer in chat applications or the Organizations console.

After the policies are attached to accounts and organizational units (OU), any current and future Amazon Q Developer in chat applications configurations for the accounts in scope will automatically comply with the governance and permissions settings. For more information, see [Understanding declarative policy inheritance](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html).

If you try to perform an action restricted by a chat applications policy, an error message will notify you that the action is not allowed due to the chat applications policy with the recommendation to contact the management account or delegated administrator of your organization.

**Note**  
Chat applications policies are validated at runtime. This means that existing resources are continuously checked for compliance. There is no overlap with existing IAM permissions since runtime-based IAM permissions for sending notifications or interacting with Amazon Q Developer in chat applications are not currently supported.