

# Viewing recommended actions

The Recommended actions page displays a summary of your recommended actions and a table with details for individual actions. Recommended actions help you optimize your resources for performance and cost savings.

**Note**  
As the management account or a delegated administrator, you can view recommended actions for member accounts that have Automation enabled. You can apply them only for member accounts with the organization rule mode **Any allowed**. For member accounts with **None allowed**, only the account itself can apply them. For more information, see [Enabling Automation for your organization](automation-org.md).

**To access recommended actions**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Recommended actions** under the **Automation ** section.

1. You can perform the following actions on the **Recommended actions** page:

   - View recommended actions.

   - Filter recommended actions by one or more properties such as AWS Region, Resource Tag key-values, or account. If you're signed in to the management account or a delegated administrator, you can filter by organizational unit (OU). Choose one or more OUs in **Choose organizational units**. The results include the accounts in each OU and in its child OUs. If you also filter by account, the results include only the accounts that are in the chosen OUs.

   - Select the recommended actions that you want to apply.

   - View a summary of the estimated monthly savings for your selected recommended actions and the total opportunity available based on your filters.

   - Create automation rule from your selected filters. This pre-fills the rule creation form with your selected filters in the recommended actions table.