

# AWS IoT Device Defender endpoints and quotas
<a name="iot_device_defender"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="iot_device_defender_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  iot.us-east-2.amazonaws.com <br /> iot-fips.us-east-2.api.aws <br /> iot-fips.us-east-2.amazonaws.com <br /> iot.us-east-2.api.aws  | https<br />HTTPS<br />https<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  iot.us-east-1.amazonaws.com <br /> iot-fips.us-east-1.api.aws <br /> iot-fips.us-east-1.amazonaws.com <br /> iot.us-east-1.api.aws  | https<br />HTTPS<br />https<br />HTTPS | 
| US West (N. California) | us-west-1 |  iot.us-west-1.amazonaws.com <br /> iot-fips.us-west-1.api.aws <br /> iot-fips.us-west-1.amazonaws.com <br /> iot.us-west-1.api.aws  | https<br />HTTPS<br />https<br />HTTPS | 
| US West (Oregon) | us-west-2 |  iot.us-west-2.amazonaws.com <br /> iot-fips.us-west-2.api.aws <br /> iot-fips.us-west-2.amazonaws.com <br /> iot.us-west-2.api.aws  | https<br />HTTPS<br />https<br />HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  iot.ap-east-1.amazonaws.com <br /> iot.ap-east-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  iot.ap-southeast-5.amazonaws.com <br /> iot.ap-southeast-5.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  iot.ap-south-1.amazonaws.com <br /> iot.ap-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  iot.ap-northeast-2.amazonaws.com <br /> iot.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  iot.ap-southeast-1.amazonaws.com <br /> iot.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  iot.ap-southeast-2.amazonaws.com <br /> iot.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  iot.ap-northeast-1.amazonaws.com <br /> iot.ap-northeast-1.api.aws  | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  iot.ca-central-1.amazonaws.com <br /> iot-fips.ca-central-1.api.aws <br /> iot-fips.ca-central-1.amazonaws.com <br /> iot.ca-central-1.api.aws  | https<br />HTTPS<br />https<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  iot.eu-central-1.amazonaws.com <br /> iot.eu-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  iot.eu-west-1.amazonaws.com <br /> iot.eu-west-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  iot.eu-west-2.amazonaws.com <br /> iot.eu-west-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Paris) | eu-west-3 |  iot.eu-west-3.amazonaws.com <br /> iot.eu-west-3.api.aws  | HTTPS<br />HTTPS | 
| Europe (Spain) | eu-south-2 |  iot.eu-south-2.amazonaws.com <br /> iot.eu-south-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Stockholm) | eu-north-1 |  iot.eu-north-1.amazonaws.com <br /> iot.eu-north-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (Bahrain) | me-south-1 |  iot.me-south-1.amazonaws.com <br /> iot.me-south-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (UAE) | me-central-1 |  iot.me-central-1.amazonaws.com <br /> iot.me-central-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  iot.us-gov-east-1.amazonaws.com <br /> iot-fips.us-gov-east-1.api.aws <br /> iot-fips.us-gov-east-1.amazonaws.com <br /> iot.us-gov-east-1.api.aws  | https<br />HTTPS<br />https<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  iot.us-gov-west-1.amazonaws.com <br /> iot-fips.us-gov-west-1.api.aws <br /> iot-fips.us-gov-west-1.amazonaws.com <br /> iot.us-gov-west-1.api.aws  | https<br />HTTPS<br />https<br />HTTPS | 

## Service quotas
<a name="iot_device_defender_quotas"></a>


**AWS IoT Device Defender audits limits and quotas**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[Scheduled audits](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-0D30EFBA)` | The maximum number of scheduled audits. | 5 | No | 
| `[Simultaneous in progress on-demand audits](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-1EF777B4)` | The maximum number of simultaneous in progress on-demand audits. | 10 | No | 
| `[Storage duration for audit findings](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-F5608FF9)` | The maximum time, in days, that audit findings are stored after being reported. | 90 | No | 

The following service quotas apply to mitigation actions and audit mitigation action tasks:


**AWS IoT Device Defender mitigation limits and quotas**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[Mitigation actions](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-1A084077)` | The maximum number of mitigation actions. | 100 | No | 


**Audit mitigation action limits**  

| Resource | Limit | 
| --- | --- | 
| Number of audit mitigation action tasks running at the same time | 10 tasks | 
| Retention period for audit mitigation action tasks | 90 days | 


**AWS IoT Device Defender detect limits and quotas**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[Behavior metric value elements for each security profile](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-971FA845)` | The maximum number of behavior metric value elements (counts, IP addresses, ports) for each security profile. | 1000 | No | 
| `[Behaviors for each security profile](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-2F1C9734)` | The maximum number of behaviors for each security profile | 100 | No | 
| `[Custom metrics](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-53A90E98)` | The maximum number of detect custom metrics. | 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-53A90E98) | 
| `[Device metric minimum delay](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-7BF41710)` | The minimum time, in seconds, that a device must wait between sending metric reports. | 300 Seconds | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-7BF41710) | 
| `[Device metric peak reporting rate for an account](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-9AE67DFC)` | The maximum number of device-side metric reports that can be sent, per second, from all devices in an account. | 3500 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-9AE67DFC) | 
| `[Metric dimensions](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-8B5F47E6)` | The maximum number of detect metric dimensions. | 10 | No | 
| `[Security profiles for each target](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-FF03CD81)` | The maximum number of security profiles for each target (things or thing groups in the AWS account). | 5 | No | 
| `[Storage duration for detect metrics](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-2B367AAD)` | The maximum time, in days, that detect metrics are stored after being ingested. | 14 | No | 
| `[Storage duration for detect violations](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-C8D2DE05)` | The maximum time, in days, that detect violations are stored after being generated. | 30 | No | 


**ML Detect limits**  

| Resource | Quota | Adjustable | 
| --- | --- | --- | 
| Number of Detect mitigation action tasks that can be running at the same time | 5 maximum | [Yes](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-iot) | 
| Retention period for Detect mitigation action tasks | 90 days maximum | [Yes](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-iot) | 
| Retention period for models (time after which models are expired) | 30 days maximum | No | 

**AWS IoT Device Defender API throttling limits**  
This table describes the maximum number of transactions per second (TPS) that can be made to each of these AWS IoT Device Defender API actions.


**AWS IoT Device Defender API throttling limits**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[AttachSecurityProfile API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-E9111144)` | The maximum number of transactions per second (TPS) that can be made for the AttachSecurityProfile API. | 10 | No | 
| `[CancelAuditMitigationActionsTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-03D9A452)` | The maximum number of transactions per second (TPS) that can be made for the CancelAuditMitigationActionsTask API. | 10 | No | 
| `[CancelAuditTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-3AA926CF)` | The maximum number of transactions per second (TPS) that can be made for the CancelAuditTask API. | 10 | No | 
| `[CancelDetectMitigationActionsTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-13B49C07)` | The maximum number of transactions per second (TPS) that can be made for the CancelDetectMitigationActionsTask API. | 10 | No | 
| `[CreateAuditSuppression API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-0C3BA39D)` | The maximum number of transactions per second (TPS) that can be made for the CreateAuditSuppression API. | 10 | No | 
| `[CreateCustomMetric API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-E68D12E6)` | The maximum number of transactions per second (TPS) that can be made for the CreateCustomMetric API. | 10 | No | 
| `[CreateMitigationAction API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-EFA916AE)` | The maximum number of transactions per second (TPS) that can be made for the CreateMitigationAction API. | 10 | No | 
| `[CreateScheduledAudit API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-60251A2B)` | The maximum number of transactions per second (TPS) that can be made for the CreateScheduledAudit API. | 5 | No | 
| `[CreateSecurityProfile API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-A2577F1F)` | The maximum number of transactions per second (TPS) that can be made for the CreateSecurityProfile API. | 10 | No | 
| `[DeleteAccountAuditConfiguration API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-C6AA7145)` | The maximum number of transactions per second (TPS) that can be made for the DeleteAccountAuditConfiguration API. | 5 | No | 
| `[DeleteAuditSuppression API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-E70CF14E)` | The maximum number of transactions per second (TPS) that can be made for the DeleteAuditSuppression API. | 10 | No | 
| `[DeleteCustomMetric API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-CD7FC91A)` | The maximum number of transactions per second (TPS) that can be made for the DeleteCustomMetric API. | 10 | No | 
| `[DeleteDimension API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-C002DA39)` | The maximum number of transactions per second (TPS) that can be made for the DeleteDimension API. | 10 | No | 
| `[DeleteMitigationAction API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-5C712B10)` | The maximum number of transactions per second (TPS) that can be made for the DeleteMitigationAction API. | 10 | No | 
| `[DeleteScheduledAudit API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-7C0B717A)` | The maximum number of transactions per second (TPS) that can be made for the DeleteScheduledAudit API. | 5 | No | 
| `[DeleteSecurityProfile API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-A6ABB02F)` | The maximum number of transactions per second (TPS) that can be made for the DeleteSecurityProfile API. | 10 | No | 
| `[DescribeAccountAuditConfiguration API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-01C40691)` | The maximum number of transactions per second (TPS) that can be made for the DescribeAccountAuditConfiguration API. | 5 | No | 
| `[DescribeAuditFinding API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-6A19A60F)` | The maximum number of transactions per second (TPS) that can be made for the DescribeAuditFinding API. | 25 | No | 
| `[DescribeAuditMitigationActionsTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-32F19277)` | The maximum number of transactions per second (TPS) that can be made for the DescribeAuditMitigationActionsTask API. | 25 | No | 
| `[DescribeAuditSuppression API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-ADA44585)` | The maximum number of transactions per second (TPS) that can be made for the DescribeAuditSuppression API. | 10 | No | 
| `[DescribeAuditTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-146D20C5)` | The maximum number of transactions per second (TPS) that can be made for the DescribeAuditTask API. | 25 | No | 
| `[DescribeCustomMetric API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-6F3753D8)` | The maximum number of transactions per second (TPS) that can be made for the DescribeCustomMetric API. | 25 | No | 
| `[DescribeDetectMitigationActionsTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-DCAEF14C)` | The maximum number of transactions per second (TPS) that can be made for the DescribeDetectMitigationActionsTask API. | 10 | No | 
| `[DescribeDimension API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-002E66AE)` | The maximum number of transactions per second (TPS) that can be made for the DescribeDimension API. | 10 | No | 
| `[DescribeMitigationAction API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-145287EF)` | The maximum number of transactions per second (TPS) that can be made for the DescribeMitigationAction API. | 25 | No | 
| `[DescribeScheduledAudit API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-42A0EE7E)` | The maximum number of transactions per second (TPS) that can be made for the DescribeScheduledAudit API. | 5 | No | 
| `[DescribeSecurityProfile API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-8AEAB7FE)` | The maximum number of transactions per second (TPS) that can be made for the DescribeSecurityProfile API. | 25 | No | 
| `[DetachSecurityProfile API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-CF4F23BC)` | The maximum number of transactions per second (TPS) that can be made for the DetachSecurityProfile API. | 10 | No | 
| `[ListActiveViolations API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-6891CC02)` | The maximum number of transactions per second (TPS) that can be made for the ListActiveViolations API. | 10 | No | 
| `[ListAuditFindings API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-0321A666)` | The maximum number of transactions per second (TPS) that can be made for the ListAuditFindings API. | 10 | No | 
| `[ListAuditMitigationActionsExecutions API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-C6D7A02D)` | The maximum number of transactions per second (TPS) that can be made for the ListAuditMitigationActionsExecutions API. | 10 | No | 
| `[ListAuditMitigationActionsTasks API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-08C28D29)` | The maximum number of transactions per second (TPS) that can be made for the ListAuditMitigationActionsTasks API. | 10 | No | 
| `[ListAuditSuppressions API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-9227E25C)` | The maximum number of transactions per second (TPS) that can be made for the ListAuditSuppressions API. | 10 | No | 
| `[ListAuditTasks API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-B78A9E08)` | The maximum number of transactions per second (TPS) that can be made for the ListAuditTasks API. | 10 | No | 
| `[ListCustomMetrics API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-D45EEF28)` | The maximum number of transactions per second (TPS) that can be made for the ListCustomMetrics API. | 10 | No | 
| `[ListDetectMitigationActionsExecutions API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-8D3E8509)` | The maximum number of transactions per second (TPS) that can be made for the ListDetectMitigationActionsExecutions API. | 10 | No | 
| `[ListDetectMitigationActionsTasks API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-D18738F6)` | The maximum number of transactions per second (TPS) that can be made for the ListDetectMitigationActionsTasks API. | 10 | No | 
| `[ListDimensions API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-0A17A254)` | The maximum number of transactions per second (TPS) that can be made for the ListDimensions API. | 10 | No | 
| `[ListMetricValues API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-DC1637B1)` | The maximum number of transactions per second (TPS) that can be made for the ListMetricValues API. | 15 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-DC1637B1) | 
| `[ListMitigationActions API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-62C55F58)` | The maximum number of transactions per second (TPS) that can be made for the ListMitigationActions API. | 10 | No | 
| `[ListScheduledAudits API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-016FB677)` | The maximum number of transactions per second (TPS) that can be made for the ListScheduledAudits API. | 5 | No | 
| `[ListSecurityProfiles API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-DACF0EDE)` | The maximum number of transactions per second (TPS) that can be made for the ListSecurityProfiles API. | 10 | No | 
| `[ListSecurityProfilesForTarget API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-9299DD15)` | The maximum number of transactions per second (TPS) that can be made for the ListSecurityProfilesForTarget API. | 10 | No | 
| `[ListTargetsForSecurityProfile API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-014BF26E)` | The maximum number of transactions per second (TPS) that can be made for the ListTargetsForSecurityProfile API. | 10 | No | 
| `[ListViolationEvents API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-56E94C1D)` | The maximum number of transactions per second (TPS) that can be made for the ListViolationEvents API. | 10 | No | 
| `[PutVerificationStateOnViolation API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-46522656)` | The maximum number of transactions per second (TPS) that can be made for the PutVerificationStateOnViolation API. | 10 | No | 
| `[StartAuditMitigationActionsTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-81189B2F)` | The maximum number of transactions per second (TPS) that can be made for the StartAuditMitigationActionsTask API. | 10 | No | 
| `[StartDetectMitigationActionsTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-670D7C85)` | The maximum number of transactions per second (TPS) that can be made for the StartDetectMitigationActionsTask API. | 10 | No | 
| `[StartOnDemandAuditTask API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-471C1537)` | The maximum number of transactions per second (TPS) that can be made for the StartOnDemandAuditTask API. | 10 | No | 
| `[UpdateAccountAuditConfiguration API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-F62705AB)` | The maximum number of transactions per second (TPS) that can be made for the UpdateAccountAuditConfiguration API. | 5 | No | 
| `[UpdateAuditSuppression API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-CA8BDEFC)` | The maximum number of transactions per second (TPS) that can be made for the UpdateAuditSuppression API. | 10 | No | 
| `[UpdateCustomMetric API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-ABC0EA56)` | The maximum number of transactions per second (TPS) that can be made for the UpdateCustomMetric API. | 10 | No | 
| `[UpdateDimension API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-68A50D88)` | The maximum number of transactions per second (TPS) that can be made for the UpdateDimension API. | 10 | No | 
| `[UpdateMitigationAction API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-1CB31CD2)` | The maximum number of transactions per second (TPS) that can be made for the UpdateMitigationAction API. | 10 | No | 
| `[UpdateScheduledAudit API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-211671C6)` | The maximum number of transactions per second (TPS) that can be made for the UpdateScheduledAudit API. | 5 | No | 
| `[UpdateSecurityProfile API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-2145354D)` | The maximum number of transactions per second (TPS) that can be made for the UpdateSecurityProfile API. | 10 | No | 
| `[ValidateSecurityProfileBehaviors API TPS](https://console.aws.amazon.com/servicequotas/home/services/iot/quotas/L-88D87918)` | The maximum number of transactions per second (TPS) that can be made for the ValidateSecurityProfileBehaviors API. | 10 | No | 