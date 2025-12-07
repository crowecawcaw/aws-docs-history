# Service Quotas Automatic Management AWS CloudTrail logs

The following are AWS CloudTrail logs for Automatic Management critical and non-critical events.

## Critical

The following is an example of an EventBridge event for Automatic Management. This
event shows the utilization for AWS CloudTrail and is a critical event where you'd
receive notification.

```
{
    "version": "0",
    "id": "97c1eb9w-0f16-f3d5-b0d6-d6b8d6614315",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "************",
    "time": "2025-09-12T02:18:36Z",
    "region": "ca-central-1",
    "resources": ["Service: cloudtrail | Quota Name: Trails per region | Utilization: 80.0%"],
    "detail": {
        "eventArn": "arn:aws:health:ca-central-1::event/SERVICEQUOTAS/AWS_SERVICEQUOTAS_THRESHOLD_BREACH/AWS_SERVICEQUOTAS_THRESHOLD_BREACH-YUL-1757643474686",
        "service": "SERVICEQUOTAS",
        "eventTypeCode": "AWS_SERVICEQUOTAS_THRESHOLD_BREACH",
        "eventTypeCategory": "accountNotification",
        "eventScopeCode": "ACCOUNT_SPECIFIC",
        "communicationId": "a26c337bff88e2bcb6ec65835dda2152ec3f870926433ccf6c871712ed655221-1",
        "startTime": "Fri, 12 Sep 2025 02:17:54 GMT",
        "lastUpdatedTime": "Fri, 12 Sep 2025 02:17:54 GMT",
        "statusCode": "open",
        "eventRegion": "ca-central-1",
        "eventDescription": [{
            "language": "en_US",
            "latestDescription": "You are receiving this message because you opted to receive notifications from Service Quotas when utilization exceeds (80/95)% threshold.\n\nAt Fri, 12 Sep 2025 02:17:54 GMT, we detected that this AWS account has reached the utilization threshold for one or more service quotas.\n\nA list of your affected service quota(s) can be found in the \"Affected resources\" tab of your AWS Health Dashboard under the format \"Service | Quota Name | Utilization Pe Percentage\".\n\nFor unchangeable or non-adjustable quotas, we recommend designing your architecture for applications and services to prevent these limits from impacting reliability as per the AWS well architected framework.\nPlease refer to AWS Well-Architected document (1) for details.\n\nIf you have any questions or concerns, please contact the AWS Support Team (2).\n\n(1) https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/rel_manage_service_limits_aware_fixed_limits.html\n(2) https://aws.amazon.com/support"
        }],
        "affectedEntities": [{
            "entityValue": "Service: cloudtrail | Quota Name: Trails per region | Utilization: 80.0%",
            "lastUpdatedTime": "Fri, 12 Sep 2025 02:17:54 GMT"
        }],
        "affectedAccount": "111122223333",
        "page": "1",
        "totalPages": "1"
    }}
```

## Non-critical

The following is an example of an EventBridge event for Automatic Management. This
event shows the utilization for Amazon DynamoDB and is a non-critical event. This
event is sent to CloudTrail.

```
{
    "version": "0",
    "id": "ecf5de2a-0c6e-6627-761e-a60a482f0d00",
    "detail-type": "AWS Service Event via CloudTrail",
    "source": "aws.servicequotas",
    "account": "************",
    "time": "2025-09-12T08:19:07Z",
    "region": "ca-central-1",
    "resources": [],
    "detail": {
        "eventVersion": "1.10",
        "userIdentity": {
            "accountId": "555555555555",
            "invokedBy": "servicequotas.amazonaws.com"
        },
        "eventTime": "2025-09-12T08:19:07Z",
        "eventSource": "servicequotas.amazonaws.com",
        "eventName": "ServiceQuotasUtilizationBreachingThreshold",
        "awsRegion": "ca-central-1",
        "sourceIPAddress": "servicequotas.amazonaws.com",
        "userAgent": "servicequotas.amazonaws.com",
        "requestParameters": null,
        "responseElements": null,
        "eventID": "ee20d580-8015-4c20-bd6d-ef53b969aefb",
        "readOnly": false,
        "eventType": "AwsServiceEvent",
        "managementEvent": true,
        "recipientAccountId": "555555555555",
        "serviceEventDetails": {
            "action": "NOTIFY_ONLY",
            "created": "Fri Sep 12 08:19:07 UTC 2025",
            "serviceCode": "dynamodb",
            "requester": "339712738202",
            "quotaCode": "L-F98FE922",
            "quotaName": "Maximum number of tables",
            "utilizationValue": "2500.0",
            "breachingThreshold": "95",
            "adjustability": "Adjustable",
            "quotaArn": "arn:aws:servicequotas:ca-central-1:555555555555:dynamodb/L-F98FE922"
        },
        "eventCategory": "Management"
    }}
```
