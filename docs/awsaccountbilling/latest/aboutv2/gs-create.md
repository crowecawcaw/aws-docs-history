

# Connect AWS FinOps Agent to Data Hub

To use Data Hub with AWS FinOps Agent, you create a dataset and then connect an agent to the dataset. Creating an agent does not create a dataset.

1. **Create a dataset.** Create the dataset on the Data Hub page in the AWS Billing and Cost Management console, or in the AWS FinOps Agent wizard when you create an agent. For an organization-wide agent, create the dataset in the management account. For a single-account agent, create the dataset in the account that runs the agent. For steps, see [Create a dataset on the Data Hub page](gs-dataset.md).

1. **Connect an agent to the dataset.** Turn on the Data Hub setting for the agent. When you create an agent, select **Use Data Hub for this agent** in the wizard. For an agent you already have, choose **Connect** on the agent's Data Hub tab.

Follow the setup that matches the agent you run:
+ For an organization-wide agent, first [Set up the management account for organization-wide agents](setup-trusted.md), then [Create an organization-wide agent](gs-da.md) in the delegated administrator account.
+ For a single-account agent, follow [Single-account setup](gs-single.md).
+ For an agent you already have, follow [Connect an existing agent](gs-existing.md).

**Topics**
+ [Set up the management account for organization-wide agents](setup-trusted.md)
+ [Create an organization-wide agent](gs-da.md)
+ [Single-account setup](gs-single.md)
+ [Connect an existing agent](gs-existing.md)
+ [Create a dataset on the Data Hub page](gs-dataset.md)