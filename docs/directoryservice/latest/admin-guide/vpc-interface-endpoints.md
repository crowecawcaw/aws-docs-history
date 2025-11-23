# Directory Service API and interface Amazon VPC endpoints using

AWS PrivateLink

You can use AWS PrivateLink
to create a private connection
between your VPC and Directory Service and Directory Service Data APIs.
This allows you
to access Directory Service and Directory Service Data APIs
like they were
in your VPC
and
without the use
of an internet gateway, NAT device, VPN connection, or Direct Connect connection.
Instances
in your Amazon VPC
don't require public IP addresses
to access Directory Service and Directory Service Data APIs.

To establish a private connection,
you create an interface Amazon VPC endpoint
that AWS PrivateLink powers.
We create an endpoint network interface
in each subnet
that you enable
for the interface endpoint.
These are requester-managed network interfaces,
which serve
as the entry point
for traffic
that's destined
for AWS Directory Service and AWS Directory Service Data.

For more information,
see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md")
in the _AWS PrivateLink Guide_.

## Considerations for Directory Service and Directory Service Data

With Directory Service and Directory Service Data,
you can call API actions
through interface endpoints.
For information
about the prerequisites
you will need
to consider
before creating an interface endpoint,
see [Access an AWS service using an interface Amazon VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints")
in the _AWS PrivateLink Guide_.

## Directory Service and Directory Service Data Availability

Directory Service and Directory Service Data supports interface endpoints in all AWS Regions where it's available.
For information about the AWS Regions that support Directory Service and Directory Service Data, see [Region availability for Directory Service](regions.md "regions.md").

## Create an interface Amazon VPC endpoint for Directory Service and Directory Service Data

You can create an interface endpoint for Directory Service and Directory Service Data APIs using the Amazon VPC console or the AWS Command Line Interface (AWS CLI).

###### Example: Directory Service

Create an interface endpoint for Directory Service APIs using the following service name:

```
com.amazonaws.`region`.ds
```

###### Example: Directory Service Data

Create an interface endpoint for Directory Service Data APIs using the following service name:

```
com.amazonaws.`region`.ds-data
```

For more information about creating an interface endpoint, see [Access an AWS service using an interface Amazon VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

## Create a Amazon VPC endpoint policy for your interface Amazon VPC endpoint

An endpoint policy is an IAM resource policy that you attach to an interface endpoint.

###### Note

If you don't attach an endpoint policy to your interface endpoint,
AWS PrivateLink attaches a default endpoint policy to your interface endpoint on your behalf.
For more information, see [AWS PrivateLink concepts](../../../vpc/latest/privatelink/concepts.md "../../../vpc/latest/privatelink/concepts.md").

An endpoint policy specifies the following information:

- The principals (AWS accounts, IAM users, and IAM roles) that can perform actions
- The actions that can be performed
- The resources on which the actions can be performed

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.

You can control access to APIs from your Amazon VPC by attaching a custom endpoint policy to your interface endpoint.

###### Example: Amazon VPC endpoint policy for Directory Service API actions

The following is an example of a custom endpoint policy.
When you attach this policy to your interface endpoint, it grants access to the listed Directory Service actions for all principals on all resources.

Replace `action-1`, `action-2`, and `action-3` with the required permissions for the Directory Service APIs that you want to include in your policy.
For a full list, see [Directory Service API permissions: Actions,
resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md").

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "ds:`action-1`",
            "ds:`action-2`",
            "ds:`action-3`"
         ],
         "Resource":"*"
      }
   ]
}
```

###### Example: Amazon VPC endpoint policy for Directory Service Data API actions

The following is an example
of a custom endpoint policy.
When you attach this policy
to your interface endpoint,
it grants access
to the listed Directory Service Data actions
for all principals
on all resources.

Replace `action-1`,
`action-2`, and `action-3`
with the required permissions for the Directory Service Data APIs
that you want to include
in your policy.
For a full list,
see [Directory Service API permissions: Actions,
resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md").

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "ds-data:`action-1`",
            "ds-data:`action-2`",
            "ds-data:`action-3`"
         ],
         "Resource":"*"
      }
   ]
}
```
