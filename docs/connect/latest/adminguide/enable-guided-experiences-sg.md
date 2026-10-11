

# Enable step-by-step guides in Connect Customer
<a name="enable-guided-experiences-sg"></a>

Complete the following steps so that administrators can create step-by-step guides and deploy them to users.

1. Enable administrators to create step-by-step guides

   Assign the **Channels and flows - Views** security profile permission to managers and business analysts. This permission lets them configure step-by-step guides in flows.

   Because you build guides with flows, also assign the **Flows - Edit, Create** permissions.  
![The Security profile permissions page, showing the flows and views permissions.](https://docs.aws.amazon.com/connect/latest/adminguide/images/sec-perms-admin-create-sq.png)

1. Enable agents to use guides

   Assign the **Agent Applications - Custom views** permission to agents. This permission lets agents use step-by-step guides in the agent workspace.  
![The Security profile permissions page, the agent applications section, the custom views permission.](https://docs.aws.amazon.com/connect/latest/adminguide/images/sec-perms-agent-view-sq.png)

1. Increase your service quota for concurrent active chats per instance

   Every step-by-step guide runs as a chat contact. Increase your **concurrent active chats per instance** quota by the number of step-by-step guides you expect to run at the same time.

   For more information about quotas, see [Connect Customer quotas](amazon-connect-service-limits.md#connect-quotas). 
**Note**  
A disconnect flow runs as its own contact. If you set both `DefaultFlowID` and `DisconnectFlowID`, each step-by-step guide counts as two active contacts.