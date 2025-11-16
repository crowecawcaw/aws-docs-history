# Making requests to AWS IoT Wireless using IPv6

AWS IoT Wireless supports the ability for wireless resources to communicate with the cloud
using the internet protocol version 6 (IPv6), in addition to the IPv4 protocol. Dual-stack
endpoints support requests to AWS IoT Wireless over IPv6 and IPv4. There are no additional
charges for communication over IPv6.

The IPv6 protocol is the next generation IP standard with additional security features.
It offers 128-bit long address space while IPv4 has 32-bit long address. IPv4 can generate
4.29 x 10^9 addresses while IPv6 can have 3.4 x 10^38 addresses.

## IPv6 pre-requisites for control plane endpoints

For control plane endpoints, IPv6 protocol support is enabled automatically and
you can use the dual-stack endpoints. When using the endpoints for control plane clients, you
must provide the [Server Name
Indication (SNI) extension](https://www.rfc-editor.org/rfc/rfc3546#section-3.1 "https://www.rfc-editor.org/rfc/rfc3546#section-3.1"). The clients can use the SNI extension to indicate the name
of the server being contacted, and whether it's using the regular endpoints or the dual-stack
endpoints. See [Using dual-stack endpoints](#iot-wireless-ipv6-dualstack "#iot-wireless-ipv6-dualstack").

## IPv6 activation for data plane endpoints

For LNS and CUPS data plane endpoints, if you're onboarding new gateways or devices after
December 1st, 2024, they will automatically use the dual-stack endpoints.

For any gateways that have already onboarded to AWS IoT Core for LoRaWAN before December 1st, 2024,
you must request IPv6 activation to use the dual-stack endpoints. By default,
these gateways are configured to support IPv4 traffic.

Before requesting activation, we recommend that you first validate that the system
works seamlessly with IPv6. For more information, see [Testing IPv6 address compatibility](#iot-wireless-ipv6-compatibilty "#iot-wireless-ipv6-compatibilty"). You can then go to the [Gateways hub](https://console.aws.amazon.com/iot/home#/wireless/gateways "https://console.aws.amazon.com/iot/home#/wireless/gateways") in the AWS IoT console,
and choose **request IPv6 protocol activation**. You can also request IPv6
activation from the [feature spotlight](https://console.aws.amazon.com/iot/home#/featurespotlight "https://console.aws.amazon.com/iot/home#/featurespotlight")
page.

## IPv6 support for PrivateLink endpoints

AWS IoT Core for LoRaWAN supports IPv6 communication to interface VPC endpoints using
AWS PrivateLink. For more information, see [AWS IoT Core for LoRaWAN and interface VPC endpoints
(AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

## Testing IPv6 address compatibility

If you are using use Linux/Unix or Mac OS X, you can test whether you can access a
dual-stack endpoint over IPv6 by using the curl command as shown in the following
example:

```
curl -v https://api.iotwireless.`<us-east-1>`.api.aws
```

You get back information similar to the following example. If you are connected over IPv6,
the connected IP address will be an IPv6 address.

```

* About to connect() to iotwireless-us-east-1.amazonaws.com port 80 (#0)
*   Trying IPv6 address... connected
* Connected to iotwireless.dualstack.us-east-1.amazonaws.com (IPv6 address) port 80 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.18.1 (x86_64-unknown-linux-gnu) libcurl/7.18.1 OpenSSL/1.0.1t zlib/1.2.3
> Host: iotwireless.dualstack.us-east-1.amazonaws.com
```

If you are using Microsoft Windows 7 or Windows 10, you can test whether you can access a
dual-stack endpoint over IPv6 or IPv4 by using the ping command as shown in the following
example.

```
ping https://iotwireless.`<us-east-1>`.api.aws
```

## Using IPv6 addresses in IAM policies

Before you use IPv6 for your wireless resources, you must ensure that any IAM
polices that are used for IP address filtering include IPv6 address ranges. For more
information about managing access permissions with IAM, see [Identity and access management for AWS IoT Wireless](security-iam.md "security-iam.md").

IAM policies that filter IP addresses use [IP Address
Condition Operators](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress"). The following policy identifies the `54.240.143.*`
range of allowed IPv4 addresses by using IP address condition operators. Since all IPv6
addresses are outside the allowed range, this policy prevents communication using IPv6
addresses.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IPAllow",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "iotwireless:*",
 "Resource": "arn:aws:iotwireless:`us-east-1`:`111122223333`:*",
 "Condition": {
 "IpAddress": {"aws:SourceIp": "54.240.143.0/24"}
 }
 }
 ]
}`

```

To include IPv6 addresses, you can modify the policy's Condition element to allow both
IPv4 (54.240.143.0/24) and IPv6 (2001:DB8:1234:5678::/64) address ranges as shown in the
following example.

```

  "Condition": {
    "IpAddress": {
      "aws:SourceIp": [
        "54.240.143.0/24",
        "2001:DB8:1234:5678::/64"
      ]
    }
  }
```

## Using dual-stack endpoints

AWS IoT Wireless dual-stack endpoints support requests to AWS IoT Wireless over IPv6
and IPv4. When you make a request to a dual-stack endpoint, it automatically resolves to an
IPv4 or an IPv6 address. In the dual-stack mode, both IPv4 and IPv6 client connections will be
accepted.

If you're using the REST API, you can directly access an AWS IoT Wireless endpoint by
using the endpoint name (URI). AWS IoT Wireless supports only regional dual-stack endpoint
names, which means that you must specify the AWS Region as part of the name.

The following table shows the format of the control plane and data plane endpoints for
AWS IoT Wireless when using IPv4 and the dual-stack modes. For more information about these
endpoints, see [AWS IoT Wireless endpoints](../../../general/latest/gr/iot-lorawan.md#iot-wireless_region "../../../general/latest/gr/iot-lorawan.md#iot-wireless_region").

| Dual-stack endpoints for AWS IoT Wireless | Endpoint                                         | IPv4 address                                     | Dual-stack mode |
| ----------------------------------------- | ------------------------------------------------ | ------------------------------------------------ | --------------- |
| Control plane                             | api.iotwireless.`<region>`.amazonaws.com         | api.iotwireless.`<region>`.api.aws               |
| LNS (Data plane)                          | `<prefix>`.lns.lorawan.`<region>`.amazonaws.com  | `<prefix>`.lns.lorawan.`<region>`.amazonaws.com  |
| CUPS (Data plane)                         | `<prefix>`.cups.lorawan.`<region>`.amazonaws.com | `<prefix>`.cups.lorawan.`<region>`.amazonaws.com |

When using the AWS CLI and AWS SDKs, you can use a `AWS_USE_DUALSTACK_ENDPOINT` environment
variable, or the `use_dualstack_endpoint` parameter, which is a shared config file setting, to
change to a dual-stack endpoint. You can also specify the dual-stack endpoint directly as an override of the
AWS IoT Wireless endpoint in the config file. For more information, see [Dual-stack and FIPS endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md").

When you use the AWS CLI, you can set the configuration value `use_dualstack_endpoint` as
`true` in a profile in your AWS Config file. This will direct all AWS IoT Wireless requests
made by the commands to the dual-stack endpoint for the specified region. You specify the region in the
config file or in a command using the `--region` option.

```
$ aws configure set default.iotwireless.use_dualstack_endpoint true
```

Instead of using the dual-stack endpoints for all commands, to use these endpoints for specific
commands:

- You can use the dual-stack endpoint for specific commands by setting the `--endpoint-url`
  parameter for those commands. For example, in the following command, you can replace the
  `<endpoint-url>` to
  `api.iotwireless.`<region>`.api.aws`.

```
aws iotwireless list-service-profiles \
  --endpoint-url `<endpoint-url>`
```

- You can set up separate profiles in your AWS Config file. For example, create
  one profile that sets `use_dualstack_endpoint` to true, and a profile that
  does not set `use_dualstack_endpoint`. When you run a command, specify
  which profile you want to use, depending upon whether or not you want to use the
  dual-stack endpoint.
