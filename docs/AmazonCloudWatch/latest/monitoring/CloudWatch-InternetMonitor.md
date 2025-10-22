# Supported AWS Regions for Internet Monitor

The AWS Regions and AWS Local Zones where Amazon CloudWatch Internet Monitor is supported are listed in this section. For more information about Regions that 
 Internet Monitor is supported in, including opt-in Regions, see [Amazon CloudWatch Internet Monitor 
 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwim_region.html "https://docs.aws.amazon.com/general/latest/gr/cwim_region.html") in the *Amazon Web Services General Reference*.

Note that Internet Monitor stores data for a monitor in only the AWS Region in which you create the monitor, although a monitor
 can include resources in multiple Regions.



| Region name (Opt-in support) | Region |
| --- | --- |
| Africa (Cape Town) | `af-south-1` |
| Asia Pacific (Hong Kong) | `ap-east-1` |
| Asia Pacific (Hyderabad) | `ap-south-2` |
| Asia Pacific (Jakarta) | `ap-southeast-3` |
| Asia Pacific (Melbourne) | `ap-southeast-4` |
| Europe (Milan) | `eu-south-1` |
| Europe (Spain) | `eu-south-2` |
| Europe (Zurich) | `eu-central-2` |
| Middle East (Bahrain) | `me-south-1` |
| Middle East (UAE) | `me-central-1` |
| Region name (Default support) | Region |
| --- | --- |
| US East (Ohio) | `us-east-2` |
| US East (N. Virginia) | `us-east-1` |
| US West (N. California) | `us-west-1` |
| US West (Oregon) | `us-west-2` |
| Asia Pacific (Mumbai) | `ap-south-1` |
| Asia Pacific (Osaka) | `ap-northeast-3` |
| Asia Pacific (Seoul) | `ap-northeast-2` |
| Asia Pacific (Singapore) | `ap-southeast-1` |
| Asia Pacific (Sydney) | `ap-southeast-2` |
| Asia Pacific (Tokyo) | `ap-northeast-1` |
| Canada (Central) | `ca-central-1` |
| Europe (Frankfurt) | `eu-central-1` |
| Europe (Ireland) | `eu-west-1` |
| Europe (London) | `eu-west-2` |
| Europe (Paris) | `eu-west-3` |
| Europe (Stockholm) | `eu-north-1` |
| South America (São Paulo) | `sa-east-1` | For Local Zones support, you must enable the Local Zone and attach it to the VPC that you want to monitor internet traffic for. Internet Monitor does not support Local Zones for other resources types. The Local Zones that are supported are listed in the following table.
| Local Zone | Parent Region | Type |
| --- | --- | --- |
| `us-east-1-dfw-2a` | `us-east-1` | Availability Zone |
| `us-east-1-mia-2a` | `us-east-1` | Availability Zone |
| `us-east-1-qro-1a` | `us-east-1` | Frontier Zone |
| `us-east-1-lim-1a` | `us-east-1` | Frontier Zone |
| `us-east-1-atl-2a` | `us-east-1` | Availability Zone |
| `us-east-1-bue-1a` | `us-east-1` | Frontier Zone |
| `us-east-1-mci-1a` | `us-east-1` | Frontier Zone |
| `us-west-2-lax-1a` | `us-west-2` | Availability Zone |
| `us-west-2-lax-1b` | `us-west-2` | Availability Zone |
| `af-south-1-los-1a` | `af-south-1` | Frontier Zone |
