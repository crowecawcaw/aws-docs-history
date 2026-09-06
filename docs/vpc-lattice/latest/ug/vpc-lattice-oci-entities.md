

# Access and share VPC Lattice entities
<a name="vpc-lattice-oci-entities"></a>

You can also connect your ODB network to services, resources, and other clients in VPCs using VPC Lattice. These connectivity options are powered through the default service network, resource gateway, and service-network endpoint provisioned by VPC Lattice.

## Access VPC Lattice services and resources
<a name="vpc-lattice-oci-entities-access"></a>

To access other entities, associate services or resources that you own, or are shared with you, to the default service network. Clients in the ODB network can access the services or resources through the default service-network endpoint.

### Considerations
<a name="vpc-lattice-oci-entities-considerations"></a>

The following are considerations for connecting to other VPC Lattice entities:
+ You can add new service-network endpoints, VPC associations, VPC Lattice resources and services to the service network, but you can't modify the resources provisioned by VPC Lattice on behalf of the ODB network. These must be managed through the Oracle Database@AWS APIs.

## Share your ODB network through VPC Lattice
<a name="vpc-lattice-share-odb-network"></a>

You can share your ODB network resources with clients in other VPCs, accounts or on premises. To get started, create a resource configuration for the resources that you want to share. The resource configurations must use the default resource gateway for your ODB network. You can then associate the resources with your default service network.

Clients in other VPCs or AWS accounts that you've shared your service network with can access these resources through their own service network endpoints or VPC associations. For more information, see [Manage associations for a VPC Lattice resource configuration](resource-configuration-associations.md).

### Considerations
<a name="share-odb-network-considerations"></a>

The following are considerations for sharing your ODB network:
+ We recommend only sharing ODB network instances as IP-based resources.
+ VPC Lattice doesn't support OCI's Single Client Access Name (SCAN) listener DNS.