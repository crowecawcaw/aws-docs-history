

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Supported data source types for automated evidence
<a name="control-data-sources"></a>



When you create a custom control in AWS Audit Manager, you can set up your control to collect automated evidence from the following data source types:
+ AWS CloudTrail 
+ AWS Security Hub CSPM
+ AWS Config
+ AWS API calls 

Each data source type offers distinct capabilities for capturing user activity logs, compliance findings, resource configurations, and more. 

In this chapter you can learn about each of these automated data source types, and the specific AWS Security Hub CSPM controls, AWS Config rules, and AWS API calls that are supported by Audit Manager.

## Key points
<a name="controls-automated-data-sources"></a>

The following table provides an overview of each automated data source type.


| Data source type | Description | Evidence collection frequency | To use this data source type... | When this control is active in an assessment... | Related troubleshooting tips | 
| --- | --- | --- | --- | --- | --- | 
| AWS CloudTrail | Tracks a specific user activity.  | Continuous. | Select from the list of [supported event names](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-cloudtrail.html). | Audit Manager filters your CloudTrail logs based on the keyword that you choose. The results are imported as **User activity** evidence. | [My assessment isn’t collecting user activity evidence from AWS CloudTrail](evidence-collection-issues.md#no-evidence-from-cloudtrail) | 
| AWS Config | Captures a snapshot of your resource security posture by reporting findings from AWS Config. | Based on the triggers defined in the AWS Config rule. | Choose a rule type, then select a rule.+  For managed rules, select from the list of [supported managed rule keywords](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-managed-rules). <br />+  For custom rules, select from the list of [your available rules](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-custom-rules).  | Audit Manager gets the findings for this rule directly from AWS Config. The result is imported as Compliance check evidence. | [My assessment isn’t collecting compliance check evidence from AWS Config](evidence-collection-issues.md#no-evidence-from-config)<br />[AWS Config integration issues](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-issues.html#config-rule-integration.title) | 
| AWS Security Hub CSPM | Captures a snapshot of your resource security posture by reporting findings from Security Hub CSPM. | Based on the schedule of the Security Hub CSPM check. | Select from the list of [supported Security Hub CSPM control IDs](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-ash.html). | Audit Manager gets the result of the security check directly from Security Hub CSPM. The result is imported as **Compliance check** evidence. | [My assessment isn’t collecting compliance check evidence from AWS Security Hub CSPM](evidence-collection-issues.md#no-evidence-from-security-hub) | 
| AWS API calls  | Takes a snapshot of your resource configuration directly through an API call to the specified AWS service.  | Daily, weekly, or monthly. | Select from the list of [supported API calls](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-api.html), then select your preferred frequency. | Audit Manager makes the API call based on the frequency that you specify. The response is imported as Configuration data evidence.  | [My assessment isn’t collecting configuration data evidence for an AWS API call](evidence-collection-issues.md#no-evidence-from-aws-api-calls) | 

**Tip**  
You can create custom controls that collect evidence using predefined groupings of the above data sources. These data source groupings are known as [AWS managed sources](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#aws-managed-source). Each AWS managed source represents a common control or a core control that aligns with a common compliance requirement. This gives you an efficient way to map your compliance requirements to a relevant group of AWS data sources. To see the available common controls, see [Finding the available controls in AWS Audit Manager](access-available-controls.md).  
Alternatively, you can use the four data source types above to define your own custom data sources. This gives you the flexibility to upload manual evidence, or collect automated evidence from a business-specific resource such as a custom AWS Config rule.

## Next steps
<a name="controls-automated-data-sources-next-steps"></a>

To learn more about the specific data sources that you can use in your custom controls, see the following pages.
+ [AWS Config Rules supported by AWS Audit Manager](control-data-sources-config.md)
+ [AWS Security Hub CSPM controls supported by AWS Audit Manager](control-data-sources-ash.md)
+ [AWS API calls supported by AWS Audit Manager](control-data-sources-api.md)
+ [AWS CloudTrail event names supported by AWS Audit Manager](control-data-sources-cloudtrail.md)