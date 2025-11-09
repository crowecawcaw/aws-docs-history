# Amazon Elastic VMware Service endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                                                                                               | Protocol                         |
| ------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)           | us-east-2      | evs.us-east-2.amazonaws.com<br>evs-fips.us-east-2.api.aws<br>evs-fips.us-east-2.amazonaws.com<br>evs.us-east-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)    | us-east-1      | evs.us-east-1.amazonaws.com<br>evs-fips.us-east-1.api.aws<br>evs-fips.us-east-1.amazonaws.com<br>evs.us-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | evs.us-west-2.amazonaws.com<br>evs-fips.us-west-2.api.aws<br>evs-fips.us-west-2.amazonaws.com<br>evs.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)    | ap-south-1     | evs.ap-south-1.amazonaws.com<br>evs.ap-south-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore) | ap-southeast-1 | evs.ap-southeast-1.amazonaws.com<br>evs.ap-southeast-1.api.aws                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)    | ap-southeast-2 | evs.ap-southeast-2.amazonaws.com<br>evs.ap-southeast-2.api.aws                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)     | ap-northeast-1 | evs.ap-northeast-1.amazonaws.com<br>evs.ap-northeast-1.api.aws                                                         | HTTPS<br>HTTPS                   |
| Canada (Central)         | ca-central-1   | evs.ca-central-1.amazonaws.com<br>evs.ca-central-1.api.aws                                                             | HTTPS<br>HTTPS                   |
| Europe (Frankfurt)       | eu-central-1   | evs.eu-central-1.amazonaws.com<br>evs.eu-central-1.api.aws                                                             | HTTPS<br>HTTPS                   |
| Europe (Ireland)         | eu-west-1      | evs.eu-west-1.amazonaws.com<br>evs.eu-west-1.api.aws                                                                   | HTTPS<br>HTTPS                   |
| Europe (London)          | eu-west-2      | evs.eu-west-2.amazonaws.com<br>evs.eu-west-2.api.aws                                                                   | HTTPS<br>HTTPS                   |
| Europe (Milan)           | eu-south-1     | evs.eu-south-1.amazonaws.com<br>evs.eu-south-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Europe (Paris)           | eu-west-3      | evs.eu-west-3.amazonaws.com<br>evs.eu-west-3.api.aws                                                                   | HTTPS<br>HTTPS                   |

## Service quotas

| Name                              | Default                  | Adjustable                                                                                                                                                                 | Description                                                                                       |
| --------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Environment count per AWS account | Each supported Region: 1 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/evs/quotas/L-27E780D9 "https://console.aws.amazon.com/servicequotas/home/services/evs/quotas/L-27E780D9") | The maximum number of EVS environments that can be created in this account in the current Region. |
| Host count per EVS environment    | Each supported Region: 5 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/evs/quotas/L-96A49955 "https://console.aws.amazon.com/servicequotas/home/services/evs/quotas/L-96A49955") | Maximum number of Hosts that can be provisioned within a single EVS environment                   |

These service quotas are listed under
**Amazon Elastic VMware Service** in the Service Quotas console.
To request a quota increase for values that are shown as adjustable, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_.

###### Important

To enable Amazon EVS environment creation, your host count per EVS environment quota must be at least 4. The default quota is 0. To increase this quota, go to the [Service Quotas console](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas") and request a quota increase.

###### Important

Ensure that your EC2 Running On-Demand Standard Instance quota reflects the number of vCPUs that you need for all of the EC2 instances that you will use on Amazon EVS. Each i4i.metal instance uses 128 vCPUs. For information about increasing EC2 service quotas, see [Request an increase](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#request-increase "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#request-increase") in the
_Amazon EC2 User Guide_.

###### Note

If you plan to use EC2 Dedicated Hosts for your Amazon EVS environment, ensure that your EC2 Dedicated i4i Hosts quota reflects the number of Dedicated Hosts that you intend to use for a desired Region.
For information about increasing EC2 service quotas, see [Request an increase](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#request-increase "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#request-increase") in the
_Amazon EC2 User Guide_.

###### Note

Amazon CloudWatch collects AWS usage metrics for Amazon EVS resources that have quotas (environment and hosts).
For more information, see [CloudWatch Usage Metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.md") in the _Amazon CloudWatch User Guide_.

###### Note

The default values are the initial quotas set by AWS. These default values are
separate from the actual applied quota values and maximum possible service quotas.
For more information, see [Terminology in Service Quotas](../../../servicequotas/latest/userguide/intro.md#intro_getting-started "../../../servicequotas/latest/userguide/intro.md#intro_getting-started") in the
_Service Quotas User Guide_.
