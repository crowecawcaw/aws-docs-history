# Requesting a quota increase

For adjustable quotas, you can request a quota increase at
the _account-level_ or the _resource-level_. Smaller increases are usually
automatically approved while larger requests are submitted to Support. Larger increase requests take time to review,
process, approve, and deploy. You can track your request case in the Support console.

###### Note

Quota increase requests don't receive priority support. Support can approve, deny,
or partially approve your requests. If you have an urgent quota request, or if your quota
increase request is denied, contact Support for assistance.

## Using the AWS Management Console to request

an increase

Increase your quotas at the account or resource level in the [Getting Started with the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md "../../../awsconsolehelpdocs/latest/gsg/getting-started.md").

###### To request a service quota increase

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home").
2. In the navigation pane, choose **AWS services**.
3. Choose an AWS service from the list, or enter the name of the service in the
   search box.
4. If the quota is adjustable, you can request a quota increase at either the
   account-level or resource-level based on the value listed in the
   **Adjustability** column.
   - **Account-level** – Request a
     quota increase at the account-level for an account-level quota such as
     `Domains per Region` for Amazon OpenSearch Service. To do so, select the
     quota from the list and choose **Request increase at
     account-level**.
   - **Resource-level** – Request a
     quota increase for a specific resource for a resource-level quota such
     as `Instances per domain` for Amazon OpenSearch Service. To do so, choose
     the quota name to view additional information about the quota. Under the
     **Resource-level quotas** section, select the
     resource for which you want to increase the quota value, and choose the
     **Request increase at resource-level** button.

5. For **Increase quota value**, enter the new value. The new
   value must be greater than the current value.
6. Choose **Request**.
7. To view any pending or recently resolved requests in the console, navigate to
   the **Request history** tab from the service's details page, or
   choose **Dashboard** from the navigation pane. For pending
   requests, choose the status of the request to open the request receipt. The
   initial status of a request is **Pending**. After the status
   changes to **Quota requested**, you'll see the case number with
   Support. Choose the case number to open the ticket for your request.

## Using the AWS CLI to request a quota

increase

Requesting a quota increase using the AWS CLI requires you to provide
Service Quotas with the necessary permission to create a support case on your behalf. You can provide this permission by
attaching the [AWS managed policy](identity-access-management.md#predefined-policies "identity-access-management.md#predefined-policies") `ServiceQuotasFullAccess` to your IAM principal
or adding `iam:CreateServiceLinkedRole` [to your existing IAM policy.](identity-access-management.md#iam-policies "identity-access-management.md#iam-policies")

Account-level increase request AWS CLI

###### To request a quota increase at the account-level

The `RequestServiceQuotaIncrease` operation, which submits
the request, requires the quota code for the quota. So begin by getting
the quota code.

The following example commands show how to request a quota increase at
the account-level for the Amazon OpenSearch Service.

1. Get the list of services supported by Service Quotas with the [ListServices](../../2019-06-24/apireference/API_ListServices.md "../../2019-06-24/apireference/API_ListServices.md") operation. The response includes the
   `ServiceCode` and `ServiceName` for each
   service. The `ServiceCode` for Amazon OpenSearch Service is
   `es`.
2. Get the list of Amazon OpenSearch Service quotas and their corresponding applied
   quota values at the account-level by calling the [ListServiceQuotas](../../2019-06-24/apireference/API_ListServiceQuotas.md "../../2019-06-24/apireference/API_ListServiceQuotas.md") operation with request parameters
   `ServiceCode` as `es`, and
   `QuotaAppliedAtLevel` as `ACCOUNT`. The
   response includes the `QuotaName`,
   `QuotaCode`, `Value`, and
   `QuotaAppliedAtLevel` for each quota of the Amazon OpenSearch Service
   that is applied at the account-level. If the value in the
   `QuotaAppliedAtLevel` field is `ACCOUNT`,
   then the `Value` represents the Applied quota value at
   the account-level. The following CLI example retrieves the quota
   code for a OpenSearch Service quota.

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
 ]
}`
```

3. Next, call the [RequestServiceQuotaIncrease](../../2019-06-24/apireference/API_RequestServiceQuotaIncrease.md "../../2019-06-24/apireference/API_RequestServiceQuotaIncrease.md") operation and specify the
   `QuotaCode` in the request parameter.

The following example requests an increase at the account-level in
the `Instances per domain` quota to `100`. It
uses the required quota code, `L-6408ABDE`, to identify
the quota. If the command completes successfully, the
`Status` field in the response displays the current
status of the request. The `QuotaRequestedAtLevel` field
in the response specifies that this request applies to the
account-level.

###### Note

You can't request a quota increase at the account-level for a
resource-level quota through the AWS CLI. This operation results
in the creation of a support case where you can provide the ARN
to specify the resource on which the new quota value should
apply. However, the `Instances per domain` quota for
Amazon OpenSearch Service is an exception.

```
`$` `aws service-quotas request-service-quota-increase \
 --service-code es \
 --quota-code L-6408ABDE \
 --desired-value 100``{
 "RequestedQuota": {
 "QuotaName": "Instances per domain",
 "Status": "PENDING",
 "DesiredValue": 100,
 "Created": 1580446904.067,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-6408ABDE",
 "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}",
 "QuotaRequestedAtLevel": "ACCOUNT"
 "Id": "a12345",
 "Unit": "None"
 "QuotaContext": {
 "ContextId": "*"
 "ContextScopeType": "AWS::OpenSearchService::Domain",
 "ContextScope": "RESOURCE",
 }
 }
}`
```

4. To get the updated status of the request, use the [GetRequestedServiceQuotaChange](../../2019-06-24/apireference/API_GetRequestedServiceQuotaChange.md "../../2019-06-24/apireference/API_GetRequestedServiceQuotaChange.md"), [ListRequestedServiceQuotaChangeHistory](../../2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.md "../../2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.md") or [ListRequestedServiceQuotaChangeHistoryByQuota](../../2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistoryByQuota.md "../../2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistoryByQuota.md")
   operations.

Resource-level quota increase request AWS CLI

###### To request a quota increase at the resource-level

The `RequestServiceQuotaIncrease` operation, which submits
the request, requires the quota code for the quota. So begin by getting
the quota code. To request a quota increase for a specific resource, use
the Amazon Resource Name (ARN) `ResourceARN` as the value for
the `ContextId` parameter when you make your request.

The following example commands show how to request a resource-level
quota increase for the OpenSearch Service.

1. Get the list of services supported by Service Quotas with the [ListServices](../../2019-06-24/apireference/API_ListServices.md "../../2019-06-24/apireference/API_ListServices.md") operation. The response includes the
   `ServiceCode` and `ServiceName` for each
   service. The `ServiceCode` for Amazon OpenSearch Service is
   `es`.
2. Get the list of Amazon OpenSearch Service quotas and their corresponding applied
   quota values at the resource-level by calling the [ListServiceQuotas](../../2019-06-24/apireference/API_ListServiceQuotas.md "../../2019-06-24/apireference/API_ListServiceQuotas.md") operation with request parameters
   `ServiceCode` as `es`, and
   `QuotaAppliedAtLevel` as `RESOURCE`. The
   response includes the `QuotaName`,
   `QuotaCode`, `Value`, and
   `QuotaAppliedAtLevel` for each quota of the Amazon OpenSearch Service
   that is applied at the resource-level. If the value in the
   `QuotaAppliedAtLevel` field is `RESOURCE`,
   then the `Value` represents the Applied quota value at
   the resource-level. In this case, the response for this quota will
   also contain the `QuotaContext` structure which further
   specifies the `ContextId` or the ARN to which the quota
   value is applied. The following CLI example retrieves the quota code
   for a OpenSearch Service quota.

```
`$` `aws service-quotas list-service-quotas \
 --service-code es \
 --quota-applied-at-level RESOURCE``{
 "Quotas": [
 {
 "QuotaName": "Instances per domain",
 "Adjustable": true,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
 "Value": 100.0,
 "QuotaAppliedAtLevel": "RESOURCE",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-6408ABDE",
 "Unit": "None",
 "QuotaContext": {
 "ContextScope": "RESOURCE",
 "ContextScopeType": "AWS::OpenSearchService::Domain",
 "ContextId": "arn:aws:esus-east-1:123456789012:domain/opensearch-domain-1",
 }
 },
 {
 "QuotaName": "Instances per domain",
 "Adjustable": true,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
 "Value": 100.0,
 "QuotaAppliedAtLevel": "RESOURCE",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-6408ABDE",
 "Unit": "None",
 "QuotaContext": {
 "ContextScope": "RESOURCE",
 "ContextScopeType": "AWS::OpenSearchService::Domain",
 "ContextId": "arn:aws:esus-east-1:123456789012:domain/opensearch-domain-2",
 }
 }
 ]
}`
```

3. Next, call the [RequestServiceQuotaIncrease](../../2019-06-24/apireference/API_RequestServiceQuotaIncrease.md "../../2019-06-24/apireference/API_RequestServiceQuotaIncrease.md") operation and specify the
   `ServiceCode`, `QuotaCode`,
   `ContextId`, and `DesiredValue` request
   parameters.

The following example requests an increase in the `Instances
 per domain` quota to `100` for a specific
Amazon OpenSearch Service domain with the ARN as
arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-1.
If the command completes successfully, the `Status` field
in the response displays the current status of the request.
`QuotaRequestedAtLevel` field in the response
contains the value `RESOURCE` which specifies that this
request is for a specific resource.

```
`$` `aws service-quotas request-service-quota-increase \
 --service-code es \
 --quota-code L-6408ABDE \
 --desired-value 200 \
 --context-id arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-1``{
 "RequestedQuota": {
 "QuotaName": "Instances per domain",
 "Status": "PENDING",
 "DesiredValue": 200.0,
 "Created": 1580446904.067,
 "QuotaArn": "arn:aws:servicequotas:us-east-1:123456789012:es/L-6408ABDE",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-6408ABDE",
 "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}",
 "QuotaRequestedAtLevel": "RESOURCE",
 "Id": "a12345",
 "Unit": "None"
 "QuotaContext": {
 "ContextId": "arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-1"
 "ContextScopeType": "AWS::OpenSearchService::Domain",
 "ContextScope": "RESOURCE",
 }
 }
}`
```

4. To get the updated status of the request, use the [GetRequestedServiceQuotaChange](../../2019-06-24/apireference/API_GetRequestedServiceQuotaChange.md "../../2019-06-24/apireference/API_GetRequestedServiceQuotaChange.md"), [ListRequestedServiceQuotaChangeHistory](../../2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.md "../../2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.md") or [ListRequestedServiceQuotaChangeHistoryByQuota](../../2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistoryByQuota.md "../../2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistoryByQuota.md")
   operations.

After the request is resolved, the **Applied quota value** for the
quota is set to the new value.
