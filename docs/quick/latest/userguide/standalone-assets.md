# Managing assets in a Amazon Quick Free or Plus account

In a Amazon Quick Free or Plus account, assets represent the resources created and used
within your account – including chat agents, spaces, automations, and other
AI-powered tools. The Assets page in the Manage Account interface lets administrators
view, search, filter, and manage all assets across the account.

###### Note

This section applies to Amazon Quick Free and Plus accounts created at [aws.com/quick](https://aws.com/quick "https://aws.com/quick"). For information about managing
resources in AWS Console–based accounts, see [Administering Amazon Quick](../../../quicksuite/latest/userguide/qsysadmin.md "../../../quicksuite/latest/userguide/qsysadmin.md").

###### Topics

- [Navigating to asset management](#standalone-assets-navigate "#standalone-assets-navigate")
- [Viewing assets by name](#standalone-assets-by-name "#standalone-assets-by-name")
- [Viewing assets by user](#standalone-assets-by-user "#standalone-assets-by-user")
- [Using bulk actions](#standalone-assets-bulk "#standalone-assets-bulk")
- [Built-in assets](#standalone-assets-built-in "#standalone-assets-built-in")
- [Managing individual assets](#standalone-assets-individual "#standalone-assets-individual")

## Navigating to asset management

###### To access the Assets page

1. Sign in to Amazon Quick at [aws.com/quick](https://aws.com/quick "https://aws.com/quick").
2. From the navigation panel, choose your
   username.
3. Choose **Manage account**.
4. In the left navigation, choose **Assets**.

The Assets page opens, displaying all resources in your account.

## Viewing assets by name

The default view on the Assets page is **By asset name**, which
lists all assets in a single table.

###### Topics

- [Assets table columns](#standalone-assets-table-columns "#standalone-assets-table-columns")
- [Sorting and searching](#standalone-assets-sort-search "#standalone-assets-sort-search")

### Assets table columns

- **Name** – The display name of the
  asset (for example, _My Assistant_ or
  _RFP Response Generator_).
- **Type** – The asset type (for
  example, _Chat agent_, _Space_, or _Automation_).

Each row includes:

- A **checkbox** for selecting the asset
  (used with bulk actions).
- A **More options** menu for asset-specific
  actions.

### Sorting and searching

- Choose a column header to sort the table by that column.
- Use the **Search by asset name** field to filter the
  list by asset name.
- Use the **All types** dropdown to filter by a specific
  asset type.

## Viewing assets by user

Choose the **By user** tab to view assets grouped by the user who
created them.

In this view:

- Use the **Search by user name** combobox to find a specific
  user and view their assets.
- Use the **All types** dropdown to filter results by asset
  type.

This view is useful for understanding how assets are distributed across team
members and for auditing resource ownership.

## Using bulk actions

You can perform actions on multiple assets at once using the bulk action
feature.

###### To use bulk actions

1. On the Assets page, select the checkboxes next to the assets you want to
   act on. To select all assets, choose the **Select all**
   checkbox in the table header.

After selecting one or more assets, the **Bulk action**
button becomes active. 2. Choose **Bulk action** and select the desired action from
the dropdown menu.

###### Note

The **Bulk action** button is disabled until at least one
asset is selected.

## Built-in assets

Every new Amazon Quick account includes a set of built-in assets that provide
ready-to-use AI-powered tools for common business tasks. These assets are available
immediately after account creation and do not count against any resource limits.

| Asset name                            | Description                                                                                                                           |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **My Assistant**                      | The default chat agent for your account. Provides<br>general-purpose AI assistance for questions, analysis, and document<br>creation. |
| **Whiteboard Notes<br>Generator**     | Generates structured notes from whiteboard images or meeting<br>discussions.                                                          |
| **Flows Idea<br>Generator**           | Suggests automation workflow ideas based on your described<br>business processes.                                                     |
| **5-Why Root Cause<br>Analysis**      | Guides you through a structured root cause analysis using<br>the 5-Why methodology.                                                   |
| **Marketing Video<br>Analyzer**       | Analyzes marketing video content and provides insights on<br>messaging, audience, and effectiveness.                                  |
| **Social Media Content<br>Creator**   | Creates social media posts, captions, and content plans<br>tailored to your brand and goals.                                          |
| **Job Description<br>Generator**      | Drafts professional job descriptions based on role<br>requirements and company context.                                               |
| **Product Launch Email<br>Generator** | Creates email campaigns for product launches, including<br>subject lines and body content.                                            |
| **Customer Interest<br>Optimizer**    | Analyzes customer data to identify interest patterns and<br>suggest optimization strategies.                                          |
| **Flows Prompt<br>Helper**            | Assists with writing effective prompts for Amazon Quick<br>automations and flows.                                                     |
| **RFP Response<br>Generator**         | Drafts responses to Requests for Proposal (RFPs) based on<br>your organization's capabilities and the RFP<br>requirements.            |

###### Tip

Built-in assets serve as starting points. You can customize these assets or
create new ones tailored to your organization's specific needs. For more
information about creating custom chat agents, see [Create and deploy AI assistants using Amazon Quick chat
agents](../../../quicksuite/latest/userguide/working-with-agents.md "../../../quicksuite/latest/userguide/working-with-agents.md").

## Managing individual assets

To manage a specific asset, choose the **More options** menu in
the asset's row. The available actions depend on the asset type and may include
options such as viewing details, editing, sharing, or deleting the asset.
