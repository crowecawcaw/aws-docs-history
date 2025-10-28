# Reviewing finding details and history in

Security Hub CSPM

In AWS Security Hub CSPM, a _finding_ is an observable record of a
security check or security-related detection. Security Hub CSPM generates a finding when it completes a
security check of a control and when it ingests a finding from an integrated AWS service
or third-party product. Each finding includes a history of changes and other details, such
as a severity rating and information about the affected resources.

You can review the history and other details of individual findings on the Security Hub CSPM console
or programmatically with the Security Hub CSPM API or the AWS CLI.

To help you streamline your analysis, the Security Hub CSPM console displays a finding panel when
you choose a specific finding. The panel includes different menus and tabs for reviewing
specific details of a finding.

**Actions menu**
From this menu, you can review the complete JSON of a finding or add notes. A finding can have
only one note attached to it at a time. This menu also provides options to [set the workflow status of a
finding](findings-workflow-status.md "findings-workflow-status.md") or [send a finding to a
custom action](findings-custom-action.md "findings-custom-action.md") in Amazon EventBridge.

**Investigate menu**
From this menu, you can investigate a finding in Amazon Detective. Detective extracts entities, such as
IP addresses and AWS users, from a finding and visualizes their activity. You can use the entity activity as a starting point to investigate the cause and impact of a finding.

**Overview tab**
This tab provides a summary of a finding. For example, you can determine when a finding was
created and last updated, in which account it exists, and the source of the
finding. For control findings, this tab also shows the name of the associated
AWS Config rule and a link to remediation guidance in the Security Hub CSPM documentation.

In the **Resources** snapshot on the
**Overview** tab, you can get a brief overview of the
resources involved in a finding. For some resources, this includes an
**Open resource** option, which links directly to an
impacted resource on the relevant AWS service console. The
**History** snapshot shows up to two changes made to the
finding on the most recent date for which history is being tracked. For example,
if you made one change yesterday and another one today, the snapshot shows
today's change. To review earlier entries, switch to the
**History** tab.

The **Compliance** row expands to show more details. For
example, if a control includes parameters, you can review the parameter values
that Security Hub CSPM currently uses when conducting security checks for the
control.

**Resources tab**

This tab provides details about the resources involved in a finding. If you're
signed in to the account that owns a resource, you can review the resource in
the applicable AWS service console. If you're not the owner of a resource,
this tab displays the AWS account ID for the owner.

The **Details** row shows resource-specific details in a
finding. It shows the [ResourceDetails](../../1.0/APIReference/API_ResourceDetails.md "../../1.0/APIReference/API_ResourceDetails.md") section of the finding in JSON
format.

The **Tags** row shows tag keys and values that are assigned
to the resources involved in a finding. Resources that are [supported by the GetResources operation](../../../resourcegroupstagging/latest/APIReference/supported-services.md "../../../resourcegroupstagging/latest/APIReference/supported-services.md") of the
AWS Resource Groups Tagging API can be tagged. Security Hub CSPM calls this operation by using a [service-linked role](using-service-linked-roles.md "using-service-linked-roles.md") when
processing new or updated findings, and retrieves the resource tags if the
AWS Security Finding Format (ASFF) `Resource.Id` field is populated with the ARN of a
resource. Security Hub CSPM ignores invalid resource IDs. For more information about the
inclusion of resource tags in findings, see [Tags](asff-resources-attributes.md#asff-resources-tags "asff-resources-attributes.md#asff-resources-tags").

**History tab**

This tab tracks the history of a finding. Finding history is available for
active and archived findings. It provides an immutable trail of changes made to
a finding over time, including what ASFF field changed, when the change
occurred, and by which user. Each page on the tab displays up to 20 changes.
More recent changes are displayed first.

For active findings, finding history is available for up to 90 days. For
archived findings, finding history is available for up to 30 days. Finding
history includes changes that were made manually, or automatically by [Security Hub CSPM automation rules](automation-rules.md "automation-rules.md"). It doesn't include
changes to top-level timestamp fields, such as the `CreatedAt` and
`UpdatedAt` fields.

If you're signed in to a Security Hub CSPM administrator account, finding history is for
the administrator account and all member accounts.

**Threat tab**

This tab includes data from the [Action](../../1.0/APIReference/API_Action.md "../../1.0/APIReference/API_Action.md"), [Malware](../../1.0/APIReference/API_Malware.md "../../1.0/APIReference/API_Malware.md"), and [ProcessDetails](../../1.0/APIReference/API_Process.md "../../1.0/APIReference/API_Process.md") objects of the ASFF, including
the type of threat and whether a resource is the target or actor. These details
typically apply to findings that originate in Amazon GuardDuty.

**Vulnerabilities tab**

This tab displays data from the [Vulnerability](../../1.0/APIReference/API_Vulnerability.md "../../1.0/APIReference/API_Vulnerability.md") object of the ASFF, including
whether there are exploits or available fixes associated with a finding. These
details typically apply to findings that originate in Amazon Inspector.

The rows on each tab include a copy or filter option. For example, if you open the panel
for a finding that has a workflow status of **Notified**, you can choose
the filter option next to the **Workflow status** row. If you choose
**Show all findings with this value**, Security Hub CSPM filters the findings table
and displays only findings with the same workflow status.

## Reviewing finding details and

history

Choose your preferred method, and follow the steps to review finding details in
Security Hub CSPM.

If you enable cross-Region aggregation and sign in to the aggregation Region, finding
data includes data from the aggregation Region and linked Regions. In other Regions,
finding data is specific to that Region only. For more information about cross-Region
aggregation, see [Understanding cross-Region aggregation in Security Hub CSPM](finding-aggregation.md "finding-aggregation.md").

Security Hub CSPM console

###### Reviewing finding details and history

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. To display a finding list, do one of the following:
   - In the navigation pane, choose
     **Findings**. Add search filters as
     necessary to narrow the finding list.
   - In the navigation pane, choose
     **Insights**. Choose an insight. Then,
     in the results list, choose an insight result.
   - In the navigation pane, choose
     **Integrations**. Choose **See
     findings** for an integration.
   - In the navigation pane, choose
     **Controls**.

3. Choose a finding. The finding panel displays the details of the
   finding.
4. In the finding panel, do any of the following:
   - To review specific details for the finding, choose a
     tab.
   - To take action on the finding, choose an option from the
     **Actions** menu.
   - To investigate the finding in Amazon Detective, choose an
     **Investigate** option.

###### Note

If you integrate with AWS Organizations and you're signed in to a member
account, the finding panel includes the account name. For member
accounts that are invited manually, instead of through Organizations, the finding
panel includes only the account ID.

Security Hub CSPM API
Use the [GetFindings](../../1.0/APIReference/API_GetFindings.md "../../1.0/APIReference/API_GetFindings.md") operation of the Security Hub CSPM API, or
if you're using the AWS CLI, run the [get-findings](../../../cli/latest/reference/securityhub/get-findings.md "../../../cli/latest/reference/securityhub/get-findings.md") command. You can provide one or
more values for the `Filters` parameter to narrow the findings to
retrieve.

If the volume of results is too large, you can use the
`MaxResults` parameter to limit the findings to a specified
number and the `NextToken` parameter to paginate findings. Use
the `SortCriteria` parameter to sort the findings by a specific
field.

For example, the following AWS CLI command retrieves the findings that match
the specified filter criteria, and sorts the results in descending order by
the `LastObservedAt` field. This example is formatted for Linux,
macOS, or Unix, and it uses the backslash (\) line-continuation character to
improve readability.

```
`$` `aws securityhub get-findings \
--filters '{"GeneratorId":[{"Value": "`aws-foundational`","Comparison":"`PREFIX`"}],"WorkflowStatus": [{"Value": "`NEW`","Comparison":"`EQUALS`"}],"Confidence": [{"Gte": `85`}]}' --sort-criteria '{"Field": "`LastObservedAt`","SortOrder": "`desc`"}' --page-size `5` --max-items `100``
```

To review finding history, use the [GetFindingHistory](../../1.0/APIReference/API_GetFindingHistory.md "../../1.0/APIReference/API_GetFindingHistory.md") operation. If you're using
the AWS CLI, run the [get-finding-history](../../../cli/latest/reference/securityhub/get-finding-history.md "../../../cli/latest/reference/securityhub/get-finding-history.md") command. Identify the
finding that you want to get history for with the `ProductArn`
and `Id` fields. For information about these fields, see [AwsSecurityFindingIdentifier](../../1.0/APIReference/API_AwsSecurityFindingIdentifier.md "../../1.0/APIReference/API_AwsSecurityFindingIdentifier.md"). Each request
can retrieve the history for only one finding.

For example, the following AWS CLI command retrieves the history for the
specified finding. This example is formatted for Linux, macOS, or Unix, and
it uses the backslash (\) line-continuation character to improve
readability.

```
`$` `aws securityhub get-finding-history \
--region `us-west-2` \
--finding-identifier Id="`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",ProductArn="arn:aws:securityhub:`us-west-2`:`123456789012`:product/`123456789012`/default" \
--max-results `2` \
--start-time "`2021-09-30T15:53:35.573Z`" \
--end-time "`2021-09-31T15:53:35.573Z`"`
```

PowerShell
Use the `Get-SHUBFinding` cmdlet. Optionally populate the
`Filter` parameter to narrow the findings to retrieve.

For example, the following cmdlet retrieves the findings that match the
specified filters.

```
Get-SHUBFinding -Filter @{AwsAccountId = [Amazon.SecurityHub.Model.StringFilter]@{Comparison = "EQUALS"; Value = "XXX"};ComplianceStatus = [Amazon.SecurityHub.Model.StringFilter]@{Comparison = "EQUALS"; Value = 'FAILED'}}
```

###### Note

If you filter findings by `CompanyName` or `ProductName`,
Security Hub CSPM uses the values that are part of the `ProductFields` ASFF object.
Security Hub CSPM doesn't use the top-level `CompanyName` and
`ProductName` fields.
