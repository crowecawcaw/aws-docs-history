# Handle AWS Cloud Map DiscoverInstances API request throttling

AWS Cloud Map throttles [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API requests for
each AWS account on a per-Region basis. Throttling helps improve the performance of the service
and helps provide fair usage for all AWS Cloud Map customers. Throttling ensures that calls to the
AWS Cloud Map [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API doesn't exceed the maximum allowed [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API request
quotas. [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API calls originating from any of the following sources are subject
to the request quotas:

- A third-party application
- A command line tool
- The AWS Cloud Map console
  If you exceed an API throttling quota, you get the `RequestLimitExceeded` error
  code. For more information, see [Request rate limiting](#throttling-rate-based "#throttling-rate-based").

## How throttling is applied

AWS Cloud Map uses the [token bucket
algorithm](https://en.wikipedia.org/wiki/Token_bucket "https://en.wikipedia.org/wiki/Token_bucket") to implement API throttling. With this algorithm, your account has a
_bucket_ that holds a specific number of _tokens_. The
number of tokens in the bucket represents your throttling quota at any given second. There is
one bucket for a single Region, and it applies to all endpoints in the Region.

### Request rate limiting

Throttling limits the number of [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API requests
that you can make. Each request removes one token from the bucket. For example, the bucket size
for the [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API operation is 2,000 tokens, so you can make up to 2,000 [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") requests in one second. If you exceed 2,000 requests in one second,
you're throttled and the remaining requests within that second fail.

Buckets automatically refill at a set rate. If the bucket isn't at capacity, a set number
of tokens is added back every second until the bucket reaches capacity. If the bucket is at
capacity when refill tokens arrive, then these tokens are discarded. The bucket size for the
[DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API operation is 2,000 tokens, and the refill rate is 1,000 tokens
every second. If you make 2,000 [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API requests
in a second, the bucket is immediately reduced to zero (0) tokens. The bucket is then refilled
by up to 1,000 tokens every second until it reaches its maximum capacity of 2,000
tokens.

You can use tokens as they are added to the bucket. You don't need to wait for the bucket
to be at maximum capacity before you make API requests. If you deplete the bucket by making
2,000 [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API requests in one second, you can still make up to 1,000 [DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md") API requests every second after that for as long as you need. This
means that you can immediately use the refill tokens as they are added to your bucket. The
bucket only starts to refill to the maximum capacity when you make fewer API requests every
second than the refill rate.

### Retries or batch processing

If an API request fails, your application might need to retry the request. To reduce the
number of API requests, use an appropriate sleep interval between successive requests. For best
results, use an increasing or variable sleep interval.

### Calculating the sleep interval

When you have to poll or retry an API request, we recommend using an exponential backoff
algorithm to calculate the sleep interval between API calls. By using progressively longer wait
times between retries for consecutive error responses, you can reduce the number of failed
requests. For more information and implementation examples of this algorithm, see [Retry Behavior](../../../sdkref/latest/guide/feature-retry-behavior.md "../../../sdkref/latest/guide/feature-retry-behavior.md") in the _AWS SDKs and Tools Reference Guide_.

## Adjusting API throttling quotas

You can request an increase to API throttling quotas for your AWS account. To request a
quota adjustment, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
