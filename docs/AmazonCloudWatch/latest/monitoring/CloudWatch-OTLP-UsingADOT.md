# Exporting collector-less telemetry using AWS Distro for OpenTelemetry (ADOT) SDK

You can use the ADOT SDKs to go collector-less and to send traces and logs directly to the OTLP endpoints.

###### Note

Application Signals includes Transaction Search capabilities. To avoid duplicate costs, disable Application Signals in the ADOT SDK and keep `OTEL_AWS_APPLICATION_SIGNALS_ENABLED` set to false (default setting).
 

###### Topics

* [Prerequisite](#CloudWatch-OTLP-UsingADOT-Prerequisite "#CloudWatch-OTLP-UsingADOT-Prerequisite")
* [Set up IAM permissions for your role](#setup-iam-permissions-role "#setup-iam-permissions-role")
* [Configure your credentials providers](#configure-credentials-providers "#configure-credentials-providers")
* [Enabling ADOT SDKs](#Enabling-ADOT "#Enabling-ADOT")

## Prerequisite


Make sure Transaction Search is enabled to send spans to the X-Ray OTLP endpoint. For more information, see [Getting started with Transaction Search](CloudWatch-Transaction-Search-getting-started.md "CloudWatch-Transaction-Search-getting-started.md").


## Set up IAM permissions for your role


Follow these steps to attach the necessary IAM policies to your role:


**Traces:**


1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** and find and select your configured role.
3. Under the **Permissions** tab, choose **Add permissions**, then **Attach policies**.
4. Using the search box, search for the `AWSXrayWriteOnlyPolicy`.
5. Select the `AWSXrayWriteOnlyPolicy` policy and choose **Add permissions**.

**Logs:**


1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** and find and select your configured role.
3. Under the **Permissions** tab, choose **Add permissions**, then **Create inline policy**.
4. Select **CloudWatch Logs** for the service and under **Actions allowed**, filter and select:



```
logs:PutLogEvents
logs:DescribeLogGroups
logs:DescribeLogStreams

```
5. The following is an example IAM policy that grants the required permissions:



```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CloudWatchLogsAccess",
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams"
               
            ],
            "Resource": [
                "arn:aws:logs:*:*:log-group:*"
            ]
        }
    ]
}
```

## Configure your credentials providers


ADOT uses the AWS SDKs to automatically discover valid credentials required to export your telemetry data to AWS. For guidance on configuring credentials for your specific environment, [refer to the documentation on how the AWS SDKS retrieves credentials.](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html "https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html")


**Setting up IAM credentials for on-premise hosts:**


Configure your AWS credentials in your on-premises host by entering the following command. Replace `ACCESS_KEY_ID` and `SECRET_ACCESS_KEY` with the credentials for your configured IAM role or user.



```
$ aws configure
AWS Access Key ID [None]: ACCESS_KEY_ID
AWS Secret Access Key [None]: SECRET_ACCESS_ID
Default region name [None]: MY_REGION
Default output format [None]: json
```

## Enabling ADOT SDKs


You can enable logs and traces for your application to be sent directly to the OTLP endpoints from AWS Distro for OpenTelemetry (ADOT) SDK on Java, Node.js, Python, and .Net.



Java
###### Note

You must use **ADOT Java Agent version 2.11.2 or later** for these features to be available.


1. Download the latest version of the AWS Distro for OpenTelemetry Java auto-instrumentation agent. You can download the latest version by using this command:



```
curl -L -O https://github.com/aws-observability/aws-otel-java-instrumentation/releases/latest/download/aws-opentelemetry-agent.jar
```

You can view information about all released versions at [aws-otel-java-instrumentation Releases](https://github.com/aws-observability/aws-otel-java-instrumentation/releases "https://github.com/aws-observability/aws-otel-java-instrumentation/releases").
2. To enable the different exporter that directly sends telemetry to the OTLP endpoints and to optimize benefits, use the following environment variables before you start your application:


**Traces:**




	* Set `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` to specify the X-Ray OTLP traces endpoint: `https://xray.[`AWSRegion`].amazonaws.com/v1/traces`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="https://xray.us-west-2.amazonaws.com/v1/traces"
	```
	* Set `OTEL_TRACES_EXPORTER` to `otlp` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` variable to `http/protobuf` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_RESOURCE_ATTRIBUTES` variable to specify the following information as key-value pairs. These environment variables are used by Application Signals, and is converted into X-Ray trace annotations and CloudWatch metric dimensions.:
	
	
	
	
		+ (Optional) `service.name` sets the name of the service. This will be displayed as the service name for your application in Application Signals dashboards. If you don't provide a value for this key, the default of `UnknownService` is used.
		+ (Optional) `deployment.environment` sets the environment that the application runs in. This will be displayed as the **Hosted In** environment of your application.
		+ (Optional) To enable log correlation, in `OTEL_RESOURCE_ATTRIBUTES`, set an additional environment variable `aws.log.group.names` for the log groups of your application. By doing so, the traces and metrics from your application can be correlated with the relevant log entries from these log groups. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP` with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. To enable metric to log correlation, setting this current environmental variable is enough. For more information, see [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the logging configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md").
**Logs:**




	* Set `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` to specify the CloudWatch OTLP logs endpoint: `https://logs.[`AWSRegion`].amazonaws.com/v1/logs`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT="https://logs.us-west-2.amazonaws.com/v1/logs"
	```
	* Set `OTEL_EXPORTER_OTLP_LOGS_HEADERS` to specify the log group and log stream (note: these must created **before** running ADOT) you want to export your logs to: `x-aws-log-group=[CW-LOG-GROUP-NAME],x-aws-log-stream=[CW-LOG-STREAM-NAME]`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=MyLogGroup,x-aws-log-stream=default
	```
	* Set `OTEL_LOGS_EXPORTER` to `otlp` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` variable to `http/protobuf` (this is optional and is the default value if this environment variable is not set).
3. Set `JAVA_TOOL_OPTIONS` to specify the path where the AWS Distro for OpenTelemetry Java auto-instrumentation agent is stored. For example:



```
export JAVA_TOOL_OPTIONS=" -javaagent:$AWS_ADOT_JAVA_INSTRUMENTATION_PATH"
export AWS_ADOT_JAVA_INSTRUMENTATION_PATH="./aws-opentelemetry-agent.jar"
```
4. Your application should now be running with ADOT Java instrumentation and will generate spans and logs. Spans will be stored in the `aws/spans` CloudWatch log group, while logs will be stored in the log group specified in the `OTEL_EXPORTER_OTLP_LOGS_HEADERS` header. You can also view the logs and metrics correlated with your spans in the CloudWatch Traces and Metrics Console.
5. Start your application with the environment variables listed in the previous step. The following is an example of a starting script.



```
JAVA_TOOL_OPTIONS=" -javaagent:$AWS_ADOT_JAVA_INSTRUMENTATION_PATH" \
OTEL_METRICS_EXPORTER=none \
OTEL_TRACES_EXPORTER=otlp \
OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://xray.us-east-1.amazonaws.com/v1/traces \
OTEL_LOGS_EXPORTER=otlp \
OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=http/protobuf \
OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=https://logs.us-east-1.amazonaws.com/v1/logs \
OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=MyLogGroup,x-aws-log-stream=default 
OTEL_RESOURCE_ATTRIBUTES="service.name=$YOUR_SVC_NAME" \
java -jar $MY_JAVA_APP.jar
```


Node.js
###### Note

You must use **ADOT JavaScript version 0.7.0 or later** for these features to be available.


1. Download the latest version of the AWS Distro for OpenTelemetry JavaScript auto-instrumentation. Install it by running the following command.



```
npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation
```

You can view information about all released versions at [aws-otel-js-instrumentation Releases](https://github.com/aws-observability/aws-otel-js-instrumentation/releases "https://github.com/aws-observability/aws-otel-js-instrumentation/releases").
2. To enable the different exporter that directly sends telemetry to the OTLP endpoints and to optimize benefits, use the following environment variables before you start your application:


**Traces:**




	* Set `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` to specify the X-Ray OTLP traces endpoint: `https://xray.[`AWSRegion`].amazonaws.com/v1/traces`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="https://xray.us-west-2.amazonaws.com/v1/traces"
	```
	* Set `OTEL_TRACES_EXPORTER` to `otlp` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` variable to `http/protobuf` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_RESOURCE_ATTRIBUTES` variable to specify the following information as key-value pairs. These environment variables are used by Application Signals, and is converted into X-Ray trace annotations and CloudWatch metric dimensions.:
	
	
	
	
		+ (Optional) `service.name` sets the name of the service. This will be displayed as the service name for your application in Application Signals dashboards. If you don't provide a value for this key, the default of `UnknownService` is used.
		+ (Optional) `deployment.environment` sets the environment that the application runs in. This will be diplayed as the **Hosted In** environment of your application.
		+ (Optional) To enable log correlation, in `OTEL_RESOURCE_ATTRIBUTES`, set an additional environment variable `aws.log.group.names` for the log groups of your application. By doing so, the traces and metrics from your application can be correlated with the relevant log entries from these log groups. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP` with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. To enable metric to log correlation, setting this current environmental variable is enough. For more information, see [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the logging configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md").
**Logs:**




	* Set `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` to specify the CloudWatch OTLP logs endpoint: `https://logs.[`AWSRegion`].amazonaws.com/v1/logs`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT="https://logs.us-west-2.amazonaws.com/v1/logs"
	```
	* Set `OTEL_EXPORTER_OTLP_LOGS_HEADERS` to specify the log group and log stream (note: these must created **before** running ADOT) you want to export your logs to: `x-aws-log-group=[CW-LOG-GROUP-NAME],x-aws-log-stream=[CW-LOG-STREAM-NAME]`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=MyLogGroup,x-aws-log-stream=default
	```
	* Set `OTEL_LOGS_EXPORTER` to `otlp` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` variable to `http/protobuf` (this is optional and is the default value if this environment variable is not set).
3. Your application should now be running with ADOT JavaScript instrumentation and will generate spans and logs. Spans will be stored in the `aws/spans` CloudWatch log group, while logs will be stored in the log group specified in the `OTEL_EXPORTER_OTLP_LOGS_HEADERS` header. You can also view the logs and metrics correlated with your spans in the CloudWatch Traces and Metrics Console.
4. Start your application with the environment variables listed in the previous step. The following is an example of a starting script.


Replace `$SVC_NAME` with your application name. This will be displayed as the name of the application.



```
OTEL_METRICS_EXPORTER=none \
OTEL_TRACES_EXPORTER=otlp \
OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://xray.us-east-1.amazonaws.com/v1/traces \
OTEL_LOGS_EXPORTER=otlp \
OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=http/protobuf \
OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=https://logs.us-east-1.amazonaws.com/v1/logs \
OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=MyLogGroup,x-aws-log-stream=default 
OTEL_RESOURCE_ATTRIBUTES="service.name=$YOUR_SVC_NAME" \
node --require '@aws/aws-distro-opentelemetry-node-autoinstrumentation/register' your-application.js
```


Python
###### Note

You must use **ADOT Python version 0.10.0 or later** and have **`botocore`** installed for these features to be available.


1. Download the latest version of the AWS Distro for OpenTelemetry Python auto-instrumentation. Install it by running the following command.



```
pip install aws-opentelemetry-distro
```

You can view information about all released versions at [aws-otel-python-instrumentation Releases](https://github.com/aws-observability/aws-otel-python-instrumentation/releases "https://github.com/aws-observability/aws-otel-python-instrumentation/releases").
2. To enable the different exporter that directly sends telemetry to the OTLP endpoints and to optimize benefits, use the following environment variables before you start your application:


**For both traces and logs configurations, you must set the following environment variables:**




	* `OTEL_PYTHON_DISTRO` to `aws_distro`
	* `OTEL_PYTHON_CONFIGURATOR` to `aws_configurator`
**Traces:**




	* Set `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` to specify the X-Ray OTLP traces endpoint: `https://xray.[`AWSRegion`].amazonaws.com/v1/traces`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="https://xray.us-west-2.amazonaws.com/v1/traces"
	```
	* Set `OTEL_TRACES_EXPORTER` to `otlp` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` variable to `http/protobuf` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_RESOURCE_ATTRIBUTES` variable to specify the following information as key-value pairs. These environment variables are used by Application Signals, and is converted into X-Ray trace annotations and CloudWatch metric dimensions.:
	
	
	
	
		+ (Optional) `service.name` sets the name of the service. This will be displayed as the service name for your application in Application Signals dashboards. If you don't provide a value for this key, the default of `UnknownService` is used.
		+ (Optional) `deployment.environment` sets the environment that the application runs in. This will be diplayed as the **Hosted In** environment of your application.
		+ (Optional) To enable log correlation, in `OTEL_RESOURCE_ATTRIBUTES`, set an additional environment variable `aws.log.group.names` for the log groups of your application. By doing so, the traces and metrics from your application can be correlated with the relevant log entries from these log groups. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP` with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. To enable metric to log correlation, setting this current environmental variable is enough. For more information, see [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the logging configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md").
**Logs:**




	* Set `OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED` to `true`
	* Set `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` to specify the CloudWatch OTLP logs endpoint: `https://logs.[`AWSRegion`].amazonaws.com/v1/logs`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT="https://logs.us-west-2.amazonaws.com/v1/logs"
	```
	* Set `OTEL_EXPORTER_OTLP_LOGS_HEADERS` to specify the log group and log stream (note: these must created **before** running ADOT) you want to export your logs to: `x-aws-log-group=[CW-LOG-GROUP-NAME],x-aws-log-stream=[CW-LOG-STREAM-NAME]`
	
	
	For example:
	
	
	
	```
	export OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=MyLogGroup,x-aws-log-stream=default
	```
	* Set `OTEL_LOGS_EXPORTER` to `otlp` (this is optional and is the default value if this environment variable is not set).
	* Set `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` variable to `http/protobuf` (this is optional and is the default value if this environment variable is not set).
3. Your application should now be running with ADOT Python instrumentation and will generate spans and logs. Spans will be stored in the `aws/spans` CloudWatch log group, while logs will be stored in the log group specified in the `OTEL_EXPORTER_OTLP_LOGS_HEADERS` header. You can also view the logs and metrics correlated with your spans in the CloudWatch Traces and Metrics Console.
4. Start your application with the environment variables listed in the previous step. The following is an example of a starting script.


Replace `$SVC_NAME` with your application name. This will be displayed as the name of the application.


Replace `$PYTHON_APP` with the location and name of your application.



```
OTEL_METRICS_EXPORTER=none \
OTEL_TRACES_EXPORTER=otlp \
OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://xray.us-east-1.amazonaws.com/v1/traces \
OTEL_LOGS_EXPORTER=otlp \
OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=http/protobuf \
OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=https://logs.us-east-1.amazonaws.com/v1/logs \
OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=MyLogGroup,x-aws-log-stream=default
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
OTEL_RESOURCE_ATTRIBUTES="service.name=$YOUR_SVC_NAME" \
opentelemetry-instrument python $MY_PYTHON_APP.py
```


.Net
###### Note


* **ADOT .NET version 1.8.0 or later** is required for these features to be available.
* Compression is currently not supported.
* Logs is currently not supported.

Download the latest version of the AWS Distro for OpenTelemetry .NET auto-instrumentation package. You can view information about all released versions at [aws-otel-dotnet-instrumentation Releases](https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases "https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases").


To enable the different exporters that directly sends telemetry to the OTLP endpoints and to optimize benefits, use the following environment variables before you start your application (replace `dotnet-service-name` in the `OTEL_RESOURCE_ATTRIBUTES` environment variable with the service name of your choice):


**Traces:**



* You **MUST** set `OTEL_TRACES_EXPORTER` to `none`
* You **MUST** set `OTEL_AWS_SIG_V4_ENABLED` to `true`


This feature is **not enabled automatically in .NET**. The environment variable is required specifically to identify this use case within the .NET instrumentation. This requirement is unique to .NET and does **not apply to other supported languages**.

The following is an example setup for Linux.



```
export INSTALL_DIR=OpenTelemetryDistribution
export CORECLR_ENABLE_PROFILING=1
export CORECLR_PROFILER={918728DD-259F-4A6A-AC2B-B85E1B658318}
export CORECLR_PROFILER_PATH=${INSTALL_DIR}/linux-x64/OpenTelemetry.AutoInstrumentation.Native.so
export DOTNET_ADDITIONAL_DEPS=${INSTALL_DIR}/AdditionalDeps
export DOTNET_SHARED_STORE=${INSTALL_DIR}/store
export DOTNET_STARTUP_HOOKS=${INSTALL_DIR}/net/OpenTelemetry.AutoInstrumentation.StartupHook.dll
export OTEL_DOTNET_AUTO_HOME=${INSTALL_DIR}

export OTEL_DOTNET_AUTO_PLUGINS="AWS.Distro.OpenTelemetry.AutoInstrumentation.Plugin, AWS.Distro.OpenTelemetry.AutoInstrumentation"
export OTEL_TRACES_EXPORTER=none
export OTEL_AWS_SIG_V4_ENABLED=true

export OTEL_RESOURCE_ATTRIBUTES=service.name=dotnet-service-name
export OTEL_METRICS_EXPORTER=none
export OTEL_LOGS_EXPORTER=none
export OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://xray.us-east-1.amazonaws.com/v1/traces
```

The following is an example setup for Windows Server:



```
$env:INSTALL_DIR = "OpenTelemetryDistribution" 
$env:CORECLR_ENABLE_PROFILING = 1 
$env:CORECLR_PROFILER = "{918728DD-259F-4A6A-AC2B-B85E1B658318}" 
$env:CORECLR_PROFILER_PATH = Join-Path $env:INSTALL_DIR "win-x64/OpenTelemetry.AutoInstrumentation.Native.dll" 
$env:DOTNET_ADDITIONAL_DEPS = Join-Path $env:INSTALL_DIR "AdditionalDeps" 
$env:DOTNET_SHARED_STORE = Join-Path $env:INSTALL_DIR "store" 
$env:DOTNET_STARTUP_HOOKS = Join-Path $env:INSTALL_DIR "net/OpenTelemetry.AutoInstrumentation.StartupHook.dll" 
$env:OTEL_DOTNET_AUTO_HOME = $env:INSTALL_DIR 
$env:OTEL_DOTNET_AUTO_PLUGINS = "AWS.Distro.OpenTelemetry.AutoInstrumentation.Plugin, AWS.Distro.OpenTelemetry.AutoInstrumentation"

$env:OTEL_TRACES_EXPORTER=none
$env:OTEL_AWS_SIG_V4_ENABLED=true

$env:OTEL_RESOURCE_ATTRIBUTES=service.name=dotnet-service-name
$env:OTEL_METRICS_EXPORTER=none
$env:OTEL_LOGS_EXPORTER=none
$env:OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf
$env:OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://xray.us-east-1.amazonaws.com/v1/traces
```

1. Start your application with the environment variables listed in the previous step.
2. (Optional) Alternatively, you can use the installation scripts provided to help installation and setup of AWS Distro for OpenTelemetry .NET auto-instrumentation package.


For Linux, download and install the Bash installation script from the GitHub releases page:



```
# Download and Install
curl -L -O https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases/latest/download/aws-otel-dotnet-install.sh
chmod +x ./aws-otel-dotnet-install.sh
./aws-otel-dotnet-install.sh
# Instrument
. $HOME/.otel-dotnet-auto/instrument.shexport OTEL_RESOURCE_ATTRIBUTES=service.name=dotnet-service-name
```

For Windows Server, download and install the PowerShell installation script from the GitHub releases page:



```
# Download and Install
$module_url = "https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases/latest/download/AWS.Otel.DotNet.Auto.psm1"
$download_path = Join-Path $env:temp "AWS.Otel.DotNet.Auto.psm1"
Invoke-WebRequest -Uri $module_url -OutFile $download_path
Import-Module $download_path
Install-OpenTelemetryCore
# Instrument
Import-Module $download_path
Register-OpenTelemetryForCurrentSession -OTelServiceName "dotnet-service-name"
Register-OpenTelemetryForIIS
```

You can find the NuGet package of the AWS Distro for OpenTelemetry .NET auto-instrumentation package in the [official NuGet repository](https://www.nuget.org/packages/AWS.Distro.OpenTelemetry.AutoInstrumentation "https://www.nuget.org/packages/AWS.Distro.OpenTelemetry.AutoInstrumentation"). Be sure to check the [README file](https://github.com/aws-observability/aws-otel-dotnet-instrumentation/blob/main/src/AWS.Distro.OpenTelemetry.AutoInstrumentation/nuget-readme.md "https://github.com/aws-observability/aws-otel-dotnet-instrumentation/blob/main/src/AWS.Distro.OpenTelemetry.AutoInstrumentation/nuget-readme.md") for instructions.
