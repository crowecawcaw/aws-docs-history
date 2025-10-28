# VPC Lattice for Oracle Database@AWS

VPC Lattice powers AWS managed service integrations for [Oracle Database@AWS](../../../odb/latest/UserGuide/what-is-odb.md "../../../odb/latest/UserGuide/what-is-odb.md") (ODB) and provides you with
simplified connectivity between the ODB network, AWS VPCs and on premise. To support this
connectivity, VPC Lattice provisions the following entities on your behalf:

**Default service network**

The default service network uses the naming convention `default-odb-network-`randomHash``

**Default service-network endpoint**
There is no name for this AWS resource.

**Resource gateway**

The resource gateway uses the naming convention `default-odb-network-`randomHash``

VPC Lattice supports AWS managed service integrations, referred to as
_managed integrations_ to your ODB network. By default, Oracle Cloud
Infrastructure (OCI) Managed Backup to Amazon S3 is enabled. You can choose to enable self-managed
access to Amazon S3 and Zero-ETL.

Once you create your ODB network, you can view the provisioned resources using the
AWS Management Console or AWS CLI. The following example command lists the ODB network's default managed
integrations and any other resources you might have for this service network:

```
aws vpc-lattice list-service-network-resource-associations \
        --service-network-identifier default-odb-network-`randomHash`
```

## Considerations

The following considerations apply to VPC Lattice for Oracle Database@AWS:

- You can't delete the default service network, service-network endpoint, resource gateway, or any ODB managed integrations
  provisioned by VPC Lattice. To delete these entities, delete your ODB network or disable the managed integrations.
- Clients can only access the managed integrations in the ODB network. Clients
  outside the ODB network, such as in your VPCs, cannot use these managed
  integrations to access S3 or Zero-ETL.
- You can't
  connect to any of the managed integrations outside of the ODB network
  provisioned by VPC Lattice.
- All traffic to Amazon S3 goes through the default service-network endpoint and
  standard processing charges for accessing resources apply. All Zero-ETL traffic
  goes over the resource gateway and standard data processing charges for
  resources that you share apply. For more information, see [VPC Lattice pricing](https://aws.amazon.com/vpc/lattice/pricing/ "https://aws.amazon.com/vpc/lattice/pricing/").
- There are no hourly charges for Oracle Database@AWS managed integrations.
- You can manage the resources provisioned by VPC Lattice just like any other
  service network. You can share the default service network with other
  AWS accounts or organizations, and add new endpoints, VPC associations,
  VPC Lattice services and resources to the default network.
- The following permissions are required for VPC Lattice to provision Oracle Database@AWS resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowODBEC2andLatticeActions",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:CreateTags",
 "ec2:DescribeAvailabilityZones",
 "ec2:CreateOdbNetworkPeering",
 "ec2:DeleteOdbNetworkPeering",
 "ec2:ModifyOdbNetworkPeering",
 "ec2:DescribeVpcEndpointAssociations",
 "ec2:CreateVpcEndpoint",
 "ec2:DeleteVpcEndpoints",
 "ec2:DescribeVpcEndpoints",
 "vpc-lattice:CreateServiceNetwork",
 "vpc-lattice:DeleteServiceNetwork",
 "vpc-lattice:GetServiceNetwork",
 "vpc-lattice:CreateServiceNetworkResourceAssociation",
 "vpc-lattice:DeleteServiceNetworkResourceAssociation",
 "vpc-lattice:GetServiceNetworkResourceAssociation",
 "vpc-lattice:CreateResourceGateway",
 "vpc-lattice:DeleteResourceGateway",
 "vpc-lattice:GetResourceGateway",
 "vpc-lattice:CreateServiceNetworkVpcEndpointAssociation"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Sid": "AllowSLRActionsForLattice",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "vpc-lattice.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

To use VPC Lattice for Oracle Database@AWS, we recommend that you are familiar with [service
networks](service-networks.md "service-networks.md"), [service-network
associations](service-network-associations.md "service-network-associations.md"), and [resource gateways](resource-gateway.md "resource-gateway.md") in VPC Lattice.

###### Topics

- [Oracle Cloud Infrastructure (OCI) Managed Backup to Amazon S3](vpc-lattice-oci-managed-backup.md "vpc-lattice-oci-managed-backup.md")
- [Amazon S3 access](vpc-lattice-oci-s3-access.md "vpc-lattice-oci-s3-access.md")
- [Zero-ETL for Amazon Redshift](vpc-lattice-oci-zero-etl.md "vpc-lattice-oci-zero-etl.md")
- [Access and share VPC Lattice entities](vpc-lattice-oci-entities.md "vpc-lattice-oci-entities.md")
