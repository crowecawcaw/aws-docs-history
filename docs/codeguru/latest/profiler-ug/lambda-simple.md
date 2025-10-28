# Easier option for Java 8 on Amazon Linux 2 and Java 11 and Java 17 (Corretto)

runtimes

You can enable CodeGuru Profiler from the AWS console by setting environment variables and
updating configuration for your AWS Lambda function. This method works for Java 8 on Amazon Linux 2
and Java 11 and Java 17 (Corretto) runtimes.

If you're profiling applications that run on Lambda, set the following environment
variables to your Lambda function.

- `AWS_CODEGURU_PROFILER_GROUP_NAME` – Identifies the profiling group
  name.
- `AWS_CODEGURU_PROFILER_TARGET_REGION` – Identifies the target
  region of the profiling group.
- `AWS_CODEGURU_PROFILER_HEAP_SUMMARY_ENABLED` – Optional. Set this
  variable to `true` to enable heap summary. The default is
  `false`.
- `JAVA_TOOL_OPTIONS` – Set this variable to
  `-javaagent:/opt/codeguru-profiler-java-agent-standalone.jar`.
  For information about setting environment variables in the AWS Lambda console, see [Using
  AWS Lambda environment variables](../../../lambda/latest/dg/configuration-envvars.md "../../../lambda/latest/dg/configuration-envvars.md").

Add a layer to your Lambda function using the following layer ARN. For more information
on Lambda layers, see [AWS Lambda Layers](../../../lambda/latest/dg/configuration-layers.md#configuration-layers-using "../../../lambda/latest/dg/configuration-layers.md#configuration-layers-using").

```
arn:aws:lambda:`LAMBDA-FUNCTION-REGION-CODE`:157417159150:layer:AWSCodeGuruProfilerJavaAgentLayer:11
```

For example, if your Lambda function is in Region `us-east-1`, then the ARN
would be the following.

```
arn:aws:lambda:us-east-1:157417159150:layer:AWSCodeGuruProfilerJavaAgentLayer:11
```

The CodeGuru Profiler heap summary is an optional feature that shows your application's heap usage
over time. For more information on the heap summary, see [Understanding the heap
summary](working-with-visualizations-heap-summary.md "working-with-visualizations-heap-summary.md").

Your Lambda function runs normally with the CodeGuru Profiler agent running in parallel. The agent
submits your first profile after running for a total of 5 minutes. Processing can take up to
15 minutes.
