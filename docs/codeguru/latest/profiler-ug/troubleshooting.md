# Troubleshooting

This section helps you troubleshoot common problems you might encounter when working with
Amazon CodeGuru Profiler.

###### Topics

- [Why are certain methods missing from my
  profile?](#troubleshooting-missing-functions "#troubleshooting-missing-functions")
- [I don't see any messages from CodeGuru Profiler in my
  application logs.](#troubleshooting-agent-not-running "#troubleshooting-agent-not-running")
- [I get a
  ResourceNotFoundException in the application logs. The profiling group doesn't
  exist.](#troubleshooting-profiler-group-does-not-exist "#troubleshooting-profiler-group-does-not-exist")
- [I received a 403 Forbidden error in the
  agent. The agent doesn't have permission to submit data.](#troubleshooting-agent-permission "#troubleshooting-agent-permission")
- [I don't see any data in the console.](#troubleshooting-no-data "#troubleshooting-no-data")
- [There isn't enough data. The profile only
  has a few frames.](#troubleshooting-not-enough-data "#troubleshooting-not-enough-data")
- [I don’t see any profiling data for my AWS Lambda
  function.](#troubleshooting-lambda "#troubleshooting-lambda")
- [I have errors in my Lambda function log.](#troubleshooting-lambda-error "#troubleshooting-lambda-error")
- [I received a ValidationException
  error in the agent.](#troubleshooting-lambda-agent "#troubleshooting-lambda-agent")
- [Why don't I see heap summary data?](#troubleshooting-heap-summary "#troubleshooting-heap-summary")

## Why are certain methods missing from my

profile?

The CodeGuru Profiler tool can miss methods that the Java virtual machine (JVM) has chosen to inline
for performance reasons. This inlining biases the CodeGuru Profiler data.

Additionally, because CodeGuru Profiler does statistical sampling, methods that are rarely called or
are executed quickly might not be sampled in any given time range.

## I don't see any messages from CodeGuru Profiler in my

application logs.

Make sure CodeGuru Profiler is running. If you are integrating with CodeGuru Profiler by making a code change,
make sure you call `.start()` on your `Profiler` object at the beginning
of your program. If you are integrating with CodeGuru Profiler without making a code change and are
instead using either the JVM command line or Lambda configuration, then make sure all
configuration and environment variables are properly set.

Check the logs to make sure the agent is running. When CodeGuru Profiler starts and is configured
correctly, one of the following log statements appear.

- Java agent: `Starting the profiler`
- Python agent: `Starting profiler`

After you deploy the CodeGuru Profiler agent to your application, wait 15 minutes for data to
arrive.

The following example shows a successful submission of CodeGuru Profiler data when integrating with
your JVM-based application.

```
INFO: Attempting to report profile data: ....

INFO: Successfully reported profile

```

The following example shows a successful submission of CodeGuru Profiler data when integrating with
your Python-based application.

```
INFO: Attempting to report profile data: ....

INFO: Reported profile successfully

```

## I get a

ResourceNotFoundException in the application logs. The profiling group doesn't
exist.

Make sure you've created a profiling group with the same name that is used in the
error through the console or API. Also, be sure you're using the correct AWS Region for the
profiler. Do this by running your application in the same Region where you created the
profiling group, or by manually configuring the agent to target a given Region.

For more information, see [Step 3: Set permissions
for CodeGuru Profiler](setting-up.md#setting-up-step-3 "setting-up.md#setting-up-step-3").

## I received a 403 Forbidden error in the

agent. The agent doesn't have permission to submit data.

Make sure you've given full CodeGuru Profiler permissions to the role with which the agent is
running. Make sure the agent is using the right credentials, either through the default
credential provider or by explicitly providing the credentials in the builder.

For more information, see [Setting up CodeGuru Profiler](setting-up.md "setting-up.md").

## I don't see any data in the console.

Make sure the agent is configured and deployed successfully so that it reports profiles.
By default, the CodeGuru Profiler profiling agent profiles for 5 minutes before submitting its first
profile. Wait 10–15 minutes after the first profile submission, and check the logs to
make sure the agent is running.

## There isn't enough data. The profile only

has a few frames.

For CodeGuru Profiler to provide statistically valid information, it needs your application to be
running under load. We recommend running your application for at least an hour with at least
30% CPU utilization.

## I don’t see any profiling data for my AWS Lambda

function.

You can profile your Lambda functions running in Java or Python if they are called often
enough for CodeGuru Profiler to gather enough data. Invoke your Lambda function several times over a 5
minute period.

Your Lambda function runs the way it typically does, while the CodeGuru Profiler agent runs in
parallel. After running for 5 minutes, the agent submits your first profile. Processing can
take up to 15 minutes.

## I have errors in my Lambda function log.

If you enabled profiling from the Lambda console and continuously see
`CreateProfilingGroup` error messages or `ResourceNotFoundException`
in your logs, your Lambda function did not run long enough for the
`CreateProfilingGroup` API call to succeed. You can manually create a proﬁling
group with Lambda as your compute platform from the CodeGuru Profiler console. Set the name to
`aws-lambda-`lambda-function-name``.

## I received a `ValidationException`

error in the agent.

If you see the following error in your logs, it means you configured your profiling group
for AWS Lambda, but not your agent. For more information on how to configure the agent with
Lambda, see [Profiling your applications that
run on AWS Lambda](setting-up-lambda.md "setting-up-lambda.md").

```
software.amazon.awssdk.services.codeguruprofiler.model.ValidationException: Profiling group is configured for AWS Lambda compute platform, whereas CodeGuru Profiler agent  is not running on AWS Lambda. Please refer to CodeGuru Profiler's documentation to learn more.
```

## Why don't I see heap summary data?

The heap summary feature is supported in **OpenJDK8u262b01+** and all
versions of **OpenJDK11**. If your JDK version is not supported, you will see
a log message from the CodeGuru Profiler agent such as `Cannot use memory profiling features because
 JDK Flight Recorder is not available on this JVM.` In this case, heap summary data
will not be collected.

If your JDK version is supported, make sure heap summary data collection is
enabled.

To enable heap summary data collection by code, add `.withHeapSummary(true)` to
the CodeGuru Profiler builder.

To enable heap summary data collection from the command line, refer to the following
example.

```
-javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.4.jar="profilingGroupName:myProfilingGroup,heapSummaryEnabled:true"
```

To enable heap summary data collection using environment variables, set
`AWS_CODEGURU_PROFILER_HEAP_SUMMARY_ENABLED` to `true`.

### Garbage collection

ACPRP uses data collected during garbage collection cycles to provide the heap summary
feature. The data gathered depends on your application's garbage collection configuration
and activity.

CodeGuru Profiler supports garbage collectors such as Serial, Parallel, CMS, and G1. CodeGuru Profiler
currently does not support Shenandoah and ZGC.

Heap summaries are collected during garbage collection cycles, depending on your garbage
collection algorithm. This typically corresponds to a 'full' or 'old generation' collection,
which is normally the rarest cycle. Depending on your application's characteristics (such as
low-traffic environments or applications that don't have long-lived objects) you may never
see a full collection. In this case, you do not receive heap summary data.

For applications with low garbage collection activity, you can try selecting a wider
time range on the CPU view. Then, check if the heap summary option is available.

You can try to force manual garbage collection in your application periodically by using
`System.gc()`. You can also enable garbage collection logging to monitor which
collections are happening.

### Advanced troubleshooting

Enable the CodeGuru Profiler debugging log. The CodeGuru Profiler agent uses `java.util.logging`
(JUL).

The following is an example `log4j` configuration.

```
<Logger name="javaClass" level="TRACE"/>
<Logger name="software.amazon.codeguruprofilerjavaagent" level="TRACE"/>
```

The following is an example `logging.properties` configuration.

```
javaClass.level=ALL
software.amazon.codeguruprofilerjavaagent.level=ALL
```

###### Note

Including the `javaClass` namespace is important for some messages due to
the way some Kotlin classes are compiled.

Enable Java Flight Recorder debug logging for JDK11+. Add
`'-Xlog:jfr*=trace'` to your JVM arguments to see more logging information from
the Java Flight Recorder subsystem. There are some issues with JDK8 logging, which make it
difficult or impossible to enable these debug logs.
