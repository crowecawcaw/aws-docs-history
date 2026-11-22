

# Endpoints and quotas for Amazon OpenSearch Memory

This topic lists the service endpoints, quotas, and limits for Amazon OpenSearch Memory. You can request an increase to a quota that is marked as adjustable. Unless noted otherwise, a request that exceeds a limit fails with `ValidationException`. A [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html) or [UpdateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html) request that would exceed an account quota, such as the number of strategies in a space, fails with `ServiceQuotaExceededException`.

**Topics**
+ [Service endpoints](#memory-quotas-endpoints)
+ [Spaces](#memory-quotas-spaces)
+ [Events](#memory-quotas-events)
+ [Memories](#memory-quotas-memories)
+ [Metadata](#memory-quotas-metadata)
+ [Search requests](#memory-quotas-search)
+ [Request rates](#memory-quotas-rates)

## Service endpoints
<a name="memory-quotas-endpoints"></a>


| Region name | Region | Control plane endpoint | Data plane endpoint | Protocol | 
| --- | --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | osm.us-east-1.api.aws | sp-XXXXXXXXXXXX.osm.us-east-1.on.aws | HTTPS | 
| US West (Oregon) | us-west-2 | osm.us-west-2.api.aws | sp-XXXXXXXXXXXX.osm.us-west-2.on.aws | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | osm.ap-northeast-1.api.aws | sp-XXXXXXXXXXXX.osm.ap-northeast-1.on.aws | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | osm.eu-central-1.api.aws | sp-XXXXXXXXXXXX.osm.eu-central-1.on.aws | HTTPS | 

Space and tagging operations use the control plane endpoint. Event and memory operations use the endpoint of the space. The AWS SDKs and the AWS CLI choose the endpoint for you. OpenSearch Memory doesn't have FIPS endpoints.

## Spaces
<a name="memory-quotas-spaces"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Spaces per account in each AWS Region | 50 | Yes | 
| Memory strategies per space | 10 | No | 
| Maximum event retention (eventExpiryDays) | 365 days | No | 
| Maximum memory retention (memoryExpiryDays) | Forever | No | 

## Events
<a name="memory-quotas-events"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Messages per conversational event | 100 | No | 
| Text per event, across all messages | 5 MiB (UTF-8) | No | 
| Structured data per event | 1 MiB | No | 
| Maximum JSON nesting depth of structured data | 10 | No | 
| Extraction tokens per minute, per account in each AWS Region | 400,000 | Yes | 
| Event IDs per [BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html) request | 10 | No | 
| Session IDs per [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html) request | 10 | No | 
| Session IDs per [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html) request | 10 | No | 
| Actor IDs per [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html) request | 10 | No | 

## Memories
<a name="memory-quotas-memories"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Memory content per [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html) request | 16,000 characters | No | 
| Memory content per [UpdateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html) request | 16,000 characters | No | 
| Strategy selectors per [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) request | 5 | No | 
| Strategy selectors per [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html) request | 5 | No | 
| Strategy names per selector | 20 | No | 

## Metadata
<a name="memory-quotas-metadata"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Distinct metadata keys per space | 50 | Yes | 

## Search requests
<a name="memory-quotas-search"></a>


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Size of query and sort together | 64 KB | No | 
| Clauses per query, counting function\_score functions | 32 | No | 
| Nesting depth of bool queries | 5 | No | 
| Values per terms or ids query | 100 | No | 
| Decay functions per function\_score query | 3 | No | 
| Distinct neural query texts per query | 1 | No | 
| k in a neural query | 100 | No | 
| Event IDs in a terms query on event\_ids in a [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html) request | 10 | No | 
| Results per page (maxResults) | 100 | No | 
| Response size of a [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) request | 5 MiB | No | 
| Response size of a [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html) request | 5 MiB | No | 

## Request rates
<a name="memory-quotas-rates"></a>

The following table lists the request rate for each operation, per account in each AWS Region. A request that exceeds the rate fails with `ThrottlingException`. The AWS SDKs retry throttled requests automatically. If your application receives `ThrottlingException`, retry with exponential backoff. For more information, see [Error retries and exponential backoff](memory-errors.md#memory-errors-retries).


| Operation | Requests per second | Adjustable | 
| --- | --- | --- | 
| [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html) | 5 | Yes | 
| [UpdateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html) | 5 | Yes | 
| [DeleteSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteSpace.html) | 5 | Yes | 
| [ListSpaces](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListSpaces.html) | 10 | Yes | 
| [GetSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetSpace.html) | 20 | Yes | 
| [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_TagResource.html) | 5 | No | 
| [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UntagResource.html) | 5 | No | 
| [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListTagsForResource.html) | 5 | No | 
| [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html) | 50 | Yes | 
| [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html) | 100 | Yes | 
| [BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html) | 50 | Yes | 
| [ListEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListEvents.html) | 50 | Yes | 
| [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html) | 20 | Yes | 
| [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html) | 20 | Yes | 
| [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html) | 10 | Yes | 
| [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html) | 20 | Yes | 
| [UpdateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html) | 10 | Yes | 
| [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html) | 50 | Yes | 
| [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) | 30 | Yes | 
| [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html) | 10 | Yes | 