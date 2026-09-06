

# User pool metrics in CloudWatch
<a name="metrics-for-cognito-user-pools"></a>

User pools report user-activity statistics to CloudWatch as metrics. From CloudWatch, you can analyze the volume of authentication activity and quota usage in your user pools. With the information in these metrics, you can set alarms for noteworthy events and adjust your user pool configuration as needed. Where user-activity logging has detailed records of user activity in your user pools, CloudWatch metrics have aggregated statistics and performance indicators.

The following table lists the metrics available for Amazon Cognito user pools. Amazon Cognito publishes metrics to the namespaces `AWS/Cognito` and `AWS/Usage`. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) in *Amazon CloudWatch User Guide*.

For more information about tracking quotas and usage, see [Track quota usage](quotas.md#track-quota-usage) and [Track monthly active users (MAUs)](quotas.md#track-mau-usage).

**Note**  
Metrics that haven't had any new data points in the past two weeks don't appear in the console. They also don't appear when you enter their metric name or dimension names in the search box in the **All metrics** tab in the console. In addition, they are not returned in the results of a list-metrics command. The best way to retrieve these metrics is with the `get-metric-data` or `get-metric-statistics` commands in the AWS CLI.


| Metric | Description | Namespace | 
| --- | --- | --- | 
| SignUpSuccesses | Provides the total number of successful user registration requests made to the Amazon Cognito user pool. A successful user registration request produces a value of 1, whereas an unsuccessful request produces a value of 0. A throttled request is also considered as an unsuccessful request, and hence a throttled request will also produce a count of 0.<br />To find the percentage of successful user registration requests, use the `Average` statistic on this metric. To count the total number of user registration requests, use the `Sample Count` statistic on this metric. To count the total number of successful user registration requests, use the `Sum` statistic on this metric. To count the total number of failed user registration requests, use the CloudWatch `Math` expression and subtract the `Sum` statistic from the `Sample Count` statistic.<br />This metric is published for each user pool for each user pool client. In case when the user registration is performed by an admin, the metric is published with the user pool client as `Admin`.<br />Note that this metric is not emitted for [User import](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html) and [User migration](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-import-using-lambda.html) cases.<br />Metric dimension: `UserPool`, `UserPoolClient`<br />Units: Count | AWS/Cognito | 
| SignUpThrottles | Provides the total number of throttled user registration requests made to the Amazon Cognito user pool. A count of 1 is published whenever a user registration request is throttled. <br />To count the total number of throttled user registration requests, use the `Sum` statistic for this metric.<br />This metric is published for each user pool for each client. In case when the request that was throttled was made by an administrator, the metric is published with user pool client as `Admin`.<br />Metric dimension: `UserPool`, `UserPoolClient`<br />Units: Count | AWS/Cognito | 
| SignInSuccesses | Provides the total number of successful user authentication requests made to the Amazon Cognito user pool. A user authentication is considered successful when authentication token is issued to the user. A successful authentication produces a value of 1, whereas an unsuccessful request produces a value of 0. A throttled request is also considered as an unsuccessful request, and hence a throttled request will also produce a count of 0. <br />To find the percentage of successful user authentication requests, use the `Average` statistic on this metric. To count the total number of user authentication requests, use the `Sample Count` statistic on this metric. To count the total number of successful user authentication requests, use the `Sum` statistic on this metric. To count the total number of failed user authentication requests, use the CloudWatch `Math` expression and subtract the `Sum` statistic from the `Sample Count` statistic.<br />This metric is published for each user pool for each client. In case an invalid user pool client is provided with a request, the corresponding user pool client value in the metric contains a fixed value `Invalid` instead of the actual invalid value sent in the request.<br />Note that requests to refresh the Amazon Cognito token is not included in this metric. There is a separate metric for providing `Refresh` token statistics.<br />Metric dimension: `UserPool`, `UserPoolClient`<br />Units: Count | AWS/Cognito | 
| SignInThrottles | Provides the total number of throttled user authentication requests made to the Amazon Cognito user pool. A count of 1 is published whenever an authentication request is throttled.<br />To count the total number of throttled user authentication requests, use the `Sum` statistic for this metric.<br />This metric is published for each user pool for each client. In case an invalid user pool client is provided with a request, the corresponding user pool client value in the metric contains a fixed value `Invalid` instead of the actual invalid value sent in the request.<br />Requests to refresh Amazon Cognito token is not included in this metric. There is a separate metric for providing `Refresh` token statistics.<br />Metric dimension: `UserPool`, `UserPoolClient`<br />Units: Count | AWS/Cognito | 
| TokenRefreshSuccesses | Provides the total number of successful requests to refresh an Amazon Cognito token that were made to the Amazon Cognito user pool. A successful refresh Amazon Cognito token request produces a value of 1, whereas an unsuccessful request produces a value of 0. A throttled request is also considered as an unsuccessful request, and hence a throttled request will also produce a count of 0. <br />To find the percentage of successful requests to refresh an Amazon Cognito token, use the `Average` statistic on this metric. To count the total number of requests to refresh an Amazon Cognito token, use the `Sample Count` statistic on this metric. To count the total number of successful requests to refresh an Amazon Cognito token, use the `Sum` statistic on this metric. To count the total number of failed requests to refresh an Amazon Cognito token, use the CloudWatch `Math` expression and subtract the `Sum` statistic from the `Sample Count` statistic.<br />This metric is published per each user pool client. If an invalid user pool client is in a request, the user pool client value contains a fixed value of `Invalid`.<br />Metric dimension: `UserPool`, `UserPoolClient`<br />Units: Count | AWS/Cognito | 
| TokenRefreshThrottles | Provides the total number of throttled requests to refresh an Amazon Cognito token that were made to the Amazon Cognito user pool. A count of 1 is published whenever a refresh Amazon Cognito token request is throttled.<br />To count the total number of throttled requests to refresh an Amazon Cognito token, use the `Sum` statistic for this metric.<br />This metric is published for each user pool for each client. In case an invalid user pool client is provided with a request, corresponding user pool client value in the metric contains a fixed value `Invalid` instead of the actual invalid value sent in the request.<br />Metric dimension: `UserPool`, `UserPoolClient`<br />Units: Count | AWS/Cognito | 
| FederationSuccesses | Provides the total number of successful identity federation requests to the Amazon Cognito user pool. An identity federation is considered successful when Amazon Cognito issues authentication tokens to the user. A successful identity federation request produces a value of 1, whereas an unsuccessful request produces a value of 0. Throttled requests and requests that generate an authorization code but no tokens produce a value of 0.<br />To find the percentage of successful identity federation requests, use the `Average` statistic on this metric. To count the total number of identity federation requests, use the `Sample Count` statistic on this metric. To count the total number of successful identity federation requests, use the `Sum` statistic on this metric. To count the total number of failed identity federation requests, use the CloudWatch `Math` expression and subtract the `Sum` statistic from the `Sample Count` statistic.<br />Metric dimension: `UserPool`, `UserPoolClient`, `IdentityProvider`<br />Units: Count | AWS/Cognito | 
| FederationThrottles | Provides the total number of throttled identity federation requests to the Amazon Cognito user pool. A count of 1 is published whenever an identity federation request is throttled.<br />To count the total number of throttled identity federation requests, use the `Sum` statistic for this metric.<br />Metric dimension: `UserPool`, `UserPoolClient`, `IdentityProvider`<br />Units: Count | AWS/Cognito | 
| CallCount | Provides the total number of calls customers made related to a category. This metric includes all the calls, such as throttled calls, failed calls, and successful calls.<br />The category quota is enforced for each AWS account across all user pools in an account and Region. <br />You can count the total number of calls in a category using the `Sum` statistic for this metric.<br />Metric dimension: Service, Type, Resource, Class<br />Units: Count | AWS/Usage | 
| ThrottleCount | Provides the total number of throttled calls related to a category. <br />This metric is published at the account level.<br />You can count the total number of calls in a category, using the `Sum` statistic for this metric.<br />Metric dimension: Service, Type, Resource, Class<br />Units: Count | AWS/Usage | 

## Viewing threat protection metrics
<a name="user-pool-settings-viewing-threat-protection-metrics"></a>

The metrics that your user pool publishes have statistical information about the effect that your threat protection settings have on user authentication activity. You might want to know how many users are attempting to sign in with compromised credentials. You can also find out what percentage of sign-in activity was evaluated to have some level of risk. Amazon Cognito publishes metrics for threat protection features to your account in Amazon CloudWatch. Amazon Cognito groups the threat protection metrics together by risk level and also by request level.

To add context to your risk analysis, you can [view information about individual user sign-in attempts](cognito-user-pool-settings-adaptive-authentication.md#user-pool-settings-adaptive-authentication-event-user-history), either in your user pool or in an exported data source.

**To view metrics in the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Choose Amazon Cognito.

1. Choose a group of aggregated metrics, such as **By Risk Classification**. 

1. The **All metrics** tab displays all metrics for that choice. You can do the following:
   + To sort the table, use the column heading.
   + To graph a metric, select the check box next to the metric. To select all metrics, select the check box in the heading row of the table.
   + To filter by resource, choose the resource ID, and then choose **Add to search**.
   + To filter by metric, choose the metric name, and then choose **Add to search**.


|  Metric  |  Description  |  Metric Dimensions  | Namespace | 
| --- | --- | --- | --- | 
| CompromisedCredentialRisk | Requests where Amazon Cognito detected compromised credentials. | Operation: The type of operation. `PasswordChange`, `SignIn`, or `SignUp` are the only dimensions.<br />UserPoolId: The identifier of the user pool.<br />RiskLevel: high (default), medium, or low. | AWS/Cognito | 
| AccountTakeoverRisk | Requests where Amazon Cognito detected account take-over risk. | Operation: The type of operation. `PasswordChange`, `SignIn`, or `SignUp` are the only dimensions.<br />UserPoolId: The identifier of the user pool.<br />RiskLevel: high, medium, or low. | AWS/Cognito | 
| OverrideBlock | Requests that Amazon Cognito blocked because of the configuration provided by the developer. | Operation: The type of operation. `PasswordChange`, `SignIn`, or `SignUp` are the only dimensions.<br />UserPoolId: The identifier of the user pool.<br />RiskLevel: high, medium, or low. | AWS/Cognito | 
| Risk | Requests that Amazon Cognito marked as risky. | Operation: The type of operation, such as `PasswordChange`, `SignIn`, or `SignUp`.<br />UserPoolId: The identifier of the user pool. | AWS/Cognito | 
| NoRisk | Requests where Amazon Cognito did not identify any risk.  | Operation: The type of operation, such as `PasswordChange`, `SignIn`, or `SignUp`.<br />UserPoolId: The identifier of the user pool. | AWS/Cognito | 

Amazon Cognito offers you two predefined groups of metrics for ready analysis in CloudWatch. **By Risk Classification** identifies the granularity of the risk level for requests that Amazon Cognito identifies as risky. **By Request Classification** reflects metrics aggregated by request level.


|  Aggregated Metrics Group  |  Description  | 
| --- | --- | 
| By Risk Classification | Requests that Amazon Cognito identifies as risky. | 
| By Request Classification | Metrics aggregated by request. | 

## Dimensions for Amazon Cognito user pools
<a name="dimensions-for-cognito-user-pools"></a>

The following dimensions are used to refine the usage metrics that are published by Amazon Cognito. The dimensions only apply to `CallCount` and `ThrottleCount ` metrics.


| Dimension | Description | 
| --- | --- | 
| Service | The name of the AWS service containing the resource. For Amazon Cognito usage metrics, the value for this dimension is `Cognito user pool`. | 
| Type | The type of entity that is being reported. The only valid value for Amazon Cognito usage metrics is API. | 
| Resource | The type of resource that is running. The only valid value is category name.  | 
| Class | The class of resource being tracked. Amazon Cognito doesn't use the class dimension. | 

## Use the CloudWatch console to track metrics
<a name="use-the-cloud-watch-console-to-track-metrics"></a>

You can track and collect Amazon Cognito user pools metrics using CloudWatch. The CloudWatch dashboard will display metrics about every AWS service you use. You can use CloudWatch to create metric alarms. The alarms can be set up to send you notifications or make a change to a specific resource that you are monitoring. To view service quota metrics in CloudWatch, complete the following steps.

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. In **All metrics** select a metric and a dimension.

1. Select the check box next to a metric. The metrics will appear in the graph.

**Note**  
Metrics that haven't had any new data points in the past two weeks don't appear in the console. They also don't appear when you enter their metric name or dimension names in the search box in the All metrics tab in the console, and they are not returned in the results of a list-metrics command. The best way to retrieve these metrics is with the `get-metric-data` or `get-metric-statistics` commands in the AWS CLI.

## Create a CloudWatch alarm for a quota
<a name="create-a-cloud-watch-alarm"></a>

 Amazon Cognito provides CloudWatch usage metrics that correspond to the AWS service quotas for `CallCount` and `ThrottleCount` APIs. For more information about tracking usage in CloudWatch, see [Track quota usage](quotas.md#track-quota-usage).

In the Service Quotas console, you can create alarms that alert you when your usage approaches a service quota. To learn how to set up a CloudWatch alarm using the Service Quotas console, see [Service Quotas and CloudWatch alarms](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html).