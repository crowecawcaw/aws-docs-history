# Request throttling for the Elastic Load Balancing API

Elastic Load Balancing throttles its API requests for each AWS account on a per-Region basis. We do this
to help the performance and availability of the service. Throttling ensures that requests
to the Elastic Load Balancing API do not exceed the maximum allowed API request limits. API requests are
subject to the request limits whether you call them or they are called on your behalf (for
example, by the AWS Management Console or a third-party application).

If you exceed an Elastic Load Balancing API throttling limit, you get the `ThrottlingException`
error code and a `Rate exceeded` error message.

We recommend that you prepare to handle throttling gracefully. For more information, see
[Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ "https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/"). If you experience a high level of
throttling, you can contact AWS Support to help you evaluate your API usage and potential
solutions. Each case is evaluated individually. Support might increase your limits within the
safety limits of the system, to maintain high availability and predictable performance.

## How throttling is applied

Elastic Load Balancing uses the [token bucket
algorithm](https://en.wikipedia.org/wiki/Token_bucket "https://en.wikipedia.org/wiki/Token_bucket") to implement API throttling. With this algorithm, your account has
a _bucket_ that holds a specific number of
_tokens_. The number of tokens in the bucket represents your
throttling limit at any given second.

Elastic Load Balancing provides two sets of API actions. ELB API version 2 supports the following types
of load balancers: Application Load Balancers, Network Load Balancers, and Gateway Load Balancers. ELB API version 1 supports Classic Load Balancers. Each
ELB API version has its own buckets and tokens.

Services that call the Elastic Load Balancing API on your behalf, such as Amazon EC2, Amazon ECS, Amazon EC2 Auto Scaling,
and AWS CloudFormation have their own account-level buckets. These services do not consume tokens
from your buckets.

## Request rate limiting

With request rate limiting, you are throttled on the number of API requests that you
make. Each request that you make removes one token from the bucket. For example, the
token bucket size for non-mutating API actions is 40 tokens. You can make up to 40
`Describe*` requests in one second. If you exceed 40
`Describe*` requests in one second, you are throttled and the remaining
requests within that second fail.

Buckets automatically refill at a set rate. If a bucket is below its maximum
capacity, a set number of tokens is added back every second until the bucket reaches its
maximum capacity. If a bucket is full when refill tokens arrive, they are discarded.
A bucket can't hold more than its maximum number of tokens. For example, the bucket
size for non-mutating API actions is 40 tokens and the refill rate is 10 tokens per
second. If you make 40 `DescribeLoadBalancers` requests in one second, the
bucket is reduced to zero (0) tokens. We add 10 refill tokens to the bucket every
second, until it reaches its maximum capacity of 40 tokens. This means that it takes
4 seconds for an empty bucket to reach its maximum capacity, if no requests are
made during that time.

You do not need to wait for a bucket to be completely full before you can make API
requests. You can use tokens as they are added to a bucket. If you immediately use the
refill tokens, the bucket does not reach its maximum capacity.

There is an account-level throttling limit that is shared across all Elastic Load Balancing API actions.
The capacity of the account-level bucket is 40 tokens and the refill rate is 10 request
tokens per second.

## Request token bucket sizes and refill rates

For request rate limiting purposes, API actions are grouped into categories. Each
category has its own limits.

###### Categories

- **Mutating actions** — API actions that create, modify,
  or delete resources. This category generally includes all API actions that are not categorized
  as _non-mutating actions_. These actions have a lower throttling limit than
  non-mutating API actions.
- **Non-mutating actions** — API actions that
  retrieve data about resources. These API actions typically have the highest API
  throttling limits.
- **Resource-intensive actions** — API actions
  that take the most time and consume the most resources to complete. These actions have an
  even lower throttling limit than mutating actions. These actions are throttled
  separately from other mutating actions.
- **Registration actions** —
  API actions that register or deregister targets. These API actions
  are throttled separately from other mutating actions.
- **Uncategorized actions** — These API actions receive
  their own token bucket sizes and refill rates, even though they fall under one of the other
  categories.

The following table shows the default capacity and refill rates for the categorized request token buckets.

| Category               | ELBv2 actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | ELBv1 actions                                                                                                                                                                                                                                                                                           | Bucket capacity | Refill rate (per second) |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------ |
| **Resource-intensive** | `CreateLoadBalancer`, `SetSubnets`                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `CreateLoadBalancer`,<br>`AttachLoadBalancerToSubnets`,<br>`DetachLoadBalancerFromSubnets`,<br>`EnableAvailabilityZonesForLoadBalancer`,<br>`DisableAvailabilityZonesForLoadBalancer`                                                                                                                   | 10              | 0.2 **†**                |
| **Registration**       | `RegisterTargets`, `DeregisterTargets`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `RegisterInstancesWithLoadBalancer`,<br>`DeregisterInstancesFromLoadBalancer`                                                                                                                                                                                                                           | 20              | 4                        |
| **Non-mutating**       | `DescribeAccountLimits`,<br>`DescribeCapacityReservation`,<br>`DescribeListenerAttributes`,<br>`DescribeListenerCertificates`,<br>`DescribeListeners`,<br>`DescribeLoadBalancerAttributes`,<br>`DescribeLoadBalancers`, `DescribeRules`,<br>`DescribeSSLPolicies`, `DescribeTags`,<br>`DescribeTargetGroupAttributes`,<br>`DescribeTargetGroups`,<br>`DescribeTargetHealth`                                                                                                                                      | `Describe*`                                                                                                                                                                                                                                                                                             | 40              | 10                       |
| **Mutating**           | `AddListenerCertificates`, `AddTags`,<br>`CreateListener`, `CreateRule`,<br>`CreateTargetGroup`, `DeleteListener`,<br>`DeleteLoadBalancer`, `DeleteRule`,<br>`DeleteTargetGroup`,<br>`ModifyCapacityReservation`, `ModifyIpPools`,<br>`ModifyListener`, `ModifyListenerAttributes`,<br>`ModifyLoadBalancerAttributes`, `ModifyRule`,<br>`ModifyTargetGroup`,<br>`ModifyTargetGroupAttributes`,<br>`RemoveListenerCertificates`, `RemoveTags`,<br>`SetIpAddressType`, `SetRulePriorities`,<br>`SetSecurityGroups` | `AddTags`, `ApplySecurityGroupsToLoadBalancer`,<br>`ConfigureHealthCheck`,<br>`CreateAppCookieStickinessPolicy`,<br>`CreateLbCookieStickinessPolicy`,<br>`CreateLoadBalancerListener`,<br>`CreateLoadBalancerPolicy`, `Delete*`,<br>`ModifyLoadBalancerAttributes`, `RemoveTags`,<br>`SetLoadBalancer*` | 20              | 3                        |

The following table shows the default capacity and refill rates for the uncategorized request token buckets for ELBv2.

| ELBv2 actions                                                                                                                                   | Bucket capacity | Refill rate (per second) |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------ |
| `CreateTrustStore`                                                                                                                              | 10              | 0.2 **†**                |
| `AddTrustStoreRevocations`,<br>`DeleteSharedTrustStoreAssociation`,<br>`DeleteTrustStore`, `ModifyTrustStore`,<br>`RemoveTrustStoreRevocations` | 10              | 0.2 **†**                |
| `GetResourcePolicy`,<br>`GetTrustStoreCaCertificatesBundle`,<br>`GetTrustStoreRevocationContent`                                                | 20              | 4                        |
| `DescribeTrustStoreAssociations`,<br>`DescribeTrustStoreRevocations`,<br>`DescribeTrustStores`                                                  | 40              | 10                       |

**†** Fractional refill rates require several seconds to generate one full token.

## Monitoring API requests

You can use AWS CloudTrail to monitor your Elastic Load Balancing API requests. For more information, see
[Log API calls for Elastic Load Balancing using AWS CloudTrail](cloudtrail-logs.md "cloudtrail-logs.md").
