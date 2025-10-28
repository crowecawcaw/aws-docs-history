# Verifying your quota request

Verify your quota request by viewing the request history history in the Service Quotas console.
The console displays all open quota requests and requests closed in the last year.

###### Note

Some AWS services may only be available in certain AWS Regions. If you have quota
increase requests in different Regions, be sure to select the appropriate Region
first.

Using the AWS Management Console

###### To view the quota request history

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home").
2. To view any pending or recently resolved requests, choose
   **Quota request history** from the navigation
   pane.

The **Recent quota increase requests** panel displays
information about your open recent quota increase requests and any requests
closed within the last year.

- **Service** – Displays the service name
  selected for the request.
- **Quota name** – Displays the quota name
  selected for the quota increase.
- **Status** – Displays the status of a
  request for a quota increase.

You may see the following status types:

    + **Pending** – Quota increase
     request is under review by AWS.
    + **Case opened** – Service Quotas has opened
     a support case to process the request.
    + **Approved** – Quota increase
     request is approved.
    + **Rejected** – Quota increase
     request can't be approved by Service Quotas. Contact Support for
     more details.
    + **Case closed** – The support case
     associated with this request was closed. View the support
     case correspondence for more information.
    + **Request not valid** – Service Quotas can't
     process your resource-level quota increase request because
     the `ResourceARN` specified as part of the
     `ContextId` attribute is not valid.

- **Requested quota value** – The increased
  quota value you requested for the quota.
- **Request date** – The date you requested
  the quota increase.
- **Last updated date** – The last date the
  request received an update.

View details about a service, quota name, and status in the
**Quota request history** table by choosing one of the
entries.

Using AWS CLI

###### To view the quota request history

- The `ListRequestedServiceQuotaChangeHistory` operation,
  which submits the request, requires a
  `QuotaRequestedAtLevel` parameter. The following CLI
  example is for all resource and account level requests.

```
`$` `aws service-quotas list-requested-service-quota-change-history \
 --quota-applied-at-level ALL``{
 "RequestedQuotas": [
 {
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
 "ContextScope": "RESOURCE"
 }
 },
 {
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
 "ContextId": "arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-2",
 "ContextScopeType": "AWS::OpenSearchService::Domain",
 "ContextScope": "RESOURCE"
 }
 },
 {
 "QuotaName": "Domains per Region",
 "Status": "PENDING",
 "DesiredValue": 120.0,
 "Created": 1580446904.067,
 "Adjustable": true,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-076D529E",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-076D529E",
 "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}"
 "QuotaRequestedAtLevel": "ACCOUNT",
 "Id": "a123456",
 "Unit": "None",
 },
 {
 "QuotaName": "Instances per domain",
 "Status": "PENDING"
 "DesiredValue": 300.0,
 "Created": 1580446904.067,
 "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
 "ServiceName": "Amazon OpenSearch Service",
 "GlobalQuota": false,
 "ServiceCode": "es",
 "QuotaCode": "L-6408ABDE",
 "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}"
 "QuotaRequestedAtLevel": "ACCOUNT",
 "Id": "a1234567",
 "Unit": "None",
 "QuotaContext": {
 "ContextId": "*",
 "ContextScopeType": "AWS::OpenSearchService::Domain",
 "ContextScope": "RESOURCE"
 }
 }
 ]
}`
```
