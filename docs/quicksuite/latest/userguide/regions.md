# AWS Regions, websites, IP address ranges, and endpoints

AWS cloud-computing resources are housed in highly available facilities in different
areas of the world (for example, North America, Europe, and Asia). These facilities are each
part of an AWS Region. For more information about AWS Regions and Availability Zones
(AZs), see [Global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

The IP addresses listed in the sections below are the ranges where Amazon Quick Suite traffic
originates from when making outbound connections to databases. They are not the IP address
ranges that you use to connect to the Amazon Quick Suite website or service API. For more
information about authorizing Amazon Quick Suite, [Authorizing
connections to AWS data sources](../../../quicksight/latest/user/enabling-access.md "../../../quicksight/latest/user/enabling-access.md").

###### Topics

- [Supported AWS Regions for Amazon Quick Suite](#regions-qs "#regions-qs")
- [Supported AWS Regions for Amazon Q in Quick Suite](#regions-aqs "#regions-aqs")
- [Cross-Region inference with Amazon Q in Quick Suite](#q-cross-region-inferencing "#q-cross-region-inferencing")
- [Cross-Region calls for web search](#web-search-cross-region "#web-search-cross-region")

## Supported AWS Regions for Amazon Quick Suite

Amazon Quick Suite is currently supported in the following AWS Regions. The following list
provides websites, IP address ranges, and endpoints for Amazon Quick Suite in each
AWS Region.

###### Note

\*Only Quick Sight features are supported in these regions.

| Region name                 | Region code    | Website for user access                            | API endpoints (HTTPS)                     | IP address range for data source connectivity |
| --------------------------- | -------------- | -------------------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| US East (Ohio)\*            | us-east-2      | `https://us-east-2.quicksight.aws.amazon.com`      | `quicksight.us-east-2.amazonaws.com`      | 52.15.247.160/27                              |
| US East (N. Virginia)       | us-east-1      | `https://us-east-1.quicksight.aws.amazon.com`      | `quicksight.us-east-1.amazonaws.com`      | 52.23.63.224/27                               |
| US West (Oregon)            | us-west-2      | `https://us-west-2.quicksight.aws.amazon.com`      | `quicksight.us-west-2.amazonaws.com`      | 54.70.204.128/27                              |
| Africa (Cape Town)\*        | af-south-1     | `https://af-south-1.quicksight.aws.amazon.com`     | `quicksight.af-south-1.amazonaws.com`     | 13.246.220.192/27                             |
| Asia Pacific (Jakarta)\*    | ap-southeast-3 | `https://ap-southeast-3.quicksight.aws.amazon.com` | `quicksight.ap-southeast-3.amazonaws.com` | 43.218.71.192/27                              |
| Asia Pacific (Mumbai)\*     | ap-south-1     | `https://ap-south-1.quicksight.aws.amazon.com`     | `quicksight.ap-south-1.amazonaws.com`     | 52.66.193.64/27                               |
| Asia Pacific (Seoul)\*      | ap-northeast-2 | `https://ap-northeast-2.quicksight.aws.amazon.com` | `quicksight.ap-northeast-2.amazonaws.com` | 13.124.145.32/27                              |
| Asia Pacific (Singapore)\*  | ap-southeast-1 | `https://ap-southeast-1.quicksight.aws.amazon.com` | `quicksight.ap-southeast-1.amazonaws.com` | 13.229.254.0/27                               |
| Asia Pacific (Sydney)       | ap-southeast-2 | `https://ap-southeast-2.quicksight.aws.amazon.com` | `quicksight.ap-southeast-2.amazonaws.com` | 54.153.249.96/27                              |
| Asia Pacific (Tokyo)\*      | ap-northeast-1 | `https://ap-northeast-1.quicksight.aws.amazon.com` | `quicksight.ap-northeast-1.amazonaws.com` | 13.113.244.32/27                              |
| Canada (Central)\*          | ca-central-1   | `https://ca-central-1.quicksight.aws.amazon.com`   | `quicksight.ca-central-1.amazonaws.com`   | 15.223.73.0/27                                |
| China (Beijing)\*           | cn-north-1     | `https://cn-north-1.quicksight.amazonaws.cn`       | `quicksight.cn-north-1.amazonaws.com.cn`  | 71.136.65.64/27                               |
| Europe (Frankfurt)\*        | eu-central-1   | `https://eu-central-1.quicksight.aws.amazon.com`   | `quicksight.eu-central-1.amazonaws.com`   | 35.158.127.192/27                             |
| Europe (Ireland)            | eu-west-1      | `https://eu-west-1.quicksight.aws.amazon.com`      | `quicksight.eu-west-1.amazonaws.com`      | 52.210.255.224/27                             |
| Europe (London)\*           | eu-west-2      | `https://eu-west-2.quicksight.aws.amazon.com`      | `quicksight.eu-west-2.amazonaws.com`      | 35.177.218.0/27                               |
| Europe (Milan)\*            | eu-south-1     | `https://eu-south-1.quicksight.aws.amazon.com`     | `quicksight.eu-south-1.amazonaws.com`     | 18.102.150.128/27                             |
| Europe (Paris)\*            | eu-west-3      | `https://eu-west-3.quicksight.aws.amazon.com`      | `quicksight.eu-west-3.amazonaws.com`      | 13.38.202.0/27                                |
| Europe (Spain)\*            | eu-south-2     | `https://eu-south-2.quicksight.aws.amazon.com`     | `quicksight.eu-south-2.amazonaws.com`     | 18.101.99.160/27                              |
| Europe (Stockholm)\*        | eu-north-1     | `https://eu-north-1.quicksight.aws.amazon.com`     | `quicksight.eu-north-1.amazonaws.com`     | 13.53.191.64/27                               |
| Europe (Zurich)\*           | eu-central-2   | `https://eu-central-2.quicksight.aws.amazon.com`   | `quicksight.eu-central-2.amazonaws.com`   | 16.63.53.32/27                                |
| South America (São Paulo)\* | sa-east-1      | `https://sa-east-1.quicksight.aws.amazon.com`      | `quicksight.sa-east-1.amazonaws.com`      | 18.230.46.192/27                              |
| AWS GovCloud (US-West)\*    | gov-west-1     | `quicksight.us-gov-west-1.amazonaws.com`           | `quicksight.us-gov-west-1.amazonaws.com`  | 160.1.180.32/27                               |
| Israel (Tel Aviv)\*         | il-central-1   | `https://il-central-1.quicksight.aws.amazon.com`   | `quicksight.il-central-1.amazonaws.com`   | 51.17.195.32/27                               |
| Middle East (UAE)\*         | me-central-1   | `https://me-central-1.quicksight.aws.amazon.com`   | `quicksight.me-central-1.amazonaws.com`   | 51.112.11.224/27                              |

## Supported AWS Regions for Amazon Q in Quick Suite

Amazon Q in Quick Suite Generative BI features including scenarios are currently supported in the
following AWS Regions:

| Region                                    | Scenarios     |
| ----------------------------------------- | ------------- |
| US East (N. Virginia) (us-east-1)         | ✓             |
| US East (Ohio) (us-east-2)                | ✓             |
| US West (Oregon) (us-west-2)              | ✓             |
| Asia Pacific (Mumbai) (ap-south-1)        | ✓             |
| Asia Pacific (Seoul) (ap-northeast-2)     | ✓             |
| Asia Pacific (Singapore) (ap-southeast-1) | ✓             |
| Asia Pacific (Tokyo) (ap-northeast-1)     | ✓             |
| Asia Pacific (Sydney) (ap-southeast-2)    | ✓             |
| Canada (Central) (ca-central-1)           | Not Available |
| Europe (Frankfurt) (eu-central-1)         | ✓             |
| Europe (Ireland) (eu-west-1)              | ✓             |
| Europe (London) (eu-west-2)               | ✓             |
| Europe (Paris) (eu-west-3)                | ✓             |
| Europe (Stockholm) (eu-north-1)           | Not Available |
| Europe (Zurich) (eu-central-2)            | Not Available |
| South America (São Paulo) (sa-east-1)     | Not Available |

For a list of region codes and endpoints for Quick Suite and Q in Quick Suite features,
see [Supported AWS Regions for Amazon Quick Suite](#regions-qs "#regions-qs").

## Cross-Region inference with Amazon Q in Quick Suite

With cross-Region inference, Amazon Q in Quick Suite will automatically select the optimal Region within
your geography (as described in more detail below) to process your inference request,
maximizing available compute resources and model availability, and providing the best
customer experience. With cross-Region inference, you get:

- Complete access to most advanced Amazon Q in Quick Suite AI capabilities and features
- Access to a variety of models suitable for different tasks
- Improved performance for all your applications

Cross-Region inference requests are kept within the AWS Regions that are part of the
geography where the data originally resides. For example, a request made within the US
is kept within the AWS Regions in the US. Although the data remains stored only in the
primary Region, when using cross-Region inference, your input prompts and output results
may move outside of your primary Region. All data will be transmitted encrypted across
Amazon's secure network.

###### Note

There's no additional cost for using cross-Region inference.

Amazon CloudWatch and AWS CloudTrail logs won't specify the AWS
Region in which data inference occurs.

### Supported regions for

Amazon Q in Quick Suite cross-Region inference

For a list of Region codes and endpoints supported in Amazon Q in Quick Suite, see [Supported
AWS regions for Amazon Quick Suite](../../../quicksight/latest/user/regions-aqs.md "../../../quicksight/latest/user/regions-aqs.md").

| Supported Amazon Q in Quick Suite geography | Inferenced regions                                                                                                                                                                                                                                                                                              |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia) (us-east-1)           | • US East (N. Virginia) (us-east-1)<br>• US East (Ohio) (us-east-2)<br>• US West (Oregon) (us-west-2)                                                                                                                                                                                                           |
| US East (Ohio) (us-east-2)                  | • US East (N. Virginia) (us-east-1)<br>• US East (Ohio) (us-east-2)<br>• US West (Oregon) (us-west-2)                                                                                                                                                                                                           |
| US West (Oregon) (us-west-2)                | • US East (N. Virginia) (us-east-1)<br>• US East (Ohio) (us-east-2)<br>• US West (Oregon) (us-west-2)                                                                                                                                                                                                           |
| Asia Pacific (Mumbai) (ap-south-1)          | • Asia Pacific (Tokyo) (ap-northeast-1)<br>• Asia Pacific (Seoul) (ap-northeast-2)<br>• Asia Pacific (Mumbai) (ap-south-1)<br>• Asia Pacific (Singapore) (ap-southeast-1)<br>• Asia Pacific (Sydney) (ap-southeast-2)<br>• Asia Pacific (Osaka) (ap-northeast-3)\*<br>• Asia Pacific (Hyderabad) (ap-south-2)\* |
| Asia Pacific (Seoul) (ap-northeast-2)       | • Asia Pacific (Tokyo) (ap-northeast-1)<br>• Asia Pacific (Seoul) (ap-northeast-2)<br>• Asia Pacific (Mumbai) (ap-south-1)<br>• Asia Pacific (Singapore) (ap-southeast-1)<br>• Asia Pacific (Sydney) (ap-southeast-2)<br>• Asia Pacific (Osaka) (ap-northeast-3)\*<br>• Asia Pacific (Hyderabad) (ap-south-2)\* |
| Asia Pacific (Singapore) (ap-southeast-1)   | • Asia Pacific (Tokyo) (ap-northeast-1)<br>• Asia Pacific (Seoul) (ap-northeast-2)<br>• Asia Pacific (Mumbai) (ap-south-1)<br>• Asia Pacific (Singapore) (ap-southeast-1)<br>• Asia Pacific (Sydney) (ap-southeast-2)<br>• Asia Pacific (Osaka) (ap-northeast-3)\*<br>• Asia Pacific (Hyderabad) (ap-south-2)\* |
| Asia Pacific (Tokyo) (ap-northeast-1)       | • Asia Pacific (Tokyo) (ap-northeast-1)<br>• Asia Pacific (Seoul) (ap-northeast-2)<br>• Asia Pacific (Mumbai) (ap-south-1)<br>• Asia Pacific (Singapore) (ap-southeast-1)<br>• Asia Pacific (Sydney) (ap-southeast-2)<br>• Asia Pacific (Osaka) (ap-northeast-3)\*<br>• Asia Pacific (Hyderabad) (ap-south-2)\* |
| Asia Pacific (Sydney) (ap-southeast-2)      | • Asia Pacific (Tokyo) (ap-northeast-1)<br>• Asia Pacific (Seoul) (ap-northeast-2)<br>• Asia Pacific (Mumbai) (ap-south-1)<br>• Asia Pacific (Singapore) (ap-southeast-1)<br>• Asia Pacific (Sydney) (ap-southeast-2)<br>• Asia Pacific (Osaka) (ap-northeast-3)\*<br>• Asia Pacific (Hyderabad) (ap-south-2)\* |
| Europe (Frankfurt) (eu-central-1)           | • Europe (Frankfurt) (eu-central-1)<br>• Europe (Stockholm) (eu-north-1)<br>• Europe (Ireland) (eu-west-1)<br>• Europe (Paris) (eu-west-3)                                                                                                                                                                      |
| Europe (Ireland) (eu-west-1)                | • Europe (Frankfurt) (eu-central-1)<br>• Europe (Stockholm) (eu-north-1)<br>• Europe (Ireland) (eu-west-1)<br>• Europe (Paris) (eu-west-3)                                                                                                                                                                      |
| Europe (Paris) (eu-west-3)                  | • Europe (Frankfurt) (eu-central-1)<br>• Europe (Stockholm) (eu-north-1)<br>• Europe (Ireland) (eu-west-1)<br>• Europe (Paris) (eu-west-3)                                                                                                                                                                      |
| Europe (Stockholm) (eu-north-1)             | • Europe (Frankfurt) (eu-central-1)<br>• Europe (Stockholm) (eu-north-1)<br>• Europe (Ireland) (eu-west-1)<br>• Europe (Paris) (eu-west-3)                                                                                                                                                                      |

###### Note

Service is not yet launched in these marked regions (\*), but inference may
still occur.

## Cross-Region calls for web search

Amazon Quick Suite makes cross-Region calls for web search functionality in Chat, Agents, and Research features. Cross-Region calls are API calls made by Amazon Quick Suite from one AWS Region to another AWS Region.

###### Note

Cross-Region calls for web search apply to Chat, Agents, and Research features that include web search capabilities.

### Web search regional availability

Amazon Quick Suite web search capability is securely hosted in the US East (N. Virginia) AWS Region. While Amazon Quick Suite is available in multiple regions, all web search queries are processed through the web search service in the US East region.

| Region name and code                   | Web search processing region      |
| -------------------------------------- | --------------------------------- |
| US East (N. Virginia) (us-east-1)      | US East (N. Virginia) (us-east-1) |
| US West (Oregon) (us-west-2)           | US East (N. Virginia) (us-east-1) |
| Europe (Ireland) (eu-west-1)           | US East (N. Virginia) (us-east-1) |
| Asia Pacific (Sydney) (ap-southeast-2) | US East (N. Virginia) (us-east-1) |
