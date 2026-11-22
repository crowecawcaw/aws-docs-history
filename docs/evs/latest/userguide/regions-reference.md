

# AWS Regions for Amazon EVS

You create an Amazon Elastic VMware Service environment and its hosts in one Region and one Availability Zone, so check the Region before you plan your network.

The authoritative list of Amazon EVS Regions and service endpoints is [Amazon Elastic VMware Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/evs.html) in the * AWS General Reference*. That page is updated when Amazon EVS becomes available in a new Region.

## Regions where Amazon EVS is available
<a name="regions-list"></a>

The following table lists Regions where Amazon EVS is available. The columns show the Region name, the Region code that you use with the AWS CLI and API, and notes that apply to Amazon EVS in that Region.


| Region name | Region code | Notes | 
| --- | --- | --- | 
| US East (N. Virginia) |  `us-east-1`  | None | 
| US East (Ohio) |  `us-east-2`  | None | 
| US West (N. California) |  `us-west-1`  | None | 
| US West (Oregon) |  `us-west-2`  | None | 
| Asia Pacific (Hyderabad) |  `ap-south-2`  | None | 
| Asia Pacific (Malaysia) |  `ap-southeast-5`  | None | 
| Asia Pacific (Mumbai) |  `ap-south-1`  | None | 
| Asia Pacific (Osaka) |  `ap-northeast-3`  | None | 
| Asia Pacific (Seoul) |  `ap-northeast-2`  | None | 
| Asia Pacific (Singapore) |  `ap-southeast-1`  | None | 
| Asia Pacific (Sydney) |  `ap-southeast-2`  | None | 
| Asia Pacific (Taipei) |  `ap-east-2`  | None | 
| Asia Pacific (Tokyo) |  `ap-northeast-1`  | None | 
| Canada (Central) |  `ca-central-1`  | None | 
| Canada West (Calgary) |  `ca-west-1`  | None | 
| Europe (Frankfurt) |  `eu-central-1`  | None | 
| Europe (Ireland) |  `eu-west-1`  | None | 
| Europe (London) |  `eu-west-2`  | None | 
| Europe (Milan) |  `eu-south-1`  | None | 
| Europe (Paris) |  `eu-west-3`  | None | 
| Europe (Spain) |  `eu-south-2`  | None | 
| Europe (Stockholm) |  `eu-north-1`  | None | 
| Europe (Zurich) |  `eu-central-2`  | None | 
| Israel (Tel Aviv) |  `il-central-1`  | None | 
| Mexico (Central) |  `mx-central-1`  | None | 
| South America (São Paulo) |  `sa-east-1`  | None | 

Amazon EVS isn’t available in the AWS GovCloud (US) Regions. If you need Amazon EVS in a Region that isn’t listed, contact your AWS account team.

## Instance types by Region
<a name="regions-instance-types"></a>

For the Amazon EC2 instance types that Amazon EVS supports, see [Supported VCF versions and instance types](versions-provided.md). The r7i instance types are available in every Region where Amazon EVS is available.

To check which instance types and VMware Cloud Foundation (VCF) versions are available to your account in a Region, run `aws evs get-versions` in that Region. For more information, see [Check what is available to you](versions-provided.md#check-provided-versions).