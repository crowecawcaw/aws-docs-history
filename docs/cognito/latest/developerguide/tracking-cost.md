

# Monitoring and managing costs
<a name="tracking-cost"></a>

Like with any other AWS service, it's important to understand the effect of your Amazon Cognito configuration and usage on your AWS bill. As part of your preparations for the deployment of user pools to production, set up monitoring and safeguards for activity and resource consumption. When you know where to look and what actions produce additional cost, you can set up precautions against surprises in your bill.

Amazon Cognito charges for the following dimensions of your usage.
+ User pool monthly active users (MAUs)—rate varies by [feature plan](cognito-sign-in-feature-plans.md)
+ User pool MAUs signed in with OIDC or SAML federation
+ Request volume for machine to machine (M2M) authorization, from both `client_credentials` grants at the token endpoint and the `GetClientToken` API operation
+ Purchased usage above default quotas for some categories of user pool APIs

Additionally, features of your user pool like email messages, SMS messages, and Lambda triggers can incur costs in dependent services. For a complete overview, see [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing).

## Viewing and anticipating costs
<a name="tracking-cost-monitoring"></a>

High-volume events like product launches and opening up to new userbases can increase your MAU count and have a cost impact. Estimate the new user count in advance and watch activity as it happens. You might find that you want to accommodate the volume with a purchase of additional quota capacity, or control the volume with additional security measures.

You can view and report on your AWS costs in the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/home). You can find your most recent charges for Amazon Cognito in the **Billing and payments** section. Under **Bills**, **Charges by service**, filter on `Cognito` to view your usage. For more information, see [Viewing your bill](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/getting-viewing-bill.html) in the *AWS Billing User Guide*.

To monitor API request rates, review the **Utilization** metric in the Service Quotas console. For example, both `client_credentials` grant requests to the token endpoint and [GetClientToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetClientToken.html) API requests display as **Rate of ClientAuthentication requests**, because they share a request quota. In your bill, these requests are associated with the app client that produced them. With this information, you can equitably allocate costs to the tenants in a [multi-tenant architecture](multi-tenant-application-best-practices.md).

To get a count of token-endpoint M2M requests for a period of time, you can also send [AWS CloudTrail events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html) for analysis. Query your CloudTrail events for `Token_POST` events with a client credentials grant. The following CloudWatch Insights query returns this count. To include M2M requests that you make with the `GetClientToken` API operation, use the **Rate of ClientAuthentication requests** utilization metric described earlier in this section.

```
filter eventName = "Token_POST" and @message like '"grant_type":["client_credentials"]' | stats count(*)
```

## Managing costs
<a name="tracking-cost-managing"></a>

Amazon Cognito bills based on user count, feature usage, and request volume. The following are some tips to manage cost in Amazon Cognito,

**Don't activate inactive users**  
Typical operations that make a user active are sign-in, sign-up, and password reset. For a more thorough list, see [Monthly active users](quotas.md#monthly-active-users). Amazon Cognito doesn't count inactive users toward your bill. Avoid any operations that set a user active. Instead of the [AdminGetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.html) API operation, query users with the [ListUsers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html) operation. Don't perform high-volume administrative testing of user pool operations with inactive users.

**Link federated users**  
Users who sign in with a SAML 2.0 or OpenID Connect (OIDC) identity provider have a higher cost than [local users](cognito-terms.md#terms-localuser). You can [link these users to a local user profile](cognito-user-pools-identity-federation-consolidate-users.md). A linked user can sign in as a local user with the attributes and access that come with their federated user. Users from SAML or OIDC IdPs who, in the course of a month, only sign in with a linked local account are billed as local users.

**Manage request rates**  
If your user pool is approaching the upper limit of your quota, you might consider purchasing additional capacity to handle the volume. You might be able to reduce the volume of requests in your application. For more information, see [Optimize request rates for quota limits](quotas.md#optimize-quotas).

**Request a new token only when you need one**  
Machine to machine (M2M) authorization with client credentials grants can reach a high volume of token requests. Each new token request has an effect on your request-rate quota and the size of your bill. To optimize cost, include token expiration settings and token handling in the design of your applications.
+ [Cache access tokens](amazon-cognito-user-pools-using-tokens-caching-tokens.md) so that when your application requests a new token, it receives a cached version of a previously-issued token. When you implement this method, your caching proxy acts as a guard against applications that request access tokens without awareness of the expiration of previously-acquired tokens. Caching tokens is ideal for short-lived microservices like Lambda functions and Docker containers.
+ Implement token-handling mechanisms in your applications that account for token expiration. Don’t request a new token until previous tokens are about to expire. As a best practice, refresh tokens at about 75% of the token lifetime. This practice maximizes token duration while ensuring user continuity in your application.

  Evaluate the confidentiality and availability needs of each application and configure the user pool app client to issue access tokens with an appropriate validity period. Custom token duration works best with longer-lived APIs and servers that can persistently manage the frequency of requests for credentials.

**ListUsers, not AdminGetUser**  
To query the attributes of users in your user pool, use the [ListUsers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html) API operation and associated [SDK](https://aws.amazon.com/developer/tools/) methods when possible. [AdminGetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.html) marks a user as active for the month and contributes to the monthly active users (MAUs) that are used to calculate your bill for user pools.

**Manage feature plans**  
When you choose a [feature plan](cognito-sign-in-feature-plans.md) in a user pool, the billing rate applies to all MAUs in the user pool. If you have users that don't need features that come with a higher-level feature plan, separate them into another user pool.