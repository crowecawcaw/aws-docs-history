# Activating and managing Lambda SnapStart

To use SnapStart, activate SnapStart on a new or existing Lambda function. Then, publish and invoke a function version.

###### Topics

- [Activating SnapStart (console)](#snapshot-console "#snapshot-console")
- [Activating SnapStart (AWS CLI)](#snapshot-cli "#snapshot-cli")
- [Activating SnapStart (API)](#snapshot-api "#snapshot-api")
- [Lambda SnapStart and function states](#snapstart-function-states "#snapstart-function-states")
- [Updating a snapshot](#update-snapshot "#update-snapshot")
- [Using SnapStart with AWS SDKs](#snapstart-credentials "#snapstart-credentials")
- [Using SnapStart with CloudFormation, AWS SAM, and AWS CDK](#snapstart-cfn-sam "#snapstart-cfn-sam")
- [Deleting snapshots](#snapshot-delete "#snapshot-delete")

## Activating SnapStart (console)

###### To activate SnapStart for a function

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the name of a function.
3. Choose **Configuration**, and then choose **General
   configuration**.
4. On the **General configuration** pane, choose **Edit**.
5. On the **Edit basic settings** page, for **SnapStart**, choose
   **Published versions**.
6. Choose **Save**.
7. [Publish a function version](configuration-versions.md#configuration-versions-config "configuration-versions.md#configuration-versions-config"). Lambda initializes your
   code, creates a snapshot of the initialized execution environment, and then caches the snapshot for
   low-latency access.
8. [Invoke the function version](configuration-versions.md#versioning-versions-using "configuration-versions.md#versioning-versions-using").

## Activating SnapStart (AWS CLI)

###### To activate SnapStart for an existing function

1. Update the function configuration by running the [update-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html") command with the **--snap-start** option.

```
`aws lambda update-function-configuration \
 --function-name my-function \
 --snap-start ApplyOn=PublishedVersions`
```

2. Publish a function version with the [publish-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html") command.

```
`aws lambda publish-version \
 --function-name my-function`
```

3. Confirm that SnapStart is activated for the function version by running the [get-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-configuration.html") command and specifying the version number. The following example
   specifies version 1.

```
`aws lambda get-function-configuration \
 --function-name my-function:`1``
```

If the response shows that [OptimizationStatus](../api/API_SnapStartResponse.md "../api/API_SnapStartResponse.md") is `On` and [State](../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State "../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State") is `Active`, then SnapStart is activated and a snapshot is available for the specified function version.

```
"SnapStart": {
    "ApplyOn": "PublishedVersions",
    `"OptimizationStatus": "On"`
 },
 `"State": "Active"`,
```

4. Invoke the function version by running the [invoke](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html")
   command and specifying the version. The following example invokes version 1.

```
`aws lambda invoke \
 --cli-binary-format raw-in-base64-out \
 --function-name my-function:`1` \
 --payload '{ "name": "Bob" }' \
 response.json`
```

The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](../../../cli/latest/userguide/cli-configure-options.md#cli-configure-options-list "../../../cli/latest/userguide/cli-configure-options.md#cli-configure-options-list") in the _AWS Command Line Interface User Guide for Version 2_.

###### To activate SnapStart when you create a new function

1. Create a function by running the [create-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html") command with the **--snap-start** option. For
   **--role**, specify the Amazon Resource Name (ARN) of your [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md").

```
`aws lambda create-function \
 --function-name `my-function` \
 --runtime "`java25`" \
 --zip-file fileb://my-function.zip \
 --handler my-function.handler \
 --role `arn:aws:iam::111122223333:role/lambda-ex` \
 --snap-start ApplyOn=PublishedVersions`
```

2. Create a version with the [publish-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html") command.

```
`aws lambda publish-version \
 --function-name `my-function``
```

3. Confirm that SnapStart is activated for the function version by running the [get-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-configuration.html") command and specifying the version number. The following example
   specifies version 1.

```
`aws lambda get-function-configuration \
 --function-name my-function:`1``
```

If the response shows that [OptimizationStatus](../api/API_SnapStartResponse.md "../api/API_SnapStartResponse.md") is `On` and [State](../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State "../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State") is `Active`, then SnapStart is activated and a snapshot is available for the specified function version.

```
"SnapStart": {
     "ApplyOn": "PublishedVersions",
     `"OptimizationStatus": "On"`
  },
  `"State": "Active"`,
```

4. Invoke the function version by running the [invoke](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html")
   command and specifying the version. The following example invokes version 1.

```
`aws lambda invoke \
 --cli-binary-format raw-in-base64-out \
 --function-name my-function:`1` \
 --payload '{ "name": "Bob" }' \
 response.json`
```

The **cli-binary-format** option is required if you're using AWS CLI version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](../../../cli/latest/userguide/cli-configure-options.md#cli-configure-options-list "../../../cli/latest/userguide/cli-configure-options.md#cli-configure-options-list") in the _AWS Command Line Interface User Guide for Version 2_.

## Activating SnapStart (API)

###### To activate SnapStart

1. Do one of the following:
   - Create a new function with SnapStart activated by using the [CreateFunction](../api/API_CreateFunction.md "../api/API_CreateFunction.md") API action
     with the [SnapStart](../api/API_SnapStart.md "../api/API_SnapStart.md") parameter.
   - Activate SnapStart for an existing function by using the [UpdateFunctionConfiguration](../api/API_UpdateFunctionConfiguration.md "../api/API_UpdateFunctionConfiguration.md")
     action with the [SnapStart](../api/API_SnapStart.md "../api/API_SnapStart.md") parameter.

2. Publish a function version with the [PublishVersion](../api/API_PublishVersion.md "../api/API_PublishVersion.md") action. Lambda
   initializes your code, creates a snapshot of the initialized execution environment, and then caches the
   snapshot for low-latency access.
3. Confirm that SnapStart is activated for the function version by using the [GetFunctionConfiguration](../api/API_GetFunctionConfiguration.md "../api/API_GetFunctionConfiguration.md")
   action. Specify a version number to confirm that SnapStart is activated for that version. If the response shows that [OptimizationStatus](../api/API_SnapStartResponse.md "../api/API_SnapStartResponse.md") is `On` and [State](../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State "../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State") is `Active`, then SnapStart is activated and a snapshot is available for the specified function version.

```
"SnapStart": {
        "ApplyOn": "PublishedVersions",
        `"OptimizationStatus": "On"`
     },
     `"State": "Active"`,
```

4. Invoke the function version with the [Invoke](../api/API_Invoke.md "../api/API_Invoke.md") action.

## Lambda SnapStart and function states

The following function states can occur when you use SnapStart.

**Pending**

Lambda is initializing your code and taking a snapshot of
the initialized execution environment. Any invocations or other API actions that operate
on the function version will fail.

**Active**

Snapshot creation is complete and you can invoke the
function. To use SnapStart, you must invoke the published function version, not the
unpublished version ($LATEST).

**Inactive**

The `Inactive` state can occur when Lambda periodically regenerates function snapshots to apply software updates. In this instance, if your function fails to initialize,
the function can enter an `Inactive` state.

For functions using a Java runtime, Lambda deletes snapshots after 14 days without an invocation. If you invoke the function version after 14 days, Lambda returns a
`SnapStartNotReadyException` response and begins initializing a new snapshot. Wait until the
function version reaches the `Active` state, and then invoke it again.

**Failed**

Lambda encountered an error when running the initialization code or creating the snapshot.

## Updating a snapshot

Lambda creates a snapshot for each published function version. To update a snapshot, publish a new function
version.

## Using SnapStart with AWS SDKs

To make AWS SDK calls from your function, Lambda generates an ephemeral set of credentials by assuming your
function's execution role. These credentials are available as environment variables during your function's
invocation. You don't need to provide credentials for the SDK directly in code. By default, the credential
provider chain sequentially checks each place where you can set credentials and chooses the first
available—usually the environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`,
and `AWS_SESSION_TOKEN`).

###### Note

When SnapStart is activated, the Lambda runtime automatically uses the container credentials (`AWS_CONTAINER_CREDENTIALS_FULL_URI` and `AWS_CONTAINER_AUTHORIZATION_TOKEN`) instead of the access key environment variables. This prevents credentials from expiring before the function is restored.

## Using SnapStart with CloudFormation, AWS SAM, and AWS CDK

- **AWS CloudFormation:** Declare the [SnapStart](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.md") entity in your template.
- **AWS Serverless Application Model (AWS SAM):** Declare the [SnapStart](../../../serverless-application-model/latest/developerguide/sam-resource-function.md#sam-function-snapstart "../../../serverless-application-model/latest/developerguide/sam-resource-function.md#sam-function-snapstart") property in your template.
- **AWS Cloud Development Kit (AWS CDK):** Use the [SnapStartProperty](../../../cdk/api/v2/java/software/amazon/awscdk/services/lambda/CfnFunction.md "../../../cdk/api/v2/java/software/amazon/awscdk/services/lambda/CfnFunction.md") type.

## Deleting snapshots

Lambda deletes snapshots when:

- You delete the function or function version.
- **Java runtimes only** — You don't invoke the function version for 14 days. After 14 days without an invocation, the function
  version transitions to the [Inactive](#snapstart-function-states "#snapstart-function-states") state. If you invoke the function version after 14 days, Lambda returns a
  `SnapStartNotReadyException` response and begins initializing a new snapshot. Wait until the
  function version reaches the [Active](#snapstart-function-states "#snapstart-function-states") state, and then invoke it again.

Lambda removes all resources associated with deleted snapshots in compliance with the General Data Protection Regulation (GDPR).
