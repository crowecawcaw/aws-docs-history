# Service limits

See the following checks for the service limits (also known as quotas) category.

All checks in this category have the following descriptions:

**Alert Criteria**

- Yellow: 80% of limit reached.
- Red: 100% of limit reached.
- Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more
  AWS Regions.

**Recommended Action**

If you expect to exceed a service limit, request an increase directly from the
[Service Quotas](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas") console. If Service Quotas
doesn’t support your service yet, you can open a support case in [Support Center](https://console.aws.amazon.com/support/home?region=us-east-1#/case/create?issueType=service-limit-increase&type=service_limit_increase "https://console.aws.amazon.com/support/home?region=us-east-1#/case/create?issueType=service-limit-increase&type=service_limit_increase").

**Report columns**

- Status
- Service
- Region
- Limit Amount
- Current Usage

###### Note

- Values are based on a snapshot, so your current usage might differ. Quota and
  usage data can take up to 24 hours to reflect any changes. In cases where quotas
  have been recently increased, you might temporarily see utilization that exceeds
  the quota.

###### Check names

- [Auto Scaling Groups](service-limits.md#auto-scaling-groups "service-limits.md#auto-scaling-groups")
- [Auto Scaling Launch Configurations](service-limits.md#auto-scaling-launch-configurations "service-limits.md#auto-scaling-launch-configurations")
- [CloudFormation Stacks](service-limits.md#cloudformation-stacks "service-limits.md#cloudformation-stacks")
- [DynamoDB Read Capacity](service-limits.md#dynamo-db-read-capacity "service-limits.md#dynamo-db-read-capacity")
- [DynamoDB Write Capacity](service-limits.md#dynamo-db-write-capacity "service-limits.md#dynamo-db-write-capacity")
- [EBS Active Snapshots](service-limits.md#ebs-active-snapshots "service-limits.md#ebs-active-snapshots")
- [EBS Cold HDD (sc1) Volume
  Storage](service-limits.md#ebs-cold-hdd-sc1-volume-storage "service-limits.md#ebs-cold-hdd-sc1-volume-storage")
- [EBS General Purpose SSD
  (gp2) Volume Storage](service-limits.md#ebs-general-purpose-ssd-gp2-volume-storage "service-limits.md#ebs-general-purpose-ssd-gp2-volume-storage")
- [EBS General Purpose SSD
  (gp3) Volume Storage](service-limits.md#ebs-general-purpose-ssd-gp3-volume-storage "service-limits.md#ebs-general-purpose-ssd-gp3-volume-storage")
- [EBS Magnetic (standard) Volume
  Storage](service-limits.md#ebs-magnetic-standard-volume-storage "service-limits.md#ebs-magnetic-standard-volume-storage")
- [EBS Provisioned IOPS
  SSD (io1) Volume Aggregate IOPS](service-limits.md#ebs-provisioned-iops-ssd-volume-aggregate-iops "service-limits.md#ebs-provisioned-iops-ssd-volume-aggregate-iops")
- [EBS Provisioned IOPS SSD
  (io1) Volume Storage](service-limits.md#ebs-provisioned-iops-ssd-io1-volume-storage "service-limits.md#ebs-provisioned-iops-ssd-io1-volume-storage")
- [EBS Provisioned IOPS SSD
  (io2) Volume Storage](service-limits.md#ebs-provisioned-iops-ssd-io2-volume-storage "service-limits.md#ebs-provisioned-iops-ssd-io2-volume-storage")
- [EBS Throughput
  Optimized HDD (st1) Volume Storage](service-limits.md#ebs-throughput-optimized-hdd-st1-volume-storage "service-limits.md#ebs-throughput-optimized-hdd-st1-volume-storage")
- [EC2 On-Demand Instances](service-limits.md#ec2-on-demand-instances "service-limits.md#ec2-on-demand-instances")
- [EC2 Reserved Instance Leases](service-limits.md#ec2-reserved-instance-leases "service-limits.md#ec2-reserved-instance-leases")
- [EC2-Classic Elastic IP Addresses](service-limits.md#ec2-elastic-ip-addresses "service-limits.md#ec2-elastic-ip-addresses")
- [EC2-VPC Elastic IP Address](service-limits.md#ec2-vpc-elastic-ip-address "service-limits.md#ec2-vpc-elastic-ip-address")
- [ELB Application Load Balancers](service-limits.md#elb-application-load-balancers "service-limits.md#elb-application-load-balancers")
- [ELB Classic Load Balancers](service-limits.md#elb-classic-load-balancers "service-limits.md#elb-classic-load-balancers")
- [ELB Network Load Balancers](service-limits.md#elb-network-load-balancers "service-limits.md#elb-network-load-balancers")
- [IAM Group](service-limits.md#iam-group "service-limits.md#iam-group")
- [IAM Instance Profiles](service-limits.md#iam-instance-profiles "service-limits.md#iam-instance-profiles")
- [IAM Policies](service-limits.md#iam-policies "service-limits.md#iam-policies")
- [IAM Roles](service-limits.md#iam-roles "service-limits.md#iam-roles")
- [IAM Server Certificates](service-limits.md#iam-server-certificates "service-limits.md#iam-server-certificates")
- [IAM Users](service-limits.md#iam-users "service-limits.md#iam-users")
- [Kinesis Shards per Region](service-limits.md#kinesis-shards-per-region "service-limits.md#kinesis-shards-per-region")
- [Lambda Code Storage Usage](service-limits.md#Lambda-Code-Storage-Usage "service-limits.md#Lambda-Code-Storage-Usage")
- [RDS Cluster Parameter Groups](service-limits.md#rds-cluster-parameter-groups "service-limits.md#rds-cluster-parameter-groups")
- [RDS Cluster Roles](service-limits.md#rds-cluster-roles "service-limits.md#rds-cluster-roles")
- [RDS Clusters](service-limits.md#rds-clusters "service-limits.md#rds-clusters")
- [RDS DB Instances](service-limits.md#rds-db-instances "service-limits.md#rds-db-instances")
- [RDS DB Manual Snapshots](service-limits.md#rds-db-manual-snapshots "service-limits.md#rds-db-manual-snapshots")
- [RDS DB Parameter Groups](service-limits.md#rds-db-parameter-groups "service-limits.md#rds-db-parameter-groups")
- [RDS DB Security Groups](service-limits.md#rds-db-security-groups "service-limits.md#rds-db-security-groups")
- [RDS Event Subscriptions](service-limits.md#rds-event-subscriptions "service-limits.md#rds-event-subscriptions")
- [RDS Max Auths per Security
  Group](service-limits.md#rds-max-auths-per-security-group "service-limits.md#rds-max-auths-per-security-group")
- [RDS Option Groups](service-limits.md#rds-option-groups "service-limits.md#rds-option-groups")
- [RDS Read Replicas per Master](service-limits.md#rds-read-replicas-per-master "service-limits.md#rds-read-replicas-per-master")
- [RDS Reserved Instances](service-limits.md#rds-reserved-instances "service-limits.md#rds-reserved-instances")
- [RDS Subnet Groups](service-limits.md#rds-subnet-groups "service-limits.md#rds-subnet-groups")
- [RDS Subnets per Subnet Group](service-limits.md#rds-subnets-per-subnet-group "service-limits.md#rds-subnets-per-subnet-group")
- [RDS Total Storage Quota](service-limits.md#rds-total-storage-quota "service-limits.md#rds-total-storage-quota")
- [Route 53 Hosted Zones](service-limits.md#route-53-hosted-zones "service-limits.md#route-53-hosted-zones")
- [Route 53 Max Health Checks](service-limits.md#route-53-max-health-checks "service-limits.md#route-53-max-health-checks")
- [Route 53 Reusable Delegation
  Sets](service-limits.md#route-53-reusable-delegation-sets "service-limits.md#route-53-reusable-delegation-sets")
- [Route 53 Traffic Policies](service-limits.md#route-53-traffic-policies "service-limits.md#route-53-traffic-policies")
- [Route 53 Traffic Policy
  Instances](service-limits.md#route-53-traffic-policy-instances "service-limits.md#route-53-traffic-policy-instances")
- [SES Daily Sending Quota](service-limits.md#ses-daily-sending-quota "service-limits.md#ses-daily-sending-quota")
- [VPC](service-limits.md#vpc-quota-check "service-limits.md#vpc-quota-check")
- [VPC Internet Gateways](service-limits.md#vpc-internet-gateways "service-limits.md#vpc-internet-gateways")

## Auto Scaling Groups

**Description**

Checks for usage that is more than 80% of the Auto Scaling Groups quota.

**Check ID**

`fW7HH0l7J9`

**Additional Resources**

[Auto Scaling quotas](../../../autoscaling/latest/userguide/as-account-limits.md "../../../autoscaling/latest/userguide/as-account-limits.md")

## Auto Scaling Launch Configurations

**Description**

Checks for usage that is more than 80% of the Auto Scaling launch configurations
quota.

**Check ID**

`aW7HH0l7J9`

**Additional Resources**

[Auto Scaling quotas](../../../autoscaling/latest/userguide/as-account-limits.md "../../../autoscaling/latest/userguide/as-account-limits.md")

## CloudFormation Stacks

**Description**

Checks for usage that is more than 80% of the CloudFormation stacks
quota.

**Check ID**

`gW7HH0l7J9`

**Additional Resources**

[CloudFormation quotas](../../../AWSCloudFormation/latest/UserGuide/cloudformation-limits.md "../../../AWSCloudFormation/latest/UserGuide/cloudformation-limits.md")

## DynamoDB Read Capacity

**Description**

Checks for usage that is more than 80% of the DynamoDB provisioned throughput
limit for reads per AWS account.

**Check ID**

`6gtQddfEw6`

**Additional Resources**

[DynamoDB
quotas](../../../general/latest/gr/ddb.md "../../../general/latest/gr/ddb.md")

## DynamoDB Write Capacity

**Description**

Checks for usage that is more than 80% of the DynamoDB provisioned throughput
limit for writes per AWS account.

**Check ID**

`c5ftjdfkMr`

**Additional Resources**

[DynamoDB
quotas](../../../general/latest/gr/ddb.md "../../../general/latest/gr/ddb.md")

## EBS Active Snapshots

**Description**

Checks for usage that is more than 80% of the EBS active snapshots
quota.

**Check ID**

`eI7KK0l7J9`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EBS Cold HDD (sc1) Volume

Storage

**Description**

Checks for usage that is more than 80% of the EBS Cold HDD (sc1) volume
storage quota.

**Check ID**

`gH5CC0e3J9`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EBS General Purpose SSD

(gp2) Volume Storage

**Description**

Checks for usage that is more than 80% of the EBS General Purpose SSD
(gp2) volume storage quota.

**Check ID**

`dH7RR0l6J9`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EBS General Purpose SSD

(gp3) Volume Storage

**Description**

Checks for usage that is more than 80% of the EBS General Purpose SSD
(gp3) volume storage quota.

**Check ID**

`dH7RR0l6J3`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EBS Magnetic (standard) Volume

Storage

**Description**

Checks for usage that is more than 80% of the EBS Magnetic (standard)
volume storage quota.

**Check ID**

`cG7HH0l7J9`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EBS Provisioned IOPS

SSD (io1) Volume Aggregate IOPS

**Description**

Checks for usage that is more than 80% of the EBS Provisioned IOPS SSD
(io1) volume aggregate IOPS quota.

**Check ID**

`tV7YY0l7J9`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EBS Provisioned IOPS SSD

(io1) Volume Storage

**Description**

Checks for usage that is more than 80% of the EBS Provisioned IOPS SSD
(io1) volume storage quota.

**Check ID**

`gI7MM0l7J9`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EBS Provisioned IOPS SSD

(io2) Volume Storage

**Description**

Checks for usage that is more than 80% of the EBS Provisioned IOPS SSD
(io2) volume storage quota.

**Check ID**

`gI7MM0l7J2`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EBS Throughput

Optimized HDD (st1) Volume Storage

**Description**

Checks for usage that is more than 80% of the EBS Throughput Optimized HDD
(st1) volume storage quota.

**Check ID**

`wH7DD0l3J9`

**Additional Resources**

[Amazon EBS
limits](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md")

## EC2 On-Demand Instances

**Description**

Checks for usage that is more than 80% of the EC2 On-Demand Instances
quota.

**Check ID**

`0Xc6LMYG8P`

**Additional Resources**

[Amazon EC2 quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md")

## EC2 Reserved Instance Leases

**Description**

Checks for usage that is more than 80% of the EC2 Reserved Instance leases
quota.

**Check ID**

`iH7PP0l7J9`

**Additional Resources**

[Amazon EC2 quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md")

## EC2-Classic Elastic IP Addresses

**Description**

Checks for usage that is more than 80% of the EC2-Classic Elastic IP
addresses quota.

**Check ID**

`aW9HH0l8J6`

**Additional Resources**

[Amazon EC2 quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md")

## EC2-VPC Elastic IP Address

**Description**

Checks for usage that is more than 80% of the EC2-VPC Elastic IP address
quota.

**Check ID**

`lN7RR0l7J9`

**Additional Resources**

[VPC Elastic IP quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-eips "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-eips")

## ELB Application Load Balancers

**Description**

Checks for usage that is more than 80% of the ELB Application Load Balancers quota.

**Check ID**

`EM8b3yLRTr`

**Additional Resources**

[Elastic Load Balancing
quotas](../../../general/latest/gr/elb.md "../../../general/latest/gr/elb.md")

## ELB Classic Load Balancers

**Description**

Checks for usage that is more than 80% of the ELB Classic Load Balancers quota.

**Check ID**

`iK7OO0l7J9`

**Additional Resources**

[Elastic Load Balancing
quotas](../../../general/latest/gr/elb.md "../../../general/latest/gr/elb.md")

## ELB Network Load Balancers

**Description**

Checks for usage that is more than 80% of the ELB Network Load Balancers quota.

**Check ID**

`8wIqYSt25K`

**Additional Resources**

[Elastic Load Balancing
quotas](../../../general/latest/gr/elb.md "../../../general/latest/gr/elb.md")

## IAM Group

**Description**

Checks for usage that is more than 80% of the IAM group quota.

**Check ID**

`sU7XX0l7J9`

**Additional Resources**

[IAM quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md")

## IAM Instance Profiles

**Description**

Checks for usage that is more than 80% of the IAM instance profiles
quota.

**Check ID**

`nO7SS0l7J9`

**Additional Resources**

[IAM quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md")

## IAM Policies

**Description**

Checks for usage that is more than 80% of the IAM policies quota.

**Check ID**

`pR7UU0l7J9`

**Additional Resources**

[IAM quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md")

## IAM Roles

**Description**

Checks for usage that is more than 80% of the IAM roles quota.

**Check ID**

`oQ7TT0l7J9`

**Additional Resources**

[IAM quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md")

## IAM Server Certificates

**Description**

Checks for usage that is more than 80% of the IAM server certificates
quota.

**Check ID**

`rT7WW0l7J9`

**Additional Resources**

[IAM quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md")

## IAM Users

**Description**

Checks for usage that is more than 80% of the IAM users quota.

**Check ID**

`qS7VV0l7J9`

**Additional Resources**

[IAM quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md")

## Kinesis Shards per Region

**Description**

Checks for usage that is more than 80% of the Kinesis shards per Region
quota.

**Check ID**

`bW7HH0l7J9`

**Additional Resources**

[Kinesis quotas](../../../streams/latest/dev/service-sizes-and-limits.md "../../../streams/latest/dev/service-sizes-and-limits.md")

## Lambda Code Storage Usage

**Description**

Checks for code storage usage that is more than 80% of the account limit.

###### Note

Results for this check are automatically refreshed several times
daily, and refresh requests are not allowed. It might take a few
hours for changes to appear.

For AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md") API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**

`c1dfprch07`

**Alert Criteria**

- Yellow: 80% of limit reached.

**Recommended Action**

Please identify unused lambda functions or versions and remove them to free up the code storage for your account in the region. If you need additional storage, please create a support case in Support Center. If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can open a support case in Support Center.

**Additional Resources**

- [Lambda Code Storage Usage](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md")

**Report columns**

- Status
- Region
- The qualified function ARN for this resource.
- The function code storage usage in MegaBytes with 2 decimals.
- The amount of versions in the function
- Last Updated Time

## RDS Cluster Parameter Groups

**Description**

Checks for usage that is more than 80% of the RDS cluster parameter groups
quota.

**Check ID**

`jtlIMO3qZM`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Cluster Roles

**Description**

Checks for usage that is more than 80% of the RDS cluster roles
quota.

**Check ID**

`7fuccf1Mx7`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Clusters

**Description**

Checks for usage that is more than 80% of the RDS clusters quota.

**Check ID**

`gjqMBn6pjz`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS DB Instances

**Description**

Checks for usage that is more than 80% of the RDS DB instances
quota.

**Check ID**

`XG0aXHpIEt`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS DB Manual Snapshots

**Description**

Checks for usage that is more than 80% of the RDS DB manual snapshots
quota.

**Check ID**

`dV84wpqRUs`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS DB Parameter Groups

**Description**

Checks for usage that is more than 80% of the RDS DB parameter groups
quota.

**Check ID**

`jEECYg2YVU`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS DB Security Groups

**Description**

Checks for usage that is more than 80% of the RDS DB security groups
quota.

**Check ID**

`gfZAn3W7wl`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Event Subscriptions

**Description**

Checks for usage that is more than 80% of the RDS event subscriptions
quota.

**Check ID**

`keAhfbH5yb`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Max Auths per Security

Group

**Description**

Checks for usage that is more than 80% of the RDS max auths per security
group quota.

**Check ID**

`dBkuNCvqn5`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Option Groups

**Description**

Checks for usage that is more than 80% of the RDS option groups
quota.

**Check ID**

`3Njm0DJQO9`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Read Replicas per Master

**Description**

Checks for usage that is more than 80% of the RDS read replicas per master
quota.

**Check ID**

`pYW8UkYz2w`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Reserved Instances

**Description**

Checks for usage that is more than 80% of the RDS Reserved Instances
quota.

**Check ID**

`UUDvOa5r34`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Subnet Groups

**Description**

Checks for usage that is more than 80% of the RDS subnet groups
quota.

**Check ID**

`dYWBaXaaMM`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Subnets per Subnet Group

**Description**

Checks for usage that is more than 80% of the RDS subnets per subnet group
quota.

**Check ID**

`jEhCtdJKOY`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## RDS Total Storage Quota

**Description**

Checks for usage that is more than 80% of the RDS total storage
quota.

**Check ID**

`P1jhKWEmLa`

**Additional Resources**

[Amazon RDS quotas](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")

## Route 53 Hosted Zones

**Description**

Checks for usage that is more than 80% of the Route 53 hosted zones quota per
account.

**Check ID**

`dx3xfcdfMr`

**Additional Resources**

[Route 53
quotas](../../../general/latest/gr/r53.md "../../../general/latest/gr/r53.md")

## Route 53 Max Health Checks

**Description**

Checks for usage that is more than 80% of the Route 53 health checks quota
per account.

**Check ID**

`ru4xfcdfMr`

**Additional Resources**

[Route 53
quotas](../../../general/latest/gr/r53.md "../../../general/latest/gr/r53.md")

## Route 53 Reusable Delegation

Sets

**Description**

Checks for usage that is more than 80% of the Route 53 reusable delegation
sets quota per account.

**Check ID**

`ty3xfcdfMr`

**Additional Resources**

[Route 53
quotas](../../../general/latest/gr/r53.md "../../../general/latest/gr/r53.md")

## Route 53 Traffic Policies

**Description**

Checks for usage that is more than 80% of the Route 53 traffic policies quota
per account.

**Check ID**

`dx3xfbjfMr`

**Additional Resources**

[Route 53
quotas](../../../general/latest/gr/r53.md "../../../general/latest/gr/r53.md")

## Route 53 Traffic Policy

Instances

**Description**

Checks for usage that is more than 80% of the Route 53 traffic policy
instances quota per account.

**Check ID**

`dx8afcdfMr`

**Additional Resources**

[Route 53
quotas](../../../general/latest/gr/r53.md "../../../general/latest/gr/r53.md")

## SES Daily Sending Quota

**Description**

Checks for usage that is more than 80% of the Amazon SES daily sending
quota.

**Check ID**

`hJ7NN0l7J9`

**Additional Resources**

[Amazon SES
quotas](../../../ses/latest/dg/quotas.md "../../../ses/latest/dg/quotas.md")

## VPC

**Description**

Checks for usage that is more than 80% of the VPC quota.

**Check ID**

`jL7PP0l7J9`

**Additional Resources**

[VPC quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md")

## VPC Internet Gateways

**Description**

Checks for usage that is more than 80% of the VPC Internet gateways
quota.

**Check ID**

`kM7QQ0l7J9`

**Additional Resources**

[VPC quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md")
