

# AWS Regions, websites, IP address ranges, and endpoints
<a name="regions"></a>

AWS cloud-computing resources are housed in highly available facilities in different areas of the world (for example, North America, Europe, and Asia). These facilities are each part of an AWS Region. For more information about AWS Regions and Availability Zones (AZs), see [Global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

The IP addresses listed in the sections below are the ranges where Amazon Quick traffic originates from when making outbound connections to databases. They are not the IP address ranges that you use to connect to the Amazon Quick website or service API. For more information about authorizing Amazon Quick, [Authorizing connections to AWS data sources](https://docs.aws.amazon.com/quicksight/latest/user/enabling-access.html).

**Topics**
+ [Supported AWS Regions for Amazon Quick](#regions-qs)
+ [Cross-Region calls for web search](#web-search-cross-region)
+ [Cross-Region inference for Australia, Japan, Europe, and the United States](#cross-region-inference)
+ [AWS Regions for Amazon Q in Quick](#regions-q-in-quick)

## Supported AWS Regions for Amazon Quick
<a name="regions-qs"></a>

Amazon Quick is currently supported in the following AWS Regions. The following list provides websites, IP address ranges, and endpoints for Amazon Quick in each AWS Region. 



| Region name | Region code | Agentic Features | Website for user access | API endpoints (HTTPS) | IP address range for data source connectivity | 
| --- | --- | --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 | No |  https://us-east-2.quicksight.aws.amazon.com  |  quicksight.us-east-2.amazonaws.com  | 52.15.247.160/27 | 
| US East (N. Virginia) | us-east-1 | Yes |  https://us-east-1.quicksight.aws.amazon.com  |  quicksight.us-east-1.amazonaws.com  | 52.23.63.224/27 | 
| US West (Oregon) | us-west-2 | Yes |  https://us-west-2.quicksight.aws.amazon.com  |  quicksight.us-west-2.amazonaws.com  | 54.70.204.128/27 | 
| Africa (Cape Town) | af-south-1 | No |  https://af-south-1.quicksight.aws.amazon.com  |  quicksight.af-south-1.amazonaws.com  | 13.246.220.192/27 | 
| Asia Pacific (Jakarta) | ap-southeast-3 | No |  https://ap-southeast-3.quicksight.aws.amazon.com  |  quicksight.ap-southeast-3.amazonaws.com  | 43.218.71.192/27 | 
| Asia Pacific (Malaysia) | ap-southeast-5 | No |  https://ap-southeast-5.quicksight.aws.amazon.com  |  quicksight.ap-southeast-5.amazonaws.com  | 56.68.33.0/27 | 
| Asia Pacific (Mumbai) | ap-south-1 | No |  https://ap-south-1.quicksight.aws.amazon.com  |  quicksight.ap-south-1.amazonaws.com  | 52.66.193.64/27 | 
| Asia Pacific (Seoul) | ap-northeast-2 | No |  https://ap-northeast-2.quicksight.aws.amazon.com  |  quicksight.ap-northeast-2.amazonaws.com  | 13.124.145.32/27 | 
| Asia Pacific (Singapore) | ap-southeast-1 | No |  https://ap-southeast-1.quicksight.aws.amazon.com  |  quicksight.ap-southeast-1.amazonaws.com  | 13.229.254.0/27 | 
| Asia Pacific (Sydney) | ap-southeast-2 | Yes |  https://ap-southeast-2.quicksight.aws.amazon.com  |  quicksight.ap-southeast-2.amazonaws.com  | 54.153.249.96/27 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | Yes |  https://ap-northeast-1.quicksight.aws.amazon.com  |  quicksight.ap-northeast-1.amazonaws.com  | 13.113.244.32/27 | 
| Canada (Central) | ca-central-1 | No |  https://ca-central-1.quicksight.aws.amazon.com  |  quicksight.ca-central-1.amazonaws.com  | 15.223.73.0/27 | 
| China (Beijing) | cn-north-1 | No |  https://cn-north-1.quicksight.amazonaws.cn  |  quicksight.cn-north-1.amazonaws.com.cn  | 71.136.65.64/27 | 
| Europe (Frankfurt) | eu-central-1 | Yes |  https://eu-central-1.quicksight.aws.amazon.com  |  quicksight.eu-central-1.amazonaws.com  | 35.158.127.192/27 | 
| Europe (Ireland) | eu-west-1 | Yes |  https://eu-west-1.quicksight.aws.amazon.com  |  quicksight.eu-west-1.amazonaws.com  | 52.210.255.224/27 | 
| Europe (London) | eu-west-2 | Yes |  https://eu-west-2.quicksight.aws.amazon.com  |  quicksight.eu-west-2.amazonaws.com  | 35.177.218.0/27 | 
| Europe (Milan) | eu-south-1 | No |  https://eu-south-1.quicksight.aws.amazon.com  |  quicksight.eu-south-1.amazonaws.com  | 18.102.150.128/27 | 
| Europe (Paris) | eu-west-3 | No |  https://eu-west-3.quicksight.aws.amazon.com  |  quicksight.eu-west-3.amazonaws.com  | 13.38.202.0/27 | 
| Europe (Spain) | eu-south-2 | No |  https://eu-south-2.quicksight.aws.amazon.com  |  quicksight.eu-south-2.amazonaws.com  | 18.101.99.160/27 | 
| Europe (Stockholm) | eu-north-1 | No |  https://eu-north-1.quicksight.aws.amazon.com  |  quicksight.eu-north-1.amazonaws.com  | 13.53.191.64/27 | 
| Europe (Zurich) | eu-central-2 | No |  https://eu-central-2.quicksight.aws.amazon.com  |  quicksight.eu-central-2.amazonaws.com  | 16.63.53.32/27 | 
| South America (São Paulo) | sa-east-1 | No |  https://sa-east-1.quicksight.aws.amazon.com  |  quicksight.sa-east-1.amazonaws.com  | 18.230.46.192/27 | 
| AWS GovCloud (US-East) | gov-east-1 | No |  https://quicksight.us-gov-east-1.amazonaws.com  |  quicksight.us-gov-east-1.amazonaws.com  | 18.252.165.64/27 | 
| AWS GovCloud (US-West) | gov-west-1 | Yes |  https://quicksight.us-gov-west-1.amazonaws.com  |  quicksight.us-gov-west-1.amazonaws.com  | 160.1.180.32/27 | 
| Israel (Tel Aviv) | il-central-1 | No |  https://il-central-1.quicksight.aws.amazon.com  |  quicksight.il-central-1.amazonaws.com  | 51.17.195.32/27 | 
| Middle East (UAE) | me-central-1 | No |  https://me-central-1.quicksight.aws.amazon.com  |  quicksight.me-central-1.amazonaws.com  | 51.112.11.224/27 | 

If your IAM Identity Center instance is replicated to multiple Regions, you can create your Quick Enterprise subscription in an active additional Region. For more information, see [Set up Amazon Quick with IAM Identity Center multi-Region](setting-up-sso.md#idc-multi-region).

## Cross-Region calls for web search
<a name="web-search-cross-region"></a>

Amazon Quick makes cross-Region calls for web search functionality in Chat, Agents, and Research features. When using web search, requests originating in US West (Oregon) are processed in the US East (N. Virginia) Region. For customers in EMEA Regions, web search queries are processed in the Europe (Ireland) Region.

### Web search regional availability
<a name="web-search-regional-availability"></a>


| Region name and code | Web search processing region | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | US East (N. Virginia) (us-east-1) | 
| US West (Oregon) (us-west-2) | US East (N. Virginia) (us-east-1) | 
| Europe (Ireland) (eu-west-1) | Europe (Ireland) (eu-west-1) | 
| Europe (Frankfurt) (eu-central-1) | Europe (Ireland) (eu-west-1) | 
| Europe (London) (eu-west-2) | Europe (Ireland) (eu-west-1) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Asia Pacific (Tokyo) (ap-northeast-1) | 

## Cross-Region inference for Australia, Japan, Europe, and the United States
<a name="cross-region-inference"></a>

With cross-Region inference, Amazon Quick automatically selects the optimal Region within your geography to process your inference request. This approach maximizes available compute resources and model availability. With cross-Region inference, you get:
+ Complete access to the most advanced Amazon Quick AI capabilities and features
+ Access to a variety of models suitable for different tasks
+ Improved performance for all your applications

Cross-Region inference requests stay within the AWS Regions in the geography where your data originally resides. For example, a request made in the US stays within the AWS Regions in the US. Although data is stored only in your primary Region, your input prompts and output results might move outside of that Region when you use cross-Region inference. Amazon transmits all data encrypted across its secure network.

**Note**  
There is no additional cost for using cross-Region inference.  
Amazon CloudWatch and AWS CloudTrail logs do not specify the AWS Region in which data inference occurs.

### Supported Regions for cross-Region inference
<a name="cross-region-inference-supported-regions"></a>

For a list of Region codes and endpoints supported in Amazon Quick AI capabilities and features, see [Supported AWS Regions for Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/regions-aqs.html).

The following table summarizes the supported geographies and their inference Regions for Amazon Quick cross-Region inference.


| Supported Amazon Quick geography | Inference Regions | 
| --- | --- | 
| United States | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Europe | Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (London) (eu-west-2) | 
| Australia | Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Japan | Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Osaka) (ap-northeast-3) | 

## AWS Regions for Amazon Q in Quick
<a name="regions-q-in-quick"></a>

**Topics**
+ [Supported AWS Regions for Amazon Q in Quick](#regions-aqs)

### Supported AWS Regions for Amazon Q in Quick
<a name="regions-aqs"></a>

Amazon Q in Quick Generative BI features including scenarios are currently supported in the following AWS Regions:


| Region | Scenarios | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | ✓ Yes | 
| US East (Ohio) (us-east-2) | ✓ Yes | 
| US West (Oregon) (us-west-2) | ✓ Yes | 
| Asia Pacific (Mumbai) (ap-south-1) | ✓ Yes | 
| Asia Pacific (Seoul) (ap-northeast-2) | ✓ Yes | 
| Asia Pacific (Singapore) (ap-southeast-1) | ✓ Yes | 
| Asia Pacific (Tokyo) (ap-northeast-1) | ✓ Yes | 
| Asia Pacific (Sydney) (ap-southeast-2) | ✓ Yes | 
| Canada (Central) (ca-central-1) | Not Available | 
| Europe (Frankfurt) (eu-central-1) | ✓ Yes | 
| Europe (Ireland) (eu-west-1) | ✓ Yes | 
| Europe (London) (eu-west-2) | ✓ Yes | 
| Europe (Paris) (eu-west-3) | ✓ Yes | 
| Europe (Stockholm) (eu-north-1) | Not Available | 
| Europe (Zurich) (eu-central-2) | Not Available | 
| South America (São Paulo) (sa-east-1) | Not Available | 

The following table shows the detailed per-Region inference routing.


| Supported Amazon Q in Quick geography | Inferenced regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) |  +  US East (N. Virginia) (us-east-1) <br />+  US East (Ohio) (us-east-2) <br />+  US West (Oregon) (us-west-2)   | 
| US East (Ohio) (us-east-2) |  +  US East (N. Virginia) (us-east-1) <br />+  US East (Ohio) (us-east-2) <br />+  US West (Oregon) (us-west-2)   | 
| US West (Oregon) (us-west-2) |  +  US East (N. Virginia) (us-east-1) <br />+  US East (Ohio) (us-east-2) <br />+  US West (Oregon) (us-west-2)   | 
| Asia Pacific (Mumbai) (ap-south-1) |  +  Asia Pacific (Tokyo) (ap-northeast-1) <br />+  Asia Pacific (Seoul) (ap-northeast-2) <br />+  Asia Pacific (Mumbai) (ap-south-1) <br />+  Asia Pacific (Singapore) (ap-southeast-1) <br />+  Asia Pacific (Sydney) (ap-southeast-2) <br />+  Asia Pacific (Osaka) (ap-northeast-3)\* <br />+  Asia Pacific (Hyderabad) (ap-south-2)\*   | 
| Asia Pacific (Seoul) (ap-northeast-2) |  +  Asia Pacific (Tokyo) (ap-northeast-1) <br />+  Asia Pacific (Seoul) (ap-northeast-2) <br />+  Asia Pacific (Mumbai) (ap-south-1) <br />+  Asia Pacific (Singapore) (ap-southeast-1) <br />+  Asia Pacific (Sydney) (ap-southeast-2) <br />+  Asia Pacific (Osaka) (ap-northeast-3)\* <br />+  Asia Pacific (Hyderabad) (ap-south-2)\*   | 
| Asia Pacific (Singapore) (ap-southeast-1) |  +  Asia Pacific (Tokyo) (ap-northeast-1) <br />+  Asia Pacific (Seoul) (ap-northeast-2) <br />+  Asia Pacific (Mumbai) (ap-south-1) <br />+  Asia Pacific (Singapore) (ap-southeast-1) <br />+  Asia Pacific (Sydney) (ap-southeast-2) <br />+  Asia Pacific (Osaka) (ap-northeast-3)\* <br />+  Asia Pacific (Hyderabad) (ap-south-2)\*   | 
| Asia Pacific (Tokyo) (ap-northeast-1) |  +  Asia Pacific (Tokyo) (ap-northeast-1) <br />+  Asia Pacific (Osaka) (ap-northeast-3)   | 
| Asia Pacific (Sydney) (ap-southeast-2) |  +  Asia Pacific (Sydney) (ap-southeast-2) <br />+  Asia Pacific (Melbourne) (ap-southeast-4)   | 
| Europe (Frankfurt) (eu-central-1) |  +  Europe (Frankfurt) (eu-central-1) <br />+  Europe (Stockholm) (eu-north-1) <br />+  Europe (Ireland) (eu-west-1) <br />+  Europe (London) (eu-west-2) <br />+  Europe (Paris) (eu-west-3)   | 
| Europe (Ireland) (eu-west-1) |  +  Europe (Frankfurt) (eu-central-1) <br />+  Europe (Stockholm) (eu-north-1) <br />+  Europe (Ireland) (eu-west-1) <br />+  Europe (London) (eu-west-2) <br />+  Europe (Paris) (eu-west-3)   | 
| Europe (London) (eu-west-2) |  +  Europe (Frankfurt) (eu-central-1) <br />+  Europe (Stockholm) (eu-north-1) <br />+  Europe (Ireland) (eu-west-1) <br />+  Europe (London) (eu-west-2) <br />+  Europe (Paris) (eu-west-3)   | 
| Europe (Paris) (eu-west-3) |  +  Europe (Frankfurt) (eu-central-1) <br />+  Europe (Stockholm) (eu-north-1) <br />+  Europe (Ireland) (eu-west-1) <br />+  Europe (London) (eu-west-2) <br />+  Europe (Paris) (eu-west-3)   | 
| Europe (Stockholm) (eu-north-1) |  +  Europe (Frankfurt) (eu-central-1) <br />+  Europe (Stockholm) (eu-north-1) <br />+  Europe (Ireland) (eu-west-1) <br />+  Europe (London) (eu-west-2) <br />+  Europe (Paris) (eu-west-3)   | 

**Note**  
Service is not yet launched in these marked regions (\*), but inference may still occur.