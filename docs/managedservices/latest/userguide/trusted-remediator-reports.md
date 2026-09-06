

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Trusted Remediator reports
<a name="trusted-remediator-reports"></a>

**Topics**
+ [Trusted Remediator Remediation Summary report](#trusted-remediator-summary)
+ [Trusted Remediator Configuration Summary report](#trusted-remediator-config-summary)
+ [Trusted Advisor Check Summary report](#trusted-advisor-check-summary)

## Trusted Remediator Remediation Summary report
<a name="trusted-remediator-summary"></a>

The Trusted Remediator Remediation Status report provides information about the remediations that occurred during previous remediation cycles. The default number of weeks is 1. To customize the report, specify the number of weeks based on your remediation schedule.


| **Field Name** | **Definition** | 
| --- | --- | 
| Date | The date that the data was collected on. | 
| Account ID | The AWS account ID that the resource belongs to | 
| Account Name | The AWS account name | 
| Check Category | The AWS Trusted Advisor check category | 
| Check Name | The name of the remediated Trusted Advisor check | 
| Check ID | The ID of the remediated Trusted Advisor check | 
| Execution Mode | The execution mode that was configured for the specific Trusted Advisor check | 
| OpsItem ID | The ID of the OpsItem created by Trusted Advisor for remediation | 
| OpsItem Status | The status of the OpsItem created by Trusted Advisor at the time of reporting | 
| Resource ID | The ARN of the resource created for remediation | 

## Trusted Remediator Configuration Summary report
<a name="trusted-remediator-config-summary"></a>

The Trusted Remediator Configuration Summary report provides information about the current Trusted Remediator Remediation configurations for each Trusted Advisor check.


| **Field Name** | **Definition** | 
| --- | --- | 
| Date | The date that the data was collected on. | 
| Account ID | The AWS account ID that the configuration applies to | 
| Account Name | The AWS account name | 
| Check Category | The AWS Trusted Advisor check category | 
| Check Name | The name of the remediated Trusted Advisor check that the configuration applies to | 
| Check ID | The ID of the remediated Trusted Advisor check that the configuration applies to | 
| Execution Mode | The execution mode that was configured for the specific Trusted Advisor check | 
| Override to Automated | The tag pattern, if configured, to override execution mode to Automated | 
| Override to Manual | The tag pattern, if configured, to override execution mode to Manual | 

## Trusted Advisor Check Summary report
<a name="trusted-advisor-check-summary"></a>

The Trusted Advisor Check Summary report provides information about the current Trusted Advisor checks. This report collects data after each weekly remediation schedule. The default number of weeks is 1. To customize the report, specify the number of weeks based on your remediation cycle.


| **Field Name** | **Definition** | 
| --- | --- | 
| Date | The date that the data was collected on. | 
| Account ID | The AWS account ID that the configuration applies to | 
| Customer Name | The AWS account name | 
| Check Category | The AWS Trusted Advisor check category | 
| Check Name | The name of the remediated Trusted Advisor check that the configuration applies to | 
| Check ID | The ID of the remediated Trusted Advisor check that the configuration applies to | 
| Status | The alert status of the check. Possible statuses are ok (green), warning (yellow), error (red), or not\_available | 
| Resources Flagged | The number of AWS resources that were flagged (listed) by the Trusted Advisor check. | 
| Resources Ignored | The number of AWS resources that were ignored by Trusted Advisor because you marked them as suppressed. | 
| Resources in critical state | The number of resources in critical state | 
| Resources in warning state | The number of resources in warning state | 