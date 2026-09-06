

# Quotas in AWS Elemental MediaConnect
<a name="quotas"></a>

The following table describes quotas, formerly referred to as *limits*, in AWS Elemental MediaConnect. For information about quotas that can be changed, see [AWS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).


| Resource | Default quota | Comments | 
| --- | --- | --- | 
| Bridges | 40 per gateway | The maximum number of bridges that a gateway can have.You cannot increase this quota. | 
| Entitlements | 50 per flow | The maximum number of entitlements that you can grant on a flow.You cannot increase this quota. | 
| Flows | 20 per AWS Region | The maximum number of flows that you can create in each AWS Region.<br />You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediaconnect/quotas). | 
| Outputs | 50 per transport stream flow<br />10 per CDI flow | The maximum number of outputs that a flow can have.You cannot increase this quota. | 
| Sources | 2 per transport stream flow<br />1 per CDI flow | The maximum number of sources that a flow can have.You cannot increase this quota. | 
| RouterInputs | 20 per AWS Region | The maximum number of router inputs that you can create in each AWS Region.<br />You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediaconnect/quotas). | 
| RouterNetworkInterfaces | 10 per AWS Region | The maximum number of router network interfaces that you can create in each AWS Region.<br />You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediaconnect/quotas). | 
| RouterOutputs | 20 per AWS Region | The maximum number of router outputs that you can create in each AWS Region.<br />You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediaconnect/quotas). | 
| VpcInterfaces | 2 ENA interfaces and 1 EFA interface per flow | The maximum number of VPC interfaces that a flow can have.You cannot increase this quota. | 

**Note**  
To optimize performance, we recommend that you set up your workflow for an aggregate output bandwidth of 400 Mb/s or less. For more information, see [Best practices](best-practices.md).

## Feature-specific output limitations
<a name="feature-specific-output-limits"></a>

The following features have additional output limitations:


|  Feature  |  Output limitation  | 
| --- | --- | 
| Content quality analysis  | Maximum of 10 outputs per flow. If exceeded, content quality analysis is automatically disabled.  | 
| Thumbnails  | Maximum of 10 outputs per flow. If exceeded, thumbnail generation is automatically disabled. | 

## Limits for API requests
<a name="limits-api"></a>

The following table describes the limits for API request frequency in MediaConnect. You cannot increase these limits. If you exceed these limits, you receive an HTTP 429 (`too many requests`) error.


|  API method  |  Limit  | Comments | 
| --- | --- | --- | 
| Frequency of API requests - steady state | 30 requests per second for each account in a Region for the following APIs:+  `DescribeFlow` <br />+  `DescribeFlowSourceMetadata` <br />+  `DescribeFlowSourceThumbnail` <br />+  `GetRouterInput` <br />+  `GetRouterInputSourceMetadata` <br />+  `GetRouterInputThumbnail` <br />+  `GetRouterOutput` <br />+  `TakeRouterInput` <br />5 requests per second for each account in a Region for all other APIs. | You cannot increase this limit. | 
| Frequency of API requests - burst mode | For all APIs:+  30 requests per second for each account in a Region.  | You cannot increase this limit.<br />In burst mode, you can temporarily exceed the steady state limit. If API requests exceed the burst mode limit, your requests are throttled and you receive an HTTP 429 error. The limit refills at a rate of 5 requests per second. | 

**Note**  
If your application exceeds these limits, implement exponential backoff for retries. For more information, see [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *Amazon Web Services General Reference*.