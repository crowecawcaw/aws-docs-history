

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Quotas for the AWS Partner Central Account API
<a name="account-quotas"></a>

The AWS Partner Central Account API has the following quotas.

## Additional quotas
<a name="account-additional-quotas"></a>

The following table lists the Account API quotas. To request a quota increase, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard).


**Additional quotas**  

| Display name | Description | AWS catalog default | Sandbox catalog default | 
| --- | --- | --- | --- | 
| Open connection invitations per account | The maximum number of open connection invitations you can maintain with partner accounts. | 1,000 | 1,000 | 
| Active connections per account | The maximum number of active connections you can maintain with partner accounts. | 1,000 | 1,000 | 
| Email domains per partner | The maximum number of email domains that can be associated with a partner account for AWS training certification. | 50 | 50 | 
| Rate of connection invitations per account | The maximum number of connection invitations per day that you can send. | 50 | 50 | 
| Rate of profile update tasks per account | The maximum number of profile update tasks per day that you can initiate. | 10 | 10 | 
| Rate of profile visibility updates per account | The maximum number of profile visibility updates per day that you can initiate. | 5 | 5 | 
| Rate of email verification codes per email address | The maximum number of email verification codes per day that you can request. | 5 | Not applicable. The Sandbox catalog doesn't send emails. | 
| Items per business plan | The maximum number of business plan items (goals, key performance indicators, initiatives, and activities combined) in one business plan. Adjustable. | 500 | 500 | 
| Attachments per business plan | The maximum number of attachments in one business plan, including imports in progress. Adjustable. | 100 | 100 | 
| Rate of business plans per account per year | The maximum number of business plans you can create per year. Adjustable. | 50 | 50 | 

## Understanding and managing quotas
<a name="understanding-and-managing-quotas"></a>

### Rate limiting
<a name="rate-limiting"></a>

When an API rate limit is reached, the service will respond with a ThrottlingException. To better handle rate limiting, AWS recommends implementing exponential backoff and retry strategies in your application.

### Requesting a quota increase
<a name="requesting-a-quota-increase"></a>

If the default quotas do not meet your requirements, you can request a quota increase through the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard). The Service Quotas console is a browser-based interface that you can use to view and manage your service quotas. You can access Service Quotas from any AWS Management Console page by choosing it on the top navigation bar, or by searching for Service Quotas in the AWS Management Console.