

# AWS resources and shared VPC subnets
<a name="vpc-sharing-service-behavior"></a>

The following AWS services support resources in shared VPC subnets. For more information, follow the links to the corresponding service documentation.
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Shared_subnets)
+ [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html#CHAP_ReplicationInstance.VPC.Configurations.ScenarioVPCShared)
+ [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html#ec2-shared-VPC-subnets)
+ [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html)
+ Amazon ElastiCache (Redis OSS)
+ [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/mount-fs-diff-account-same-vpc.html)
+ [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/network-reqs.html#network-requirements-shared)
+ Elastic Load Balancing
  + [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html#register-targets-shared-subnets)
  + [ Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html#prerequisites)
  + [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html#register-targets-shared-subnets)
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-clusters-in-a-vpc.html#emr-vpc-shared-subnet)
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/shared-vpc.html)
+ AWS Lambda
+ Amazon MQ running Apache MQ (not Rabbit MQ)
+ Amazon MSK
+ AWS Network Manager
  + [AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-vpc-attachment.html#cloudwan-vpc-attachments-shared-subnets)
  + [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/how-network-access-analyzer-works.html#analyzer-limitations)
  + [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/how-reachability-analyzer-works.html#considerations)
+ Amazon OpenSearch Service
+ [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#interface-endpoint-shared-subnets)†
+ [Amazon Relational Database Service (RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Shared_subnets)
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-shared-subnet-vpc.html)
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html)
+ [Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/create-domain-sagemaker-unified-studio-quick.html)
+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-transit-gateways.html#transit-gateway-shared-subnets)
+ [AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-endpoints.html#shared-vpc)
+ Amazon VPC
  + [Peering](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html#vpc-peering-limitations)
  + [Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-network-limitations.html)
+ [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-target-group.html#target-group-shared-subnets)

† You can connect to all AWS services that support PrivateLink using a VPC endpoint in a shared VPC. For a list of services that support PrivateLink, see [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html) in the *AWS PrivateLink Guide*.

This list is intended to include all services that support launching resources in shared VPC subnets. Despite our best efforts, there might be services that support launching resources in shared VPC subnets but are not listed here. We encourage you to submit documentation feedback if you have questions.