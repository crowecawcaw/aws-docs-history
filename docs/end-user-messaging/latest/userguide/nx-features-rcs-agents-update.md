

# Update an RCS agent
<a name="nx-features-rcs-agents-update"></a>

Update the settings on an existing AWS RCS Agent, including whether deletion protection is enabled.

**To update an RCS agent using the AWS CLI**
+ At the command line, enter the following command, replacing {{rcs-agentId}} with the ID of the agent to update.

  ```
  $ aws pinpoint-sms-voice-v2 update-rcs-agent \
  > --rcs-agent-id {{rcs-agentId}} \
  > --deletion-protection-enabled
  ```

Because AWS End User Messaging does not provide a delete operation for RCS agents, deletion protection is the control you use to govern whether an agent can be removed.