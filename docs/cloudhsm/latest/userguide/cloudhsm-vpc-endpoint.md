# AWS CloudHSM and VPC endpoints

You can establish a private connection between your VPC and AWS CloudHSM by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access AWS CloudHSM APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with AWS CloudHSM APIs. Traffic between your VPC and AWS CloudHSM
does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for AWS CloudHSM VPC

endpoints

Before you set up an interface VPC endpoint for AWS CloudHSM, ensure that you review
[Interface endpoint
properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

- AWS CloudHSM supports making calls to all of its API actions from your VPC.

## Creating an interface VPC endpoint for

AWS CloudHSM

You can create a VPC endpoint for the AWS CloudHSM service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

To create a VPC endpoint for AWS CloudHSM, use the following service name:

```
com.amazonaws.`<region>`.cloudhsmv2
```

For example, in the US West (Oregon) Region (`us-west-2`), the service name
would be:

```
com.amazonaws.us-west-2.cloudhsmv2
```

To make it easier to use the VPC endpoint, you can enable a [private DNS hostname](../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns "../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns") for
your VPC endpoint. If you select the **Enable Private DNS Name** option, the
standard AWS CloudHSM DNS hostnames
(`https://cloudhsmv2.`<region>`.amazonaws.com` and `https://cloudhsmv2.`<region>`.api.aws`) resolves
to your VPC endpoint.

This option makes it easier to use the VPC endpoint. The AWS SDKs and AWS CLI use the
standard AWS CloudHSM DNS hostname by default, so you do not need to specify the VPC endpoint URL in
applications and commands.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for AWS CloudHSM

You can attach an endpoint policy to your VPC endpoint that controls access to
AWS CloudHSM. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling
access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User
Guide_.

###### Example: VPC endpoint policy for AWS CloudHSM actions

The following is an example of an endpoint policy for AWS CloudHSM. When attached to an
endpoint, this policy grants access to the listed AWS CloudHSM actions for all principals
on all resources. See [Identity and access management for AWS CloudHSM](identity-access-management.md "identity-access-management.md") for other AWS CloudHSM actions and their corresponding IAM permissions.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`<cloudhsm>`:`<DescribeBackups>`",
            "`<cloudhsm>`:`<DescribeClusters>`",
            "`<cloudhsm>`:`<ListTags>`",
         ],
         "Resource":"*"
      }
   ]
}
```
