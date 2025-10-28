# View the IAM Access Analyzer findings

dashboard

AWS Identity and Access Management Access Analyzer organizes external, internal, and unused access findings into a visual
summary dashboard. The dashboard helps you gain visibility into the effective use of
permissions at scale and identify accounts and AWS resources that need attention. You can
use the dashboard to review findings by AWS organization, account, and finding
type.

For external and internal access findings:

- The dashboard highlights the split between public access findings, external access
  findings, and internal access findings.
- The dashboard provides a breakdown of findings by resource type.
  For unused access findings:

- The dashboard highlights the AWS accounts with the most unused access
  findings.
- The dashboard provides a breakdown of findings by type.
  After you create any type of access analyzer, IAM Access Analyzer automatically adds new
  findings to the relevant dashboard. This allows you to identify and prioritize the areas
  with the most security concerns.

The summary dashboards give you a high-level view of the access issues detected by
IAM Access Analyzer across your AWS environment. You can then drill down into the individual
findings to investigate further and take appropriate actions to resolve them.

## Viewing the summary

dashboard for external and internal access analyzers

###### Note

After you create or update an analyzer, it can take time for the summary
dashboard to reflect updates to findings.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Access Analyzer**. The **Summary**
   window is displayed.
3. Choose **Select analyzers**.
4. In the **Select analyzers** window, choose
   **Organization** or **Account** for the
   **Zone of trust**.

###### Note

Only the AWS Organizations management account or delegated administrator can choose
**Organization** as the zone of trust. 5. Choose external and internal access analyzers from the **Resource
access analyzers** dropdown.

###### Note

You can select a maximum of one external access analyzer and a maximum of
one internal access analyzer. 6. Choose **Update**. A summary of the findings for the selected
external and internal access analyzers is displayed in the **Resource
access findings** section.

![Resource findings access analyzer dashboard.](images/access-analyzer-dashboard-external-internal-new.png)

In the preceding image, the resource findings dashboard is visible from within the
**Summary** page.

1. The **Active findings** section includes the number of active
   findings for public access, the number of active findings that provide access
   outside of the account or organization, and the number of active internal access
   findings for the selected analyzers. Choose a number to list all of the active
   findings of each type.
2. The **Resource types** section includes a breakdown of the
   resource types with active findings for the selected analyzers. Choose
   **View all active findings** for a complete list of active
   findings for the selected analyzers.
3. The **Key resources** section includes a summary of the key
   resources with active findings. This information helps you prioritize findings
   for your business-critical resources. Choose **View all active
   findings** for a complete list of active findings for the selected
   analyzers.

## Viewing the summary dashboard for

unused access analyzers

###### Note

After you create or update an analyzer, based on the amount of users and
roles, it can take time for the summary dashboard to reflect updates to
findings.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Access Analyzer**. The **Access Analyzer
   Summary** window is displayed.
3. Choose **Select analyzers**.
4. In the **Select analyzers** window, choose
   **Organization** or **Account** for the
   **Zone of trust**.

###### Note

Only the AWS Organizations management account or delegated administrator can choose
**Organization** as the zone of trust. 5. Choose an unused access analyzer from the **Unused access
analyzers** dropdown. 6. Choose **Update summary**. A summary of the findings for the
selected unused access analyzer is displayed in the **Unused access
findings** section.

![Unused access analyzer dashboard.](images/access-analyzer-dashboard-unused-new.png)

In the preceding image, the unused access findings dashboard is visible from within
the **Summary** page.

1. The **Active findings** section includes the number of active
   findings for unused roles, unused credentials, and unused permissions in your
   account or organization. **Unused credentials** include both
   unused access key and unused password findings. **Unused
   permissions** include both users and roles with unused permissions.
   Choose a number to list all of the active findings of each type.
2. The **Findings overview** section includes a breakdown of the
   type of active findings. Choose **View all active findings**
   for a complete list of active findings for the analyzer's account or
   organization.
3. The **Finding status** section includes a breakdown of the
   status of findings (**Active**, **Archived**,
   and **Resolved**) for your account or organization. You can
   select the findings statuses to display in the **Filter displayed
   data** dropdown.
4. The **Accounts with the most findings for unused access**
   section is only displayed if the selected accounts of your unused access
   analyzer is at the organization level. It includes a breakdown of the accounts
   in your organization with the most active findings. This is not an exhaustive
   list of every account in your organization. Your analyzer might have active
   findings for other accounts not listed in this section.
