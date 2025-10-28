# Service Quotas in AWS GovCloud (US)

[Service Quotas](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas") enables you to view and manage your AWS service quotas from a central location.
You can view the AWS default quotas, your account-level or applied quotas and request for quota increases.
Through its [integration with AWS CloudWatch](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md"), you can also view usage against quotas and configure alarms to get notified when approaching a quota threshold.
Service Quotas offers both a console experience and programmatic access via the AWS SDK, and is available to all AWS customers at no additional cost.

## How Service Quotas differs for AWS GovCloud (US)

- The [Quota request template](../../../servicequotas/latest/userguide/organization-templates.md "../../../servicequotas/latest/userguide/organization-templates.md") is currently not supported in AWS GovCloud(US) Regions.

## Documentation for Service Quotas

[Service Quotas documentation](../../../servicequotas/index.md "../../../servicequotas/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- The initial quota value established by AWS (default value) and the new quota
  value after a quota increase (applied value).
- Information related to open quota increase requests or requests that were
  closed in the last 90 days.
- Tags on any service quota with applied values.
