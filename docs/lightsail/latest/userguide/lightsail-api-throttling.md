

# Request throttling for the Amazon Lightsail API
<a name="lightsail-api-throttling"></a>

Amazon Lightsail throttles API requests for each AWS account. Throttling ensures that requests to the Amazon Lightsail API do not exceed the maximum allowed API request limits. Amazon Lightsail applies request limits to all API requests, whether they originate from:
+ A third-party application
+ A command line tool
+ The Amazon Lightsail console

Amazon Lightsail implements two types of API throttling: static request-rate limiting and dynamic request-rate limiting.

## Static request-rate limiting
<a name="lightsail-api-throttling-static"></a>

Amazon Lightsail primarily uses the token bucket algorithm to implement static request-rate limiting on a per-Region basis. With this algorithm, your account has a bucket for each API that holds a specific number of tokens. The number of tokens in the bucket represents your throttling limit at any given second.

With static request-rate limiting, Amazon Lightsail evaluates each API individually and throttles you based on the number of requests you make per API. Each request that you make removes one token from the API's bucket. For example, the token bucket size for `GetInstances` is 20 tokens. You can make up to 20 `GetInstances` requests in one second. If you exceed 20 requests in a second, you are throttled on that API. The remaining requests within that second fail. However, requests for other APIs are not affected.

Buckets automatically refill at a set rate. If the bucket is below its maximum capacity, a set number of tokens is added back to it every second until it reaches its maximum capacity. If the bucket is full when refill tokens arrive, they are discarded. The bucket can't hold more than its maximum number of tokens. For example, the bucket size for `GetInstances` is 20 tokens, and the refill rate is 5 tokens per second. If you make 20 `GetInstances` requests in one second, the bucket is reduced to zero (0) tokens. The bucket is then refilled by 5 tokens every second, until it reaches its maximum capacity of 20 tokens. This means that an empty bucket reaches its maximum capacity after 4 seconds if no requests are made during that time.

You do not need to wait for the bucket to be completely full before you can make API requests. Incoming API requests use the refill tokens as they are added to the bucket. If you immediately use the refill tokens, the bucket does not reach its maximum capacity. For example, the bucket size for `GetInstances` is 20 tokens and the refill rate is 5 tokens per second. If you deplete the bucket by making 20 API requests in a second, you can continue to make 5 API requests per second by using the refill tokens as they are added to the bucket. The bucket can refill to the maximum capacity only if you make fewer than 5 API requests per second.

If you exceed a static request-rate limit, you receive an exception with error code `ThrottlingException` and HTTP status code **403** with the following message:

*"The maximum API request rate has been exceeded for your account. Please try your request again shortly. For best results using the Lightsail API, use an increased time interval between requests."*

### Request token bucket sizes and refill rates
<a name="lightsail-api-throttling-static-buckets"></a>

The following table lists the token bucket sizes and refill rates for each API action category.


|  Categories/API actions  |  Bucket maximum capacity (per API action)  |  Bucket refill rate  | 
| --- | --- | --- | 
|  +  Disk mutating actions <br />+  KeyPair mutating actions <br />+  Start, stop, or reboot instance actions   | 20 | 10 | 
|  +  Put, close, or open instance public ports actions <br />+  Domain mutating actions <br />+  `GetBuckets` <br />+  `GetContainerImages` <br />+  `GetContainerServiceDeployments` <br />+  `GetContainerServices` <br />+  `GetDisks` <br />+  `GetInstance` <br />+  `GetInstanceSnapshot` <br />+  `GetInstanceSnapshots` <br />+  `GetInstanceState` <br />+  `GetInstances` <br />+  `GetLoadBalancer` <br />+  `GetLoadBalancers` <br />+  `GetOperations` <br />+  `GetStaticIp` <br />+  `GetStaticIps`   | 20 | 5 | 
|  +  `CopyInstanceSnapshot` <br />+  `CreateInstanceSnapshot` <br />+  `DeleteInstance` <br />+  `DeleteInstanceSnapshot` <br />+  `PeerVpc` <br />+  `UnpeerVpc`   | 20 | 1 | 
|  +  `AttachLoadBalancerTlsCertificate` <br />+  `CreateInstances` <br />+  `CreateInstancesFromSnapshot` <br />+  `DeleteLoadBalancerTlsCertificate` <br />+  `GetBucketAccessKeys`   | 10 | 1 | 
|  +  StaticIp mutating actions <br />+  Contact method mutating actions <br />+  `SetIpAddressType` <br />+  Create or delete certificate actions <br />+  Copy or export snapshot actions <br />+  `DeleteKnownHostKeys` <br />+  `UpdateInstanceMetadataOptions`   | 1 | 1 | 
|  +  All Bucket mutating actions except `DeleteBucket` <br />+  `DeleteRelationalDatabase`   | 5 | 2 | 
|  +  All Container mutating actions except `DeleteContainerImage` <br />+  `CreateCloudFormationStack` <br />+  `ResetDistributionCache` <br />+  `TestAlarm`   | 1 | 0.5 | 
|  +  `AttachCertificateToDistribution` <br />+  `CreateDistribution` <br />+  `DeleteBucket` <br />+  `DeleteDistribution` <br />+  `DetachCertificateFromDistribution` <br />+  `UpdateDistribution`   | 2 | 0.2 | 
|  +  `DeleteAutoSnapshot` <br />+  `DeleteContainerImage` <br />+  `DisableAddOn` <br />+  `EnableAddOn` <br />+  `GetAlarms` <br />+  `GetAutoSnapshots` <br />+  `GetContactMethods` <br />+  `GetContainerLog` <br />+  `IsVpcPeered`   | 5 | 1 | 
|  +  `TagResource` <br />+  `UntagResource`   | 40 | 10 | 
|  +  `CreateRelationalDatabaseSnapshot` <br />+  `GetRelationalDatabase` <br />+  `GetRelationalDatabaseEvents` <br />+  `GetRelationalDatabaseSnapshot` <br />+  `GetRelationalDatabaseSnapshots` <br />+  `GetRelationalDatabases`   | 20 | 4 | 
|  +  `GetBucketMetricData` <br />+  `GetContainerServiceMetricData` <br />+  `GetDistributionBundles` <br />+  `GetDistributionLatestCacheReset` <br />+  `GetDistributionMetricData` <br />+  `GetDistributions` <br />+  `UpdateDistributionBundle`   | 7 | 5 | 
|  +  `AttachInstancesToLoadBalancer` <br />+  `DetachInstancesFromLoadBalancer`   | 10 | 2 | 
| `CreateGUISessionAccessDetails` | 20 | 20 | 
| `CreateLoadBalancer` | 3 | 1 | 
| `CreateRelationalDatabaseFromSnapshot` | 15 | 1 | 
| `DeleteAlarm` | 3 | 1 | 
| `DeleteLoadBalancer` | 10 | 3 | 
| `GetCertificateDetails` | 10 | 5 | 
| `GetCertificates` | 8 | 5 | 
| `GetCostEstimate` | 5 | 5 | 
| `GetLoadBalancerMetricData` | 20 | 10 | 
| `GetLoadBalancerTlsCertificates` | 10 | 5 | 
| `GetRelationalDatabaseBlueprints` | 10 | 2 | 
| `GetRelationalDatabaseLogEvents` | 6 | 2 | 
| `GetRelationalDatabaseLogStreams` | 20 | 3 | 
| `GetRelationalDatabaseParameters` | 20 | 3 | 
| `GetSetupHistory` | 5 | 5 | 
| `PutAlarm` | 3 | 1 | 
| `RebootRelationalDatabase` | 20 | 3 | 
| `RegisterContainerImage` | 5 | 1 | 
| `SetResourceAccessForBucket` | 2 | 0.4 | 
| `SetupInstanceHttps` | 5 | 5 | 
| `StartGUISession` | 5 | 5 | 
| `StartRelationalDatabase` | 20 | 3 | 
| `StopGUISession` | 5 | 5 | 
| `StopRelationalDatabase` | 20 | 3 | 
| `UpdateLoadBalancerAttribute` | 15 | 2 | 
| `UpdateRelationalDatabase` | 6 | 3 | 
| `UpdateRelationalDatabaseParameters` | 20 | 3 | 
| All `Get*` API actions that are not included in any other category | 20 | 10 | 

## Dynamic request-rate limiting
<a name="lightsail-api-throttling-dynamic"></a>

In addition to static request-rate limiting, Amazon Lightsail uses dynamic request-rate limiting for certain API actions. Unlike static limits which are fixed for all customers and implemented on a per-Region basis, dynamic limits automatically scale based on the number of resources in your account, and are tracked globally across all AWS Regions.

### How it works
<a name="lightsail-api-throttling-dynamic-how-it-works"></a>

Dynamic request-rate limiting tracks your requests for a subset of Lightsail API actions. It uses rolling 1-hour and 24-hour time windows. For each rolling time window, you get an API request limit based on the number of Lightsail resources you have. At any given moment, the system evaluates requests within a rolling time window (1-hour or 24-hour) and counts how many requests you made within that window. It compares this count against your limit for that time window. Every incoming request is evaluated against both time windows simultaneously. To avoid throttling, you must remain within both your 1-hour and 24-hour limits.

The following table shows the dynamic API limits for each resource type and time window.


|  Resource  |  API actions that count towards dynamic limits  |  API actions that are subject to throttling  |  Time window  |  Dynamic API limits  | 
| --- | --- | --- | --- | --- | 
| Lightsail instance | Static IP mutating API actions (`AttachStaticIp`, `AllocateStaticIp`, `ReleaseStaticIp`, `DetachStaticIp`) | `AttachStaticIp`, `AllocateStaticIp` | 1 hour | 10x the number of Lightsail instances or 50, whichever is greater | 
| Lightsail instance | Static IP mutating API actions (`AttachStaticIp`, `AllocateStaticIp`, `ReleaseStaticIp`, `DetachStaticIp`) | `AttachStaticIp`, `AllocateStaticIp` | 24 hours | 20x the number of Lightsail instances or 500, whichever is greater | 

### When does throttling occur
<a name="lightsail-api-throttling-dynamic-when"></a>

Your dynamic request limits are calculated based on the number of Lightsail instances in your account. The 1-hour limit is either 10 times your instance count or 50, whichever is greater. The 24-hour limit is either 20 times your instance count or 500, whichever is greater. For example, with 3 instances, your 1-hour limit is 50 API requests (the minimum of 50) and your 24-hour limit is 500 API requests (the minimum of 500). With 30 instances, your 1-hour limit scales to 300 API requests and your 24-hour limit scales to 600. As you grow your Lightsail instances, your limits grow proportionally for Static IP API actions.

At any given moment, the system evaluates requests within a rolling time window (1-hour or 24-hour), and counts the total number of `AttachStaticIp`, `AllocateStaticIp`, `DetachStaticIp`, and `ReleaseStaticIp` API requests you have made within that window. Of these four, only `AllocateStaticIp` and `AttachStaticIp` are subject to throttling. You are throttled on these requests when the total count of all four Static IP API requests exceeds your 1-hour or 24-hour limit. `DetachStaticIp` and `ReleaseStaticIp` requests count toward your limit. However, these requests are never throttled by dynamic request-rate limiting. This ensures you always have control over resource management and cost optimization. Throttling automatically ends when enough API requests move outside the time window to bring your total count back under the limit.

For example, assume you have 5 or fewer instances. This gives you the minimum 1-hour limit of 50 requests. If you make 51 `AllocateStaticIp` or `AttachStaticIp` API requests in rapid succession, you are throttled until the oldest API request falls outside the 1-hour time window—approximately 1 hour from when you made that first API request. Because both limits are evaluated simultaneously, you can be throttled even when you are well within one limit. Assume you have 10 instances, giving you a 1-hour limit of 100 and a 24-hour limit of 500. If you make 25 API requests per hour for 20 consecutive hours, you have made 500 API requests total within the 24-hour window. If you then try to make one more request, you are throttled by your 24-hour limit. This occurs even though you are well under your 1-hour limit of 100 for that specific hour.

If you exceed the dynamic throttling limits, you receive an exception with error code `ThrottlingException` and HTTP status code **403** with the following message:

*"The operation cannot be completed at this time for your account. Try again later or contact AWS Support for assistance."*

## How dynamic and static limits work together
<a name="lightsail-api-throttling-dynamic-and-static"></a>

Both dynamic and static limits are evaluated independently for every request, and you must stay within both limits to avoid throttling. You can think of static limits as controlling how fast you can make requests (the rate), while dynamic limits control how many total requests you can make within a time period (the volume).

For example, with 10 instances you have a 1-hour dynamic limit of 100 API requests and a static limit of 1 API request per second. If you try to make 5 `AttachStaticIp` requests simultaneously, the static limit blocks you after the first request. You must wait 1 second between each request due to the static limit, but you do not hit your dynamic limit until you make 100 API requests. Conversely, with 5 instances, you have a 1-hour dynamic limit of 50 API requests. If you make 1 API request per second for 50 seconds, each request passes the static limit check. However, your 51st request exceeds your dynamic limit of 50 and is throttled until older API requests begin to age out of the 1-hour window.

## Request a limit increase
<a name="lightsail-api-throttling-request-limit-increase"></a>

If your workload requires higher dynamic request-rate limits, you can request an increase for your account.

**To request a dynamic limit increase**

1. Open [AWS Support Center](https://support.console.aws.amazon.com/support/home#/) and start a new case.

1. For **Subject**, enter **Request an increase in my Amazon Lightsail API dynamic throttling limits**.

1. For **Description**, provide the following information:
   + A brief description of your use case. If available, include the IDs of a few Lightsail requests that were throttled.
   + The one-hour time window when peak throttling or usage occurred.