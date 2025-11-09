# Amazon ECS Service Connect with shared

AWS Cloud Map namespaces

Amazon ECS Service Connect supports using shared AWS Cloud Map namespaces across multiple
AWS accounts within the same AWS Region. This capability enables you to create
distributed applications where services running in different AWS accounts can discover and
communicate with each other through Service Connect. Shared namespaces are managed using
AWS Resource Access Manager (AWS RAM), which allows secure cross-account resource sharing. For more information
about shared namespaces, see [Cross-account AWS Cloud Map namespace
sharing](../../../cloud-map/latest/dg/sharing-namespaces.md "../../../cloud-map/latest/dg/sharing-namespaces.md") in the _AWS Cloud Map Developer Guide_.

###### Important

You must use the `AWSRAMPermissionCloudMapECSFullPermission` managed
permission to share the namespace for Service Connect to work properly with the
namespace.

When you use shared AWS Cloud Map namespaces with Service Connect, services from multiple
AWS accounts can participate in the same service namespace. This is particularly useful
for organizations with multiple AWS accounts that need to maintain service-to-service
communication across account boundaries while preserving security and isolation.

###### Note

To communicate with services that are in different VPCs, you will need to configure
inter-VPC connectivity. This can be achieved using a VPC Peering connection. For more
information, see [Create or delete a VPC
Peering connection](../../../vpc/latest/peering/create-vpc-peering-connection.md "../../../vpc/latest/peering/create-vpc-peering-connection.md") in the _Amazon Virtual Private Cloud VPC Peering
guide_.

## Considerations

Consider the following when using shared AWS Cloud Map namespaces with
Service Connect:

- AWS RAM must be available in the AWS Region where you want to use the shared
  namespace.
- The shared namespace must be in the same AWS Region as your Amazon ECS services
  and clusters.
- You must use the namespace ARN, not the ID, when configuring
  Service Connect with a shared namespace.
- All namespace types are supported: HTTP, Private DNS, and Public DNS
  namespaces.
- If access to a shared namespace is revoked, Amazon ECS operations that require
  interaction with the namespace (such as `CreateService`,
  `UpdateService`, and `ListServicesByNamespace`) will
  fail. For more information about troubleshooting permissions issues with shared
  namespaces, see [Troubleshooting
  Amazon ECS Service Connect with shared AWS Cloud Map namespaces](service-connect-shared-namespaces-troubleshooting.md "service-connect-shared-namespaces-troubleshooting.md").
- For service discovery using DNS queries in a shared private DNS
  namespace:
  - The namespace owner will need to call
    `create-vpc-association-authorization` with the ID of the
    private hosted zone associated with the namespace, and the consumer's
    VPC.

  ```
  aws route53 create-vpc-association-authorization --hosted-zone-id `Z1234567890ABC` --vpc VPCRegion=`us-east-1`,VPCId=`vpc-12345678`
  ```

  - The namespace consumer will need to call
    `associate-vpc-with-hosted-zone` with the ID of the
    private hosted zone.

  ```
  aws route53 associate-vpc-with-hosted-zone --hosted-zone-id `Z1234567890ABC` --vpc VPCRegion=`us-east-1`,VPCId=`vpc-12345678`
  ```

- Only the namespace owner can manage the resource share.
- Namespace consumers can create and manage services within the shared namespace
  but cannot modify the namespace itself.
- Discovery names must be unique within the shared namespace, regardless of
  which account creates the service.
- Services in the shared namespace can discover and connect to services from
  other AWS accounts that have access to the namespace.
- When enabling TLS for Service Connect and using a shared namespace, the AWS Private CA
  Certificate Authority (CA) is scoped to the namespace. When access to the shared
  namespace is revoked, access to the CA is stopped.
- When working with a shared namespace, namespace owners and consumers don't
  have access to cross-account Amazon CloudWatch metrics by default. Target metrics are
  published only to accounts that own client services. An account that owns
  client services doesn't have access to metrics received by an account owning
  client-server services, and the other way around. To allow for cross-account
  access to metrics, set up
  CloudWatch cross-account observability. For more information about configuring
  cross-account observability, see [CloudWatch cross-account observabilty](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.md") in the
  _Amazon CloudWatch User Guide_. For more information about the CloudWatch
  metrics for Service Connect, see [Amazon ECS CloudWatch metrics](available-metrics.md "available-metrics.md") .
