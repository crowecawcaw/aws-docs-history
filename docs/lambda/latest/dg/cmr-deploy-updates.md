

# Deploying runtime updates

As a runtime publisher, you release each runtime update as a new runtime version. You then roll it out by updating your runtime aliases. A runtime update changes code that runs in your consumers' Lambda Event Functions. This topic explains how to roll out updates safely, monitor them, and roll them back if a problem occurs.

For an overview of how runtime updates work, see [Customer-managed runtimes](runtimes-customer-managed.md).

## Your responsibilities as a runtime publisher
<a name="cmr-deploy-updates-responsibilities"></a>

When you publish a runtime, you own its updates. Lambda doesn't patch or test customer-managed runtimes for you. Your responsibilities include the following:
+ **Backward compatibility** – Each update must keep working with the functions that already use the alias. Avoid changes that break existing function code or configuration.
+ **Testing** – Test each new runtime version before you point an alias to it.
+ **Security patching** – Apply patches to every component of your runtime. This includes the operating system, the language runtime, the runtime interface client, and any libraries that you include. If you build on a Lambda base image, rebuild your image to pick up new patches to the base image. For more information, see [Building a runtime image from a Lambda base image](cmr-base-images.md).
+ **Communication** – Tell your consumers what changed in each update. Add release notes to each runtime version. For more information, see [Update release notes](cmr-versions.md#cmr-publish-versions-update-notes). Runtime metrics don't identify consumers, and CloudTrail events in your account show which accounts use your runtime but not who to contact. We recommend that you keep a way to reach consumers, such as a registry of consumer accounts, a mailing list, or a chat channel.

How often you patch your runtime is a business decision. Base it on your security requirements and those of your consumers. To make frequent updates practical, we recommend that you automate them with a runtime update pipeline. For more information, see [Building a runtime update pipeline](#cmr-deploy-updates-pipeline).

## Runtime update workflow
<a name="cmr-deploy-updates-workflow"></a>

A runtime update typically follows these steps:

1. **Build** – Build a new runtime image. For more information, see [Building runtime images](cmr-building-images.md).

1. **Push** – Push the image to an Amazon Elastic Container Registry (Amazon ECR) repository in the same AWS Region as the runtime.

1. **Create a version** – Create a runtime version from the image. No function uses the new version until you point an alias to it. For more information, see [Runtime versions](cmr-versions.md).

1. **Test** – Test the new version. For example, pin a test function to the new version with the **Manual** runtime update mode. You can also update a development alias that only your test functions use.

1. **Roll out in stages** – Update your aliases one at a time, with a bake period between each update. For more information, see [Safe rollout mechanisms](#cmr-deploy-updates-safe-rollout).

1. **Monitor** – Watch the runtime metrics for the new version and the updated alias. For more information, see [Monitoring function health during a rollout](#cmr-deploy-updates-monitoring).

1. **Continue or roll back** – If the new version is healthy, update the next alias. If you find a problem, point the alias back to the previous version. For more information, see [Rolling back a runtime update](#cmr-deploy-updates-rollback-concepts).

## Safe rollout mechanisms
<a name="cmr-deploy-updates-safe-rollout"></a>

A faulty runtime update can affect every function that uses an alias. To limit the impact, combine the following mechanisms:

Alias-based staging  
Create an alias for each stage of your release process, such as `dev`, `test`, and `prod`. Ask consumers to use the alias that matches each of their environments. Then update each alias in turn, with a bake period between updates. A problem that appears in `dev` doesn't reach functions that use `prod`. For more information, see [Alias strategies](cmr-aliases.md#cmr-aliases-strategies).

Region-by-Region staggering  
Runtimes are Regional, so you update the aliases in each Region separately. Update one Region at a time, and check the runtime's health before you move to the next Region. For more information, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).

Cold-start gating  
An alias update doesn't reach all functions at once. Functions in **Auto** mode pick up the new version at their next cold start. Lambda replaces execution environments routinely, so the update rolls out gradually. Environments that are already running keep the previous version until Lambda replaces them.  
Functions in **Function update** mode pick up the new version only when their owner next deploys them. Functions in **Manual** mode don't change. For more information, see [How alias updates reach functions](cmr-aliases.md#cmr-aliases-resolution).

Customer-managed runtimes don't use the [two-phase rollout](runtimes-update.md#runtime-management-two-phase) that Lambda uses for Lambda-managed runtimes. You control the pace of the rollout by choosing when to update each alias in each Region.

Choose a bake period that's long enough for many functions to start new execution environments with the new version. Functions in **Function update** mode might move to the new version days or weeks after you update the alias.

## Monitoring function health during a rollout
<a name="cmr-deploy-updates-monitoring"></a>

Lambda publishes runtime metrics to Amazon CloudWatch in the account that owns the runtime. The `RuntimeInvocations` and `RuntimeInvocationErrors` metrics count invocations of all functions that use the runtime. You can view them by runtime name, runtime version, and runtime alias. For the metric reference and for instructions on viewing metrics and creating alarms, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

`RuntimeInvocationErrors` counts invocations that fail for any of the following reasons:
+ An unhandled exception (a function error)
+ A timeout
+ A crash of the runtime or function process
+ An initialization (init) failure

Lambda doesn't count an invocation that completes as an error, even if the function returns an application-level error in its response. For example, a response body with an HTTP 500 status code doesn't count as an error. Because the metric includes errors in your consumers' own function code, compare the error rate of the old and new runtime version or alias. Don't alarm on absolute values. For more information, see [Runtime metrics](cmr-monitoring.md#cmr-monitoring-metrics).

The runtime version and runtime alias dimensions help you judge a rollout in the following ways:
+ **Compare versions** – Compare the error rate (`RuntimeInvocationErrors` divided by `RuntimeInvocations`) of the new version with the error rate of the previous version. Compare them over the same period, when traffic is similar. A higher error rate for the new version suggests a problem with the update.
+ **Compare aliases** – Check whether errors are concentrated in the alias that you updated. For example, if the error rate rises for `dev` but not for `prod`, the new version is the likely cause.
+ **See impact across all consumers** – In each Region, the metrics include invocations from every account that uses the runtime. You can see the impact of an update across your whole consumer base without access to your consumers' functions. The metrics don't show function names or account IDs.
+ **Track rollout progress** – As Lambda replaces execution environments, `RuntimeInvocations` for the new version rise and `RuntimeInvocations` for the previous version fall. This shows how much of your traffic uses the new version.

We recommend that you create a CloudWatch alarm on the error rate of each alias. Configure your update pipeline to stop the rollout when an alarm enters the `ALARM` state. For instructions on creating an alarm, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

## Rolling back a runtime update
<a name="cmr-deploy-updates-rollback-concepts"></a>

To roll back an update, point the alias back to the previous runtime version. Functions in **Auto** mode pick up the previous version at their next cold start. You don't need to change the functions. If several aliases point to the faulty version, roll back each of them. For instructions, see [Roll back a runtime update](#cmr-deploy-updates-rollback).

Functions in **Function update** mode don't change when you roll back an alias. They keep the runtime version that they were deployed with until their owner deploys them again. This isn't necessarily a problem. The issue in the faulty version might not affect these functions, and they might be working as expected. Tell your consumers about the rollback so that they can decide whether to redeploy.

After you roll back, fix the issue and roll forward with a new runtime version. Runtime versions are immutable, so you can't fix a version in place.

Runtime consumers can also roll back on their own. A consumer can pin a function to an earlier runtime version with **Manual** mode. For more information, see [Using a customer-managed runtime](cmr-using.md).

Don't delete the faulty version right away. Functions in **Function update** or **Manual** mode might still use it. Check the `RuntimeInvocations` metric for the version before you delete it. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

## Compatibility constraints on updates
<a name="cmr-deploy-updates-compatibility"></a>

Each alias declares the capabilities and architectures that it supports. A new runtime version must support at least those capabilities and architectures. Otherwise, the alias update fails. This check stops an update from breaking functions that rely on what the alias declares.

A new version can add capabilities or architectures. For example, you can publish a multi-architecture version to add arm64 support. After you point the alias to that version, the alias gains the architecture. For more information, see [Add a capability or architecture to an alias](cmr-aliases.md#cmr-aliases-compatibility-add).

You can't remove a capability or architecture from an alias by pointing it to a version that drops the capability. Lambda blocks that update to protect functions that rely on the alias. To stop offering a capability, create a new alias for versions without it, and move consumers to it. For more information, see [Stop offering a capability](cmr-aliases.md#cmr-aliases-compatibility-remove).

For more information about alias compatibility, see [Alias compatibility](cmr-aliases.md#cmr-aliases-compatibility).

## Building a runtime update pipeline
<a name="cmr-deploy-updates-pipeline"></a>

We recommend that you automate runtime updates with a pipeline, for example with AWS CodePipeline and AWS CodeBuild. A pipeline makes frequent security patching practical and applies the same checks to every update. A typical pipeline has the following stages:

1. **Build** – Build the runtime image with the latest patches, and run unit tests.

1. **Publish** – Push the image to Amazon ECR, and replicate it to each Region where you publish the runtime. Then create a runtime version in each Region. To validate the request first, use the `--dry-run` option.

1. **Test** – Pin test functions to the new version, and run integration tests. If the version supports both architectures, test a function on each architecture.

1. **Update aliases in stages** – Update each alias in turn, such as `dev`, `test`, and then `prod`. Update the `prod` alias one Region at a time.

1. **Bake and monitor** – After each alias update, wait for a bake period. Stop the pipeline if an error rate alarm enters the `ALARM` state.

1. **Promote or roll back** – If the alarms stay healthy, continue to the next stage. Otherwise, point the updated aliases back to the previous version.

For more information about automating updates across Regions, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).

## Deploy a runtime update in stages
<a name="cmr-deploy-updates-staged-rollout"></a>

The following example rolls out version `v8.3.2` of the `companyphp8` runtime. First, you create the version and test it with a pinned function. Then you update the `dev`, `test`, and `prod` aliases in turn.

Before you start, make sure that you have the following:
+ A runtime named `companyphp8` in the `us-east-1` Region, in account `123456789012`. Its `dev`, `test`, and `prod` aliases point to version `v8.3.1`.
+ A new runtime image, tagged `v8.3.2`, in the `companyphp8` Amazon ECR repository. For more information, see [Building runtime images](cmr-building-images.md).
+ A test function named `cmr-test-fn` that uses the `companyphp8` runtime. For more information, see [Using a customer-managed runtime](cmr-using.md).
+ Permissions for `lambda:CreateRuntimeVersion`, `lambda:GetRuntimeVersion`, `lambda:UpdateRuntimeAlias`, `lambda:GetRuntimeAlias`, `lambda:PutRuntimeManagementConfig`, `lambda:AssociateRuntimeVersion`, and `lambda:InvokeFunction`. To create the runtime version, you also need `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` on the Amazon ECR repository that contains the image. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

### Deploy a runtime update in stages (AWS CLI)
<a name="cmr-deploy-updates-staged-rollout-cli"></a>

First, create the new runtime version and test it with a pinned function.

**To create and test a new runtime version (AWS CLI)**

1. To create the runtime version, run the `create-runtime-version` command:

   ```bash
   aws lambda-core create-runtime-version \
     --runtime-name {{companyphp8}} \
     --name {{v8.3.2}} \
     --image-uri {{123456789012.dkr.ecr.us-east-1.amazonaws.com/companyphp8:v8.3.2}} \
     --release-notes "{{Updates PHP to 8.3.2 and applies the latest OS security patches.}}" \
     --region {{us-east-1}}
   ```

1. To wait until the version is `ACTIVE`, run the following command:

   ```bash
   aws lambda-core wait runtime-version-active \
     --runtime-name {{companyphp8}} \
     --name {{v8.3.2}} \
     --region {{us-east-1}}
   ```

1. To pin the test function to the new version, run the `put-runtime-management-config` command:

   ```bash
   aws lambda put-runtime-management-config \
     --function-name {{cmr-test-fn}} \
     --update-runtime-on Manual \
     --runtime-version-arn {{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.2}} \
     --region {{us-east-1}}
   ```

   The pin takes effect right away. Lambda updates the function, and new invocations use the pinned version.

1. To test the function, invoke it:

   ```bash
   aws lambda invoke \
     --function-name {{cmr-test-fn}} \
     --region {{us-east-1}} \
     {{response.json}}
   ```

   Check that the response in `response.json` is what you expect. Run your full set of tests against the function.

1. To confirm that the function used the new version, search its logs for the `INIT_START` line:

   ```bash
   aws logs filter-log-events \
     --log-group-name /aws/lambda/{{cmr-test-fn}} \
     --filter-pattern INIT_START
   ```

   The latest `INIT_START` line shows the runtime version, similar to the following:

   ```text
   INIT_START Runtime Version: companyphp8:v8.3.2 Runtime Version ARN: arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.2
   ```

If the version supports both x86\_64 and arm64, test a function on each architecture. When you finish testing, you can return the test function to **Auto** mode. To do this, run `put-runtime-management-config` with `--update-runtime-on Auto`.

Next, roll out the version through your aliases.

**To roll out a runtime version through aliases (AWS CLI)**

1. To update the `dev` alias, run the `update-runtime-alias` command:

   ```bash
   aws lambda-core update-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{dev}} \
     --runtime-version {{v8.3.2}} \
     --region {{us-east-1}}
   ```

   If the new version doesn't support all the capabilities and architectures that the alias declares, the command fails. For more information, see [Compatibility constraints on updates](#cmr-deploy-updates-compatibility).

   If an alias has its own lifecycle, include the `--release-lifecycle` option with the complete lifecycle in each `update-runtime-alias` command. Otherwise, the update clears the alias lifecycle. For more information, see [Rules for release states and dates](cmr-lifecycle.md#cmr-lifecycle-consistency).

1. To verify the update, run the `get-runtime-alias` command:

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{dev}} \
     --query "[State,RuntimeVersion]" \
     --region {{us-east-1}}
   ```

   You should see the following output:

   ```json
   [
       "ACTIVE",
       "v8.3.2"
   ]
   ```

1. Monitor the `dev` alias for your bake period. Compare the error rate of `v8.3.2` with the error rate of `v8.3.1`. For instructions, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

1. If the `dev` alias is healthy, update the `test` alias:

   ```bash
   aws lambda-core update-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{test}} \
     --runtime-version {{v8.3.2}} \
     --region {{us-east-1}}
   ```

1. Monitor the `test` alias for your bake period.

1. If the `test` alias is healthy, update the `prod` alias:

   ```bash
   aws lambda-core update-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}} \
     --runtime-version {{v8.3.2}} \
     --region {{us-east-1}}
   ```

1. Monitor the `prod` alias. Watch `RuntimeInvocations` for `v8.3.2` rise as functions move to the new version.

If you find a problem at any stage, roll back that alias, and don't update the later aliases. For instructions, see [Roll back a runtime update](#cmr-deploy-updates-rollback). If you publish the runtime in more than one Region, repeat the alias updates in each Region. For more information, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).

## Roll back a runtime update
<a name="cmr-deploy-updates-rollback"></a>

The following example rolls back the `prod` alias of the `companyphp8` runtime from `v8.3.2` to `v8.3.1`. Before you start, stop your pipeline so that it doesn't update more aliases. You need the `lambda:UpdateRuntimeAlias` and `lambda:GetRuntimeAlias` permissions.

### Roll back a runtime update (console)
<a name="cmr-deploy-updates-rollback-console"></a>

To roll back in the Lambda console, update the alias to point to the previous runtime version. Follow the steps in [To update a runtime alias (console)](cmr-aliases.md#cmr-aliases-update-console), and choose the previous runtime version.

### Roll back a runtime update (AWS CLI)
<a name="cmr-deploy-updates-rollback-cli"></a>

**To roll back a runtime update (AWS CLI)**

1. To point the alias back to the previous version, run the `update-runtime-alias` command:

   ```bash
   aws lambda-core update-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}} \
     --runtime-version {{v8.3.1}} \
     --region {{us-east-1}}
   ```

1. To verify the rollback, run the `get-runtime-alias` command:

   ```bash
   aws lambda-core get-runtime-alias \
     --runtime-name {{companyphp8}} \
     --name {{prod}} \
     --query "[State,RuntimeVersion]" \
     --region {{us-east-1}}
   ```

   You should see the following output:

   ```json
   [
       "ACTIVE",
       "v8.3.1"
   ]
   ```

1. Repeat the preceding steps for each other alias that points to `v8.3.2`, such as `dev` and `test`.

1. Monitor `RuntimeInvocations` for each version. As functions start new execution environments, `RuntimeInvocations` for `v8.3.1` rise and `RuntimeInvocations` for `v8.3.2` fall. For instructions, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

To tell consumers about the problem, you can update the release notes of `v8.3.2`. For more information, see [Update release notes](cmr-versions.md#cmr-publish-versions-update-notes). After you fix the issue, create a new version, such as `v8.3.3`, and roll it out. For instructions, see [Deploy a runtime update in stages](#cmr-deploy-updates-staged-rollout).