# Connecting to AWS IoT FleetWise through an

interface VPC endpoint

You can connect directly to AWS IoT FleetWise by using an [interface VPC
endpoint (AWS PrivateLink)](../../../AmazonVPC/latest/UserGuide/vpce-interface.md "../../../AmazonVPC/latest/UserGuide/vpce-interface.md") in your Virtual Private Cloud (VPC), instead of
connecting over the internet. When you use an interface VPC endpoint, communication
between your VPC and AWS IoT FleetWise is conducted entirely within the AWS network. Each
VPC endpoint is represented by one or more [Elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") (ENIs) with private IP addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to AWS IoT FleetWise without an
internet gateway, NAT device, VPN connection, or Direct Connect connection. The instances in
your VPC don't need public IP addresses to communicate with the AWS IoT FleetWise
API.

To use AWS IoT FleetWise through your VPC, you must connect from an instance that is inside
the VPC or connect your private network to your VPC by using an AWS Virtual Private Network (VPN) or Direct Connect. For information about Amazon VPN, see [VPN
connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the _Amazon Virtual Private Cloud User Guide_. For
information about AWS Direct Connect, see [Creating
a connection](../../../directconnect/latest/UserGuide/create-connection.md "../../../directconnect/latest/UserGuide/create-connection.md") in the _Direct Connect User Guide_.

You can create an interface VPC endpoint to connect to AWS IoT FleetWise by using the AWS
console or AWS Command Line Interface (AWS CLI) commands. For more information, see [Creating an interface endpoint](../../../AmazonVPC/latest/UserGuide/vpce-interface.md#create-interface-endpoint "../../../AmazonVPC/latest/UserGuide/vpce-interface.md#create-interface-endpoint").

After you create an interface VPC endpoint, if you enable private DNS hostnames for the endpoint, the default AWS IoT FleetWise endpoint
resolves to
your VPC endpoint. The default service name endpoint for AWS IoT FleetWise is in the following format.

```
iotfleetwise.`Region`.amazonaws.com
```

If you don't enable private DNS hostnames, Amazon VPC provides a DNS endpoint name that you
can use in the following format.

```
`VPCE_ID`.iotfleetwise.`Region`.vpce.amazonaws.com
```

For more information, see [Interface VPC endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.

AWS IoT FleetWise supports making calls to all of its [API actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") inside your VPC.

You can attach VPC endpoint policies to a VPC endpoint to control access for IAM
principals. You can also associate security groups with a VPC endpoint to control
inbound and outbound access based on the origin and destination of network traffic, such
as a range of IP addresses. For more information, see [Controlling access to services
with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md").

###### Note

AWS IoT FleetWise supports all VPC endpoints with dual-stack mode. For information about service endpoints, see [AWS IoT FleetWise endpoints and quotas](../../../general/latest/gr/iotfleetwise.md "../../../general/latest/gr/iotfleetwise.md").

## Creating a VPC endpoint policy for

AWS IoT FleetWise

You can create a policy for Amazon VPC endpoints for AWS IoT FleetWise to specify the following:

- The principal that can or can't perform actions
- The actions that can or can't be performed

For more information, see [Controlling
access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User
Guide_.

###### Example – VPC endpoint policy to deny all access from a specified AWS account

The following VPC endpoint policy denies AWS account
`123456789012` all API calls using the endpoint.

```
{
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        },
        {
            "Action": "*",
            "Effect": "Deny",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "`123456789012`"
                ]
            }
        }
    ]
}

```

###### Example – VPC endpoint policy to allow VPC access only to a specified IAM principal (user)

The following VPC endpoint policy allows full access only to the a user
`lijuan` in AWS account
`123456789012`. It denies all other IAM
principals access to the endpoint.

```
{
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::`123456789012`:user/`lijuan`"
                ]
            }
        }]
}

```

###### Example – VPC endpoint policy for AWS IoT FleetWise actions

The following is an example of an endpoint policy for AWS IoT FleetWise. When attached to an
endpoint, this policy grants access to the listed AWS IoT FleetWise actions for the
IAM user `fleetWise` in the AWS account
`123456789012`.

```
{
    "Statement": [
        {
             "Principal": {
                "AWS": [
                    "arn:aws:iam::`123456789012`:user/`fleetWise`"
                },
            "Resource": "*",
            "Effect": "Allow",
            "Action": [
                "iotfleetwise:ListFleets",
                "iotfleetwise:ListCampaigns",
                "iotfleetwise:CreateVehicle",
            ]
           }
    ]
}
```
