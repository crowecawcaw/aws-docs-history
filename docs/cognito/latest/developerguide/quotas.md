

# Quotas in Amazon Cognito
<a name="quotas"></a>

Amazon Cognito has default quotas, formerly referred to as *limits*, for the maximum number of operations that you can perform in your account. Amazon Cognito also has quotas for the maximum number and size of Amazon Cognito resources.

Each Amazon Cognito quota represents a maximum volume of requests in one AWS Region in one AWS account. For example, your apps can make API requests at *up to* the **Default quota (RPS)** rate for `UserAuthentication` operations against all of your user pools in US East (N. Virginia). Your apps in Asia Pacific (Tokyo) can produce the same volume of requests against all of your user pools in their own Region. AWS can only grant a quota increase request in one Region at a time. A successful quota increase in US East (N. Virginia) has no effect on your maximum request rate in Asia Pacific (Tokyo).

**Topics**
+ [Understanding API request rate quotas](#operation-quotas)
+ [Managing API request rate quotas](#managing-request-rate-quotas)
+ [Amazon Cognito user pools API operation categories and request rate quotas](#category_operations)
+ [Amazon Cognito identity pools (federated identities) API operation request rate quotas](#amazon-cognito-identity-pools-federated-identities-request-rate-quotas)
+ [Quotas on resource number and size](#resource-quotas)

## Understanding API request rate quotas
<a name="operation-quotas"></a>

### Quota categorization
<a name="quota-categorization"></a>

Amazon Cognito enforces a maximum request rate for API operations. For more information about the API operations that Amazon Cognito makes available, see the API reference guides for [user pools](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/Welcome.html) and [identity pools](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html). For user pools, these operations are grouped into categories of common use cases like `UserAuthentication` or `UserCreation`. For a list of user pool API operations by category, see [Amazon Cognito user pools API operation categories and request rate quotas](#category_operations). 

In the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home), you can track your quota usage by category user pools and identity pools.If the request rate of your Amazon Cognito user pools or exceeds a quota, you can purchase additional capacity. You can track your user pool quota usage by category and purchase quota increases in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home).

Operation quotas are defined as the maximum number of requests per second (RPS) for all operations within a category. The Amazon Cognito user pools service applies quotas to all operations in each category. For example, the category `UserCreation` includes four operations: `SignUp`, `ConfirmSignUp`, `AdminCreateUser`, and `AdminConfirmSignUp`. It's allocated with a combined quota of 50 RPS. If multiple operations take place at the same time, each operation within this category can call up to 50 RPS separately or combined. 

**Note**  
Category quotas only apply to user pools. Amazon Cognito applies each identity pool quota to a single operation. For both per-category and per-operation request rate quotas, AWS measures the aggregate rate of all requests from all user pools or identity pools in your AWS account in one Region.

### Amazon Cognito user pools API operations with special request rate handling
<a name="api-operation-special-handling"></a>

Operation quotas are measured and enforced for the combined total requests at the category level, except for the `AdminRespondToAuthChallenge` and `RespondToAuthChallenge` operations, where special handling rules are applied. 

The `UserAuthentication` category includes four operations in the Amazon Cognito user pools API: `AdminInitiateAuth`, `InitiateAuth`, `AdminRespondToAuthChallenge`, and `RespondToAuthChallenge`. Additionally, user authentication in the hosted UI contributes to this quota. The `InitiateAuth` and `AdminInitiateAuth` operations are measured and enforced per category quota. The matching operations `RespondToAuthChallenge` and `AdminRespondToAuthChallenge` are subject to a separate quota that is three times the `UserAuthentication` category limit. This elevated quota accommodates multiple authentication challenges set up in your apps. The quota is sufficient to cover the large majority of use cases. After your app makes up to three responses to authentication challenges, additional requests count toward the `UserAuthentication` category quota. [Multi-factor authentication (MFA)](user-pool-settings-mfa.md#user-pool-settings-mfa.title), [device authentication](amazon-cognito-user-pools-device-tracking.md#amazon-cognito-user-pools-device-tracking.title), and [custom authentication](user-pool-lambda-challenge.md#user-pool-lambda-challenge.title) are all examples of challenge prompts that you might engineer into your user pool.

For example, if your quota for the `UserAuthentication` category is 80 RPS, you can call `RespondToAuthChallenge` or `AdminRespondToAuthChallenge` at a rate up to 240 RPS (3 \* 80 RPS). If your user pool prompts for four rounds of challenge per authentication and 70 users sign in per second, then the total `RespondToAuthChallenge` is 280 RPS (70 x 4), which is 40 RPS above the quota. The extra 40 RPS is added to 70 `InitiateAuth` calls, making the total usage of `UserAuthentication` category 110 RPS (40 \+ 70). Because this value exceeds the category quota set at 80 RPS by 30 RPS, Amazon Cognito throttles requests from your app.

### Monthly active users
<a name="monthly-active-users"></a>

When Amazon Cognito calculates user pool billing, it charges you a rate for each *monthly active user (MAU)*. Consider your current and projected MAU count in your planning for quota increase requests. A user is counted as a MAU if, within a calendar month, there is an identity operation related to that user. When you [link federated users to local users](cognito-user-pools-identity-federation-consolidate-users.md), with SAML or OIDC federation, the local user will count as an enterprise directory MAU or `EnterpriseMAU`, regardless of whether the user signs in directly or via federation. See [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing/) for more information.
+ Sign-up or administrative creation of a user. [User CSV import](cognito-user-pools-using-import-tool.md) *doesn't* contribute to your MAU count.
+ User account confirmation or attribute verification.
+ Sign-in and challenge response. Operations that you authorize with the currently signed-in user's access token don't contribute to your MAU count; however, because sign-in produces access tokens, these operations indicate that the associated user is an MAU.
+ Sign-out and token revocation.
+ Password self-service reset and setting of user passwords as an administrator. *Resetting* user passwords as an administrator ([AdminResetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.html)) doesn't contribute to your MAU count.
+ Change user attributes or group membership.
+ Query detailed attributes of a user as an administrator.

**Note**  
The category *Query detailed attributes of a user as an administrator* includes the API operation [AdminGetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.html), but not [ListUsers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html). A detailed user-by-user query in a large user pool can have a significant impact on your AWS bill. To avoid additional cost, collect user data with `ListUsers` or store user information in an external database.

You aren't charged for additional sessions by any active user, or for any users that weren't active within a calendar month. In a month where you have changed your user pool feature plan between the available options of *Lite*, *Essentials*, and *Plus*, your bill for that month is computed from the sum of monthly active users (MAUs) in each tier, with each MAU assigned to the highest-priced assigned tier when the user was active. For example:

1. At the beginning of the month, your user pool is on the Plus feature plan.

1. User A signs in on the first day of the month.

1. User B signs in on the first and last days of the month.

1. On the tenth day of the month, you switch your feature plan to Essentials.

1. User C signs in on the last day of the month.

In this scenario, user A and user B are Plus MAUs and user C is an Essentials MAU.

**Lite MAU**  
A user that was active at least once in a month when the user pool was on the Lite feature plan, and was never active when the user pool was on the Essentials or Plus plans.

**Essentials MAU**  
A user that was active at least once in a month when the user pool was on the Essentials feature plan, and was never active when the user pool was on the Plus plan.

**Plus MAU**  
A user that was active at least once in a month when the user pool was on the Plus plan.

For more information, see [User pool feature plans](cognito-sign-in-feature-plans.md).

## Managing API request rate quotas
<a name="managing-request-rate-quotas"></a>

### Identify quota requirements
<a name="identify-quota-requirements"></a>

**Important**  
If you increase Amazon Cognito quotas for categories such as `UserAuthentication`, `UserCreation`, or `AccountRecovery`, you may need to increase quotas for other AWS services. For example, messages that Amazon Cognito sends with Amazon Simple Notification Service (Amazon SNS) or Amazon Simple Email Service (Amazon SES) can fail if request rate quotas are insufficient in those services.

To calculate quota requirements, determine how many active users will interact with your application in a specific time period. For example, if you expect your application to sign in an average of one million active users within an eight-hour period, then you must be able to authenticate an average of 35 users per second. 

In addition, if you assume that the average user session is two hours, and you configure tokens to expire after an hour, each user must refresh their tokens once during their session. The required average quota for the `UserAuthentication` category to support this load is 70 RPS.

If you assume a peak-to-average ratio of 3:1 by accounting for the variance of user sign-in frequency during the eight-hour period, then you need the desired `UserAuthentication` quota of 200 RPS. 

**Note**  
If you call multiple operations for each user action, you must sum up the individual operation call rates at the category level.

### Optimize request rates for quota limits
<a name="optimize-quotas"></a>

Because increasing API rate limits adds costs to your AWS bill, consider adjustments to your usage model before you request a quota increase. The following are some examples of app architecture that optimizes request rates.

**Retry the attempt after a back-off waiting period**  
You can catch errors with each API call, and then re-try the attempt after a back-off period. You can adjust the back-off algorithm according to business needs and load. Amazon SDKs have built-in retry logic. For more information, see [ Tools to Build on AWS.](https://aws.amazon.com/tools/ ) 

**Use an external database for frequently updated attributes**  
If your application requires several calls to a user pool to read or write custom attributes, use external storage. You can use your preferred database to store custom attributes or use a cache layer to load a user profile during sign-in. You can reference this profile from the cache when needed, instead of reloading the user profile from a user pool.

**Validate JSON web tokens (JWTs) on the client side**  
Applications must validate JWT tokens before trusting them. You can verify the signature and validity of tokens on the client side without sending API requests to a user pool. After the token is validated, you can trust claims in the token and use the claims instead of making more `getUser` API calls. For more information, see [ Verifying a JSON Web Token.](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html)

**Throttle traffic to your web application with a waiting room**  
If you expect traffic from a large number of users signing in during a time-bound event, such as taking an exam or attending a live event, you can optimize request traffic with self-throttling mechanisms. You can, for example, set up a waiting room where users can stand by until a session is available, allowing you to process requests when you have available capacity. See the [AWS Virtual Waiting Room solution](https://aws.amazon.com/solutions/implementations/aws-virtual-waiting-room) for a reference architecture of a waiting room. 

**Cache JWTs**  
Reuse access tokens until they expire. For an example framework with token caching in an API Gateway, see [Managing user pool token expiration and caching](amazon-cognito-user-pools-using-tokens-caching-tokens.md). Instead of generating API requests to query user information, cache ID tokens until they expire, and read user attributes from the cache.

For more information about working with API request rates in AWS, see [Managing and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/). For information about optimizing Amazon Cognito operations that add costs to your AWS bill, see [Managing costs](tracking-cost.md#tracking-cost-managing).

### Track quota usage
<a name="track-quota-usage"></a>

Amazon Cognito generates `CallCount` and `ThrottleCount` metrics in Amazon CloudWatch for each API operation category at the account level. You can use `CallCount` to track the total number of calls customers made related to a category. You can use `ThrottleCount` to track the total number of throttled calls related to a category. You can use the `CallCount` and `ThrottleCount` metrics with the `Sum` statistic to count the total number of calls in a category. For more information, see [CloudWatch usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html).

When monitoring service quotas, *utilization* is the percentage of a service quota in use. For example, if the quota value is 200 resources, and 150 resources are in use, the utilization is 75%. *Usage* is the number of resources or operations in use for a service quota.

**Tracking usage through CloudWatch metrics**  
You can track and collect Amazon Cognito user pools utilization metrics with CloudWatch. The CloudWatch dashboard displays metrics about every AWS service that you use. With CloudWatch, you can create metric alarms to notify you or change a specific resource that you are monitoring. For more information about CloudWatch metrics, see [Track your CloudWatch usage metrics](tracking-quotas-and-usage-in-cloud-watch-and-service-quotas.md).

**Tracking utilization through Service Quotas metrics**  
Amazon Cognito user pools are integrated with Service Quotas, a console interface to display and manage your service quota usage. In the Service Quotas console, you can look up the value of a specific quota, view monitoring information, request a quota increase, or set up CloudWatch alarms. After your account has been active for a while, you can view a graph of your resource utilization.

The **Applied account-level quota value** column in the Service Quotas console for [Amazon Cognito user pools](https://console.aws.amazon.com/servicequotas/home/services/cognito-idp/quotas) and [Amazon Cognito identity pools](https://console.aws.amazon.com/servicequotas/home/services/cognito-identity/quotas) displays your current quota. The **Utilization** column displays your current rate of quota usage. Adjustable Amazon Cognito user pools requests-per-second (RPS) quotas display their current usage. The Service Quotas console can also navigate you to CloudWatch metrics for a closer look at a selected quota metric. For more information on viewing quotas in the Service Quotas console, see [Viewing Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html).

### Track monthly active users (MAUs)
<a name="track-mau-usage"></a>

The number of monthly active users (MAUs) in your user pool contributes important data to your planning for increases to request-rate quotas. You can compare your API request rates to the number of users you had active in a given time period. With that knowledge, you can calculate how an increase in active users of your applications will affect your quotas in your usage model. For example, imagine that your combined applications in US West (Oregon) resulted in 2 million active users in a month and your `UserAuthentication` category received occasional throttling errors at the default quota of 120 requests per second (RPS). In the previous month, before your successful advertising campaign, you had 1 million MAUs and your applications never exceeded 80 RPS. If you anticipate a similar spike as a result of a new TV spot, you might purchase an additional 40 RPS to accommodate the next million users with an adjusted quota of 160 RPS.

**To review your MAUs**  
Access the [AWS Billing console](https://console.aws.amazon.com/billing/home) and review a recent bill. Under **charges by service**, you can filter on **Cognito** to view a breakdown of your MAUs for that billing period.

### Requesting a quota increase
<a name="api-request-rate-quotas"></a>

Amazon Cognito has a quota for the maximum number of operations per second that you can perform in your user pools and identity pools in each AWS Region. You can purchase an increase to adjustable Amazon Cognito user pools API request rate quotas. For adjustable user pools categories, you can request a higher account-level max limit in Service Quotas and then use the Amazon Cognito provisioning API to set your desired rate. For more information, see [Managing provisioned limits](#provisioned-quotas).

To request a higher account-level max limit, use the Service Quotas console or the Service Quotas API operations `ListAWSDefaultServiceQuotas` and `RequestServiceQuotaIncrease`.
+ To request an account-level max limit increase using the Service Quotas console, see [Requesting a API quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.
+ Some account-level max limit increases are auto-approved. Otherwise, AWS targets completion of quota increase requests within 10 days. However, several considerations might cause the request processing time to exceed 10 days. Some requests, for example, might require Amazon Cognito to provision additional hardware capacity, and seasonal increases in request volumes might introduce delays.
+ If the quota isn't available in Service Quotas, use the [Service limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

**Note**  
Only adjustable quotas can be increased.

**Note**  
Quota increases are regional configurations. A quota increase in one AWS Region doesn't affect your quotas in other Regions. If you require higher API quotas in multiple Regions, you must request a quota increase in each Region separately.

**Note**  
Requesting an account-level max limit increase is only the first step. After your request is approved, you must call `UpdateProvisionedLimit` or use the Amazon Cognito console to set your provisioned limit. For more information, see [Managing provisioned limits](#provisioned-quotas).

### Managing provisioned limits
<a name="provisioned-quotas"></a>

Amazon Cognito user pools supports a two-tier quota model for adjustable API rate quotas. With this model, you can programmatically increase or decrease your provisioned request rate without contacting AWS Support. The two tiers work as follows:

**Account-level max limit**  
The maximum rate that you can provision, set through Service Quotas. To increase your account-level max limit, submit a quota increase request in the Service Quotas console. Some requests are auto-approved. For more information, see [Requesting a quota increase](#api-request-rate-quotas).

**Provisioned limit**  
The rate, in requests per second (RPS), that Amazon Cognito currently enforces for your account. You can adjust this value up to your account-level max limit with the Amazon Cognito provisioning API operations.

For example, if your `UserAuthentication` account-level max limit is 500 RPS, you can use the `UpdateProvisionedLimit` API operation to set your provisioned limit to 300 RPS. You can later reduce the provisioned limit back to the default, and you are only billed for the time at the higher rate.

**Important**  
You are billed for provisioned capacity above the default rate, prorated based on actual usage time. For pricing, see [Amazon Cognito pricing](https://aws.amazon.com/cognito/pricing/).

#### Managing provisioned limits in the console
<a name="provisioned-quotas-console"></a>

You can view and manage your provisioned limits in the Amazon Cognito console. Open the **User pools** page and choose the **Provisioned limits** tab. On this tab, you can view your current provisioned limits and account-level max limits for each adjustable API category. You can increase or decrease your provisioned rate within your approved account-level max limit.

#### Provisioning API operations
<a name="provisioned-quotas-api"></a>

Amazon Cognito provides the following API operations for managing provisioned limits. These operations require authentication and the corresponding IAM permissions.

**[GetProvisionedLimit](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetProvisionedLimit.html)**  
Returns the current provisioned limit value for a specific API category. The response includes the provisioned limit value and the default (free) limit value.

**[UpdateProvisionedLimit](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateProvisionedLimit.html)**  
Sets your provisioned limit value for a specific API category. The requested value must be between the default limit and your Service Quotas account-level max limit. This operation takes effect immediately.

Both operations take a `LimitDefinition` parameter that identifies the limit to manage. For user pools API rate limits, the limit definition has a class of `API_CATEGORY` and an attributes map with the `Category` key. For example, to manage the `UserAuthentication` limit, specify a limit definition with `{"Category": "UserAuthentication"}`.

**Example GetProvisionedLimit request and response**  
The following example returns the provisioned limit for the `UserAuthentication` API category.  
**Request**  

```
{
    "LimitDefinition": {
        "LimitClass": "API_CATEGORY",
        "Attributes": {"Category": "UserAuthentication"}
    }
}
```
**Response**  

```
{
    "Limit": {
        "LimitDefinition": {
            "LimitClass": "API_CATEGORY",
            "Attributes": {"Category": "UserAuthentication"}
        },
        "ProvisionedLimitValue": 120,
        "FreeLimitValue": 120
    }
}
```

**Example UpdateProvisionedLimit request and response**  
The following example sets the provisioned limit for the `UserAuthentication` API category to 300 RPS.  
**Request**  

```
{
    "LimitDefinition": {
        "LimitClass": "API_CATEGORY",
        "Attributes": {"Category": "UserAuthentication"}
    },
    "RequestedLimitValue": 300
}
```
**Response**  

```
{
    "Limit": {
        "LimitDefinition": {
            "LimitClass": "API_CATEGORY",
            "Attributes": {"Category": "UserAuthentication"}
        },
        "ProvisionedLimitValue": 300,
        "FreeLimitValue": 120
    }
}
```

The following IAM actions control access to these operations:
+ `cognito-idp:GetProvisionedLimit`
+ `cognito-idp:UpdateProvisionedLimit`

**Note**  
Cross-account access is not supported. Only the owning account can manage its provisioned limits.

#### Provisioning workflow
<a name="provisioned-quotas-workflow"></a>

The following workflow describes how to increase your provisioned limit.

1. Determine your required rate. For more information, see [Identify quota requirements](#identify-quota-requirements).

1. If your required rate exceeds your current Service Quotas account-level max limit, request an increase in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/cognito-idp/quotas).

1. After your account-level max limit is approved, call `UpdateProvisionedLimit` with your desired rate.

1. To reduce your provisioned rate and stop additional billing, call `UpdateProvisionedLimit` with the default limit value or a lower value.

#### Considerations
<a name="provisioned-quotas-considerations"></a>
+ Provisioned limits are account-level resources. They apply to the aggregate rate of all requests from all user pools in one AWS Region in your AWS account.
+ The `LimitManagement` category, which includes `GetProvisionedLimit` and `UpdateProvisionedLimit`, is rate-limited to 1 request per second per account.
+ Only adjustable quota categories support provisioning. For a list of adjustable categories, see [Amazon Cognito user pools API operation categories and request rate quotas](#category_operations).
+ If your user pool uses managed login, you can't use the provisioning API to adjust the `UserAuthentication` or `UserFederation` categories. To increase these quotas, submit a Service Quotas increase request through the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/cognito-idp/quotas) or use the [Service limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).
+ Changes to provisioned quotas are regional. A provisioned quota change in one AWS Region doesn't affect your quotas in other Regions.
+ All calls to provisioning API operations are logged in AWS CloudTrail.

## Amazon Cognito user pools API operation categories and request rate quotas
<a name="category_operations"></a>

Because Amazon Cognito has overlapping classes of API operations with [differing authorization models](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html), each operation belongs to a category. Each category has its own pooled quota for all member API operations, across all user pools in one AWS Region in your account. You can only request an increase to *adjustable* category quotas. For more information, see [Requesting a quota increase](#api-request-rate-quotas). Quota adjustments apply to the user pools in your account in a single Region. Amazon Cognito restricts operations in some categories[3](#cognito-quotas-individual-rates-note) to 5 requests per second (RPS), per user pool. The **Default quota (RPS)** additionally applies to all user pools in an AWS account.

**Note**  
The quota for each category is measured in Monthly Active Users (MAUs). AWS accounts with fewer than two million MAUs can operate within the default quota. If you have less than one million MAUs and Amazon Cognito is throttling requests, consider optimizing your app. For more information, see [Optimize request rates for quota limits](#optimize-quotas).

Category operation quotas are applied across all users in all user pools within one AWS Region. Amazon Cognito also maintains a quota for the number of requests that your app can generate against one user. You must limit per-user API requests as shown in the following table.

**Amazon Cognito user pools per-user request rate quotas**


| Operation | Operations per user per second | 
| --- | --- | 
| Read user profileExamples: `GetUser`, `GetDevice`, `InitiateAuth`, `RespondToAuthChallenge` | 10 | 
| Write user profileExamples: `UpdateUserAttributes`, `SetUserSettings` | 10 | 

You must limit per-category API requests as shown in the following table.

**Amazon Cognito user pools per-category request rate quotas**


| Category | Description | Default quota (RPS) | Adjustable | 
| --- | --- | --- | --- | 
| UserAuthentication+  [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) <br />+  Token refresh with `InitiateAuth` or the [token endpoint](token-endpoint.md) <br />+  [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html)[1](#cognito-quotas-auth-challenge-note) <br />+  [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) <br />+  [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html)[1](#cognito-quotas-auth-challenge-note) <br />+  [GetTokensFromRefreshToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.html) <br />+  Managed login or classic hosted UI sign-in and MFA for [local users](cognito-terms.md#terms-localuser) in [authorization-code or implicit grants](federation-endpoints-oauth-grants.md)[2](#cognito-quotas-hosted-ui-note)  | Operations that authenticate (sign in) a user. These operations are subject to [Amazon Cognito user pools API operations with special request rate handling](#api-operation-special-handling). | 120 | Yes | 
| UserCreation+  [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html) <br />+  [ConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.html) <br />+  [AdminCreateUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html) <br />+  [AdminConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.html)  | Operations that create or confirm an Amazon Cognito local user. This is a user that is created and verified directly by your Amazon Cognito user pools. | 50 | Yes | 
| UserFederationOperations that federate (authenticate) users with a third-party identity provider into your Amazon Cognito user pools. | Operations that submit an IdP response to a user pool federation endpoint. OIDC or social provider operations that result in an IdP token, and all SAML requests, contribute to this quota. | 25 | Yes | 
| UserAccountRecovery+  [ChangePassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ChangePassword.html) <br />+  [ConfirmForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.html) <br />+  [ForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.html) <br />+  [AdminResetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.html) <br />+  [AdminSetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.html) <br />+  [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html)[1](#cognito-quotas-auth-challenge-note) <br />+  [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html)[1](#cognito-quotas-auth-challenge-note) <br />+  Managed login password reset  | Operations that recover a user's account, or change or update a user's password. | 30 | No | 
| UserRead+  [AdminGetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.html) <br />+  [AdminGetUserAuthFactors](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUserAuthFactors.html) <br />+  [GetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUser.html)  | Operations that retrieve a user from your user pools.  | 120 | Yes | 
| UserUpdate+  [AdminAddUserToGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminAddUserToGroup.html) <br />+  [AdminDeleteUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUserAttributes.html) <br />+  [AdminUpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html) <br />+  [AdminDeleteUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUser.html) <br />+  [AdminDisableUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDisableUser.html) <br />+  [AdminEnableUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminEnableUser.html) <br />+  [AdminLinkProviderForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.html) <br />+  [AdminDisableProviderForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDisableProviderForUser.html) <br />+  [VerifyUserAttribute](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifyUserAttribute.html) <br />+  [DeleteUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUser.html) <br />+  [DeleteUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserAttributes.html) <br />+  [UpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.html) <br />+  [AdminUserGlobalSignOut](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.html) <br />+  [GlobalSignOut](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.html) <br />+  [AdminRemoveUserFromGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRemoveUserFromGroup.html)  |  Operations that you use to manage users and user attributes. | 25 | No | 
| UserToken+  [RevokeToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RevokeToken.html)  | Operations for token management | 120 | Yes | 
| UserResourceRead+  [AdminGetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.html) <br />+  [AdminListGroupsForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListGroupsForUser.html) <br />+  [AdminListDevices](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.html) <br />+  [GetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetDevice.html) <br />+  [ListDevices](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListDevices.html) <br />+  [GetUserAttributeVerificationCode](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserAttributeVerificationCode.html) <br />+  [ResendConfirmationCode](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.html) <br />+  [AdminListUserAuthEvents](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListUserAuthEvents.html)  | Operations that retrieve user resource information from Amazon Cognito, such as a remembered device or a group membership. | 50 | Yes | 
| UserResourceUpdate+  [AdminForgetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminForgetDevice.html) <br />+  [AdminUpdateAuthEventFeedback](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateAuthEventFeedback.html) <br />+  [AdminSetUserMFAPreference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserMFAPreference.html) <br />+  [AdminDeleteSoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteSoftwareToken.html) <br />+  [AdminSetUserSettings](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserSettings.html) <br />+  [AdminUpdateDeviceStatus](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateDeviceStatus.html) <br />+  [UpdateDeviceStatus](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.html) <br />+  [UpdateAuthEventFeedback](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateAuthEventFeedback.html) <br />+  [ConfirmDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.html) <br />+  [SetUserMFAPreference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserMFAPreference.html) <br />+  [SetUserSettings](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserSettings.html) <br />+  [VerifySoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifySoftwareToken.html) <br />+  [AssociateSoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AssociateSoftwareToken.html) <br />+  [ForgetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ForgetDevice.html)  | Operations that update resource information for a user, such as a remembered device or a group membership. | 25 | No | 
| UserList+  [ListUsers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html) <br />+  [ListUsersInGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsersInGroup.html)  | Operations that return a list of users. | 30 | No | 
| UserPoolRead+  [DescribeUserPool ](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html) <br />+  [ListUserPools](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPools.html)  | Operations that read your user pools. | 15 | No | 
| UserPoolUpdate+  [CreateUserPool ](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html) <br />+  [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html) <br />+  [DeleteUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPool.html)  | Operations that create, update, or delete your user pools. | 15 | No | 
| UserPoolResourceRead+  [DescribeIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.html) <br />+  [DescribeResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeResourceServer.html) <br />+  [DescribeUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserImportJob.html) <br />+  [DescribeUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.html) <br />+  [GetCSVHeader](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetCSVHeader.html) <br />+  [GetGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetGroup.html) <br />+  [GetSigningCertificate](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetSigningCertificate.html) <br />+  [GetIdentityProviderByIdentifier](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetIdentityProviderByIdentifier.html) <br />+  [GetUserPoolMfaConfig](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserPoolMfaConfig.html) <br />+  [ListGroups](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListGroups.html) <br />+  [ListIdentityProviders](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListIdentityProviders.html) <br />+  [ListResourceServers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListResourceServers.html) <br />+  [ListTagsForResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListTagsForResource.html) <br />+  [ListUserImportJobs](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserImportJobs.html) <br />+  [DescribeRiskConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeRiskConfiguration.html) <br />+  [GetUICustomization](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUICustomization.html) <br />+  [DescribeManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBranding.html) <br />+  [DescribeManagedLoginBrandingByClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBrandingByClient.html)  | Operations that retrieve information about resources, such as groups or resource servers, from a user pool.[3](#cognito-quotas-individual-rates-note) | 20 | No | 
| UserPoolResourceUpdate+  [AddCustomAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddCustomAttributes.html) <br />+  [CreateGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateGroup.html) <br />+  [CreateIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html) <br />+  [CreateResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateResourceServer.html) <br />+  [CreateUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserImportJob.html) <br />+  [CreateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.html) <br />+  [DeleteGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteGroup.html) <br />+  [DeleteIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteIdentityProvider.html) <br />+  [DeleteResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteResourceServer.html) <br />+  [DeleteUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolDomain.html) <br />+  [SetUserPoolMfaConfig](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.html) <br />+  [StartUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StartUserImportJob.html) <br />+  [StopUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StopUserImportJob.html) <br />+  [UpdateGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateGroup.html) <br />+  [UpdateIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.html) <br />+  [UpdateResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateResourceServer.html) <br />+  [UpdateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.html) <br />+  [SetRiskConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetRiskConfiguration.html) <br />+  [SetUICustomization](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUICustomization.html) <br />+  [TagResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_TagResource.html) <br />+  [UntagResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UntagResource.html) <br />+  [CreateManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateManagedLoginBranding.html) <br />+  [UpdateManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateManagedLoginBranding.html) <br />+  [DeleteManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteManagedLoginBranding.html)  | Operations that modify resources, such as groups or resource servers, in a user pool.[3](#cognito-quotas-individual-rates-note) | 15 | No | 
| UserPoolClientRead+  [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html) <br />+  [ListUserPoolClients](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.html)  | Operations that retrieve information about your user pool clients.[3](#cognito-quotas-individual-rates-note) | 15 | No | 
| UserPoolClientUpdate+  [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html) <br />+  [DeleteUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClient.html) <br />+  [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html)  | Operations that create, update, and delete your user pool clients.[3](#cognito-quotas-individual-rates-note) | 15 | No | 
| ClientAuthentication+  `client_credentials` grant type requests to the [token endpoint](token-endpoint.md) <br />+  [GetClientToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetClientToken.html)  | Operations that generate credentials to be used in authorizing machine-to-machine requests | 150 | No | 
| LimitManagement+  [GetProvisionedLimit](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetProvisionedLimit.html) <br />+  [UpdateProvisionedLimit](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateProvisionedLimit.html)  | Operations that retrieve or update your provisioned API rate limits | 1 | No | 

 1 A `RespondToAuthChallenge` or `AdminRespondToAuthChallenge` response with a `ChallengeName` of `NEW_PASSWORD_REQUIRED` counts toward the `UserAccountRecovery` category. All other challenge responses count toward the `UserAuthentication` category.

2 Each managed login or classic hosted UI operation during sign-in contributes one request to the quota. For example, a user who signs in and provides an MFA code contributes 2 requests. Token redemption in authorization-code grants is subject to an additional quota allocation at the same rate as your quota in the `UserAuthentication` category.

3 Any individual operation in this category has a constraint that prevents the operation from being called at a rate higher than 5 RPS for a single user pool.

### Bulk request-rate limits for user pool domains
<a name="category_operations-managedlogin"></a>

The following quotas apply to the overall volume of requests to a user pool domain.


| Operation | Description | Default quota (RPS) | Adjustable | 
| --- | --- | --- | --- | 
| Requests from source IP | Volume of requests from one IP address to one domain | 300 | No | 
| Requests to app client | Volume of requests for one app client ID in one domain | 300 | No | 
| Requests to domain | Overall volume of requests for the services of one user pool domain | 500 | No | 
| Requests for JSON web key documents | Volume of requests for jwks.json in one AWS account in one AWS Region | 50,000 | No | 

## Amazon Cognito identity pools (federated identities) API operation request rate quotas
<a name="amazon-cognito-identity-pools-federated-identities-request-rate-quotas"></a>


| Operation | Description | Default quota (RPS)[1](#identity-pools-request-rate-variable-note) | Adjustable | Quota increase eligibility | 
| --- | --- | --- | --- | --- | 
| GetId | Retrieve an identity ID from an identity pool. | 25 | Yes | Contact your account team. | 
| GetOpenIdToken | Retrieve an OpenID token from an identity pool in the classic workflow. | 200 | Yes | Contact your account team. | 
| GetCredentialsForIdentity | Retrieve AWS credentials from an identity pool in the enhanced workflow. | 200 | Yes | Contact your account team. | 
| GetOpenIdTokenForDeveloperIdentity | Retrieve an OpenID token from an identity pool in the developer workflow. | 50 | Yes | Contact your account team. | 
| ListIdentities | Retrieve a list of identity IDs in an identity pool. | 5 | Yes | Contact your account team. | 
| DeleteIdentities | Delete one or more registered identities from an identity pool. | 10 | Yes | Contact your account team. | 
| TagResource | Apply a tag to an identity pool. | 5 | Yes | Contact your account team. | 
| UntagResource | Remove a tag from an identity pool. | 5 | Yes | Contact your account team. | 
| ListTagsForResource | Display a list of the tags applied to an identity pool. | 10 | Yes | Contact your account team. | 

1 The default quota is the minimum request rate quota for the identity pools in any AWS Region in your AWS account. Your RPS quota might be higher in some Regions.

## Quotas on resource number and size
<a name="resource-quotas"></a>

Resource quotas are the maximum number or size of resources, input fields, time duration, and other miscellaneous features in Amazon Cognito.

You can request an adjustment to some resource quotas in the Service Quotas console or from a [Service limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). To request a quota from the Service Quotas console, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota isn't available in Service Quotas, use the [Service limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

**Note**  
Resource quotas at the AWS account level, like *User pools per Region*, apply to Amazon Cognito resources in each AWS Region. For example, you can have 1,000 user pools in US East (N. Virginia) and another 1,000 in Europe (Stockholm).

The following tables indicate default resource quotas, and whether they're adjustable.

### Amazon Cognito user pools resource quotas
<a name="resource-quotas-cup"></a>

The following quotas describe the maximum number or length of items that you can create in user pools.


| Resource | Quota | Adjustable | Maximum quota | 
| --- | --- | --- | --- | 
| App clients per user pool | 1,000 | Yes | 10,000 | 
| User pools per Region | 1,000 | Yes | 10,000 | 
| Identity providers per user pool | 300 | Yes | 1,000 | 
| Resource servers per user pool | 25 | Yes | 300 | 
| Users per user pool | 40,000,000 | Yes | Contact your account team. | 
| Total combined changes in pre token generation Lambda trigger[1](#cognito-resource-quotas-claims-note) | 5,000 | Yes | Contact your account team. | 
| Managed login branding styles per user pool | 20 | No | N/A | 
| Managed login terms documents per user pool | 40 | No | N/A | 
| Custom attributes per user pool | 50 | No | N/A | 
| Characters per attribute | 2,048 bytes | No | N/A | 
| Characters in custom attribute name | 20 | No | N/A | 
| Required minimum password characters in password policy | 6–99 | No | N/A | 
| Email messages sent daily per AWS account[2](#cognito-resource-quotas-email-note) | 50 | No | N/A | 
| Email MFA messages sent to one email address hourly per requester IP address | 5-20 | No | N/A | 
| Characters in email subject | 140 | No | N/A | 
| Characters in email message | 20,000 | No | N/A | 
| Characters in SMS verification message | 140 | No | N/A | 
| Characters in password | 256 | No | N/A | 
| Characters in identity provider name | 32 | No | N/A | 
| Characters in a SAML response | 100,000 | No | N/A | 
| Identifiers per identity provider | 50 | No | N/A | 
| Identities linked to a user | 5 | No | N/A | 
| Passkey/WebAuthn authenticators per user | 20 | No | N/A | 
| Callback URLs per app client | 100 | No | N/A | 
| Logout URLs per app client | 100 | No | N/A | 
| Scopes per resource server | 100 | No | N/A | 
| Scopes per app client | 50 | No | N/A | 
| Custom domains per Region | 4 | No | N/A | 
| Groups to which each user can belong | 100 | No | N/A | 
| Groups per user pool | 10,000 | No | N/A | 

1 This quota might be encountered in tokens from a [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md). The number of existing and added claims plus scopes in access and identity tokens in one transaction must add up to a number smaller than or equal to this quota. Suppressed claims and scopes don't contribute to this quota.

2 This quota applies only if you are using the default email feature for an Amazon Cognito user pool. For a higher email delivery volume, configure your user pool to use your Amazon SES email configuration. This restriction resets daily at 0900 UTC. For more information, see [Email settings for Amazon Cognito user pools](user-pool-email.md).

### Amazon Cognito user pools session validity parameters
<a name="resource-quotas-cup-session"></a>

The following quotas describe the available settings for the duration of authentication artifacts and user sessions in user pools.


| Token | Quota | 
| --- | --- | 
| ID token | 5 minutes – 1 day | 
| Refresh token | 1 hour – 3,650 days | 
| Access token | 5 minutes – 1 day | 
| Hosted UI session cookie | 1 hour | 
| Authentication session token | 3 minutes – 15 minutes | 

### Amazon Cognito user pools code security resource quotas (non-adjustable)
<a name="resource-quotas-cup-codes"></a>

The following quotas describe the available time periods related to codes for sign-in, sign-up, and password reset.


| Resource | Quota | 
| --- | --- | 
| Sign-up confirmation code validity period | 24 hours | 
| User attribute verification code validity period | 24 hours | 
| Multi-factor authentication (MFA) code validity period | 3–15 minutes | 
| Forgot password code validity period | 1 hour | 
| Maximum number of ConfirmForgotPassword and ForgotPassword requests per user per hour[1](#cognito-resource-quotas-confirmforgotpassword-note) | 5–20 | 
| Maximum number of ResendConfirmationCode requests per user per hour | 5 | 
| Maximum number of ConfirmSignUp requests per user per hour | 15 | 
| Maximum number of ChangePassword requests per user per hour | 5 | 
| Maximum number of GetUserAttributeVerificationCode requests per user per hour | 5 | 
| Maximum number of VerifyUserAttribute requests per user per hour | 15 | 

1 Amazon Cognito evaluates risk factors in the request to update passwords and assigns a quota that's tied to the evaluated risk level. For more information, see [Forgot password behavior](managing-users-passwords.md#forgot-password).

### Amazon Cognito user pools user import job resource quotas
<a name="resource-quotas-cup-import"></a>

The following quotas describe the resources and limits available to user import jobs.


| Resource | Quota | Adjustable | Maximum quota | 
| --- | --- | --- | --- | 
| User import jobs per user pool | 1,000 | Yes | Contact your account team. | 
| Maximum characters per user import CSV row | 16,000 | No | N/A | 
| Maximum CSV file size | 100 MB | No | N/A | 
| Maximum number of users per CSV file | 500,000 | No | N/A | 

### Amazon Cognito identity pools (federated identities) resource quotas
<a name="resource-quotas-cib"></a>

The following quotas describe the maximum number or length of items that you can create in identity pools.


| Resource | Quota | Adjustable | Maximum quota | 
| --- | --- | --- | --- | 
| Identity pools per account | 1,000 | Yes | N/A | 
| Amazon Cognito user pool providers per identity pool | 50 | Yes | 1000 | 
| Character length of an identity pool name | 128 bytes | No | N/A | 
| Character length of a login provider name | 2,048 bytes | No | N/A | 
| Identities per identity pool | Unlimited | No | N/A | 
| Identity providers for which role mappings can be specified  | 10 | No | N/A | 
| Results from a single list or lookup call | 60 | No | N/A | 
| Role-based access control (RBAC) rules | 25 | No | N/A | 

### Amazon Cognito Sync resource quotas
<a name="resource-quotas-sync"></a>

The following quotas describe the maximum number or length of items that you can create in Amazon Cognito Sync.


| Resource | Quota | Adjustable | Maximum quota | 
| --- | --- | --- | --- | 
| Datasets per identity | 20 | Yes | Contact your account team. | 
| Records per dataset | 1,024 | Yes | Contact your account team. | 
| Size of a single dataset | 1 MB | Yes | Contact your account team. | 
| Characters in dataset name | 128 bytes | No | N/A | 
| Waiting time for a bulk publish after a successful request | 24 hours | No | N/A | 