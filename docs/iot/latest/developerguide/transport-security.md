# Transport security in AWS IoT Core

TLS (Transport Layer Security) is a cryptographic protocol that is designed for secure
communication over a computer network. The AWS IoT Core Device Gateway requires customers to
encrypt all communication while in-transit by using TLS for connections from devices to the
Gateway. TLS is used to achieve confidentiality of the application protocols (MQTT, HTTP,
and WebSocket) supported by AWS IoT Core. TLS support is available in a number of programming
languages and operating systems. Data within AWS is encrypted by the specific AWS
service. For more information about data encryption on other AWS services, see the
security documentation for that service.

###### Contents

- [TLS protocols](#tls-ssl-policy "#tls-ssl-policy")
- [Security policies](#tls-policy-table "#tls-policy-table")
- [Important notes for transport security in
  AWS IoT Core](#tls-ssl-core "#tls-ssl-core")
- [Transport security for LoRaWAN wireless devices](#tls-lorawan "#tls-lorawan")

## TLS protocols

AWS IoT Core supports the following versions of the TLS protocol:

- TLS 1.3
- TLS 1.2

With AWS IoT Core, you can configure the TLS settings (for [TLS 1.2](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.2 "https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.2")
and [TLS
1.3](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3 "https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3")) in domain configurations. For more information, see [Configuring TLS settings in domain
configurations](iot-endpoints-tls-config.md "iot-endpoints-tls-config.md").

## Security policies

A security policy is a combination of TLS protocols and their ciphers that determine
which protocols and ciphers are supported during TLS negotiations between a client and a
server. You can configure your devices to use predefined security policies based on your
needs. Note that AWS IoT Core doesn't support custom security policies.

You can choose one of the predefined security policies for your devices when
connecting them to AWS IoT Core. The names of the most recent predefined security policies
in AWS IoT Core include version information based on the year and month that they were
released. The default predefined security policy is
`IoTSecurityPolicy_TLS13_1_2_2022_10`. To specify a security policy, you
can use the AWS IoT console or the AWS CLI. For more information, see [Configuring TLS settings in domain
configurations](iot-endpoints-tls-config.md "iot-endpoints-tls-config.md").

The following table describes the most recent predefined security policies that
AWS IoT Core supports. The `IotSecurityPolicy_` has been removed from policy
names in the heading row so that they fit.

| **Security policy**           | TLS13_1_3_2022_10 | TLS13_1_2_2022_10 | TLS12_1_2_2022_10 | TLS12_1_0_2016_01\* | TLS12_1_0_2015_01\* |
| ----------------------------- | ----------------- | ----------------- | ----------------- | ------------------- | ------------------- | --- | --------- |
| **TCP Port**                  | 443/8443/8883     | 443/8443/8883     | 443/8443/8883     | 443                 | 8443/8883           | 443 | 8443/8883 |
| **TLS<br>Protocols**          |
| TLS 1.2                       |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| TLS 1.3                       | ✓                 | ✓                 |                   |                     |                     |     |           |
| **TLS<br>Ciphers**            |
| TLS_AES_128_GCM_SHA256        | ✓                 | ✓                 |                   |                     |                     |     |           |
| TLS_AES_256_GCM_SHA384        | ✓                 | ✓                 |                   |                     |                     |     |           |
| TLS_CHACHA20_POLY1305_SHA256  | ✓                 | ✓                 |                   |                     |                     |     |           |
| ECDHE-RSA-AES128-GCM-SHA256   |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-RSA-AES128-SHA256       |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-RSA-AES128-SHA          |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-RSA-AES256-GCM-SHA384   |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-RSA-AES256-SHA384       |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-RSA-AES256-SHA          |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| AES128-GCM-SHA256             |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| AES128-SHA256                 |                   | ✓                 | ✓                 | ✓                   |                     | ✓   | ✓         |
| AES128-SHA                    |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| AES256-GCM-SHA384             |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| AES256-SHA256                 |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| AES256-SHA                    |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| DHE-RSA-AES256-SHA            |                   |                   |                   |                     |                     | ✓   | ✓         |
| ECDHE-ECDSA-AES128-GCM-SHA256 |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-ECDSA-AES128-SHA256     |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-ECDSA-AES128-SHA        |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-ECDSA-AES256-GCM-SHA384 |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-ECDSA-AES256-SHA384     |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |
| ECDHE-ECDSA-AES256-SHA        |                   | ✓                 | ✓                 | ✓                   | ✓                   | ✓   | ✓         |

###### Note

`TLS12_1_0_2016_01` is only available in the following AWS Regions:
ap-east-1, ap-northeast-2, ap-south-1, ap-southeast-2, ca-central-1, cn-north-1,
cn-northwest-1, eu-north-1, eu-west-2, eu-west-3, me-south-1, sa-east-1, us-east-2,
us-gov-west-1, us-gov-west-2, us-west-1.

`TLS12_1_0_2015_01` is only available in the following AWS Regions:
ap-northeast-1, ap-southeast-1, eu-central-1, eu-west-1, us-east-1,
us-west-2.

## Important notes for transport security in

AWS IoT Core

For devices that connect to AWS IoT Core using [MQTT](mqtt.md "mqtt.md"), TLS encrypts the connection
between the devices and the broker, and AWS IoT Core uses TLS client authentication to
identify devices. For more information, see [Client
authentication](client-authentication.md "client-authentication.md"). For devices that connect to AWS IoT Core using [HTTP](http.md "http.md"), TLS
encrypts the connection between the devices and the broker, and authentication is
delegated to AWS Signature Version 4. For more information, see [Signing
requests with Signature Version 4](../../../general/latest/gr/create-signed-request.md "../../../general/latest/gr/create-signed-request.md") in the _AWS
General Reference_.

When you connect devices to AWS IoT Core, sending the [Server Name Indication (SNI)
extension](https://tools.ietf.org/html/rfc3546#section-3.1 "https://tools.ietf.org/html/rfc3546#section-3.1") is not required but highly recommended. To use features such as
[multi-account registration](x509-client-certs.md#multiple-account-cert "x509-client-certs.md#multiple-account-cert"), [custom domains](iot-custom-endpoints-configurable-custom.md "iot-custom-endpoints-configurable-custom.md"), [VPC endpoints](IoTCore-VPC.md "IoTCore-VPC.md"), and [configured TLS policies](iot-endpoints-tls-config.md "iot-endpoints-tls-config.md"), you must use the SNI extension and provide the
complete endpoint address in the `host_name` field. The
`host_name` field must contain the endpoint you are calling. That
endpoint must be one of the following:

- The `endpointAddress` returned by `aws iot describe-endpoint --endpoint-type iot:Data-ATS`
- The `domainName` returned by `aws iot describe-domain-configuration –-domain-configuration-name
"`domain_configuration_name`"`

Connections attempted by devices with the incorrect or invalid `host_name`
value will fail. AWS IoT Core will log failures to CloudWatch for the authentication type of
[Custom
Authentication](custom-authentication.md "custom-authentication.md").

AWS IoT Core doesn't support the [SessionTicket TLS extension](https://www.ietf.org/rfc/rfc5077.txt "https://www.ietf.org/rfc/rfc5077.txt").

## Transport security for LoRaWAN wireless devices

LoRaWAN devices follow the security practices described in [LoRaWAN ™ SECURITY: A White Paper Prepared for the LoRa Alliance™ by Gemalto,
Actility, and Semtech](https://lora-alliance.org/sites/default/files/2019-05/lorawan_security_whitepaper.pdf "https://lora-alliance.org/sites/default/files/2019-05/lorawan_security_whitepaper.pdf").

For more information about transport security with LoRaWAN devices, see [LoRaWAN
data and transport security](../../../iot-wireless/latest/developerguide/iot-lorawan-security.md "../../../iot-wireless/latest/developerguide/iot-lorawan-security.md").
