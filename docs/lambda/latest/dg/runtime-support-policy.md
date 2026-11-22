

# Runtime deprecation

This topic describes how Lambda deprecates runtimes, what happens to Lambda Event Functions that use deprecated runtimes, and how to get notified about upcoming deprecations.

**Note**  
This topic applies to Lambda-managed runtimes. If your function uses a [customer-managed runtime](runtimes-customer-managed.md), the runtime publisher sets the deprecation schedule, and Lambda doesn't send deprecation notifications for it. For more information, see [Runtime lifecycle](cmr-lifecycle.md).

## Runtime deprecation policy
<a name="runtime-deprecation-policy"></a>

Lambda runtimes for .zip file archives combine an operating system, a programming language, and software libraries. These components receive maintenance and security updates. Lambda deprecates a runtime when any major component reaches the end of community long-term support (LTS) and security updates are no longer available. This component is most often the language runtime. In some cases, Lambda deprecates a runtime because the operating system (OS) reaches end of LTS.

After a runtime is deprecated, we may no longer apply security patches or updates to that runtime, and functions using that runtime are no longer eligible for technical support. Such deprecated runtimes are provided 'as-is', without any warranties, and may contain bugs, errors, defects, or other vulnerabilities.

To learn more about managing runtime upgrades and deprecation, see the following sections and [Managing AWS Lambda runtime upgrades](https://aws.amazon.com/blogs/compute/managing-aws-lambda-runtime-upgrades/) on the *AWS Compute Blog*.

**Important**  
Lambda occasionally delays deprecation of a Lambda runtime for a limited period beyond the end of support date of the language version that the runtime supports. During this period, Lambda only applies security patches to the runtime OS. Lambda doesn't apply security patches to programming language runtimes after they reach their end of support date.

## Shared responsibility model
<a name="runtimes-shared-responsibility"></a>

 Lambda curates and publishes security updates for all supported managed runtimes and container base images. By default, Lambda applies these updates automatically to functions that use managed runtimes. If you changed the default automatic runtime update setting, see the [runtime management controls shared responsibility model](runtime-management-configure-settings.md#runtime-management-shared). For functions deployed using container images, you're responsible for the updates. Rebuild your function's container image from the latest base image, and then redeploy it. 

 When a runtime is deprecated, Lambda's responsibility for updating the managed runtime and container base images ceases. You are responsible for upgrading your functions to use a supported runtime or base image. 

 In all cases, you are responsible for applying updates to your function code, including its dependencies. Your responsibilities under the shared responsibility model are summarized in the following table.


| Runtime lifecycle phase | Lambda's responsibilities | Your responsibilities | 
| --- | --- | --- | 
| Supported managed runtime | Provide regular runtime updates with security patches and other updates.<br />Apply runtime updates automatically by default (see [Runtime update modes](runtimes-update.md#runtime-management-controls) for non-default behaviors). | Update your function code, including dependencies, to address any security vulnerabilities. | 
| Supported container image | Provide regular updates to container base image with security patches and other updates. | Update your function code, including dependencies, to address any security vulnerabilities.<br />Regularly re-build and re-deploy your container image using the latest base image. | 
| Managed runtime approaching deprecation | Notify customers before runtime deprecation through documentation, Health Dashboard, email, and Trusted Advisor.<br />Responsibility for runtime updates ends at deprecation. | Monitor Lambda documentation, Health Dashboard, email, or Trusted Advisor for runtime deprecation information.<br />Upgrade functions to a supported runtime before the previous runtime is deprecated. | 
| Container image approaching deprecation | Deprecation notifications are not available for functions using container images.<br />Responsibility for container base image updates ends at deprecation. | Be aware of deprecation schedules and upgrade functions to a supported base image before the previous image is deprecated. | 

## Runtime use after deprecation
<a name="runtime-deprecation-levels"></a>

After a runtime is deprecated, we may no longer apply security patches or updates to that runtime, and functions using that runtime are no longer eligible for technical support. You can continue to invoke your functions indefinitely. However, we strongly recommend that you migrate to a supported runtime. Deprecated runtimes are provided 'as-is', without any warranties, and may contain bugs, errors, defects, or other vulnerabilities. Functions that use a deprecated runtime may also experience degraded performance or other issues, such as a certificate expiry, that can cause them to stop working properly.

You can update a function to use a newer supported runtime at any time after a runtime is deprecated. We recommend testing your function with the new runtime before applying changes in production environments. You will not be able to revert to the deprecated runtime after function updates are blocked. We recommend using function [versions](configuration-versions.md) and [aliases](configuration-aliases.md) to enable safe deployment with rollback.

If you can't migrate your functions before a runtime is deprecated, you can extend support by creating a [customer-managed runtime](runtimes-customer-managed.md) for that language version. You then control the runtime's patching and deprecation schedule. After Lambda deprecates a runtime, Lambda no longer updates the matching base image, so you're responsible for patching all components of your runtime, including the language runtime. For more information, see [Building a runtime image from a Lambda base image](cmr-base-images.md).

The following timeline describes what happens when a runtime is deprecated:


| Runtime lifecycle phase | When | What | 
| --- | --- | --- | 
| Deprecation notice period | At least 180 days before deprecation |  +  We send notifications through email and the Health Dashboard to accounts that have functions using this runtime in their `$LATEST` version. <br />+  Affected functions are also listed in the [Health Dashboard Scheduled changes tab](https://docs.aws.amazon.com/health/latest/ug/aws-health-account-views.html) and the [AWS Trusted Advisor deprecated runtimes check](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#aws-lambda-functions-deprecated-runtimes).   | 
| Deprecation | Deprecation date |  +  We may no longer apply security updates or other updates. <br />+  Functions are no longer eligible for technical support. <br />+  You can no longer create or update functions using the deprecated runtime in the Lambda console. You can continue to create and update functions through the AWS CLI, AWS SAM, or CloudFormation.   | 
| Block function create | At least 30 days after deprecation |  +  Lambda begins blocking creation of new functions. <br />+  You can continue to update code and configuration for existing functions through the AWS CLI, AWS SAM, or CloudFormation.   | 
| Block function update | At least 60 days after deprecation |  +  Lambda begins blocking the update of code and configuration for existing functions. <br />+  You can still upgrade the function configuration to a supported runtime. However, rolling back to the deprecated runtime may be blocked.   | 

**Note**  
For some runtimes, we are delaying the block-function-create and block-function-update dates beyond the usual 30 and 60 days after deprecation. We have made this change in response to customer feedback. This change gives you more time to upgrade your functions. Refer to the tables in [Supported runtimes](lambda-runtimes.md#runtimes-supported) and [Deprecated runtimes](#runtimes-deprecated) to see the dates for your runtime. Lambda will not start blocking function creates or updates before the dates given in these tables.

## Receiving runtime deprecation notifications
<a name="runtime-deprecation-notify"></a>

When a runtime approaches its deprecation date, Lambda sends you an email alert if any functions in your AWS account use that runtime. Notifications are also displayed in the Health Dashboard and in AWS Trusted Advisor.
+ Receiving email notifications:

  Lambda sends you an email alert at least **180 days** before a runtime is deprecated. This email lists the $LATEST versions of all functions using the runtime. To see a full list of affected function versions, use Trusted Advisor or see [Retrieve data about Lambda Event Functions that use a deprecated runtime](#runtimes-list-deprecated).

  Lambda sends email notification to your AWS account's primary account contact. For information about viewing or updating the email addresses in your account, see [Updating contact information](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html) in the *AWS General Reference*.
+ Receiving notifications through the Health Dashboard:

  The Health Dashboard displays a notification at least **180 days** before a runtime is deprecated. Notifications appear on the **Your account health** page under [Other notifications](https://health.aws.amazon.com/health/home#/account/dashboard/other-notifications). The **Affected resources** tab of the notification lists the $LATEST versions of all functions using the runtime.
**Note**  
To see a full and up-to-date list of affected function versions, use Trusted Advisor or see [Retrieve data about Lambda Event Functions that use a deprecated runtime](#runtimes-list-deprecated).

  Health Dashboard notifications expire 90 days after the affected runtime is deprecated.
+ Using AWS Trusted Advisor

  Trusted Advisor displays a notification at least **180 days** before a runtime is deprecated. Notifications appear on the [Security](https://console.aws.amazon.com/trustedadvisor/home#/category/security) page. A list of your affected functions is displayed under **AWS Lambda Functions Using Deprecated Runtimes**. This list of functions shows both $LATEST and published versions and updates automatically to reflect your functions' current status.

  You can turn on weekly email notifications from Trusted Advisor in the [Preferences](https://console.aws.amazon.com/trustedadvisor/home?#/preferences) page of the Trusted Advisor console.

## Retrieve data about Lambda Event Functions that use a deprecated runtime
<a name="runtimes-list-deprecated"></a>

When a Lambda runtime is approaching deprecation, Lambda alerts you through email and provides notifications in the Health Dashboard and Trusted Advisor. These emails and notifications list the $LATEST versions of functions using the runtime. To list all of your Event Function versions that use a particular runtime, you can use the AWS Command Line Interface (AWS CLI) or one of the AWS SDKs.

If you have a large number of functions which use a runtime that is due to be deprecated, you can also use the AWS CLI or AWS SDKs to help you prioritize updates to your most commonly invoked functions.

Refer to the following sections to learn how to use the AWS CLI and AWS SDKs to gather data about Event Functions that use a particular runtime.

### Listing function versions that use a particular runtime
<a name="runtimes-list-deprecated-versions"></a>

To list all versions of your Lambda Event Functions that use a particular runtime, run the following AWS CLI command. This command doesn't return Lambda Web Functions. Replace `RUNTIME_IDENTIFIER` with the name of the runtime that's being deprecated and choose your own AWS Region. To list only $LATEST function versions, omit `--function-version ALL` from the command.

```
aws lambda list-functions --function-version ALL --region {{us-east-1}} --output text --query "Functions[?Runtime=='{{RUNTIME_IDENTIFIER}}'].FunctionArn" 
```

**Tip**  
The example command lists functions in the `us-east-1` Region for a particular AWS account. Repeat this command for each Region in which your account has functions and for each of your AWS accounts.

This example applies only to Lambda-managed runtimes. Functions that use a customer-managed runtime have the `Runtime` value `custom`, so the command doesn't return them. To find functions that use a customer-managed runtime, see [Find functions that use a customer-managed runtime](cmr-using.md#cmr-using-list-functions).

You can also list Event Functions that use a particular runtime using one of the AWS SDKs. The following example code uses the V3 AWS SDK for JavaScript and the AWS SDK for Python (Boto3) to return a list of the function ARNs for functions using a particular runtime. The example code also returns the CloudWatch log group for each of the listed functions. You can use this log group to find the last invocation date for the function. See the following section [Identifying most commonly and most recently invoked functions](#runtimes-list-deprecated-statistics) for more information.

------
#### [ Node.js ]

**Example JavaScript code to list functions using a particular runtime**  

```js
import { LambdaClient, ListFunctionsCommand } from "@aws-sdk/client-lambda";
const lambdaClient = new LambdaClient();

const command = new ListFunctionsCommand({
    FunctionVersion: "ALL",
    MaxItems: 50
});
const response = await lambdaClient.send(command);

for (const f of response.Functions){
    if (f.Runtime == '{{<your_runtime>}}'){ // Use the runtime id, e.g. 'nodejs24.x' or 'python3.14'
        console.log(f.FunctionArn);
        // get the CloudWatch log group of the function to
        // use later for finding the last invocation date
        console.log(f.LoggingConfig.LogGroup);
    }   
}
// If your account has more functions than the specified
// MaxItems, use the returned pagination token in the 
// next request with the 'Marker' parameter
if ('NextMarker' in response){
    let paginationToken = response.NextMarker;
  }
```

------
#### [ Python ]

**Example Python code to list functions using a particular runtime**  

```python
import boto3
from botocore.exceptions import ClientError

def list_lambda_functions(target_runtime):

    lambda_client = boto3.client('lambda')
    
    response = lambda_client.list_functions(
        FunctionVersion='ALL',
        MaxItems=50
    )
    if not response['Functions']:
            print("No Lambda functions found")
    else: 
        for function in response['Functions']:   
            if function['PackageType']=='Zip' and function['Runtime'] == target_runtime: 
                print(function['FunctionArn'])
                # Print the CloudWatch log group of the function
                # to use later for finding last invocation date
                print(function['LoggingConfig']['LogGroup'])

    if 'NextMarker' in response:
       pagination_token = response['NextMarker']

if __name__ == "__main__":
    # Replace python3.12 with the appropriate runtime ID for your Lambda functions
    list_lambda_functions('{{python3.12}}')
```

------

To learn more about using an AWS SDK to list your functions using the [ListFunctions](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctions.html) action, see the [SDK documentation](https://aws.amazon.com/developer/tools/) for your preferred programming language.

You can also use the AWS Config Advanced queries feature to list all your Lambda Event Functions that use an affected runtime. AWS Config doesn't return Lambda Web Functions. This query only returns function $LATEST versions, but you can aggregate queries to list function across all regions and multiple AWS accounts with a single command. To learn more, see [Querying the Current Configuration State of AWS Auto Scaling Resources](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html) in the *AWS Config Developer Guide*.

### Identifying most commonly and most recently invoked functions
<a name="runtimes-list-deprecated-statistics"></a>

If your AWS account contains functions that use a runtime that's due to be deprecated, you might want to prioritize updating functions that are frequently invoked or functions that have been invoked recently.

If you have only a few functions, you can use the CloudWatch Logs console to gather this information by looking at your functions' log streams. See [View log data sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#ViewingLogData) for more information.

To see the number of recent function invocations, you can also use the CloudWatch metrics information shown in the Lambda console. To view this information, do the following:

1. Open the [Event Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Select the function you want to see invocation statistics for.

1. Choose the **Monitor** tab.

1. Set the time period you wish to view statistics for using the date range picker. Recent invocations are displayed in the **Invocations** pane.

For accounts with larger numbers of functions, it can be more efficient to gather this data programmatically using the AWS CLI or one of the AWS SDKs using the [DescribeLogStreams](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.html) and [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) API actions.

The following examples provide code snippets using the V3 AWS SDK for JavaScript and the AWS SDK for Python (Boto3) to identify the last invoke date for a particular function and to determine the number of invocations for a particular function in the last 14 days.

------
#### [ Node.js ]

**Example JavaScript code to find last invocation time for a function**  

```js
import { CloudWatchLogsClient, DescribeLogStreamsCommand } from "@aws-sdk/client-cloudwatch-logs";
const cloudWatchLogsClient = new CloudWatchLogsClient();
const command = new DescribeLogStreamsCommand({
    logGroupName: '{{<your_log_group_name>}}',
    orderBy: 'LastEventTime',
    descending: true,
    limit: 1
});
try {
    const response = await cloudWatchLogsClient.send(command);
    const lastEventTimestamp = response.logStreams.length > 0 ? 
        response.logStreams[0].lastEventTimestamp : null;
    // Convert the UNIX timestamp to a human-readable format for display
    const date = new Date(lastEventTimestamp).toLocaleDateString();
    const time = new Date(lastEventTimestamp).toLocaleTimeString();
    console.log(`${date} ${time}`);
    
} catch (e){
    console.error('Log group not found.')
}
```

------
#### [ Python ]

**Example Python code to find last invocation time for a function**  

```python
import boto3
from datetime import datetime

cloudwatch_logs_client  = boto3.client('logs')

response = cloudwatch_logs_client.describe_log_streams(
    logGroupName='{{<your_log_group_name>}}',
    orderBy='LastEventTime',
    descending=True,
    limit=1
)

try:
    if len(response['logStreams']) > 0:
        last_event_timestamp = response['logStreams'][0]['lastEventTimestamp']
        print(datetime.fromtimestamp(last_event_timestamp/1000)) # Convert timestamp from ms to seconds
    else:
        last_event_timestamp = None
except:
    print('Log group not found')
```

------

**Tip**  
You can find your function's log group name using the [ListFunctions](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctions.html) API operation. See the code in [Listing function versions that use a particular runtime](#runtimes-list-deprecated-versions) for an example of how to do this.

------
#### [ Node.js ]

**Example JavaScript code to find number of invocations in last 14 days**  

```js
import { CloudWatchClient, GetMetricStatisticsCommand } from "@aws-sdk/client-cloudwatch";
const cloudWatchClient = new CloudWatchClient();
const command = new GetMetricStatisticsCommand({
    Namespace: 'AWS/Lambda',
    MetricName: 'Invocations',
    StartTime: new Date(Date.now()-86400*1000*14), // 14 days ago
    EndTime: new Date(Date.now()),
    Period: 86400 * 14, // 14 days.
    Statistics: ['Sum'],
    Dimensions: [{
        Name: 'FunctionName',
        Value: '{{<your_function_name>}}'
    }]
});
const response = await cloudWatchClient.send(command);
const invokesInLast14Days = response.Datapoints.length > 0 ? 
    response.Datapoints[0].Sum : 0;

console.log('Number of invocations: ' + invokesInLast14Days);
```

------
#### [ Python ]

**Example Python code to find number of invocations in last 14 days**  

```python
import boto3
from datetime import datetime, timedelta

cloudwatch_client = boto3.client('cloudwatch')

response = cloudwatch_client.get_metric_statistics(
    Namespace='AWS/Lambda',
    MetricName='Invocations',
    Dimensions=[
        {
            'Name': 'FunctionName',
            'Value': '{{<your_function_name>}}'
        },
    ],
    StartTime=datetime.now() - timedelta(days=14),
    EndTime=datetime.now(),
    Period=86400 * 14, # 14 days
    Statistics=[
        'Sum'
    ]
)

if len(response['Datapoints']) > 0:
    invokes_in_last_14_days = int(response['Datapoints'][0]['Sum'])
else:
    invokes_in_last_14_days = 0

print(f'Number of invocations: {invokes_in_last_14_days}')
```

------

## Deprecated runtimes
<a name="runtimes-deprecated"></a>

The following runtimes have reached end of support:


| Name | Identifier | Operating system | Deprecation date | Block function create | Block function update | 
| --- | --- | --- | --- | --- | --- | 
| .NET 8 |  dotnet8  | Amazon Linux 2023 |  Nov 10, 2026  |  Jul 29, 2027  |  Aug 31, 2027  | 
| .NET 9 (container only) |  dotnet9  | Amazon Linux 2023 |  Nov 10, 2026  |  N/A  |  N/A  | 
| Python 3.10 |  python3.10  | Amazon Linux 2 |  Oct 31, 2026  |  Jul 29, 2027  |  Aug 31, 2027  | 
| OS-only Runtime |  provided.al2  | Amazon Linux 2 |  Jul 31, 2026  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Node.js 20 |  nodejs20.x  | Amazon Linux 2023 |  Apr 30, 2026  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Ruby 3.2 |  ruby3.2  | Amazon Linux 2 |  Mar 31, 2026  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Python 3.9 |  python3.9  | Amazon Linux 2 |  Dec 15, 2025  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Node.js 18 |  nodejs18.x  | Amazon Linux 2 |  Sep 1, 2025  |  Jul 29, 2027  |  Aug 31, 2027  | 
| .NET 6 |  dotnet6  | Amazon Linux 2 |  Dec 20, 2024  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Python 3.8 |  python3.8  | Amazon Linux 2 |  Oct 14, 2024  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Node.js 16 |  nodejs16.x  | Amazon Linux 2 |  Jun 12, 2024  |  Jul 29, 2027  |  Aug 31, 2027  | 
| .NET 7 (container only) |  dotnet7  | Amazon Linux 2 |  May 14, 2024  |  N/A  |  N/A  | 
| Java 8 |  java8  | Amazon Linux |  Jan 8, 2024  |  Feb 8, 2024  |  Aug 31, 2027  | 
| Go 1.x |  go1.x  | Amazon Linux |  Jan 8, 2024  |  Feb 8, 2024  |  Aug 31, 2027  | 
| OS-only Runtime |  provided  | Amazon Linux |  Jan 8, 2024  |  Feb 8, 2024  |  Aug 31, 2027  | 
| Ruby 2.7 |  ruby2.7  | Amazon Linux 2 |  Dec 7, 2023  |  Jan 9, 2024  |  Aug 31, 2027  | 
| Node.js 14 |  nodejs14.x  | Amazon Linux 2 |  Dec 4, 2023  |  Jan 9, 2024  |  Aug 31, 2027  | 
| Python 3.7 |  python3.7  | Amazon Linux |  Dec 4, 2023  |  Jan 9, 2024  |  Aug 31, 2027  | 
| .NET Core 3.1 |  dotnetcore3.1  | Amazon Linux 2 |  Apr 3, 2023  |  Apr 3, 2023  |  May 3, 2023  | 
| Node.js 12 |  nodejs12.x  | Amazon Linux 2 |  Mar 31, 2023  |  Mar 31, 2023  |  Apr 30, 2023  | 
| Python 3.6 |  python3.6  | Amazon Linux |  Jul 18, 2022  |  Jul 18, 2022  |  Aug 29, 2022  | 
| .NET 5 (container only) |  dotnet5.0  | Amazon Linux 2 |  May 10, 2022  |  N/A  |  N/A  | 
| .NET Core 2.1 |  dotnetcore2.1  | Amazon Linux |  Jan 5, 2022  |  Jan 5, 2022  |  Apr 13, 2022  | 
| Node.js 10 |  nodejs10.x  | Amazon Linux 2 |  Jul 30, 2021  |  Jul 30, 2021  |  Feb 14, 2022  | 
| Ruby 2.5 |  ruby2.5  | Amazon Linux |  Jul 30, 2021  |  Jul 30, 2021  |  Mar 31, 2022  | 
| Python 2.7 |  python2.7  | Amazon Linux |  Jul 15, 2021  |  Jul 15, 2021  |  May 30, 2022  | 
| Node.js 8.10 |  nodejs8.10  | Amazon Linux |  Mar 6, 2020  |  Feb 4, 2020  |  Mar 6, 2020  | 
| Node.js 4.3 |  nodejs4.3  | Amazon Linux |  Mar 5, 2020  |  Feb 3, 2020  |  Mar 5, 2020  | 
| Node.js 4.3 edge |  nodejs4.3-edge  | Amazon Linux |  Mar 5, 2020  |  Mar 31, 2019  |  Apr 30, 2019  | 
| Node.js 6.10 |  nodejs6.10  | Amazon Linux |  Aug 12, 2019  |  Jul 12, 2019  |  Aug 12, 2019  | 
| .NET Core 1.0 |  dotnetcore1.0  | Amazon Linux |  Jun 27, 2019  |  Jun 30, 2019  |  Jul 30, 2019  | 
| .NET Core 2.0 |  dotnetcore2.0  | Amazon Linux |  May 30, 2019  |  Apr 30, 2019  |  May 30, 2019  | 
| Node.js 0.10 |  nodejs  | Amazon Linux |  Aug 30, 2016  |  Sep 30, 2016  |  Oct 31, 2016  | 

In almost all cases, the end-of-life date of a language version or operating system is known well in advance. The following links give end-of-life schedules for each language that Lambda supports as a managed runtime.

**Language and framework support policies**
+ **Node.js** – [github.com](https://github.com/nodejs/Release#release-schedule)
+ **Python** – [devguide.python.org](https://devguide.python.org/versions/#versions)
+ **Ruby** – [www.ruby-lang.org](https://www.ruby-lang.org/en/downloads/branches/)
+ **Java** – [www.oracle.com](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) and [Corretto FAQs](https://aws.amazon.com/corretto/faqs/)
+ **Go** – [golang.org](https://golang.org/doc/devel/release.html)
+ **.NET** – [dotnet.microsoft.com](https://dotnet.microsoft.com/platform/support/policy/dotnet-core)