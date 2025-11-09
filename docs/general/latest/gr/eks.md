# Amazon Elastic Kubernetes Service endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                        | Protocol       |
| -------------------------- | -------------- | --------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | eks.us-east-2.amazonaws.com<br>fips.eks.us-east-2.amazonaws.com | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | eks.us-east-1.amazonaws.com<br>fips.eks.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | eks.us-west-1.amazonaws.com<br>fips.eks.us-west-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | eks.us-west-2.amazonaws.com<br>fips.eks.us-west-2.amazonaws.com | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | eks.af-south-1.amazonaws.com                                    | HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | eks.ap-east-1.amazonaws.com                                     | HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | eks.ap-south-2.amazonaws.com                                    | HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | eks.ap-southeast-3.amazonaws.com                                | HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | eks.ap-southeast-5.amazonaws.com                                | HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | eks.ap-southeast-4.amazonaws.com                                | HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | eks.ap-south-1.amazonaws.com                                    | HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | eks.ap-southeast-6.amazonaws.com                                | HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | eks.ap-northeast-3.amazonaws.com                                | HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | eks.ap-northeast-2.amazonaws.com                                | HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | eks.ap-southeast-1.amazonaws.com                                | HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | eks.ap-southeast-2.amazonaws.com                                | HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | eks.ap-east-2.amazonaws.com                                     | HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | eks.ap-southeast-7.amazonaws.com                                | HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | eks.ap-northeast-1.amazonaws.com                                | HTTPS          |
| Canada (Central)           | ca-central-1   | eks.ca-central-1.amazonaws.com                                  | HTTPS          |
| Canada West (Calgary)      | ca-west-1      | eks.ca-west-1.amazonaws.com                                     | HTTPS          |
| Europe (Frankfurt)         | eu-central-1   | eks.eu-central-1.amazonaws.com                                  | HTTPS          |
| Europe (Ireland)           | eu-west-1      | eks.eu-west-1.amazonaws.com                                     | HTTPS          |
| Europe (London)            | eu-west-2      | eks.eu-west-2.amazonaws.com                                     | HTTPS          |
| Europe (Milan)             | eu-south-1     | eks.eu-south-1.amazonaws.com                                    | HTTPS          |
| Europe (Paris)             | eu-west-3      | eks.eu-west-3.amazonaws.com                                     | HTTPS          |
| Europe (Spain)             | eu-south-2     | eks.eu-south-2.amazonaws.com                                    | HTTPS          |
| Europe (Stockholm)         | eu-north-1     | eks.eu-north-1.amazonaws.com                                    | HTTPS          |
| Europe (Zurich)            | eu-central-2   | eks.eu-central-2.amazonaws.com                                  | HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | eks.il-central-1.amazonaws.com                                  | HTTPS          |
| Mexico (Central)           | mx-central-1   | eks.mx-central-1.amazonaws.com                                  | HTTPS          |
| Middle East (Bahrain)      | me-south-1     | eks.me-south-1.amazonaws.com                                    | HTTPS          |
| Middle East (UAE)          | me-central-1   | eks.me-central-1.amazonaws.com                                  | HTTPS          |
| South America (São Paulo)  | sa-east-1      | eks.sa-east-1.amazonaws.com                                     | HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | eks.us-gov-east-1.amazonaws.com                                 | HTTPS          |
| AWS GovCloud (US-West)     | us-gov-west-1  | eks.us-gov-west-1.amazonaws.com                                 | HTTPS          |

Additionally, the EKS API has dual-stack endpoints. The dual-stack endpoint was introduced in
August 2024. To use the dual-stack endpoints with the AWS CLI, see the [Dual-stack and FIPS endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md") configuration in the
_AWS SDKs and Tools Reference Guide_. The following lists the new
endpoints:

EKS API public endpoint
`eks.`region`.api.aws`

IRSA OIDC Issuer URLs
`oidc-eks.`region`.api.aws`

The following endpoint provides the Amazon EKS Auth API. The EKS Pod Identity Agent on your
nodes connects to this endpoint to get the credentials for each pod.

| Region Name                | Region         | Endpoint                        | Protocol |
| -------------------------- | -------------- | ------------------------------- | -------- |
| US East (Ohio)             | us-east-2      | eks-auth.us-east-2.api.aws      | HTTPS    |
| US East (N. Virginia)      | us-east-1      | eks-auth.us-east-1.api.aws      | HTTPS    |
| US West (N. California)    | us-west-1      | eks-auth.us-west-1.api.aws      | HTTPS    |
| US West (Oregon)           | us-west-2      | eks-auth.us-west-2.api.aws      | HTTPS    |
| Africa (Cape Town)         | af-south-1     | eks-auth.af-south-1.api.aws     | HTTPS    |
| Asia Pacific (Hong Kong)   | ap-east-1      | eks-auth.ap-east-1.api.aws      | HTTPS    |
| Asia Pacific (Hyderabad)   | ap-south-2     | eks-auth.ap-south-2.api.aws     | HTTPS    |
| Asia Pacific (Jakarta)     | ap-southeast-3 | eks-auth.ap-southeast-3.api.aws | HTTPS    |
| Asia Pacific (Malaysia)    | ap-southeast-5 | eks-auth.ap-southeast-5.api.aws | HTTPS    |
| Asia Pacific (Melbourne)   | ap-southeast-4 | eks-auth.ap-southeast-4.api.aws | HTTPS    |
| Asia Pacific (Mumbai)      | ap-south-1     | eks-auth.ap-south-1.api.aws     | HTTPS    |
| Asia Pacific (New Zealand) | ap-southeast-6 | eks-auth.ap-southeast-6.api.aws | HTTPS    |
| Asia Pacific (Osaka)       | ap-northeast-3 | eks-auth.ap-northeast-3.api.aws | HTTPS    |
| Asia Pacific (Seoul)       | ap-northeast-2 | eks-auth.ap-northeast-2.api.aws | HTTPS    |
| Asia Pacific (Singapore)   | ap-southeast-1 | eks-auth.ap-southeast-1.api.aws | HTTPS    |
| Asia Pacific (Sydney)      | ap-southeast-2 | eks-auth.ap-southeast-2.api.aws | HTTPS    |
| Asia Pacific (Taipei)      | ap-east-2      | eks-auth.ap-east-2.api.aws      | HTTPS    |
| Asia Pacific (Thailand)    | ap-southeast-7 | eks-auth.ap-southeast-7.api.aws | HTTPS    |
| Asia Pacific (Tokyo)       | ap-northeast-1 | eks-auth.ap-northeast-1.api.aws | HTTPS    |
| Canada (Central)           | ca-central-1   | eks-auth.ca-central-1.api.aws   | HTTPS    |
| Canada West (Calgary)      | ca-west-1      | eks-auth.ca-west-1.api.aws      | HTTPS    |
| Europe (Frankfurt)         | eu-central-1   | eks-auth.eu-central-1.api.aws   | HTTPS    |
| Europe (Ireland)           | eu-west-1      | eks-auth.eu-west-1.api.aws      | HTTPS    |
| Europe (London)            | eu-west-2      | eks-auth.eu-west-2.api.aws      | HTTPS    |
| Europe (Milan)             | eu-south-1     | eks-auth.eu-south-1.api.aws     | HTTPS    |
| Europe (Paris)             | eu-west-3      | eks-auth.eu-west-3.api.aws      | HTTPS    |
| Europe (Spain)             | eu-south-2     | eks-auth.eu-south-2.api.aws     | HTTPS    |
| Europe (Stockholm)         | eu-north-1     | eks-auth.eu-north-1.api.aws     | HTTPS    |
| Europe (Zurich)            | eu-central-2   | eks-auth.eu-central-2.api.aws   | HTTPS    |
| Israel (Tel Aviv)          | il-central-1   | eks-auth.il-central-1.api.aws   | HTTPS    |
| Mexico (Central)           | mx-central-1   | eks-auth.mx-central-1.api.aws   | HTTPS    |
| Middle East (Bahrain)      | me-south-1     | eks-auth.me-south-1.api.aws     | HTTPS    |
| Middle East (UAE)          | me-central-1   | eks-auth.me-central-1.api.aws   | HTTPS    |
| South America (São Paulo)  | sa-east-1      | eks-auth.sa-east-1.api.aws      | HTTPS    |
| AWS GovCloud (US-East)     | us-gov-east-1  | eks-auth.us-gov-east-1.api.aws  | HTTPS    |
| AWS GovCloud (US-West)     | us-gov-west-1  | eks-auth.us-gov-west-1.api.aws  | HTTPS    |

## Service quotas

| Name                                           | Default                      | Adjustable                                                                                                                                                                 | Description                                                                                                                       |
| ---------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Access entries per cluster                     | Each supported Region: 3,000 | No                                                                                                                                                                         | The maximum number of access entries per cluster.                                                                                 |
| Clusters                                       | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-1194D53C "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-1194D53C") | The maximum number of EKS clusters in this account in the current Region.                                                         |
| Control plane security groups per cluster      | Each supported Region: 4     | No                                                                                                                                                                         | The maximum number of control plane security groups per cluster (these are specified when you create the cluster).                |
| EKS Anywhere Enterprise Subscriptions          | Each supported Region: 10    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-EA277FDC "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-EA277FDC") | The maximum number of EKS Anywhere Enterprise Subscriptions in this account in the current Region.                                |
| Fargate profiles per cluster                   | Each supported Region: 10    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-33415657 "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-33415657") | The maximum number of Fargate profiles per cluster.                                                                               |
| Label pairs per Fargate profile selector       | Each supported Region: 5     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-23414FF3 "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-23414FF3") | The maximum number of label pairs per Fargate profile selector.                                                                   |
| Managed node groups per cluster                | Each supported Region: 30    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-6D54EA21 "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-6D54EA21") | The maximum number of managed node groups per cluster.                                                                            |
| Nodes per managed node group                   | Each supported Region: 450   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-BD136A63 "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-BD136A63") | The maximum number of nodes per managed node group.                                                                               |
| Public endpoint access CIDR ranges per cluster | Each supported Region: 40    | No                                                                                                                                                                         | The maximum number of public endpoint access CIDR ranges per cluster (these are specified when you create or update the cluster). |
| Registered clusters                            | Each supported Region: 10    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-FDFA5F81 "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-FDFA5F81") | The maximum number of registered clusters in this account in the current Region.                                                  |
| Remote node networks per cluster               | Each supported Region: 15    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-5C12D558 "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-5C12D558") | The maximum number of remote node networks per cluster.                                                                           |
| Remote pod networks per cluster                | Each supported Region: 15    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-6AFFD1D8 "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-6AFFD1D8") | The maximum number of remote pod networks per cluster.                                                                            |
| Selectors per Fargate profile                  | Each supported Region: 5     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-D78D8AF8 "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas/L-D78D8AF8") | The maximum number of selectors per Fargate profile.                                                                              |

###### Note

The default values are the initial quotas set by AWS. These default values are
separate from the actual applied quota values and maximum possible service quotas.
For more information, see [Terminology in Service Quotas](../../../servicequotas/latest/userguide/intro.md#intro_getting-started "../../../servicequotas/latest/userguide/intro.md#intro_getting-started") in the
_Service Quotas User Guide_.

These service quotas are listed under
**Amazon Elastic Kubernetes Service (Amazon EKS)** in the Service Quotas console.
To request a quota increase for values that are shown as adjustable, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_.

## AWS Fargate service quotas

The **AWS Fargate** service in the Service Quotas console lists several
service quotas. The following table only describes the quota that is applicable to
Amazon EKS.

New AWS accounts might have lower initial quotas that can increase over time.
Fargate constantly monitors the account usage within each AWS Region, and then
automatically increases the quotas based on the usage. You can also request a quota
increase for values that are shown as adjustable. For more information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_.

| Name                                  | Default | Adjustable                                                                                                                                                   | Description                                                                                                          |
| ------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Fargate On-Demand vCPU resource count | 6       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/fargate/quotas "https://console.aws.amazon.com/servicequotas/home/services/fargate/quotas") | The number of Fargate vCPUs that can run concurrently as<br>Fargate On-Demand in this account in the current Region. |

###### Note

The default values are the initial quotas set by AWS. These default values are
separate from the actual applied quota values and maximum possible service quotas.
For more information, see [Terminology in Service Quotas](../../../servicequotas/latest/userguide/intro.md#intro_getting-started "../../../servicequotas/latest/userguide/intro.md#intro_getting-started") in the
_Service Quotas User Guide_.

###### Note

Fargate additionally enforces Amazon ECS tasks and Amazon EKS pods launch rate quotas. For
more information, see [AWS Fargate throttling
quotas](../../../AmazonECS/latest/userguide/throttling.md "../../../AmazonECS/latest/userguide/throttling.md") in the _Amazon Elastic Container Service User Guide for AWS Fargate_.
