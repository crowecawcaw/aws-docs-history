

# Reviewing the details of a security standard
<a name="securityhub-standards-view-controls"></a>

After you enable a security standard in AWS Security Hub CSPM, you can use the console to review the details of the standard. On the console, the details page for a standard includes the following information:
+ The current security score for the standard.
+ A table of controls that apply to the standard.
+ Aggregated statistics for controls that apply to the standard.
+ A visual summary of the status of the controls that apply to the standard.
+ A visual summary of security checks for controls that are enabled and apply to the standard. If you integrate with AWS Organizations, controls that are enabled in at least one organization account are considered enabled.

To review these details, choose **Security standards** in the navigation pane on the console. Then, in the section for the standard, choose **View results**. For deeper analysis, you can filter and sort the data, and drill down to review the details of individual controls that apply to the standard.

**Topics**
+ [Understanding the standard security score](#standard-details-overview)
+ [Reviewing the controls for a standard](#standard-controls-list)

## Understanding the standard security score
<a name="standard-details-overview"></a>

On the AWS Security Hub CSPM console, the details page for a standard displays the security score for the standard. The score is the percentage of controls that passed evaluation, relative to the total number of controls that apply to the standard, are enabled, and have evaluation data. Under the score is a chart that summarizes security checks for controls that are enabled for the standard. This includes the number of passed and failed security checks. For administrator accounts, the standard score and chart are aggregated across the administrator account and all member accounts. To review failed security checks for controls that have a specific severity, choose the severity.

When you enable a standard, Security Hub CSPM generates a preliminary security score for the standard, typically within 30 minutes of your first visit to the **Summary** page or the **Security standards** page on the Security Hub CSPM console. Scores are generated only for standards that are enabled when you visit those pages. In addition, AWS Config resource recording must be configured for the scores to appear. In the China Regions and AWS GovCloud (US) Regions, it can take up to 24 hours for Security Hub CSPM to generate a preliminary score. After Security Hub CSPM generates a preliminary score for a standard, it updates the score every 24 hours. For more information, see [Calculating security scores](standards-security-score.md).

All the data on **Security standards** detail pages is specific to the current AWS Region unless you set an aggregation Region. If you set an aggregation Region, security scores apply across Regions and include findings for all linked Regions. In addition, the compliance status of controls reflects findings from linked Regions, and the number of security checks includes findings from linked Regions.

## Reviewing the controls for a standard
<a name="standard-controls-list"></a>

When you use the AWS Security Hub CSPM console to review the details of a standard that you enabled, you can review a table of security controls that apply to the standard. For each control, the table includes the following information:
+ The control ID and title.
+ The status of the control. For more information, see [Evaluating compliance status and control status](controls-overall-status.md).
+ The severity assigned to the control.
+ The number of failed checks and the total number of checks. If applicable, the **Failed checks** field also specifies the number of findings with a status of **Unknown**.
+ Whether the control supports custom parameters. For more information, see [Understanding control parameters in Security Hub CSPM](custom-control-parameters.md).

Security Hub CSPM updates control statuses and the count of security checks every 24 hours. A timestamp at the top of the page indicates when Security Hub CSPM most recently updated this data.

For administrator accounts, control statuses and the number of security checks are aggregated across the administrator account and all member accounts. The count of enabled controls includes controls that are enabled for the standard in the administrator account or at least one member account. The count of disabled controls includes controls that are disabled for the standard in the administrator account and all member accounts.

You can filter the table of controls that apply to the standard. Using the **Filter by** options next to the table, you can choose to view only enabled or only disabled controls for the standard. If you display only enabled controls, you can further filter the table by control status. You can then focus on controls that have a specific control status. In addition to the **Filter by** options, you can enter filter criteria in the **Filter controls** box. For example, you can filter by control ID or title.

Choose your preferred access method. Then follow the steps to review the controls that apply to a standard that you enabled.

------
#### [ Security Hub CSPM console ]

**To review the controls for an enabled standard**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. Choose **Security standards** in the navigation pane.

1. In the section for the standard, choose **View results**.

The table at the bottom of the page lists all the controls that apply to the standard. You can filter and sort the table. You can also download the current page of the table as a CSV file. To do this, choose **Download** above the table. If you filter the table, the downloaded file includes only the controls that match your current filter settings.

------
#### [ Security Hub CSPM API ]

**To review the controls for an enabled standard**

1. Use the [ListSecurityControlDefinitions](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListSecurityControlDefinitions.html) operation of the Security Hub CSPM API. If you're using the AWS CLI, run the [list-security-control-definitions](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-security-control-definitions.html) command.

   Specify the Amazon Resource Name (ARN) of the standard that you want to review controls for. To obtain ARNs for standards, use the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) operation or run the [describe-standards](https://docs.aws.amazon.com/cli/latest/reference/securityhub/describe-standards.html) command. If you don't specify the ARN for a standard, Security Hub CSPM returns all security control IDs.

1. Use the [ListStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListStandardsControlAssociations.html) operation of the Security Hub CSPM API, or run the [list-standards-control-associations](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-standards-control-associations.html) command. This operation tells you which standards a control is enabled in.

   Identify the control by providing the security control ID or ARN. Pagination parameters are optional.

The following example tells you which standards the Config.1 control is enabled in.

```
$ aws securityhub list-standards-control-associations --region {{us-east-1}} --security-control-id {{Config.1}}
```

------