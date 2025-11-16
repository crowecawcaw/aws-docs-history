# Using AWS IoT Device Management secure tunneling with interface VPC

endpoints

AWS IoT Device Management secure tunneling supports interface VPC endpoints. You can use VPC endpoints to
keep traffic between your VPC and AWS IoT Secure Tunneling within the AWS network, without
requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect
connection.

Interface VPC endpoints are powered by [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md"), a
technology that enables you to privately access services by using private IP addresses. For
more information, see [Access an AWS service
using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the AWS PrivateLink Guide.

###### Contents

- [Prerequisites](#Create-ST-VPC-endpoints-prereq "#Create-ST-VPC-endpoints-prereq")
- [Receiving tunnel notifications through
  VPC endpoints](#ST-VPC-Receive-notifications "#ST-VPC-Receive-notifications")
- [Creating VPC endpoints for secure
  tunneling](#Create-ST-VPC-endpoints-Create "#Create-ST-VPC-endpoints-Create")
- [Configuring VPC endpoint policies on
  Proxy Server](#Create-ST-VPC-endpoints-Configure "#Create-ST-VPC-endpoints-Configure")
- [Next steps](#Create-ST-VPC-endpoints-Next "#Create-ST-VPC-endpoints-Next")

## Prerequisites

Before you create VPC endpoints for AWS IoT Secure Tunneling, verify that you have the
following:

- An AWS account with the necessary permissions to create VPC
  endpoints.
- A VPC in your AWS account.
- Understanding of AWS IoT Device Management secure tunneling concepts.
- Familiarity with VPC endpoint policies and AWS Identity and Access Management (IAM)

## Receiving tunnel notifications through

VPC endpoints

To receive tunnel notifications through a VPC endpoint, your devices can connect to
the AWS IoT Core data plane through a VPC endpoint and subscribe to the secure tunneling
reserved MQTT topic.

For instructions on how to create and configure a VPC endpoint in the AWS IoT Core data
plane, see [Using AWS IoT Core with interface VPC endpoints](IoTCore-VPC.md "IoTCore-VPC.md") in the AWS IoT Developer Guide.

## Creating VPC endpoints for secure

tunneling

You can create VPC endpoints for both secure tunneling control plane and proxy
server.

###### To create a VPC endpoint for secure tunneling

1. Follow the steps in [Creating an
   interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the Amazon VPC Developer Guide
2. For **Service name**, choose one of the following options
   based on your endpoint type:

###### Control plane

    * Standard:
     `com.amazonaws.<region>.iot.tunneling.api`
    * FIPS (available in FIPS regions):
     `com.amazonaws.<region>.iot-fips.tunneling.api`

###### Proxy server

    * Standard:
     `com.amazonaws.<region>.iot.tunneling.data`
    * FIPS (available in FIPS regions):
     `com.amazonaws.<region>.iot-fips.tunneling.data`

Replace `<region>` with your AWS Region. For
example, `us-east-1`. 3. Complete the remaining steps in the VPC endpoint creation process according to
your network requirements.

## Configuring VPC endpoint policies on

Proxy Server

In addition to client access token-based authorization that is used to authorize
connections to tunnels, you can use VPC endpoint policies to further restrict how
devices can use a VPC endpoint to connect to the Secure Tunneling Proxy Server. VPC
endpoint policies follow an IAM-like syntax and are configured on the VPC endpoint
itself.

Note that the only supported IAM action for proxy server VPC endpoint policies is
`iot:ConnectToTunnel`.

Below are examples of different VPC endpoint policies.

### Proxy server VPC endpoint policy examples

The following examples show Proxy Server VPC endpoint policy configurations for
common use cases.

###### Example - Default policy

This policy allows devices within your VPC to connect to any tunnel in the
same AWS Region where the endpoint is created, across any AWS
account.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

###### Example - Restrict access to specific AWS accounts

This policy allows the VPC endpoint to connect only to tunnels in specific
AWS accounts.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "iot:ConnectToTunnel",
            "Resource": [
                "arn:aws:iot:us-east-1:111122223333:tunnel/*",
                "arn:aws:iot:us-east-1:444455556666:tunnel/*"
            ]
        }
    ]
}
```

###### Example - Restrict connections by tunnel endpoint

You can restrict VPC endpoint access to only allow devices to connect to the
source or destination end of a tunnel.

Source only:

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "iot:ConnectToTunnel",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iot:ClientMode": "source"
                }
            }
        }
    ]
}
```

Destination only:

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "iot:ConnectToTunnel",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iot:ClientMode": "destination"
                }
            }
        }
    ]
}
```

###### Example - Restrict access based on resource tags

This policy allows the VPC endpoint to connect only to tunnels that are tagged
with a specific key-value pair.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "iot:ConnectToTunnel",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/Environment": "Production"
                }
            }
        }
    ]
}
```

###### Example - Combined policy conditions

This policy demonstrates combining multiple policy elements. It allows
connections to any tunnel in a specific AWS account, but only if the tunnel is
tagged with `AllowConnectionsThroughPrivateLink` set to
`true` and the client is not connecting to the destination end of
the tunnel.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "iot:ConnectToTunnel",
            "Resource": [
                "arn:aws:iot:us-east-1:111122223333:tunnel/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/AllowConnectionsThroughPrivateLink": "true"
                }
            }
        },
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "iot:ConnectToTunnel",
            "Resource": [
                "arn:aws:iot:us-east-1:111122223333:tunnel/*"
            ],
            "Condition": {
                "StringEquals": {
                    "iot:ClientMode": "destination"
                }
            }
        }
    ]
}
```

## Next steps

After you create and configure your VPC endpoints for AWS IoT Secure Tunneling, consider the
following:

- Test your VPC endpoint configuration by connecting devices through the
  endpoint.
- Monitor VPC endpoint usage through Amazon CloudWatch metrics.
- Review and update your VPC endpoint policies as needed for your security
  requirements.

For more information about AWS IoT Device Management secure tunneling, see [AWS IoT Secure Tunneling](secure-tunneling.md "secure-tunneling.md").
