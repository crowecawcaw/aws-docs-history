

# Turn the Data Hub setting off for one agent

The Data Hub setting is per agent, and the account that runs the agent owns it. Disconnect Data Hub from an agent when you want that agent to answer at the service and account level while other agents in your organization keep answering at the individual resource level. The Data Hub setting is the only per-agent control over how much detail an agent returns.

1. Open AWS FinOps Agent in the account that runs the agent, and open the agent.

1. Open the **Billing and Cost Management Data Hub** tab.

1. Choose **Disconnect**.

Disconnecting deletes that agent's Data Hub connection, leaves every dataset in place, and changes no other agent. To connect the agent again, see [Connect an existing agent](gs-existing.md).