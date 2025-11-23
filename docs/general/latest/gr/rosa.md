# Red Hat OpenShift Service on AWS endpoints and quotas

Red Hat OpenShift Service on AWS (ROSA) currently does not support programmatic access to service endpoints via the AWS CLI. The following are the AWS Regions and service quotas for this service.
Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more
information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

## Service endpoints

| Region name               | Region         | Available for ROSA with hosted control planes | Available for ROSA classic |
| ------------------------- | -------------- | --------------------------------------------- | -------------------------- |
| US East (N. Virginia)     | us-east-1      | Yes                                           | Yes                        |
| US East (Ohio)            | us-east-2      | Yes                                           | Yes                        |
| US West (N. California)   | us-west-1      | No                                            | Yes                        |
| US West (Oregon)          | us-west-2      | Yes                                           | Yes                        |
| Africa (Cape Town)        | af-south-1     | Yes                                           | Yes                        |
| Asia Pacific (Hong Kong)  | ap-east-1      | Yes                                           | Yes                        |
| Asia Pacific (Hyderabad)  | ap-south-2     | Yes                                           | Yes                        |
| Asia Pacific (Jakarta)    | ap-southeast-3 | Yes                                           | Yes                        |
| Asia Pacific (Melbourne)  | ap-southeast-4 | Yes                                           | Yes                        |
| Asia Pacific (Mumbai)     | ap-south-1     | Yes                                           | Yes                        |
| Asia Pacific (Osaka)      | ap-northeast-3 | Yes                                           | Yes                        |
| Asia Pacific (Seoul)      | ap-northeast-2 | Yes                                           | Yes                        |
| Asia Pacific (Singapore)  | ap-southeast-1 | Yes                                           | Yes                        |
| Asia Pacific (Sydney)     | ap-southeast-2 | Yes                                           | Yes                        |
| Asia Pacific (Tokyo)      | ap-northeast-1 | Yes                                           | Yes                        |
| Canada (Central)          | ca-central-1   | Yes                                           | Yes                        |
| Europe (Frankfurt)        | eu-central-1   | Yes                                           | Yes                        |
| Europe (Ireland)          | eu-west-1      | Yes                                           | Yes                        |
| Europe (London)           | eu-west-2      | Yes                                           | Yes                        |
| Europe (Milan)            | eu-south-1     | Yes                                           | Yes                        |
| Europe (Paris)            | eu-west-3      | Yes                                           | Yes                        |
| Europe (Spain)            | eu-south-2     | Yes                                           | Yes                        |
| Europe (Stockholm)        | eu-north-1     | Yes                                           | Yes                        |
| Europe (Zurich)           | eu-central-2   | Yes                                           | Yes                        |
| Middle East (Bahrain)     | me-south-1     | Yes                                           | Yes                        |
| Middle East (UAE)         | me-central-1   | Yes                                           | Yes                        |
| South America (São Paulo) | sa-east-1      | Yes                                           | Yes                        |
| AWS GovCloud (US-East)    | us-gov-east-1  | No                                            | Yes                        |
| AWS GovCloud (US-West)    | us-gov-west-1  | No                                            | Yes                        |

## Service quotas

ROSA uses service quotas for Amazon EC2, Amazon Virtual Private Cloud, Amazon Elastic Block Store, and Elastic Load Balancing. These quotas are listed
in the corresponding namespace in the Service Quotas console. Although most default values are suitable for most workloads, you may need to request a quota increase for the following cases.

- ROSA classic clusters require a minimum of 100 vCPUs for cluster creation, availability, and upgrades. The default value for Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) Amazon EC2 instances is 5 vCPUs. If you do not increase this quota, cluster creation fails.
- Some optional cluster configuration features, such as custom security groups, may require you to request a quota increase. For example, ROSA associates one security group with network interfaces in worker machine pools by default. Because the default quota for security groups per network interface is 5, if you want to add 5 custom security groups you must request a quota increase to bring the total number of security groups on worker network interfaces to 6.

To increase quotas, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1216C47A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1216C47A") and request a quota increase. For more information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

###### Note

You can check your quotas using the AWS SDKs, but the SDK calculation doesn't include existing ROSA resources. The quota check in the SDK may pass, and ROSA cluster creation may fail. To fix this issue, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1216C47A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1216C47A") and request a quota increase.

| ROSA-required quotas                                             | Name | Service code | Default | Minimum required                                                                                                                                                           | Adjustable                                                                                                                                                                                                                         | Description |
| ---------------------------------------------------------------- | ---- | ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances | ec2  | 5            | 100     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1216C47A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1216C47A") | Maximum number of vCPUs assigned to the Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances.<br>The default value of 5 vCPUs is not sufficient to create ROSA clusters. ROSA requires 100 vCPUs for cluster creation. |
| Storage for General Purpose SSD (gp3) volumes, in TiB            | ebs  | 50           | 300     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ebs/quotas/L-7A658B76 "https://console.aws.amazon.com/servicequotas/home/services/ebs/quotas/L-7A658B76") | The maximum aggregated amount of storage, in TiB, that can be provisioned across General Purpose SSD (gp3) volumes in this Region.                                                                                                 |
| Storage for General Purpose SSD (gp2) volumes, in TiB            | ebs  | 50           | 300     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ebs/quotas/L-D18FCD1D "https://console.aws.amazon.com/servicequotas/home/services/ebs/quotas/L-D18FCD1D") | The maximum aggregated amount of storage, in TiB, that can be provisioned across General Purpose SSD (gp2) volumes in this Region.                                                                                                 |
| Storage for Provisioned IOPS SSD (io1) volumes, in TiB           | ebs  | 50           | 300     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ebs/quotas/L-FD252861 "https://console.aws.amazon.com/servicequotas/home/services/ebs/quotas/L-FD252861") | The maximum aggregated amount of storage, in TiB, that can be provisioned across Provisioned IOPS SSD (io1) volumes in this Region.                                                                                                |

###### Note

The default values are the initial quotas set by AWS. These default values are
separate from the actual applied quota values and maximum possible service quotas.
For more information, see [Terminology in Service Quotas](../../../servicequotas/latest/userguide/intro.md#intro_getting-started "../../../servicequotas/latest/userguide/intro.md#intro_getting-started")
in the _Service Quotas User Guide_.

### General AWS service quotas

ROSA uses the following default quotas for Amazon EC2, Amazon VPC, Amazon EBS, and ELB.

###### Amazon EC2

- [EC2-VPC Elastic IPs](ec2-service.md#limits_ec2 "ec2-service.md#limits_ec2")

###### Amazon VPC

- [VPCs per Region](vpc-service.md#vpc-quotas "vpc-service.md#vpc-quotas")
- [Network interfaces per Region](vpc-service.md#vpc-quotas "vpc-service.md#vpc-quotas")
- [Internet gateways per Region](vpc-service.md#vpc-quotas "vpc-service.md#vpc-quotas")

###### Amazon EBS

- [Snapshots per Region](ebs-service.md#limits_ebs "ebs-service.md#limits_ebs")
- [IOPS for Provisioned IOPS SSD (io1) volumes](ebs-service.md#limits_ebs "ebs-service.md#limits_ebs")

###### ELB

- [Application Load Balancers per Region](elb.md#limits_elastic_load_balancer "elb.md#limits_elastic_load_balancer")
- [Classic Load Balancers per Region](elb.md#limits_elastic_load_balancer "elb.md#limits_elastic_load_balancer")
