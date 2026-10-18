

# Create Jira issues for findings
<a name="export-findings-to-issue-tracker"></a>

AWS Security Agent provides the ability to create Jira issues directly from security findings, so your team can track and resolve them in Jira. You can create issues for findings from a penetration test or a code review. For information about connecting Jira, see [Connect AWS Security Agent to Jira](connect-jira.md).

When you create an issue, AWS Security Agent creates one Jira issue for each finding you select, in the project you choose. The issue includes the finding’s details, such as its description and suggested fix.

Before you begin, make sure you have connected a Jira project to an Agent Space, and that the project allows the **Task** issue type.

**Issue type requirement**  
The Jira project you choose must allow the **Task** issue type.

## Creating issues for findings
<a name="_creating_issues_for_findings"></a>

Create Jira issues from your findings so your team can track and remediate security and code review issues directly in Jira. This procedure assumes you have already connected a Jira project to an Agent Space.

1. Sign in to the AWS Security Agent web application.

1. Open the penetration test or code review run that contains the findings.

1. On the **Findings** tab, choose **Multiselect Findings**.

1. In the findings list, select the check box next to each finding you want to create an issue for.

1. On the **Findings** tab, choose **Create Issues**.

1. Select the Jira project to create the issues in, then confirm.

   AWS Security Agent creates a Jira issue for each selected finding. This might take a few moments if you selected multiple findings. After an issue is created, the finding shows an **Issue** section with the issue details.

## Opening a linked issue in Jira
<a name="_opening_a_linked_issue_in_jira"></a>

If a finding has an associated Jira issue, you can open it to view or update its status. To open a linked issue in Jira:

1. Open the finding.

1. Expand the **Issue** section.

1. Choose the **Issue key** to open the issue in Jira.

## Unlinking an issue from a finding
<a name="_unlinking_an_issue_from_a_finding"></a>

If you no longer want a finding linked to its Jira issue, you can remove the link. Unlinking removes the link only; it does not delete the issue in Jira. To unlink an issue from a finding:

1. On the **Findings** tab, choose **Multiselect Findings**.

1. On the **Findings** tab, select the findings you want to unlink.

1. Choose **Unlink Issues**, then confirm.