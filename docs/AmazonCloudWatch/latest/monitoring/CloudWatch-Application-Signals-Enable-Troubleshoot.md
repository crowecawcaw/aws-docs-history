# Troubleshooting your Application Signals installation

This section contains troubleshooting tips for CloudWatch Application Signals.

###### Topics

* [Application Signals Java layer cold start performance](#Application-Signals-troubleshoot-cold-start-performance "#Application-Signals-troubleshoot-cold-start-performance")
* [Application doesn't start after Application Signals is enabled](#Application-Signals-troubleshoot-starting "#Application-Signals-troubleshoot-starting")
* [Python application doesn't start after Application Signals is enabled](#Application-Signals-troubleshoot-starting-Python "#Application-Signals-troubleshoot-starting-Python")
* [No Application Signals data for Python application that uses a WSGI server](#Application-Signals-troubleshoot-Python-WSGI "#Application-Signals-troubleshoot-Python-WSGI")
* [My Node.js application is not instrumented or isn't generating Application Signals telemetry](#Application-Signals-troubleshoot-telemetry-nodejs "#Application-Signals-troubleshoot-telemetry-nodejs")
* [My .NET application isn't instrumented or breaks for AWS SDK calls](#Application-Signals-troubleshoot-sdk-calls "#Application-Signals-troubleshoot-sdk-calls")
* [No application data in Application Signals dashboard](#Application-Signals-troubleshoot-missingdata "#Application-Signals-troubleshoot-missingdata")
* [Service metrics or dependency metrics have Unknown values](#Application-Signals-troubleshoot-unknown-values "#Application-Signals-troubleshoot-unknown-values")
* [Handling a ConfigurationConflict when managing the Amazon CloudWatch 
 Observability EKS add-on](#Application-Signals-troubleshoot-conflict "#Application-Signals-troubleshoot-conflict")
* [I want to filter out unnecessary metrics and traces](#Application-Signals-troubleshoot-cardinality "#Application-Signals-troubleshoot-cardinality")
* [What does InternalOperation mean?](#Application-Signals-troubleshoot-InternalOperation "#Application-Signals-troubleshoot-InternalOperation")
* [How do I enable logging
 for .NET applications?](#Application-Signals-troubleshoot-dotnet-logging "#Application-Signals-troubleshoot-dotnet-logging")
* [How can I resolve assembly version conflicts in .NET applications?](#Application-Signals-troubleshoot-dotnet-conflicts "#Application-Signals-troubleshoot-dotnet-conflicts")
* [Can I disable FluentBit?](#Application-Signals-troubleshoot-FluentBit "#Application-Signals-troubleshoot-FluentBit")
* [Can I filter container logs
 before exporting to CloudWatch Logs?](#Application-Signals-troubleshoot-filter-logs "#Application-Signals-troubleshoot-filter-logs")
* [Resolving TypeError when Using AWS Distro for OpenTelemetry (ADOT) JavaScript Lambda Layer](#lambda-execution "#lambda-execution")
* [TypeError when using Response Streaming Lambda handlers with AWS Distro for OpenTelemetry (ADOT) JavaScript Lambda Layer](#lambda-execution-streaming "#lambda-execution-streaming")
* [Update to required versions of agents or Amazon EKS add-on](#CloudWatch-Application-Signals-Agent-Versions "#CloudWatch-Application-Signals-Agent-Versions")
* [Embedded Metric Format (EMF) disabled for Application Signals](#emf-appsignals "#emf-appsignals")

## Application Signals Java layer cold start performance


Adding the Application Signals Layer to Java Lambda functions increases the startup latency (cold start time). The following tips can help reduce latency for time-sensitive functions.


**Fast startup for Java agent**  – The Application Signals Java Lambda Layer includes a Fast Startup feature that's turned off by default but can be enabled by setting the OTEL\_JAVA\_AGENT\_FAST\_STARTUP\_ENABLED variable to true. When enabled, this feature 
 configures the JVM to use tiered compilation level 1 C1 compiler to generate quick optimized native code for faster cold starts. The C1 compiler prioritizes speed at the cost of long-term optimization whereas the C2 compiler provides superior overall 
 performance by profiling data over time.


For more information, see [Fast startup for Java agent](https://github.com/open-telemetry/opentelemetry-lambda/blob/main/java/README.md#fast-startup-for-java-agent "https://github.com/open-telemetry/opentelemetry-lambda/blob/main/java/README.md#fast-startup-for-java-agent") .


**Reduce cold start times with Provisioned Concurrency** – AWS Lambda provisioned concurrency pre-allocates a specified number of function instances, keeping them initialized and ready to handle requests immediately.
 This reduces cold-start times by eliminating the need to initialize the function environment during execution, ensuring faster and more consistent performance, especially for latency-sensitive workloads. For more information, see [Configuring provisioned concurrency for a function](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html "https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html") .


**Optimize startup performance using Lambda SnapStart** – AWS Lambda SnapStart is a feature that optimizes the startup performance of Lambda functions by creating a pre-initialized snapshot of the execution environment after the function's initialization phase. This snapshot is then reused to start 
 new instances, significantly reducing cold-start times by skipping the initialization process during function invocation. For information, see [Improving startup performance with Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html "https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html") 


## Application doesn't start after Application Signals is enabled


If your application on an Amazon EKS cluster doesn't start after you enable Application Signals on the cluster, check
 for the following:



* Check if the application has been instrumented by another monitoring solution. Application Signals 
 might not support co-existing with other instrumentation solutions.
* Confirm that your the application meets the compatibility requirements to use 
 Application Signals. For more information, see [Supported systems](CloudWatch-Application-Signals-supportmatrix.md "CloudWatch-Application-Signals-supportmatrix.md").
* If your application failed to pull the Application Signals artifacts such as the AWS Distro for
 OpenTelemetery Java or Python agent and CloudWatch agent images, it could be a network issue.

To mitigate the issue, remove the annotation `instrumentation.opentelemetry.io/inject-java: "true"` 
 or `instrumentation.opentelemetry.io/inject-python: "true"`
 from your application deployment manifest, and re-deploy your application. Then check if the application is working.


**Known issues**


The runtime metrics collection in the Java SDK release v1.32.5 is known to not work with applications using JBoss Wildfly. This issue extends to the 
 Amazon CloudWatch Observability EKS add-on, affecting versions `2.3.0-eksbuild.1` through `2.5.0-eksbuild.1`.


If you are impacted, either downgrade the version or disable your runtime metrics collection by adding the 
 environment variable `OTEL_AWS_APPLICATION_SIGNALS_RUNTIME_ENABLED=false` to your application.
 


## Python application doesn't start after Application Signals is enabled


It is a known issue in OpenTelemetry auto-instrumentation that a missing `PYTHONPATH` environment variable can sometimes cause the application to fail to start
. To resolve this, ensure that you set the `PYTHONPATH` environment variable to the location of your application’s working directory.
 For more information about this issue, see 
 [Python autoinstrumentation setting of PYTHONPATH is not compliant with Python's module resolution behavior, breaking Django applications](https://github.com/open-telemetry/opentelemetry-operator/issues/2302 "https://github.com/open-telemetry/opentelemetry-operator/issues/2302").
 


For Django applications, there are additional required configurations, which are outlined in the 
 [OpenTelemetry Python documentation](https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html "https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html").



* Use the `--noreload` flag to prevent automatic reloading.
* Set the `DJANGO_SETTINGS_MODULE` environment variable to the location of your Django application’s `settings.py` file. 
 This ensures that OpenTelemetry can correctly access and integrate with your Django settings.

## No Application Signals data for Python application that uses a WSGI server


If you are using a WSGI server such as Gunicorn or uWSGI, you must make additional changes to make the ADOT Python auto-instrumentation work.


###### Note

Be sure that you are using the latest version of ADOT Python and the Amazon CloudWatch Observability EKS add-on before proceeding.


###### Additional steps to enable Application Signals with a WSGI server

1. Import the auto-instrumentation in the forked worker processes.


For Gunicorn, use the `post_fork` hook:



```
# gunicorn.conf.py
def post_fork(server, worker):
    from opentelemetry.instrumentation.auto_instrumentation import sitecustomize
```

For uWSGI, use the `import` directive.



```
#  uwsgi.ini
[uwsgi]
; required for the instrumentation of worker processes
enable-threads = true
lazy-apps = true
import = opentelemetry.instrumentation.auto_instrumentation.sitecustomize
```
2. Enable the configuration for ADOT Python auto-instrumentation to skip the main process and defer to workers by setting the 
 `OTEL_AWS_PYTHON_DEFER_TO_WORKERS_ENABLED` environment variable to `true`.

## My Node.js application is not instrumented or isn't generating Application Signals telemetry


To enable Application Signals for Node.js, you must ensure that your Node.js application uses the CommonJS (CJS) module format. 
 The AWS Distro for OpenTelemetry Node.js doesn't support the ESM module format, because OpenTelemetry JavaScript’s support 
 of ESM is experimental and is a work in progress.


To determine if your application is using CJS and not ESM, make sure that your application does not fulfill the 
 [conditions to enable ESM](https://nodejs.org/api/esm.html#enabling "https://nodejs.org/api/esm.html#enabling").


## My .NET application isn't instrumented or breaks for AWS SDK calls


The AWS Distro for Open Telemetry (ADOT) SDK for .NET does not support AWS SDK for .NET V4. Use AWS SDK .NET V3 for full Application Signals support.


## No application data in Application Signals dashboard


If metrics or traces are missing in the Application Signals dashboards, the following might be causes. Investigate
 these causes only if you have waited 15 minutes for Application Signals to collect and display data since your 
 last update.



* Make sure that your library and framework you are using is supported by the ADOT Java agent.
For more information, see [Libraries / Frameworks](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md#libraries--frameworks "https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md#libraries--frameworks").
* Make sure that the CloudWatch agent is running. First check the status of the CloudWatch agent pods and make sure 
 they are all in `Running` status.



```
kubectl -n amazon-cloudwatch get pods.
```

Add the following to the CloudWatch agent configuration file to enable debugging logs, and then restart the agent.



```
"agent": {

  "region": "${REGION}",
  "debug": true
},
```

Then check for errors in the CloudWatch agent pods.
* Check for configuration issues with the CloudWatch agent. Confirm that the following is 
 still in the CloudWatch agent configuration file and the agent has been restarted since it was added.



```
"agent": {
  "region": "${REGION}",
  "debug": true
},
```

Then check the OpenTelemetry debugging logs for error messages such as 
 `ERROR io.opentelemetry.exporter.internal.grpc.OkHttpGrpcExporter - Failed to export ...`. These 
 messages might indicate the problem.


If that doesn't solve the issue, dump and check the environment variables with names that start 
 with `OTEL_` by describing the pod with the `kubectl describe pod` command.
* To enable the OpenTelemetry Python debug logging, set the environment variable `OTEL_PYTHON_LOG_LEVEL` to `debug` and redeploy the application.
* Check for wrong or insufficient permissions for exporting data from the CloudWatch
 agent. If you see `Access Denied` messages in the CloudWatch agent logs, this might be the issue. 
 It is possible that the permissions applied when you installed the CloudWatch agent were later changed or revoked.
* Check for an AWS Distro for OpenTelemetry (ADOT) issue when generating telemetry data.


Make sure that the instrumentation annotations `instrumentation.opentelemetry.io/inject-java` and 
  `sidecar.opentelemetry.io/inject-java` are applied to the application deployment and the value is
 `true`. Without these, the application pods will not be instrumented even if the ADOT addon is 
 installed correctly.


Next, check if the `init` container is applied on the application and the `Ready` state
 is `True`. If the `init` container is not ready, see the status for the reason.


If the issue persists, enable debug logging on the OpenTelemetry Java SDK by setting
 the environment variable `OTEL_JAVAAGENT_DEBUG` to true and redeploying the application. Then
 look for messages that start with `ERROR io.telemetry`.
* The metric/span exporter might be dropping data. To find out, check the application log
 for messages that include `Failed to export...`
* The CloudWatch agent might be getting throttled when sending metrics or spans to Application Signals.
 Check for messages indicating throttling in the CloudWatch agent logs.
* Make sure that you've enabled the service discovery setup. You need to do this only once in your Region. 


To confirm this, in the CloudWatch console choose **Application Signals**, **Services**. If Step 1 is
 not marked **Complete**, choose **Start discovering your services**. Data should start flowing in within five minutes.

## Service metrics or dependency metrics have Unknown values


If you see **UnknownService**, **UnknownOperation**, **UnknownRemoteService**, or 
 **UnknownRemoteOperation** for a dependency name or operation in the Application Signals dashboards,
 check whether the occurrence of data points for the unknown remote service and unknown remote operation are 
 coinciding with their deployments.



* **UnknownService** means that the name of an instrumented application is unknown.
 If the `OTEL_SERVICE_NAME` environment variable is undefined and `service.name` isn't specified
 in `OTEL_RESOURCE_ATTRIBUTES`, the service name is set to `UnknownService`. To fix this, 
 specify the service name in `OTEL_SERVICE_NAME` or `OTEL_RESOURCE_ATTRIBUTES`.
* **UnknownOperation** means that the name of an invoked operation is unknown.
 This occurs when Application Signals is unable to discover an operation name which invokes the remote 
 call, or when the extracted operation name contains high cardinality values.
* **UnknownRemoteService** means that the name of the destination service is unknown.
 This occurs when the system is unable to extract the destination service name that the remote call accesses.


One solution is to create a custom span around the function that sends out the request, and add the attribute `aws.remote.service` 
 with the designated value. Another option is to configure the CloudWatch agent to customize the metric value of `RemoteService`. For more
 information about customizations in the CloudWatch agent, see [Enable CloudWatch Application Signals](CloudWatch-Agent-Application_Signals.md "CloudWatch-Agent-Application_Signals.md").
* **UnknownRemoteOperation** means that the name of the destination operation is unknown.
 This occurs when the system is unable to extract the destination operation name that the remote call accesses.


One solution is to create a custom span around the function that sends out the request, and add the attribute `aws.remote.operation` 
 with the designated value. Another option is to configure the CloudWatch agent to customize the metric value of `RemoteOperation`. For more
 information about customizations in the CloudWatch agent, see [Enable CloudWatch Application Signals](CloudWatch-Agent-Application_Signals.md "CloudWatch-Agent-Application_Signals.md").

## Handling a ConfigurationConflict when managing the Amazon CloudWatch 
 Observability EKS add-on


When you install or update the Amazon CloudWatch Observability EKS add-on, if you notice a failure caused by
 a `Health Issue` of type `ConfigurationConflict` with a description that 
 starts with 
 `Conflicts found when trying to apply. Will not continue due to resolve conflicts mode`, 
 it is likely because you already have the CloudWatch agent and its associated components such as the 
 ServiceAccount, the ClusterRole and the ClusterRoleBinding installed on the cluster. When the 
 add-on tries to install the CloudWatch agent and its associated components, if it 
 detects any change in the contents, it by default fails the installation or update to avoid 
 overwriting the state of the resources on the cluster.


If you are trying to onboard to the Amazon CloudWatch Observability EKS add-on and you see this failure, 
 we recommend deleting an existing CloudWatch agent setup that you had previously installed on the cluster 
 and then installing the EKS add-on. Be sure to back up any customizations you might have made 
 to the original CloudWatch agent setup such as a custom agent configuration, and provide these to the
 Amazon CloudWatch Observability EKS add-on when you next install or update it. If you had previously 
 installed the CloudWatch agent for onboarding to Container Insights, see
 [Deleting the CloudWatch agent and Fluent Bit
 for Container Insights](ContainerInsights-delete-agent.md "ContainerInsights-delete-agent.md") for more information.


Alternatively, the add-on supports a conflict resolution configuration option 
 that has the capability to specify `OVERWRITE`. You can use this option to proceed 
 with installing or updating the add-on by overwriting the conflicts on the cluster. 
 If you are using the Amazon EKS console, you'll find the **Conflict resolution method** when you 
 choose the **Optional configuration settings** when you create
 or update the add-on. If you are using the AWS CLI, you can supply the `--resolve-conflicts OVERWRITE` 
 to your command to create or update the add-on.
 


## I want to filter out unnecessary metrics and traces


If Application Signals is collecting traces and metrics that you don't want, see 
 [Manage high-cardinality operations](Application-Signals-Cardinality.md "Application-Signals-Cardinality.md")
 for information about configuring the CloudWatch agent with custom rules to reduce cardinality.


For information about customizing trace sampling rules, see [Configure sampling rules](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-console.html#xray-console "https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-console.html#xray-console") in the X-Ray documentation.


## What does `InternalOperation` mean?


An `InternalOperation` is an operation that is triggered by the application internally rather than by an external invocation.
 Seeing `InternalOperation` is expected, healthy behavior.


Some typical examples where you would see `InternalOperation` include the following:



* **Preloading on start**– Your application performs an operation named `loadDatafromDB` which reads metadata from a 
 database during the warm up phase. Instead of observing `loadDatafromDB` as a service operation, you'll see it categorized as an `InternalOperation`.
* **Async execution in the background**– Your application subscribes to an event queue, and processes streaming data 
 accordingly whenever there’s an update. Each triggered operation will be under `InternalOperation` as a service operation.
* **Retrieving host information from a service registry**– Your application talks to a service registry for service discovery. 
 All interactions with the discovery system are classified as an `InternalOperation`.

## How do I enable logging
 for .NET applications?


To enable logging for .NET applications, configure the following environment variables.
 For more information about how to configure these environment variables, see [Troubleshooting .NET automatic instrumentation issues](https://opentelemetry.io/docs/zero-code/net/troubleshooting/#general-steps "https://opentelemetry.io/docs/zero-code/net/troubleshooting/#general-steps") in the OpenTelemetry
 documentation.



* `OTEL_LOG_LEVEL`
* `OTEL_DOTNET_AUTO_LOG_DIRECTORY`
* `COREHOST_TRACE`
* `COREHOST_TRACEFILE`

## How can I resolve assembly version conflicts in .NET applications?


If you get the following error, see [Assembly version conflicts](https://opentelemetry.io/docs/zero-code/net/troubleshooting/#assembly-version-conflicts "https://opentelemetry.io/docs/zero-code/net/troubleshooting/#assembly-version-conflicts") in the OpenTelemetry documentation for resolution
 steps.



```
Unhandled exception. System.IO.FileNotFoundException: Could not load file or assembly 'Microsoft.Extensions.DependencyInjection.Abstractions, Version=7.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60'. The system cannot find the file specified.

File name: 'Microsoft.Extensions.DependencyInjection.Abstractions, Version=7.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60'
   at Microsoft.AspNetCore.Builder.WebApplicationBuilder..ctor(WebApplicationOptions options, Action`1 configureDefaults)
   at Microsoft.AspNetCore.Builder.WebApplication.CreateBuilder(String[] args)
   at Program.<Main>$(String[] args) in /Blog.Core/Blog.Core.Api/Program.cs:line 26
```

## Can I disable FluentBit?


You can disable FluentBit by configuring the Amazon CloudWatch Observability EKS add-on. For more information, 
 see [(Optional)
 Additional configuration](install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration "install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration").


## Can I filter container logs
 before exporting to CloudWatch Logs?


No, filtering container logs is not yet supported.


## Resolving TypeError when Using AWS Distro for OpenTelemetry (ADOT) JavaScript Lambda Layer


Your Lambda function may fail with this error: `TypeError - "Cannot redefine property: handler"` when you:
 
 
 



* Use the ADOT JavaScript Lambda Layer
* Use `esbuild` to compile TypeScript
* Export your handler with the `export` keyword

The ADOT JavaScript Lambda Layer needs to modify your handler at runtime. When you use the `export` keyword with `esbuild` (directly or through AWS CDK), 
 `esbuild` makes your handler immutable, preventing these modifications.
 
 


Export your handler function using `module.exports` instead of the `export` keyword:
 
 



```
// Before
export const handler = (event) => {
  // Handler Code
}
```


```
// After
const handler = async (event) => {
  // Handler Code
}
module.exports = { handler }
```

## TypeError when using Response Streaming Lambda handlers with AWS Distro for OpenTelemetry (ADOT) JavaScript Lambda Layer


Your Lambda function may fail with this error: `TypeError - "responseStream.write is not a function"` when you:
 
 
 



* Use the ADOT JavaScript Lambda Layer with AWS Lambda Instrumentation enabled (enabled by default)
* Using the response streaming feature in Node.js managed runtimes. For example, when your function handler is like:



```
* export const handler = awslambda.streamifyResponse(...)
```

The AWS Lambda Instrumentation in the ADOT JavaScript Lambda Layer currently does not support Response Streaming in Node.js managed runtimes, so it must be disabled to avoid this TypeError.


## Update to required versions of agents or Amazon EKS add-on


After August 9, 2024, CloudWatch Application Signals will no longer support older versions of the Amazon CloudWatch Observability EKS add-on, 
 the CloudWatch agent, and the AWS Distro for OpenTelemetry auto-instrumentation agent. 



* For the Amazon CloudWatch Observability EKS add-on, versions older than `v1.7.0-eksbuild.1`
 won't be supported.
* For the CloudWatch agent, versions older than `1.300040.0`
 won't be supported.
* For the AWS Distro for OpenTelemetry auto-instrumentation agent:




	+ For Java, versions older than `1.32.2` aren't supported.
	+ For Python, versions older than `0.2.0` aren't supported.
	+ For .NET, versions older than `1.3.2` aren't supported.
	+ For Node.js, versions older than `0.3.0` aren't supported.

###### Important

The latest versions of the agents include updates to the Application Signals metric schema. These updates are not backward compatible, 
 and this can result in data issues if incompatible versions are used. To help ensure a seamless transition to the new 
 functionality, do the following:


* If your application is running on Amazon EKS, be sure to restart all instrumented applications
 after you update the Amazon CloudWatch Observability add-on.
* For applications running on other platforms, be sure to upgrade **both** the CloudWatch agent and the 
 AWS OpenTelemetry auto-instrumentation agent to the latest versions.

The instructions in the following sections can help you update to a supported version.


###### Contents

* [Update the Amazon CloudWatch Observability EKS add-on](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-Upgrade-Addon "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-Upgrade-Addon")


	+ [Use the console](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Upgrade-Addon-Console "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Upgrade-Addon-Console")
	+ [Use the AWS CLI](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Upgrade-Addon-CLI "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Upgrade-Addon-CLI")
* [Update the CloudWatch agent and ADOT agent](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-Upgrade-Agents "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-Upgrade-Agents")


	+ [Update on Amazon ECS](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Upgrade-Agents-ECS "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Upgrade-Agents-ECS")
	+ [Update on Amazon EC2 or other architectures](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Upgrade-Addon-EC2 "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Upgrade-Addon-EC2")

### Update the Amazon CloudWatch Observability EKS add-on


To the Amazon CloudWatch Observability EKS add-on, you can use the AWS Management Console or the AWS CLI.


#### Use the console


###### To upgrade the add-on using the console

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose the name of the Amazon EKS cluster to update.
3. Choose the **Add-ons** tab, then choose **Amazon CloudWatch Observability**.
4. Choose **Edit**, select the version you want to update to, and then choose **Save changes**.


Be sure to choose `v1.7.0-eksbuild.1` or later.
5. Enter one of the following AWS CLI commands to restart your services.



```
  # Restart a deployment
  kubectl rollout restart deployment/`name`
  # Restart a daemonset
  kubectl rollout restart daemonset/`name`
  # Restart a statefulset
  kubectl rollout restart statefulset/`name`
```

#### Use the AWS CLI


###### To upgrade the add-on using the AWS CLI

1. Enter the following command to find the latest version.



```
aws eks describe-addon-versions \
--addon-name amazon-cloudwatch-observability
```
2. Enter the following command to update the add-on. Replace `$VERSION` with a version that 
 is `v1.7.0-eksbuild.1` or later. Replace `$AWS_REGION` and `$CLUSTER` with 
 your Region and cluster name.



```
aws eks update-addon \
--region `$AWS_REGION` \
--cluster-name `$CLUSTER` \
--addon-name amazon-cloudwatch-observability \
--addon-version `$VERSION` \
# required only if the advanced configuration is used.
--configuration-values `$JSON_CONFIG`
```

###### Note

If you're using an custom configuration for the add-on, you can find an example 
 of the configuration to use for `$JSON_CONFIG` in [Enable CloudWatch Application Signals](CloudWatch-Agent-Application_Signals.md "CloudWatch-Agent-Application_Signals.md").
3. Enter one of the following AWS CLI commands to restart your services.



```
  # Restart a deployment
  kubectl rollout restart deployment/`name`
  # Restart a daemonset
  kubectl rollout restart daemonset/`name`
  # Restart a statefulset
  kubectl rollout restart statefulset/`name`
```

### Update the CloudWatch agent and ADOT agent


If your services are running on architectures other than Amazon EKS, you will need to upgrade 
 both the CloudWatch agent and the ADOT auto-instrumentation agent to use the latest Application Signals features.


#### Update on Amazon ECS


###### To upgrade your agents for services running on Amazon ECS

1. Create a new task definition revision. For more information, see 
 [Updating a task definition using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2 "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2").
2. Replace the `$IMAGE` of the `ecs-cwagent` container with the latest image tag from
 [cloudwatch-agent](https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent "https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent") 
 on Amazon ECR.


If you upgrade to a fixed version, be sure to use a version equal to or later than `1.300040.0`.
3. Replace the `$IMAGE` of the `init` container with the latest image tag from the following locations:




	* For Java, use [aws-observability/adot-autoinstrumentation-java](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-java "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-java").
	
	
	If you upgrade to a fixed version, be sure to use a version equal to or later than `1.32.2`.
	* For Python, use [aws-observability/adot-autoinstrumentation-python](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-python "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-python").
	
	
	If you upgrade to a fixed version, be sure to use a version equal to or later than `0.2.0`.
	* For .NET, use [aws-observability/adot-autoinstrumentation-dotnet](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-dotnet "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-dotnet").
	
	
	If you upgrade to a fixed version, be sure to use a version equal to or later
	 than `1.3.2`.
	* For Node.js, use [aws-observability/adot-autoinstrumentation-node](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-node "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-node").
	
	
	If you upgrade to a fixed version, be sure to use a version equal to or later
	 than `0.3.0`.
4. Update the Application Signals environment variables in your app container by following the instructions
 at [Step 4: 
 Instrument your application with the CloudWatch agent](CloudWatch-Application-Signals-ECS-Sidecar.md#CloudWatch-Application-Signals-Enable-ECS-Instrument "CloudWatch-Application-Signals-ECS-Sidecar.md#CloudWatch-Application-Signals-Enable-ECS-Instrument").
5. Deploy your service with the new task definition.

#### Update on Amazon EC2 or other architectures


###### To upgrade your agents for services running on Amazon EC2 or other architectures

1. Be sure to select 
 version `1.300040.0` or later of the CloudWatch agent version.
2. Download the latest version of the AWS Distro for OpenTelemetry auto-instrumentation agent from one of 
 the following locations:




	* For Java, use [aws-otel-java-instrumentation](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-java "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-java") .
	
	
	If you upgrade to a fixed version, be sure to choose `1.32.2` or later.
	* For Python, use [aws-otel-python-instrumentation](https://github.com/aws-observability/aws-otel-python-instrumentation/releases "https://github.com/aws-observability/aws-otel-python-instrumentation/releases") .
	
	
	If you upgrade to a fixed version, be sure to choose `0.2.0` or later.
	* For .NET, use [aws-otel-dotnet-instrumentation](https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases "https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases").
	
	
	If you upgrade to a fixed version, be sure to choose `1.3.2` or
	 later.
	* For Node.js, use [aws-otel-js-instrumentation](https://github.com/aws-observability/aws-otel-js-instrumentation/releases "https://github.com/aws-observability/aws-otel-js-instrumentation/releases") .
	
	
	If you upgrade to a fixed version, be sure to choose `0.3.0` or
	 later.
3. Apply the updated Application Signals environment variables to your application, then start your application. For more
 information, see [Step 3: Instrument your application and start it](CloudWatch-Application-Signals-Enable-EC2Main.md#CloudWatch-Application-Signals-Enable-Other-instrument "CloudWatch-Application-Signals-Enable-EC2Main.md#CloudWatch-Application-Signals-Enable-Other-instrument").

## Embedded Metric Format (EMF) disabled for Application Signals


Disabling EMF for the `/aws/application-signals/data` log group can have the following impact on Application Signals functionality.



* Application Signals metrics and charts will not be displayed
* Application Signals functionality will be degraded

**How do I restore Application Signals?**


When Application Signals displays empty charts or metrics, you must enable EMF for the `/aws/application-signals/data` log group to restore full functionality. For more information, see
 [PutAccountPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html#API_PutAccountPolicy_RequestSyntax "https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html#API_PutAccountPolicy_RequestSyntax").
