

# Reviewing the details of controls in Security Hub CSPM
<a name="securityhub-standards-control-details"></a>

Selecting a control on the **Controls** page or standard details page of the Security Hub CSPM console takes you to a page of control details.

The top of the control details page indicates the control status. The control status summarizes the performance of a control based on the compliance status of the control findings. Security Hub CSPM typically generates the initial control status within 30 minutes after your first visit to the **Summary** page or **Security standards** page on the Security Hub CSPM console. Statuses are only available for controls that are enabled when you visit those pages.

The control details page also provides a breakdown of the compliance status of the control findings for the past 24 hours. For more information about control status and compliance status, see [Evaluating compliance status and control status](controls-overall-status.md).

AWS Config resource recording must be configured for the control status to appear. After control statuses are generated for the first time, Security Hub CSPM updates the control status every 24 hours based on findings from the previous 24 hours.

Administrator accounts see an aggregated control status across the administrator account and member accounts. If you have set an aggregation Region, the control status includes findings across all linked Regions. For more information about control status, see [Evaluating compliance status and control status](controls-overall-status.md).

You can also enable or disable the control from the control details page.

**Note**  
It can take up to 24 hours after enabling a control for first-time control statuses to be generated in the China Regions and AWS GovCloud (US) Regions.

The **Standards and Requirements** tab lists the standards that a control can be enabled for and the requirements related to the control from different compliance frameworks.

The **Checks** tab lists active findings for the control for the past 24 hours. Control findings are generated and updated when Security Hub CSPM runs security checks for the control. The list on this tab doesn't include archived findings.

For each finding, the list provides access to finding details such as the compliance status and related resource. You can also set the workflow status of each finding and send findings to custom actions. For more information, see [Reviewing and managing control findings](securityhub-control-manage-findings.md).

## Viewing details for a control
<a name="view-control-details-console"></a>

Choose your preferred access method, and follow these steps to review details for a control. Details apply to the current account and Region and include the following:
+ The title and description of the control.
+ A link to remediation guidance for failed control findings.
+ The severity of the control.
+ The status of the control.

On the console, you can also review a list of recent findings for the control. To do this programmatically, you can use the [GetFindings](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindings.html) operation of the Security Hub CSPM API.

------
#### [ Security Hub CSPM console ]

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. Choose **Controls** in the navigation pane.

1. Select a control.

------
#### [ Security Hub CSPM API ]

1. Run `[`ListSecurityControlDefinitions`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListSecurityControlDefinitions.html)`, and provide one or more standard ARNs to get a list of control IDs for that standard. To obtain standard ARNs, run [`DescribeStandards`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html). If you don't provide a standard ARN, this API returns all Security Hub CSPM control IDs. This API returns standard-agnostic security control IDs, not the standard-based control IDs that existed prior to these feature releases.

   **Example request:**

   ```
   {
       "StandardsArn": "arn:aws:securityhub:::{{standards/aws-foundational-security-best-practices/v/1.0.0}}"
   }
   ```

1. Run `[`BatchGetSecurityControls`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetSecurityControls.html)` to get details about one or more controls in the current AWS account and AWS Region.

   **Example request:**

   ```
   {
       "SecurityControlIds": ["{{Config.1}}", "{{IAM.1}}"]
   }
   ```

------
#### [ AWS CLI ]

1. Run the `[`list-security-control-definitions`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-security-control-definitions.html)` command, and provide one or more standard ARNs to get a list of control IDs. To obtain standard ARNs, run the `describe-standards` command. If you don't provide a standard ARN, this command returns all Security Hub CSPM control IDs. This command returns standard-agnostic security control IDs, not the standard-based control IDs that existed prior to these feature releases.

   ```
   aws securityhub --region {{us-east-1}} list-security-control-definitions --standards-arn "arn:aws:securityhub:{{us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0}}"
   ```

1. Run the `[`batch-get-security-controls`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/batch-get-security-controls.html)` command to get details about one or more controls in the current AWS account and AWS Region.

   ```
   aws securityhub --region {{us-east-1}} batch-get-security-controls --security-control-ids {{'["Config.1", "IAM.1"]'}}
   ```

------