

# Service Quotas in AWS GovCloud (US)
<a name="govcloud-servicequotas"></a>

 [Service Quotas](https://console.aws.amazon.com/servicequotas) enables you to view and manage your AWS service quotas from a central location. You can view the AWS default quotas, your account-level or applied quotas and request for quota increases. Through its [integration with AWS CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.html), you can also view usage against quotas and configure alarms to get notified when approaching a quota threshold. Service Quotas offers both a console experience and programmatic access via the AWS SDK, and is available to all AWS customers at no additional cost.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Service Quotas differs
<a name="govcloud-servicequotas-diffs"></a>

The following differences apply to Service Quotas:
+ The [Quota request template](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) is currently not supported in AWS GovCloud(US) Regions.

## Documentation
<a name="govcloud-servicequotas-docs"></a>
+  [Service Quotas documentation](https://docs.aws.amazon.com/servicequotas/index.html) 

## Export-controlled content
<a name="govcloud-servicequotas-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ The initial quota value established by AWS (default value) and the new quota value after a quota increase (applied value).
+ Information related to open quota increase requests or requests that were closed in the last 90 days.
+ Tags on any service quota with applied values.