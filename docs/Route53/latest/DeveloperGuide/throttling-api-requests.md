# Throttling for Amazon Route 53 API requests

###### Important

Amazon Route 53 updated its API throttling behavior. The update includes increasing the
requests per second limit and introducing change-based throttling. This page describes
the updated limits in detail.

Amazon Route 53 throttles API requests on a per-account basis to maintain service stability and
ensure fair usage for all customers. Route 53 applies two independent limits:

- **Request rate:** the number of API requests per
  second.
- **Change throughput:** the number of individual DNS
  record changes per second, aggregated across the API actions that modify DNS
  data.
  A request can be throttled by either limit. When a request is throttled, Amazon Route 53 returns
  an HTTP 400 error (`Bad request`). The response header also includes a
  `Code` element with a value of `Throttling` and a
  `Message` element with a value of `Rate exceeded`.

## How throttling is applied

Amazon Route 53 uses a token bucket algorithm. Each limit has a bucket that holds a maximum
number of tokens. Each request (for the request rate limit) or each change (for the
change throughput limit) removes tokens from the applicable bucket. The bucket refills
at a fixed rate every second, up to its maximum capacity. If refill tokens arrive when
the bucket is already full, Route 53 discards them.

Two values describe each bucket:

- **Bucket maximum capacity** is your burst: the
  number of requests or changes Route 53 can absorb at once when the bucket is
  full.
- **Bucket refill rate** is your sustained rate:
  the number of requests or changes per second you can maintain
  indefinitely.

You can use refill tokens as they are added; you do not need to wait for the bucket to
refill completely.

## Request rate token bucket sizes and refill rates

Route 53 applies request rate throttling at two levels:

- **Account level:** all Amazon Route 53 API requests
  from your account draw from one bucket.
- **Account and operation level:** each API action
  also has its own bucket.

A request consumes a token from both buckets and is throttled if either bucket is
empty. The following actions have different default request rate limits.

Request rate limits per API action| API action | Bucket maximum capacity | Bucket refill rate |
| --- | --- | --- |
| All Amazon Route 53 API actions combined (account level) | 50 | 10 |
| Any single API action not listed below (per-action default) | 50 | 10 |
| `AssociateVPCWithHostedZone` | 20 | 5 |
| `ChangeCidrCollection` | 40 | 5 |
| `CreateCidrCollection` | 40 | 5 |
| `CreateHealthCheck` | 50 | 0.5 |
| `CreateHostedZone` | 40 | 2 |
| `CreateReusableDelegationSet` | 40 | 2 |
| `CreateTrafficPolicyInstance` | 1 | 1 |
| `DeleteCidrCollection` | 40 | 5 |
| `DeleteHealthCheck` | 15 | 3 |
| `DeleteHostedZone` | 40 | 5 |
| `DeleteReusableDelegationSet` | 40 | 5 |
| `DeleteTrafficPolicyInstance` | 1 | 1 |
| `DisassociateVPCFromHostedZone` | 10 | 5 |
| `GetHealthCheckLastFailureReason` | 4 | 1 |
| `GetHealthCheckStatus` | 4 | 1 |
| `UpdateHealthCheck` | 50 | 5 |
| `UpdateTrafficPolicyInstance` | 1 | 1 |

For the complete list of Amazon Route 53 API actions, see [Actions](../APIReference/API_Operations_Amazon_Route_53.md "../APIReference/API_Operations_Amazon_Route_53.md")
in the _Amazon Route 53 API Reference_.

### `CreateHealthCheck` requests

You can submit one `CreateHealthCheck` request every 2 seconds per
AWS account. This corresponds to the refill rate of 0.5 requests per second shown
in the preceding table.

## Change throughput limiting

In addition to the request rate limit, the API actions that modify DNS data are
subject to a change throughput limit. This limit uses a separate token bucket that
depletes based on the number of DNS record changes a request makes, not the number of
requests. Change throughput is limited per AWS account, not per API action. All of the
following actions draw from one bucket, which has a maximum capacity of 1,500 changes
(burst) and refills at 100 changes per second (sustained).

Changes are counted as follows:

Tokens consumed per operation| Operation | Tokens consumed |
| --- | --- |
| `ChangeResourceRecordSets` | 1 per `CREATE`, 1 per `DELETE`, 2 per<br>`UPSERT` |
| `AssociateVPCWithHostedZone` | 2 |
| `DisassociateVPCFromHostedZone` | 2 |
| `CreateHostedZone` | 2 |
| `DeleteHostedZone` | 2 |

All other Amazon Route 53 API actions consume no change throughput tokens and are limited
only by the request rate.

**Example:** You can submit a single request containing
1,000 changes (a burst), which consumes 1,000 tokens. After the burst, the bucket
refills at 100 tokens per second. If you continue submitting 100 changes per second,
you can sustain that rate indefinitely. If you attempt to sustain 500 changes per
second, the bucket depletes and subsequent requests are throttled until it
refills.

## Monitor API throttling

You can monitor your Amazon Route 53 API usage by watching for HTTP 400 responses in your
application logs, or by tracking API usage through CloudWatch metrics. When you receive
throttling errors, your requests are exceeding one of the limits described in the
preceding sections.

## Retries and exponential backoff

When you poll or retry an API request, we recommend using an exponential backoff
algorithm to calculate the sleep interval between requests. Exponential backoff uses
progressively longer waits between retries for consecutive error responses. Implement a
maximum delay interval and a maximum number of retries, and consider adding jitter
(randomized delay) to prevent successive collisions. For more information, see [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ "https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/") in the AWS Builders'
Library.

Each AWS SDK implements automatic retry logic, including an adaptive retry mode that
adjusts the client-side request rate in response to throttling. For workloads that
regularly approach these limits, consider enabling adaptive retries. For more
information, see [Retry behavior](../../../sdkref/latest/guide/feature-retry-behavior.md "../../../sdkref/latest/guide/feature-retry-behavior.md") in the
_AWS SDKs and Tools Reference Guide_.

## Requesting a limit increase

You can request an increase to either the API request rate or the change throughput
limit through AWS Support. To request an increase:

- Open the [AWS Support
  Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home").
- Create a case and choose **Service limit
  increase**.
- For **Limit type**, choose **Route 53**.
- Provide your current usage and the limit you need.

## Best practices for API throttling

- **Balance request rate against batch size:** If
  you are throttled by the request rate limit, send more changes per request. If
  you are throttled by the change throughput limit, reduce your total change rate.
  Neither very small nor very large batches are optimal on their own.
- **Use batching for atomicity:** All changes in a
  single `ChangeResourceRecordSets` request are applied atomically, so
  they succeed or fail together.
- **Spread changes over time:** Distribute changes
  evenly across seconds instead of submitting large batches
  simultaneously.
- **Rely on burst for occasional spikes, not sustained
  throughput:** Burst capacity accommodates legitimate traffic spikes;
  it is not a sustained operating ceiling.
- **Retry with exponential backoff:** When you
  receive HTTP 400 responses, retry after a delay that increases with each attempt
  (see [Retries and exponential backoff](#retries-and-exponential-backoff "#retries-and-exponential-backoff")).
- **Request limit increases proactively:** If you
  anticipate workload growth, request an increase before you hit the limit (see
  [Requesting a limit increase](#requesting-a-limit-increase "#requesting-a-limit-increase")).

For broader Amazon Route 53 guidance, see [Best practices for Amazon Route 53](best-practices.md "best-practices.md").
