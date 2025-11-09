# AWS IoT Wireless endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

The following sections describe the service endpoints for AWS IoT Wireless.
AWS IoT Core for Amazon Sidewalk can only be used in the AWS Region `us-east-1`. You can use
these endpoints to perform the operations in the [AWS IoT Wireless API Reference](../../../iot-wireless/2020-11-22/apireference.md "../../../iot-wireless/2020-11-22/apireference.md").

For information about:

- Connecting to and using the LoRaWAN gateways and devices, see [Connecting gateways and devices to
  AWS IoT Core for LoRaWAN](../../../iot/latest/developerguide/connect-iot-lorawan-getting-started.md "../../../iot/latest/developerguide/connect-iot-lorawan-getting-started.md") in the _AWS IoT Developer Guide_.
- Connecting to and using the Amazon Sidewalk end devices, see [Connecting Sidewalk end devices to
  AWS IoT Core for Amazon Sidewalk](../../../iot/latest/developerguide/iot-sidewalk-onboard.md "../../../iot/latest/developerguide/iot-sidewalk-onboard.md") in the _AWS IoT Developer Guide_.

###### Topics

- [AWS IoT Core for LoRaWAN - control plane endpoints](#iot-lorawan-control-plane-endpoints "#iot-lorawan-control-plane-endpoints")
- [AWS IoT Core for LoRaWAN - data plane endpoints](#iot-lorawan-data-plane-endpoints "#iot-lorawan-data-plane-endpoints")

### AWS IoT Core for LoRaWAN - control plane endpoints

The following table contains AWS Region-specific endpoints for
AWS IoT Core for LoRaWAN - control plane operations. You can use
the regular endpoint which has the format
`api.iotwireless.`<region>`.amazonaws.com`,
or the dual-stack endpoint, which uses the format
`api.iotwireless.`<region>`.api.aws`.

###### Note

- When using the endpoints for control plane clients, you
  must provide the [Server Name
  Indication (SNI) extension](https://www.rfc-editor.org/rfc/rfc3546#section-3.1 "https://www.rfc-editor.org/rfc/rfc3546#section-3.1"). The clients can use the SNI extension to indicate the name
  of the server being contacted, and whether it's using the regular endpoints or the dual-stack
  endpoints.
- For AWS IoT Core for Amazon Sidewalk, use the endpoint in the `us-east-1`
  AWS Region.

For information about the operations supported by the
AWS IoT Wireless - control plane endpoints, see [AWS IoT Wireless API
operations](../../../iot-wireless/2020-11-22/apireference/API_Operations.md "../../../iot-wireless/2020-11-22/apireference/API_Operations.md") in the _AWS IoT Wireless API
Reference_.

| Region Name               | Region         | Endpoint                                                                               | Protocol |
| ------------------------- | -------------- | -------------------------------------------------------------------------------------- | -------- |
| US East (N. Virginia)     | us-east-1      | api.iotwireless.us-east-1.amazonaws.com<br>api.iotwireless.us-east-1.api.aws           | HTTPS    |
| US West (Oregon)          | us-west-2      | api.iotwireless.us-west-2.amazonaws.com<br>api.iotwireless.us-west-2.api.aws           | HTTPS    |
| Europe (Ireland)          | eu-west-1      | api.iotwireless.eu-west-1.amazonaws.com<br>api.iotwireless.eu-west-1.api.aws           | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | api.iotwireless.eu-central-1.amazonaws.com<br>api.iotwireless.eu-central-1.api.aws     | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | api.iotwireless.ap-northeast-1.amazonaws.com<br>api.iotwireless.ap-northeast-1.api.aws | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | api.iotwireless.ap-southeast-2.amazonaws.com<br>api.iotwireless.ap-southeast-2.api.aws | HTTPS    |
| South America (São Paulo) | sa-east-1      | api.iotwireless.sa-east-1.amazonaws.com<br>api.iotwireless.sa-east-1.api.aws           | HTTPS    |

### AWS IoT Core for LoRaWAN - data plane endpoints

The AWS IoT Core for LoRaWAN - data plane endpoints are specific to each
AWS account and AWS Region. To find the
AWS IoT Core for LoRaWAN - data plane endpoint for your AWS account and
AWS Region, use the [get-service-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-endpoint.html") CLI command shown here, or the [GetServiceEndpoint](../../../iot-wireless/2020-11-22/apireference/API_GetServiceEndpoint.md "../../../iot-wireless/2020-11-22/apireference/API_GetServiceEndpoint.md") REST API.

###### Note

To use the dual-stack endpoints for the data plane endpoints for your gateways, if
you have already onboarded your gateways before December 1st, 2024, you may need to request
IPv6 activation. For more information, see [Using
IPv6 with AWS IoT Wireless](../../../iot-wireless/latest/developerguide/wireless-ipv6-access.md "../../../iot-wireless/latest/developerguide/wireless-ipv6-access.md").

```
aws iotwireless get-service-endpoint
```

This command returns information about:

- The service type for which you want to get endpoint information about,
  which can be `CUPS` or `LNS`.
- The CUPS or LNS server trust certificate depending on the endpoint
  specified.
- Your data plane API endpoint in the following format:

```
`account-specific-prefix`.`service`.lorawan.`aws-region`.amazonaws.com
```

where `service` can be `cups` or
`lns`.

The following table contains generic representations of the AWS Account-specific
LNS endpoints for each Region that AWS IoT Core for LoRaWAN supports. In the
**Endpoint** column, the
`account-specific-prefix` from your
Account-specific endpoint replaces `prefix` shown in the
generic endpoint representation.

| LNS endpoints             | Region Name    | Region                                            | Endpoint | Protocol |
| ------------------------- | -------------- | ------------------------------------------------- | -------- | -------- |
| US East (N. Virginia)     | us-east-1      | `prefix`.lns.lorawan.us-east-1.amazonaws.com      | WSS      |
| US West (Oregon)          | us-west-2      | `prefix`.lns.lorawan.us-west-2.amazonaws.com      | WSS      |
| Europe (Ireland)          | eu-west-1      | `prefix`.lns.lorawan.eu-west-1.amazonaws.com      | WSS      |
| Europe (Frankfurt)        | eu-central-1   | `prefix`.lns.lorawan.eu-central-1.amazonaws.com   | WSS      |
| Asia Pacific (Tokyo)      | ap-northeast-1 | `prefix`.lns.lorawan.ap-northeast-1.amazonaws.com | WSS      |
| Asia Pacific (Sydney)     | ap-southeast-2 | `prefix`.lns.lorawan.ap-southeast-2.amazonaws.com | WSS      |
| South America (São Paulo) | sa-east-1      | `prefix`.lns.lorawan.sa-east-1.amazonaws.com      | WSS      |

The following table contains generic representations of the AWS Account-specific
CUPS endpoints for each Region that AWS IoT Core supports. In the
**Endpoint** column, the
`account-specific-prefix` from your
Account-specific endpoint replaces `prefix` shown in the
generic endpoint representation.

| CUPS endpoints            | Region Name    | Region                                             | Endpoint | Protocol |
| ------------------------- | -------------- | -------------------------------------------------- | -------- | -------- |
| US East (N. Virginia)     | us-east-1      | `prefix`.cups.lorawan.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | `prefix`.cups.lorawan.us-west-2.amazonaws.com      | HTTPS    |
| Europe (Ireland)          | eu-west-1      | `prefix`.cups.lorawan.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | `prefix`.cups.lorawan.eu-central-1.amazonaws.com   | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | `prefix`.cups.lorawan.ap-northeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | `prefix`.cups.lorawan.ap-southeast-2.amazonaws.com | HTTPS    |
| South America (São Paulo) | sa-east-1      | `prefix`.cups.lorawan.sa-east-1.amazonaws.com      | HTTPS    |

For information about the actions supported by the
AWS IoT Wireless - data plane endpoints, see [AWS IoT Wireless API
operations](../../../iot-wireless/2020-11-22/apireference/API_Operations.md "../../../iot-wireless/2020-11-22/apireference/API_Operations.md") in the _AWS IoT Wireless API
Reference_.

## Service quotas

The following tables describes the maximum number of transactions per second (TPS)
that can be made to each action in the [AWS IoT
Wireless API](../../../iot-wireless/2020-11-22/apireference/Welcome.md "../../../iot-wireless/2020-11-22/apireference/Welcome.md"), which includes AWS IoT Core for LoRaWAN and AWS IoT Core for Amazon Sidewalk.

###### Contents

- [Wireless devices and device data
  quotas](#iot-wireless_quotas-device-data "#iot-wireless_quotas-device-data")
- [LoRaWAN gateways API
  throttling](#iot-wireless_quotas-gateways "#iot-wireless_quotas-gateways")
- [Profiles and
  destinations API throttling](#iot-wireless_quotas-destinations-profiles "#iot-wireless_quotas-destinations-profiles")
- [Sidewalk and logging API
  throttling](#iot-wireless_quotas-sidewalk "#iot-wireless_quotas-sidewalk")
- [Tagging and endpoint API
  throttling](#iot-wireless_quotas-tagging "#iot-wireless_quotas-tagging")
- [Device location and
  additional AWS IoT Wireless API limits](#iot-wireless_quotas-additional "#iot-wireless_quotas-additional")

### Wireless devices and device data

quotas

The following service quotas apply to LoRaWAN and Sidewalk devices. It also includes
device metrics, and device data quotas, which are transmitted between wireless devices,
gateways, and the cloud.

| AWS IoT Wireless devices API throttling                 | Limit display name                                    | Description | Default value                                                                                                                                                                              | Adjustable |
| ------------------------------------------------------- | ----------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `TPS limit for AssociateWirelessDeviceWithThing`        | TPS limit for AssociateWirelessDeviceWithThing        | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6407631C "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6407631C") |
| `TPS limit for CreateNetworkAnalyzerConfiguration`      | TPS limit for CreateNetworkAnalyzerConfiguration      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6796B05C "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6796B05C") |
| `TPS limit for CreateWirelessDevice`                    | TPS limit for CreateWirelessDevice                    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3B5AF547 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3B5AF547") |
| `TPS limit for DeleteNetworkAnalyzerConfiguration`      | TPS limit for DeleteNetworkAnalyzerConfiguration      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4F7C7CD3 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4F7C7CD3") |
| `TPS limit for DeleteWirelessDevice`                    | TPS limit for DeleteWirelessDevice                    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A755236A "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A755236A") |
| `TPS limit for DisassociateWirelessDeviceFromThing`     | TPS limit for DisassociateWirelessDeviceFromThing     | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4951240E "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4951240E") |
| `TPS limit for GetEventConfigurationByResourceTypes`    | TPS limit for GetEventConfigurationByResourceTypes    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FAE31118 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FAE31118") |
| `TPS limit for GetMetricConfiguration`                  | TPS limit for GetMetricConfiguration                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8007AA14 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8007AA14") |
| `TPS limit for GetMetrics`                              | TPS limit for GetMetrics                              | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0253A672 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0253A672") |
| `TPS limit for GetWirelessDevice`                       | TPS limit for GetWirelessDevice                       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-2639F0B0 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-2639F0B0") |
| `TPS limit for GetWirelessDeviceStatistics`             | TPS limit for GetWirelessDeviceStatistics             | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-CCEFD4AF "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-CCEFD4AF") |
| `TPS limit for ListEventConfigurations`                 | TPS limit for ListEventConfigurations                 | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A2058506 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A2058506") |
| `TPS limit for ListNetworkAnalyzerConfigurations`       | TPS limit for ListNetworkAnalyzerConfigurations       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0F5F17D1 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0F5F17D1") |
| `TPS limit for ListWirelessDevices`                     | TPS limit for ListWirelessDevices                     | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-35D1818B "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-35D1818B") |
| `TPS limit for SendDataToWirelessDevice`                | TPS limit for SendDataToWirelessDevice                | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0E4BA92F "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0E4BA92F") |
| `TPS limit for TestWirelessDevice`                      | TPS limit for TestWirelessDevice                      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FC84B266 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FC84B266") |
| `TPS limit for UpdateEventConfigurationByResourceTypes` | TPS limit for UpdateEventConfigurationByResourceTypes | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-882084A6 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-882084A6") |
| `TPS limit for UpdateMetricConfiguration`               | TPS limit for UpdateMetricConfiguration               | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-189593ED "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-189593ED") |
| `TPS limit for UpdateWirelessDevice`                    | TPS limit for UpdateWirelessDevice                    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B4636E40 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B4636E40") |

### LoRaWAN gateways API

throttling

This table describes the maximum TPS for APIs used with LoRaWAN gateways. The
gateways route messages between LoRaWAN devices and AWS IoT Core for LoRaWAN.

| AWS IoT Wireless gateway API throttling                    | Limit display name                                       | Description | Default value                                                                                                                                                                              | Adjustable |
| ---------------------------------------------------------- | -------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `TPS limit for AssociateWirelessGatewayWithCertificate`    | TPS limit for AssociateWirelessGatewayWithCertificate    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4915A563 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4915A563") |
| `TPS limit for AssociateWirelessGatewayWithThing`          | TPS limit for AssociateWirelessGatewayWithThing          | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B29C7ECC "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B29C7ECC") |
| `TPS limit for CreateWirelessGateway`                      | TPS limit for CreateWirelessGateway                      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C2F6FC68 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C2F6FC68") |
| `TPS limit for CreateWirelessGatewayTask`                  | TPS limit for CreateWirelessGatewayTask                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-05BE3C0D "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-05BE3C0D") |
| `TPS limit for CreateWirelessGatewayTaskDefinition`        | TPS limit for CreateWirelessGatewayTaskDefinition        | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8FFCC81A "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8FFCC81A") |
| `TPS limit for DeleteWirelessGateway`                      | TPS limit for DeleteWirelessGateway                      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6DEF44D2 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6DEF44D2") |
| `TPS limit for DeleteWirelessGatewayTask`                  | TPS limit for DeleteWirelessGatewayTask                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B0F3D444 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B0F3D444") |
| `TPS limit for DeleteWirelessGatewayTaskDefinition`        | TPS limit for DeleteWirelessGatewayTaskDefinition        | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-182F8619 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-182F8619") |
| `TPS limit for DisassociateWirelessGatewayFromCertificate` | TPS limit for DisassociateWirelessGatewayFromCertificate | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-907EFF6F "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-907EFF6F") |
| `TPS limit for DisassociateWirelessGatewayFromThing`       | TPS limit for DisassociateWirelessGatewayFromThing       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-33206197 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-33206197") |
| `TPS limit for GetWirelessGateway`                         | TPS limit for GetWirelessGateway                         | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-42B55186 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-42B55186") |
| `TPS limit for GetWirelessGatewayCertificate`              | TPS limit for GetWirelessGatewayCertificate              | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-81B64868 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-81B64868") |
| `TPS limit for GetWirelessGatewayFirmwareInformation`      | TPS limit for GetWirelessGatewayFirmwareInformation      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0C3B538C "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0C3B538C") |
| `TPS limit for GetWirelessGatewayStatistics`               | TPS limit for GetWirelessGatewayStatistics               | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3103F50C "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3103F50C") |
| `TPS limit for GetWirelessGatewayTask`                     | TPS limit for GetWirelessGatewayTask                     | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-334EA895 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-334EA895") |
| `TPS limit for GetWirelessGatewayTaskDefinition`           | TPS limit for GetWirelessGatewayTaskDefinition           | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7AF1469B "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7AF1469B") |
| `TPS limit for ListWirelessGatewayTaskDefinitions`         | TPS limit for ListWirelessGatewayTaskDefinitions         | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-CC2D61C3 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-CC2D61C3") |
| `TPS limit for ListWirelessGateways`                       | TPS limit for ListWirelessGateways                       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F881E3D9 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F881E3D9") |
| `TPS limit for UpdateWirelessGateway`                      | TPS limit for UpdateWirelessGateway                      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A1F96616 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A1F96616") |

### Profiles and

destinations API throttling

This table describes the maximum TPS for device profiles, service profiles, and
destinations that can route messages to other AWS services.

| AWS IoT Wireless device profiles and destination API throttling | Limit display name                 | Description | Default value                                                                                                                                                                              | Adjustable |
| --------------------------------------------------------------- | ---------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `TPS limit for CreateDestination`                               | TPS limit for CreateDestination    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0641E5DC "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0641E5DC") |
| `TPS limit for CreateDeviceProfile`                             | TPS limit for CreateDeviceProfile  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6829C2D4 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6829C2D4") |
| `TPS limit for CreateServiceProfile`                            | TPS limit for CreateServiceProfile | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F8530DBD "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F8530DBD") |
| `TPS limit for DeleteDestination`                               | TPS limit for DeleteDestination    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-EB538AAC "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-EB538AAC") |
| `TPS limit for DeleteDeviceProfile`                             | TPS limit for DeleteDeviceProfile  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-50B185BA "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-50B185BA") |
| `TPS limit for DeleteServiceProfile`                            | TPS limit for DeleteServiceProfile | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A25EC315 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A25EC315") |
| `TPS limit for GetDestination`                                  | TPS limit for GetDestination       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8E7EAF51 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8E7EAF51") |
| `TPS limit for GetDeviceProfile`                                | TPS limit for GetDeviceProfile     | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4FCAEFF0 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4FCAEFF0") |
| `TPS limit for GetServiceProfile`                               | TPS limit for GetServiceProfile    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-905ED905 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-905ED905") |
| `TPS limit for ListDestinations`                                | TPS limit for ListDestinations     | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E54A2621 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E54A2621") |
| `TPS limit for ListDeviceProfiles`                              | TPS limit for ListDeviceProfiles   | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E6CBA335 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E6CBA335") |
| `TPS limit for ListServiceProfiles`                             | TPS limit for ListServiceProfiles  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-647D6C46 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-647D6C46") |
| `TPS limit for UpdateDestination`                               | TPS limit for UpdateDestination    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-AA413BB8 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-AA413BB8") |

### Sidewalk and logging API

throttling

This table describes the maximum TPS for Amazon Sidewalk APIs and APIs that are
used for log levels based on resource types.

| AWS IoT Wireless Sidewalk and logging API throttling   | Limit display name                                   | Description | Default value                                                                                                                                                                              | Adjustable |
| ------------------------------------------------------ | ---------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `TPS limit for AssociateAwsAccountWithPartnerAccount`  | TPS limit for AssociateAwsAccountWithPartnerAccount  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-13EE3A12 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-13EE3A12") |
| `TPS limit for DeleteWirelessDeviceImportTask`         | TPS limit for DeleteWirelessDeviceImportTask         | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-85E750DE "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-85E750DE") |
| `TPS limit for DeregisterWirelessDevice`               | TPS limit for DeregisterWirelessDevice               | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D260A47D "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D260A47D") |
| `TPS limit for GetLogLevelsByResourceTypes`            | TPS limit for GetLogLevelsByResourceTypes            | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C2175B1E "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C2175B1E") |
| `TPS limit for GetPartnerAccount`                      | TPS limit for GetPartnerAccount                      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DEFAE009 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DEFAE009") |
| `TPS limit for GetResourceLogLevel`                    | TPS limit for GetResourceLogLevel                    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6175FC12 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6175FC12") |
| `TPS limit for GetWirelessDeviceImportTask`            | TPS limit for GetWirelessDeviceImportTask            | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-16EAB1D1 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-16EAB1D1") |
| `TPS limit for ListDevicesForWirelessDeviceImportTask` | TPS limit for ListDevicesForWirelessDeviceImportTask | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-18A5F69F "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-18A5F69F") |
| `TPS limit for ListPartnerAccounts`                    | TPS limit for ListPartnerAccounts                    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FB636C37 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-FB636C37") |
| `TPS limit for ListWirelessDeviceImportTasks`          | TPS limit for ListWirelessDeviceImportTasks          | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9704EC18 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9704EC18") |
| `TPS limit for PutResourceLogLevel`                    | TPS limit for PutResourceLogLevel                    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-12D6182B "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-12D6182B") |
| `TPS limit for ResetAllResourceLogLevels`              | TPS limit for ResetAllResourceLogLevels              | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-96FA888E "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-96FA888E") |
| `TPS limit for ResetResourceLogLevel`                  | TPS limit for ResetResourceLogLevel                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9CF47CC5 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9CF47CC5") |
| `TPS limit for StartSingleWirelessDeviceImportTask`    | TPS limit for StartSingleWirelessDeviceImportTask    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7B8D0453 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7B8D0453") |
| `TPS limit for StartWirelessDeviceImportTask`          | TPS limit for StartWirelessDeviceImportTask          | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9C8BB3C8 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9C8BB3C8") |
| `TPS limit for UpdateLogLevelsByResourceTypes`         | TPS limit for UpdateLogLevelsByResourceTypes         | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0D8E249D "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0D8E249D") |
| `TPS limit for UpdatePartnerAccount`                   | TPS limit for UpdatePartnerAccount                   | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3AC27648 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-3AC27648") |
| `TPS limit for UpdateWirelessDeviceImportTask`         | TPS limit for UpdateWirelessDeviceImportTask         | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E8B6C4D2 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E8B6C4D2") |

### Tagging and endpoint API

throttling

This table describes the maximum TPS for the `GetServiceEndpoint` API
and APIs used for tagging resources.

| AWS IoT Wireless tagging and GetServiceEndpoint API throttling | Limit display name                | Description | Default value                                                                                                                                                                              | Adjustable |
| -------------------------------------------------------------- | --------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `TPS limit for GetServiceEndpoint`                             | TPS limit for GetServiceEndpoint  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-13F3B5DD "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-13F3B5DD") |
| `TPS limit for ListTagsForResource`                            | TPS limit for ListTagsForResource | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DEC8385B "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DEC8385B") |
| `TPS limit for TagResource`                                    | TPS limit for TagResource         | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9D5A90BD "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9D5A90BD") |
| `TPS limit for UntagResource`                                  | TPS limit for UntagResource       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DF869DBB "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DF869DBB") |

### Device location and

additional AWS IoT Wireless API limits

This table describes the maximum TPS for other, additional AWS IoT Wireless API
throttling including AWS IoT Core device location, the network analyzer feature,
FUOTA, and multicast groups.

| AWS IoT Wireless limits and quotas                                    | Limit display name                                                  | Description | Default value                                                                                                                                                                              | Adjustable |
| --------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| `TPS limit for AssociateMulticastGroupWithFuotaTask`                  | TPS limit for AssociateMulticastGroupWithFuotaTask                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E91B60DF "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E91B60DF") |
| `TPS limit for AssociateWirelessDeviceWithFuotaTask`                  | TPS limit for AssociateWirelessDeviceWithFuotaTask                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4AC6BBEA "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4AC6BBEA") |
| `TPS limit for AssociateWirelessDeviceWithMulticastGroup`             | TPS limit for AssociateWirelessDeviceWithMulticastGroup             | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-92ECAB75 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-92ECAB75") |
| `TPS limit for CancelMulticastGroupSession`                           | TPS limit for CancelMulticastGroupSession                           | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-72AB9EAE "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-72AB9EAE") |
| `TPS limit for CreateFuotaTask`                                       | TPS limit for CreateFuotaTask                                       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E3C6A79E "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E3C6A79E") |
| `TPS limit for CreateMulticastGroup`                                  | TPS limit for CreateMulticastGroup                                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D07E0E7A "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D07E0E7A") |
| `TPS limit for DeleteFuotaTask`                                       | TPS limit for DeleteFuotaTask                                       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-89C556FB "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-89C556FB") |
| `TPS limit for DeleteMulticastGroup`                                  | TPS limit for DeleteMulticastGroup                                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-93C5A1DB "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-93C5A1DB") |
| `TPS limit for DeleteQueuedMessages`                                  | TPS limit for DeleteQueuedMessages                                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B6937DF9 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B6937DF9") |
| `TPS limit for DisassociateAwsAccountFromPartnerAccount`              | TPS limit for DisassociateAwsAccountFromPartnerAccount              | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A432E505 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A432E505") |
| `TPS limit for DisassociateMulticastGroupFromFuotaTask`               | TPS limit for DisassociateMulticastGroupFromFuotaTask               | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-61A27891 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-61A27891") |
| `TPS limit for DisassociateWirelessDeviceFromFuotaTask`               | TPS limit for DisassociateWirelessDeviceFromFuotaTask               | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0C83FCE2 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0C83FCE2") |
| `TPS limit for DisassociateWirelessDeviceFromMulticastGroup`          | TPS limit for DisassociateWirelessDeviceFromMulticastGroup          | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-1DF3438B "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-1DF3438B") |
| `TPS limit for GetFuotaTask`                                          | TPS limit for GetFuotaTask                                          | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D33E220F "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D33E220F") |
| `TPS limit for GetMulticastGroup`                                     | TPS limit for GetMulticastGroup                                     | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-72A5D5E0 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-72A5D5E0") |
| `TPS limit for GetMulticastGroupSession`                              | TPS limit for GetMulticastGroupSession                              | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9C8C92B3 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9C8C92B3") |
| `TPS limit for GetNetworkAnalyzerConfiguration`                       | TPS limit for GetNetworkAnalyzerConfiguration                       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6AF47E8B "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6AF47E8B") |
| `TPS limit for GetPosition`                                           | TPS limit for GetPosition                                           | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B8A41F6F "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-B8A41F6F") |
| `TPS limit for GetPositionConfiguration`                              | TPS limit for GetPositionConfiguration                              | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-5FCBB48D "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-5FCBB48D") |
| `TPS limit for GetPositionEstimate`                                   | TPS limit for GetPositionEstimate                                   | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D6B79324 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D6B79324") |
| `TPS limit for GetResourceEventConfiguration`                         | TPS limit for GetResourceEventConfiguration                         | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E4F0512E "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E4F0512E") |
| `TPS limit for GetResourcePosition`                                   | TPS limit for GetResourcePosition                                   | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F654617D "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F654617D") |
| `TPS limit for ListFuotaTasks`                                        | TPS limit for ListFuotaTasks                                        | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0604C085 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-0604C085") |
| `TPS limit for ListMulticastGroups`                                   | TPS limit for ListMulticastGroups                                   | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4DEB3C3F "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-4DEB3C3F") |
| `TPS limit for ListMulticastGroupsByFuotaTask`                        | TPS limit for ListMulticastGroupsByFuotaTask                        | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7CE08A6C "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-7CE08A6C") |
| `TPS limit for ListPositionConfigurations`                            | TPS limit for ListPositionConfigurations                            | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F4D43AC0 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F4D43AC0") |
| `TPS limit for ListQueuedMessages`                                    | TPS limit for ListQueuedMessages                                    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D91B7067 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-D91B7067") |
| `TPS limit for PutPositionConfiguration`                              | TPS limit for PutPositionConfiguration                              | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A4CD53FD "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-A4CD53FD") |
| `TPS limit for SendDataToMulticastGroup`                              | TPS limit for SendDataToMulticastGroup                              | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-1346D5EC "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-1346D5EC") |
| `TPS limit for StartBulkAssociateWirelessDeviceWithMulticastGroup`    | TPS limit for StartBulkAssociateWirelessDeviceWithMulticastGroup    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F930F6AD "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-F930F6AD") |
| `TPS limit for StartBulkDisassociateWirelessDeviceFromMulticastGroup` | TPS limit for StartBulkDisassociateWirelessDeviceFromMulticastGroup | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8DBB3861 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8DBB3861") |
| `TPS limit for StartFuotaTask`                                        | TPS limit for StartFuotaTask                                        | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DB770805 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-DB770805") |
| `TPS limit for StartMulticastGroupSession`                            | TPS limit for StartMulticastGroupSession                            | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6FC5E39D "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-6FC5E39D") |
| `TPS limit for StartNetworkAnalyzerStream`                            | TPS limit for StartNetworkAnalyzerStream                            | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9E25CA04 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-9E25CA04") |
| `TPS limit for UpdateFuotaTask`                                       | TPS limit for UpdateFuotaTask                                       | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-5369BF7E "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-5369BF7E") |
| `TPS limit for UpdateMulticastGroup`                                  | TPS limit for UpdateMulticastGroup                                  | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8E864D54 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8E864D54") |
| `TPS limit for UpdateNetworkAnalyzerConfiguration`                    | TPS limit for UpdateNetworkAnalyzerConfiguration                    | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8367137B "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-8367137B") |
| `TPS limit for UpdatePosition`                                        | TPS limit for UpdatePosition                                        | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C80BC655 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-C80BC655") |
| `TPS limit for UpdateResourceEventConfiguration`                      | TPS limit for UpdateResourceEventConfiguration                      | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-70D824D9 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-70D824D9") |
| `TPS limit for UpdateResourcePosition`                                | TPS limit for UpdateResourcePosition                                | 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E01F1EA2 "https://console.aws.amazon.com/servicequotas/home/services/iotwireless/quotas/L-E01F1EA2") |
