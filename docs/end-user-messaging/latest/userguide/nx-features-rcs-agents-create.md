

# Create an RCS agent
<a name="nx-features-rcs-agents-create"></a>

Create an AWS RCS Agent, the top-level resource that represents your brand for RCS messaging. After you create the agent, you submit a testing registration and associate it with the agent before you can send test messages. For the full setup walkthrough, see [How to get set up](nx-rcs-get-set-up.md).

**To create an RCS agent using the AWS CLI**

1. At the command line, enter the following command. The `--deletion-protection-enabled` option prevents the agent from being removed until you disable it.

   ```
   $ aws pinpoint-sms-voice-v2 create-rcs-agent \
   > --deletion-protection-enabled
   ```

1. The response includes the RCS agent ID and a status of `CREATED`. Save the agent ID, because you use it when you associate a registration and when you send messages.

After the agent is created, submit a testing registration and associate it with the agent. For the association step, see [Associate a registration with an agent](nx-features-rcs-agents-associate.md).