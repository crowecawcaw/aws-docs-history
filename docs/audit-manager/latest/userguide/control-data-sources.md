# Supported data source types for automated evidence

When you create a custom control in AWS Audit Manager, you can set up your control to collect
automated evidence from the following data source types:

- AWS CloudTrail
- AWS Security Hub CSPM
- AWS Config
- AWS API calls
  Each data source type offers distinct capabilities for capturing user activity logs,
  compliance findings, resource configurations, and more.

In this chapter you can learn about each of these automated data source types, and the
specific AWS Security Hub CSPM controls, AWS Config rules, and AWS API calls that are supported by
Audit Manager.

## Key points

The following table provides an overview of each automated data source type.

| Data source type      | Description                                                                                                   | Evidence collection frequency                         | To use this data source type...                                                                                                                                                                                                                                                                                                                                                                                                       | When this control is active in an assessment...                                                                                                       | Related troubleshooting tips                                                                                                                                                                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS CloudTrail        | Tracks a specific user activity.                                                                              | Continuous.                                           | Select from the list of [supported event names](control-data-sources-cloudtrail.md "control-data-sources-cloudtrail.md").                                                                                                                                                                                                                                                                                                             | Audit Manager filters your CloudTrail logs based on the keyword that you choose. The results<br>are imported as \*_User activity_<br>• evidence.      | [My assessment isn’t collecting user activity evidence from AWS CloudTrail](evidence-collection-issues.md#no-evidence-from-cloudtrail "evidence-collection-issues.md#no-evidence-from-cloudtrail")                                                                                                                              |
| AWS Config            | Captures a snapshot of your resource security posture by reporting findings from<br>AWS Config.               | Based on the triggers defined in the AWS Config rule. | Choose a rule type, then select a rule.<br>• For managed rules, select from the list of [supported managed rule keywords](control-data-sources-config.md#aws-config-managed-rules "control-data-sources-config.md#aws-config-managed-rules").<br>• For custom rules, select from the list of [your available rules](control-data-sources-config.md#aws-config-custom-rules "control-data-sources-config.md#aws-config-custom-rules"). | Audit Manager gets the findings for this rule directly from AWS Config. The result is imported<br>as \*_Compliance check_<br>• evidence.              | [My assessment isn’t collecting compliance check evidence from AWS Config](evidence-collection-issues.md#no-evidence-from-config "evidence-collection-issues.md#no-evidence-from-config")<br>[AWS Config integration issues](control-issues.md#config-rule-integration.title "control-issues.md#config-rule-integration.title") |
| AWS Security Hub CSPM | Captures a snapshot of your resource security posture by reporting findings from<br>Security Hub CSPM.        | Based on the schedule of the Security Hub CSPM check. | Select from the list of [supported Security Hub CSPM<br>control IDs](control-data-sources-ash.md "control-data-sources-ash.md").                                                                                                                                                                                                                                                                                                      | Audit Manager gets the result of the security check directly from Security Hub CSPM. The result is<br>imported as \*_Compliance check_<br>• evidence. | [My assessment isn’t collecting compliance check evidence from AWS Security Hub CSPM](evidence-collection-issues.md#no-evidence-from-security-hub "evidence-collection-issues.md#no-evidence-from-security-hub")                                                                                                                |
| AWS API calls         | Takes a snapshot of your resource configuration directly through an API call to<br>the specified AWS service. | Daily, weekly, or monthly.                            | Select from the list of [supported API<br>calls](control-data-sources-api.md "control-data-sources-api.md"), then select your preferred frequency.                                                                                                                                                                                                                                                                                    | Audit Manager makes the API call based on the frequency that you specify. The response is<br>imported as \*_Configuration data_<br>• evidence.        | [My assessment isn’t collecting configuration data evidence for an AWS API call](evidence-collection-issues.md#no-evidence-from-aws-api-calls "evidence-collection-issues.md#no-evidence-from-aws-api-calls")                                                                                                                   |

###### Tip

You can create custom controls that collect evidence using predefined groupings of the
above data sources. These data source groupings are known as [AWS managed
sources](concepts.md#aws-managed-source "concepts.md#aws-managed-source"). Each AWS managed source represents a common control or a core control
that aligns with a common compliance requirement. This gives you an efficient way to map
your compliance requirements to a relevant group of AWS data sources. To see the available
common controls, see [Finding the available controls in AWS Audit Manager](access-available-controls.md "access-available-controls.md").

Alternatively, you can use the four data source types above to define your own custom
data sources. This gives you the flexibility to upload manual evidence, or collect automated
evidence from a business-specific resource such as a custom AWS Config rule.

## Next steps

To learn more about the specific data sources that you can use in your custom controls,
see the following pages.

- [AWS Config Rules supported by AWS Audit Manager](control-data-sources-config.md "control-data-sources-config.md")
- [AWS Security Hub CSPM controls supported by AWS Audit Manager](control-data-sources-ash.md "control-data-sources-ash.md")
- [AWS API calls supported by AWS Audit Manager](control-data-sources-api.md "control-data-sources-api.md")
- [AWS CloudTrail event names supported by AWS Audit Manager](control-data-sources-cloudtrail.md "control-data-sources-cloudtrail.md")
