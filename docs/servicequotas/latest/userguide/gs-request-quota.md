# Viewing service quotas

###### Note

If you are searching for service quotas for a specific AWS service, review
[Service endpoints
and quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md") in the _AWS General Reference guide_.

Service Quotas enables you to review the AWS default value and applied values of a particular
_quota_. Certain resource-level quotas, such as `Instances per domain`
for Amazon OpenSearch Service, also display applied quota values per resource. Refer to
[Terminology in Service Quotas](intro.md#intro_getting-started "intro.md#intro_getting-started")
for detailed definitions of these values.

Your account's actual quota value may be less than the AWS default quota value if you recently created
the account, or if you use the account minimally.

AWS Management Console

###### To view the quotas for a service

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home").
2. In the navigation pane, choose **AWS
   services**.
3. Select an AWS service from the list, or enter the name of the service
   in the search field.

The console displays details for the selected service's quota, including
the **quota name**, **applied quota value**, **AWS default quota**,
**utilization**, and if the quota is **adjustable** at the account-level or
resource-level.

If the applied quota value or utilization is
not available, the console displays **Not
available**.
You can request your applied quota value through the
Support Center Console. 4. Choose a specific **quota name** to view the Details page, which displays that quota's **description**,
**quota code**, **quota ARN**, **utilization**, **applied quota value**,
and the **AWS default quota**.

If applicable, the Details page also displays any **resource-level quota**, **alarms**,
**quota increase request history**, and any of the quota's **tags**.

AWS CLI

###### Viewing default quota values

View the default values for the quotas for a specific
AWS service.

- Call the [ListDefaultServiceQuotas](../../2019-06-24/apireference/API_ListDefaultServiceQuotas.md "../../2019-06-24/apireference/API_ListDefaultServiceQuotas.md") operation with a service code. If
  you don't have the service code, you can get a list of supported services with the [ListServices](../../2019-06-24/apireference/API_ListServices.md "../../2019-06-24/apireference/API_ListServices.md") operation. The response includes the
  `ServiceCode` and `ServiceName` for each
  service. The `ServiceCode` for Amazon OpenSearch Service is `es`.
  The following CLI example retrieves default values for Amazon OpenSearch Service
  quotas.

```
`$` `aws service-quotas list-aws-default-service-quotas \
 --service-code es \``{
 "Quotas": [
 {
 "QuotaName": "Domains per Region",
 "Adjustable": true,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-076D529E",
 "Value": 100.0,
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-076D529E",
 "Unit": "None",
 },
 {
 "QuotaName": "Dedicated master instances per domain",
 "Adjustable": false,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-AE676A72",
 "Value": 5.0,
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-AE676A72",
 "Unit": "None",
 },
 {
 "QuotaName": "Warm instances per domain",
 "Adjustable": false,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-1F053E6F",
 "Value": 150.0,
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-1F053E6F",
 "Unit": "None",
 },
 {
 "QuotaName": "Instances per domain",
 "Adjustable": true,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
 "Value": 80.0,
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-6408ABDE",
 "Unit": "None",
 "QuotaContext": {
 "ContextScope": "RESOURCE",
 "ContextScopeType": "AWS::OpenSearchService::Domain",
 }
 }
 ]
}`
```

###### Viewing applied quota values

View the applied quota values for a specified AWS service. For some
quotas, only the default values are available. If the applied quota value
isn't available for a quota, the quota is not returned in the response. If
this happens, contact Support for the applied quota value.

- Call the [ListServiceQuotas](../../2019-06-24/apireference/API_ListServiceQuotas.md "../../2019-06-24/apireference/API_ListServiceQuotas.md") operation with a service code.
  You can choose to retrieve all applied quota values either at the
  account-level, resource-level, or all levels by passing
  `ACCOUNT`, `RESOURCE`, or `ALL`
  respectively as the value for
  the parameter `QuotaAppliedAtLevel`.

The following CLI example retrieves all quota values applied at the
account-level for OpenSearch Service.

```
`$` `aws service-quotas list-service-quotas \
 --service-code es \
 --quota-applied-at-level ACCOUNT``{
 "Quotas": [
 {
 "QuotaName": "Domains per Region",
 "Adjustable": true,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-076D529E",
 "Value": 100.0,
 "QuotaAppliedAtLevel": "ACCOUNT",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-076D529E",
 "Unit": "None",
 },
 {
 "QuotaName": "Dedicated master instances per domain",
 "Adjustable": false,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-AE676A72",
 "Value": 5.0,
 "QuotaAppliedAtLevel": "ACCOUNT",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-AE676A72",
 "Unit": "None",
 },
 {
 "QuotaName": "Warm instances per domain",
 "Adjustable": false,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-1F053E6F",
 "Value": 150.0,
 "QuotaAppliedAtLevel": "ACCOUNT",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-1F053E6F",
 "Unit": "None",
 },
 {
 "QuotaName": "Instances per domain",
 "Adjustable": true,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
 "Value": 80.0,
 "QuotaAppliedAtLevel": "ACCOUNT",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-6408ABDE",
 "Unit": "None",
 "QuotaContext": {
 "ContextScope": "RESOURCE",
 "ContextScopeType": "AWS::OpenSearchService::Domain",
 "ContextId": "*"
 }
 }
 ]
}`
```
