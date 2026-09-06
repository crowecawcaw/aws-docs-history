

# AWS IoT Greengrass V1 endpoints and quotas
<a name="greengrass"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="greengrass_region"></a>

### Control Plane Operations
<a name="greengrass-control-plane-endpoints"></a>

The following table contains AWS Region-specific endpoints that AWS IoT Greengrass supports for group management operations.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 | greengrass.us-east-2.amazonaws.com | HTTPS | 
| US East (N. Virginia) | us-east-1 | greengrass.us-east-1.amazonaws.com | HTTPS | 
| US West (Oregon) | us-west-2 | greengrass.us-west-2.amazonaws.com | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | greengrass.ap-south-1.amazonaws.com | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 | greengrass.ap-northeast-2.amazonaws.com | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | greengrass.ap-southeast-1.amazonaws.com | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | greengrass.ap-southeast-2.amazonaws.com | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | greengrass.ap-northeast-1.amazonaws.com | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | greengrass.eu-central-1.amazonaws.com | HTTPS | 
| Europe (Ireland) | eu-west-1 | greengrass.eu-west-1.amazonaws.com | HTTPS | 
| Europe (London) | eu-west-2 | greengrass.eu-west-2.amazonaws.com | HTTPS | 
| AWS GovCloud (US-East) | us-gov-east-1 | greengrass.us-gov-east-1.amazonaws.com<br />greengrass.us-gov-east-1.amazonaws.com<br />greengrass-ats.iot.us-gov-east-1.amazonaws.com<br />greengrass-fips.us-gov-east-1.amazonaws.com | HTTPS<br />HTTPS<br />MQTT and HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 | greengrass.us-gov-west-1.amazonaws.com<br />greengrass-ats.iot.us-gov-west-1.amazonaws.com<br />greengrass.us-gov-west-1.amazonaws.com | HTTPS<br />MQTT and HTTPS<br />HTTPS | 

### AWS IoT Device Operations
<a name="greengrass-device-endpoints"></a>

The following table contains AWS Region-specific Amazon Trust Services (ATS) endpoints for AWS IoT device management operations, such as shadow sync. This is a data plane API.

To look up your account-specific endpoint, use the [aws iot describe-endpoint --endpoint-type iot:Data-ATS](https://docs.aws.amazon.com/cli/latest/reference/iot/describe-endpoint.html) command.



| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 | *prefix*-ats.iot.us-east-2.amazonaws.com | HTTPS, MQTT | 
| US East (N. Virginia) | us-east-1 | *prefix*-ats.iot.us-east-1.amazonaws.com | HTTPS, MQTT | 
| US West (Oregon) | us-west-2 | *prefix*-ats.iot.us-west-2.amazonaws.com | HTTPS, MQTT | 
| Asia Pacific (Mumbai) | ap-south-1 | *prefix*-ats.iot.ap-south-1.amazonaws.com | HTTPS, MQTT | 
| Asia Pacific (Seoul) | ap-northeast-2 | *prefix*-ats.iot.ap-northeast-2.amazonaws.com | HTTPS, MQTT | 
| Asia Pacific (Singapore) | ap-southeast-1 | *prefix*-ats.iot.ap-southeast-1.amazonaws.com | HTTPS, MQTT | 
| Asia Pacific (Sydney) | ap-southeast-2 | *prefix*-ats.iot.ap-southeast-2.amazonaws.com | HTTPS, MQTT | 
| Asia Pacific (Tokyo) | ap-northeast-1 | *prefix*-ats.iot.ap-northeast-1.amazonaws.com | HTTPS, MQTT | 
| China (Beijing) | cn-north-1 | prefix.ats.iot.cn-north-1.amazonaws.com.cn | HTTPS, MQTT | 
| Europe (Frankfurt) | eu-central-1 | *prefix*-ats.iot.eu-central-1.amazonaws.com | HTTPS, MQTT | 
| Europe (Ireland) | eu-west-1 | *prefix*-ats.iot.eu-west-1.amazonaws.com | HTTPS, MQTT | 
| Europe (London) | eu-west-2 | *prefix*-ats.iot.eu-west-2.amazonaws.com | HTTPS, MQTT | 
| AWS GovCloud (US-West) | us-gov-west-1 | prefix-ats.iot.us-gov-west-1.amazonaws.com | HTTPS, MQTT | 
| AWS GovCloud (US-East) | us-gov-east-1 | prefix-ats.iot.us-gov-east-1.amazonaws.com | HTTPS, MQTT | 

**Note**  
Legacy Verisign endpoints are currently supported for [some Regions](#greengrass-legacy-endpoints), but we recommend that you use ATS endpoints with ATS root certificate authority (CA) certificates. For more information, see [Server Authentication](https://docs.aws.amazon.com/iot/latest/developerguide/server-authentication.html) in the *AWS IoT Developer Guide*.

### Discovery Operations
<a name="greengrass-runtime-endpoints"></a>

The following table contains AWS Region-specific ATS endpoints for device discovery operations using the [AWS IoT Greengrass Discovery API](https://docs.aws.amazon.com/greengrass/v1/developerguide/gg-discover-api.html). This is a data plane API.



| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 | greengrass-ats.iot.us-east-2.amazonaws.com | HTTPS | 
| US East (N. Virginia) | us-east-1 | greengrass-ats.iot.us-east-1.amazonaws.com | HTTPS | 
| US West (Oregon) | us-west-2 | greengrass-ats.iot.us-west-2.amazonaws.com | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | greengrass-ats.iot.ap-south-1.amazonaws.com | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 | greengrass-ats.iot.ap-northeast-2.amazonaws.com | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | greengrass-ats.iot.ap-southeast-1.amazonaws.com | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | greengrass-ats.iot.ap-southeast-2.amazonaws.com | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | greengrass-ats.iot.ap-northeast-1.amazonaws.com | HTTPS | 
| China (Beijing) | cn-north-1 | greengrass.ats.iot.cn-north-1.amazonaws.com.cn | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | greengrass-ats.iot.eu-central-1.amazonaws.com | HTTPS | 
| Europe (Ireland) | eu-west-1 | greengrass-ats.iot.eu-west-1.amazonaws.com | HTTPS | 
| Europe (London) | eu-west-2 | greengrass-ats.iot.eu-west-2.amazonaws.com | HTTPS | 
| AWS GovCloud (US-West) | us-gov-west-1 | greengrass-ats.iot.us-gov-west-1.amazonaws.com | HTTPS | 
| AWS GovCloud (US-East) | us-gov-east-1 | greengrass-ats.iot.us-gov-east-1.amazonaws.com | HTTPS | 

**Note**  
Legacy Verisign endpoints are currently supported for [some Regions](#greengrass-legacy-endpoints), but we recommend that you use ATS endpoints with ATS root CA certificates. For more information, see [Server authentication](https://docs.aws.amazon.com/iot/latest/developerguide/server-authentication.html) in the *AWS IoT Developer Guide*.

### Supported Legacy Endpoints
<a name="greengrass-legacy-endpoints"></a>

We recommend that you use the ATS endpoints in the preceding tables with ATS root CA certificates. For backward compatibility, AWS IoT Greengrass currently supports legacy Verisign endpoints in the following AWS Regions. This support is expected to end in the future. For more information, see [Server authentication](https://docs.aws.amazon.com/iot/latest/developerguide/server-authentication.html) in the *AWS IoT Developer Guide*.

When using legacy Verisign endpoints, you must use Verisign root CA certificates.

------
#### [ AWS IoT Device Operations (Legacy Endpoints) ]



| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | prefix.iot.us-east-1.amazonaws.com | HTTPS, MQTT | 
| US West (Oregon) | us-west-2 | prefix.iot.us-west-2.amazonaws.com | HTTPS, MQTT | 
| Asia Pacific (Sydney) | ap-southeast-2 | prefix.iot.ap-southeast-2.amazonaws.com | HTTPS, MQTT | 
| Asia Pacific (Tokyo) | ap-northeast-1 | prefix.iot.ap-northeast-1.amazonaws.com | HTTPS, MQTT | 
| Europe (Frankfurt) | eu-central-1 | prefix.iot.eu-central-1.amazonaws.com | HTTPS, MQTT | 
| Europe (Ireland) | eu-west-1 | prefix.iot.eu-west-1.amazonaws.com | HTTPS, MQTT | 

To look up your account-specific legacy endpoint, use the [aws iot describe-endpoint --endpoint-type iot:Data](https://docs.aws.amazon.com/cli/latest/reference/iot/describe-endpoint.html) command.

------
#### [ Discovery Operations (Legacy Endpoints) ]



| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | greengrass.iot.us-east-1.amazonaws.com | HTTPS | 
| US West (Oregon) | us-west-2 | greengrass.iot.us-west-2.amazonaws.com | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | greengrass.iot.ap-southeast-2.amazonaws.com | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | greengrass.iot.ap-northeast-1.amazonaws.com | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | greengrass.iot.eu-central-1.amazonaws.com | HTTPS | 
| Europe (Ireland) | eu-west-1 | greengrass.iot.eu-west-1.amazonaws.com | HTTPS | 

------

## Service quotas
<a name="limits_greengrass"></a>

### AWS IoT Greengrass Cloud API
<a name="gg_cloud_limits"></a>



| Description | Default | 
| --- | --- | 
| Maximum number of AWS IoT devices per AWS IoT Greengrass group. | 2500 | 
| Maximum number of Lambda functions per group. | 200 | 
| Maximum number of resources per Lambda function. | 20 | 
| Maximum number of resources per group. | 200 | 
| Maximum number of transactions per second (TPS) on the AWS IoT Greengrass APIs. | See [TPS](#gg_core_limits_tps). | 
| Maximum number of subscriptions per group. | 10000 | 
| Maximum number of subscriptions that specify Cloud as the source per group. | 50 | 
| Maximum length of a core thing name. | 124 bytes of UTF-8 encoded characters. | 

#### TPS
<a name="gg_core_limits_tps"></a>

The default quota for the maximum number of transactions per second on the AWS IoT Greengrass APIs depends on the API and the AWS Region where AWS IoT Greengrass is used.

For most APIs and [supported AWS Regions](#greengrass_region), the default quota is 30. Exceptions are noted in the following tables.


**API exceptions**  

| API | Default | 
| --- | --- | 
| CreateDeployment | 20 | 


**AWS Region exceptions**  

| AWS Region | Default | 
| --- | --- | 
| China (Beijing) | 10 | 
| AWS GovCloud (US-West) | 10 | 
| AWS GovCloud (US-East) | 10 | 

This quota applies per AWS account. For example, in the US East (N. Virginia) Region, each account has a default quota of 30 TPS. Each API (such as `CreateGroupVersion` or `ListFunctionDefinitions`) has a quota of 30 TPS. This includes control plane and data plane operations. Requests that exceed the account or API quotas are throttled. To request account and API quota increases, including quotas for specific APIs, contact your AWS Enterprise Support representative.

### AWS IoT Greengrass Core
<a name="gg_core_limits"></a>



| Description | Default | 
| --- | --- | 
| Maximum number of routing table entries that specify Cloud as the source. | 50 (matches AWS IoT subscription quota) | 
| Maximum size of messages sent by an AWS IoT device. | 128 KB (matches AWS IoT message size quota) | 
| Minimum message queue size in the Greengrass core router. | 256 KB | 
| Maximum length of a topic string. | 256 bytes of UTF-8 encoded characters. | 
| Maximum number of forward slashes (/) in a topic or topic filter. | 7 | 
| Minimum disk space needed to run the Greengrass Core software. | 128 MB<br />400 MB when using [OTA updates](https://docs.aws.amazon.com/greengrass/v1/developerguide/core-ota-update.html) | 
| Minimum RAM to run the Greengrass Core software. | 128 MB<br />198 MB when using [stream manager](https://docs.aws.amazon.com/greengrass/v1/developerguide/stream-manager.html) | 

The Greengrass Core software provides a service to detect the IP addresses of your Greengrass core devices. It sends this information to the AWS IoT Greengrass cloud service and allows AWS IoT devices to download the IP address of the Greengrass core they need to connect to. 

Do not use this feature if any of the following is true:
+ The IP address of a Greengrass core device changes frequently.
+ The Greengrass core device is not always available to AWS IoT devices in its group.
+ The Greengrass core has multiple IP addresses and an AWS IoT device is unable to reliably determine which address to use.
+ Your organization's security policies don't allow you to send devices' IP addresses to the AWS Cloud.