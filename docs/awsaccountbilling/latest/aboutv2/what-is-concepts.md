

# Concepts


| Term | Description | 
| --- | --- | 
| Dataset | Your cost and usage data, which AWS provisions and keeps current. A dataset is an AWS resource with its own Amazon Resource Name (ARN), so you can tag it, scope access to it, and delete it. You create a dataset on the Data Hub page in the AWS Billing and Cost Management console, or in the AWS FinOps Agent wizard when you create an agent. You then connect the dataset to an agent in AWS FinOps Agent, and the agent queries the dataset to answer questions that need an individual resource, hourly detail, or a field such as a resource identifier or a cost allocation tag. | 
| Dataset schema | The set of columns in a dataset. Public preview offers one schema, cost\_usage, which follows the [CUR 2.0 data dictionary](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2.html) in the AWS Data Exports User Guide. | 
| Billing view | The AWS Billing and Cost Management resource that decides which accounts a set of cost and usage data covers. A dataset covers the accounts in the primary billing view of the account that creates it. | 
| Management account | The account that owns your organization's billing and structure in AWS Organizations. During public preview the management account is the only account that can provision a dataset covering an entire organization. | 
| Delegated administrator account | A member account you register to run your organization-wide agents in AWS FinOps Agent. Those agents query Data Hub across your organization, so no one on your FinOps team needs management-account privileges. | 