

# AWS IoT Wireless endpoints and quotas
<a name="iot-lorawan"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="iot-wireless_region"></a>

The following sections describe the service endpoints for AWS IoT Wireless. AWS IoT Core for Amazon Sidewalk can only be used in the AWS Region `us-east-1`. You can use these endpoints to perform the operations in the [AWS IoT Wireless API Reference](https://docs.aws.amazon.com/iot-wireless/latest/apireference/).

For information about:
+ Connecting to and using the LoRaWAN gateways and devices, see [Connecting gateways and devices to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-getting-started.html) in the *AWS IoT Developer Guide*.
+ Connecting to and using the Amazon Sidewalk end devices, see [Connecting Sidewalk end devices to AWS IoT Core for Amazon Sidewalk](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk-onboard.html) in the *AWS IoT Developer Guide*.

**Topics**
+ [AWS IoT Core for LoRaWAN - control plane endpoints](#iot-lorawan-control-plane-endpoints)
+ [AWS IoT Core for LoRaWAN - data plane endpoints](#iot-lorawan-data-plane-endpoints)

### AWS IoT Core for LoRaWAN - control plane endpoints
<a name="iot-lorawan-control-plane-endpoints"></a>

The following table contains AWS Region-specific endpoints for AWS IoT Core for LoRaWAN - control plane operations. You can use the regular endpoint which has the format `api.iotwireless.{{<region>}}.amazonaws.com`, or the dual-stack endpoint, which uses the format `api.iotwireless.{{<region>}}.api.aws`.

**Note**  
When using the endpoints for control plane clients, you must provide the [Server Name Indication (SNI) extension](https://www.rfc-editor.org/rfc/rfc3546#section-3.1). The clients can use the SNI extension to indicate the name of the server being contacted, and whether it's using the regular endpoints or the dual-stack endpoints.
For AWS IoT Core for Amazon Sidewalk, use the endpoint in the `us-east-1` AWS Region.

For information about the operations supported by the AWS IoT Wireless - control plane endpoints, see [AWS IoT Wireless API operations](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_Operations.html) in the *AWS IoT Wireless API Reference*.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | api.iotwireless.us-east-1.amazonaws.com<br />api.iotwireless.us-east-1.api.aws | HTTPS | 
| US West (Oregon) | us-west-2 | api.iotwireless.us-west-2.amazonaws.com<br />api.iotwireless.us-west-2.api.aws | HTTPS | 
| Europe (Ireland) | eu-west-1 | api.iotwireless.eu-west-1.amazonaws.com<br />api.iotwireless.eu-west-1.api.aws | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | api.iotwireless.eu-central-1.amazonaws.com<br />api.iotwireless.eu-central-1.api.aws | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | api.iotwireless.ap-northeast-1.amazonaws.com<br />api.iotwireless.ap-northeast-1.api.aws | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | api.iotwireless.ap-southeast-2.amazonaws.com<br />api.iotwireless.ap-southeast-2.api.aws | HTTPS | 
| South America (São Paulo) | sa-east-1 | api.iotwireless.sa-east-1.amazonaws.com<br />api.iotwireless.sa-east-1.api.aws | HTTPS | 

### AWS IoT Core for LoRaWAN - data plane endpoints
<a name="iot-lorawan-data-plane-endpoints"></a>

The AWS IoT Core for LoRaWAN - data plane endpoints are specific to each AWS account and AWS Region. To find the AWS IoT Core for LoRaWAN - data plane endpoint for your AWS account and AWS Region, use the [get-service-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-endpoint.html) CLI command shown here, or the [GetServiceEndpoint](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetServiceEndpoint.html) REST API.

**Note**  
To use the dual-stack endpoints for the data plane endpoints for your gateways, if you have already onboarded your gateways before December 1st, 2024, you may need to request IPv6 activation. For more information, see [Using IPv6 with AWS IoT Wireless](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/wireless-ipv6-access.html).

```
aws iotwireless get-service-endpoint
```

This command returns information about:
+ The service type for which you want to get endpoint information about, which can be `CUPS` or `LNS`.
+ The CUPS or LNS server trust certificate depending on the endpoint specified.
+ Your data plane API endpoint in the following format:

  ```
  {{account-specific-prefix}}.{{service}}.lorawan.{{aws-region}}.amazonaws.com
  ```

where `{{service}}` can be `cups` or `lns`.

The following table contains generic representations of the AWS Account-specific LNS endpoints for each Region that AWS IoT Core for LoRaWAN supports. In the **Endpoint** column, the `{{account-specific-prefix}}` from your Account-specific endpoint replaces {{prefix}} shown in the generic endpoint representation.


**LNS endpoints**  

| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | {{prefix}}.lns.lorawan.us-east-1.amazonaws.com | WSS | 
| US West (Oregon) | us-west-2 | {{prefix}}.lns.lorawan.us-west-2.amazonaws.com | WSS | 
| Europe (Ireland) | eu-west-1 | {{prefix}}.lns.lorawan.eu-west-1.amazonaws.com | WSS | 
| Europe (Frankfurt) | eu-central-1 | {{prefix}}.lns.lorawan.eu-central-1.amazonaws.com | WSS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | {{prefix}}.lns.lorawan.ap-northeast-1.amazonaws.com | WSS | 
| Asia Pacific (Sydney) | ap-southeast-2 | {{prefix}}.lns.lorawan.ap-southeast-2.amazonaws.com | WSS | 
| South America (São Paulo) | sa-east-1 | {{prefix}}.lns.lorawan.sa-east-1.amazonaws.com | WSS | 

The following table contains generic representations of the AWS Account-specific CUPS endpoints for each Region that AWS IoT Core supports. In the **Endpoint** column, the `{{account-specific-prefix}}` from your Account-specific endpoint replaces {{prefix}} shown in the generic endpoint representation.


**CUPS endpoints**  

| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | {{prefix}}.cups.lorawan.us-east-1.amazonaws.com | HTTPS | 
| US West (Oregon) | us-west-2 | {{prefix}}.cups.lorawan.us-west-2.amazonaws.com | HTTPS | 
| Europe (Ireland) | eu-west-1 | {{prefix}}.cups.lorawan.eu-west-1.amazonaws.com | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | {{prefix}}.cups.lorawan.eu-central-1.amazonaws.com | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | {{prefix}}.cups.lorawan.ap-northeast-1.amazonaws.com | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | {{prefix}}.cups.lorawan.ap-southeast-2.amazonaws.com | HTTPS | 
| South America (São Paulo) | sa-east-1 | {{prefix}}.cups.lorawan.sa-east-1.amazonaws.com | HTTPS | 

For information about the actions supported by the AWS IoT Wireless - data plane endpoints, see [AWS IoT Wireless API operations](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_Operations.html) in the *AWS IoT Wireless API Reference*.

## Service quotas
<a name="limits_iotwireless"></a>

The following tables describes the maximum number of transactions per second (TPS) that can be made to each action in the [AWS IoT Wireless API](https://docs.aws.amazon.com/iot-wireless/latest/apireference/Welcome.html), which includes AWS IoT Core for LoRaWAN and AWS IoT Core for Amazon Sidewalk.

**Topics**
+ [Wireless devices and device data quotas](#iot-wireless_quotas-device-data)
+ [LoRaWAN gateways API throttling](#iot-wireless_quotas-gateways)
+ [Profiles and destinations API throttling](#iot-wireless_quotas-destinations-profiles)
+ [Sidewalk and logging API throttling](#iot-wireless_quotas-sidewalk)
+ [Tagging and endpoint API throttling](#iot-wireless_quotas-tagging)
+ [Device location and additional AWS IoT Wireless API limits](#iot-wireless_quotas-additional)

### Wireless devices and device data quotas
<a name="iot-wireless_quotas-device-data"></a>

The following service quotas apply to LoRaWAN and Sidewalk devices. It also includes device metrics, and device data quotas, which are transmitted between wireless devices, gateways, and the cloud.


**AWS IoT Wireless devices API throttling**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[TPS limit for AssociateWirelessDeviceWithThing](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6407631C)` | TPS limit for AssociateWirelessDeviceWithThing | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6407631C) | 
| `[TPS limit for CreateNetworkAnalyzerConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6796B05C)` | TPS limit for CreateNetworkAnalyzerConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6796B05C) | 
| `[TPS limit for CreateWirelessDevice](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3B5AF547)` | TPS limit for CreateWirelessDevice | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3B5AF547) | 
| `[TPS limit for DeleteNetworkAnalyzerConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4F7C7CD3)` | TPS limit for DeleteNetworkAnalyzerConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4F7C7CD3) | 
| `[TPS limit for DeleteWirelessDevice](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A755236A)` | TPS limit for DeleteWirelessDevice | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A755236A) | 
| `[TPS limit for DisassociateWirelessDeviceFromThing](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4951240E)` | TPS limit for DisassociateWirelessDeviceFromThing | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4951240E) | 
| `[TPS limit for GetEventConfigurationByResourceTypes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FAE31118)` | TPS limit for GetEventConfigurationByResourceTypes | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FAE31118) | 
| `[TPS limit for GetMetricConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8007AA14)` | TPS limit for GetMetricConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8007AA14) | 
| `[TPS limit for GetMetrics](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0253A672)` | TPS limit for GetMetrics | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0253A672) | 
| `[TPS limit for GetWirelessDevice](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-2639F0B0)` | TPS limit for GetWirelessDevice | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-2639F0B0) | 
| `[TPS limit for GetWirelessDeviceStatistics](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-CCEFD4AF)` | TPS limit for GetWirelessDeviceStatistics | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-CCEFD4AF) | 
| `[TPS limit for ListEventConfigurations](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A2058506)` | TPS limit for ListEventConfigurations | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A2058506) | 
| `[TPS limit for ListNetworkAnalyzerConfigurations](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0F5F17D1)` | TPS limit for ListNetworkAnalyzerConfigurations | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0F5F17D1) | 
| `[TPS limit for ListWirelessDevices](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-35D1818B)` | TPS limit for ListWirelessDevices | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-35D1818B) | 
| `[TPS limit for SendDataToWirelessDevice](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0E4BA92F)` | TPS limit for SendDataToWirelessDevice | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0E4BA92F) | 
| `[TPS limit for TestWirelessDevice](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FC84B266)` | TPS limit for TestWirelessDevice | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FC84B266) | 
| `[TPS limit for UpdateEventConfigurationByResourceTypes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-882084A6)` | TPS limit for UpdateEventConfigurationByResourceTypes | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-882084A6) | 
| `[TPS limit for UpdateMetricConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-189593ED)` | TPS limit for UpdateMetricConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-189593ED) | 
| `[TPS limit for UpdateWirelessDevice](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B4636E40)` | TPS limit for UpdateWirelessDevice | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B4636E40) | 

### LoRaWAN gateways API throttling
<a name="iot-wireless_quotas-gateways"></a>

This table describes the maximum TPS for APIs used with LoRaWAN gateways. The gateways route messages between LoRaWAN devices and AWS IoT Core for LoRaWAN.


**AWS IoT Wireless gateway API throttling**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[TPS limit for AssociateWirelessGatewayWithCertificate](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4915A563)` | TPS limit for AssociateWirelessGatewayWithCertificate | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4915A563) | 
| `[TPS limit for AssociateWirelessGatewayWithThing](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B29C7ECC)` | TPS limit for AssociateWirelessGatewayWithThing | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B29C7ECC) | 
| `[TPS limit for CreateWirelessGateway](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C2F6FC68)` | TPS limit for CreateWirelessGateway | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C2F6FC68) | 
| `[TPS limit for CreateWirelessGatewayTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-05BE3C0D)` | TPS limit for CreateWirelessGatewayTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-05BE3C0D) | 
| `[TPS limit for CreateWirelessGatewayTaskDefinition](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8FFCC81A)` | TPS limit for CreateWirelessGatewayTaskDefinition | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8FFCC81A) | 
| `[TPS limit for DeleteWirelessGateway](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6DEF44D2)` | TPS limit for DeleteWirelessGateway | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6DEF44D2) | 
| `[TPS limit for DeleteWirelessGatewayTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B0F3D444)` | TPS limit for DeleteWirelessGatewayTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B0F3D444) | 
| `[TPS limit for DeleteWirelessGatewayTaskDefinition](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-182F8619)` | TPS limit for DeleteWirelessGatewayTaskDefinition | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-182F8619) | 
| `[TPS limit for DisassociateWirelessGatewayFromCertificate](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-907EFF6F)` | TPS limit for DisassociateWirelessGatewayFromCertificate | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-907EFF6F) | 
| `[TPS limit for DisassociateWirelessGatewayFromThing](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-33206197)` | TPS limit for DisassociateWirelessGatewayFromThing | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-33206197) | 
| `[TPS limit for GetWirelessGateway](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-42B55186)` | TPS limit for GetWirelessGateway | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-42B55186) | 
| `[TPS limit for GetWirelessGatewayCertificate](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-81B64868)` | TPS limit for GetWirelessGatewayCertificate | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-81B64868) | 
| `[TPS limit for GetWirelessGatewayFirmwareInformation](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0C3B538C)` | TPS limit for GetWirelessGatewayFirmwareInformation | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0C3B538C) | 
| `[TPS limit for GetWirelessGatewayStatistics](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3103F50C)` | TPS limit for GetWirelessGatewayStatistics | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3103F50C) | 
| `[TPS limit for GetWirelessGatewayTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-334EA895)` | TPS limit for GetWirelessGatewayTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-334EA895) | 
| `[TPS limit for GetWirelessGatewayTaskDefinition](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7AF1469B)` | TPS limit for GetWirelessGatewayTaskDefinition | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7AF1469B) | 
| `[TPS limit for ListWirelessGatewayTaskDefinitions](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-CC2D61C3)` | TPS limit for ListWirelessGatewayTaskDefinitions | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-CC2D61C3) | 
| `[TPS limit for ListWirelessGateways](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F881E3D9)` | TPS limit for ListWirelessGateways | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F881E3D9) | 
| `[TPS limit for UpdateWirelessGateway](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A1F96616)` | TPS limit for UpdateWirelessGateway | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A1F96616) | 

### Profiles and destinations API throttling
<a name="iot-wireless_quotas-destinations-profiles"></a>

This table describes the maximum TPS for device profiles, service profiles, and destinations that can route messages to other AWS services.


**AWS IoT Wireless device profiles and destination API throttling**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[TPS limit for CreateDestination](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0641E5DC)` | TPS limit for CreateDestination | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0641E5DC) | 
| `[TPS limit for CreateDeviceProfile](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6829C2D4)` | TPS limit for CreateDeviceProfile | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6829C2D4) | 
| `[TPS limit for CreateServiceProfile](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F8530DBD)` | TPS limit for CreateServiceProfile | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F8530DBD) | 
| `[TPS limit for DeleteDestination](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-EB538AAC)` | TPS limit for DeleteDestination | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-EB538AAC) | 
| `[TPS limit for DeleteDeviceProfile](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-50B185BA)` | TPS limit for DeleteDeviceProfile | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-50B185BA) | 
| `[TPS limit for DeleteServiceProfile](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A25EC315)` | TPS limit for DeleteServiceProfile | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A25EC315) | 
| `[TPS limit for GetDestination](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8E7EAF51)` | TPS limit for GetDestination | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8E7EAF51) | 
| `[TPS limit for GetDeviceProfile](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4FCAEFF0)` | TPS limit for GetDeviceProfile | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4FCAEFF0) | 
| `[TPS limit for GetServiceProfile](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-905ED905)` | TPS limit for GetServiceProfile | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-905ED905) | 
| `[TPS limit for ListDestinations](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E54A2621)` | TPS limit for ListDestinations | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E54A2621) | 
| `[TPS limit for ListDeviceProfiles](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E6CBA335)` | TPS limit for ListDeviceProfiles | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E6CBA335) | 
| `[TPS limit for ListServiceProfiles](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-647D6C46)` | TPS limit for ListServiceProfiles | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-647D6C46) | 
| `[TPS limit for UpdateDestination](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-AA413BB8)` | TPS limit for UpdateDestination | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-AA413BB8) | 

### Sidewalk and logging API throttling
<a name="iot-wireless_quotas-sidewalk"></a>

This table describes the maximum TPS for Amazon Sidewalk APIs and APIs that are used for log levels based on resource types.


**AWS IoT Wireless Sidewalk and logging API throttling**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[TPS limit for AssociateAwsAccountWithPartnerAccount](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-13EE3A12)` | TPS limit for AssociateAwsAccountWithPartnerAccount | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-13EE3A12) | 
| `[TPS limit for DeleteWirelessDeviceImportTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-85E750DE)` | TPS limit for DeleteWirelessDeviceImportTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-85E750DE) | 
| `[TPS limit for DeregisterWirelessDevice](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D260A47D)` | TPS limit for DeregisterWirelessDevice | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D260A47D) | 
| `[TPS limit for GetLogLevelsByResourceTypes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C2175B1E)` | TPS limit for GetLogLevelsByResourceTypes | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C2175B1E) | 
| `[TPS limit for GetPartnerAccount](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DEFAE009)` | TPS limit for GetPartnerAccount | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DEFAE009) | 
| `[TPS limit for GetResourceLogLevel](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6175FC12)` | TPS limit for GetResourceLogLevel | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6175FC12) | 
| `[TPS limit for GetWirelessDeviceImportTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-16EAB1D1)` | TPS limit for GetWirelessDeviceImportTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-16EAB1D1) | 
| `[TPS limit for ListDevicesForWirelessDeviceImportTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-18A5F69F)` | TPS limit for ListDevicesForWirelessDeviceImportTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-18A5F69F) | 
| `[TPS limit for ListPartnerAccounts](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FB636C37)` | TPS limit for ListPartnerAccounts | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FB636C37) | 
| `[TPS limit for ListWirelessDeviceImportTasks](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9704EC18)` | TPS limit for ListWirelessDeviceImportTasks | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9704EC18) | 
| `[TPS limit for PutResourceLogLevel](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-12D6182B)` | TPS limit for PutResourceLogLevel | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-12D6182B) | 
| `[TPS limit for ResetAllResourceLogLevels](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-96FA888E)` | TPS limit for ResetAllResourceLogLevels | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-96FA888E) | 
| `[TPS limit for ResetResourceLogLevel](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9CF47CC5)` | TPS limit for ResetResourceLogLevel | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9CF47CC5) | 
| `[TPS limit for StartSingleWirelessDeviceImportTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7B8D0453)` | TPS limit for StartSingleWirelessDeviceImportTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7B8D0453) | 
| `[TPS limit for StartWirelessDeviceImportTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9C8BB3C8)` | TPS limit for StartWirelessDeviceImportTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9C8BB3C8) | 
| `[TPS limit for UpdateLogLevelsByResourceTypes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0D8E249D)` | TPS limit for UpdateLogLevelsByResourceTypes | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0D8E249D) | 
| `[TPS limit for UpdatePartnerAccount](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3AC27648)` | TPS limit for UpdatePartnerAccount | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3AC27648) | 
| `[TPS limit for UpdateWirelessDeviceImportTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E8B6C4D2)` | TPS limit for UpdateWirelessDeviceImportTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E8B6C4D2) | 

### Tagging and endpoint API throttling
<a name="iot-wireless_quotas-tagging"></a>

This table describes the maximum TPS for the `GetServiceEndpoint` API and APIs used for tagging resources.


**AWS IoT Wireless tagging and GetServiceEndpoint API throttling**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[TPS limit for GetServiceEndpoint](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-13F3B5DD)` | TPS limit for GetServiceEndpoint | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-13F3B5DD) | 
| `[TPS limit for ListTagsForResource](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DEC8385B)` | TPS limit for ListTagsForResource | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DEC8385B) | 
| `[TPS limit for TagResource](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9D5A90BD)` | TPS limit for TagResource | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9D5A90BD) | 
| `[TPS limit for UntagResource](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DF869DBB)` | TPS limit for UntagResource | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DF869DBB) | 

### Device location and additional AWS IoT Wireless API limits
<a name="iot-wireless_quotas-additional"></a>

This table describes the maximum TPS for other, additional AWS IoT Wireless API throttling including AWS IoT Core device location, the network analyzer feature, FUOTA, and multicast groups.


**AWS IoT Wireless limits and quotas**  

| Limit display name | Description | Default value | Adjustable | 
| --- | --- | --- | --- | 
| `[TPS limit for AssociateMulticastGroupWithFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E91B60DF)` | TPS limit for AssociateMulticastGroupWithFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E91B60DF) | 
| `[TPS limit for AssociateWirelessDeviceWithFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4AC6BBEA)` | TPS limit for AssociateWirelessDeviceWithFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4AC6BBEA) | 
| `[TPS limit for AssociateWirelessDeviceWithMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-92ECAB75)` | TPS limit for AssociateWirelessDeviceWithMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-92ECAB75) | 
| `[TPS limit for CancelMulticastGroupSession](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-72AB9EAE)` | TPS limit for CancelMulticastGroupSession | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-72AB9EAE) | 
| `[TPS limit for CreateFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E3C6A79E)` | TPS limit for CreateFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E3C6A79E) | 
| `[TPS limit for CreateMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D07E0E7A)` | TPS limit for CreateMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D07E0E7A) | 
| `[TPS limit for DeleteFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-89C556FB)` | TPS limit for DeleteFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-89C556FB) | 
| `[TPS limit for DeleteMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-93C5A1DB)` | TPS limit for DeleteMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-93C5A1DB) | 
| `[TPS limit for DeleteQueuedMessages](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B6937DF9)` | TPS limit for DeleteQueuedMessages | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B6937DF9) | 
| `[TPS limit for DisassociateAwsAccountFromPartnerAccount](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A432E505)` | TPS limit for DisassociateAwsAccountFromPartnerAccount | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A432E505) | 
| `[TPS limit for DisassociateMulticastGroupFromFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-61A27891)` | TPS limit for DisassociateMulticastGroupFromFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-61A27891) | 
| `[TPS limit for DisassociateWirelessDeviceFromFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0C83FCE2)` | TPS limit for DisassociateWirelessDeviceFromFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0C83FCE2) | 
| `[TPS limit for DisassociateWirelessDeviceFromMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-1DF3438B)` | TPS limit for DisassociateWirelessDeviceFromMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-1DF3438B) | 
| `[TPS limit for GetFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D33E220F)` | TPS limit for GetFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D33E220F) | 
| `[TPS limit for GetMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-72A5D5E0)` | TPS limit for GetMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-72A5D5E0) | 
| `[TPS limit for GetMulticastGroupSession](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9C8C92B3)` | TPS limit for GetMulticastGroupSession | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9C8C92B3) | 
| `[TPS limit for GetNetworkAnalyzerConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6AF47E8B)` | TPS limit for GetNetworkAnalyzerConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6AF47E8B) | 
| `[TPS limit for GetPosition](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B8A41F6F)` | TPS limit for GetPosition | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B8A41F6F) | 
| `[TPS limit for GetPositionConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-5FCBB48D)` | TPS limit for GetPositionConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-5FCBB48D) | 
| `[TPS limit for GetPositionEstimate](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D6B79324)` | TPS limit for GetPositionEstimate | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D6B79324) | 
| `[TPS limit for GetResourceEventConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E4F0512E)` | TPS limit for GetResourceEventConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E4F0512E) | 
| `[TPS limit for GetResourcePosition](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F654617D)` | TPS limit for GetResourcePosition | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F654617D) | 
| `[TPS limit for ListFuotaTasks](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0604C085)` | TPS limit for ListFuotaTasks | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0604C085) | 
| `[TPS limit for ListMulticastGroups](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4DEB3C3F)` | TPS limit for ListMulticastGroups | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4DEB3C3F) | 
| `[TPS limit for ListMulticastGroupsByFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7CE08A6C)` | TPS limit for ListMulticastGroupsByFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7CE08A6C) | 
| `[TPS limit for ListPositionConfigurations](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F4D43AC0)` | TPS limit for ListPositionConfigurations | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F4D43AC0) | 
| `[TPS limit for ListQueuedMessages](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D91B7067)` | TPS limit for ListQueuedMessages | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D91B7067) | 
| `[TPS limit for PutPositionConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A4CD53FD)` | TPS limit for PutPositionConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A4CD53FD) | 
| `[TPS limit for SendDataToMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-1346D5EC)` | TPS limit for SendDataToMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-1346D5EC) | 
| `[TPS limit for StartBulkAssociateWirelessDeviceWithMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F930F6AD)` | TPS limit for StartBulkAssociateWirelessDeviceWithMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F930F6AD) | 
| `[TPS limit for StartBulkDisassociateWirelessDeviceFromMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8DBB3861)` | TPS limit for StartBulkDisassociateWirelessDeviceFromMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8DBB3861) | 
| `[TPS limit for StartFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DB770805)` | TPS limit for StartFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DB770805) | 
| `[TPS limit for StartMulticastGroupSession](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6FC5E39D)` | TPS limit for StartMulticastGroupSession | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6FC5E39D) | 
| `[TPS limit for StartNetworkAnalyzerStream](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9E25CA04)` | TPS limit for StartNetworkAnalyzerStream | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9E25CA04) | 
| `[TPS limit for UpdateFuotaTask](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-5369BF7E)` | TPS limit for UpdateFuotaTask | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-5369BF7E) | 
| `[TPS limit for UpdateMulticastGroup](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8E864D54)` | TPS limit for UpdateMulticastGroup | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8E864D54) | 
| `[TPS limit for UpdateNetworkAnalyzerConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8367137B)` | TPS limit for UpdateNetworkAnalyzerConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8367137B) | 
| `[TPS limit for UpdatePosition](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C80BC655)` | TPS limit for UpdatePosition | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C80BC655) | 
| `[TPS limit for UpdateResourceEventConfiguration](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-70D824D9)` | TPS limit for UpdateResourceEventConfiguration | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-70D824D9) | 
| `[TPS limit for UpdateResourcePosition](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E01F1EA2)` | TPS limit for UpdateResourcePosition | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E01F1EA2) | 