

AWS FinOps Agent is in preview release and is subject to change.

# Getting started with AWS FinOps Agent
<a name="getting-started"></a>

To start using AWS FinOps Agent, sign in to the AWS Management Console, switch to the US East (N. Virginia) (us-east-1) Region, and open the AWS FinOps Agent Console page. Create your first agent with the creation wizard. The wizard creates the IAM roles the agent needs and attaches the required policies for you, so you can get started without configuring IAM manually. You can optionally connect Jira and Slack during creation so the agent can create tickets and post messages.

After the agent is created, open its web application to upload your initial context (an account-to-owner mapping and any organization-specific instructions such as known exceptions, prioritization rules, and review cadence), run your first query, and set up your first event-triggered cost anomaly detection automation. The agent acts only on the data sources and integrations you connect during setup.

If your IAM administrator manages permissions centrally, or if you want to author the agent's roles and policies yourself, see the [AWS FinOps Agent IAM setup guide](setting-up.md) for the full list of IAM policies, roles, and trust relationships.