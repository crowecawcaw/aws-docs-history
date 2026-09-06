

# Request throttling for the Amazon ECS API
<a name="request-throttling"></a>

Amazon Elastic Container Service throttles all API requests for each AWS account on a per-Region basis. We do this to ensure consistent performance and fair usage of the service for all Amazon ECS customers. Throttling ensures that calls to the Amazon ECS API do not exceed the maximum allowed API request quotas for both Amazon ECS and the other AWS services that it integrates with. API calls are subject to the request quotas whether they originate from:
+ A third-party application
+ A command line tool
+ The Amazon ECS console

If you exceed an API throttling quota, you get the `ThrottlingException` error code.

```
An error occurred (ThrottlingException) when calling the DescribeClusters operation (reached max retries: 4): Rate exceeded.
com.amazonaws.services.ecs.model.AmazonECSException: Rate exceeded (Service: AmazonECS; Status Code: 400; Error
Code: ThrottlingException; Request ID: 5ed90669-e454-464d-9b2f-6523bc86f537; Proxy: null)
```

## How throttling Is applied
<a name="throttling-how"></a>

Amazon ECS uses the [token bucket algorithm](https://en.wikipedia.org/wiki/Token_bucket) to implement API throttling. With this algorithm, your account has a *bucket* that holds a specific number of *tokens*. The number of tokens in the bucket represents your throttling quota at any given second.

Amazon ECS examines the rate of API request submissions for all Amazon ECS APIs in your account, per Region, and applies two types of API throttling quotas: *sustained* and *burst*. The sustained rate is the average number of API requests allowed per second over time for an operation. The burst rate is the maximum number of API requests allowed in any one second. With burst, you can periodically make a higher number of API requests than the sustained rate. Following which, Amazon ECS throttles subsequent API requests until the rate of API requests allowed over time stabilizes to the sustained rate. In the token bucket algorithm, the *bucket maximum capacity* signifies the burst rate and the *bucket refill rate* is the sustained rate. We will use these terms to provide you an illustration of Amazon ECS API request throttling in the following example.

You are throttled on the number of API requests you make and each request removes one token from the token bucket. For example, the bucket size for *Cluster read actions*, such as the `DescribeClusters` API, is 50 tokens, so you can make up to 50 `DescribeClusters` requests in one second. If you exceed 50 requests in a second, you are throttled and the remaining requests within that second fail.

Buckets automatically refill at a set rate. If the bucket is below its maximum capacity, a set number of tokens is added back to it every second until it reaches its maximum capacity. If the bucket is full when refill tokens arrive, they are discarded. The bucket cannot hold more than its maximum number of tokens. For example, the bucket size for *Cluster read actions*, such as the `DescribeClusters` API, is 50 tokens, and the refill rate is 20 tokens per second. If you make 50 `DescribeClusters` API requests in a second, the bucket is immediately reduced to zero tokens. The bucket is then refilled by 20 tokens every second, until it reaches its maximum capacity of 50 tokens. This means that the previously empty bucket reaches its maximum capacity after 2.5 seconds.

You do not need to wait for the bucket to be completely full before you can make API requests. You can use tokens as they are added to the bucket. If you immediately use the refill tokens, the bucket does not reach its maximum capacity. For example, the bucket size for *Cluster read actions*, such as the `DescribeClusters` API, is 50 tokens, and the refill rate is 20 tokens per second. If you deplete the bucket by making 50 API requests in a second, you can continue to make 20 API requests per second. The bucket can refill to the maximum capacity only if you make fewer than 20 API requests per second.

## Request Token Bucket Sizes and Refill Rates
<a name="throttling-quotas"></a>

For request rate limiting purposes, API actions are grouped into categories. All API actions in a category share the same token bucket. For instance, `DescribeClusters` and `ListClusters` APIs share the *Cluster read actions* bucket, for which capacity is 50 and refill rate is 20. This means that the cumulative number of API requests for all *Cluster read actions* is throttled by the same burst rate quota of 50 API requests. Thus, you can make 25 `DescribeClusters` and 25 `ListClusters` API requests in one second, or 30 `DescribeClusters` and 20 `ListClusters`, or 50 `DescribeClusters` and 0 `ListClusters`, or 0 `DescribeClusters` and 50 `ListClusters`, but you cannot make 50 `DescribeClusters` and 50 `ListClusters` requests at the same time. Sustained rate is similarly applied cumulatively to all API requests within a bucket.

The following table shows the bucket capacity (or burst) and refill rate (or sustained) for all AWS Regions. All API action categories enforce rate quotas for each AWS account on a per-Region basis.


| API action category | Actions | Bucket maximum capacity (or Burst rate) | Bucket refill rate (or Sustained rate) | 
| --- | --- | --- | --- | 
| Cluster modify actions |  +   `CreateCluster` <br />+   `DeleteCluster` <br />+   `PutClusterCapacityProviders` <br />+   `UpdateCluster` <br />+   `UpdateClusterSettings`   | 20 | 1 | 
| Cluster read actions |  +   `DescribeClusters` <br />+   `ListClusters`   | 50 | 20 | 
| Task definition modify actions |  +   `DeregisterTaskDefinition` <br />+   `RegisterTaskDefinition`   | 20 | 1 | 
| Task definition read actions |  +   `DescribeTaskDefinition` <br />+   `ListTaskDefinitions` <br />+   `ListTaskDefinitionFamilies`   | 50 | 20 | 
| Task definition deletion actions |  +  `DeleteTaskDefinitions`   | 5 | 1 | 
| Capacity provider modify actions |  +   `CreateCapacityProvider` <br />+   `DeleteCapacityProvider` <br />+   `UpdateCapacityProvider`   | 10 | 1 | 
| Capacity provider read actions |  +   `DescribeCapacityProviders`   | 50 | 20 | 
| Tag modify actions |  +   `TagResource` <br />+   `UntagResource`   | 20 | 10 | 
| Tag read actions |  +   `ListTagsForResource`   | 50 | 20 | 
| Setting modify actions |  +   `DeleteAccountSetting` <br />+   `PutAccountSetting` <br />+   `PutAccountSettingDefault`   | 10 | 1 | 
| Setting read actions |  +   `ListAccountSettings`   | 50 | 20 | 
| Cluster resource modify actions |  +  `DeleteAttributes` <br />+  `DeregisterContainerInstance` <br />+  `ExecuteCommand` <br />+  `PutAttributes` <br />+  `RunTask`[1](#note-1) <br />+  `StartTask` <br />+  `StopTask` <br />+  `UpdateContainerAgent` <br />+  `UpdateContainerInstancesStates`   | 100 | 40 | 
| Cluster resource read actions |  +  `DescribeContainerInstances` <br />+  `DescribeTasks` <br />+  `ListAttributes` <br />+  `ListContainerInstances` <br />+  `ListTasks`   | 100 | 20 | 
| Agent modify actions |  +  `RegisterContainerInstance` <br />+  `SubmitAttachmentStateChanges` <br />+  `SubmitContainerStateChange` <br />+  `SubmitTaskStateChange`   | 200 | 120 | 
| Service modify actions |  +  `CreateService` <br />+  `DeleteService` <br />+  `UpdateService`   | 50 | 5 | 
| Service read actions |  +  `DescribeServices` <br />+  `ListServices`   | 100 | 20 | 
| Service deployment actions |  +  `DescribeServiceDeployments` <br />+  `ListServiceDeployments`   | 50 | 20 | 
| Service revision actions |  +  `DescribeServiceRevisions`   | 50 | 20 | 
| Task protection actions |  +  `UpdateTaskProtection` <br />+  `GetTaskProtection`   | 200 | 80 | 
| Cluster service resource read actions |  +  `ListServicesByNamespace`   | 10 | 1 | 

<a name="note-1"></a>1 AWS Fargate additionally throttles Amazon ECS `RunTask` API to the rates listed [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/throttling.html) in the *Amazon ECS Developer Guide*.

## Adjusting API throttling quotas
<a name="throttling-increase"></a>

You can request an increase for API throttling quotas for your AWS account. To request a quota adjustment, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

## Handling API throttling
<a name="handling-throttling"></a>

You can implement an error retry and exponential back-off strategy to avoid the impact of throttling errors on your workloads. If you use AWS SDK, the automatic retry logic is already built-in and configurable. You can refer to the following resources for more details:
+ [Error retries and exponential backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) in the AWS General Reference Guide
+ [Exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) blog post
+ [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) article in the Amazon Builder’s Library