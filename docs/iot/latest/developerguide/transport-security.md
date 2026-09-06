

# Transport security in AWS IoT Core
<a name="transport-security"></a>

TLS (Transport Layer Security) is a cryptographic protocol that is designed for secure communication over a computer network. The AWS IoT Core Device Gateway requires customers to encrypt all communication while in-transit by using TLS for connections from devices to the Gateway. TLS is used to achieve confidentiality of the application protocols (MQTT, HTTP, and WebSocket) supported by AWS IoT Core. TLS support is available in a number of programming languages and operating systems. Data within AWS is encrypted by the specific AWS service. For more information about data encryption on other AWS services, see the security documentation for that service.

**Topics**
+ [TLS protocols](#tls-ssl-policy)
+ [Security policies](#tls-policy-table)
+ [Important notes for transport security in AWS IoT Core](#tls-ssl-core)
+ [Transport security for LoRaWAN wireless devices](#tls-lorawan)

## TLS protocols
<a name="tls-ssl-policy"></a>

AWS IoT Core supports the following versions of the TLS protocol:
+ TLS 1.3 
+ TLS 1.2

With AWS IoT Core, you can configure the TLS settings (for [TLS 1.2](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.2) and [TLS 1.3](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3)) in domain configurations. For more information, see [Configuring TLS settings in domain configurations](iot-endpoints-tls-config.md).

## Security policies
<a name="tls-policy-table"></a>

A security policy is a combination of TLS protocols and their ciphers that determine which protocols and ciphers are supported during TLS negotiations between a client and a server. You can configure your devices to use predefined security policies based on your needs. Note that AWS IoT Core doesn't support custom security policies.

You can choose one of the predefined security policies for your devices when connecting them to AWS IoT Core. The names of the most recent predefined security policies in AWS IoT Core include version information based on the year and month that they were released. The default predefined security policy for non-AWS GovCloud (US) regions is `IoTSecurityPolicy_TLS13_1_2_2022_10` and `IoTSecurityPolicy_TLS13_1_2_2022_01` for AWS GovCloud (US) regions. To specify a security policy, you can use the AWS IoT console or the AWS CLI. For more information, see [Configuring TLS settings in domain configurations](iot-endpoints-tls-config.md).

The following table describes the most recent predefined security policies that AWS IoT Core supports. The `IotSecurityPolicy_` has been removed from policy names in the heading row so that they fit.


<table>
<thead>
  <tr><th><b>Security policy</b></th><th>TLS13_1_3_2022_10</th><th>TLS13_1_2_2022_10</th><th>TLS12_1_2_2022_10</th><th colspan="2">TLS12_1_0_2016_01*</th><th colspan="2">TLS12_1_0_2015_01*</th><th>TLS13_1_2_2022_01*</th></tr>
</thead>
<tbody>
  <tr><td><b>TCP Port</b></td><td>443/8443/8883</td><td>443/8443/8883</td><td>443/8443/8883</td><td>443</td><td>8443/8883</td><td>443</td><td>8443/8883</td><td>443/8443/8883</td></tr>
  <tr><td colspan="9"><b>TLS Protocols</b></td></tr>
  <tr><td>TLS 1.2</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>TLS 1.3</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td>✓</td></tr>
  <tr><td colspan="9"><b>TLS Ciphers</b></td></tr>
  <tr><td>TLS_AES_128_GCM_SHA256</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td>✓</td></tr>
  <tr><td>TLS_AES_256_GCM_SHA384</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td>✓</td></tr>
  <tr><td>TLS_CHACHA20_POLY1305_SHA256</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES128-GCM-SHA256</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA256</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-RSA-AES256-GCM-SHA384</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA384</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>AES128-GCM-SHA256</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td></tr>
  <tr><td>AES128-SHA256</td><td></td><td>✓</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td></tr>
  <tr><td>AES128-SHA</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>AES256-GCM-SHA384</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td></tr>
  <tr><td>AES256-SHA256</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td></tr>
  <tr><td>AES256-SHA</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>DHE-RSA-AES256-SHA</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES128-GCM-SHA256</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA256</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-GCM-SHA384</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA384</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
</tbody>
</table>


**Note**  
`TLS12_1_0_2016_01` is only available in the following AWS Regions: ap-east-1, ap-northeast-2, ap-south-1, ap-southeast-2, ca-central-1, cn-north-1, cn-northwest-1, eu-north-1, eu-west-2, eu-west-3, me-south-1, sa-east-1, us-east-2, us-west-1.  
`TLS12_1_0_2015_01` is only available in the following AWS Regions: ap-northeast-1, ap-southeast-1, eu-central-1, eu-west-1, us-east-1, us-west-2.  
`TLS13_1_2_2022_01` is only available in AWS GovCloud (US) regions.

## Important notes for transport security in AWS IoT Core
<a name="tls-ssl-core"></a>

For devices that connect to AWS IoT Core using [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html), TLS encrypts the connection between the devices and the broker, and AWS IoT Core uses TLS client authentication to identify devices. For more information, see [Client authentication](https://docs.aws.amazon.com/iot/latest/developerguide/client-authentication.html). For devices that connect to AWS IoT Core using [HTTP](https://docs.aws.amazon.com/iot/latest/developerguide/http.html), TLS encrypts the connection between the devices and the broker, and authentication is delegated to AWS Signature Version 4. For more information, see [Signing requests with Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/create-signed-request.html) in the *AWS General Reference*.

When you connect devices to AWS IoT Core, sending the [Server Name Indication (SNI) extension](https://tools.ietf.org/html/rfc3546#section-3.1) is not required but highly recommended. To use features such as [multi-account registration](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html#multiple-account-cert), [custom domains](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-custom.html), [VPC endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-VPC.html), and [configured TLS policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-endpoints-tls-config.html), you must use the SNI extension and provide the complete endpoint address in the `host_name` field. The `host_name` field must contain the endpoint you are calling. That endpoint must be one of the following:
+ The `endpointAddress` returned by `aws iot [describe-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-endpoint.html) --endpoint-type iot:Data-ATS`
+ The `domainName` returned by `aws iot [describe-domain-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html) –-domain-configuration-name "{{domain_configuration_name}}"`

Connections attempted by devices with the incorrect or invalid `host_name` value will fail. AWS IoT Core will log failures to CloudWatch for the authentication type of [Custom Authentication](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html).

AWS IoT Core doesn't support the [SessionTicket TLS extension](https://www.ietf.org/rfc/rfc5077.txt).

## Transport security for LoRaWAN wireless devices
<a name="tls-lorawan"></a>

LoRaWAN devices follow the security practices described in [LoRaWAN ™ SECURITY: A White Paper Prepared for the LoRa Alliance™ by Gemalto, Actility, and Semtech](https://lora-alliance.org/sites/default/files/2019-05/lorawan_security_whitepaper.pdf). 

For more information about transport security with LoRaWAN devices, see [LoRaWAN data and transport security](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan-security.html).