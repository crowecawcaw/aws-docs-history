# Deploy using the sidecar strategy


## Step 1: Enable Application Signals
 in your account


You must first enable Application Signals in your account. If you haven't, see [Enable Application Signals in your account](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md").


## Step 2: Create IAM roles


You must create an IAM role. If you already have created this role, you might
 need to add permissions to it.



* **ECS task role—** Containers use this role to run. 
 The permissions should be whatever your applications need, plus **CloudWatchAgentServerPolicy**.

For more information about creating IAM roles, see 
 [Creating IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html").


## Step 3: Prepare CloudWatch agent configuration


First, prepare the agent configuration with Application Signals enabled. To do this, create a local file
 named 
 `/tmp/ecs-cwagent.json`. 



```
{
  "traces": {
    "traces_collected": {
      "application_signals": {}
    }
  },
  "logs": {
    "metrics_collected": {
      "application_signals": {}
    }
  }
}
```

Then upload this configuration to the SSM Parameter Store. To do this, enter the
 following command. In the file, replace `$REGION` with your
 actual Region name.



```
aws ssm put-parameter \
--name "ecs-cwagent" \
--type "String" \
--value "`cat /tmp/ecs-cwagent.json`" \
--region "`$REGION`"
```

## Step 4: 
 Instrument your application with the CloudWatch agent


The next step is to instrument your application for CloudWatch Application Signals.



Java
###### To instrument your application on Amazon ECS with the CloudWatch agent

1. First, specify a bind mount. The volume will be used to share files across containers in the 
 next steps. You will use this bind mount later in this procedure.



```
"volumes": [
  {
    "name": "opentelemetry-auto-instrumentation"
  }
]
```
2. Add a CloudWatch agent sidecar definition. To do this, append a new container called 
 `ecs-cwagent` to your application's task definition. Replace `$REGION` with your actual 
 Region name. Replace `$IMAGE` with the path to the latest CloudWatch container image on Amazon Elastic Container Registry. For more information, see 
 [cloudwatch-agent](https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent "https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent") on Amazon ECR.


If you want to enable the CloudWatch agent with a daemon strategy instead, see the instructions at
 [Deploy using the daemon strategy](CloudWatch-Application-Signals-ECS-Daemon.md "CloudWatch-Application-Signals-ECS-Daemon.md").



```
{
  "name": "ecs-cwagent",
  "image": "`$IMAGE`",
  "essential": true,
  "secrets": [
    {
      "name": "CW_CONFIG_CONTENT",
      "valueFrom": "ecs-cwagent"
    }
  ],
  "logConfiguration": {
    "logDriver": "awslogs",
    "options": {
      "awslogs-create-group": "true",
      "awslogs-group": "/ecs/ecs-cwagent",
      "awslogs-region": "`$REGION`",
      "awslogs-stream-prefix": "ecs"
    }
  }
}
```
3. Append a new container `init` to your application's task definition. Replace
 `$IMAGE` with the latest image from the 
 [AWS Distro for OpenTelemetry Amazon ECR image repository](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-java "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-java").
 



```
{
  "name": "init",
  "image": "`$IMAGE`",
  "essential": false,
  "command": [
    "cp",
    "/javaagent.jar",
    "/otel-auto-instrumentation/javaagent.jar"
  ],
  "mountPoints": [
    {
      "sourceVolume": "opentelemetry-auto-instrumentation",
      "containerPath": "/otel-auto-instrumentation",
      "readOnly": false
    }
  ]
}
```
4. Add a dependency on the `init` container to make sure that this container finishes before your application container starts.



```
"dependsOn": [
  {
    "containerName": "init",
    "condition": "SUCCESS"
  }
]
```
5. Add the following environment variables to your application container. You must be using
 version 1.32.2 or later of the AWS Distro for OpenTelemetry [auto-instrumentation
 agent for Java](https://opentelemetry.io/docs/zero-code/java/agent/ "https://opentelemetry.io/docs/zero-code/java/agent/").




| Environment variable | Setting to enable Application Signals |
| --- | --- |
| `OTEL_RESOURCE_ATTRIBUTES` | Specify the following information as key-value pairs: <br>• `service.name` sets the name of the service. This will be diplayed as the service name for your application in Application Signals dashboards. If you don't provide a value for this key, the default of `UnknownService` is used. <br>• `deployment.environment` sets the environment that the application runs in. This will be diplayed as the **Hosted In** environment of your application in Application Signals dashboards. If you don't specify this, the default of `generic:default` is used. This attribute key is used only by Application Signals, and is converted into X-Ray trace annotations and CloudWatch metric dimensions. (Optional) To enable log correlation for Application Signals, set an additional environment variable `aws.log.group.names` to be the log group name for your application log. By doing so, the traces and metrics from your application can be correlated with the relevant log entries from the log group. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP` with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. To enable metric to log correlation, setting this current environmental variable is enough. For more information, see [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the logging configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md"). |
| `OTEL_AWS_APPLICATION_SIGNALS_ENABLED` | Set to `true` to have your container start sending X-Ray traces and CloudWatch metrics to Application Signals. |
| `OTEL_METRICS_EXPORTER` | Set to `none` to disable other metrics exporters. |
| `OTEL_LOGS_EXPORTER` | Set to `none` to disable other logs exporters. |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | Set to `http/protobuf` to send metrics and traces to Application Signals using HTTP. |
| `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT` | Set to `http://localhost:4316/v1/metrics` to send metrics to the CloudWatch sidecar. |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | Set to `http://localhost:4316/v1/traces` to send traces to the CloudWatch sidecar. |
| `OTEL_TRACES_SAMPLER` | Set this to `xray` to set X-Ray as the traces sampler. |
| `OTEL_PROPAGATORS` | Set `xray` as one of the propagators. |
| `JAVA_TOOL_OPTIONS` | Set to `" -javaagent:$`AWS_ADOT_JAVA_INSTRUMENTATION_PATH`"` Replace `AWS_ADOT_JAVA_INSTRUMENTATION_PATH` with the path where the AWS Distro for OpenTelemetry Java auto-instrumentation agent is stored. For example, `/otel-auto-instrumentation/javaagent.jar` | 6. Mount the volume `opentelemetry-auto-instrumentation` that you defined in step 1 of this procedure. If you don't need to enable log correlation with metrics and traces, use the following example for a Java application. If you want to enable log correlation, see the next step instead. ``` { "name": "`my-app`", ... "environment": [ { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "service.name=`$SVC_NAME`" }, { "name": "OTEL_LOGS_EXPORTER", "value": "none" }, { "name": "OTEL_METRICS_EXPORTER", "value": "none" }, { "name": "OTEL_EXPORTER_OTLP_PROTOCOL", "value": "http/protobuf" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_ENABLED", "value": "true" }, { "name": "JAVA_TOOL_OPTIONS", "value": " -javaagent:/otel-auto-instrumentation/javaagent.jar" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT", "value": "http://localhost:4316/v1/metrics" }, { "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "value": "http://localhost:4316/v1/traces" }, { "name": "OTEL_TRACES_SAMPLER", "value": "xray" }, { "name": "OTEL_PROPAGATORS", "value": "tracecontext,baggage,b3,xray" } ], "dependsOn": [ { "containerName": "init", "condition": "SUCCESS" } ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation", "containerPath": "/otel-auto-instrumentation", "readOnly": false } ] } ``` Python Before you enable Application Signals for your Python applications, be aware of the following considerations. <br>• In some containerized applications, a missing `PYTHONPATH` environment variable can sometimes cause the application to fail to start. To resolve this, ensure that you set the `PYTHONPATH` environment variable to the location of your application’s working directory. This is due to a known issue with OpenTelemetry auto-instrumentation. For more information about this issue, see [Python autoinstrumentation setting of PYTHONPATH is not compliant](https://github.com/open-telemetry/opentelemetry-operator/issues/2302 "https://github.com/open-telemetry/opentelemetry-operator/issues/2302"). <br>• For Django applications, there are additional required configurations, which are outlined in the [OpenTelemetry Python documentation](https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html "https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html"). + Use the `--noreload` flag to prevent automatic reloading. + Set the `DJANGO_SETTINGS_MODULE` environment variable to the location of your Django application’s `settings.py` file. This ensures that OpenTelemetry can correctly access and integrate with your Django settings. <br>• If you're using a WSGI server for your Python application, in addition to the following steps in this section, see [No Application Signals data for Python application that uses a WSGI server](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-Python-WSGI "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-Python-WSGI") for information to make Application Signals work. ###### To instrument your Python application on Amazon ECS with the CloudWatch agent 1. First, specify a bind mount. The volume will be used to share files across containers in the next steps. You will use this bind mount later in this procedure. ``` "volumes": [ { "name": "opentelemetry-auto-instrumentation-python" } ] ``` 2. Add a CloudWatch agent sidecar definition. To do this, append a new container called `ecs-cwagent` to your application's task definition. Replace `$REGION` with your actual Region name. Replace `$IMAGE` with the path to the latest CloudWatch container image on Amazon Elastic Container Registry. For more information, see [cloudwatch-agent](https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent "https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent") on Amazon ECR. If you want to enable the CloudWatch agent with a daemon strategy instead, see the instructions at [Deploy using the daemon strategy](CloudWatch-Application-Signals-ECS-Daemon.md "CloudWatch-Application-Signals-ECS-Daemon.md"). ``` { "name": "ecs-cwagent", "image": "`$IMAGE`", "essential": true, "secrets": [ { "name": "CW_CONFIG_CONTENT", "valueFrom": "ecs-cwagent" } ], "logConfiguration": { "logDriver": "awslogs", "options": { "awslogs-create-group": "true", "awslogs-group": "/ecs/ecs-cwagent", "awslogs-region": "`$REGION`", "awslogs-stream-prefix": "ecs" } } } ``` 3. Append a new container `init` to your application's task definition. Replace `$IMAGE` with the latest image from the [AWS Distro for OpenTelemetry Amazon ECR image repository](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-python "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-python"). ``` { "name": "init", "image": "$IMAGE", "essential": false, "command": [ "cp", "-a", "/autoinstrumentation/.", "/otel-auto-instrumentation-python" ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation-python", "containerPath": "/otel-auto-instrumentation-python", "readOnly": false } ] } ``` 4. Add a dependency on the `init` container to make sure that this container finishes before your application container starts. ``` "dependsOn": [ { "containerName": "init", "condition": "SUCCESS" } ] ``` 5. Add the following environment variables to your application container.
| Environment variable | Setting to enable Application Signals |
| --- | --- |
| `OTEL_RESOURCE_ATTRIBUTES` | Specify the following information as key-value pairs: <br>• `service.name` sets the name of the service. This will be diplayed as the service name for your application in Application Signals dashboards. If you don't provide a value for this key, the default of `UnknownService` is used. <br>• `deployment.environment` sets the environment that the application runs in. This will be diplayed as the **Hosted In** environment of your application in Application Signals dashboards. If you don't specify this, the default of `generic:default` is used. This attribute key is used only by Application Signals, and is converted into X-Ray trace annotations and CloudWatch metric dimensions. (Optional) To enable log correlation for Application Signals, set an additional environment variable `aws.log.group.names` to be the log group name for your application log. By doing so, the traces and metrics from your application can be correlated with the relevant log entries from the log group. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP` with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. To enable metric to log correlation, setting this current environmental variable is enough. For more information, see [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the logging configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md"). |
| `OTEL_AWS_APPLICATION_SIGNALS_ENABLED` | Set to `true` to have your container start sending X-Ray traces and CloudWatch metrics to Application Signals. |
| `OTEL_METRICS_EXPORTER` | Set to `none` to disable other metrics exporters. |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | Set to `http/protobuf` to send metrics and traces to CloudWatch using HTTP. |
| `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT` | Set to `http://127.0.0.1:4316/v1/metrics` to send metrics to the CloudWatch sidecar. |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | Set to `http://127.0.0.1:4316/v1/traces` to send traces to the CloudWatch sidecar. |
| `OTEL_TRACES_SAMPLER` | Set this to `xray` to set X-Ray as the traces sampler. |
| `OTEL_PROPAGATORS` | Add `xray` as one of the propagators. |
| `OTEL_PYTHON_DISTRO` | Set to `aws_distro` to use the ADOT Python instrumentation. |
| `OTEL_PYTHON_CONFIGURATOR` | Set to `aws_configurator` to use the ADOT Python configuration. |
| `PYTHONPATH` | Replace `$APP_PATH` with the location of the application’s working directory within the container. This is required for the Python interpreter to find your application modules. |
| `DJANGO_SETTINGS_MODULE` | Required only for Django applications. Set it to the location of your Django application’s `settings.py` file. Replace `$PATH_TO_SETTINGS`. | 6. Mount the volume `opentelemetry-auto-instrumentation-python` that you defined in step 1 of this procedure. If you don't need to enable log correlation with metrics and traces, use the following example for a Python application. If you want to enable log correlation, see the next step instead. ``` { "name": "`my-app`", ... "environment": [ { "name": "PYTHONPATH", "value": "/otel-auto-instrumentation-python/opentelemetry/instrumentation/auto_instrumentation:$APP_PATH:/otel-auto-instrumentation-python" }, { "name": "OTEL_EXPORTER_OTLP_PROTOCOL", "value": "http/protobuf" }, { "name": "OTEL_TRACES_SAMPLER", "value": "xray" }, { "name": "OTEL_TRACES_SAMPLER_ARG", "value": "endpoint=http://localhost:2000" }, { "name": "OTEL_LOGS_EXPORTER", "value": "none" }, { "name": "OTEL_PYTHON_DISTRO", "value": "aws_distro" }, { "name": "OTEL_PYTHON_CONFIGURATOR", "value": "aws_configurator" }, { "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "value": "http://localhost:4316/v1/traces" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT", "value": "http://localhost:4316/v1/metrics" }, { "name": "OTEL_METRICS_EXPORTER", "value": "none" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_ENABLED", "value": "true" }, { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "service.name=`$SVC_NAME`" }, { "name": "DJANGO_SETTINGS_MODULE", "value": "$PATH_TO_SETTINGS.settings" } ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation-python", "containerPath": "/otel-auto-instrumentation-python", "readOnly": false } ] } ``` 7. (Optional) To enable log correlation, do the following before you mount the volume. In `OTEL_RESOURCE_ATTRIBUTES`, set an additional environment variable `aws.log.group.names` for the log groups of your application. By doing so, the traces and metrics from your application can be correlated with the relevant log entries from these log groups. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP` with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. To enable metric to log correlation, setting this current environmental variable is enough. For more information, see [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the logging configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md"). The following is an example. To enable log correlation, use this example when you mount the volume `opentelemetry-auto-instrumentation-python` that you defined in step 1 of this procedure. ``` { "name": "`my-app`", ... "environment": [ { "name": "PYTHONPATH", "value": "/otel-auto-instrumentation-python/opentelemetry/instrumentation/auto_instrumentation:$APP_PATH:/otel-auto-instrumentation-python" }, { "name": "OTEL_EXPORTER_OTLP_PROTOCOL", "value": "http/protobuf" }, { "name": "OTEL_TRACES_SAMPLER", "value": "xray" }, { "name": "OTEL_TRACES_SAMPLER_ARG", "value": "endpoint=http://localhost:2000" }, { "name": "OTEL_LOGS_EXPORTER", "value": "none" }, { "name": "OTEL_PYTHON_DISTRO", "value": "aws_distro" }, { "name": "OTEL_PYTHON_CONFIGURATOR", "value": "aws_configurator" }, { "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "value": "http://localhost:4316/v1/traces" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT", "value": "http://localhost:4316/v1/metrics" }, { "name": "OTEL_METRICS_EXPORTER", "value": "none" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_ENABLED", "value": "true" }, { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "aws.log.group.names=`$YOUR_APPLICATION_LOG_GROUP`,service.name=`$SVC_NAME`" }, { "name": "DJANGO_SETTINGS_MODULE", "value": "$PATH_TO_SETTINGS.settings" } ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation-python", "containerPath": "/otel-auto-instrumentation-python", "readOnly": false } ] } ``` .NET ###### To instrument your application on Amazon ECS with the CloudWatch agent 1. First, specify a bind mount. The volume will be used to share files across containers in the next steps. You will use this bind mount later in this procedure. ``` "volumes": [ { "name": "opentelemetry-auto-instrumentation" } ] ``` 2. Add a CloudWatch agent sidecar definition. To do this, append a new container called `ecs-cwagent` to your application's task definition. Replace `$REGION` with your actual Region name. Replace `$IMAGE` with the path to the latest CloudWatch container image on Amazon Elastic Container Registry. For more information, see [cloudwatch-agent](https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent "https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent") on Amazon ECR. If you want to enable the CloudWatch agent with a daemon strategy instead, see the instructions at [Deploy using the daemon strategy](CloudWatch-Application-Signals-ECS-Daemon.md "CloudWatch-Application-Signals-ECS-Daemon.md"). ``` { "name": "ecs-cwagent", "image": "`$IMAGE`", "essential": true, "secrets": [ { "name": "CW_CONFIG_CONTENT", "valueFrom": "ecs-cwagent" } ], "logConfiguration": { "logDriver": "awslogs", "options": { "awslogs-create-group": "true", "awslogs-group": "/ecs/ecs-cwagent", "awslogs-region": "`$REGION`", "awslogs-stream-prefix": "ecs" } } } ``` 3. Append a new container `init` to your application's task definition. Replace `$IMAGE` with the latest image from the [AWS Distro for OpenTelemetry Amazon ECR image repository](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-dotnet "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-dotnet"). For a Linux container instance, use the following. ``` { "name": "init", "image": "`$IMAGE`", "essential": false, "command": [ "cp", "-a", "autoinstrumentation/.", "/otel-auto-instrumentation" ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation", "containerPath": "/otel-auto-instrumentation", "readOnly": false } ] } ``` For a Windows Server container instance, use the following. ``` { "name": "init", "image": "`$IMAGE`", "essential": false, "command": [ "CMD", "/c", "xcopy", "/e", "C:\\autoinstrumentation\\*", "C:\\otel-auto-instrumentation", "&&", "icacls", "C:\\otel-auto-instrumentation", "/grant", "*S-1-1-0:R", "/T" ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation", "containerPath": "C:\\otel-auto-instrumentation", "readOnly": false } ] } ``` 4. Add a dependency on the `init` container to make sure that this container finishes before your application container starts. ``` "dependsOn": [ { "containerName": "init", "condition": "SUCCESS" } ] ``` 5. Add the following environment variables to your application container. You must be using version 1.1.0 or later of the AWS Distro for OpenTelemetry [auto-instrumentation agent for .NET](https://opentelemetry.io/docs/zero-code/net/ "https://opentelemetry.io/docs/zero-code/net/").
| Environment variable | Setting to enable Application Signals |
| --- | --- |
| `OTEL_RESOURCE_ATTRIBUTES` | Specify the following information as key-value pairs: <br>• `service.name` sets the name of the service. This will be diplayed as the service name for your application in Application Signals dashboards. If you don't provide a value for this key, the default of `UnknownService` is used. <br>• `deployment.environment` sets the environment that the application runs in. This will be diplayed as the **Hosted In** environment of your application in Application Signals dashboards. If you don't specify this, the default of `generic:default` is used. This attribute key is used only by Application Signals, and is converted into X-Ray trace annotations and CloudWatch metric dimensions. |
| `OTEL_AWS_APPLICATION_SIGNALS_ENABLED` | Set to `true` to have your container start sending X-Ray traces and CloudWatch metrics to Application Signals. |
| `OTEL_METRICS_EXPORTER` | Set to `none` to disable other metrics exporters. |
| `OTEL_LOGS_EXPORTER` | Set to `none` to disable other logs exporters. |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | Set to `http/protobuf` to send metrics and traces to Application Signals using HTTP. |
| `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT` | Set to `http://localhost:4316/v1/metrics` to send metrics to the CloudWatch sidecar. |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | Set to `http://localhost:4316/` to send traces to the CloudWatch sidecar. |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | Set to `http://localhost:4316/v1/traces` to send traces to the CloudWatch sidecar. |
| `OTEL_DOTNET_AUTO_HOME` | Set to the installation location of ADOT .NET automatic instrumentation. |
| `OTEL_DOTNET_AUTO_PLUGINS` | Set to `AWS.Distro.OpenTelemetry.AutoInstrumentation.Plugin, AWS.Distro.OpenTelemetry.AutoInstrumentation` to enable the Application Signals plugin. |
| `CORECLR_ENABLE_PROFILING` | Set to `1` to enable the profiler. |
| `CORECLR_PROFILER` | Set to `{918728DD-259F-4A6A-AC2B-B85E1B658318}` as the CLSID of the profiler. |
| `CORECLR_PROFILER_PATH` | Set this to the path of the profiler. On Linux, set it to `${OTEL_DOTNET_AUTO_HOME}/linux-x64/OpenTelemetry.AutoInstrumentation.Native.so` On Windows Server, set it to `${OTEL_DOTNET_AUTO_HOME}/win-x64/OpenTelemetry.AutoInstrumentation.Native.dll` |
| `DOTNET_ADDITIONAL_DEPS` | Set this to the folder path of `${OTEL_DOTNET_AUTO_HOME}/AdditionalDeps`. |
| `DOTNET_SHARED_STORE` | Set this to the folder path of `${OTEL_DOTNET_AUTO_HOME}/store`. |
| `DOTNET_STARTUP_HOOKS` | Set this to path of the managed assembly `${OTEL_DOTNET_AUTO_HOME}/net/OpenTelemetry.AutoInstrumentation.StartupHook.dll` to run before the main application's entry point. | 6. Mount the volume `opentelemetry-auto-instrumentation` that you defined in step 1 of this procedure. For Linux, use the following. ``` { "name": "my-app", ... "environment": [ { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "service.name=$SVC_NAME" }, { "name": "CORECLR_ENABLE_PROFILING", "value": "1" }, { "name": "CORECLR_PROFILER", "value": "{918728DD-259F-4A6A-AC2B-B85E1B658318}" }, { "name": "CORECLR_PROFILER_PATH", "value": "/otel-auto-instrumentation/linux-x64/OpenTelemetry.AutoInstrumentation.Native.so" }, { "name": "DOTNET_ADDITIONAL_DEPS", "value": "/otel-auto-instrumentation/AdditionalDeps" }, { "name": "DOTNET_SHARED_STORE", "value": "/otel-auto-instrumentation/store" }, { "name": "DOTNET_STARTUP_HOOKS", "value": "/otel-auto-instrumentation/net/OpenTelemetry.AutoInstrumentation.StartupHook.dll" }, { "name": "OTEL_DOTNET_AUTO_HOME", "value": "/otel-auto-instrumentation" }, { "name": "OTEL_DOTNET_AUTO_PLUGINS", "value": "AWS.Distro.OpenTelemetry.AutoInstrumentation.Plugin, AWS.Distro.OpenTelemetry.AutoInstrumentation" }, { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "aws.log.group.names=$YOUR_APPLICATION_LOG_GROUP,service.name=aws-dotnet-service-name" }, { "name": "OTEL_LOGS_EXPORTER", "value": "none" }, { "name": "OTEL_METRICS_EXPORTER", "value": "none" }, { "name": "OTEL_EXPORTER_OTLP_PROTOCOL", "value": "http/protobuf" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_ENABLED", "value": "true" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT", "value": "http://localhost:4316/v1/metrics" }, { "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "value": "http://localhost:4316/v1/traces" }, { "name": "OTEL_EXPORTER_OTLP_ENDPOINT", "value": "http://localhost:4316" }, { "name": "OTEL_TRACES_SAMPLER", "value": "xray" }, { "name": "OTEL_TRACES_SAMPLER_ARG", "value": "endpoint=http://localhost:2000" }, { "name": "OTEL_PROPAGATORS", "value": "tracecontext,baggage,b3,xray" } ], "dependsOn": [ { "containerName": "init", "condition": "SUCCESS" } ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation", "containerPath": "/otel-auto-instrumentation", "readOnly": false } ] } ``` For Windows Server, use the following. ``` { "name": "my-app", ... "environment": [ { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "service.name=$SVC_NAME" }, { "name": "CORECLR_ENABLE_PROFILING", "value": "1" }, { "name": "CORECLR_PROFILER", "value": "{918728DD-259F-4A6A-AC2B-B85E1B658318}" }, { "name": "CORECLR_PROFILER_PATH", "value": "C:\\otel-auto-instrumentation\\win-x64\\OpenTelemetry.AutoInstrumentation.Native.dll" }, { "name": "DOTNET_ADDITIONAL_DEPS", "value": "C:\\otel-auto-instrumentation\\AdditionalDeps" }, { "name": "DOTNET_SHARED_STORE", "value": "C:\\otel-auto-instrumentation\\store" }, { "name": "DOTNET_STARTUP_HOOKS", "value": "C:\\otel-auto-instrumentation\\net\\OpenTelemetry.AutoInstrumentation.StartupHook.dll" }, { "name": "OTEL_DOTNET_AUTO_HOME", "value": "C:\\otel-auto-instrumentation" }, { "name": "OTEL_DOTNET_AUTO_PLUGINS", "value": "AWS.Distro.OpenTelemetry.AutoInstrumentation.Plugin, AWS.Distro.OpenTelemetry.AutoInstrumentation" }, { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "aws.log.group.names=$YOUR_APPLICATION_LOG_GROUP,service.name=dotnet-service-name" }, { "name": "OTEL_LOGS_EXPORTER", "value": "none" }, { "name": "OTEL_METRICS_EXPORTER", "value": "none" }, { "name": "OTEL_EXPORTER_OTLP_PROTOCOL", "value": "http/protobuf" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_ENABLED", "value": "true" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT", "value": "http://localhost:4316/v1/metrics" }, { "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "value": "http://localhost:4316/v1/traces" }, { "name": "OTEL_EXPORTER_OTLP_ENDPOINT", "value": "http://localhost:4316" }, { "name": "OTEL_TRACES_SAMPLER", "value": "xray" }, { "name": "OTEL_TRACES_SAMPLER_ARG", "value": "endpoint=http://localhost:2000" }, { "name": "OTEL_PROPAGATORS", "value": "tracecontext,baggage,b3,xray" } ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation", "containerPath": "C:\\otel-auto-instrumentation", "readOnly": false } ], "dependsOn": [ { "containerName": "init", "condition": "SUCCESS" } ] } ``` Node.js ###### Note If you are enabling Application Signals for a Node.js application with ESM, see [Setting up a Node.js application with the ESM module format](#ECS-NodeJs-ESM "#ECS-NodeJs-ESM") before you start these steps. ###### To instrument your application on Amazon ECS with the CloudWatch agent 1. First, specify a bind mount. The volume will be used to share files across containers in the next steps. You will use this bind mount later in this procedure. ``` "volumes": [ { "name": "opentelemetry-auto-instrumentation-node" } ] ``` 2. Add a CloudWatch agent sidecar definition. To do this, append a new container called `ecs-cwagent` to your application's task definition. Replace `$REGION` with your actual Region name. Replace `$IMAGE` with the path to the latest CloudWatch container image on Amazon Elastic Container Registry. For more information, see [cloudwatch-agent](https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent "https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent") on Amazon ECR. If you want to enable the CloudWatch agent with a daemon strategy instead, see the instructions at [Deploy using the daemon strategy](CloudWatch-Application-Signals-ECS-Daemon.md "CloudWatch-Application-Signals-ECS-Daemon.md"). ``` { "name": "ecs-cwagent", "image": "`$IMAGE`", "essential": true, "secrets": [ { "name": "CW_CONFIG_CONTENT", "valueFrom": "ecs-cwagent" } ], "logConfiguration": { "logDriver": "awslogs", "options": { "awslogs-create-group": "true", "awslogs-group": "/ecs/ecs-cwagent", "awslogs-region": "`$REGION`", "awslogs-stream-prefix": "ecs" } } } ``` 3. Append a new container `init` to your application's task definition. Replace `$IMAGE` with the latest image from the [AWS Distro for OpenTelemetry Amazon ECR image repository](https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-node "https://gallery.ecr.aws/aws-observability/adot-autoinstrumentation-node"). ``` { "name": "init", "image": "`$IMAGE`", "essential": false, "command": [ "cp", "-a", "/autoinstrumentation/.", "/otel-auto-instrumentation-node" ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation-node", "containerPath": "/otel-auto-instrumentation-node", "readOnly": false } ], } ``` 4. Add a dependency on the `init` container to make sure that this container finishes before your application container starts. ``` "dependsOn": [ { "containerName": "init", "condition": "SUCCESS" } ] ``` 5. Add the following environment variables to your application container.
| Environment variable | Setting to enable Application Signals |
| --- | --- |
| `OTEL_RESOURCE_ATTRIBUTES` | Specify the following information as key-value pairs: <br>• `service.name` sets the name of the service. This will be diplayed as the service name for your application in Application Signals dashboards. If you don't provide a value for this key, the default of `UnknownService` is used. <br>• `deployment.environment` sets the environment that the application runs in. This will be diplayed as the **Hosted In** environment of your application in Application Signals dashboards. If you don't specify this, the default of `generic:default` is used. This attribute key is used only by Application Signals, and is converted into X-Ray trace annotations and CloudWatch metric dimensions. (Optional) To enable log correlation for Application Signals, set an additional environment variable `aws.log.group.names` to be the log group name for your application log. By doing so, the traces and metrics from your application can be correlated with the relevant log entries from the log group. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP` with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. To enable metric to log correlation, setting this current environmental variable is enough. For more information, see [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the logging configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md"). |
| `OTEL_AWS_APPLICATION_SIGNALS_ENABLED` | Set to `true` to have your container start sending X-Ray traces and CloudWatch metrics to Application Signals. |
| `OTEL_METRICS_EXPORTER` | Set to `none` to disable other metrics exporters. |
| `OTEL_LOGS_EXPORTER` | Set to `none` to disable other logs exporters. |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | Set to `http/protobuf` to send metrics and traces to Application Signals using OTLP/HTTP and protobuf. |
| `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT` | Set to `http://localhost:4316/v1/metrics` to send metrics to the CloudWatch sidecar. |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | Set to `http://localhost:4316/v1/traces` to send traces to the CloudWatch sidecar. |
| `OTEL_TRACES_SAMPLER` | Set this to `xray` to set X-Ray as the traces sampler. |
| `OTEL_PROPAGATORS` | Set `xray` as one of the propagators. |
| `NODE_OPTIONS` | Set to `--require `AWS_ADOT_NODE_INSTRUMENTATION_PATH``. Replace `AWS_ADOT_NODE_INSTRUMENTATION_PATH` with the path where the AWS Distro for OpenTelemetry Node.js auto-instrumentation is stored. For example, `/otel-auto-instrumentation-node/autoinstrumentation.js` | 6. Mount the volume `opentelemetry-auto-instrumentation` that you defined in step 1 of this procedure. If you don't need to enable log correlation with metrics and traces, use the following example for a Node.js application. If you want to enable log correlation, see the next step instead. For your Application Container, add a dependency on the `init` container to make sure that container finishes before your application container starts. ``` { "name": "`my-app`", ... "environment": [ { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "service.name=`$SVC_NAME`" }, { "name": "OTEL_LOGS_EXPORTER", "value": "none" }, { "name": "OTEL_METRICS_EXPORTER", "value": "none" }, { "name": "OTEL_EXPORTER_OTLP_PROTOCOL", "value": "http/protobuf" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_ENABLED", "value": "true" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT", "value": "http://localhost:4316/v1/metrics" }, { "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "value": "http://localhost:4316/v1/traces" }, { "name": "OTEL_TRACES_SAMPLER", "value": "xray" }, { "name": "OTEL_TRACES_SAMPLER_ARG", "value": "endpoint=http://localhost:2000" }, { "name": "NODE_OPTIONS", "value": "--require /otel-auto-instrumentation-node/autoinstrumentation.js" } ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation-node", "containerPath": "/otel-auto-instrumentation-node", "readOnly": false } ], "dependsOn": [ { "containerName": "init", "condition": "SUCCESS" } ] } ``` 7. (Optional) To enable log correlation, do the following before you mount the volume. In `OTEL_RESOURCE_ATTRIBUTES`, set an additional environment variable `aws.log.group.names` for the log groups of your application. By doing so, the traces and metrics from your application can be correlated with the relevant log entries from these log groups. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP` with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. To enable metric to log correlation, setting this current environmental variable is enough. For more information, see [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the logging configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md"). The following is an example. Use this example to enable log correlation when you mount the volume `opentelemetry-auto-instrumentation` that you defined in step 1 of this procedure. ``` { "name": "`my-app`", ... "environment": [ { "name": "OTEL_RESOURCE_ATTRIBUTES", "value": "aws.log.group.names=`$YOUR_APPLICATION_LOG_GROUP`,service.name=`$SVC_NAME`" }, { "name": "OTEL_LOGS_EXPORTER", "value": "none" }, { "name": "OTEL_METRICS_EXPORTER", "value": "none" }, { "name": "OTEL_EXPORTER_OTLP_PROTOCOL", "value": "http/protobuf" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_ENABLED", "value": "true" }, { "name": "OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT", "value": "http://localhost:4316/v1/metrics" }, { "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "value": "http://localhost:4316/v1/traces" }, { "name": "OTEL_TRACES_SAMPLER", "value": "xray" }, { "name": "OTEL_TRACES_SAMPLER_ARG", "value": "endpoint=http://localhost:2000" }, { "name": "NODE_OPTIONS", "value": "--require /otel-auto-instrumentation-node/autoinstrumentation.js" } ], "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation-node", "containerPath": "/otel-auto-instrumentation-node", "readOnly": false } ], "dependsOn": [ { "containerName": "init", "condition": "SUCCESS" } ] } ``` **Setting up a Node.js application with the ESM module format** We provide limited support for Node.js applications with the ESM module format. For details, see [Known limitations about Node.js with ESM](CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations "CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations"). For the ESM module format, using the `init` container to inject the Node.js instrumentation SDK doesn’t apply. To enable Application Signals for Node.js with ESM, skip steps 1 and 3 of the previous procedure, and do the following instead. ###### To enable Application Signals for a Node.js application with ESM 1. Install the relevant dependencies to your Node.js application for autoinstrumentation: ``` npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation npm install @opentelemetry/instrumentation@0.54.0 ``` 2. In steps 5 and 6 in the previous procedure, remove the mounting of the volume `opentelemetry-auto-instrumentation-node`: ``` "mountPoints": [ { "sourceVolume": "opentelemetry-auto-instrumentation-node", "containerPath": "/otel-auto-instrumentation-node", "readOnly": false } ] ``` Replace the node options with the following. ``` { "name": "NODE_OPTIONS", "value": "--import @aws/aws-distro-opentelemetry-node-autoinstrumentation/register --experimental-loader=@opentelemetry/instrumentation/hook.mjs" } ``` ## Step 5: Deploy your application Create a new revision of your task definition and deploy it to your application cluster. You should see three containers in the newly created task: <br>• `init`– A required container for initializing Application Signals. <br>• `ecs-cwagent`– A container running the CloudWatch agent <br>• ``my-app``– This is the example application container in our documentation. In your actual workloads, this specific container might not exist or might be replaced with your own service containers. ## (Optional) Step 6: Monitor your application health Once you have enabled your applications on Amazon ECS, you can monitor your application health. For more information, see [Monitor the operational health of your applications with Application Signals](Services.md "Services.md").
