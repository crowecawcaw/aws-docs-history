

# Amazon Application Recovery Controller (ARC) endpoints and quotas
<a name="arc"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="arc_region"></a>

### Zonal shift
<a name="arc_region_zonal_shift"></a>

Zonal shift in ARC is available in all AWS Regions, including the Beijing and Ningxia Regions and AWS GovCloud (US). The Region switch, routing control, and readiness check capabilities of the ARC service are not available in the Beijing and Ningxia Regions nor in AWS GovCloud (US). 

For the ARC **Zonal Shift API**, including API operations for zonal autoshift in the Regions that include the zonal autoshift capability, use the following endpoints.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  arc-zonal-shift.us-east-2.amazonaws.com <br /> arc-zonal-shift-fips.us-east-2.api.aws <br /> arc-zonal-shift.us-east-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  arc-zonal-shift.us-east-1.amazonaws.com <br /> arc-zonal-shift-fips.us-east-1.api.aws <br /> arc-zonal-shift.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  arc-zonal-shift.us-west-1.amazonaws.com <br /> arc-zonal-shift-fips.us-west-1.api.aws <br /> arc-zonal-shift.us-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  arc-zonal-shift.us-west-2.amazonaws.com <br /> arc-zonal-shift-fips.us-west-2.api.aws <br /> arc-zonal-shift.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  arc-zonal-shift.af-south-1.amazonaws.com <br /> arc-zonal-shift.af-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  arc-zonal-shift.ap-east-1.amazonaws.com <br /> arc-zonal-shift.ap-east-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  arc-zonal-shift.ap-south-2.amazonaws.com <br /> arc-zonal-shift.ap-south-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  arc-zonal-shift.ap-southeast-3.amazonaws.com <br /> arc-zonal-shift.ap-southeast-3.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  arc-zonal-shift.ap-southeast-5.amazonaws.com <br /> arc-zonal-shift.ap-southeast-5.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  arc-zonal-shift.ap-southeast-4.amazonaws.com <br /> arc-zonal-shift.ap-southeast-4.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  arc-zonal-shift.ap-south-1.amazonaws.com <br /> arc-zonal-shift.ap-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  arc-zonal-shift.ap-southeast-6.amazonaws.com <br /> arc-zonal-shift.ap-southeast-6.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  arc-zonal-shift.ap-northeast-3.amazonaws.com <br /> arc-zonal-shift.ap-northeast-3.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  arc-zonal-shift.ap-northeast-2.amazonaws.com <br /> arc-zonal-shift.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  arc-zonal-shift.ap-southeast-1.amazonaws.com <br /> arc-zonal-shift.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  arc-zonal-shift.ap-southeast-2.amazonaws.com <br /> arc-zonal-shift.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  arc-zonal-shift.ap-east-2.amazonaws.com <br /> arc-zonal-shift.ap-east-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  arc-zonal-shift.ap-southeast-7.amazonaws.com <br /> arc-zonal-shift.ap-southeast-7.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  arc-zonal-shift.ap-northeast-1.amazonaws.com <br /> arc-zonal-shift.ap-northeast-1.api.aws  | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  arc-zonal-shift.ca-central-1.amazonaws.com <br /> arc-zonal-shift-fips.ca-central-1.api.aws <br /> arc-zonal-shift.ca-central-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| Canada West (Calgary) | ca-west-1 |  arc-zonal-shift.ca-west-1.amazonaws.com <br /> arc-zonal-shift-fips.ca-west-1.api.aws <br /> arc-zonal-shift.ca-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  arc-zonal-shift.eu-central-1.amazonaws.com <br /> arc-zonal-shift.eu-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  arc-zonal-shift.eu-west-1.amazonaws.com <br /> arc-zonal-shift.eu-west-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  arc-zonal-shift.eu-west-2.amazonaws.com <br /> arc-zonal-shift.eu-west-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Milan) | eu-south-1 |  arc-zonal-shift.eu-south-1.amazonaws.com <br /> arc-zonal-shift.eu-south-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Paris) | eu-west-3 |  arc-zonal-shift.eu-west-3.amazonaws.com <br /> arc-zonal-shift.eu-west-3.api.aws  | HTTPS<br />HTTPS | 
| Europe (Spain) | eu-south-2 |  arc-zonal-shift.eu-south-2.amazonaws.com <br /> arc-zonal-shift.eu-south-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Stockholm) | eu-north-1 |  arc-zonal-shift.eu-north-1.amazonaws.com <br /> arc-zonal-shift.eu-north-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Zurich) | eu-central-2 |  arc-zonal-shift.eu-central-2.amazonaws.com <br /> arc-zonal-shift.eu-central-2.api.aws  | HTTPS<br />HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  arc-zonal-shift.il-central-1.amazonaws.com <br /> arc-zonal-shift.il-central-1.api.aws  | HTTPS<br />HTTPS | 
| Mexico (Central) | mx-central-1 |  arc-zonal-shift.mx-central-1.amazonaws.com <br /> arc-zonal-shift.mx-central-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (Bahrain) | me-south-1 |  arc-zonal-shift.me-south-1.amazonaws.com <br /> arc-zonal-shift.me-south-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (UAE) | me-central-1 |  arc-zonal-shift.me-central-1.amazonaws.com <br /> arc-zonal-shift.me-central-1.api.aws  | HTTPS<br />HTTPS | 
| South America (São Paulo) | sa-east-1 |  arc-zonal-shift.sa-east-1.amazonaws.com <br /> arc-zonal-shift.sa-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  arc-zonal-shift.us-gov-east-1.amazonaws.com <br /> arc-zonal-shift-fips.us-gov-east-1.api.aws <br /> arc-zonal-shift.us-gov-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  arc-zonal-shift.us-gov-west-1.amazonaws.com <br /> arc-zonal-shift-fips.us-gov-west-1.api.aws <br /> arc-zonal-shift.us-gov-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS | 

### Regional features
<a name="r53_region_regional"></a>

For the ARC **Region switch API**, use the following endpoints.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  arc-region-switch.us-east-2.api.aws <br /> arc-region-switch-fips.us-east-2.api.aws  | HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  arc-region-switch.us-east-1.api.aws <br /> arc-region-switch-control-plane-fips.us-east-1.api.aws <br /> arc-region-switch-fips.us-east-1.api.aws <br /> arc-region-switch-control-plane.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  arc-region-switch.us-west-1.api.aws <br /> arc-region-switch-fips.us-west-1.api.aws  | HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  arc-region-switch.us-west-2.api.aws <br /> arc-region-switch-fips.us-west-2.api.aws  | HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  arc-region-switch.af-south-1.api.aws  | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  arc-region-switch.ap-east-1.api.aws  | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  arc-region-switch.ap-south-2.api.aws  | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  arc-region-switch.ap-southeast-3.api.aws  | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  arc-region-switch.ap-southeast-5.api.aws  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  arc-region-switch.ap-southeast-4.api.aws  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  arc-region-switch.ap-south-1.api.aws  | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  arc-region-switch.ap-southeast-6.api.aws  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  arc-region-switch.ap-northeast-3.api.aws  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  arc-region-switch.ap-northeast-2.api.aws  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  arc-region-switch.ap-southeast-1.api.aws  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  arc-region-switch.ap-southeast-2.api.aws  | HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  arc-region-switch.ap-east-2.api.aws  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  arc-region-switch.ap-southeast-7.api.aws  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  arc-region-switch.ap-northeast-1.api.aws  | HTTPS | 
| Canada (Central) | ca-central-1 |  arc-region-switch.ca-central-1.api.aws  | HTTPS | 
| Canada West (Calgary) | ca-west-1 |  arc-region-switch.ca-west-1.api.aws  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  arc-region-switch.eu-central-1.api.aws  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  arc-region-switch.eu-west-1.api.aws  | HTTPS | 
| Europe (London) | eu-west-2 |  arc-region-switch.eu-west-2.api.aws  | HTTPS | 
| Europe (Milan) | eu-south-1 |  arc-region-switch.eu-south-1.api.aws  | HTTPS | 
| Europe (Paris) | eu-west-3 |  arc-region-switch.eu-west-3.api.aws  | HTTPS | 
| Europe (Spain) | eu-south-2 |  arc-region-switch.eu-south-2.api.aws  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  arc-region-switch.eu-north-1.api.aws  | HTTPS | 
| Europe (Zurich) | eu-central-2 |  arc-region-switch.eu-central-2.api.aws  | HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  arc-region-switch.il-central-1.api.aws  | HTTPS | 
| Mexico (Central) | mx-central-1 |  arc-region-switch.mx-central-1.api.aws  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  arc-region-switch.me-south-1.api.aws  | HTTPS | 
| Middle East (UAE) | me-central-1 |  arc-region-switch.me-central-1.api.aws  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  arc-region-switch.sa-east-1.api.aws  | HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  arc-region-switch.us-gov-east-1.api.aws <br /> arc-region-switch-fips.us-gov-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  arc-region-switch.us-gov-west-1.api.aws <br /> arc-region-switch-control-plane-fips.us-gov-west-1.api.aws <br /> arc-region-switch-fips.us-gov-west-1.api.aws <br /> arc-region-switch-control-plane.us-gov-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 

When you use the AWS CLI or SDKs to submit requests with ARC **Recovery Readiness API** (for readiness checks), **Recovery Control Configuration API** or **Recovery Cluster API** (for routing control), you must specify the AWS Region as `us-west-2`.

For the ARC **Recovery Readiness API** (for readiness checks) or **Recovery Control Configuration API**, use the following endpoints, respectively.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US West (Oregon) Region | us-west-2 | route53-recovery-readiness.amazonaws.com | HTTPS | 
| US West (Oregon) Region | us-west-2 | route53-recovery-control-config.amazonaws.com | HTTPS | 

For the ARC **Recovery Cluster API**, in addition to specifying the Region as `us-west-2`, you also must specify one of your five Regional cluster endpoints. The endpoint that you specify must target the ARC cluster that hosts the routing controls that you want to get or update the state for. 

ARC creates endpoints for each cluster in the following five Regions: US East (N. Virginia) (us-east-1), Europe (Ireland) (eu-west-1), US West (Oregon) (us-west-2), Asia Pacific (Tokyo) (ap-northeast-1), and Asia Pacific (Sydney) (ap-southeast-2). Routing Controls provide five regional endpoints to ensure high availability, even in the face of failures. To achieve their full resilience, it's important to have retry logic that can use all five endpoints as necessary. To learn more, see [Get and update routing control states using the API](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.api.html) and [ Best practices for Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

The following are examples of the Regional cluster endpoints for routing control in ARC.


| Endpoint | Region | 
| --- | --- | 
| https://aaaaaaaa.route53-recovery-cluster.eu-west-1.amazonaws.com | eu-west-1 | 
| https://bbbbbbb.route53-recovery-cluster.ap-northeast-1.amazonaws.com | ap-northeast-1 | 
| https://ccccccc.route53-recovery-cluster.us-west-2.amazonaws.com | us-west-2 | 
| https://ddddddd.route53-recovery-cluster.us-east-1.amazonaws.com | us-east-1 | 
| https://eeeeeee.route53-recovery-cluster.ap-southeast-2.amazonaws.com | ap-southeast-2 | 

## Service quotas
<a name="route53arc-quotas"></a>

For more information, see [Quotas in Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-ar-quotas.html) in the *Amazon Application Recovery Controller (ARC) Developer Guide*.