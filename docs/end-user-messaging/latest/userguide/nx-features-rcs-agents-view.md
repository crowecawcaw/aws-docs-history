

# View RCS agents
<a name="nx-features-rcs-agents-view"></a>

View the RCS agents in your account and check their status, including the status of the testing agent.

**To view RCS agents using the AWS CLI**

1. At the command line, enter the following command.

   ```
   $ aws pinpoint-sms-voice-v2 describe-rcs-agents
   ```

1. To check a specific agent and its testing agent status, filter the response by agent ID.

   ```
   $ aws pinpoint-sms-voice-v2 describe-rcs-agents \
   > --query "RcsAgents[?RcsAgentId=='{{rcs-agentId}}'].{Status:Status,TestingStatus:TestingAgent.Status}"
   ```

The testing agent status progresses from `PENDING` to `ACTIVE`. Wait until the testing agent status shows `ACTIVE` before you add a test device or send a test message.