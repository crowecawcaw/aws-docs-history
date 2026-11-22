

# Create a dataset on the Data Hub page

You can create a dataset on the Data Hub page at any time, whether or not an agent exists. To create a dataset, you need the Data Hub actions for the person who creates it, described in [Identity-based policy examples](security-iam.md#sec-policies).

1. Open the AWS Billing and Cost Management console in the account that will hold the dataset, and choose **Data Hub** in the navigation pane.

1. Choose **Create dataset**.

1. For **Name**, enter a name of 1 to 64 characters, using lowercase letters, digits, and underscores and starting with a letter or a digit. AWS FinOps Agent reads the name when it lists datasets.

1. For **Schema name**, choose `cost_usage`.

1. For **Tags**, add a key and an optional value if you want them. A dataset carries up to 50 tags.

1. Choose **Create dataset**, then watch the status of the new row reach **Active**.

**Important**  
Provisioning takes up to 24 hours, and **Status** reads **Active** when agents can query the dataset.

When provisioning does not finish, **Status** reads **Failed** and the status reason on the dataset detail page states why. A dataset that has not finished provisioning still counts against the quota of one dataset per account, so read the status reason, delete the dataset, and create it again. If the same reason repeats, contact AWS Support.

You can change the name and the tags after creation. Choose **Edit** on the dataset detail page. A change to the name or the tags leaves the provisioned data in place. The schema, the coverage, and the account are fixed at creation, so changing any of those means deleting the dataset and creating a new one, which loads the history again.

On the **Data Hub** page, choose the dataset name to open its detail page, which reports the following.


| Field | What it reports | 
| --- | --- | 
| Status | The dataset status, which reads Provisioning, Active, or Failed, with the status reason beside it when provisioning did not complete. An Active dataset returns to Provisioning when AWS finds a problem with the data, and queries are rejected until it is Active again. | 
| Schema name | cost\_usage. | 
| Data | The period the dataset covers, which is 13 months of resource-level cost and usage in the CUR 2.0 schema. | 
| Last refreshed | When the data behind an answer was last updated. | 
| Tags | The tags on the dataset, with Manage tags to change them. | 

**Note**  
The dataset detail page does not list the agents that read the dataset. In the delegated administrator case those agents live in another account, which the management account cannot enumerate, so the page reports the dataset and leaves consumers out.