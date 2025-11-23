# AWS HealthLake and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and AWS HealthLake by creating an
_interface VPC endpoint_. Interface VPC endpoints are powered by
[AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that you
can use to privately access HealthLake; APIs without an internet gateway, NAT device, VPN
connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to
communicate with HealthLake; APIs. Traffic between your VPC and HealthLake; does not
leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for HealthLake VPC

endpoints

Before you set up an interface VPC endpoint for HealthLake, be sure you review
[Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

HealthLake supports making calls to all of its API actions from your VPC.

## Creating an interface VPC endpoint for

HealthLake;

You can create a VPC endpoint for the HealthLake; service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for HealthLake; using the following service name:

- com.amazonaws.`region`.healthlake

If you turn on private DNS for the endpoint, you can make API requests to HealthLake
using its default DNS name for the Region. For example, `*healthlake.us-east-1.amazonaws.com*`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

HealthLake

You can attach an endpoint policy to your VPC endpoint that controls access to
HealthLake. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for HealthLake actions

The following is an example of an endpoint policy for HealthLake. When attached
to an endpoint, this policy grants access to the HealthLake
`CreateFHIRDatastore` action for all principals on all
resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`healthlake`:`create-fhir-datastore`"
         ],
         "Resource":"*"
      }
   ]
}
```
