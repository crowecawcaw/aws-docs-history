

# Amazon WorkSpaces endpoints and quotas
<a name="wsp"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="wsp_region"></a>

**Note**  
The AWS Regions in the following table apply to WorkSpaces personal. For the AWS Regions that apply to WorkSpaces pools, see [AWS Regions for WorkSpaces pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-regions.html) in the *Amazon WorkSpaces Administration Guide*. The endpoints are the same for both versions of the WorkSpaces service.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  workspaces.us-east-2.amazonaws.com <br /> workspaces-fips.us-east-2.api.aws <br /> workspaces-fips.us-east-2.amazonaws.com <br /> workspaces.us-east-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  workspaces.us-east-1.amazonaws.com <br /> workspaces-fips.us-east-1.api.aws <br /> workspaces-fips.us-east-1.amazonaws.com <br /> workspaces.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  workspaces.us-west-2.amazonaws.com <br /> workspaces-fips.us-west-2.api.aws <br /> workspaces-fips.us-west-2.amazonaws.com <br /> workspaces.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  workspaces.af-south-1.amazonaws.com <br /> workspaces.af-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  workspaces.ap-southeast-5.amazonaws.com <br /> workspaces.ap-southeast-5.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  workspaces.ap-south-1.amazonaws.com <br /> workspaces.ap-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  workspaces.ap-northeast-2.amazonaws.com <br /> workspaces.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  workspaces.ap-southeast-1.amazonaws.com <br /> workspaces.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  workspaces.ap-southeast-2.amazonaws.com <br /> workspaces.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  workspaces.ap-northeast-1.amazonaws.com <br /> workspaces.ap-northeast-1.api.aws  | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  workspaces.ca-central-1.amazonaws.com <br /> workspaces.ca-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  workspaces.eu-central-1.amazonaws.com <br /> workspaces.eu-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  workspaces.eu-west-1.amazonaws.com <br /> workspaces.eu-west-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  workspaces.eu-west-2.amazonaws.com <br /> workspaces.eu-west-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Paris) | eu-west-3 |  workspaces.eu-west-3.amazonaws.com <br /> workspaces.eu-west-3.api.aws  | HTTPS<br />HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  workspaces.il-central-1.amazonaws.com <br /> workspaces.il-central-1.api.aws  | HTTPS<br />HTTPS | 
| South America (São Paulo) | sa-east-1 |  workspaces.sa-east-1.amazonaws.com <br /> workspaces.sa-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  workspaces.us-gov-east-1.amazonaws.com <br /> workspaces-fips.us-gov-east-1.api.aws <br /> workspaces-fips.us-gov-east-1.amazonaws.com <br /> workspaces.us-gov-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  workspaces.us-gov-west-1.amazonaws.com <br /> workspaces-fips.us-gov-west-1.api.aws <br /> workspaces-fips.us-gov-west-1.amazonaws.com <br /> workspaces.us-gov-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 

## Service quotas
<a name="limits_workspaces"></a>


| Resource | Default | Description | Adjustable | 
| --- | --- | --- | --- | 
| WorkSpaces | 1 | The maximum number of WorkSpaces in this account in the current Region. | Yes | 
| Graphics WorkSpaces | 0 | The maximum number of Graphics WorkSpaces in this account in the current Region. Graphics bundle is no longer supported after November 30, 2023. We recommend migrating your WorkSpaces to Graphics.g4dn bundle. For more information, see [Migrate a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/migrate-workspaces.html) in the *WorkSpaces Administration Guide*.  | Yes | 
| GraphicsPro WorkSpaces | 0 | The maximum number of GraphicsPro WorkSpaces in this account in the current Region. | Yes | 
| Images | 40 | The maximum number of images in this account in the current Region. | Yes | 
| Bundles | 50 | The maximum number of bundles in this account in the current Region. This quota applies only to custom bundles, not to public bundles. | No | 
| Connection aliases | 20 | The maximum number of connection aliases in this account in the current Region. | No | 
| Directories | 50 | The maximum number of directories that can be registered for use with Amazon WorkSpaces in this account in the current Region. | No | 
| IP access control groups | 100 | The maximum number of IP access control groups in this account in the current Region. | No | 
| Rules per IP access control group | 10 | The maximum number of rules per IP access control group in this account in the current Region. | No | 
| IP access control groups per directory | 25 | The maximum number of IP access control groups per directory in this account in the current Region. | No | 
| WorkSpaces Pools | 10 | The maximum number of WorkSpaces Pools in this account in the current Region. | Yes | 
| General Purpose Value streaming instances for WorkSpaces Pools | 10 | The maximum number of General Purpose Value streaming instances that can be used for WorkSpaces Pools in this account in the current Region. | Yes | 
| General Purpose Standard streaming instances for WorkSpaces Pools | 10 | The maximum number of General Purpose Standard instances that can be used for WorkSpaces Pools in this account in the current Region.  | Yes | 
| General Purpose Performance streaming instances for WorkSpaces Pools | 10 | The maximum number of General Purpose Performance streaming instances that can be used for WorkSpaces Pools in this account in the current Region. | Yes | 
| General Purpose Power streaming instances for WorkSpaces Pools" | 10 | The maximum number of General Purpose Power streaming instances that can be used for WorkSpaces Pools in this account in the current Region. | Yes | 
| General Purpose PowerPro streaming instances for WorkSpaces Pools"  | 10 | The maximum number of General Purpose PowerPro streaming instances that can be used for WorkSpaces Pools in this account in the current Region. | Yes | 
| Graphics.g4dn xlarge streaming instances for WorkSpaces Pools | 0 | The maximum number of Graphics.g4dn xlarge streaming instances that can be used for WorkSpaces Pools in this account in the current Region. | No | 
| Graphics.g4dn 4xlarge streaming instances for WorkSpaces Pools | 0 | The maximum number of Graphics.g4dn 4xlarge streaming instances that can be used for WorkSpaces Pools in this account in the current Region. | No | 