# Step 4: Deploy the agent with an alias

After configuring your agent, you need to deploy it with an alias to make it available
for use. In this procedure, you'll prepare your agent for deployment by creating an
alias and version of your agent. The alias points to the version, allowing you to invoke
your agent through a stable endpoint while maintaining the ability to update the
underlying implementation.

For more information, see [Deploy and use an Amazon Bedrock agent in your application](agents-deploy.md "agents-deploy.md").

###### Deploy the agent with an alias

1. In the Amazon Bedrock console, open the agent that you created in [Step 2: Create an Amazon Bedrock agent](agent-tutorial-step2.md "agent-tutorial-step2.md")
2. Choose **Create Alias**.
3. For **Alias name**, enter a name for the alias. For example
   `DateTimeAliasAgentAlias`.
4. (Optional) For **Description**, enter a description.
5. For **Associate a version**, select **Create a new version and associate it to this alias**.
6. Choose **Create alias**.
7. Test the alias by following the instructions at [Step 3: Test the agent](agent-tutorial-step3.md "agent-tutorial-step3.md"). For
   step 6, choose the alias that you just created.
