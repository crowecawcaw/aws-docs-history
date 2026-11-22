

# Set up the management account for organization-wide agents

In the management account, you enable organization-wide access, choose where your agents run, and create the dataset. To create a dataset, you need the Data Hub actions for the person who creates it, described in [Identity-based policy examples](security-iam.md#sec-policies). Permission to register a delegated administrator does not include the Data Hub actions.

Trusted access for AWS FinOps Agent is what lets an agent in one account read a dataset another account holds, by authorizing the service to assume `AWSServiceRoleForFinOpsAgent` in the account that holds the dataset. Data Hub has no trusted access setting of its own.

1. In the management account, open AWS FinOps Agent and choose **Set up organization-wide access**.

1. On **Step 1, Enable organization-wide access**, choose **Enable organization-wide access**. Enabling organization-wide access makes AWS FinOps Agent a trusted service in AWS Organizations and deploys a read-only role to your accounts.

1. On **Step 2, Choose a delegated administrator**, under **Choose where the agent will run**, choose **Delegated administrator account** and select the member account that runs your organization-wide agents. AWS recommends this option. Choose **No delegated administrator account** to run the agents in the management account instead. Then choose **Next**.

1. On **Step 3, Set up Billing and Cost Management tools**, in the **Billing and Cost Management Data Hub** card, where **Dataset status** shows **No dataset**, choose **Create dataset**. The Data Hub panel opens over the step.

1. In the panel, enter a **Name**, choose `cost_usage` for **Schema name**, and add tags if you want them. For the field rules, see [Create a dataset on the Data Hub page](gs-dataset.md). Then choose **Create dataset**.

1. Close the panel to return to **Step 3**. **Dataset status** on the Data Hub card now shows the status of the dataset: **Provisioning**, **Active**, or **Failed**. Provisioning takes up to 24 hours. You do not need to wait for the dataset to be **Active** to finish setup.

1. Choose **Next**. On **Step 4, Review and finish**, check the trusted access, the delegated administrator, and the dataset, then choose **Finish setup**. The dataset keeps provisioning after you finish setup, and the agent answers at the individual resource level once the dataset is **Active**.