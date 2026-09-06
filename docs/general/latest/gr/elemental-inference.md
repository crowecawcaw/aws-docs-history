

# AWS Elemental Inference endpoints and quotas
<a name="elemental-inference"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="elemental-inference_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 |  elemental-inference.us-east-1.amazonaws.com  | HTTPS | 
| US West (Oregon) | us-west-2 |  elemental-inference.us-west-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  elemental-inference.ap-south-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  elemental-inference.ap-southeast-2.amazonaws.com  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  elemental-inference.eu-west-1.amazonaws.com  | HTTPS | 

## Service quotas
<a name="limits_elemental-inference"></a>


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Active feeds per account | ap-south-1: 1 Count<br />eu-west-1: 1 Count<br />Each of the other supported Regions: 2 Count |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/elemental-inference/quotas/L-EB1E4A1B)  | The maximum number of feeds that can be actively running simultaneously in this account in the current AWS Region. | 
| Enabled outputs per feed | Each supported Region: 3 Count | No | The maximum number of outputs that can be enabled per feed in this account in the current AWS Region. | 
| Request rate for AssociateFeed | Each supported Region: 5 Count/Second | No | The maximum number of AssociateFeed requests per second that you can send in this account in the current AWS Region. | 
| Request rate for AssociateFeed, in a burst | Each supported Region: 30 Count | No | The maximum number of AssociateFeed requests that you can send in one burst in this account in the current AWS Region. | 
| Request rate for CreateFeed | Each supported Region: 5 Count/Second | No | The maximum number of CreateFeed requests per second that you can send in this account in the current AWS Region. | 
| Request rate for CreateFeed, in a burst | Each supported Region: 30 Count | No | The maximum number of CreateFeed requests that you can send in one burst in this account in the current AWS Region. | 
| Request rate for DeleteFeed | Each supported Region: 5 Count/Second | No | The maximum number of DeleteFeed requests per second that you can send in this account in the current AWS Region. | 
| Request rate for DeleteFeed, in a burst | Each supported Region: 30 Count | No | The maximum number of DeleteFeed requests that you can send in one burst in this account in the current AWS Region. | 
| Request rate for DisassociateFeed | Each supported Region: 5 Count/Second | No | The maximum number of DisassociateFeed requests per second that you can send in this account in the current AWS Region. | 
| Request rate for DisassociateFeed, in a burst | Each supported Region: 30 Count | No | The maximum number of DisassociateFeed requests that you can send in one burst in this account in the current AWS Region. | 
| Request rate for GetFeed | Each supported Region: 5 Count/Second | No | The maximum number of GetFeed requests per second that you can send in this account in the current AWS Region. | 
| Request rate for GetFeed, in a burst | Each supported Region: 30 Count | No | The maximum number of GetFeed requests that you can send in one burst in this account in the current AWS Region. | 
| Request rate for GetMetadata | Each supported Region: 2 Count/Second | No | The maximum number of GetMetadata requests per second that you can send for each feed, input, and output combination in the current AWS Region. | 
| Request rate for GetMetadata, in a burst | Each supported Region: 5 Count | No | The maximum number of GetMetadata requests that you can send in one burst for each feed, input, and output combination in the current AWS Region. | 
| Request rate for ListFeeds | Each supported Region: 5 Count/Second | No | The maximum number of ListFeeds requests per second that you can send in this account in the current AWS Region. | 
| Request rate for ListFeeds, in a burst | Each supported Region: 30 Count | No | The maximum number of ListFeeds requests that you can send in one burst in this account in the current AWS Region. | 
| Request rate for PutMedia | Each supported Region: 1.5 Count/Second | No | The maximum number of PutMedia requests per second that you can send for each feed, input, and stream combination in the current AWS Region. | 
| Request rate for PutMedia, in a burst | Each supported Region: 5 Count | No | The maximum number of PutMedia requests that you can send in one burst for each feed, input, and stream combination in the current AWS Region. | 
| Request rate for UpdateFeed | Each supported Region: 5 Count/Second | No | The maximum number of UpdateFeed requests per second that you can send in this account in the current AWS Region. | 
| Request rate for UpdateFeed, in a burst | Each supported Region: 30 Count | No | The maximum number of UpdateFeed requests that you can send in one burst in this account in the current AWS Region. | 
| Total dictionaries per account | Each supported Region: 10 Count |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/elemental-inference/quotas/L-6FCCF60B)  | The maximum number of dictionaries that you can create in this account in the current AWS Region. | 
| Total feeds per account | Each supported Region: 1,000 Count | No | The maximum number of feeds that you can create in this account in the current AWS Region. | 
| Total outputs per feed | Each supported Region: 30 Count | No | The maximum number of outputs that you can create per feed in this account in the current AWS Region. | 