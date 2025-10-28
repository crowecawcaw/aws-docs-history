# Viewing generated findings in GuardDuty

console

When GuardDuty detects an activity that matches the pattern of a security issue, GuardDuty generates a
finding. This finding is associated with a resource type that may have been
compromised during this activity. You can view the details associated with each finding that GuardDuty
generates.

If you are using a GuardDuty administrator account, you can view the generated findings on behalf of the
member accounts. However, a member account can view the findings generated in their own
account. A member account can't view the findings generated for other member
accounts.

###### Steps to view findings in GuardDuty console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the left navigation pane, choose **Findings**.

GuardDuty displays the findings in a tabular format. By default, this table
is sorted in decreasing order based on the **Last seen** column value, displaying
the most recent findings at the top.

Findings with a sword icon (
![Sword icon that represents attack sequence finding in GuardDuty console.](images/attack-sequences-icon.PNG)
) represent an attack sequence finding. 3. To view details associated with a finding, select its **Title**.
This will open the finding details side panel. For an attack sequence finding, this side
panel includes a _summarized version_ of the attack sequence, and
to expand this view, choose **View details**.

For information about the fields listed in this side panel,
see [Finding details](guardduty_findings-summary.md "guardduty_findings-summary.md"). 4. ###### (Optional) to download finding JSON

    1. Select the finding, and
     then choose the **Actions** menu.
    2. On the **Actions** menu, choose **View and export JSON**.
    3. On the **Findings JSON** window, choose **Download**.


    ###### Note

    In some cases, GuardDuty becomes aware that certain findings are false
     positives after they have been generated. GuardDuty provides a
     **Confidence** field in the finding's JSON, and sets
     its value to zero. This way GuardDuty lets you know that you can safely ignore
     such findings.

    Findings without the **Confidence** field are
     not considered false positives.

## Navigating Findings page

This section provides key information about various elements
on the **Findings** page. This will help you analyze the generated findings
for threat analysis and response.

The following list explains **Findings** page elements that will help you better understand
the generated findings:

- **Threat type**:

Threat type includes individual GuardDuty findings and attack sequence findings. By default,
the page displays **All findings**.

To filter the findings table view, on the **Threat type** menu, choose
one of the options – **Attack sequence findings only** or
**Individual findings only**.

- **Resource and Count columns**:

The **Resource**
column in the findings table shows the name of the potentially compromised AWS resource. For
an attack sequence finding, this column shows the number of potentially compromised AWS resources.
To view the resource names, select the _number_ under the **Resource**
column.

The **Count** column indicates the number of times GuardDuty observes
a specific finding. When GuardDuty detects that an activity that matches
a previously identified security issue, it increments the count for that specific finding. For
an attack sequence finding, this column value indicates the total number of signals and findings involved
in the generation of the finding.

- **Sorting findings by table columns**:

If there is an _arrow_ next
to a column header, then you can sort the findings table based on the column.
Select the column header to sort the findings in either increasing or decreasing order of the value in that
column.

- **Filtering findings**:

Based on specific property attributes, such as `Account ID` and
`Resource type`, you can further filter the findings table. For information
about types of filters you can use, see
[Filtering GuardDuty findings](guardduty_filter-findings.md "guardduty_filter-findings.md").

- **Status and Saved rules**:

The **Status** menu includes two values – **Current** and
**Archived**. The default view is **Current**
findings in the table.

When you no longer want GuardDuty to generate a finding that matches a specific criteria, you
can suppress that finding. GuardDuty archives that finding. When GuardDuty detects this finding again, you will
not be notified of this observation. To specifically view archived findings, on the
**Status** menu, choose **Archived**.

**Saved rules** is a feature that helps you automatically filter and take
actions on findings that match a specified criteria. Actions may include archiving findings
or suppressing them from future notifications.

For
more information, see [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").
