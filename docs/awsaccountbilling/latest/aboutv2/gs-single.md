

# Single-account setup

Use this setup to run an agent in the management account or in a member account. In the wizard, you create the dataset on the Data Hub step, then finish creating the agent. A dataset created in a member account covers that account. A dataset created in the management account covers the whole organization. To create a dataset, you need the Data Hub actions for the person who creates it, described in [Identity-based policy examples](security-iam.md#sec-policies).

1. Open AWS FinOps Agent in that account and choose **Create agent**.

1. On **Step 4, Set up Billing and Cost Management tools**, if **Dataset status** shows **No dataset**, choose **Create dataset**. In the panel that opens, enter a **Name**, choose `cost_usage` for **Schema name**, and add tags if you want them. For the field rules, see [Create a dataset on the Data Hub page](gs-dataset.md).

1. Confirm that **Use Data Hub for this agent** is selected. The checkbox is unavailable until the account has a dataset, and the checkbox selects itself once the dataset is created.

1. Choose **Next**, finish the remaining steps, and on the **Review and create** step, choose **Create agent**.

When a dataset already exists in the account, **Dataset status** shows the status of that dataset, and **Create dataset** does not appear.