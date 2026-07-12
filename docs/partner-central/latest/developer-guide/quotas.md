The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Quotas for the AWS Partner Central Selling API

AWS Partner Central selling API enforces quotas to ensure fair usage and to protect the service from
misuse. Below are the detailed quotas for various API operations and associations per
opportunity.

## API operation quotas

| Type                                     | API operation                      | Quota (per partner account)            |
| ---------------------------------------- | ---------------------------------- | -------------------------------------- |
| Read actions                             | GetOpportunity                     | 10 per second; 100,000 per 24<br>hours |
| GetAwsOpportunitySummary                 |
| ListOpportunities                        |
| ListSolutions                            |
| GetEngagementInvitation                  |
| ListEngagementInvitations                |
| Prospecting read actions                 | GetProspectingFromEngagementTask   | 100 per second                         |
| Prospecting read actions                 | ListProspectingFromEngagementTasks | 50 per second                          |
| Write actions                            | CreateOpportunity                  | 1 per second; 10,000 per 24<br>hours   |
| UpdateOpportunity                        |
| AssociateOpportunity                     |
| DisassociateOpportunity                  |
| RejectEngagementInvitation               |
| AssignOpportunity                        |
| StartEngagementFromOpportunityTask       |
| StartEngagementByAcceptingInvitationTask |
| Prospecting write actions                | StartProspectingFromEngagementTask | 2 per second                           |
| Engagement write actions                 | CreateEngagement                   | 15 per second                          |

## Association quotas per opportunity

| Related entity                 | Quota              |
| ------------------------------ | ------------------ |
| AWS products                   | 20 per opportunity |
| Partner Solutions              | 10 per opportunity |
| AWS Marketplace solutions      | 10 per opportunity |
| AWS Marketplace products       | 10 per opportunity |
| AWS Marketplace private offers | 1 per opportunity  |

## Understanding and managing quotas

### Rate limiting

When an API rate limit is reached, the service will respond with a
ThrottlingException. To better handle rate limiting, AWS recommends implementing exponential backoff and retry strategies in your application.

### Time window for quotas

The daily quotas reset on a rolling 24 hour period. Your requests would be
throttled e.g. if you have performed 10,000 write actions in the last 24 hours and
are trying to perform the 10,001st request. Ensure that your application's usage
patterns take this into account to prevent unintentional throttling.

### Requesting a quota increase

If the default quotas do not meet your requirements, you can request a quota
increase through the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard"). The Service Quotas console is a browser-based
interface that you can use to view and manage your service quotas. You can access
Service Quotas from any AWS Management Console page by choosing it on the top navigation bar, or
by searching for Service Quotas in the AWS Management Console.
