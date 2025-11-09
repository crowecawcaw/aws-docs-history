# Making requests to AWS IoT FleetWise using IPv6

You can communicate with AWS IoT FleetWise over Internet Protocol version 6 (IPv6) and IPv4 to manage your resources. Dual-stack
endpoints support requests to AWS IoT FleetWise APIs over IPv6 and IPv4. There are no additional
charges for communication over IPv6.

The IPv6 protocol is the next generation IP standard with additional security features.
It offers 128-bit long address space while IPv4 has 32-bit long address. IPv4 can generate
4.29 x 10^9 addresses while IPv6 can have 3.4 x 10^38 addresses.

## IPv6 prerequisites for control plane endpoints

IPv6 protocol support is automatically enabled for control plane endpoints. When using the endpoints for control plane clients, you
must provide the [Server Name
Indication (SNI) extension](https://www.rfc-editor.org/rfc/rfc3546#section-3.1 "https://www.rfc-editor.org/rfc/rfc3546#section-3.1"). Clients can use the SNI extension to indicate the name
of the server being contacted, and whether it's using the regular endpoints or the dual-stack
endpoints. See [Using dual-stack endpoints](#fleetwise-ipv6-dualstack "#fleetwise-ipv6-dualstack").

## IPv6 support for AWS PrivateLink endpoints

AWS IoT FleetWise supports IPv6 communication to interface VPC endpoints using
AWS PrivateLink.

## Testing IPv6 address compatibility

If you're using use Linux/Unix or Mac OS X, you can test whether you can access a
dual-stack endpoint over IPv6 by using the curl command as shown in the following
example:

```
curl -v https://iotfleetwise.`<us-east-1>`.api.aws
```

You get back information similar to the following example. If you're connected over IPv6,
the connected IP address will be an IPv6 address.

```
* Host iotfleetwise.us-east-1.api.aws:443 was resolved.
* IPv6: ::ffff:3.82.78.135, ::ffff:54.211.220.216, ::ffff:54.211.201.157
* IPv4: (none)
*   Trying [::ffff:3.82.78.135]:443...
* Connected to iotfleetwise.us-east-1.api.aws (::ffff:3.82.78.135) port 443
* ALPN: curl offers h2,http/1.1
```

If you're using Microsoft Windows 7 or Windows 10, you can test whether you can access a
dual-stack endpoint over IPv6 or IPv4 by using the ping command as shown in the following
example.

```
ping iotfleetwise.`<us-east-1>`.api.aws
```

## Using IPv6 addresses in IAM policies

Before you use IPv6 for your resources, you must ensure that any IAM
polices that are used for IP address filtering include IPv6 address ranges. For more
information about managing access permissions with IAM, see [Identity and Access Management for AWS IoT FleetWise](security-iam.md "security-iam.md").

IAM policies that filter IP addresses use [IP Address
Condition Operators](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress"). The following policy identifies the `54.240.143.*`
range of allowed IPv4 addresses by using IP address condition operators. Since all IPv6
addresses are outside the allowed range, this policy prevents communication using IPv6
addresses.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IPAllow",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "iotfleetwise:*",
 "Resource": "arn:aws:iotfleetwise:`us-east-1`:`111122223333`:*",
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

AWS IoT FleetWise dual-stack endpoints support requests to AWS IoT FleetWise APIs over IPv6
and IPv4. When you make a request to a dual-stack endpoint, it automatically resolves to an
IPv4 or an IPv6 address. In the dual-stack mode, both IPv4 and IPv6 client connections are
accepted.

If you're using the REST API, you can directly access an AWS IoT FleetWise endpoint by
using the endpoint name (URI). AWS IoT FleetWise supports only regional dual-stack endpoint
names, which means that you must specify the AWS Region as part of the name.

The following table shows the format of control plane endpoints for
AWS IoT FleetWise when using IPv4 and the dual-stack modes. For more information about these
endpoints, see [AWS IoT FleetWise endpoints](../../../general/latest/gr/iotfleetwise.md "../../../general/latest/gr/iotfleetwise.md").

| Endpoint      | IPv4 address                          | Dual-stack mode                 |
| ------------- | ------------------------------------- | ------------------------------- |
| Control plane | iotfleetwise.`<region>`.amazonaws.com | iotfleetwise.`<region>`.api.aws |

When using the AWS CLI and AWS SDKs, you can use a `AWS_USE_DUALSTACK_ENDPOINT` environment
variable, or the `use_dualstack_endpoint` parameter, which is a shared config file setting, to
change to a dual-stack endpoint. You can also specify the dual-stack endpoint directly as an override of the
AWS IoT FleetWise endpoint in the config file. For more information, see [Dual-stack and FIPS endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md").

When you use the AWS CLI, you can set the configuration value `use_dualstack_endpoint` as
`true` in a profile in your AWS Config file. This will direct all AWS IoT FleetWise requests
made by the commands to the dual-stack endpoint for the specified region. You specify the region in the
config file or in a command using the `--region` option.

```
$ aws configure set default.iotfleetwise.use_dualstack_endpoint true
```

Instead of using the dual-stack endpoints for all commands, to use these endpoints for specific
commands:

- You can use the dual-stack endpoint for specific commands by setting the `--endpoint-url`
  parameter for those commands. For example, in the following command, you can replace the
  `<endpoint-url>` to
  `iotfleetwise.`<region>`.api.aws`.

```
aws iotfleetwise list-fleets \
  --endpoint-url `<endpoint-url>`
```

- You can set up separate profiles in your AWS Config file. For example, create
  one profile that sets `use_dualstack_endpoint` to true, and a profile that
  does not set `use_dualstack_endpoint`. When you run a command, specify
  which profile you want to use, depending upon whether or not you want to use the
  dual-stack endpoint.
