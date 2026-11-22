

# Runtime lifecycle

As a runtime publisher, you can use a release lifecycle to show the stage of a customer-managed runtime. The lifecycle tells runtime consumers whether a runtime is in preview, generally available, or deprecated. It also tells them the date when the runtime becomes deprecated. You can also set dates when Lambda starts to block consumers from creating or updating Lambda Event Functions that use the runtime.

The release lifecycle is optional. You can set it on a runtime, on a runtime alias, or on both. This topic is for runtime publishers who set the lifecycle and for runtime consumers who need to understand it.

## Telling consumers about lifecycle changes
<a name="cmr-lifecycle-communication"></a>

Lambda doesn't send notifications about customer-managed runtimes. For example, Lambda doesn't create AWS Health events, send emails, or add AWS Trusted Advisor checks when you deprecate a runtime. As the runtime publisher, you must tell your consumers about lifecycle changes.

Lambda shows the release lifecycle to consumers as a property of each runtime alias. Consumers can view it by using the Lambda API. For runtimes in your own account, you can also use the Lambda console. For more information, see [How runtime consumers see the lifecycle](#cmr-lifecycle-consumers).

We recommend that you announce lifecycle changes through the channels your consumers already use. Examples include internal portals, email lists, release notes, and the runtime or alias description. Give consumers enough time to migrate before any block date.

## Release states and lifecycle dates
<a name="cmr-lifecycle-properties"></a>

You set the lifecycle in the `ReleaseLifecycle` object. It has the following properties. All properties are optional. You specify dates as UTC dates in `yyyy-mm-dd` format.


**ReleaseLifecycle properties**  

| Property | Description | 
| --- | --- | 
| `ReleaseState` | The release state of the runtime or alias. Valid values:+  `PREVIEW` – The runtime is available for early testing and feedback. <br />+  `GA` – The runtime is ready for production use. <br />+  `DEPRECATED` – The runtime is deprecated. We recommend that consumers migrate to a supported runtime or alias.  | 
| `DeprecationDate` | The date when the runtime or alias becomes deprecated. On and after this date, Lambda returns the `ReleaseState` as `DEPRECATED`. | 
| `FunctionCreateBlockDate` | The date when Lambda starts to block `CreateFunction` requests that use the runtime or alias. | 
| `FunctionUpdateBlockDate` | The date when Lambda starts to block `UpdateFunctionCode` and `UpdateFunctionConfiguration` requests for functions that use the runtime or alias. | 

The three dates don't depend on each other. You can set them in any order. For example, you can block function creation before the deprecation date, or you can deprecate the runtime first and block function creation later.

## How Lambda enforces block dates
<a name="cmr-lifecycle-enforcement"></a>

Block dates take effect on the date that you specify, not on the day after. Starting on that date, Lambda enforces the blocks as follows:
+ On and after the `FunctionCreateBlockDate`, `CreateFunction` requests that use the runtime or alias fail.
+ On and after the `FunctionUpdateBlockDate`, `UpdateFunctionCode` and `UpdateFunctionConfiguration` requests for functions that use the runtime or alias fail.

Block dates affect only these three function operations. They don't affect invocations.

The `DeprecationDate` changes the release state that Lambda reports. It doesn't block function operations by itself. To block them, set the block dates.

Deprecation never stops your functions from running. Functions that use the runtime or alias continue to run after the `DeprecationDate`. They also continue to run after the `FunctionCreateBlockDate` and the `FunctionUpdateBlockDate`.

The following table summarizes how block dates and deletion affect function operations. Each column shows the effect of one condition by itself. If more than one condition applies, an operation fails if any of them blocks it.


**Function operations by block date and deletion status**  

| Operation | On or after the function create block date | On or after the function update block date | The runtime alias or pinned runtime version is scheduled for deletion | 
| --- | --- | --- | --- | 
| Create a function that uses the alias (CreateFunction) | Fails | Allowed | Fails | 
| Update the function code (UpdateFunctionCode) | Allowed | Fails | Fails | 
| Update the function configuration to specify the alias (UpdateFunctionConfiguration) | Allowed | Fails | Fails | 
| Update other function configuration, such as memory or timeout (UpdateFunctionConfiguration) | Allowed | Fails | Fails | 
| Pin the function to a runtime version (Manual mode) | Allowed | Allowed. Switching the function back to Auto mode fails. | Fails if the version that you pin to is scheduled for deletion. Pinning to an available version works, and you can then update the function again. | 
| Invoke the function | Allowed | Allowed | Depends on whether the runtime version or runtime alias is scheduled for deletion, and on the function's runtime update mode. For details, see [How deletion affects functions](cmr-delete.md#cmr-delete-function-impact). | 

On or after the function update block date, you can still update the function configuration to move the function to a different alias or runtime.

Block dates don't apply to functions in **Manual** mode. To return such a function to **Auto** or **Function update** mode, its alias must not be blocked.

Consumers can't override block dates for customer-managed runtimes. A consumer who needs more time can create their own customer-managed runtime from your runtime images, if you make the images available. For more information, see [Creating a runtime](cmr-create.md) and [Building runtime images](cmr-building-images.md).

You can also stop consumers from using a runtime by removing their permissions from the runtime's resource-based policy. This blocks new `CreateFunction` and `UpdateFunctionConfiguration` requests that reference the runtime. It doesn't affect functions that already use it. Unlike block dates, a permission change blocks both operations at once. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## Rules for release states and dates
<a name="cmr-lifecycle-consistency"></a>

Lambda makes sure that the `ReleaseState` and `DeprecationDate` agree. The following rules apply when you create or update a release lifecycle:
+ If you set `ReleaseState` to `DEPRECATED`, you must also specify a `DeprecationDate`. The `DeprecationDate` must be today or earlier.
+ If you set `ReleaseState` to `PREVIEW` or `GA`, the `DeprecationDate` must be later than today.
+ If you specify a `ReleaseLifecycle` without a `ReleaseState`, Lambda sets the state to `GA`. If the `DeprecationDate` is today or earlier, Lambda sets the state to `DEPRECATED` instead.

If your request doesn't follow these rules, it fails with a validation error.

When you read a lifecycle, Lambda calculates the state based on today's UTC date. On and after the `DeprecationDate`, Lambda always returns the `ReleaseState` as `DEPRECATED`. This happens automatically. You don't need to update the state yourself.

When you update a runtime or alias, the lifecycle that you specify replaces the lifecycle already stored on that resource. Lambda doesn't merge the lifecycles field by field, so fields that you omit are removed. If an update request doesn't include `ReleaseLifecycle`, Lambda clears the existing lifecycle. This applies to every update, including updates that change only other settings, such as the description. The replacement applies only to the resource that you update. It doesn't combine an alias lifecycle with the runtime lifecycle.

Follow these practices when you update a runtime or alias:
+ To change one lifecycle field, specify the complete lifecycle in your update request. Include all the fields that you want to keep.
+ To keep the lifecycle unchanged when you update other settings, such as the description, include the current lifecycle in the request.
+ To get the current lifecycle, run the `get-runtime` command for a runtime, or the `get-runtime-alias` command for an alias. The `get-runtime-alias` response shows the lifecycle that applies to the alias. If the alias doesn't have its own lifecycle, the response shows the runtime-level lifecycle. In that case, don't add it to the alias update. Otherwise, the alias gets its own lifecycle and no longer follows changes to the runtime-level lifecycle.

If you clear the lifecycle of an alias, the runtime-level lifecycle applies to the alias again.

The `get-runtime-alias` response doesn't show whether the lifecycle belongs to the alias or to the runtime. To check, compare it with the `get-runtime` output. If the two match, the alias might not have its own lifecycle.

## Runtime-level and alias-level lifecycles
<a name="cmr-lifecycle-levels"></a>

You can set a release lifecycle on a runtime, on individual runtime aliases, or on both. Runtime versions don't have a lifecycle.
+ **Runtime level** – The lifecycle applies to all aliases of the runtime that don't have their own lifecycle. Use this approach when your aliases are release stages for the same runtime, such as `dev`, `test`, and `prod`. All stages share one lifecycle, so you set it one time.
+ **Alias level** – The lifecycle applies to one alias. It replaces the runtime-level lifecycle for that alias. Use this approach when your aliases are separate branches of a runtime that you retire at different times. For example, you might have aliases for different operating system versions or major language versions.

If an alias has its own lifecycle, Lambda uses only the alias lifecycle for that alias. Lambda doesn't combine it with the runtime-level lifecycle. The alias doesn't inherit any runtime-level property, even a property that the alias lifecycle doesn't set. If you want an alias to have a block date, set it in the alias lifecycle.

An alias lifecycle is an optional override of the runtime lifecycle. The dates in an alias lifecycle can be earlier or later than the matching dates on the runtime.

For example, a runtime named `java8` has two aliases, `al2` and `al2023`. Each alias uses a different version of Amazon Linux. With the following settings, you can retire the `al2` branch before the rest of the runtime:


**Example: Runtime-level and alias-level deprecation dates**  

| Resource | Lifecycle set on resource | Effective deprecation date | 
| --- | --- | --- | 
| java8 (runtime) | DeprecationDate: 2030-06-30 | 2030-06-30 | 
| al2 (alias) | DeprecationDate: 2027-06-30 | 2027-06-30. The alias lifecycle replaces the runtime lifecycle. | 
| al2023 (alias) | None | 2030-06-30. The alias inherits the runtime lifecycle. | 

In this example, if you later add a `FunctionUpdateBlockDate` to the `java8` runtime lifecycle, the block date applies to `al2023` but not to `al2`. The `al2` alias uses only its own lifecycle.

## How runtime consumers see the lifecycle
<a name="cmr-lifecycle-consumers"></a>

Consumers see the release lifecycle as a property of each runtime alias. When you call `GetRuntimeAlias` or `ListRuntimeAliases`, the `ReleaseLifecycle` in the response is the lifecycle that applies to the alias. If the alias has its own lifecycle, Lambda returns it. Otherwise, Lambda returns the runtime-level lifecycle. If neither is set, the response doesn't include `ReleaseLifecycle`.

For runtimes in your account, the Lambda console also shows lifecycle information. If the runtime is in another account, use the AWS CLI or the Lambda API.

Consumers in another account need the publisher to grant `lambda:GetRuntimeAlias` and `lambda:ListRuntimeAliases` in the runtime's resource-based policy. For more information, see [Sharing a customer-managed runtime](cmr-permissions.md#cmr-permissions-sharing).

If you're a runtime consumer, we recommend that you check the lifecycle of the aliases that your functions use. Plan your migration before the block dates. For instructions, see [Viewing lifecycle information](#cmr-lifecycle-view).

## Comparison with Lambda-managed runtime deprecation
<a name="cmr-lifecycle-compare"></a>

Lifecycles for customer-managed runtimes use the same block-date model as Lambda-managed runtimes. However, the runtime publisher sets the schedule. The following table summarizes the differences. For more information about Lambda-managed runtimes, see [Runtime deprecation](runtime-support-policy.md).


**Lambda-managed and customer-managed runtime deprecation**  

| Topic | Lambda-managed runtimes | Customer-managed runtimes | 
| --- | --- | --- | 
| Who sets the schedule | AWS, based on the deprecation policy | The runtime publisher | 
| Block dates | Lambda blocks function creates at least 30 days after deprecation. Lambda blocks function updates at least 60 days after deprecation. | Optional. You choose the dates, and they can be in any order. | 
| Scope | Each runtime identifier, such as python3.14 | Each runtime, each runtime alias, or both | 
| Release states | Supported or deprecated | PREVIEW, GA, or DEPRECATED | 
| Notifications | Health Dashboard, email, and AWS Trusted Advisor | None from Lambda. The publisher notifies consumers. | 
| Invocations after block dates | Continue | Continue | 

## Planning a deprecation
<a name="cmr-lifecycle-planning"></a>

To retire a runtime or alias with the least impact on consumers, we recommend the following steps:

1. Publish the successor runtime or alias, so that consumers have a supported target. For more information, see [Creating a runtime](cmr-create.md) and [Runtime aliases](cmr-aliases.md).

1. Set the `DeprecationDate` and, if you plan to enforce the schedule, the block dates. For instructions, see [Setting the lifecycle for a runtime](#cmr-lifecycle-set-runtime) and [Setting the lifecycle for a runtime alias](#cmr-lifecycle-set-alias).

1. Notify your consumers. Include the dates and the successor runtime or alias.

1. Track migration by monitoring the `RuntimeInvocations` metric for each alias. For more information, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

1. After consumers have migrated, delete the alias, runtime versions, or runtime that you no longer need. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

**Important**  
Deleting a runtime alias or runtime version can cause invocations to fail for functions that still use it. Unlike block dates, deletion affects running functions. Before you delete a resource, confirm that consumers no longer use it.

## Setting the lifecycle for a runtime
<a name="cmr-lifecycle-set-runtime"></a>

You can set the release lifecycle when you create a runtime, or add or change it later. A runtime-level lifecycle applies to every alias that doesn't have its own lifecycle.

**To set the lifecycle for a runtime (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime.

1. Choose **Manage runtime lifecycle**.

1. For **Release status**, select a release status.

1. Enter the dates that you want to set for **Deprecation date**, **Block function creation**, and **Block function update**.

1. Choose **Save settings**.

**Note**  
The dates are optional. If you set the release status to **Deprecated**, the deprecation date is required and must be today or earlier.

**To set the lifecycle for a new runtime (AWS CLI)**
+ To set the lifecycle when you create a runtime, run the `create-runtime` command with the `--release-lifecycle` option. The following example creates a runtime named `companyphp8` in the `PREVIEW` state.

  ```bash
  aws lambda-core create-runtime \
    --name {{companyphp8}} \
    --description "{{PHP 8 runtime for Example Corp}}" \
    --release-lifecycle ReleaseState=PREVIEW \
    --region us-east-1
  ```

**To set or change the lifecycle for an existing runtime (AWS CLI)**
+ To set or change the lifecycle of an existing runtime, run the `update-runtime` command with the `--release-lifecycle` option. You can use shorthand syntax or JSON. The following example makes the `companyphp8` runtime generally available and sets its deprecation and block dates.

  ```bash
  aws lambda-core update-runtime \
    --runtime-name {{companyphp8}} \
    --release-lifecycle '{"ReleaseState":"GA","DeprecationDate":"2027-06-30","FunctionCreateBlockDate":"2027-06-30","FunctionUpdateBlockDate":"2027-09-30"}' \
    --region us-east-1
  ```

  You should see output similar to the following:

  ```json
  {
      "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
      "Name": "companyphp8",
      "Description": "PHP 8 runtime for Example Corp",
      "ReleaseLifecycle": {
          "ReleaseState": "GA",
          "DeprecationDate": "2027-06-30",
          "FunctionCreateBlockDate": "2027-06-30",
          "FunctionUpdateBlockDate": "2027-09-30"
      },
      "Created": "2026-10-01T10:05:17.443Z",
      "LastModified": "2026-10-05T14:38:52.344Z"
  }
  ```

  The `update-runtime` command replaces the runtime's stored lifecycle with the lifecycle in your request. To change only one property, specify the complete lifecycle, including the values that you want to keep. The following example moves the function update block date and keeps the other values from the previous example.

  ```bash
  aws lambda-core update-runtime \
    --runtime-name {{companyphp8}} \
    --release-lifecycle '{"ReleaseState":"GA","DeprecationDate":"2027-06-30","FunctionCreateBlockDate":"2027-06-30","FunctionUpdateBlockDate":"{{2027-12-31}}"}' \
    --region us-east-1
  ```

## Setting the lifecycle for a runtime alias
<a name="cmr-lifecycle-set-alias"></a>

You can set a release lifecycle on an existing alias in the Lambda console. With the AWS CLI, you can set it when you create the alias with the `create-runtime-alias` command, or later with the `update-runtime-alias` command.

**To set the lifecycle for a runtime alias (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime, and then choose the **Aliases** tab.

1. Select the runtime alias that you want to update.

1. Choose **Alias actions**, and then choose **Manage alias lifecycle**.

1. For **Release status**, select a release status. If the runtime is deprecated and you want functions to keep using this alias, set a future deprecation date for the alias. The alias lifecycle overrides the runtime lifecycle. For more information, see [Runtime-level and alias-level lifecycles](#cmr-lifecycle-levels).

1. Enter the dates that you want to set for **Deprecation date**, **Block function creation**, and **Block function update**.

1. Choose **Save settings**.

**Note**  
The dates are optional. If you set the release status to **Deprecated**, the deprecation date is required and must be today or earlier.

**To set the lifecycle for a runtime alias (AWS CLI)**
+ The `update-runtime-alias` command requires the `--runtime-version` option. To keep the alias on its current runtime version, specify the version that the alias already uses. To find it, run the `get-runtime-alias` command. For an example, see [Example: Deprecating a runtime alias](#cmr-lifecycle-deprecate-example).

  The following example sets the lifecycle of the `al2` alias of the `java8` runtime. The alias keeps runtime version `2026-09-15.1`. If the alias already has a lifecycle, the lifecycle in this request replaces it.

  ```bash
  aws lambda-core update-runtime-alias \
    --runtime-name {{java8}} \
    --name {{al2}} \
    --runtime-version {{2026-09-15.1}} \
    --release-lifecycle '{"DeprecationDate":"2027-06-30","FunctionCreateBlockDate":"2027-06-30","FunctionUpdateBlockDate":"2027-09-30"}' \
    --region us-east-1
  ```

  To set the lifecycle when you create an alias, add the same `--release-lifecycle` option to the `create-runtime-alias` command.

## Viewing lifecycle information
<a name="cmr-lifecycle-view"></a>

Publishers and consumers can view the lifecycle that applies to an alias. Publishers can also view the runtime-level lifecycle.

In the Lambda console, the lifecycle of each alias appears in the list of aliases on the runtime's **Aliases** tab.

If the runtime is in another account, you can't view it in the Lambda console. Use the AWS CLI instead.

**To view the lifecycle of a runtime alias (AWS CLI)**

1. To view the lifecycle that applies to an alias, run the `get-runtime-alias` command. The following example gets the `al2023` alias of the `java8` runtime. This alias doesn't have its own lifecycle, so the response shows the runtime-level lifecycle.

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{java8}} \
     --name {{al2023}} \
     --region us-east-1
   ```

   You should see output similar to the following:

   ```json
   {
       "Name": "al2023",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/java8/alias/al2023",
       "RuntimeVersion": "2026-09-15.2",
       "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/java8/version/2026-09-15.2",
       "State": "ACTIVE",
       "Description": "Java 8 on Amazon Linux 2023",
       "Compatibility": {
           "Architectures": ["x86_64", "arm64"],
           "IntegrationModels": ["RuntimeAPI"],
           "ManagedInstances": "Supported"
       },
       "ReleaseLifecycle": {
           "ReleaseState": "GA",
           "DeprecationDate": "2030-06-30"
       },
       "Created": "2026-09-15T09:12:44.102Z",
       "LastModified": "2026-09-20T16:03:21.876Z"
   }
   ```

1. (Optional) To view the lifecycle of every alias of a runtime, run the `list-runtime-aliases` command. Consumers in other accounts can specify the runtime ARN instead of the runtime name.

   ```bash
   aws lambda-core list-runtime-aliases \
     --runtime-name {{arn:aws:lambda:us-east-1:123456789012:runtime/java8}} \
     --region us-east-1
   ```

1. (Optional) To view the runtime-level lifecycle, run the `get-runtime` command.

   ```bash
   aws lambda-core get-runtime \
     --runtime-name {{java8}} \
     --region us-east-1
   ```

## Example: Deprecating a runtime alias
<a name="cmr-lifecycle-deprecate-example"></a>

In this example, you're the publisher of the `java8` runtime. You want to retire the `al2` alias and move consumers to the `al2023` alias. The runtime itself stays supported until `2030-06-30`. You set an alias-level lifecycle on `al2` that deprecates it and blocks function creation on `2027-06-30`. It blocks function updates on `2027-09-30`.

**To deprecate a runtime alias (AWS CLI)**

1. To confirm that the successor alias is ready, run the `get-runtime-alias` command for `al2023`. Check that its `State` is `ACTIVE`.

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{java8}} \
     --name {{al2023}} \
     --region us-east-1
   ```

1. To find the runtime version that `al2` uses, run the `get-runtime-alias` command for `al2`. Note the `RuntimeVersion` value in the response, such as `2026-09-15.1`.

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{java8}} \
     --name {{al2}} \
     --region us-east-1
   ```

1. To set the alias lifecycle, run the `update-runtime-alias` command. Specify the current runtime version so that the alias doesn't move to a different version.

   ```bash
   aws lambda-core update-runtime-alias \
     --runtime-name {{java8}} \
     --name {{al2}} \
     --runtime-version {{2026-09-15.1}} \
     --description "{{Deprecation scheduled for 2027-06-30. Migrate to the al2023 alias.}}" \
     --release-lifecycle '{"DeprecationDate":"2027-06-30","FunctionCreateBlockDate":"2027-06-30","FunctionUpdateBlockDate":"2027-09-30"}' \
     --region us-east-1
   ```

   You should see output similar to the following:

   ```json
   {
       "Name": "al2",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/java8/alias/al2",
       "RuntimeVersion": "2026-09-15.1",
       "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/java8/version/2026-09-15.1",
       "State": "ACTIVE",
       "Description": "Deprecation scheduled for 2027-06-30. Migrate to the al2023 alias.",
       "Compatibility": {
           "Architectures": ["x86_64", "arm64"],
           "IntegrationModels": ["RuntimeAPI"],
           "ManagedInstances": "Supported"
       },
       "ReleaseLifecycle": {
           "ReleaseState": "GA",
           "DeprecationDate": "2027-06-30",
           "FunctionCreateBlockDate": "2027-06-30",
           "FunctionUpdateBlockDate": "2027-09-30"
       },
       "Created": "2026-03-02T11:20:05.318Z",
       "LastModified": "2026-10-05T15:47:10.529Z"
   }
   ```

   The `ReleaseState` is `GA` until `2027-06-30`. On that date, Lambda returns `DEPRECATED` automatically.

1. Notify the consumers of the `al2` alias. Include the deprecation date, the block dates, and the successor alias.

1. Monitor the `RuntimeInvocations` metric for the `al2` alias to track migration. For more information, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

1. After consumers stop using the alias, delete it. For more information, see [Deleting and restoring runtimes](cmr-delete.md).