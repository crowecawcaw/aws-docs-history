# Troubleshoot invocation issues in Lambda

When you invoke a Lambda function, Lambda validates the request and checks for scaling capacity before sending the
event to your function or, for asynchronous invocation, to the event queue. Invocation errors can be caused by
issues with request parameters, event structure, function settings, user permissions, resource permissions, or
limits.

If you invoke your function directly, you see any invocation errors in the response from Lambda. If you invoke
your function asynchronously with an event source mapping or through another service, you might find errors in logs,
a dead-letter queue, or a failed-event destination. Error handling options and retry behavior vary depending on how
you invoke your function and on the type of error.

For a list of error types that the `Invoke` operation can return, see [Invoke](../api/API_Invoke.md "../api/API_Invoke.md").

###### Topics

- [Lambda: Function times out during Init phase (Sandbox.Timedout)](#troubleshooting-timeouts "#troubleshooting-timeouts")
- [IAM: lambda:InvokeFunction not authorized](#troubleshooting-invocation-noauth "#troubleshooting-invocation-noauth")
- [Lambda: Couldn't find valid bootstrap (Runtime.InvalidEntrypoint)](#troubleshooting-invocation-bootstrap "#troubleshooting-invocation-bootstrap")
- [Lambda: Operation cannot be performed ResourceConflictException](#troubleshooting-invocation-ResourceConflictException "#troubleshooting-invocation-ResourceConflictException")
- [Lambda: Function is stuck in Pending](#troubleshooting-invocation-pending "#troubleshooting-invocation-pending")
- [Lambda: One function is using all concurrency](#troubleshooting-invocation-allconcurrency "#troubleshooting-invocation-allconcurrency")
- [General: Cannot invoke function with other accounts or services](#troubleshooting-invocation-cannotinvoke "#troubleshooting-invocation-cannotinvoke")
- [General: Function invocation is looping](#troubleshooting-invocation-loop "#troubleshooting-invocation-loop")
- [Lambda: Alias routing with provisioned concurrency](#troubleshooting-invocation-alias "#troubleshooting-invocation-alias")
- [Lambda: Cold starts with provisioned concurrency](#troubleshooting-invocation-coldstart "#troubleshooting-invocation-coldstart")
- [Lambda: Cold starts with new versions](#troubleshooting-invocation-newversion "#troubleshooting-invocation-newversion")
- [EFS: Function could not mount the EFS file system](#troubleshooting-invocation-efsmount "#troubleshooting-invocation-efsmount")
- [EFS: Function could not connect to the EFS file system](#troubleshooting-invocation-efsconnect "#troubleshooting-invocation-efsconnect")
- [EFS: Function could not mount the EFS file system due to timeout](#troubleshooting-invocation-efstimeout "#troubleshooting-invocation-efstimeout")
- [Lambda: Lambda detected an IO process that was taking too long](#troubleshooting-invocation-ioprocess "#troubleshooting-invocation-ioprocess")
- [Container:
  CodeArtifactUserException errors](#troubleshooting-deployment-container-artifact "#troubleshooting-deployment-container-artifact")
- [Container:
  InvalidEntrypoint errors](#troubleshooting-deployment-container-entrypoint "#troubleshooting-deployment-container-entrypoint")

## Lambda: Function times out during Init phase (Sandbox.Timedout)

**Error:**
_Task timed out after 3.00 seconds_

When the [Init](lambda-runtime-environment.md#runtimes-lifecycle-ib "lambda-runtime-environment.md#runtimes-lifecycle-ib") phase times out, Lambda initializes the execution environment again by re-running the `Init` phase when the next invoke request arrives. This is called a [suppressed init](lambda-runtime-environment.md#suppressed-init "lambda-runtime-environment.md#suppressed-init"). However, if your function is configured with a short [timeout duration](configuration-timeout.md "configuration-timeout.md") (generally around 3 seconds), the suppressed init might not complete during the allocated timeout duration, causing the `Init` phase to time out again. Alternatively, the suppressed init completes but does not leave enough time for the [Invoke](lambda-runtime-environment.md#runtimes-lifecycle-invoke "lambda-runtime-environment.md#runtimes-lifecycle-invoke") phase to complete, causing the `Invoke` phase to time out.

To reduce timeout errors, use one or more of the following strategies:

- **Increase the function timeout duration**: Extend the [timeout](configuration-timeout.md "configuration-timeout.md") to give the `Init` and `Invoke` phases time to complete successfully.
- **Increase the function memory allocation**: More [memory](configuration-memory.md "configuration-memory.md") also means more proportional CPU allocation, which can speed up both the `Init` and `Invoke` phases.
- **Optimize the function initialization code**: Reduce the time needed for initialization to ensure that the the `Init` and `Invoke` phase can complete within the configured timeout.

## IAM: lambda:InvokeFunction not authorized

**Error:**
_User: arn:aws:iam::123456789012:user/developer is not authorized to perform: lambda:InvokeFunction on
resource: my-function_

Your user, or the role that you assume, must have permission to invoke a function. This
requirement also applies to Lambda functions and other compute resources that invoke functions. Add the AWS managed
policy **AWSLambdaRole** to your user, or add a custom policy that allows the
`lambda:InvokeFunction` action on the target function.

###### Note

The name of the IAM action (`lambda:InvokeFunction`) refers to the `Invoke`
Lambda API operation.

For more information, see [Managing permissions in AWS Lambda](lambda-permissions.md "lambda-permissions.md")
.

## Lambda: Couldn't find valid bootstrap (Runtime.InvalidEntrypoint)

**Error:**
_Couldn't find valid bootstrap(s): [/var/task/bootstrap /opt/bootstrap]_

This error typically occurs when the root of your deployment package doesn't contain an executable file named `bootstrap`. For example, if you're deploying a `provided.al2023` function with a .zip file, the `bootstrap` file must be at the root of the .zip file, not in a directory.

## Lambda: Operation cannot be performed ResourceConflictException

**Error:**
_ResourceConflictException: The operation cannot be performed at this time. The function is currently in
the following state: Pending_

When you connect a function to a virtual private cloud (VPC) at the time of creation, the function enters a
`Pending` state while Lambda creates elastic network interfaces. During this time, you can't invoke or
modify your function. If you connect your function to a VPC after creation, you can invoke it while the update is
pending, but you can't modify its code or configuration.

For more information, see [Lambda function states](functions-states.md "functions-states.md")
.

## Lambda: Function is stuck in Pending

**Error:**
_A function is stuck in the `Pending` state for several minutes._

If a function is stuck in the `Pending` state for more than six minutes, call one of the following
API operations to unblock it:

- [UpdateFunctionCode](../api/API_UpdateFunctionCode.md "../api/API_UpdateFunctionCode.md")
- [UpdateFunctionConfiguration](../api/API_UpdateFunctionConfiguration.md "../api/API_UpdateFunctionConfiguration.md")
- [PublishVersion](../api/API_PublishVersion.md "../api/API_PublishVersion.md")

Lambda cancels the pending operation and puts the function into the `Failed` state. You can then
attempt another update.

## Lambda: One function is using all concurrency

**Issue:**
_One function is using all of the available concurrency, causing other functions to be
throttled._

To divide your AWS account's available concurrency in an AWS Region into pools, use [reserved concurrency](configuration-concurrency.md "configuration-concurrency.md"). Reserved concurrency ensures that a function can
always scale to its assigned concurrency, and that it doesn't scale beyond its assigned concurrency.

## General: Cannot invoke function with other accounts or services

**Issue:**
_You can invoke your function directly, but it doesn't run when another service or account invokes
it._

You grant [other services](lambda-services.md "lambda-services.md") and accounts permission to invoke a function in
the function's [resource-based policy](access-control-resource-based.md "access-control-resource-based.md"). If the invoker is in
another account, that user must also have [permission to invoke
functions](access-control-identity-based.md "access-control-identity-based.md").

## General: Function invocation is looping

**Issue:**
_Function is invoked continuously in a loop._

This typically occurs when your function manages resources in the same AWS service that triggers it. For
example, it's possible to create a function that stores an object in an Amazon Simple Storage Service (Amazon S3) bucket that's configured
with a [notification that invokes the function again](with-s3.md "with-s3.md"). To stop the function from
running, reduce the available [concurrency](lambda-concurrency.md "lambda-concurrency.md") to zero, which throttles all future
invocations. Then, identify the code path or configuration error that caused the recursive
invocation. Lambda automatically detects and stops recursive loops for some AWS services and SDKs. For more information, see
[Use Lambda recursive loop detection to prevent infinite loops](invocation-recursion.md "invocation-recursion.md").

## Lambda: Alias routing with provisioned concurrency

**Issue:**
_Provisioned concurrency spillover invocations during alias routing._

Lambda uses a simple probabilistic model to distribute the traffic between the two function versions. At low
traffic levels, you might see a high variance between the configured and actual percentage of traffic on each
version. If your function uses provisioned concurrency, you can avoid [spillover invocations](monitoring-metrics-types.md#invocation-metrics "monitoring-metrics-types.md#invocation-metrics") by configuring a higher number of
provisioned concurrency instances during the time that alias routing is active.

## Lambda: Cold starts with provisioned concurrency

**Issue:**
_You see cold starts after enabling provisioned concurrency._

When the number of concurrent executions on a function is less than or equal to the [configured level of provisioned concurrency](provisioned-concurrency.md "provisioned-concurrency.md"), there
shouldn't be any cold starts. To help you confirm if provisioned concurrency is operating normally, do the
following:

- [Check that provisioned concurrency is enabled](provisioned-concurrency.md "provisioned-concurrency.md") on the function version or alias.

###### Note

Provisioned concurrency is not configurable on the unpublished [version of the function](configuration-versions.md "configuration-versions.md") ($LATEST).

- Ensure that your triggers invoke the correct function version or alias. For example, if you're using
  Amazon API Gateway, check that API Gateway invokes the function version or alias with provisioned concurrency, not $LATEST. To
  confirm that provisioned concurrency is being used, you can check the [ProvisionedConcurrencyInvocations Amazon CloudWatch metric](monitoring-concurrency.md#provisioned-concurrency-metrics "monitoring-concurrency.md#provisioned-concurrency-metrics"). A non-zero
  value indicates that the function is processing invocations on initialized execution environments.
- Determine whether your function concurrency exceeds the configured level of provisioned concurrency by
  checking the [ProvisionedConcurrencySpilloverInvocations CloudWatch
  metric](monitoring-concurrency.md#provisioned-concurrency-metrics "monitoring-concurrency.md#provisioned-concurrency-metrics"). A non-zero value indicates that all provisioned concurrency is in use and some invocation
  occurred with a cold start.
- Check your [invocation frequency](gettingstarted-limits.md#api-requests "gettingstarted-limits.md#api-requests") (requests per second).
  Functions with provisioned concurrency have a maximum rate of 10 requests per second per provisioned
  concurrency. For example, a function configured with 100 provisioned concurrency can handle 1,000 requests per
  second. If the invocation rate exceeds 1,000 requests per second, some cold starts can occur.

## Lambda: Cold starts with new versions

**Issue:**
_You see cold starts while deploying new versions of your function._

When you update a function alias, Lambda automatically shifts provisioned concurrency to the new version based
on the weights configured on the alias.

**Error:**
_KMSDisabledException: Lambda was unable to decrypt the environment variables because the KMS key used is
disabled. Please check the function's KMS key settings._

This error can occur if your AWS Key Management Service (AWS KMS) key is disabled, or if the grant that allows Lambda to use the key
is revoked. If the grant is missing, configure the function to use a different key. Then, reassign the custom key to
recreate the grant.

## EFS: Function could not mount the EFS file system

**Error:**
_EFSMountFailureException: The function could not mount the EFS file system with access point
arn:aws:elasticfilesystem:us-east-2:123456789012:access-point/fsap-015cxmplb72b405fd._

The mount request to the function's [file system](configuration-filesystem.md "configuration-filesystem.md") was rejected.
Check the function's permissions, and confirm that its file system and access point exist and are ready for
use.

## EFS: Function could not connect to the EFS file system

**Error:**
_EFSMountConnectivityException: The function couldn't connect to the Amazon EFS file system with access point
arn:aws:elasticfilesystem:us-east-2:123456789012:access-point/fsap-015cxmplb72b405fd. Check your network
configuration and try again._

The function couldn't establish a connection to the function's [file
system](configuration-filesystem.md "configuration-filesystem.md") with the NFS protocol (TCP port 2049). Check the [security group and routing configuration](../../../efs/latest/ug/network-access.md "../../../efs/latest/ug/network-access.md") for the VPC's subnets.

If you get these errors after updating your function's VPC configuration settings, try unmounting and
remounting the file system.

## EFS: Function could not mount the EFS file system due to timeout

**Error:**
_EFSMountTimeoutException: The function could not mount the EFS file system with access point
{arn:aws:elasticfilesystem:us-east-2:123456789012:access-point/fsap-015cxmplb72b405fd} due to mount time
out._

The function could connect to the function's [file system](configuration-filesystem.md "configuration-filesystem.md"), but
the mount operation timed out. Try again after a short time and consider limiting the function's [concurrency](configuration-concurrency.md "configuration-concurrency.md") to reduce load on the file system.

## Lambda: Lambda detected an IO process that was taking too long

_EFSIOException: This function instance was stopped because Lambda detected an IO process that was taking
too long._

A previous invocation timed out and Lambda couldn't terminate the function handler. This issue can occur when an
attached file system runs out of burst credits and the baseline throughput is insufficient. To increase throughput,
you can increase the size of the file system or use provisioned throughput.

## Container:

CodeArtifactUserException errors

**Error:**
_CodeArtifactUserPendingException error message_

The CodeArtifact is pending optimization. The function transitions to the [Active state](functions-states.md "functions-states.md") when
Lambda completes the optimization. HTTP response code 409.

**Error:**
_CodeArtifactUserDeletedException error message_

The CodeArtifact is scheduled to be deleted. HTTP response code 409.

**Error:**
_CodeArtifactUserFailedException error message_

Lambda failed to optimize the code. You need to correct the code and upload it again.
HTTP response code 409.

## Container:

InvalidEntrypoint errors

**Error:**
_Runtime.ExitError or "errorType": "Runtime.InvalidEntrypoint"_

Verify that the ENTRYPOINT to your container image includes the absolute path as the
location. Also verify that the image does not contain a symlink as the ENTRYPOINT.

**Error:**
_You are using an CloudFormation template, and your container ENTRYPOINT is being overridden
with a null or empty value._

Review the [ImageConfig](../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-imageconfig.md "../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-imageconfig.md") resource in the CloudFormation template. If you declare an
`ImageConfig` resource in your template, you must provide non-empty values for
all three of the properties.
