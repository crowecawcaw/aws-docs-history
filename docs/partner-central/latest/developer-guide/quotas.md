

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Quotas for the AWS Partner Central Selling API
<a name="quotas"></a>

AWS Partner Central selling API enforces quotas to ensure fair usage and to protect the service from misuse. Below are the detailed quotas for various API operations and associations per opportunity.

## API operation quotas
<a name="api-operation-quotas"></a>



- **Read actions**
  - **API operation:**
    - GetOpportunity
    - GetAwsOpportunitySummary
    - ListOpportunities
    - ListSolutions
    - GetEngagementInvitation
    - ListEngagementInvitations
  - **Quota (per partner account):** 10 per second; 100,000 per 24 hours

- **Prospecting read actions**
  - **API operation:** GetProspectingFromEngagementTask
  - **Quota (per partner account):** 100 per second

- **Prospecting read actions**
  - **API operation:** ListProspectingFromEngagementTasks
  - **Quota (per partner account):** 50 per second

- **Write actions**
  - **API operation:**
    - CreateOpportunity
    - UpdateOpportunity
    - AssociateOpportunity
    - DisassociateOpportunity
    - RejectEngagementInvitation
    - AssignOpportunity
    - StartEngagementFromOpportunityTask 
    - StartEngagementByAcceptingInvitationTask
  - **Quota (per partner account):** 1 per second; 10,000 per 24 hours

- **Prospecting write actions**
  - **API operation:** StartProspectingFromEngagementTask
  - **Quota (per partner account):** 2 per second

- **Engagement write actions**
  - **API operation:** CreateEngagement
  - **Quota (per partner account):** 15 per second



## Association quotas per opportunity
<a name="association-quotas-per-opportunity"></a>


| Related entity | Quota | 
| --- | --- | 
| AWS products | 20 per opportunity | 
| Partner Solutions | 10 per opportunity | 
| AWS Marketplace solutions | 10 per opportunity | 
| AWS Marketplace products | 10 per opportunity | 
| AWS Marketplace private offers | 1 per opportunity | 

## Understanding and managing quotas
<a name="understanding-and-managing-quotas"></a>

### Rate limiting
<a name="rate-limiting"></a>

When an API rate limit is reached, the service will respond with a ThrottlingException. To better handle rate limiting, AWS recommends implementing exponential backoff and retry strategies in your application.

### Time window for quotas
<a name="time-window-for-quotas"></a>

The daily quotas reset on a rolling 24 hour period. Your requests would be throttled e.g. if you have performed 10,000 write actions in the last 24 hours and are trying to perform the 10,001st request. Ensure that your application's usage patterns take this into account to prevent unintentional throttling.

### Requesting a quota increase
<a name="requesting-a-quota-increase"></a>

If the default quotas do not meet your requirements, you can request a quota increase through the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard). The Service Quotas console is a browser-based interface that you can use to view and manage your service quotas. You can access Service Quotas from any AWS Management Console page by choosing it on the top navigation bar, or by searching for Service Quotas in the AWS Management Console.