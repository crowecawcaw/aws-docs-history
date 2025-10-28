# Excluding service quotas from Service Quotas Automatic Management

You won't be notified of service quotas utilizations for AWS services added to the
Automatic Management exclusion list.

You can exclude a service quota or list of quotas from being monitored by Automatic Management using the
`--exclusion-list`. You'll need the service code and quota code to
exclude the quota from Automatic Management in the AWS CLI.

Use the following procedure to exclude quotas from Automatic Management monitoring for your
AWS account using either the AWS Management Console or AWS CLI.

AWS Management Console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, select
   **Automatic Management**.
3. Under **Selected quotas for exceptions**, add the
   AWS services you do not want monitored with Automatic Management. After
   making your selection, choose **Add exceptions**.

AWS CLI
See the following AWS CLI examples for adding supported AWS services to
the Automatic Management exclusion list. You'll need to include the AWS service
code and Service Quotas code in your commands.

- **Finding supported AWS services code**
  - Use [ListServices](../../2019-06-24/apireference/API_ListServices.md "../../2019-06-24/apireference/API_ListServices.md") to list
    AWS services supported by Service Quotas. The response includes the
    `ServiceCode` and `ServiceName`
    for each service. For example, the `ServiceCode`
    for Amazon DynamoDB is `dynamodb`.

- **Finding Service Quotas codes**
  - Use [ListServiceQuotas](../../2019-06-24/apireference/API_ListServiceQuotas.md "../../2019-06-24/apireference/API_ListServiceQuotas.md") to list AWS services Service Quotas
    codes. You can specify the service with the request
    parameter `ServiceCode`. The response includes
    the `QuotaName`, `QuotaCode`,
    `Value`, and
    `QuotaAppliedAtLevel`.

###### Example Starts Automatic Management and excludes Amazon DynamoDB quota

The following example both starts Automatic Management and excludes DynamoDB as a
service quota that will not be monitored with Automatic Management. Replace the
`italicized placeholder text` in the
example command with your information.

```
aws service-quotas start-auto-management \
  --opt-in-level ACCOUNT \
  --opt-in-type NotifyOnly \
  --region `ca-central-1` \
  --exclusion-list '{"`dynamodb`":["`L-E123ABC4`"]}'
```

###### Example Exclude Amazon DynamoDB quota from Automatic Management

The following example excludes DynamoDB from Automatic Management for an
AWS account in the Canada (Central) AWS Region. Replace the
`italicized placeholder text` in the
example command with your information.

```
aws service-quotas update-auto-management \
  --opt-in-type NotifyOnly \
  --region `ca-central-1` \
  --exclusion-list '{"`dynamodb`":["`L-E123ABC4`"]}'
```
