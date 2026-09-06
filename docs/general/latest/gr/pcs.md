

# AWS Parallel Computing Service endpoints and quotas
<a name="pcs"></a>

The following tables describe the service endpoints and service quotas for AWS Parallel Computing Service. Service quotas, also referred to as *limits*, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

## Service endpoints
<a name="pcs_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  pcs.us-east-2.amazonaws.com <br /> pcs-fips.us-east-2.amazonaws.com <br /> pcs-fips.us-east-2.api.aws <br /> pcs.us-east-2.api.aws  | <br /><br /><br /> | 
| US East (N. Virginia) | us-east-1 |  pcs.us-east-1.amazonaws.com <br /> pcs-fips.us-east-1.amazonaws.com <br /> pcs-fips.us-east-1.api.aws <br /> pcs.us-east-1.api.aws  | <br /><br /><br /> | 
| US West (Oregon) | us-west-2 |  pcs.us-west-2.amazonaws.com <br /> pcs-fips.us-west-2.amazonaws.com <br /> pcs-fips.us-west-2.api.aws <br /> pcs.us-west-2.api.aws  | <br /><br /><br /> | 
| Africa (Cape Town) | af-south-1 |  pcs.af-south-1.amazonaws.com <br /> pcs.af-south-1.api.aws  | <br /> | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  pcs.ap-southeast-3.amazonaws.com <br /> pcs.ap-southeast-3.api.aws  | <br /> | 
| Asia Pacific (Mumbai) | ap-south-1 |  pcs.ap-south-1.amazonaws.com <br /> pcs.ap-south-1.api.aws  | <br /> | 
| Asia Pacific (Osaka) | ap-northeast-3 |  pcs.ap-northeast-3.amazonaws.com <br /> pcs.ap-northeast-3.api.aws  | <br /> | 
| Asia Pacific (Seoul) | ap-northeast-2 |  pcs.ap-northeast-2.amazonaws.com <br /> pcs.ap-northeast-2.api.aws  | <br /> | 
| Asia Pacific (Singapore) | ap-southeast-1 |  pcs.ap-southeast-1.amazonaws.com <br /> pcs.ap-southeast-1.api.aws  | <br /> | 
| Asia Pacific (Sydney) | ap-southeast-2 |  pcs.ap-southeast-2.amazonaws.com <br /> pcs.ap-southeast-2.api.aws  | <br /> | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  pcs.ap-northeast-1.amazonaws.com <br /> pcs.ap-northeast-1.api.aws  | <br /> | 
| Europe (Frankfurt) | eu-central-1 |  pcs.eu-central-1.amazonaws.com <br /> pcs.eu-central-1.api.aws  | <br /> | 
| Europe (Ireland) | eu-west-1 |  pcs.eu-west-1.amazonaws.com <br /> pcs.eu-west-1.api.aws  | <br /> | 
| Europe (London) | eu-west-2 |  pcs.eu-west-2.amazonaws.com <br /> pcs.eu-west-2.api.aws  | <br /> | 
| Europe (Milan) | eu-south-1 |  pcs.eu-south-1.amazonaws.com <br /> pcs.eu-south-1.api.aws  | <br /> | 
| Europe (Paris) | eu-west-3 |  pcs.eu-west-3.amazonaws.com <br /> pcs.eu-west-3.api.aws  | <br /> | 
| Europe (Spain) | eu-south-2 |  pcs.eu-south-2.amazonaws.com <br /> pcs.eu-south-2.api.aws  | <br /> | 
| Europe (Stockholm) | eu-north-1 |  pcs.eu-north-1.amazonaws.com <br /> pcs.eu-north-1.api.aws  | <br /> | 
| South America (São Paulo) | sa-east-1 |  pcs.sa-east-1.amazonaws.com <br /> pcs.sa-east-1.api.aws  | <br /> | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  pcs.us-gov-east-1.amazonaws.com <br /> pcs-fips.us-gov-east-1.amazonaws.com <br /> pcs-fips.us-gov-east-1.api.aws <br /> pcs.us-gov-east-1.api.aws  | <br /><br /><br /> | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  pcs.us-gov-west-1.amazonaws.com <br /> pcs-fips.us-gov-west-1.amazonaws.com <br /> pcs-fips.us-gov-west-1.api.aws <br /> pcs.us-gov-west-1.api.aws  | <br /><br /><br /> | 

## Service quotas
<a name="limits_pcs"></a>


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Clusters | Each supported Region: 5 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/pcs/quotas/L-0ADE95E3)  | The maximum number of clusters per Region. | 

## Internal quotas
<a name="limits_pcs_internal"></a>

The following quotas are internal and non-adjustable.


|  **Name**  |  **Default**  |  **Adjustable**  |  **Description**  | 
| --- | --- | --- | --- | 
| Concurrent cluster creation | 1 | No | The maximum number of clusters in the `Creating` state per AWS Region. | 

## Relevant quotas for other AWS services
<a name="limits_pcs_other"></a>

AWS PCS uses other AWS services. Your service quotas for those services impact your use of AWS PCS.

**Amazon EC2 service quotas that impact AWS PCS**
+ Spot instance requests
+ Running on-demand instances
+ Launch templates
+ Launch template versions
+ Amazon EC2 API requests

For more information, see [Amazon EC2 endpoints and quotas](ec2-service.md).