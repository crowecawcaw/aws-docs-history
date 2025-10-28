# Share your VPC Lattice entities

Amazon VPC Lattice integrates with AWS Resource Access Manager (AWS RAM) to enable sharing of services, resource
configurations, and service networks. AWS RAM is a service that enables you to share some
VPC Lattice entities with other AWS accounts or through AWS Organizations. With AWS RAM, you share
entities that you own by creating a _resource share_. A resource share
specifies the entities to share, and the consumers with whom to share them. Consumers can
include:

- Specific AWS accounts inside or outside of its organization in AWS Organizations.
- An organizational unit inside of its organization in AWS Organizations.
- An entire organization in AWS Organizations.
  For more information about AWS RAM, see the [AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md").

###### Contents

- [Prerequisites](#sharing-prereqs "#sharing-prereqs")
- [Share entities](#share-resources "#share-resources")
- [Stop sharing entities](#stop-sharing "#stop-sharing")
- [Responsibilities and permissions](#sharing-perms "#sharing-perms")
- [Cross-account events](#cross-account-events "#cross-account-events")

## Prerequisites for sharing VPC Lattice entities

- To share an entity, you must own it in your AWS account. This means that the
  entity must be allocated or provisioned in your account. You can't share an
  entity that has been shared with you.
- To share an entity with your organization or an organizational unit in
  AWS Organizations, you must enable sharing with AWS Organizations. For more information, see
  [Enable resource sharing within AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
  _AWS RAM User Guide_.

## Share VPC Lattice entities

To share an entity, start by creating a resource share using AWS Resource Access Manager. A resource
share specifies the entities to share, the consumers with whom they are shared, and what
actions principals can perform.

When you share a VPC Lattice entity that you own with other AWS accounts, you enable
those accounts to associate their entities with entities in your account. When you
create an association against a shared entity, we generate an Amazon Resource Name (ARN)
in the entity owner account and in the account that created the association. Therefore,
both the entity owner and the account that created the association can delete the
association.

If you are part of an organization in AWS Organizations and sharing within your organization is
enabled, consumers in your organization are automatically granted access to the shared
entity. Otherwise, consumers receive an invitation to join the resource share and are
granted access to the shared entity after accepting the invitation.

###### Considerations

- You can share three types of VPC Lattice entities: service networks, services,
  and resource configurations.
- You can share your VPC Lattice entities with any AWS account.
- You can't share your VPC Lattice entities with individual IAM users and
  roles.
- VPC Lattice supports customer-managed permissions for services, resource
  configurations, and service networks.

###### To share an entity that you own using the VPC Lattice console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Services**, **Service networks**, or
   **Resource configurations**.
3. Choose the name of the entity to open its details page, and then choose
   **Share service**, **Share service
   network**, or **Share resource configuration**
   from the **Sharing** tab.
4. Choose the AWS RAM resource shares from **Resource shares**. To
   create a resource share, choose **Create a resource share in RAM
   console**.
5. Choose **Share service**, **Share service
   network**, or **Share resource
   configuration**.

###### To share an entity that you own using the AWS RAM console

Use the procedure described in [Create a resource
share](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM User Guide_.

###### To share an entity that you own using the AWS CLI

Use the [associate-resource-share](../../../cli/latest/reference/ram/associate-resource-share.md "../../../cli/latest/reference/ram/associate-resource-share.md") command.

## Stop sharing VPC Lattice entities

To stop sharing a VPC Lattice entity that you own, you must remove it from the resource
share. Existing associations persist after you stop sharing your entity. New
associations to a previously shared entity are not allowed. When either the entity owner
or the association owner deletes an association, it is deleted from both accounts. If an
account owner wants to leave a resource share, they must ask the owner of the resource
share to remove their account from the list of accounts this resource was shared with.

###### To stop sharing an entity that you own using the VPC Lattice console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Services**, **Service networks**, or
   Resource configurations.
3. Choose the name of the entity to open its details page.
4. On the **Sharing** tab, select the check box for the resource
   share and then choose **Remove**.

###### To stop sharing an entity that you own using the AWS RAM console

See [Update a resource
share](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the _AWS RAM User Guide_.

###### To stop sharing an entity that you own using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

## Responsibilities and permissions

The following responsibilities and permissions apply when using shared VPC Lattice
entities.

### Entity owners

- The service network owner can't modify a service created by a
  consumer.
- The service network owner can't delete a service created by a
  consumer.
- The service network owner can describe all service associations for the
  service network.
- The service network owner can disassociate any service associated with the
  service network, regardless of who created the association.
- The service network owner can describe all VPC associations for the
  service network.
- The service network owner can disassociate any VPC that a consumer
  associated with the service network.
- The service network owner can describe all resource configuration
  associations for the service network.
- The service network owner can disassociate any resource configuration
  associated with the service network, regardless of who created the
  association.
- The service network owner can describe all endpoint associations for the
  service network.
- The service network owner can disassociate any endpoints associated with
  the service network, regardless of who created the association.
- The service owner can describe all service network associations with the
  service.
- The service owner can disassociate a service from any service network that
  it is associated with.
- The resource configuration owner can describe all network associations
  with the resource configuration.
- The resource configuration owner can disassociate a resource configuration
  from any service network that it is associated with.
- The VPC endpoint owner can describe the service network that it is
  associated with.
- The VPC endpoint owner can dissociate an endpoint from the
  service network.
- Only the account that created an association can update the association
  between the service network and the VPC.

### Entity consumers

- The consumer can't delete a service or resource configuration that they
  didn’t create.
- The consumer can disassociate only the services or resource configurations
  that they associated with a service network.
- The consumer and network owner can describe all associations between a
  service network and a service or resource configuration.
- The consumer can't retrieve service information of a service or resource
  configuration information of a resource configuration that they don't own.
- The consumer can describe all service associations and resource
  configurations associations with a shared service network.
- The consumer can associate a service or a resource configuration with a
  shared service network.
- The consumer can see all VPC associations with a shared service
  network.
- The consumer can associate a VPC with a shared service network.
- The consumer can disassociate only the VPCs that they associated with a
  service network.
- The consumer can create a service network VPC endpoint to connect their
  VPC to a shared service network.
- The consumer can delete only the service network VPC endpoint they created
  to connect their VPC to a shared service network.
- The consumer of a shared service can't associate a service with a service
  network that they don't own.
- The consumer of a shared service network can't associate a VPC or service
  that they don't own.
- The consumer of a shared resource configuration can't associate a resource
  configuration with a service network that they don't own.
- The consumer of a shared service network can't associate a VPC or service
  or resource configuration that they don't own.
- The consumer can describe a service, service network, or resource
  configuration that is shared with them.
- The consumer can't associate two entities if both are shared with
  them.

## Cross-account events

When entity owners and consumers perform actions on a shared entity, those actions are
recorded as cross-account events in AWS CloudTrail.

`CreateServiceNetworkResourceAssociationBySharee`

Sent to the entity owner when an entity consumer calls
CreateServiceNetworkResourceAssociation with a shared entity. If the
caller owns the resource configuration, the event is sent to the owner
of the service network. If the caller owns the service network, the
event is sent to the owner of the resource configuration.

`CreateServiceNetworkServiceAssociationBySharee`

Sent to the entity owner when an entity consumer calls [CreateServiceNetworkServiceAssociation](../APIReference/API_CreateServiceNetworkServiceAssociation.md "../APIReference/API_CreateServiceNetworkServiceAssociation.md") with a shared entity. If
the caller owns the service, the event is sent to the owner of the service
network. If the caller owns the service network, the event is sent to the
owner of the service.

`CreateServiceNetworkVpcAssociationBySharee`

Sent to the entity owner when an entity consumer calls [CreateServiceNetworkVpcAssociation](../APIReference/API_CreateServiceNetworkVpcAssociation.md "../APIReference/API_CreateServiceNetworkVpcAssociation.md") with a shared service
network.

`DeleteServiceNetworkResourceAssociationByOwner`

Sent to the association owner when the entity owner calls
DeleteServiceNetworkResourceAssociation with a shared entity. If the caller
owns the resource configuration, the event is sent to the owner of the
service network association. If the caller owns the service network, the
event is sent to the owner of the resource association.

`DeleteServiceNetworkResourceAssociationBySharee`

Sent to the entity owner when an entity consumer calls
DeleteServiceNetworkResourceAssociation with a shared entity. If the caller
owns the resource configuration, the event is sent to the owner of the
service network. If the caller owns the service network, the event is sent
to the owner of the resource configuration.

`DeleteServiceNetworkServiceAssociationByOwner`

Sent to the association owner when the entity owner calls [DeleteServiceNetworkServiceAssociation](../APIReference/API_DeleteServiceNetworkServiceAssociation.md "../APIReference/API_DeleteServiceNetworkServiceAssociation.md") with a shared entity. If
the caller owns the service, the event is sent to the owner of the service
network association. If the caller owns the service network, the event is
sent to the owner of the service association.

`DeleteServiceNetworkServiceAssociationBySharee`

Sent to the entity owner when an entity consumer calls [DeleteServiceNetworkServiceAssociation](../APIReference/API_DeleteServiceNetworkServiceAssociation.md "../APIReference/API_DeleteServiceNetworkServiceAssociation.md") with a shared entity. If
the caller owns the service, the event is sent to the owner of the service
network. If the caller owns the service network, the event is sent to the
owner of the service.

`DeleteServiceNetworkVpcAssociationByOwner`

Sent to the association owner when the entity owner calls [DeleteServiceNetworkVpcAssociation](../APIReference/API_DeleteServiceNetworkVpcAssociation.md "../APIReference/API_DeleteServiceNetworkVpcAssociation.md") with a shared service
network.

`DeleteServiceNetworkVpcAssociationBySharee`

Sent to the entity owner when an entity consumer calls [DeleteServiceNetworkVpcAssociation](../APIReference/API_DeleteServiceNetworkVpcAssociation.md "../APIReference/API_DeleteServiceNetworkVpcAssociation.md") with a shared service
network.

`GetServiceBySharee`

Sent to the entity owner when an entity consumer calls [GetService](../APIReference/API_GetService.md "../APIReference/API_GetService.md") with a shared service.

`GetServiceNetworkBySharee`

Sent to the entity owner when an entity consumer calls [GetServiceNetwork](../APIReference/API_GetServiceNetwork.md "../APIReference/API_GetServiceNetwork.md") with a shared service network.

`GetServiceNetworkResourceAssociationBySharee`

Sent to the entity owner when an entity consumer calls
GetServiceNetworkResourceAssociation with a shared entity. If the caller
owns the resource configuration, the event is sent to the owner of the
service network. If the caller owns the service network, the event is sent
to the owner of the resource configuration.

`GetServiceNetworkServiceAssociationBySharee`

Sent to the entity owner when an entity consumer calls [GetServiceNetworkServiceAssociation](../APIReference/API_GetServiceNetworkServiceAssociation.md "../APIReference/API_GetServiceNetworkServiceAssociation.md") with a shared entity. If
the caller owns the service, the event is sent to the owner of the service
network. If the caller owns the service network, the event is sent to the
owner of the service.

`GetServiceNetworkVpcAssociationBySharee`

Sent to the entity owner when an entity consumer calls [GetServiceNetworkVpcAssociation](../APIReference/API_GetServiceNetworkVpcAssociation.md "../APIReference/API_GetServiceNetworkVpcAssociation.md") with a shared service
network.

The following is an example entry for the
`CreateServiceNetworkServiceAssociationBySharee` event.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown"
    },
    "eventTime": "2023-04-27T17:12:46Z",
    "eventSource": "vpc-lattice.amazonaws.com",
    "eventName": "CreateServiceNetworkServiceAssociationBySharee",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "vpc-lattice.amazonaws.com",
    "userAgent": "ec2.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "callerAccountId": "`111122223333`"
    },
    "requestID": "ddabb0a7-70c6-4f70-a6c9-00cbe8a6a18b",
    "eventID": "bd03cdca-7edd-4d50-b9c9-eaa89f4a47cd",
    "readOnly": false,
    "resources": [
        {
            "accountId": "`123456789012`",
            "type": "AWS::VpcLattice::ServiceNetworkServiceAssociation",
            "ARN": "arn:aws:vpc-lattice:`region`:`123456789012`:servicenetworkserviceassociation/`snsa-0d5ea7bc72EXAMPLE`"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "`123456789012`",
    "eventCategory": "Management"
}
```
