AWS Systems Manager Incident Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Incident Manager,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Working with AWS Systems Manager Incident Manager and interface VPC

endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and AWS Systems Manager Incident Manager by creating an
_interface VPC endpoint_. Interface endpoints are powered by
AWS PrivateLink. With AWS PrivateLink, you can privately access Incident Manager API operations without
an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.. Instances in your
VPC don't need public IP addresses to communicate with Incident Manager API operations. Traffic
between your VPC and Incident Manager stays within the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Incident Manager VPC

endpoints

Before you set up an interface VPC endpoint for Incident Manager, ensure that you review [Interface
endpoint properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") and [AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md") in the
_Amazon VPC User Guide_.

Incident Manager supports making calls to all of its API actions from your VPC. To use all of
Incident Manager, you must create two VPC endpoints: one for `ssm-incidents` and one
for `ssm-contacts`.

## Creating an interface VPC endpoint for

Incident Manager

You can create a VPC endpoint for Incident Manager using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface
endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Incident Manager using supported service names for Incident Manager in
your AWS Region. The following examples show the interface endpoint formats for IPv4 and
dual-stack endpoints.

IPv4 endpoint formats

- `com.amazonaws.`region`.ssm-incidents`
- `com.amazonaws.`region`.ssm-contacts`

Dual-stack (IPv4 and IPv6) endpoint formats

- `aws.api.`region`.ssm-incidents`
- `aws.api.`region`.ssm-contacts`

For lists of supported endpoints for all Regions, see [AWS Systems Manager Incident Manager endpoints and
quotas](../../../general/latest/gr/incident-manager.md "../../../general/latest/gr/incident-manager.md") in the _AWS General Reference Guide_.

If you enable private DNS for the interface endpoint, you can make API requests to
Incident Manager using its default Regional DNS names in the format. The following examples show
the default Regional DNS names format.

- `ssm-incidents.`region`.amazonaws.com`
- `ssm-contacts.`region`.amazonaws.com`

For more information, see [Accessing a
service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for Incident Manager

You can attach an endpoint policy to your VPC endpoint that controls access to
Incident Manager. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which these actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Incident Manager actions

The following is an example of an endpoint policy for Incident Manager. When attached to an
endpoint, this policy grants access to the listed Incident Manager actions for all principals on
all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`ssm-contacts`:`ListContacts`",
            "`ssm-incidents`:`ListResponsePlans`",
            "`ssm-incidents`:`StartIncident`"
         ],
         "Resource":"*"
      }
   ]
}
```
