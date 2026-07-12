The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Quotas for the AWS Partner Central Account API

The AWS Partner Central Account API has the following quotas.

## Additional quotas

Additional quotas| Display name | Catalog | Description | Default value |
| --- | --- | --- | --- |
| Open connection invitations per account | AWS | The maximum number of open connection invitations you can maintain with partner accounts in the AWS catalog | 1,000 |
| Active connections per account | AWS | The maximum number of active connections you can maintain with partner accounts in the AWS catalog | 1,000 |
| Email domains per partner | AWS | The maximum number of email domains that can be associated with a partner account for AWS training certification in the AWS catalog | 50 |
| Rate of connection invitations per account | AWS | The maximum number of connection invitations per day that you can send in the AWS catalog | 50 |
| Rate of profile update tasks per account | AWS | The maximum number of profile update tasks per day that you can initiate in the AWS catalog | 10 |
| Rate of profile visibility updates per account | AWS | The maximum number of profile visibility updates per day that you can initiate in the AWS catalog | 5 |
| Rate of email verification codes per email address | AWS | The maximum number of email verification codes per day that you can request in the AWS catalog | 5 |
| Open connection invitations per account | Sandbox | The maximum number of open connection invitations you can maintain with partner accounts in the Sandbox catalog | 1,000 |
| Active connections per account | Sandbox | The maximum number of active connections you can maintain with partner accounts in the Sandbox catalog | 1,000 |
| Email domains per partner | Sandbox | The maximum number of email domains that can be associated with a partner account for AWS training certification in the Sandbox catalog | 50 |
| Rate of connection invitations per account | Sandbox | The maximum number of connection invitations per day that you can send in the Sandbox catalog | 50 |
| Rate of profile update tasks per account | Sandbox | The maximum number of profile update tasks per day that you can initiate in the Sandbox catalog | 10 |
| Rate of profile visibility updates per account | Sandbox | The maximum number of profile visibility updates per day that you can initiate in the Sandbox catalog | 5 |
| Rate of email verification codes per email address | Sandbox | The maximum number of email verification codes per day that you can request in the Sandbox catalog.<br>No emails are sent from Sandbox catalog. | N/A |

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
