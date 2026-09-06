

# AWS STS Regions and endpoints
<a name="id_credentials_temp_region-endpoints"></a>

**Note**  
AWS has made changes to the AWS Security Token Service (AWS STS) global endpoint (`https://sts.amazonaws.com`) in Regions [enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) to enhance its resiliency and performance. AWS STS requests to the global endpoint are automatically served in the same AWS Region as your workloads. These changes will not be deployed to opt-in Regions. We recommend that you use the appropriate AWS STS regional endpoints. For more information, see [AWS STS global endpoint changes](#reference_sts_global_endpoint_changes).

The following table lists the Regions and their endpoints. It indicates which ones are activated by default and which ones you can activate or deactivate.


| Region name | Endpoint | Active by default | Manually activate/deactivate | 
| --- | --- | --- | --- | 
| --Global-- | sts.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| US East (Ohio) | sts.us-east-2.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| US East (N. Virginia) | sts.us-east-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| US West (N. California) | sts.us-west-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| US West (Oregon) | sts.us-west-2.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Africa (Cape Town) | sts.af-south-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Asia Pacific (Hong Kong) | sts.ap-east-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Asia Pacific (Hyderabad) | sts.ap-south-2.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Asia Pacific (Jakarta) | sts.ap-southeast-3.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Asia Pacific (Malaysia) | sts.ap-southeast-5.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Asia Pacific (Melbourne) | sts.ap-southeast-4.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Asia Pacific (Mumbai) | sts.ap-south-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Asia Pacific (Osaka) | sts.ap-northeast-3.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Asia Pacific (Seoul) | sts.ap-northeast-2.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Asia Pacific (Singapore) | sts.ap-southeast-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Asia Pacific (Sydney) | sts.ap-southeast-2.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Asia Pacific (Thailand) | sts.ap-southeast-7.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Asia Pacific (Tokyo) | sts.ap-northeast-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Canada (Central) | sts.ca-central-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Canada West (Calgary) | sts.ca-west-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| China (Beijing) | sts.cn-north-1.amazonaws.com.cn | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes² | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| China (Ningxia) | sts.cn-northwest-1.amazonaws.com.cn | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes² | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Europe (Frankfurt) | sts.eu-central-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Europe (Ireland) | sts.eu-west-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Europe (London) | sts.eu-west-2.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Europe (Milan) | sts.eu-south-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Europe (Paris) | sts.eu-west-3.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Europe (Spain) | sts.eu-south-2.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Europe (Stockholm) | sts.eu-north-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 
| Europe (Zurich) | sts.eu-central-2.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Israel (Tel Aviv) | sts.il-central-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Mexico (Central) | sts.mx-central-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Middle East (Bahrain) | sts.me-south-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| Middle East (UAE) | sts.me-central-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No¹ | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-no.png) No | 
| South America (São Paulo) | sts.sa-east-1.amazonaws.com | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/icon-yes.png) Yes | 

¹You must [enable the Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) to use it. This automatically activates AWS STS. You cannot manually activate or deactivate AWS STS in these Regions.

²To use AWS in China, you need an account and credentials specific to AWS in China.

## AWS STS global endpoint changes
<a name="reference_sts_global_endpoint_changes"></a>

AWS has made changes to the AWS Security Token Service (AWS STS) global endpoint (`https://sts.amazonaws.com`) in Regions [enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) to enhance its resiliency and performance. Previously, all requests to the AWS STS global endpoint were served by a single AWS Region, US East (N. Virginia). Now in Regions [enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html), requests to the AWS STS global endpoint are automatically served in the same Region where the request originates, rather than the US East (N. Virginia) Region. These changes will not be deployed to opt-in Regions.

With this change, AWS STS will process your request based on the originating Region and DNS resolver used. Requests to the AWS STS global endpoint are served in the same Region as your AWS deployed workload if the DNS request for the AWS STS global endpoint is handled by the Amazon DNS server in Regions that are enabled by default. Requests to the AWS STS global endpoint will continue to be served in US East (N. Virginia) Region if your request originated from opt-in Regions or if your request was resolved using a DNS resolver other than the Amazon DNS server. For more information about Amazon DNS, see [ Amazon DNS server](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html#AmazonDNS) in the *Amazon Virtual Private Cloud User Guide*.

The following table shows how requests to the AWS STS global endpoint are routed based on your DNS provider.


| DNS Resolver | Requests to the AWS STS global endpoint routed to the local AWS Region? | 
| --- | --- | 
| Amazon DNS resolver in a Amazon VPC in an Region enabled by default | Yes | 
| Amazon DNS resolver in a Amazon VPC in an opt-in Region | No, the request will be routed to the US East (N. Virginia) Region | 
| DNS resolver provided by your ISP, a public DNS provider, or any other DNS provider | No, the request will be routed to the US East (N. Virginia) Region | 

To ensure minimal disruption to your existing processes, AWS has implemented the following measures:
+ AWS CloudTrail logs for requests made to the AWS STS global endpoint are sent to the US East (N. Virginia) Region. CloudTrail logs for requests served by AWS STS Regional endpoints will continue to be logged to their respective Region in CloudTrail.
+ CloudTrail logs for operations performed by the AWS STS global endpoint and Regional endpoints have additional fields `endpointType` and `awsServingRegion` to indicate which endpoint and Region served the request. For CloudTrail log examples, see [Example AWS STS API event using the global endpoint in CloudTrail log file](cloudtrail-integration.md#stscloudtrailexample-assumerole-sts-global-endpoint).
+ Requests made to the AWS STS global endpoint have a value of `us-east-1` for the `aws:RequestedRegion` condition key, regardless of which Region served the request.
+ Requests handled by the AWS STS global endpoint do not share a requests per second quota with Regional AWS STS endpoints.

If you have workloads in an opt-in Region and are still using the AWS STS global endpoint, we recommend migrating to AWS STS regional endpoints for improved resiliency and performance. For more information about configuring regional AWS STS endpoints, see [AWS STS Regional endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html) in the *AWS SDKs and Tools Reference Guide*.

## AWS CloudTrail and Regional endpoints
<a name="sts-regions-cloudtrail"></a>

Calls to regional and global endpoints are logged in the `tlsDetails` field in AWS CloudTrail. Calls to regional endpoints, such as `us-east-2.amazonaws.com`, are logged in CloudTrail to their appropriate region. Calls to the global endpoint, `sts.amazonaws.com`, are logged as calls to a global service. Events for global AWS STS endpoints are logged to us-east-1.

**Note**  
 `tlsDetails` can only be viewed for services that support this field. See [Services that support TLS details in CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-supported-tls-details.html) in the *AWS CloudTrail User Guide*  
For more information, see [Logging IAM and AWS STS API calls with AWS CloudTrail](cloudtrail-integration.md).