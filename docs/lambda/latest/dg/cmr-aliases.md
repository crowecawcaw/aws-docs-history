

# Runtime aliases

A runtime alias is a name that points to one runtime version. Functions always use a customer-managed runtime through an alias. As a runtime publisher, you roll out an update by pointing an alias to a new version. You roll back by pointing it to the old version. This topic explains how aliases work and how to manage them.

Runtime consumers can also use this topic to learn when alias updates reach their functions, and how to pick an alias.

## How runtime aliases work
<a name="cmr-aliases-how-it-works"></a>

Each alias belongs to one runtime, and points to one version of that runtime. To use a customer-managed runtime, a runtime consumer sets the function's runtime to `custom`. The consumer then specifies the runtime ARN and an alias name in the function's runtime configuration. For example:

```bash
aws lambda create-function \
  --function-name {{my-function}} \
  --runtime custom \
  --runtime-config RuntimeArn={{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}},RuntimeAlias={{prod}} \
  ...
```

For more information about how consumers configure functions, see [Using a customer-managed runtime](cmr-using.md).

Each alias has an Amazon Resource Name (ARN) in the format `arn:aws:lambda:{{region}}:{{account-id}}:runtime/{{runtime-name}}/alias/{{alias-name}}`.

For example, the `prod` alias of the `companyphp8` runtime has the ARN `arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod`.

When you point an alias to a different version, functions that use the alias in the **Auto** runtime update mode move to that version at their next cold start. You don't need to update or redeploy these functions. Functions in other runtime update modes don't move automatically. For more information, see [How alias updates reach functions](#cmr-aliases-resolution). To roll back, you point the alias back to the previous runtime version.

No function uses a new runtime version until an alias points to it. The exception is a function that a consumer pins to that version by using the **Manual** runtime update mode.

## How alias updates reach functions
<a name="cmr-aliases-resolution"></a>

When a function picks up an alias change depends on its runtime update mode. Consumers set the mode with runtime management controls. For more information, see [Runtime update modes](runtimes-update.md#runtime-management-controls) and [Managing Lambda runtime updates](runtime-management-configure-settings.md).

The following table shows when Lambda resolves the alias to a runtime version for each mode.


**Alias resolution by runtime update mode**  

| Runtime update mode | When Lambda resolves the alias | 
| --- | --- | 
| Auto (default) | At each cold start. The function picks up an alias change the next time Lambda initializes a new execution environment. | 
| Function update | When you create or update the function. This includes calls to CreateFunction, UpdateFunctionCode, and UpdateFunctionConfiguration. | 
| Manual | Never. Lambda ignores the alias, and the function uses the runtime version that you pin it to. | 

With the **Auto** mode, an alias update doesn't reach all functions at once. Lambda replaces execution environments from time to time, so the update rolls out gradually as new environments start. Environments that are already running keep the old version until Lambda replaces them.

Customer-managed runtimes don't use the [two-phase rollout](runtimes-update.md#runtime-management-two-phase) that Lambda uses for Lambda-managed runtimes. You control the pace of the rollout by choosing when to update each alias. For more information, see [Deploying runtime updates](cmr-deploy-updates.md).

## Alias strategies
<a name="cmr-aliases-strategies"></a>

You decide how many aliases to create, and which version each alias points to. The following strategies are common. Other patterns are also possible.
+ **Single alias** – Create one alias, such as `stable`, that all functions use. This strategy is simple and works well while you build your runtime.
+ **Staged by environment** – Create one alias for each stage of your release process, such as `dev`, `test`, and `prod`. You roll out each new runtime version to each alias in turn. Consumers can then find issues in dev and test before the update reaches prod.
+ **Semantic versioning** – The runtime represents a major version, and each alias represents a minor version. You create a runtime version for each patch release, and point only the matching minor-version alias to it. Consumers choose a minor version and receive patches automatically. Consumers decide when to move their functions to a new minor version.

The following table shows an example of the staged strategy for the `companyphp8` runtime. The publisher has rolled out version `v8.3.2` to the `dev` and `test` aliases, but not yet to `prod`.


**Example staged aliases**  

| Alias | Runtime version | 
| --- | --- | 
| dev | v8.3.2 | 
| test | v8.3.2 | 
| prod | v8.3.1 | 

The following table shows an example of the semantic versioning strategy for the `companyphp8` runtime. Each patch version maps only to its own minor-version alias. For example, version `v8.3.2` never maps to the `php8.4` alias.


**Example semantic versioning aliases**  

| Alias | Runtime version | 
| --- | --- | 
| php8.3 | v8.3.2 | 
| php8.4 | v8.4.1 | 

## Alias compatibility
<a name="cmr-aliases-compatibility"></a>

Each alias has a `Compatibility` object that tells consumers what they can rely on when they use the alias. It includes the following fields:
+ `Architectures` – The [instruction set architectures](foundation-arch.md) that functions can use with the alias: `x86_64`, `arm64`, or both.
+ `IntegrationModels` – How the runtime integrates with Lambda. The value is `RuntimeAPI`, which means that the runtime can be used with Lambda Event Functions.
+ `ManagedInstances` – Whether functions on [Lambda Managed Instances](lambda-managed-instances.md) can use the alias.

You don't set alias compatibility directly. There's no compatibility option on the operations that create or update an alias. Instead, the alias mirrors the compatibility of the runtime version that it points to. A runtime version takes its compatibility from the labels and platforms in its container image. When you point an alias to a different version, the alias compatibility changes to match that version. For what each capability means and how image labels and platforms set it, see [Architectures and feature compatibility](cmr-building-images.md#cmr-building-images-capabilities). For how a version gets its compatibility, see [Runtime version compatibility](cmr-versions.md#cmr-publish-versions-compatibility).

### How Lambda checks alias compatibility
<a name="cmr-aliases-compatibility-rules"></a>

Lambda uses alias compatibility in the following ways:
+ **When you point an alias to a version** – You can't point an alias to a runtime version that drops a capability or architecture that the alias's current version supports. The update fails unless the new version supports at least every capability and architecture of the current version. This rule protects functions that already use the alias.
+ **When a consumer creates or updates a function** – Lambda checks the function against the compatibility of the alias. The function's architecture must be one of the alias's `Architectures`. If the function runs on Lambda Managed Instances, the alias must support Lambda Managed Instances. Otherwise, the request fails.

Because you can't point an alias to a version that drops a capability, an alias never takes away a capability or architecture that consumers rely on.

### Add a capability or architecture to an alias
<a name="cmr-aliases-compatibility-add"></a>

Because an alias mirrors the version that it points to, you add a capability or architecture to an alias by pointing it to a version that has the capability. Follow these steps:

1. Build an image that supports the new capability or architecture. For a capability, add the matching label. For an architecture, build the image for that platform. For more information, see [Architectures and feature compatibility](cmr-building-images.md#cmr-building-images-capabilities).

1. Publish a runtime version from the image. For more information, see [Runtime versions](cmr-versions.md).

1. Point the alias to the new version. The alias then gains the capability or architecture. For instructions, see [Update an alias to roll out a runtime update](#cmr-aliases-update).

Adding a capability or architecture doesn't affect existing functions.

### Stop offering a capability
<a name="cmr-aliases-compatibility-remove"></a>

You can't remove a capability or architecture from an alias by pointing the alias to a version that drops it. Lambda blocks that update to protect functions that already use the alias. To stop offering a capability, create a new alias (or a new runtime) for versions that don't have the capability. Then ask consumers to move their functions to it when they're ready. For more information, see [Create a runtime alias](#cmr-aliases-create).

**Warning**  
After Lambda permanently deletes an alias, you can re-create an alias with the same name. If the re-created alias points to a version that doesn't support a capability that a function needs, that function becomes incompatible with its runtime version. The function enters the `Inactive` state. Existing execution environments continue to handle invocations, but invocations that require a cold start fail. After you restore compatibility, the function returns to the `Active` state automatically. For more information, see [Runtime lifecycle and function states](cmr-using.md#cmr-using-lifecycle).

## Alias lifecycle
<a name="cmr-aliases-lifecycle"></a>

You can set a release lifecycle on the runtime and on each alias. The lifecycle includes the release state and the deprecation date. It also includes the dates when Lambda blocks function creation and updates. An alias lifecycle is useful when your aliases represent separate branches of a runtime, such as `al2023` and `al2027`. You can then deprecate each branch independently.

An alias lifecycle is optional. If you set a lifecycle on an alias, the alias lifecycle replaces the runtime lifecycle for that alias. The alias dates can be earlier or later than the runtime dates. For more information, see [Runtime lifecycle](cmr-lifecycle.md).

## Alias states
<a name="cmr-aliases-states"></a>

A runtime alias is in one of the following states:
+ `CREATING` – Lambda is creating the alias.
+ `ACTIVE` – The alias is ready to use.
+ `UPDATING` – Lambda is updating the alias.
+ `PENDING_DELETION` – The alias is scheduled for deletion. You can restore it until the waiting period ends. For more information, see [Resources scheduled for deletion](cmr-delete.md#cmr-delete-pending).
+ `DELETING` – Lambda is deleting the alias.

You can update an alias only when it's in the `ACTIVE` state. You can't change the waiting period of an alias that's in the `PENDING_DELETION` state. If you delete an alias that's already scheduled for deletion, the request succeeds, but it doesn't change the alias's waiting period. To reschedule the deletion, restore the alias, and then delete it again. For more information, see [Rescheduling a deletion](cmr-delete.md#cmr-delete-change-period).

An alias that's scheduled for deletion keeps its name until Lambda permanently deletes it. Until then, you can't create an alias with the same name in the runtime. For more information, see [Resources scheduled for deletion](cmr-delete.md#cmr-delete-pending).

## Alias names
<a name="cmr-aliases-names-quotas"></a>

Alias names must meet the following requirements:
+ Contain 1–128 characters
+ Contain only uppercase and lowercase letters, numbers, underscores (`_`), periods (`.`), and hyphens (`-`)
+ Start and end with a letter, number, or underscore

Alias names are case-sensitive. The alias name becomes part of the alias ARN.

## Permissions for runtime aliases
<a name="cmr-aliases-permissions"></a>

To manage runtime aliases, runtime publishers need the following IAM permissions:
+ `lambda:CreateRuntimeAlias`
+ `lambda:GetRuntimeAlias`
+ `lambda:UpdateRuntimeAlias`
+ `lambda:DeleteRuntimeAlias`
+ `lambda:ListRuntimeAliases`

To use an alias in a function, runtime consumers need the `lambda:AssociateRuntimeAlias` permission on the alias ARN. Lambda checks this permission when the consumer creates the function or changes its runtime configuration, not at invocation. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## Create a runtime alias
<a name="cmr-aliases-create"></a>

Create an alias so that functions can use a runtime version. After you create the alias, share the runtime ARN and alias name with your runtime consumers.

**Prerequisites**
+ A runtime version in the `ACTIVE` state. For more information, see [Runtime versions](cmr-versions.md).
+ The `lambda:CreateRuntimeAlias` permission.

**To create a runtime alias (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime, and then choose the **Aliases** tab.

1. Choose **Create alias**.

1. For **Runtime alias name**, enter a name for the alias. The alias name must be unique for this runtime.

1. Optionally, for **Alias description**, enter a description.

1. For **Runtime version**, choose an existing runtime version from the dropdown list.

1. Choose **Create alias**.

**To create a runtime alias (AWS CLI)**

1. To create the alias, run the `create-runtime-alias` command.

   ```bash
   aws lambda-core create-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}} \
     --runtime-version {{v8.3.1}} \
     --description "{{Production alias for the companyphp8 runtime}}"
   ```

   For `--runtime-name`, you can specify the runtime name or the runtime ARN. For `--runtime-version`, specify the name of the runtime version. The alias takes its compatibility from this version. You can't set compatibility on the alias directly. For more information, see [Alias compatibility](#cmr-aliases-compatibility). You can also specify `--release-lifecycle` to set a lifecycle for the alias. For more information, see [Runtime lifecycle](cmr-lifecycle.md).

   You should see output similar to the following:

   ```json
   {
       "Name": "prod",
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod",
       "RuntimeVersion": "v8.3.1",
       "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.1",
       "State": "CREATING",
       "Description": "Production alias for the companyphp8 runtime",
       "Compatibility": {
           "Architectures": [
               "x86_64",
               "arm64"
           ],
           "IntegrationModels": [
               "RuntimeAPI"
           ],
           "ManagedInstances": "Supported"
       },
       "Created": "2026-10-05T17:00:00.000Z",
       "LastModified": "2026-10-05T17:00:00.000Z"
   }
   ```

1. To check that the alias is ready to use, run the `get-runtime-alias` command.

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}}
   ```

   Repeat this command until the value of `State` is `ACTIVE`.

   Alternatively, to wait until the alias is ready, run the following command:

   ```bash
   aws lambda-core wait runtime-alias-active \
     --runtime-name {{companyphp8}} \
     --name {{prod}}
   ```

   The command returns when the alias is `ACTIVE`.

When the alias is `ACTIVE`, consumers can configure functions to use it. For more information, see [Using a customer-managed runtime](cmr-using.md).

## Update an alias to roll out a runtime update
<a name="cmr-aliases-update"></a>

To roll out a new runtime version, update the alias to point to that version. Functions that use the alias in **Auto** mode move to the new version at their next cold start, without any function update. Functions in other modes don't move automatically. For more information, see [Controlling runtime updates](cmr-using.md#cmr-using-controls).

**Prerequisites**
+ A new runtime version in the `ACTIVE` state.
+ An alias in the `ACTIVE` state.
+ The `lambda:UpdateRuntimeAlias` permission.<a name="cmr-aliases-update-console"></a>

**To update a runtime alias (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime, and then choose the **Aliases** tab.

1. Select the runtime alias to update.

1. Choose **Alias actions**, and then choose **Update alias**.

1. Update the **Alias description**, choose a different **Runtime version** from the dropdown list, or both.

1. Choose **Update alias**.

**To update a runtime alias (AWS CLI)**

1. To point the alias to the new runtime version, run the `update-runtime-alias` command.

   ```bash
   aws lambda-core update-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}} \
     --runtime-version {{v8.3.2}}
   ```

   The `--runtime-version` parameter is required. If you omit `--description`, the description doesn't change. If you specify `--release-lifecycle`, the lifecycle that you specify replaces the existing alias lifecycle. If you omit `--release-lifecycle`, Lambda clears any lifecycle on the alias, and the runtime-level lifecycle applies. To keep the alias lifecycle, include the complete lifecycle in each update. For more information, see [Rules for release states and dates](cmr-lifecycle.md#cmr-lifecycle-consistency).

   If the new version drops a capability or architecture that the alias's current version supports, the command fails. For more information, see [Alias compatibility](#cmr-aliases-compatibility).

1. To verify the update, run the `get-runtime-alias` command.

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}}
   ```

   When the update is complete, `State` is `ACTIVE` and `RuntimeVersion` is `v8.3.2`.

**Important**  
Every `update-runtime-alias` request must specify the runtime version, even when you change only other settings, such as the description. The `RuntimeVersion` parameter is required. If two updates run at the same time, one can overwrite the other and move the alias back to an earlier version. To avoid this, follow these practices:  
Before you update an alias, run the `get-runtime-alias` command to get its current runtime version. If you don't want to change the version, pass the current version in your update request.
If the alias has its own lifecycle, include the complete lifecycle in the `--release-lifecycle` option of every update request. If you omit `--release-lifecycle`, Lambda clears the alias lifecycle.
Run updates to an alias one at a time. For example, run your deployment pipelines one at a time.

Functions in **Auto** mode pick up the new version at their next cold start. Functions in **Function update** mode pick it up the next time that the function owner updates them. Functions in **Manual** mode don't change. For more information, see [How alias updates reach functions](#cmr-aliases-resolution). To monitor a rollout, see [Deploying runtime updates](cmr-deploy-updates.md).

## Roll back a runtime update
<a name="cmr-aliases-rollback"></a>

If a new version causes problems, point the alias back to the old version. Functions in **Auto** mode pick up the previous version at their next cold start.

To roll back a runtime alias in the console, follow the steps in [To update a runtime alias (console)](#cmr-aliases-update-console). For **Runtime version**, choose the previous runtime version.

**To roll back a runtime alias (AWS CLI)**

1. To point the alias back to the previous runtime version, run the `update-runtime-alias` command.

   ```bash
   aws lambda-core update-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}} \
     --runtime-version {{v8.3.1}}
   ```

1. To verify the rollback, run the `get-runtime-alias` command.

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}}
   ```

   When the rollback is complete, `State` is `ACTIVE` and `RuntimeVersion` is `v8.3.1`.

Runtime consumers can also roll back an individual function. To do this, the consumer pins the function to an earlier runtime version by using the **Manual** runtime update mode. For more information, see [Using a customer-managed runtime](cmr-using.md).

## View runtime aliases
<a name="cmr-aliases-view"></a>

You can view the details of one alias, or list all aliases for a runtime.

In the Lambda console, the **Aliases** tab of the runtime's page lists the aliases for the runtime.

**To view runtime aliases (AWS CLI)**

1. To view the details of one alias, run the `get-runtime-alias` command.

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}}
   ```

   The output includes the runtime version that the alias points to, the alias state, its compatibility, and its effective release lifecycle.

1. To list all aliases for a runtime, run the `list-runtime-aliases` command.

   ```bash
   aws lambda-core list-runtime-aliases \
     --runtime-name {{companyphp8}}
   ```

   You should see output similar to the following:

   ```json
   {
       "Items": [
           {
               "Name": "prod",
               "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod",
               "RuntimeVersion": "v8.3.1",
               "RuntimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.1",
               "State": "ACTIVE",
               "Description": "Production alias for the companyphp8 runtime",
               "Compatibility": {
                   "Architectures": [
                       "x86_64",
                       "arm64"
                   ],
                   "IntegrationModels": [
                       "RuntimeAPI"
                   ],
                   "ManagedInstances": "Supported"
               },
               "Created": "2026-10-05T17:00:00.000Z",
               "LastModified": "2026-10-05T17:00:00.000Z"
           }
       ]
   }
   ```

   The command returns all aliases. To limit the output, use `--max-items`.

## Example: Staged rollout across aliases
<a name="cmr-aliases-staged-example"></a>

The following example rolls out runtime version `v8.3.2` through the `dev`, `test`, and `prod` aliases of the `companyphp8` runtime. Between each step, check that functions that use the updated alias work as expected. For guidance on monitoring, see [Deploying runtime updates](cmr-deploy-updates.md).

```bash
# Step 1: Roll out to development
aws lambda-core update-runtime-alias --runtime-name companyphp8 --name dev --runtime-version v8.3.2

# Step 2: After validating dev, roll out to test
aws lambda-core update-runtime-alias --runtime-name companyphp8 --name test --runtime-version v8.3.2

# Step 3: After validating test, roll out to production
aws lambda-core update-runtime-alias --runtime-name companyphp8 --name prod --runtime-version v8.3.2
```

If you find a problem at any stage, roll back that alias to `v8.3.1`, and don't update the later aliases.

## Delete a runtime alias
<a name="cmr-aliases-delete"></a>

You can't delete a runtime version while an alias points to it. After you delete the alias, you can delete the version. For more information about deleting aliases and other runtime resources, see [Deleting and restoring runtimes](cmr-delete.md).

## Next steps
<a name="cmr-aliases-next-steps"></a>

After you create your aliases, see the following topics:
+ To share your runtime with consumers and grant them access to aliases, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).
+ To learn how consumers configure functions to use an alias, see [Using a customer-managed runtime](cmr-using.md).
+ To plan and monitor runtime update rollouts, see [Deploying runtime updates](cmr-deploy-updates.md).