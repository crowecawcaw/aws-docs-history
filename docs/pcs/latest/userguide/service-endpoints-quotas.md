# Endpoints and service quotas for

AWS PCS

The following sections describe the endpoints and service quotas for AWS Parallel Computing Service
(AWS PCS). Service quotas, formerly referred to as _limits_,
are the maximum number of service resources or operations for your AWS account.

Your AWS account has default quotas for each AWS service.
Unless otherwise noted, each quota is Region-specific. You can request
increases for some quotas, and other quotas cannot be increased.

For more information, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
in the _AWS General Reference_.

###### Contents

- [Service endpoints](service-endpoints-quotas.md#service-endpoints-quotas_endpoints "service-endpoints-quotas.md#service-endpoints-quotas_endpoints")
- [Service quotas](service-endpoints-quotas.md#service-endpoints-quotas_quotas "service-endpoints-quotas.md#service-endpoints-quotas_quotas")
  - [Internal quotas](service-endpoints-quotas.md#service-endpoints-quotas_internal "service-endpoints-quotas.md#service-endpoints-quotas_internal")
  - [Relevant quotas for other AWS services](service-endpoints-quotas.md#service-endpoints-quotas_other "service-endpoints-quotas.md#service-endpoints-quotas_other")

## Service endpoints

| Region name              | Region         | Endpoint                                                                                                                               | Protocol |
| ------------------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| US East (Ohio)           | us-east-2      | pcs.us-east-2.amazonaws.com<br>pcs-fips.us-east-2.amazonaws.com<br>pcs-fips.us-east-2.api.aws<br>pcs.us-east-2.api.aws                 | HTTPS    |
| US East (N. Virginia)    | us-east-1      | pcs.us-east-1.amazonaws.com<br>pcs-fips.us-east-1.amazonaws.com<br>pcs-fips.us-east-1.api.aws<br>pcs.us-east-1.api.aws                 | HTTPS    |
| US West (Oregon)         | us-west-2      | pcs.us-west-2.amazonaws.com<br>pcs-fips.us-west-2.amazonaws.com<br>pcs-fips.us-west-2.api.aws<br>pcs.us-west-2.api.aws                 | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | pcs.ap-southeast-1.amazonaws.com<br>pcs.ap-southeast-1.api.aws                                                                         | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | pcs.ap-southeast-2.amazonaws.com<br>pcs.ap-southeast-2.api.aws                                                                         | HTTPS    |
| Asia Pacific (Tokyo)     | ap-northeast-1 | pcs.ap-northeast-1.amazonaws.com<br>pcs.ap-northeast-1.api.aws                                                                         | HTTPS    |
| Europe (Frankfurt)       | eu-central-1   | pcs.eu-central-1.amazonaws.com<br>pcs.eu-central-1.api.aws                                                                             | HTTPS    |
| Europe (Ireland)         | eu-west-1      | pcs.eu-west-1.amazonaws.com<br>pcs.eu-west-1.api.aws                                                                                   | HTTPS    |
| Europe (London)          | eu-west-2      | pcs.eu-west-2.amazonaws.com<br>pcs.eu-west-2.api.aws                                                                                   | HTTPS    |
| Europe (Stockholm)       | eu-north-1     | pcs.eu-north-1.amazonaws.com<br>pcs.eu-north-1.api.aws                                                                                 | HTTPS    |
| AWS GovCloud (US-East)   | us-gov-east-1  | pcs.us-gov-east-1.amazonaws.com<br>pcs-fips.us-gov-east-1.amazonaws.com<br>pcs-fips.us-gov-east-1.api.aws<br>pcs.us-gov-east-1.api.aws | HTTPS    |
| AWS GovCloud (US-West)   | us-gov-west-1  | pcs.us-gov-west-1.amazonaws.com<br>pcs-fips.us-gov-west-1.amazonaws.com<br>pcs-fips.us-gov-west-1.api.aws<br>pcs.us-gov-west-1.api.aws | HTTPS    |

## Service quotas

| **Name** | **Default** | **Adjustable** | **Description**                                |
| -------- | ----------- | -------------- | ---------------------------------------------- |
| Clusters | 5           | Yes            | The maximum number of clusters per AWS Region. |

###### Note

The default values are the initial quotas set by AWS. These default values
are separate from the actual applied quota values and maximum possible service
quotas. For more information, see [Terminology in Service Quotas](../../../servicequotas/latest/userguide/intro.md#intro_getting-started "../../../servicequotas/latest/userguide/intro.md#intro_getting-started") in the
_Service Quotas User Guide_.

These service quotas are listed under **AWS Parallel Computing Service
(PCS)** in the [AWS Management Console](https://console.aws.amazon.com/servicequotas/home/services "https://console.aws.amazon.com/servicequotas/home/services").
To request a quota increase for values that are shown as adjustable,
see [Requesting a
Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

###### Important

Remember to check the current AWS Region setting in the AWS Management Console.

### Internal quotas

The following quotas are internal and non-adjustable.

| **Name**                        | **Default** | **Adjustable** | **Description**                                                        |
| ------------------------------- | ----------- | -------------- | ---------------------------------------------------------------------- |
| Concurrent cluster creation     | 1           | No             | The maximum number of clusters in the `Creating` state per AWS Region. |
| Compute node groups per cluster | 10          | No             | The maximum number of compute node groups per cluster.                 |
| Queues per cluster              | 10          | No             | The maximum number of queues per cluster.                              |

### Relevant quotas for other AWS services

AWS PCS uses other AWS services. Your service quotas
for those services impact your use of AWS PCS.

###### Amazon EC2 service quotas that impact AWS PCS

- Spot instance requests
- Running on-demand instances
- Launch templates
- Launch template versions
- Amazon EC2 API requests

For more information, see [Amazon EC2 service quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md")
in the _Amazon Elastic Compute Cloud User Guide_.
