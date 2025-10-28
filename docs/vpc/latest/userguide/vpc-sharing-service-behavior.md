# AWS resources and shared VPC subnets

The following AWS services support resources in shared VPC subnets. For more information,
follow the links to the corresponding service documentation.

- [Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_VPC.md#USER_VPC.Shared_subnets "../../../AmazonRDS/latest/AuroraUserGuide/USER_VPC.md#USER_VPC.Shared_subnets")
- [AWS Database Migration Service](../../../dms/latest/userguide/CHAP_ReplicationInstance.md#CHAP_ReplicationInstance.VPC.Configurations.ScenarioVPCShared "../../../dms/latest/userguide/CHAP_ReplicationInstance.md#CHAP_ReplicationInstance.VPC.Configurations.ScenarioVPCShared")
- [Amazon EC2](../../../AWSEC2/latest/UserGuide/using-vpc.md#ec2-shared-VPC-subnets "../../../AWSEC2/latest/UserGuide/using-vpc.md#ec2-shared-VPC-subnets")
- [Amazon ECS](../../../AmazonECS/latest/developerguide/cluster-regions-zones.md "../../../AmazonECS/latest/developerguide/cluster-regions-zones.md")
- Amazon ElastiCache (Redis OSS)
- [Amazon EFS](../../../efs/latest/ug/mount-fs-diff-account-same-vpc.md "../../../efs/latest/ug/mount-fs-diff-account-same-vpc.md")
- [Amazon Elastic Kubernetes Service](../../../eks/latest/userguide/network-reqs.md#network-requirements-shared "../../../eks/latest/userguide/network-reqs.md#network-requirements-shared")
- Elastic Load Balancing
  - [Application Load Balancers](../../../elasticloadbalancing/latest/application/target-group-register-targets.md#register-targets-shared-subnets "../../../elasticloadbalancing/latest/application/target-group-register-targets.md#register-targets-shared-subnets")
  - [Gateway Load Balancers](../../../elasticloadbalancing/latest/gateway/getting-started.md#prerequisites "../../../elasticloadbalancing/latest/gateway/getting-started.md#prerequisites")
  - [Network Load Balancers](../../../elasticloadbalancing/latest/network/target-group-register-targets.md#register-targets-shared-subnets "../../../elasticloadbalancing/latest/network/target-group-register-targets.md#register-targets-shared-subnets")

- [Amazon EMR](../../../emr/latest/ManagementGuide/emr-clusters-in-a-vpc.md#emr-vpc-shared-subnet "../../../emr/latest/ManagementGuide/emr-clusters-in-a-vpc.md#emr-vpc-shared-subnet")
- [AWS Glue](../../../glue/latest/dg/shared-vpc.md "../../../glue/latest/dg/shared-vpc.md")
- AWS Lambda
- Amazon MQ running Apache MQ (not Rabbit MQ)
- Amazon MSK
- AWS Network Manager
  - [AWS Cloud WAN](../../../network-manager/latest/cloudwan/cloudwan-vpc-attachment.md#cloudwan-vpc-attachments-shared-subnets "../../../network-manager/latest/cloudwan/cloudwan-vpc-attachment.md#cloudwan-vpc-attachments-shared-subnets")
  - [Network Access Analyzer](../network-access-analyzer/how-network-access-analyzer-works.md#analyzer-limitations "../network-access-analyzer/how-network-access-analyzer-works.md#analyzer-limitations")
  - [Reachability Analyzer](../reachability/how-reachability-analyzer-works.md#considerations "../reachability/how-reachability-analyzer-works.md#considerations")

- Amazon OpenSearch Service
- [AWS PrivateLink](../privatelink/create-interface-endpoint.md#interface-endpoint-shared-subnets "../privatelink/create-interface-endpoint.md#interface-endpoint-shared-subnets")†
- [Amazon Relational Database Service (RDS)](../../../AmazonRDS/latest/UserGuide/USER_VPC.md#USER_VPC.Shared_subnets "../../../AmazonRDS/latest/UserGuide/USER_VPC.md#USER_VPC.Shared_subnets")
- [Amazon Redshift](../../../redshift/latest/mgmt/rs-shared-subnet-vpc.md "../../../redshift/latest/mgmt/rs-shared-subnet-vpc.md")
- [Amazon Route 53](../../../Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.md")
- [Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/adminguide/create-domain-sagemaker-unified-studio-quick.md "../../../sagemaker-unified-studio/latest/adminguide/create-domain-sagemaker-unified-studio-quick.md")
- [AWS Transit Gateway](../tgw/working-with-transit-gateways.md#transit-gateway-shared-subnets "../tgw/working-with-transit-gateways.md#transit-gateway-shared-subnets")
- [AWS Verified Access](../../../verified-access/latest/ug/verified-access-endpoints.md#shared-vpc "../../../verified-access/latest/ug/verified-access-endpoints.md#shared-vpc")
- Amazon VPC
  - [Peering](../peering/vpc-peering-basics.md#vpc-peering-limitations "../peering/vpc-peering-basics.md#vpc-peering-limitations")
  - [Traffic Mirroring](../mirroring/traffic-mirroring-network-limitations.md "../mirroring/traffic-mirroring-network-limitations.md")

- [Amazon VPC Lattice](../../../vpc-lattice/latest/ug/create-target-group.md#target-group-shared-subnets "../../../vpc-lattice/latest/ug/create-target-group.md#target-group-shared-subnets")
  †
  You can connect to all AWS services that support PrivateLink using a VPC endpoint in a shared VPC. For a list of services that support PrivateLink, see [AWS services that integrate with AWS PrivateLink](../privatelink/aws-services-privatelink-support.md "../privatelink/aws-services-privatelink-support.md") in the _AWS PrivateLink Guide_.

This list is intended to include all services that support launching resources in shared VPC subnets.
Despite our best efforts, there might be services that support launching resources in shared VPC subnets
but are not listed here. We encourage you to submit documentation feedback if you have questions.
