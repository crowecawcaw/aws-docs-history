

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Managing Parameter Store throughput
<a name="parameter-store-throughput"></a>

Parameter Store throughput defines the number of API transactions per second (TPS) that Systems Manager can process. The throughput setting applies to the Parameter Store as a whole rather than an individual API. By default, Parameter Store is configured with a standard throughput quota that is often suitable for low- to moderate-volume workloads. For higher-volume workloads, you can enable higher throughput, which increases the maximum number of supported transactions per second for your account and Region. You can enable and disable higher throughput as needed.

## Throughput quotas in Parameter Store
<a name="w2aac19c22c12c21c15b5"></a>

The following table lists the transaction limits for different API categories using default and higher throughput. API actions include AWS console usage, AWS CLI commands, and application reads. For more information on quotas and rate limits, see [AWS Systems Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#parameter-store).


| API actions | Default throughput | Higher throughput | 
| --- | --- | --- | 
|  [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html), [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html), and [GetParametersByPath](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html)  | 40 TPS shared across all three API actions combined |  [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html): 10,000 TPS; [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html): 1,000 TPS; [GetParametersByPath](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html): 100 TPS  | 
|  [DeleteParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameter.html) and [DeleteParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameters.html)  | 3 TPS | 5 TPS | 
|  [DescribeParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html), [GetParameterHistory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameterHistory.html), [LabelParameterVersion](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_LabelParameterVersion.html), [UnlabelParameterVersion](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UnlabelParameterVersion.html), and [PutParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html)  | 3 TPS | 10 TPS | 

In this context, a transaction is one API action for an account in a single Region. For example, the following command creates a single transaction.

```
aws ssm get-parameter --name "/myapp/prod/log-level"
```

The API actions can be distributed among applications. For example, each of the following scenarios reaches the default throughput limit of 40 TPS:
+ 1 application makes 40 `GetParameter` calls per second.
+ 10 applications make 4 `GetParameter` calls per second.
+ 40 applications make 1 `GetParameter` call per second.

A throughput limit applies to all APIs within a category. For example, the following combination of simultaneous parameter calls for an application meets the default limit of 40 TPS for parameter retrieval APIs:
+ `GetParameter` makes 25 calls per second.
+ `GetParameters` makes 10 calls per second.
+ `GetParameterByPath` makes 5 calls per second.

The `DescribeParameters` calls have a separate throughput limit. An application can make the preceding calls while also making 3 `DescribeParameters` calls per second without exceeding the overall limit for standard throughput.

 If your production requests exceed a throughput limit during standard operation or planned periods of high traffic, use the following optimization techniques. 

**Topics**
+ [Throughput quotas in Parameter Store](#w2aac19c22c12c21c15b5)
+ [Optimizing throughput in Parameter Store](#parameter-store-throughput-optimizing)
+ [Changing the throughput setting in Parameter Store](#parameter-store-throughput-increasing)

## Optimizing throughput in Parameter Store
<a name="parameter-store-throughput-optimizing"></a>

When Parameter Store receives multiple requests for parameters in a short interval, your application can experience *throttling*. For example, CloudWatch Logs or your application logs show `ThrottlingException` or `RateExceeded` errors raised by the SDK when it calls `GetParameter`, `GetParameters`, or `GetParametersByPath`. In other cases, application logic successfully retries API calls, but application latency increases. The result can be application outages, suboptimal user experience, failed deployments, complex workarounds, and lost developer time.

Multiple factors can lead to your application hitting Parameter Store quota limits, including the following: 
+  Your application scales out quickly because of a spike in traffic. For example, your application normally runs on 5 Amazon EC2 instances. When traffic increases suddenly, Amazon EC2 Auto Scaling launches 50 more instances. If each instance reads parameters when it starts, the combined requests can exceed the default request limit. 
+  Your container service starts many tasks at the same time. For example, an Amazon ECS service might start many replacement tasks during an update, and each task might read settings from Parameter Store when it starts. 
+  Your Lambda functions receive many requests at the same time. For example, Lambda might start many function environments to handle the increased traffic. Each function environment might read parameters when it starts. 
+  Your build or release process reads many parameters in a short time interval. For example, a build job might read settings for several applications or environments. 
+  Your application reads many parameters by path. For example, your application repeatedly reads all parameters under `/myapp/prod/` instead of reading only the specific parameters it needs. These repeated requests can exceed the default request limit. 

You can address Parameter Store throttling in the following complementary ways:
+ Reducing throughput

  Your application might be retrieving more data than it needs or retrieving it in an inefficient way.
+ Enabling higher throughput

  You can increase application resilience by increasing throughput quota for a specified Region and account. You can enable and disable the higher-throughput setting at any time for periods of high traffic. For production workloads that regularly generate throttling errors, consider enabling the setting permanently.

### Reducing throughput in Parameter Store
<a name="parameter-store-throughput-reduce-requests"></a>

 Whether you use standard or higher throughput, review the frequency and type of calls to Parameter Store. In some cases, you can reduce the number of requests without changing your parameters. Because cost is determined based on usage rather than on a subscription or tier model, the result is fewer billed API interactions. 
+  Cache parameter values in your application instead of reading the same values on every request. 

   For example, if your application reads `/myapp/prod/log-level` many times per minute, the application can read the value once and reuse it for a short period of time. This technique reduces repeated calls to Parameter Store. Choose a shorter reuse period for values that change often, and a longer reuse period for values that rarely change. 
+  Use [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html) when you know the names of multiple parameters. 

   For example, instead of making separate [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html) calls for the parameters `/myapp/prod/database/host`, `/myapp/prod/log-level`, and `/myapp/prod/vendor/merchant-id`, you can retrieve a list of these parameters in a single `GetParameters` request. 
+  Avoid reading more parameters than your application needs. 

  If your application needs only a few known parameters, use `GetParameter` or `GetParameters` instead of repeatedly reading an entire path such as `/myapp/prod/`. Use [GetParametersByPath](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html) when your application needs a group of parameters under a path. When you use higher throughput, the `GetParameter` quota is 100x the quota for `GetParametersByPath`. 
+  Spread out parameter reads when many resources start at the same time. 

   For example, if many Amazon EC2 instances or Amazon ECS tasks start during an update, avoid having every resource read parameters at exactly the same time. The quotas are per-second. Where possible, read parameters once and cache their values to the application, or add a small delay so that requests do not all occur in the same second. 
+  For Lambda functions, consider using the [AWS Parameters and Secrets Lambda Extension](https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html). 

   The extension can store parameter values locally for reuse by the function. This technique can reduce the number of calls to Parameter Store and can also reduce the time needed to retrieve parameter values. For a sample walkthrough of this technique, see [Using the AWS Parameter and Secrets Lambda extension to cache parameters and secrets](https://aws.amazon.com/blogs/compute/using-the-aws-parameter-and-secrets-lambda-extension-to-cache-parameters-and-secrets/). 

### Increasing throughput
<a name="parameter-store-higher-throughput"></a>

For higher-volume workloads, you can enable higher throughput. This setting increases the maximum number of supported transactions per second for your account and Region, at a cost. Consider higher throughput in the following scenarios:
+  Your application has a temporary need for higher throughput. 

   For example, a webstore might read parameters more often during a weekend sale. You can enable higher throughput before the sale begins, and then return to standard throughput after the sale ends. You can enable or disable higher throughput at any time from the Parameter Store **Settings** page or by using the AWS CLI. 
+  Your production application regularly retrieves parameters concurrently and runs into throttling issues. 

   Concurrent retrieval can happen when multiple instances, containers, functions, or build jobs read parameters from Parameter Store at the same time. Examples include the following: 
  +  Your application scales out quickly. For example, your application normally runs on 5 Amazon EC2 instances. When traffic increases suddenly, Amazon EC2 Auto Scaling launches 50 more instances. If each instance reads parameters when it starts, the combined requests can exceed the default request limit. 
  +  Your container service starts many tasks at the same time. For example, an Amazon ECS service might start many replacement tasks during an update, and each task might read settings from Parameter Store when it starts. 
  +  Your Lambda functions receive many requests at the same time. For example, Lambda might start many function environments to handle the increased traffic. Each function environment might read parameters when it starts. 
  +  Your build or release process reads many parameters in a short time interval. For example, a build job might read settings for several applications or environments. 

#### Cost considerations for higher throughput
<a name="parameter-store-throughput-cost"></a>

For the higher throughput option, additional charges apply. For current Parameter Store API pricing and examples, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/).

Charges are based on Parameter Store API interactions. An API interaction is defined as an interaction between an API request and an individual parameter. For example, if a single `GetParameter` request returns 10 parameters, this request counts as 10 Parameter Store API interactions for billing purposes.

Consider a scenario where you want to switch to higher throughput for a short period of increased traffic. Your webstore holds a weekend sale and makes `1,000,000` Parameter Store API interactions during the sale. If the cost for higher throughput in this example is `$0.05` per `10,000` API interactions, the total additional cost is approximately `$5`. You can switch back to standard throughput at the end of the sale and stop incurring costs.

#### Combining throughput and parameter tiers
<a name="parameter-store-throughput-tiers"></a>

Throughput operates independently of parameter tiers. Whereas parameter tiers control storage limits and feature availability, throughput settings control request volume. To meet performance and scale requirements, you can use tiers and throughput together.

For example, to support simple and low-load applications, you can use standard parameters with default throughput. To support large-scale, high-frequency access patterns, you can combine advanced parameters with higher throughput. In general, increasing throughput is necessary when your application exceeds default TPS limits (for example, during bursts of concurrent reads or writes), regardless of which parameter tier you use.

For more information about maximum throughput and other Parameter Store quotas, see [AWS Systems Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm).

## Changing the throughput setting in Parameter Store
<a name="parameter-store-throughput-increasing"></a>

The following procedures describe how to use Systems Manager to change the number of transactions per second that Parameter Store can process for the current AWS account and AWS Region. You can change the setting at any time.

------
#### [ Console ]

**To change Parameter Store throughput using the console**
**Tip**  
If you haven't created a parameter yet, you can use the AWS Command Line Interface (AWS CLI) or AWS Tools for Windows PowerShell to change throughput. For information, see [Changing the throughput setting in Parameter Store](#parameter-store-throughput-increasing).

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Parameter Store**.

1. Choose the **Settings** tab.

1. Choose the **Manage settings**.

1. In the **Parameter throughput** section, choose an option.

1. If prompted, select the option to approve the changes and authorize charges. Choose **Save settings**.

------
#### [ CLI ]

**To change Parameter Store throughput using the AWS CLI**

1. Open the AWS CLI and run the `aws ssm update-service-setting` command to increase or decrease the transactions per second that Parameter Store can process in the current AWS account and AWS Region. The following example increases the throughput to the high level.

   ```
   aws ssm update-service-setting \
   --setting-id arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/parameter-store/high-throughput-enabled \
   --setting-value true
   ```

   There is no output if the command succeeds. To turn off high throughput, set `--setting-value` to `false`.

1. Run the following command to view the current throughput service settings for Parameter Store in the current AWS account and AWS Region.

   ```
   aws ssm get-service-setting \
   --setting-id arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/parameter-store/high-throughput-enabled
   ```

   The system returns information similar to the following:

   ```
   {
       "ServiceSetting": {
           "SettingId": "/ssm/parameter-store/high-throughput-enabled",
           "SettingValue": "true",
           "LastModifiedDate": 1556551683.923,
           "LastModifiedUser": "arn:aws:sts::123456789012:assumed-role/Administrator/Jasper",
           "ARN": "arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled",
           "Status": "Customized"
       }
   }
   ```

------
#### [ PowerShell ]

**To change Parameter Store throughput using PowerShell**

1. Increase or decrease Parameter Store throughput in the current AWS account and AWS Region using the AWS Tools for PowerShell (Tools for PowerShell). The following example set throughput to the high level.

   ```
   Update-SSMServiceSetting -SettingId "arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/parameter-store/high-throughput-enabled" -SettingValue "true" -Region {{region}}
   ```

   There is no output if the command succeeds.

1. Run the following command to view the current throughput service settings for Parameter Store in the current AWS account and AWS Region.

   ```
   Get-SSMServiceSetting -SettingId "arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/parameter-store/high-throughput-enabled" -Region {{region}}
   ```

   The system returns information similar to the following:

   ```
   ARN              : arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled
   LastModifiedDate : 4/29/2019 3:35:44 PM
   LastModifiedUser : arn:aws:sts::123456789012:assumed-role/Administrator/Jasper
   SettingId        : /ssm/parameter-store/high-throughput-enabled
   SettingValue     : true
   Status           : Customized
   ```

------