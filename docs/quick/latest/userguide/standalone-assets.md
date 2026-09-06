

# Managing assets in a Amazon Quick Free or Plus account
<a name="standalone-assets"></a>

In a Amazon Quick Free or Plus account, assets represent the resources created and used within your account – including chat agents, spaces, automations, and other AI-powered tools. The Assets page in the Manage Account interface lets administrators view, search, filter, and manage all assets across the account.

**Note**  
This section applies to Amazon Quick Free and Plus accounts created at [aws.com/quick](https://aws.com/quick). For information about managing resources in AWS Console–based accounts, see [Administering Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/qsysadmin.html).

**Topics**
+ [Navigating to asset management](#standalone-assets-navigate)
+ [Viewing assets by name](#standalone-assets-by-name)
+ [Viewing assets by user](#standalone-assets-by-user)
+ [Using bulk actions](#standalone-assets-bulk)
+ [Built-in assets](#standalone-assets-built-in)
+ [Managing individual assets](#standalone-assets-individual)

## Navigating to asset management
<a name="standalone-assets-navigate"></a>

**To access the Assets page**

1. Sign in to Amazon Quick at [aws.com/quick](https://aws.com/quick).

1. From the navigation panel, choose your username.

1. Choose **Manage account**.

1. In the left navigation, choose **Assets**.

The Assets page opens, displaying all resources in your account.

## Viewing assets by name
<a name="standalone-assets-by-name"></a>

The default view on the Assets page is **By asset name**, which lists all assets in a single table.

**Topics**
+ [Assets table columns](#standalone-assets-table-columns)
+ [Sorting and searching](#standalone-assets-sort-search)

### Assets table columns
<a name="standalone-assets-table-columns"></a>
+ **Name** – The display name of the asset (for example, *My Assistant* or *RFP Response Generator*).
+ **Type** – The asset type (for example, *Chat agent*, *Space*, or *Automation*).

Each row includes:
+ A **checkbox** for selecting the asset (used with bulk actions).
+ A **More options** menu for asset-specific actions.

### Sorting and searching
<a name="standalone-assets-sort-search"></a>
+ Choose a column header to sort the table by that column.
+ Use the **Search by asset name** field to filter the list by asset name.
+ Use the **All types** dropdown to filter by a specific asset type.

## Viewing assets by user
<a name="standalone-assets-by-user"></a>

Choose the **By user** tab to view assets grouped by the user who created them.

In this view:
+ Use the **Search by user name** combobox to find a specific user and view their assets.
+ Use the **All types** dropdown to filter results by asset type.

This view is useful for understanding how assets are distributed across team members and for auditing resource ownership.

## Using bulk actions
<a name="standalone-assets-bulk"></a>

You can perform actions on multiple assets at once using the bulk action feature.

**To use bulk actions**

1. On the Assets page, select the checkboxes next to the assets you want to act on. To select all assets, choose the **Select all** checkbox in the table header.

   After selecting one or more assets, the **Bulk action** button becomes active.

1. Choose **Bulk action** and select the desired action from the dropdown menu.

**Note**  
The **Bulk action** button is disabled until at least one asset is selected.

## Built-in assets
<a name="standalone-assets-built-in"></a>

Every new Amazon Quick account includes a set of built-in assets that provide ready-to-use AI-powered tools for common business tasks. These assets are available immediately after account creation and do not count against any resource limits.


| Asset name | Description | 
| --- | --- | 
| My Assistant | The default chat agent for your account. Provides general-purpose AI assistance for questions, analysis, and document creation. | 
| Whiteboard Notes Generator | Generates structured notes from whiteboard images or meeting discussions. | 
| Flows Idea Generator | Suggests automation workflow ideas based on your described business processes. | 
| 5-Why Root Cause Analysis | Guides you through a structured root cause analysis using the 5-Why methodology. | 
| Marketing Video Analyzer | Analyzes marketing video content and provides insights on messaging, audience, and effectiveness. | 
| Social Media Content Creator | Creates social media posts, captions, and content plans tailored to your brand and goals. | 
| Job Description Generator | Drafts professional job descriptions based on role requirements and company context. | 
| Product Launch Email Generator | Creates email campaigns for product launches, including subject lines and body content. | 
| Customer Interest Optimizer | Analyzes customer data to identify interest patterns and suggest optimization strategies. | 
| Flows Prompt Helper | Assists with writing effective prompts for Amazon Quick automations and flows. | 
| RFP Response Generator | Drafts responses to Requests for Proposal (RFPs) based on your organization's capabilities and the RFP requirements. | 

**Tip**  
Built-in assets serve as starting points. You can customize these assets or create new ones tailored to your organization's specific needs. For more information about creating custom chat agents, see [Create and deploy AI assistants using Amazon Quick chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html).

## Managing individual assets
<a name="standalone-assets-individual"></a>

To manage a specific asset, choose the **More options** menu in the asset's row. The available actions depend on the asset type and may include options such as viewing details, editing, sharing, or deleting the asset.