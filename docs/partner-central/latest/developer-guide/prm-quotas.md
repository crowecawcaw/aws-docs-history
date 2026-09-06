

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Quotas for the AWS Partner Central Revenue Measurement API
<a name="prm-quotas"></a>

AWS Partner Central Revenue Measurement API enforces quotas to ensure fair usage and to protect the service from misuse. Below are the detailed quotas for various API operations.

## API operation quotas
<a name="prm-api-operation-quotas"></a>



- **Read actions**
  - **API operation:**
    - GetRevenueAttribution
    - GetRevenueAttributionAllocation
    - GetRevenueAttributionAllocationsTask
    - GetMarketplaceRevenueShare
    - GetMarketplaceRevenueShareAllocation
  - **Quota (per partner account):** 50 per second

- **List actions**
  - **API operation:**
    - ListRevenueAttributions
    - ListRevenueAttributionAllocations
    - ListMarketplaceRevenueShares
    - ListMarketplaceRevenueShareAllocations
    - ListTagsForResource
  - **Quota (per partner account):** 10 per second

- **Write actions**
  - **API operation:**
    - CreateRevenueAttribution
    - UpdateRevenueAttribution
    - CreateMarketplaceRevenueShare
    - CreateMarketplaceRevenueShareAllocation
    - UpdateMarketplaceRevenueShareAllocation
    - TagResource
    - UntagResource
  - **Quota (per partner account):** 2 per second

- **Async write actions**
  - **API operation:** StartRevenueAttributionAllocationsTask
  - **Quota (per partner account):** 1 per second



## Understanding and managing quotas
<a name="prm-understanding-and-managing-quotas"></a>

### Rate limiting
<a name="prm-rate-limiting"></a>

When an API rate limit is reached, the service will respond with a ThrottlingException. To better handle rate limiting, AWS recommends implementing exponential backoff and retry strategies in your application.

### Requesting a quota increase
<a name="prm-requesting-a-quota-increase"></a>

If the default quotas do not meet your requirements, you can request a quota increase through the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard). The Service Quotas console is a browser-based interface that you can use to view and manage your service quotas. You can access Service Quotas from any AWS Management Console page by choosing it on the top navigation bar, or by searching for Service Quotas in the AWS Management Console.