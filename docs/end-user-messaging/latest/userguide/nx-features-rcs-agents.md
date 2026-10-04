

# RCS Agents
<a name="nx-features-rcs-agents"></a>

An AWS RCS Agent is the top-level resource in AWS End User Messaging that represents your brand for RCS messaging. It is the unified resource that binds together your testing agent and your country launch agents (RCS for Business IDs). You define keywords and two-way messaging configuration on the AWS RCS Agent, while brand assets are defined on each registration (the testing agent or a country launch agent).

One AWS RCS Agent maps to one testing agent plus multiple country launch agents, one for each country where you launch production RCS. When you create an AWS RCS Agent in the console, the workflow guides you to create a testing agent, and the testing agent's brand configuration is used to pre-populate country launch registration forms.

The AWS RCS Agent follows this lifecycle:

1. **Create** the AWS RCS Agent.

1. **Add a testing agent** by submitting a testing registration and associating it with the agent.

1. **Test** your RCS messaging with registered test devices. No carrier approval is required for testing.

1. **Submit a country launch** registration for each country where you want to send production RCS messages.

1. **Partially approved**: at least one carrier has approved your agent, and you can start sending to recipients on approved carriers.

1. **Fully approved**: all carriers in the country have approved your agent, giving you full reach in that country.

**Note**  
AWS End User Messaging does not provide a delete operation for RCS agents. Use deletion protection to control whether an agent can be removed, which you set when you create the agent and can change with `update-rcs-agent`.

**Topics**
+ [Create an RCS agent](nx-features-rcs-agents-create.md)
+ [View RCS agents](nx-features-rcs-agents-view.md)
+ [Update an RCS agent](nx-features-rcs-agents-update.md)
+ [Associate a registration with an agent](nx-features-rcs-agents-associate.md)