

# Using a customer-managed runtime

As a runtime consumer, you use a customer-managed runtime by referencing it in the configuration of your Lambda Event Function. The runtime publisher creates the runtime, publishes its versions, and rolls out updates. You write your function code, deploy it as a .zip file archive, and choose which runtime alias your function uses.

Customer-managed runtimes work with Lambda Event Functions only. You can't use a customer-managed runtime with Lambda Web Functions. For information about runtimes for Web Functions, see [Lambda Web Function runtimes](web-functions-runtimes.md).

Using a customer-managed runtime is the same as using a Lambda-managed runtime, except for how you specify the runtime. Instead of a runtime identifier such as `python3.14`, you specify the Amazon Resource Name (ARN) of the runtime and the name of a runtime alias. Function configuration, invocation, logging, monitoring, layers, and runtime management controls work the same way.

**Important**  
A runtime publisher can push any code into the execution environments of functions that use the runtime. This code runs with the permissions of your function's execution role. Use customer-managed runtimes only from publishers that you trust.  
For third-party runtimes or critical applications, the publisher might make its runtime images available. If so, consider building your own customer-managed runtime from the publisher's container images. You then control when updates reach your functions. For more information, see [Building runtime images](cmr-building-images.md) and [Creating a runtime](cmr-create.md).

## Before you begin
<a name="cmr-using-before"></a>

Before you configure a function to use a customer-managed runtime, get the following information from the runtime publisher:
+ **Runtime ARN** – For example, `arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8`. The runtime must be in the same AWS Region as your function.
+ **Runtime alias name** – For example, `prod`. The publisher decides which aliases exist and which runtime version each alias points to. For more information, see [Alias strategies](cmr-aliases.md#cmr-aliases-strategies).
+ **Runtime documentation** – The publisher defines the handler format, the supported languages and libraries, and how the runtime behaves. Ask for the architectures and features that each alias supports, such as Lambda Managed Instances. Also ask which alias to use for your function. For more information, see [Review the runtime publisher's guidance](#cmr-using-before-guidance).

If your function runs on Lambda Managed Instances, the `Compatibility` object of the runtime alias must show `"ManagedInstances": "Supported"`. To check this value, run the `get-runtime-alias` command. For more information, see [Check the lifecycle of a runtime alias](#cmr-using-check-lifecycle).

You also need the following IAM permissions:
+ `lambda:AssociateRuntimeAlias` on the runtime alias ARN. You need this permission to create or update a function that uses the alias.
+ `lambda:AssociateRuntimeVersion` on the runtime version ARN. You need this permission only to pin your function to a specific runtime version.
+ The usual permissions to create and update functions, such as `lambda:CreateFunction`, `lambda:UpdateFunctionConfiguration`, `lambda:PutRuntimeManagementConfig`, and `iam:PassRole`.

If the runtime is in your own account, an identity-based policy that grants these permissions is enough. If the runtime is in another account, the runtime's resource-based policy must also allow your account to use it. For examples of both policies, see [Grant consumers permission to use a shared runtime](cmr-permissions.md#cmr-permissions-consumer-policy) and [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

**Note**  
When you use a runtime from another account, AWS CloudTrail also delivers a copy of some events to the runtime publisher's account. This applies to requests that reference the runtime, such as creating a function that uses it, changing its runtime alias, or pinning a runtime version. It also applies when Lambda denies these requests. The publisher's copy always shows your account ID. For requests that Lambda allows, it also shows the function ARN. It doesn't show the principal that made the request. For more information, see [Logging customer-managed runtime API calls with CloudTrail](cmr-monitoring.md#cmr-monitoring-cloudtrail).  
The runtime publisher can also see aggregate runtime metrics, such as invocations and errors, for all functions that use the runtime. These metrics don't include function names or account IDs. For more information, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

You don't need access to the publisher's images in Amazon Elastic Container Registry (Amazon ECR). Lambda manages the runtime contents for you.

### Review the runtime publisher's guidance
<a name="cmr-using-before-guidance"></a>

Before you choose a runtime and alias, read the guidance that the runtime publisher provides. The publisher can provide guidance in the following places:
+ **Runtime description and license information** – The runtime's `Description` property tells you what the runtime is for and what it contains. The `LicenseInfo` property lists the licenses for software in the runtime, such as the language runtime and libraries.
+ **Alias descriptions** – Each runtime alias can also have a `Description` property. Publishers typically describe what each alias is for. For example, an alias might be for an environment such as `dev`, `test`, or `prod`. An alias might also track a major or minor version branch of the language. Use the alias descriptions to choose the alias for your function.
+ **Publisher documentation** – Any documentation that the publisher provides outside of Lambda. For example, this documentation can describe the handler format, the supported features, and which alias to use.
+ **Release lifecycle** – If the publisher defined a deprecation lifecycle, the runtime or alias has a `ReleaseLifecycle` property. For more information, see [Runtime lifecycle and function states](#cmr-using-lifecycle).

You can't browse runtimes in other accounts in the Lambda console, because you can't list another account's runtimes. To view a shared runtime, its versions, or its aliases, use the AWS CLI or the Lambda API. You can still choose a shared runtime when you create or update a function in the console by entering the runtime alias ARN.

**To view the runtime and alias descriptions (AWS CLI)**

1. To view the runtime's description and license information, run the `get-runtime` command. For `--runtime-name`, specify the runtime ARN.

   ```bash
   aws lambda-core get-runtime \
     --runtime-name {{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}}
   ```

   The following example shows an excerpt of the output:

   ```json
   {
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
       "Name": "companyphp8",
       "Description": "PHP 8 runtime with company-approved extensions",
       "LicenseInfo": "PHP License v3.01. Includes components under the MIT and Apache-2.0 licenses."
   }
   ```

1. To view the description and lifecycle of each alias, run the `list-runtime-aliases` command. The `--query` option limits the output to the alias name, description, and release lifecycle.

   ```bash
   aws lambda-core list-runtime-aliases \
     --runtime-name {{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}} \
     --query "Items[].{Name: Name, Description: Description, ReleaseLifecycle: ReleaseLifecycle}"
   ```

   You should see output similar to the following:

   ```json
   [
       {
           "Name": "prod",
           "Description": "Production alias for the companyphp8 runtime",
           "ReleaseLifecycle": {
               "ReleaseState": "GA"
           }
       }
   ]
   ```

For a runtime in another account, the publisher must grant `lambda:GetRuntime` and `lambda:ListRuntimeAliases` in the runtime's resource-based policy. For more information, see [Sharing a customer-managed runtime](cmr-permissions.md#cmr-permissions-sharing).

If you can't view these properties, ask the publisher to grant read access to the runtime. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## How a function references a customer-managed runtime
<a name="cmr-using-reference"></a>

To use a customer-managed runtime, set the following properties in your function configuration:
+ `Runtime` – Set to the literal value `custom`.
+ `RuntimeConfig` – An object with the following required fields:
  + `RuntimeArn` – The ARN of the runtime. If the runtime is in your own account, you can specify the runtime name instead. Lambda resolves a name to a runtime in your account. To use a runtime from another account, you must specify the full ARN.
  + `RuntimeAlias` – The name of the runtime alias, such as `prod`. You must always specify an alias.

When your function uses a customer-managed runtime, the `GetFunction`, `GetFunctionConfiguration`, and `ListFunctions` responses include the `RuntimeConfig` object.

You deploy your function code as a .zip file archive, the same way as with a Lambda-managed runtime. The runtime publisher defines the handler format. Check the publisher's documentation for the value to use. Functions that you deploy as [container images](images-create.md) don't use runtimes. You can't use a customer-managed runtime with them.

### What Lambda checks when you create or update a function
<a name="cmr-using-validation"></a>

When you create a function or update its configuration, Lambda checks the runtime configuration. The request fails in any of the following cases:
+ The runtime ARN or alias name isn't in a valid format.
+ The runtime or the runtime alias doesn't exist.
+ You don't have permission to use the runtime alias, or the runtime version that you pin to.
+ Your function's architecture isn't one of the architectures that the alias declares.
+ Your function's Lambda Managed Instances configuration doesn't match what the alias allows.
+ You create a function on or after the alias's function create block date.
+ You update a function on or after the alias's function update block date.

For more information about alias compatibility, see [Alias compatibility](cmr-aliases.md#cmr-aliases-compatibility). For more information about block dates, see [Runtime lifecycle](cmr-lifecycle.md).

Lambda checks your permissions only when you create a function, change its runtime configuration, or pin it to a runtime version. Lambda doesn't check them when you update the function code or other settings, or when it invokes your function. If the publisher later removes your access, your existing function keeps running and keeps receiving alias updates.

## How runtime updates reach your function
<a name="cmr-using-updates"></a>

The runtime publisher releases an update by pointing a runtime alias to a new runtime version. By default, your function uses the new runtime version at its next cold start. You don't need to update or redeploy your function.

Execution environments that are already running keep the previous runtime version until Lambda replaces them. Lambda replaces execution environments from time to time. As a result, an update reaches your function gradually.

Customer-managed runtimes don't use the [two-phase rollout](runtimes-update.md#runtime-management-two-phase) that Lambda uses for Lambda-managed runtimes. The publisher controls when each alias changes. For more information, see [How alias updates reach functions](cmr-aliases.md#cmr-aliases-resolution).

To choose when updates reach your function, use runtime management controls. For more information, see [Controlling runtime updates](#cmr-using-controls).

## Controlling runtime updates
<a name="cmr-using-controls"></a>

Runtime management controls work the same way for customer-managed runtimes as for Lambda-managed runtimes. You use the same `PutRuntimeManagementConfig` and `GetRuntimeManagementConfig` API operations. For more information, see [Runtime update modes](runtimes-update.md#runtime-management-controls).

The runtime update mode determines when Lambda resolves your function's runtime alias to a runtime version. The following table describes each mode for customer-managed runtimes.


**Runtime update modes for customer-managed runtimes**  

| Runtime update mode | When Lambda resolves the alias | When to use it | 
| --- | --- | --- | 
| Auto (default) | At each cold start. | For most functions. Your function receives runtime updates, including security patches, as soon as the publisher releases them. | 
| Function update | When you create or update the function. This includes calls to CreateFunction, UpdateFunctionCode, and UpdateFunctionConfiguration. | To pick up runtime updates only when you deploy your function. You can then test runtime updates together with your code changes. | 
| Manual | Never. Lambda ignores the alias and uses the runtime version that you pin your function to. | To roll back a runtime update that breaks your function, or to freeze the runtime version for a short time. | 

With **Function update** mode, your function's runtime version changes only when you deploy. You're responsible for updating your function regularly so that it picks up security patches.

In **Auto** mode, published function versions follow the runtime alias, the same as `$LATEST`. Every version of your function receives runtime updates automatically, just as with Lambda-managed runtimes.

In **Function update** mode, each published function version keeps the runtime version that it used when you published it. To roll back code, configuration, and runtime version together, shift traffic to an earlier published version. For more information, see [Roll back a runtime version using published function versions](runtime-management-configure-settings.md#runtime-management-rollback-published).

You can set the runtime management configuration separately for each published function version. For example, if a published version uses **Auto** mode and a runtime update breaks it, you can set **Manual** mode on that version. This pins the version to an earlier runtime version. For instructions, see [Pin your function to a runtime version](#cmr-using-pin).

With **Manual** mode, your function still specifies a runtime alias, but Lambda doesn't use it to choose the runtime version. Your function doesn't receive any runtime updates, including security patches. We recommend that you use **Manual** mode only temporarily. When the publisher fixes the issue, return your function to **Auto** mode.

The runtime version that you pin to must support your function's architecture. To pin a function, you need the `lambda:AssociateRuntimeVersion` permission on the runtime version ARN. For instructions, see [Pin your function to a runtime version](#cmr-using-pin).

For more information about responsibilities in each mode, see [Managing Lambda runtime updates](runtime-management-configure-settings.md).

## Layers and extensions
<a name="cmr-using-layers-extensions"></a>

[Layers](chapter-layers.md) work the same way as with Lambda-managed runtimes. You attach layers to your function, and Lambda extracts them to the `/opt` directory in the execution environment. Make sure that the layer contents are compatible with the runtime.

A runtime publisher can include [extensions](lambda-extensions.md) in the runtime. You can also add your own extensions to your function in the `/opt/extensions` directory. Your extensions run alongside the runtime's extensions. If one of your extensions has the same executable name as a runtime extension, only your extension runs, and Lambda logs a warning.

## Runtime lifecycle and function states
<a name="cmr-using-lifecycle"></a>

A runtime publisher can set a release lifecycle on a runtime or a runtime alias, in the `ReleaseLifecycle` property. Not every runtime has a lifecycle. If the publisher defined one, make sure that you understand its dates before you build on the runtime. The lifecycle includes a release state, such as `DEPRECATED`, and optional dates. On or after the function create block date, you can't create functions that use the alias. On or after the function update block date, you can't update them. The block dates don't affect invocations. Your existing functions keep running, and Lambda continues to invoke them.

Lambda doesn't notify you about lifecycle changes for customer-managed runtimes. To plan your migration, check the lifecycle of the alias that your function uses. For instructions, see [Check the lifecycle of a runtime alias](#cmr-using-check-lifecycle). For more information, see [Runtime lifecycle](cmr-lifecycle.md).

Your function is normally in the `Active` [state](functions-states.md). Your function enters the `Inactive` state if the publisher makes one of the following changes:
+ Deletes the runtime alias or runtime version that your function uses.
+ Deletes the container image of the runtime version that your function uses, or removes Lambda's access to the image. This change can take up to 24 hours to take effect.
+ Makes an incompatible change, such as removing an architecture that your function uses.

When your function is `Inactive` for this reason, its `StateReasonCode` is `InvalidRuntime`. Existing execution environments continue to handle invocations. However, Lambda can't create new execution environments for your function, so invocations that require a cold start fail. When the publisher reverts the change, your function returns to the `Active` state automatically. You don't need to update or redeploy your function. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

## Create a function that uses a customer-managed runtime
<a name="cmr-using-create"></a>

When you create the function, specify the runtime ARN and the alias name.

Before you create the function, make sure that you have the following:
+ The runtime ARN and alias name from the runtime publisher
+ Your function code in a .zip file archive
+ An execution role for your function
+ The permissions described in [Before you begin](#cmr-using-before)

**To create an Event Function that uses a customer-managed runtime (console)**

1. Open the [Event Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose **Create Event Function**.

1. For **Function name**, enter a name for your function.

1. Under **Runtime source**, select **Your runtimes**, and then choose **Browse your runtimes**.

1. In the dialog box, select a runtime, and then select a runtime alias.

1. Complete the rest of the page as you would for any other Event Function.

1. Choose **Create Event Function**.

To use a runtime that another account shares with you, at step 4, select **Shared runtimes**. Then paste the runtime alias ARN.

**To create an Event Function that uses a customer-managed runtime (AWS CLI)**

1. To create the function, run the `create-function` command. Set `--runtime` to `custom`, and specify the runtime ARN and alias in `--runtime-config`.

   ```bash
   aws lambda create-function \
     --function-name {{my-function}} \
     --runtime custom \
     --runtime-config RuntimeArn={{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}},RuntimeAlias={{prod}} \
     --handler {{index.handler}} \
     --zip-file fileb://{{function.zip}} \
     --role {{arn:aws:iam::111122223333:role/my-lambda-role}} \
     --architectures {{x86_64}}
   ```

   For `--handler`, use the format that the runtime publisher documents. For `--architectures`, choose an architecture that the alias supports.

   You can also specify `--runtime-config` in JSON format:

   ```bash
   --runtime-config '{"RuntimeArn":"{{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}}","RuntimeAlias":"{{prod}}"}'
   ```

   The output includes the runtime configuration. The following example shows an excerpt of the output:

   ```json
   {
       "FunctionName": "my-function",
       "FunctionArn": "arn:aws:lambda:us-east-1:111122223333:function:my-function",
       "Runtime": "custom",
       "RuntimeConfig": {
           "RuntimeArn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
           "RuntimeAlias": "prod"
       },
       "Handler": "index.handler",
       "Architectures": [
           "x86_64"
       ],
       "State": "Pending"
   }
   ```

1. (Optional) To wait until the function is ready to invoke, run the `wait function-active-v2` command.

   ```bash
   aws lambda wait function-active-v2 \
     --function-name {{my-function}}
   ```

## Change the runtime of an existing function
<a name="cmr-using-switch"></a>

You can move an existing .zip file archive function to a customer-managed runtime. You can also move a function to a different runtime alias, or back to a Lambda-managed runtime. Before you change the runtime, make sure that your function code and handler work with the new runtime.

**To change the runtime of a function (console)**

1. Open the [Event Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of the function to update.

1. On the **Code** tab, under **Runtime settings**, choose **Edit**.

1. Under **Runtime source**, select **Your runtimes**, and then choose **Browse your runtimes**.

1. In the dialog box, select a runtime, and then select a runtime alias.

1. Choose **Save settings**.

To use a runtime that another account shares with you, at step 4, select **Shared runtimes**. Then paste the runtime alias ARN.

**To switch a function to a customer-managed runtime, or change its alias (AWS CLI)**
+ Run the `update-function-configuration` command. Specify the runtime ARN and the alias that you want to use. If the handler format is different for the new runtime, also specify `--handler`.

  ```bash
  aws lambda update-function-configuration \
    --function-name {{my-function}} \
    --runtime custom \
    --runtime-config RuntimeArn={{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}},RuntimeAlias={{prod}} \
    --handler {{index.handler}}
  ```

  To move to a different alias, such as from `test` to `prod`, run the same command with the new alias name.

**To switch a function back to a Lambda-managed runtime (AWS CLI)**
+ Run the `update-function-configuration` command, and specify a Lambda runtime identifier. You don't need to clear the runtime configuration. Lambda doesn't use `RuntimeConfig` when `Runtime` is a Lambda runtime identifier.

  ```bash
  aws lambda update-function-configuration \
    --function-name {{my-function}} \
    --runtime {{python3.14}} \
    --handler {{lambda_function.lambda_handler}}
  ```

  If your function code also changes, deploy the new code with the `update-function-code` command.

## Check which runtime version your function uses
<a name="cmr-using-check-version"></a>

You can check the runtime version in your function configuration and in your function logs.

**To check your function's runtime version (AWS CLI)**
+ Run the `get-function-configuration` command.

  ```bash
  aws lambda get-function-configuration \
    --function-name {{my-function}} \
    --query RuntimeVersionConfig
  ```

  You should see output similar to the following:

  ```json
  {
      "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.2"
  }
  ```

  The version name is the last part of the ARN.

  In **Auto** mode, this value is the runtime version that the alias currently points to. New execution environments use this version. Execution environments that are already running might still use the previous version.

Lambda also logs the runtime version in the `INIT_START` log line each time it creates an execution environment. The log line shows the runtime name and version name, followed by the runtime version ARN. For example:

```
INIT_START Runtime Version: companyphp8:v8.3.2 Runtime Version ARN: arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.2
```

To find this log line in the console, open your function's log group in the CloudWatch Logs console. For more information, see [Identifying Lambda runtime version changes](runtimes-update.md#runtime-management-identify).

## Find functions that use a customer-managed runtime
<a name="cmr-using-list-functions"></a>

Functions that use a customer-managed runtime have the `Runtime` value `custom`. For these functions, the `ListFunctions` API operation also returns a `RuntimeConfig` object that contains the `RuntimeArn` and `RuntimeAlias` fields. You can filter on these fields to find functions that use a specific runtime. For example, you might do this before you change or delete a runtime alias, or when the runtime publisher deprecates a runtime.

**To list all functions that use a customer-managed runtime (AWS CLI)**
+ Run the `list-functions` command.

  ```bash
  aws lambda list-functions --function-version ALL \
    --query "Functions[?Runtime=='custom'].{Function:FunctionArn,Runtime:RuntimeConfig.RuntimeArn,Alias:RuntimeConfig.RuntimeAlias}" \
    --output table
  ```

  For each function, the output shows the function ARN, runtime ARN, and runtime alias.

**To list functions that use a specific customer-managed runtime (AWS CLI)**
+ Run the `list-functions` command, and filter on the runtime ARN.

  ```bash
  aws lambda list-functions --function-version ALL \
    --query "Functions[?RuntimeConfig.RuntimeArn=='{{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}}'].{Function:FunctionArn,Alias:RuntimeConfig.RuntimeAlias}" \
    --output table
  ```

  To find only the functions that use a specific runtime alias, also filter on the alias name. For example:

  ```bash
  aws lambda list-functions --function-version ALL \
    --query "Functions[?RuntimeConfig.RuntimeArn=='{{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}}' && RuntimeConfig.RuntimeAlias=='{{prod}}'].FunctionArn" \
    --output table
  ```

  In the response, `RuntimeArn` is always the full runtime ARN, even if you configured the function with the runtime name. Use the full ARN in your filter.

Note the following when you use these commands:
+ The `--function-version ALL` option includes published function versions. If you omit it, the command returns only the unpublished (`$LATEST`) version of each function.
+ The command lists functions in one Region of your AWS account. Repeat the command for each Region where you have functions.
+ The command returns only functions in your own account. A runtime publisher can't list functions in runtime consumer accounts. Instead, publishers can use runtime metrics to see how much a runtime is used. For more information, see [Check usage before you delete or deprecate](cmr-monitoring.md#cmr-monitoring-uses-usage).

## Pin your function to a runtime version
<a name="cmr-using-pin"></a>

If a runtime update breaks your function, roll back by pinning your function to an earlier runtime version. To do this, use the **Manual** runtime update mode. You can also ask the runtime publisher to roll back the alias. For more information, see [Roll back a runtime update](cmr-aliases.md#cmr-aliases-rollback).

Before you pin your function, make sure that you have the following:
+ The ARN of the runtime version to pin to. To find the version that your function used before the update, check earlier `INIT_START` log lines, or ask the runtime publisher.
+ The `lambda:AssociateRuntimeVersion` permission on the runtime version ARN.
+ The `lambda:PutRuntimeManagementConfig` permission.

The steps to pin a function are the same as for functions that use Lambda-managed runtimes. Set the runtime update mode to **Manual**, and specify the full runtime version ARN. For a customer-managed runtime, the runtime version ARN has the format `arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.1`. The version must belong to the same runtime, and it must support your function's architecture. For instructions, see [Configuring the runtime update mode](runtime-management-configure-settings.md#runtime-management-configure-settings-procedures).

New execution environments use the pinned version. To return your function to automatic runtime updates, set the runtime update mode to **Auto**. Your function then uses the version that its alias points to, starting at its next cold start.

## Use Function update mode
<a name="cmr-using-function-update-mode"></a>

To pick up runtime updates only when you deploy your function, use the **Function update** runtime update mode.

The steps to set this mode are the same as for functions that use Lambda-managed runtimes. For instructions, see [Configuring the runtime update mode](runtime-management-configure-settings.md#runtime-management-configure-settings-procedures).

After this change, Lambda resolves the alias each time you create or update the function. Between deployments, your function keeps the same runtime version, even if the publisher updates the alias.

## Check the lifecycle of a runtime alias
<a name="cmr-using-check-lifecycle"></a>

To plan your migration, check the release state and block dates of the alias that your function uses.

In the Lambda console, the lifecycle of a runtime alias appears on the page for the alias. It also appears in the table of aliases on the **Aliases** tab of the runtime.

If the runtime is in another account, you can't view it in the Lambda console. Use the AWS CLI instead.

**To check the lifecycle of a runtime alias (AWS CLI)**
+ Run the `get-runtime-alias` command. For `--runtime-name`, specify the runtime ARN.

  ```bash
  aws lambda-core get-runtime-alias \
    --runtime-name {{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}} \
    --name {{prod}}
  ```

  For a runtime in another account, the publisher must grant you `lambda:GetRuntimeAlias` in the runtime's resource-based policy.

  If the publisher has set a lifecycle, the output includes a `ReleaseLifecycle` object. The following example shows an excerpt of the output:

  ```json
  {
      "Name": "prod",
      "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod",
      "RuntimeVersion": "v8.3.2",
      "ReleaseLifecycle": {
          "ReleaseState": "DEPRECATED",
          "DeprecationDate": "2027-06-30",
          "FunctionCreateBlockDate": "2027-06-30",
          "FunctionUpdateBlockDate": "2027-09-30"
      }
  }
  ```

  If the response doesn't include `ReleaseLifecycle`, the publisher hasn't set a lifecycle for the alias or the runtime.

For more information about release states and dates, see [Release states and lifecycle dates](cmr-lifecycle.md#cmr-lifecycle-properties).

## Infrastructure as code
<a name="cmr-using-iac"></a>

You can also use infrastructure as code tools to define functions that use customer-managed runtimes.

The following AWS CloudFormation template creates a function that uses a customer-managed runtime. You pass in the runtime ARN and the alias name as parameters. You also pass in the ARN of an existing execution role and the Amazon S3 bucket that holds your deployment package.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  RuntimeArn:
    Type: String
    Default: {{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}}
  RuntimeAlias:
    Type: String
    Default: {{prod}}
  ExecutionRoleArn:
    Type: String
  CodeBucket:
    Type: String
Resources:
  Function:
    Type: AWS::Lambda::Function
    Properties:
      Runtime: custom
      RuntimeConfig:
        RuntimeArn: !Ref RuntimeArn
        RuntimeAlias: !Ref RuntimeAlias
      Handler: {{index.handler}}
      Architectures:
        - {{x86_64}}
      Role: !Ref ExecutionRoleArn
      Code:
        S3Bucket: !Ref CodeBucket
        S3Key: {{function.zip}}
```

Note the following about the template:
+ If you specify `RuntimeConfig`, you must set `Runtime` to `custom`.
+ For `RuntimeArn`, specify the runtime ARN, not the runtime alias ARN. For `RuntimeAlias`, specify the alias name.
+ For `Handler`, use the format that the runtime publisher documents. For `Architectures`, choose an architecture that the alias supports.
+ Store your deployment package in an Amazon S3 bucket. CloudFormation supports inline code (`ZipFile`) only for Node.js and Python runtimes.
+ To switch the function to another alias, change the `RuntimeAlias` value and update the stack. CloudFormation updates the function in place.

For more information about the resource properties, see [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html) in the *AWS CloudFormation Template Reference Guide*.

## Getting help
<a name="cmr-using-help"></a>

The runtime publisher is responsible for the runtime's contents and behavior. If you have an issue with the runtime, such as a bug in a language library, contact the runtime publisher.

AWS Support can help you determine whether the runtime or Lambda is the cause of an issue.