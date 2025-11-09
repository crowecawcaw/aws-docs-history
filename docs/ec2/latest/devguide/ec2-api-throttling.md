# Request throttling for the Amazon EC2 API

Amazon EC2 throttles EC2 API requests for each AWS account on a per-Region basis. We do this
to help the performance of the service, and to ensure fair usage for all Amazon EC2 customers.
Throttling ensures that requests to the Amazon EC2 API do not exceed the maximum allowed API request
limits. API requests are subject to the request limits whether they originate from:

- A third-party application
- A command line tool
- The Amazon EC2 console
  If you exceed an API throttling limit, you get the `RequestLimitExceeded` error
  code.

###### Contents

- [How throttling is applied](#throttling-how "#throttling-how")
- [Request token limits](#throttling-limits-rate-based "#throttling-limits-rate-based")
- [Resource token limits](#throttling-limits-cost-based "#throttling-limits-cost-based")
- [Monitor API throttling](#throttling-monitor "#throttling-monitor")
- [Retries and exponential backoff](#api-backoff "#api-backoff")
- [Request a limit increase](#throttling-increase "#throttling-increase")

## How throttling is applied

Amazon EC2 uses the [token bucket
algorithm](https://en.wikipedia.org/wiki/Token_bucket "https://en.wikipedia.org/wiki/Token_bucket") to implement API throttling. With this algorithm, your account has
a _bucket_ that holds a specific number of
_tokens_. The number of tokens in the bucket represents your
throttling limit at any given second.

Amazon EC2 implements two types of API throttling:

###### API throttling types

- [Request rate limiting](#throttling-rate-based "#throttling-rate-based")
- [Resource rate limiting](#throttling-cost-based "#throttling-cost-based")

### Request rate limiting

With request rate limiting, each API is evaluated individually, and you are
throttled on the number of requests you make on a per-API basis. Each request
that you make removes one token from the API's bucket. For example, the token
bucket size for `DescribeHosts`, a _non-mutating_  
 API action, is 100 tokens. You can make up to 100 `DescribeHosts`
requests in one second. If you exceed 100 requests in a second, you are throttled
on that API and the remaining requests within that second fail, however, requests
for other API are not affected.

Buckets automatically refill at a set rate. If the bucket is below its maximum
capacity, a set number of tokens is added back to it every second until it reaches
its maximum capacity. If the bucket is full when refill tokens arrive, they are
discarded. The bucket can't hold more than its maximum number of tokens. For
example, the bucket size for `DescribeHosts`, a _non-mutating_
API action, is 100 tokens and the refill rate is 20 tokens per second. If you
make 100 `DescribeHosts` requests in one second, the bucket is reduced
to zero (0) tokens. The bucket is then refilled by 20 tokens every second, until
it reaches its maximum capacity of 100 tokens. This means that an empty bucket
reaches its maximum capacity after 5 seconds if no requests are made during that
time.

You do not need to wait for the bucket to be completely full before you can make
API requests. You can use refill tokens as they are added to the bucket. If you
immediately use the refill tokens, the bucket does not reach its maximum capacity.
For example, the bucket size for `DescribeHosts`, a _non-mutating_
API action, is 100 tokens and the refill rate is 20 tokens per second. If you
deplete the bucket by making 100 API requests in a second, you can continue to
make 20 API requests per second by using the refill tokens as they are added to the
bucket. The bucket can refill to the maximum capacity only if you make fewer than
20 API requests per second.

For more information, see [Request token bucket sizes and refill rates](#throttling-limits-rate-based "#throttling-limits-rate-based").

### Resource rate limiting

Some API actions, such as `RunInstances` and `TerminateInstances`, as
described in the table that follows, use resource rate limiting in addition to
request rate limiting. These API actions have a separate resource token bucket that
depletes based on the number of resources that are impacted by the request. Like
request token buckets, resource token buckets have a bucket maximum that allows you
to burst, and a refill rate that allows you to sustain a steady rate of requests for
as long as needed. If you exceed a specific bucket limit for an API, including when
a bucket has not yet refilled to support the next API request, the action of the API is
limited even though you have not reached the total API throttle limit.

For example, the resource token bucket size for `RunInstances` is 1000
tokens, and the refill rate is two tokens per second. Therefore, you can immediately
launch 1000 instances, using any number of API requests, such as one request for
1000 instances or four requests for 250 instances. After the resource token bucket
is empty, you can launch up to two instances every second, using either one request
for two instances or two requests for one instance.

For more information, see [Resource token bucket sizes and refill rates](#throttling-limits-cost-based "#throttling-limits-cost-based").

## Request token bucket sizes and refill rates

For request rate limiting purposes, API actions are grouped into the following
categories:

- **Non-mutating actions** — API actions
  that retrieve data about resources. This category generally includes all `Describe*`,
  `List*`, `Search*`, and `Get*` API actions, such as
  `DescribeRouteTables`, `SearchTransitGatewayRoutes`, and
  `GetIpamPoolCidrs`. These API actions typically have the highest API
  throttling limits.
- **Unfiltered and unpaginated non-mutating actions** —
  A specific subset of non-mutating API actions that, when requested without specifying either
  [pagination](../../../cli/latest/userguide/cli-usage-pagination.md "../../../cli/latest/userguide/cli-usage-pagination.md")
  or a [filter](../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI "../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI"),
  use tokens from a smaller token bucket. It is recommended that you make use of pagination
  and filtering so that tokens are deducted from the standard (larger) token bucket.
- **Mutating actions** — API actions that create, modify,
  or delete resources. This category generally includes all API actions that are not categorized
  as _non-mutating actions_, such as `AllocateHosts`, `ModifyHosts`,
  and `CreateCapacityReservation`. These actions have a lower throttling limit than
  non-mutating API actions.
- **Resource-intensive actions** — Mutating API actions
  that take the most time and consume the most resources to complete. These actions have an
  even lower throttling limit than _mutating actions_. They are throttled
  separately from other _mutating actions_.
- **Console non-mutating actions** — Non-mutating API
  actions that are requested from the Amazon EC2 console. These API actions are throttled separately
  from other non-mutating API actions.
- **Uncategorized actions** — These are API actions that
  receive their own token bucket sizes and refill rates, even though by definition they fit in
  one of the other categories.

| API action category                                 | Actions                                                                                                                                                                                                                                                                                        | Bucket maximum capacity | Bucket refill rate |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------ |
| **Non-mutating actions**                            | The `Describe*`, `List*`, `Search*`, and<br>`Get*` API actions that are not included in another category.                                                                                                                                                                                      | 100                     | 20                 |
| **Unfiltered and unpaginated non-mutating actions** | • `DescribeInstances`<br>• `DescribeInstanceStatus`<br>• `DescribeNetworkInterfaces`<br>• `DescribeSecurityGroups`<br>• `DescribeSnapshots`<br>• `DescribeSpotInstanceRequests`<br>• `DescribeVolumes`                                                                                         | 50                      | 10                 |
| **Mutating actions**                                | All mutating API actions that are not _Resource-intensive actions_<br>or _Uncategorized actions_.                                                                                                                                                                                              | 50                      | 5                  |
| **Resource-intensive actions**                      | • `AcceptVpcPeeringConnection`<br>• `AuthorizeSecurityGroupIngress`<br>• `CancelSpotInstanceRequests`<br>• `CreateKeyPair`<br>• `CreateVpcPeeringConnection`<br>• `DeleteVpcPeeringConnection`<br>• `RejectVpcPeeringConnection`<br>• `RevokeSecurityGroupIngress`<br>• `RequestSpotInstances` | 50                      | 5                  |
| **Console non-mutating actions**                    | The `Describe*`, `List*`, `Search*`,<br>and `Get*` API actions, that are called by the Amazon EC2 console,<br>but not included in another category.                                                                                                                                            | 100                     | 10                 |

| Uncategorized actions                                 | Bucket maximum capacity | Bucket refill rate |
| ----------------------------------------------------- | ----------------------- | ------------------ |
| `AcceptVpcEndpointConnections`                        | 10                      | 1                  |
| `AdvertiseByoipCidr`                                  | 1                       | 0.1                |
| `AssignIpv6Addresses`                                 | 100                     | 5                  |
| `AssignPrivateIpAddresses`                            | 100                     | 5                  |
| `AssignPrivateNatGatewayAddress`                      | 10                      | 1                  |
| `AssociateCapacityReservationBillingOwner`            | 1                       | 0.5                |
| `AssociateEnclaveCertificateIamRole`                  | 10                      | 1                  |
| `AssociateIamInstanceProfile`                         | 100                     | 5                  |
| `AssociateNatGatewayAddress`                          | 10                      | 1                  |
| `AttachVerifiedAccessTrustProvider`                   | 10                      | 2                  |
| `AuthorizeClientVpnIngress`                           | 5                       | 2                  |
| `CancelDeclarativePoliciesReport`                     | 1                       | 1                  |
| `CopyImage`                                           | 100                     | 1                  |
| `CreateClientVpnRoute`                                | 5                       | 2                  |
| `CreateCoipCidr`                                      | 5                       | 1                  |
| `CreateCoipPool`                                      | 5                       | 1                  |
| `CreateDefaultSubnet`                                 | 1                       | 1                  |
| `CreateDefaultVpc`                                    | 1                       | 1                  |
| `CreateLaunchTemplateVersion`                         | 100                     | 5                  |
| `CreateNatGateway`                                    | 10                      | 1                  |
| `CreateNetworkInterface`                              | 100                     | 5                  |
| `CreateRestoreImageTask`                              | 50                      | 0.1                |
| `CreateSnapshot`                                      | 100                     | 5                  |
| `CreateSnapshots`                                     | 100                     | 5                  |
| `CreateSpotDatafeedSubscription`                      | 50                      | 3                  |
| `CreateStoreImageTask`                                | 50                      | 0.1                |
| `CreateSubnetCidrReservation`                         | 5                       | 1                  |
| `CreateTags`                                          | 100                     | 10                 |
| `CreateVerifiedAccessEndpoint`                        | 20                      | 4                  |
| `CreateVerifiedAccessGroup`                           | 10                      | 2                  |
| `CreateVerifiedAccessInstance`                        | 10                      | 2                  |
| `CreateVerifiedAccessTrustProvider`                   | 10                      | 2                  |
| `CreateVolume`                                        | 100                     | 5                  |
| `CreateVpcEndpoint`                                   | 4                       | 0.3                |
| `CreateVpcEndpointServiceConfiguration`               | 10                      | 1                  |
| `DeleteClientVpnRoute`                                | 5                       | 2                  |
| `DeleteCoipCidr`                                      | 5                       | 1                  |
| `DeleteCoipPool`                                      | 5                       | 1                  |
| `DeleteCoipPoolPermission`                            | 5                       | 1                  |
| `DeleteNatGateway`                                    | 10                      | 1                  |
| `DeleteNetworkInterface`                              | 100                     | 5                  |
| `DeleteSnapshot`                                      | 100                     | 5                  |
| `DeleteSpotDatafeedSubscription`                      | 50                      | 3                  |
| `DeleteSubnetCidrReservation`                         | 5                       | 1                  |
| `DeleteQueuedReservedInstances`                       | 5                       | 5                  |
| `DeleteTags`                                          | 100                     | 10                 |
| `DeleteVerifiedAccessEndpoint`                        | 20                      | 4                  |
| `DeleteVerifiedAccessGroup`                           | 10                      | 2                  |
| `DeleteVerifiedAccessInstance`                        | 10                      | 2                  |
| `DeleteVerifiedAccessTrustProvider`                   | 10                      | 2                  |
| `DeleteVolume`                                        | 100                     | 5                  |
| `DeleteVpcEndpoints`                                  | 4                       | 0.3                |
| `DeleteVpcEndpointServiceConfigurations`              | 10                      | 1                  |
| `DeprovisionByoipCidr`                                | 1                       | 0.1                |
| `DeregisterImage`                                     | 100                     | 5                  |
| `DescribeAggregateIdFormat`                           | 10                      | 10                 |
| `DescribeByoipCidrs`                                  | 1                       | 0.5                |
| `DescribeCapacityBlockExtensionOfferings`             | 10                      | 0.15               |
| `DescribeCapacityBlockOfferings`                      | 10                      | 0.15               |
| `DescribeDeclarativePoliciesReports`                  | 5                       | 5                  |
| `DescribeHostReservations`                            | 5                       | 2                  |
| `DescribeHostReservationOfferings`                    | 5                       | 2                  |
| `DescribeIdentityIdFormat`                            | 10                      | 10                 |
| `DescribeIdFormat`                                    | 10                      | 10                 |
| `DescribeInstanceTopology`                            | 1                       | 1                  |
| `DescribeMovingAddresses`                             | 1                       | 1                  |
| `DescribePrincipalIdFormat`                           | 10                      | 10                 |
| `DescribeReservedInstancesOfferings`                  | 10                      | 10                 |
| `DescribeSecurityGroupReferences`                     | 20                      | 5                  |
| `DescribeSpotDatafeedSubscription`                    | 100                     | 13                 |
| `DescribeSpotFleetInstances`                          | 100                     | 5                  |
| `DescribeSpotFleetRequestHistory`                     | 100                     | 5                  |
| `DescribeSpotFleetRequests`                           | 50                      | 3                  |
| `DescribeStaleSecurityGroups`                         | 20                      | 5                  |
| `DescribeStoreImageTasks`                             | 50                      | 0.5                |
| `DescribeVerifiedAccessInstanceLoggingConfigurations` | 10                      | 2                  |
| `DetachVerifiedAccessTrustProvider`                   | 10                      | 2                  |
| `DisableFastLaunch`                                   | 5                       | 2                  |
| `DisableImageBlockPublicAccess`                       | 1                       | 0.1                |
| `DisableSnapshotBlockPublicAccess`                    | 1                       | 0.1                |
| `DisassociateCapacityReservationBillingOwner`         | 1                       | 0.5                |
| `DisassociateEnclaveCertificateIamRole`               | 10                      | 1                  |
| `DisassociateIamInstanceProfile`                      | 100                     | 5                  |
| `DisassociateNatGatewayAddress`                       | 10                      | 1                  |
| `EnableFastLaunch`                                    | 5                       | 2                  |
| `EnableImageBlockPublicAccess`                        | 1                       | 0.1                |
| `EnableSnapshotBlockPublicAccess`                     | 1                       | 0.1                |
| `GetAssociatedEnclaveCertificateIamRoles`             | 10                      | 1                  |
| `GetDeclarativePoliciesReportSummary`                 | 5                       | 5                  |
| `GetHostReservationPurchasePreview`                   | 5                       | 2                  |
| `ModifyImageAttribute`                                | 100                     | 5                  |
| `ModifyInstanceMetadataDefaults`                      | 2                       | 2                  |
| `ModifyInstanceMetadataOptions`                       | 100                     | 5                  |
| `ModifyLaunchTemplate`                                | 100                     | 5                  |
| `ModifyNetworkInterfaceAttribute`                     | 100                     | 5                  |
| `ModifySnapshotAttribute`                             | 100                     | 5                  |
| `ModifyVerifiedAccessEndpoint`                        | 20                      | 4                  |
| `ModifyVerifiedAccessEndpointPolicy`                  | 20                      | 4                  |
| `ModifyVerifiedAccessGroup`                           | 10                      | 2                  |
| `ModifyVerifiedAccessGroupPolicy`                     | 20                      | 4                  |
| `ModifyVerifiedAccessInstance`                        | 10                      | 2                  |
| `ModifyVerifiedAccessInstanceLoggingConfiguration`    | 10                      | 2                  |
| `ModifyVerifiedAccessTrustProvider`                   | 10                      | 2                  |
| `ModifyVpcEndpoint`                                   | 4                       | 0.3                |
| `ModifyVpcEndpointServiceConfiguration`               | 10                      | 1                  |
| `MoveAddressToVpc`                                    | 1                       | 1                  |
| `ProvisionByoipCidr`                                  | 1                       | 0.1                |
| `PurchaseCapacityBlock`                               | 10                      | 0.15               |
| `PurchaseCapacityBlockExtension`                      | 10                      | 0.15               |
| `PurchaseHostReservation`                             | 5                       | 2                  |
| `PurchaseReservedInstancesOffering`                   | 5                       | 5                  |
| `RejectVpcEndpointConnections`                        | 10                      | 1                  |
| `RestoreAddressToClassic`                             | 1                       | 1                  |
| `RevokeClientVpnIngress`                              | 5                       | 2                  |
| `RunInstances`                                        | 5                       | 2                  |
| `StartDeclarativePoliciesReport`                      | 1                       | 1                  |
| `StartInstances`                                      | 5                       | 2                  |
| `TerminateInstances`                                  | 100                     | 5                  |
| `UnassignPrivateIpAddresses`                          | 100                     | 5                  |
| `UnassignPrivateNatGatewayAddress`                    | 10                      | 1                  |
| `WithdrawByoipCidr`                                   | 1                       | 0.1                |

## Resource token bucket sizes and refill rates

The following table lists the resource token bucket sizes and refill rates for API
actions that use resource rate limiting.

| API action           | Bucket maximum capacity | Bucket refill rate |
| -------------------- | ----------------------- | ------------------ |
| `RunInstances`       | 1000                    | 2                  |
| `TerminateInstances` | 1000                    | 20                 |
| `StartInstances`     | 1000                    | 2                  |
| `StopInstances`      | 1000                    | 20                 |

## Monitor API throttling

You can use Amazon CloudWatch to monitor your Amazon EC2 API requests and to collect and track metrics
around API throttling. You can also create an alarm to warn you when you are close to
reaching the API throttling limits. For more information, see [Monitor Amazon EC2 API requests using Amazon CloudWatch](monitor.md "monitor.md").

## Retries and exponential backoff

Your application might need to retry an API request. For example:

- To check for an update in the status of a resource
- To enumerate a large number of resources (for example, all your volumes)
- To retry a request after it fails with a server error (5xx) or a throttling error

However, for a client error (4xx), you must revise the request to correct the problem
before trying the request again.

###### Resource status changes

Before you start polling to check for status updates, give the request time
to potentially complete. For example, wait a few minutes before checking whether your
instance is active. When you begin polling, use an appropriate sleep interval
between successive requests to lower the rate of API requests. For best results,
use an increasing or variable sleep interval.

Alternatively, you can use Amazon EventBridge to notify you of the status of some resources.
For example, you can use the **EC2 Instance State-change
Notification** event to notify you of a state change for an
instance. For more information, see [Automate Amazon EC2 using EventBridge](../../../AWSEC2/latest/UserGuide/automating_with_eventbridge.md "../../../AWSEC2/latest/UserGuide/automating_with_eventbridge.md").

###### Retries

When you need to poll or retry an API request, we recommend using an
exponential backoff algorithm to calculate the sleep interval between API requests.
The idea behind exponential backoff is to use progressively longer waits between
retries for consecutive error responses. You should implement a maximum delay interval,
as well as a maximum number of retries. You can also use jitter (randomized delay)
to prevent successive collisions. For more information, see [Timeouts, retries,
and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ "https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/").

Each AWS SDK implements automatic retry logic. For more information, see [Retry behavior](../../../sdkref/latest/guide/feature-retry-behavior.md "../../../sdkref/latest/guide/feature-retry-behavior.md")
in the _AWS SDKs and Tools Reference Guide_.

## Request a limit increase

You can request an increase for API throttling limits for your AWS account.

###### Recommendations

- Request at most three times your existing limit in a single request.
- Prioritize increasing bucket refill rates before increasing bucket maximum capacity.
- If the requested bucket refill rate would exceed the bucket maximum capacity, increase
  the bucket maximum capacity at the same time.
- Provide all API actions that require an increase. Limits are applied to individual
  API actions, not API action categories.
- There are both request rate and resource rate limits for the following API actions:
  `RunInstances`, `StartInstances`, `StopInstances`,
  and `TerminateInstances`. Be sure to indicate which limit should be
  increased

###### To request access to this feature

1. Open [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
2. Choose **Create case**.
3. Choose **Account and billing**.
4. For **Service**, choose **General Info and Getting Started**.
5. For **Category**, choose **Using AWS & Services**.
6. Choose **Next step: Additional information**.
7. For **Subject**, enter `Request an increase in my Amazon EC2 API
throttling limits`.
8. For **Description**, copy the following template and provide the required
   information.

```
Please increase the API throttling limits for my account.
Related page: https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-throttling.html
Description: `Brief notes about your use case. If available, include the IDs
 of a few Amazon EC2 requests that were throttled.`
Time window: `One-hour window when peak throttling or usage occurred.`
`region_1` request rate increases:
    `action`: `new_bucket_maximum_capacity`
    `action`: `new_bucket_refill_rate`
    `action`: `new_bucket_maximum_capacity`|`new_bucket_refill_rate`
`region_1` resource rate increases:
    `action`: `new_bucket_maximum_capacity`
    `action`: `new_bucket_refill_rate`
    `action`: `new_bucket_maximum_capacity`|`new_bucket_refill_rate`
`region_2` request rate increases:
    `action`: `new_bucket_maximum_capacity`
    `action`: `new_bucket_refill_rate`
    `action`: `new_bucket_maximum_capacity`|`new_bucket_refill_rate`
`region_2` resource rate increases:
    `action`: `new_bucket_maximum_capacity`
    `action`: `new_bucket_refill_rate`
    `action`: `new_bucket_maximum_capacity`|`new_bucket_refill_rate`
```

9. Choose **Next step: Solve now or contact us**.
10. On the **Contact us** tab, choose your preferred contact language
    and method of contact.
11. Choose **Submit**.
