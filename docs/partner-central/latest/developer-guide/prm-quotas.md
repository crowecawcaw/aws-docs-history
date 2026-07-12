The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Quotas for the AWS Partner Central Revenue Measurement API

AWS Partner Central Revenue Measurement API enforces quotas to ensure fair usage and to protect
the service from misuse. Below are the detailed quotas for various API operations.

## API operation quotas

| Type                                    | API operation                          | Quota (per partner account) |
| --------------------------------------- | -------------------------------------- | --------------------------- |
| Read actions                            | GetRevenueAttribution                  | 50 per second               |
| GetRevenueAttributionAllocation         |
| GetRevenueAttributionAllocationsTask    |
| GetMarketplaceRevenueShare              |
| GetMarketplaceRevenueShareAllocation    |
| List actions                            | ListRevenueAttributions                | 10 per second               |
| ListRevenueAttributionAllocations       |
| ListMarketplaceRevenueShares            |
| ListMarketplaceRevenueShareAllocations  |
| ListTagsForResource                     |
| Write actions                           | CreateRevenueAttribution               | 2 per second                |
| UpdateRevenueAttribution                |
| CreateMarketplaceRevenueShare           |
| CreateMarketplaceRevenueShareAllocation |
| UpdateMarketplaceRevenueShareAllocation |
| TagResource                             |
| UntagResource                           |
| Async write actions                     | StartRevenueAttributionAllocationsTask | 1 per second                |

## Understanding and managing quotas

### Rate limiting

When an API rate limit is reached, the service will respond with a
ThrottlingException. To better handle rate limiting, AWS recommends implementing
exponential backoff and retry strategies in your application.

### Requesting a quota increase

If the default quotas do not meet your requirements, you can request a quota
increase through the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard"). The Service Quotas console is a browser-based
interface that you can use to view and manage your service quotas. You can access
Service Quotas from any AWS Management Console page by choosing it on the top navigation bar, or
by searching for Service Quotas in the AWS Management Console.
