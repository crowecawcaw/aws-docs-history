# Filtering and sorting controls in Security Hub CSPM

On the AWS Security Hub CSPM console, you can use the **Controls** page to review a
table of the controls that are available in the current AWS Region. The exception is an
aggregation Region. If you [configured an aggregation
Region](finding-aggregation.md "finding-aggregation.md") and sign in to that Region, the console shows controls that are available
in the aggregation Region or one or more linked Regions.

To focus on a specific subset of controls, you can sort and filter the table of controls.
The **Filter by** options next to the table can help you quickly focus on
these specific subsets:

- All enabled controls, which are controls that are enabled in at least one enabled
  standard.
- All disabled controls, which are controls that are disabled in all
  standards.
- All enabled controls that have a specific control status, such as
  **Failed**. The **No data** option displays
  only those controls that don't currently have findings. For information about
  control status, see [Evaluating compliance status and control
  status](controls-overall-status.md "controls-overall-status.md").
  In addition to the **Filter by** options, you can filter the table by
  entering filter criteria in the **Filter controls** box above the table.
  For example, you can filter by control ID or severity.

By default, controls with a **Failed** status are listed first, in
descending order by severity. You can change the sort order by choosing a different column
heading.

###### Tip

If you have automated workflows based on control findings, we recommend using the
`SecurityControlId` or `SecurityControlArn`
[ASFF fields](securityhub-findings-format.md "securityhub-findings-format.md") as filters, rather than
the `Title` or `Description` fields. The latter fields can change
occasionally, whereas control ID and ARN are static identifiers.

If you're signed in to a Security Hub CSPM administrator account, **Enabled**
controls include controls that are enabled in at least one member account. If you configured
an aggregation Region, **Enabled** controls include controls that are
enabled in at least one linked Region.

If you select the option next to an enabled a control, a panel appears and displays the
standards in which the control is currently enabled. You can also see the standards in which
the control is currently disabled. From this panel, you can disable a control in all
standards. For more information, see [Disabling controls in Security Hub CSPM](disable-controls-overview.md "disable-controls-overview.md"). For
administrator accounts, the information in the panel reflects settings for all of your
member accounts.

To retrieve a list of controls programmatically, you can use the [ListSecurityControlDefinitions](../../1.0/APIReference/API_ListSecurityControlDefinitions.md "../../1.0/APIReference/API_ListSecurityControlDefinitions.md") operation of the Security Hub CSPM API.
To retrieve the details of individual controls, use the [BatchGetSecurityControls](../../1.0/APIReference/API_BatchGetSecurityControls.md "../../1.0/APIReference/API_BatchGetSecurityControls.md") operation.
