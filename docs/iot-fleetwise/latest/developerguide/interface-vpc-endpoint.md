

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Connecting to AWS IoT FleetWise through an interface VPC endpoint
<a name="interface-vpc-endpoint"></a>

You can connect directly to AWS IoT FleetWise by using an [interface VPC endpoint (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpce-interface.html) in your Virtual Private Cloud (VPC), instead of connecting over the internet. When you use an interface VPC endpoint, communication between your VPC and AWS IoT FleetWise is conducted entirely within the AWS network. Each VPC endpoint is represented by one or more [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) (ENIs) with private IP addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to AWS IoT FleetWise without an internet gateway, NAT device, VPN connection, or Direct Connect connection. The instances in your VPC don't need public IP addresses to communicate with the AWS IoT FleetWise API.

To use AWS IoT FleetWise through your VPC, you must connect from an instance that is inside the VPC or connect your private network to your VPC by using an AWS Virtual Private Network (VPN) or Direct Connect. For information about Amazon VPN, see [VPN connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html) in the *Amazon Virtual Private Cloud User Guide*. For information about AWS Direct Connect, see [Creating a connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-connection.html) in the *Direct Connect User Guide*.

You can create an interface VPC endpoint to connect to AWS IoT FleetWise by using the AWS console or AWS Command Line Interface (AWS CLI) commands. For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpce-interface.html#create-interface-endpoint).

After you create an interface VPC endpoint, if you enable private DNS hostnames for the endpoint, the default AWS IoT FleetWise endpoint resolves to your VPC endpoint. The default service name endpoint for AWS IoT FleetWise is in the following format.

```
iotfleetwise.{{Region}}.amazonaws.com
```

If you don't enable private DNS hostnames, Amazon VPC provides a DNS endpoint name that you can use in the following format.

```
{{VPCE_ID}}.iotfleetwise.{{Region}}.vpce.amazonaws.com
```

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*.

AWS IoT FleetWise supports making calls to all of its [API actions](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_Operations.html) inside your VPC.

You can attach VPC endpoint policies to a VPC endpoint to control access for IAM principals. You can also associate security groups with a VPC endpoint to control inbound and outbound access based on the origin and destination of network traffic, such as a range of IP addresses. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html).

**Note**  
AWS IoT FleetWise supports all VPC endpoints with dual-stack mode. For information about service endpoints, see [AWS IoT FleetWise endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iotfleetwise.html).

## Creating a VPC endpoint policy for AWS IoT FleetWise
<a name="api-private-link-policy"></a>

You can create a policy for Amazon VPC endpoints for AWS IoT FleetWise to specify the following:
+ The principal that can or can't perform actions
+ The actions that can or can't be performed

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

**Example – VPC endpoint policy to deny all access from a specified AWS account**  
The following VPC endpoint policy denies AWS account {{123456789012}} all API calls using the endpoint.  

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
                    "{{123456789012}}"
                ]
            }
        }
    ]
}
```

**Example – VPC endpoint policy to allow VPC access only to a specified IAM principal (user)**  
The following VPC endpoint policy allows full access only to the a user {{lijuan}} in AWS account {{123456789012}}. It denies all other IAM principals access to the endpoint.  

```
{
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::{{123456789012}}:user/{{lijuan}}"
                ]
            }
        }]
}
```

**Example – VPC endpoint policy for AWS IoT FleetWise actions**  
The following is an example of an endpoint policy for AWS IoT FleetWise. When attached to an endpoint, this policy grants access to the listed AWS IoT FleetWise actions for the IAM user {{fleetWise}} in the AWS account {{123456789012}}.  

```
{
    "Statement": [
        {
             "Principal": {
                "AWS": [
                    "arn:aws:iam::{{123456789012}}:user/{{fleetWise}}"
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