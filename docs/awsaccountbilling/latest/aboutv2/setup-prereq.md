

# Prerequisites

Before you set up Data Hub, make sure you have the Data Hub permissions and know which account to create the dataset in.

**Permissions.** Two identities need Data Hub actions: the person who creates datasets and the agent role that reads them. A member account user can create a dataset for their own account with these permissions, unless a service control policy denies `bcm-data-hub:CreateDataset`. For the actions each one needs, see [Identity-based policy examples](security-iam.md#sec-policies).

**Organization-wide agent.** Agents run in a member account you register as the delegated administrator, so users don't need access to the management account. Create the dataset in the management account, either during management account setup or on the Data Hub page. Then create an organization-wide agent in the delegated administrator account with the Data Hub setting turned on, and the agent reads that dataset, which covers every account in your organization. For more information, see [Set up the management account for organization-wide agents](setup-trusted.md), [Create a dataset on the Data Hub page](gs-dataset.md), and [Create an organization-wide agent](gs-da.md).

**Single-account agent.** Alternatively, you can run a single-account agent in any member account or in the management account. A single-account agent reads the dataset in its own account. A dataset created in a member account covers that account alone, and a dataset created in the management account covers the whole organization. Create the dataset and the agent together in the AWS FinOps Agent wizard, or create the dataset on the Data Hub page and connect an existing agent to it. For more information, see [Single-account setup](gs-single.md), [Create a dataset on the Data Hub page](gs-dataset.md), and [Connect an existing agent](gs-existing.md).