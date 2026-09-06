

# Notify quotas and limits
<a name="notify-quotas"></a>

This section describes the default quotas, rate limits, and supported countries for Notify.

## Account-level quotas
<a name="notify-quotas-account"></a>


**Account-level quotas**  

| Quota | Default value | Adjustable | 
| --- | --- | --- | 
| Notify configurations per account | 25 | Yes | 
| Messages to a single destination phone number per day (account-wide) | 10 | No | 

## Configuration-level limits
<a name="notify-quotas-configuration"></a>


**Configuration-level limits by tier**  

| Limit | Basic tier | Advanced tier | 
| --- | --- | --- | 
| Messages per day | 200 | Unlimited | 
| TPS per configuration | 1 | 25 | 
| Supported countries | 30 pre-approved | All supported\* | 

**Note**  
For a given destination phone number, the limit is 10 messages per day per notify configuration and 10 messages per day per account.

\* Some countries require a customer-owned origination identity. Use the `ListNotifyCountries` API to check which countries require customer-owned identities. For more information, see [Notify supported countries](notify-countries.md).

## API rate limits
<a name="notify-quotas-api"></a>


**API rate limits**  

| API operation | Default RPS | 
| --- | --- | 
| CreateNotifyConfiguration | 1 | 
| UpdateNotifyConfiguration | 1 | 
| DeleteNotifyConfiguration | 1 | 
| DescribeNotifyConfigurations | 1 | 
| DescribeNotifyTemplates | 1 | 
| ListNotifyCountries | 1 | 
| SendNotifyTextMessage | 1 (Basic) / 25 (Advanced) | 
| SendNotifyVoiceMessage | 1 (Basic) / 25 (Advanced) | 
| SetNotifyMessageSpendLimitOverride | 1 | 
| DeleteNotifyMessageSpendLimitOverride | 1 | 

## Requesting quota increases
<a name="notify-quotas-increase"></a>

To request an increase to any Notify quota:

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/).

1. Navigate to **AWS End User Messaging SMS**.

1. Select the quota you want to increase.

1. Choose **Request quota increase**.

Alternatively, you can create a support case at the [AWS Support Center](https://console.aws.amazon.com/support/home).