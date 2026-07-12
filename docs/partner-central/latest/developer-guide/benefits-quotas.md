The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Quotas for the AWS Partner Central Benefits API

The AWS Partner Central Benefits API has the following quotas.

## Request quotas

Request quotas| API operations | Quota (per AWS account) |
| --- | --- |
| ListBenefits | 20 per second |
| GetBenefit | 20 per second |
| AmendBenefitApplication | 10 per second |
| CancelBenefitApplication | 10 per second |
| CreateBenefitApplication | 10 per second |
| GetBenefitApplication | 20 per second |
| ListBenefitApplications | 30 per second |
| RecallBenefitApplication | 10 per second |
| SubmitBenefitApplication | 10 per second |
| UpdateBenefitApplication | 10 per second |
| GetBenefitAllocation | 20 per second |
| ListBenefitAllocations | 20 per second |
| AssociateBenefitApplicationResource | 10 per second |
| DisassociateBenefitApplicationResource | 10 per second |

## Additional quotas

Additional quotas| Display name | Catalog | Description | Default value |
| --- | --- | --- | --- |
| Benefit applications | AWS | The maximum number of benefit applications you can create in the AWS catalog | 10,000 |
| Benefit applications | Sandbox | The maximum number of benefit applications you can create in the Sandbox catalog | 10,000 |

## Understanding and managing quotas

### Rate limiting

When an API rate limit is reached, the service will respond with a
ThrottlingException. To better handle rate limiting, AWS recommends implementing exponential backoff and retry strategies in your application.

### Requesting a quota increase

If the default quotas do not meet your requirements, you can request a quota
increase through the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard"). The Service Quotas console is a browser-based
interface that you can use to view and manage your service quotas. You can access
Service Quotas from any AWS Management Console page by choosing it on the top navigation bar, or
by searching for Service Quotas in the AWS Management Console.
