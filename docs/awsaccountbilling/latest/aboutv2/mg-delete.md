

# Delete a dataset

**Warning**  
Deleting the dataset stops every agent that reads it from answering at the individual resource level. Creating the dataset again provisions the history from the start and takes up to 24 hours.

1. On the **Data Hub** page, choose the dataset name.

1. Choose **Delete**.

1. To confirm, type `delete` in the text field, then choose **Delete**.

When you delete a dataset, the confirmation does not list the agents that use it. If your agents run in a delegated administrator account, you cannot see those agents from the management account. Ask your FinOps team who uses AWS FinOps Agent before you delete.

Without the dataset, agents keep answering cost, anomaly, and optimization questions from AWS Cost Explorer, Cost Optimization Hub, and their other AWS APIs, but without detail at the individual resource level. Each agent's Data Hub preference and its connection stay in place, so the delegated administrator account needs no change when a dataset appears again.

**Note**  
Deletion happens only on the Data Hub page in the AWS Billing and Cost Management console, in the account that holds the dataset. No AWS FinOps Agent surface deletes a dataset. Disconnecting Data Hub on the agent's **Billing and Cost Management Data Hub** tab deletes that agent's Data Hub connection, stops that one agent from answering at the individual resource level, and leaves the dataset in place. See [Connect AWS FinOps Agent to Data Hub](gs-create.md).

AWS does not notify the teams that use agents in other accounts when you delete a dataset. Those teams see that the dataset is gone on the agent's **Billing and Cost Management Data Hub** tab, or notice that answers return less detail. Tell those teams before you delete the dataset.