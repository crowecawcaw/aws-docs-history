

# Document history for the Amazon VPC Lattice User Guide

The following table describes the documentation releases for VPC Lattice.

| Change | Description | Date | 
| --- |--- |--- |
| [CloudWatch metrics for VPC resources](doc-history.md) | VPC Lattice now publishes CloudWatch metrics for resource gateways, resource configurations, and resource consumers (resource VPC endpoints, service-network VPC endpoints, and service network VPC associations). | November 19, 2026 | 
| [Update resource gateway DNS resolution](doc-history.md) | You can now change the Resource Config DNS Resolution setting of a resource gateway after creation. | November 17, 2026 | 
| [Update private DNS settings](doc-history.md) | You can now change the private DNS preference and specified domains of resource VPC endpoints, service-network VPC endpoints, and service network VPC associations after creation. | November 17, 2026 | 
| [Private hosted zone reuse](doc-history.md) | For group resource configurations, VPC Lattice now reuses an existing VPC Lattice-managed private hosted zone when multiple endpoints or VPC associations in a VPC connect to groups with the same group domain. | November 17, 2026 | 
| [Enable or disable private DNS](doc-history.md) | You can now enable or disable private DNS on resource VPC endpoints, service-network VPC endpoints, and service network VPC associations after creation. | November 17, 2026 | 
| [Resource gateways in shared subnets](doc-history.md) | Participant accounts can now create resource gateways and resource configurations in shared VPC subnets. | November 10, 2026 | 
| [Added configurable IP addresses for resource gateways](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html#ipv4-address-type-per-eni) | VPC Lattice now supports configurable IP addresses for resource gateways. | October 7, 2025 | 
| [Added VPC Lattice for Oracle Database@AWS](https://docs.aws.amazon.com/vpc-lattice/latest/ug/vcp-lattice-oci.html) | VPC Lattice for Oracle Database@AWS released. | June 26, 2025 | 
| [Added dual-stack support for management endpoints](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html#service-endpoints) | VPC Lattice now supports dual-stack (IPv4 and IPv6) endpoints for all VPC Lattice management APIs. | April 30, 2025 | 
| [Share and access resources](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html) | VPC Lattice now supports sharing and accessing resources across VPC and account boundaries. This includes updates to the [VPCLatticeReadOnlyAccess](https://docs.aws.amazon.com/vpc-lattice/latest/ug/managed-policies.html#vpc-lattice-read-onlyaccess-policy) and [VPCLatticeFullAccess](https://docs.aws.amazon.com/vpc-lattice/latest/ug/managed-policies.html#vpc-lattice-fullaccess-policy) policies. | December 1, 2024 | 
| [TLS passthrough](https://docs.aws.amazon.com/vpc-lattice/latest/ug/tls-listeners.html) | VPC Lattice now supports TLS passthrough, which allows you to perform TLS termination in your application for end-to-end authentication. | May 14, 2024 | 
| [Lambda event structure version](doc-history.md) | VPC Lattice now supports a new version of the Lambda event structure. | September 7, 2023 | 
| [Support for shared VPCs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-target-group.html#target-group-shared-subnets) | Participants can create VPC Lattice target groups in a shared VPC. | July 5, 2023 | 
| [General Availability release](doc-history.md) | The release of the VPC Lattice User Guide for General Availability (GA) | March 31, 2023 | 
| [VPC Lattice now reports changes to its AWS managed policies](doc-history.md) | Changes to managed policies are reported in "AWS managed policies for VPC Lattice" in the "Security" chapter. | March 29, 2023 | 
| [Support for Application Load Balancer target type](doc-history.md) | VPC Lattice now supports creating an Application Load Balancer type target group. | March 29, 2023 | 
| [Support for all instance types](doc-history.md) | VPC Lattice now supports all instance types. | March 27, 2023 | 
| [IPv6 support](doc-history.md) | VPC Lattice now supports both IPv4 and IPv6 IP target groups.  | March 27, 2023 | 
| [HTTP2 protocol version for health checks](doc-history.md) | Health checks are now supported when the target group protocol version is HTTP2.  | March 27, 2023 | 
| [Fixed response action for listener rules](doc-history.md) | Listeners for VPC Lattice services now support fixed response actions in addition to forward actions. | March 27, 2023 | 
| [Support for custom domain names](doc-history.md) | You can now configure a custom domain name for your VPC Lattice service | February 14, 2023 | 
| [Support for BYOC (Bring Your Own Certificate)](doc-history.md) | VPC Lattice supports using your own an SSL/TLS certificate in ACM for custom domain names. | February 14, 2023 | 
| [VPC Lattice now reports an updated list of unsupported instance types](doc-history.md) | Three additional instances have been added to the unsupported list of instances. | January 26, 2023 | 
| [VPC Lattice now reports changes to its AWS managed policies](doc-history.md) | Beginning December 5, 2022, changes to managed policies are reported in the topic "AWS managed policies for VPC Lattice" in the "Security" chapter. The first change listed is the addition of permissions needed for CloudWatch monitoring. | December 5, 2022 | 
| [Initial release](doc-history.md) | Initial release of the VPC Lattice User Guide | December 5, 2022 | 