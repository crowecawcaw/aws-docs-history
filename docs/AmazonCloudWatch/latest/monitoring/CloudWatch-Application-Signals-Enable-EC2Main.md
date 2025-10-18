# Enable your applications on Amazon EC2

Enable CloudWatch Application Signals on Amazon EC2 by using the custom setup steps described in this section.

For applications running on Amazon EC2, you install and configure the CloudWatch agent and AWS Distro for OpenTelemetry yourself. On these architectures enabled with a custom Application Signals setup, Application Signals 
 doesn't autodiscover the names of your services or the hosts or clusters they run on. You must specify these names during the custom setup, and the names that you specify are what is displayed on Application Signals dashboards.

The instructions in this section are for Java, Python, and .NET applications. The steps
 have been tested on Amazon EC2 instances, but are also expected to work on other architectures
 that support AWS Distro for OpenTelemetry.

**Requirements**


* To get support for Application Signals, you must use the most recent version of both the CloudWatch
 agent and the AWS Distro for OpenTelemetry agent.
* You must have the AWS CLI installed on the instance. We recommend AWS CLI version 2, but version 1
 should also work. For more information about installing the AWS CLI, see
 [Install or update the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html").
###### Important

If you are already using OpenTelemetry with an application that you intend to enable for 
 Application Signals, see [Supported systems](CloudWatch-Application-Signals-supportmatrix.md "CloudWatch-Application-Signals-supportmatrix.md")
 before you enable Application Signals.


## Step 1: Enable Application Signals
 in your account


You must first enable Application Signals in your account. If you haven't, see [Enable Application Signals in your account](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md").


## Step 2: Download and start the CloudWatch agent


###### To install the CloudWatch agent as part of enabling Application Signals on an Amazon EC2 instance or on-premises host

1. Download the latest version of the CloudWatch agent to the instance. If the instance already has the CloudWatch agent
 installed, you might need to update it. Only versions of the agent released on November 30, 2023 or later support
 CloudWatch Application Signals.
2. Before you start the CloudWatch agent, configure it to enable Application Signals. The following
 example is a CloudWatch agent configuration that enables Application Signals for both metrics
 and traces on an EC2 host.


We recommend that you place this file at `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json`
 on Linux systems.



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
3. Attach the **CloudWatchAgentServerPolicy**
 IAM policy to the IAM role of
 your Amazon EC2 instance. For permissions for on-premises hosts, see [Permissions for on-premises servers](#Enable-OnPremise-Permissions "#Enable-OnPremise-Permissions").


	1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
	2. Choose **Roles** and find the role used by your Amazon EC2 instance. Then choose the 
	 name of that role.
	3. In the **Permissions** tab, choose **Add permissions**, 
	 **Attach policies**.
	4. Find **CloudWatchAgentServerPolicy**. Use the search box if needed. Then select the check 
	 box for that policy and choose **Add permissions**.
4. Start the CloudWatch agent by entering the following commands. Replace `agent-config-file-path`
 with the path to the CloudWatch agent configuration file, such as `./amazon-cloudwatch-agent.json`. You must 
 include the `file:` prefix as shown.



```
export CONFIG_FILE_PATH=./amazon-cloudwatch-agent.json
```


```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
-a fetch-config \
-m ec2 -s -c file:`agent-config-file-path`
```

### Permissions for on-premises servers


For an on-premises host, you will need to provide AWS authorization to your device.


###### To set up permissions for an on-premises host

1. Create the IAM user to be used to provide permissions to your on-premises host:


	1. Open the IAM console at
	 [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
	2. Choose **Users**,  **Create User**.
	3. In **User details**, for **User name**, enter a name for the new IAM user. This is the sign-in name for AWS that will be used to authenticate your host. Then 
	 choose **Next**
	4. On the **Set permissions** page, under **Permissions options**, select **Attach policies directly**.
	5. From the **Permissions policies** list, select the **CloudWatchAgentServerPolicy** policy to add to your user. Then choose **Next**.
	6. On the **Review and create** page, ensure that you are satisfied with the user name and that the **CloudWatchAgentServerPolicy** policy is in the **Permissions summary**.
	7. Choose **Create user**
2. Create and retrieve your AWS access key and secret key:


	1. In the navigation pane in the IAM console, choose **Users** and then select the user name of the user that you created in the previous step.
	2. On the user's page, choose the **Security credentials** tab. Then, in the **Access keys** section, choose **Create access key**.
	3. For **Create access key Step 1**, choose **Command Line Interface (CLI)**.
	4. For **Create access key Step 2**, optionally enter a tag and then choose **Next**.
	5. For **Create access key Step 3**, select **Download .csv file** to save a .csv file with your IAM user's access key and secret access key. You need this information for the next steps.
	6. Choose **Done**.
3. Configure your AWS credentials in your on-premises host by entering the following command. Replace `ACCESS_KEY_ID` and `SECRET_ACCESS_ID`
 with your newly generated access key and secret access key from the .csv file that you downloaded in the previous step.



```
$ aws configure
AWS Access Key ID [None]: `ACCESS_KEY_ID`
AWS Secret Access Key [None]: `SECRET_ACCESS_ID`
Default region name [None]: `MY_REGION`
Default output format [None]: json
```

## Step 3: Instrument your application and start it


The next step is to instrument your application for CloudWatch Application Signals.



Java
###### To instrument your Java applications as part of enabling Application Signals on an Amazon EC2 instance or on-premises host

1. Download the latest version of the AWS Distro for OpenTelemetry 
 Java auto-instrumentation agent. You can download the latest version by using 
 [this link](https://github.com/aws-observability/aws-otel-java-instrumentation/releases/latest/download/aws-opentelemetry-agent.jar "https://github.com/aws-observability/aws-otel-java-instrumentation/releases/latest/download/aws-opentelemetry-agent.jar"). You can view information about all released versions at
 [aws-otel-java-instrumentation Releases](https://github.com/aws-observability/aws-otel-java-instrumentation/releases "https://github.com/aws-observability/aws-otel-java-instrumentation/releases").
2. To optimize your Application Signals benefits, use environment variables to 
 provide additional information before you start your application. This information will be displayed
 in Application Signals dashboards.


	1. For the `OTEL_RESOURCE_ATTRIBUTES` variable, specify the following information as
	 key-value pairs:
	
	
	
	
		* (Optional) `service.name` sets the name of the service. This will be displayed as the service 
		 name for your application in Application Signals dashboards. If you don't provide a value for this key, the
		 default of `UnknownService` is used.
		* (Optional) `deployment.environment` sets the environment that the application runs in. 
		 This will be diplayed as the **Hosted In** environment of your
		 application in Application Signals dashboards. If you don't specify this, one of the following defaults is used:
		
		
		
		
			+ If this is an instance that is part of an Auto Scaling group, it is set to `ec2:`name-of-Auto-Scaling-group``
			+ If this is an Amazon EC2 instance that is not part of an Auto Scaling group, it is set to `ec2:default`
			+ If this is an on-premises host, it is set to `generic:default`
		This environment variable is used only by Application Signals, and is converted into X-Ray trace annotations
		 and CloudWatch metric dimensions.
		* For the `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` variable, specify the base endpoint URL where 
		 
		 traces are to be exported to. The CloudWatch agent exposes 4316 as its OTLP port. On Amazon EC2, because applications 
		 communicate with the local CloudWatch agent, you should set this value to 
		 `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces`
		* For the `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT` variable, specify the base endpoint URL where 
		 
		 metrics are to be exported to. The CloudWatch agent exposes 4316 as its OTLP port. On Amazon EC2, because applications 
		 communicate with the local CloudWatch agent, you should set this value to 
		 `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics`
		* For the `JAVA_TOOL_OPTIONS` variable, specify the path where the AWS Distro for OpenTelemetry 
		 Java auto-instrumentation agent is stored.
		
		
		
		```
		export JAVA_TOOL_OPTIONS=" -javaagent:`$AWS_ADOT_JAVA_INSTRUMENTATION_PATH`"
		```
		
		For example:
		
		
		
		```
		export AWS_ADOT_JAVA_INSTRUMENTATION_PATH=./aws-opentelemetry-agent.jar
		```
		* For the `OTEL_METRICS_EXPORTER` variable, we recommend that you set the value to
		 `none`. This disables other metrics exporters so that only the
		 Application Signals exporter is used.
		* Set `OTEL_AWS_APPLICATION_SIGNALS_ENABLED` to `true`. This generates
		 Application Signals metrics from traces.
3. Start your application with the environment variables listed in the previous step. The following
 is an example of a starting script.


###### Note

The following configuration supports only versions 1.32.2 and later of the AWS Distro for OpenTelemetry auto-instrumentation agent for Java.



```
JAVA_TOOL_OPTIONS=" -javaagent:$AWS_ADOT_JAVA_INSTRUMENTATION_PATH" \
OTEL_METRICS_EXPORTER=none \
OTEL_LOGS_EXPORTER=none \
OTEL_AWS_APPLICATION_SIGNALS_ENABLED=true \
OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces \
OTEL_RESOURCE_ATTRIBUTES="service.name=`$YOUR_SVC_NAME`" \
java -jar $MY_JAVA_APP.jar
```
4. (Optional) To enable log correlation, in `OTEL_RESOURCE_ATTRIBUTES`, set an additional environment variable `aws.log.group.names` for the log groups of your application. 
 By doing so, the traces and metrics from your application can be correlated with the relevant log entries from these log groups. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP`
 with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. 
 To enable metric to log correlation, setting this current environmental variable is enough. For more information, see
 [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the 
 logging
 configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md").
 


The following is an example of a starting script that helps enable log correlation. 



```
JAVA_TOOL_OPTIONS=" -javaagent:$AWS_ADOT_JAVA_INSTRUMENTATION_PATH" \
OTEL_METRICS_EXPORTER=none \
OTEL_LOGS_EXPORT=none \
OTEL_AWS_APPLICATION_SIGNALS_ENABLED=true \
OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces \
OTEL_RESOURCE_ATTRIBUTES="aws.log.group.names=`$YOUR_APPLICATION_LOG_GROUP`,service.name=`$YOUR_SVC_NAME`" \
java -jar $MY_JAVA_APP.jar
```


Python
###### Note

If you're using a WSGI server for your Python application, in addition to the following steps in this section, 
 see [No Application Signals data for Python application that uses a WSGI server](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-Python-WSGI "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-Python-WSGI") for information to make Application Signals work.


###### To instrument your Python applications as part of enabling Application Signals on an Amazon EC2 instance

1. Download the latest version of the AWS Distro for OpenTelemetry 
 Python auto-instrumentation agent. Install it by running the following command.



```
pip install aws-opentelemetry-distro
```

You can view information about all released versions at
 [AWS Distro for OpenTelemetry Python instrumentation](https://github.com/aws-observability/aws-otel-python-instrumentation/releases "https://github.com/aws-observability/aws-otel-python-instrumentation/releases").
2. To optimize your Application Signals benefits, use environment variables to 
 provide additional information before you start your application. This information will be displayed
 in Application Signals dashboards.


	1. For the `OTEL_RESOURCE_ATTRIBUTES` variable, specify the following information as
	 key-value pairs:
	
	
	
	
		* `service.name` sets the name of the service. This will be diplayed as the service 
		 name for your application in Application Signals dashboards. If you don't provide a value for this key, the
		 default of `UnknownService` is used.
		* `deployment.environment` sets the environment that the application runs in. 
		 This will be diplayed as the **Hosted In** environment of your
		 application in Application Signals dashboards. If you don't specify this, one of the following defaults is used:
		
		
		
		
			+ If this is an instance that is part of an Auto Scaling group, it is set to `ec2:`name-of-Auto-Scaling-group``.
			+ If this is an Amazon EC2 instance that is not part of an Auto Scaling group, it is set to `ec2:default`
			+ If this is an on-premises host, it is set to `generic:default`
		 This 
		 attribute key is used only by Application Signals, and is converted into X-Ray trace annotations and 
		 CloudWatch metric dimensions.
	2. For the `OTEL_EXPORTER_OTLP_PROTOCOL` variable, specify `http/protobuf` to export telemetry 
	 data over HTTP to the CloudWatch agent endpoints listed in the following steps.
	3. For the `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` variable, specify the base endpoint URL where 
	 
	 traces are to be exported to. The CloudWatch agent exposes 4316 as its OTLP port over HTTP. On Amazon EC2, because applications 
	 communicate with the local CloudWatch agent, you should set this value to 
	 `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces`
	4. For the `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT` variable, specify the base endpoint URL where 
	 
	 metrics are to be exported to. The CloudWatch agent exposes 4316 as its OTLP port over HTTP. On Amazon EC2, because applications 
	 communicate with the local CloudWatch agent, you should set this value to 
	 `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics`
	5. For the `OTEL_METRICS_EXPORTER` variable, we recommend that you set the value to
	 `none`. This disables other metrics exporters so that only the
	 Application Signals exporter is used.
	6. Set the `OTEL_AWS_APPLICATION_SIGNALS_ENABLED` variable to `true` to have your container start sending X-Ray traces and CloudWatch metrics
	 to Application Signals.
3. Start your application with the environment variables discussed in the previous step. The following
 is an example of a starting script.




	* Replace `$SVC_NAME` with your application name. This will
	 be displayed as the name of the application, in Application Signals dashboards.
	* Replace `$PYTHON_APP` with the location and name of your application.

```
OTEL_METRICS_EXPORTER=none \
OTEL_LOGS_EXPORTER=none \
OTEL_AWS_APPLICATION_SIGNALS_ENABLED=true \
OTEL_PYTHON_DISTRO=aws_distro \
OTEL_PYTHON_CONFIGURATOR=aws_configurator \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_TRACES_SAMPLER=xray \
OTEL_TRACES_SAMPLER_ARG="endpoint=http://localhost:2000" \
OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces \
OTEL_RESOURCE_ATTRIBUTES="service.name=`$SVC_NAME`" \
opentelemetry-instrument python `$MY_PYTHON_APP.py`
```

Before you enable Application Signals for your Python applications, be aware of the following considerations.




	* In some containerized applications, a missing `PYTHONPATH` environment variable can sometimes 
	 cause the application to fail to start. To resolve this, ensure that you set the `PYTHONPATH` environment variable 
	 to the location of your application’s working directory. This is due to a known issue with OpenTelemetry auto-instrumentation.
	 For more information about this issue, see 
	 [Python autoinstrumentation setting of PYTHONPATH is not compliant](https://github.com/open-telemetry/opentelemetry-operator/issues/2302 "https://github.com/open-telemetry/opentelemetry-operator/issues/2302").
	* For Django applications, there are additional required configurations, which are outlined 
	 in the [OpenTelemetry Python documentation](https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html "https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html").
	
	
	
	
		+ Use the `--noreload` flag to prevent automatic reloading.
		+ Set the `DJANGO_SETTINGS_MODULE` environment variable to the location of your Django 
		 application’s `settings.py` file. This ensures that OpenTelemetry can correctly access and integrate with your Django settings.
4. (Optional) To enable log correlation, in `OTEL_RESOURCE_ATTRIBUTES`, set an additional environment variable `aws.log.group.names` for the log groups of your application. 
 By doing so, the traces and metrics from your application can be correlated with the relevant log entries from these log groups. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP`
 with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. 
 To enable metric to log correlation, setting this current environmental variable is enough. For more information, see
 [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the 
 logging
 configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md").
 


The following is an example of a starting script that helps enable log correlation. 



```
OTEL_METRICS_EXPORTER=none \
OTEL_LOGS_EXPORTER=none \
OTEL_AWS_APPLICATION_SIGNALS_ENABLED=true \
OTEL_PYTHON_DISTRO=aws_distro \
OTEL_PYTHON_CONFIGURATOR=aws_configurator \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_TRACES_SAMPLER=xray \
OTEL_TRACES_SAMPLER_ARG="endpoint=http://localhost:2000" \
OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces \
OTEL_RESOURCE_ATTRIBUTES="aws.log.group.names=`$YOUR_APPLICATION_LOG_GROUP`,service.name=`$YOUR_SVC_NAME`" \
java -jar `$MY_PYTHON_APP.jar`
```


.NET
###### To instrument your .NET applications as part of enabling Application Signals on an Amazon EC2 instance or on-premises host

1. Download the latest version of the AWS Distro for OpenTelemetry 
 .NET auto-instrumentation package. You can download the latest version at 
 [aws-otel-dotnet-instrumentation Releases](https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases "https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases").
2. To enable Application Signals, set the following environment variables to provide additional information before you start your application. These variables are necessary to set up the startup hook for .NET instrumentation, before you start your 
 .NET application. Replace `dotnet-service-name` in the `OTEL_RESOURCE_ATTRIBUTES` environment variable with the service name of your choice.




	* The following is an example for Linux.
	
	
	
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
	
	export OTEL_RESOURCE_ATTRIBUTES=service.name=dotnet-service-name
	export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
	export OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4316
	export OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://127.0.0.1:4316/v1/metrics
	export OTEL_METRICS_EXPORTER=none
	export OTEL_AWS_APPLICATION_SIGNALS_ENABLED=true
	export OTEL_TRACES_SAMPLER=xray
	export OTEL_TRACES_SAMPLER_ARG=http://127.0.0.1:2000
	```
	* The following is an example for Windows Server.
	
	
	
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
	
	$env:OTEL_RESOURCE_ATTRIBUTES = "service.name=dotnet-service-name"
	$env:OTEL_EXPORTER_OTLP_PROTOCOL = "http/protobuf"
	$env:OTEL_EXPORTER_OTLP_ENDPOINT = "http://127.0.0.1:4316"
	$env:OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT = "http://127.0.0.1:4316/v1/metrics"
	$env:OTEL_METRICS_EXPORTER = "none"
	$env:OTEL_AWS_APPLICATION_SIGNALS_ENABLED = "true"
	$env:OTEL_TRACES_SAMPLER = "xray"
	$env:OTEL_TRACES_SAMPLER_ARG = "http://127.0.0.1:2000"
	```
3. Start your application with the environment variables listed in the previous step.


(Optional) Alternatively, you can use the installation scripts provided to help installation and setup of AWS Distro for OpenTelemetry .NET auto-instrumentation package.


For Linux, download and install the Bash installation script from the GitHub releases page:



```
# Download and Install
curl -L -O https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases/latest/download/aws-otel-dotnet-install.sh
chmod +x ./aws-otel-dotnet-install.sh
./aws-otel-dotnet-install.sh

# Instrument
. $HOME/.otel-dotnet-auto/instrument.sh
export OTEL_RESOURCE_ATTRIBUTES=service.name=dotnet-service-name
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

You can find the NuGet package of the AWS Distro for OpenTelemetry .NET auto-instrumentation package in the 
 [official NuGet repository](https://www.nuget.org/packages/AWS.Distro.OpenTelemetry.AutoInstrumentation "https://www.nuget.org/packages/AWS.Distro.OpenTelemetry.AutoInstrumentation"). Be sure
 to check the [README file](https://github.com/aws-observability/aws-otel-dotnet-instrumentation/blob/main/src/AWS.Distro.OpenTelemetry.AutoInstrumentation/nuget-readme.md "https://github.com/aws-observability/aws-otel-dotnet-instrumentation/blob/main/src/AWS.Distro.OpenTelemetry.AutoInstrumentation/nuget-readme.md") for instructions.


Node.js
###### Note

If you are enabling Application Signals for a Node.js application with ESM, see 

 [Setting up a Node.js application with the ESM module format](#EC2-NodeJs-ESM "#EC2-NodeJs-ESM") before you start these steps.


###### To instrument your Node.js applications as part of enabling Application Signals on an Amazon EC2 instance

1. Download the latest version of the AWS Distro for OpenTelemetry 
 JavaScript auto-instrumentation agent for Node.js. Install it by running the following command.



```
npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation
```

You can view information about all released versions at
 [AWS Distro for OpenTelemetry JavaScript instrumentation](https://github.com/aws-observability/aws-otel-js-instrumentation/releases "https://github.com/aws-observability/aws-otel-js-instrumentation/releases").
2. To optimize your Application Signals benefits, use environment variables to 
 provide additional information before you start your application. This information will be displayed
 in Application Signals dashboards.


	1. For the `OTEL_RESOURCE_ATTRIBUTES` variable, specify the following information as
	 key-value pairs:
	
	
	
	
		* `service.name` sets the name of the service. This will be diplayed as the service 
		 name for your application in Application Signals dashboards. If you don't provide a value for this key, the
		 default of `UnknownService` is used.
		* `deployment.environment` sets the environment that the application runs in. 
		 This will be diplayed as the **Hosted In** environment of your
		 application in Application Signals dashboards. If you don't specify this, one of the following defaults is used:
		
		
		
		
			+ If this is an instance that is part of an Auto Scaling group, it is set to `ec2:`name-of-Auto-Scaling-group``.
			+ If this is an Amazon EC2 instance that is not part of an Auto Scaling group, it is set to `ec2:default`
			+ If this is an on-premises host, it is set to `generic:default`
		 This 
		 attribute key is used only by Application Signals, and is converted into X-Ray trace annotations and 
		 CloudWatch metric dimensions.
	2. For the `OTEL_EXPORTER_OTLP_PROTOCOL` variable, specify `http/protobuf` to export telemetry 
	 data over HTTP to the CloudWatch agent endpoints listed in the following steps.
	3. For the `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` variable, specify the base endpoint URL where 
	 
	 traces are to be exported to. The CloudWatch agent exposes 4316 as its OTLP port over HTTP. On Amazon EC2, because applications 
	 communicate with the local CloudWatch agent, you should set this value to 
	 `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces`
	4. For the `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT` variable, specify the base endpoint URL where 
	 
	 metrics are to be exported to. The CloudWatch agent exposes 4316 as its OTLP port over HTTP. On Amazon EC2, because applications 
	 communicate with the local CloudWatch agent, you should set this value to 
	 `OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics`
	5. For the `OTEL_METRICS_EXPORTER` variable, we recommend that you set the value to
	 `none`. This disables other metrics exporters so that only the
	 Application Signals exporter is used.
	6. Set the `OTEL_AWS_APPLICATION_SIGNALS_ENABLED` variable to `true` to have your container start sending X-Ray traces and CloudWatch metrics
	 to Application Signals.
3. Start your application with the environment variables discussed in the previous step. The following
 is an example of a starting script.




	* Replace `$SVC_NAME` with your application name. This will
	 be displayed as the name of the application, in Application Signals dashboards.

```
OTEL_METRICS_EXPORTER=none \
OTEL_LOGS_EXPORTER=none \
OTEL_AWS_APPLICATION_SIGNALS_ENABLED=true \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_TRACES_SAMPLER=xray \
OTEL_TRACES_SAMPLER_ARG="endpoint=http://localhost:2000" \
OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces \
OTEL_RESOURCE_ATTRIBUTES="service.name=`$SVC_NAME`" \
node --require '@aws/aws-distro-opentelemetry-node-autoinstrumentation/register' `your-application.js`
```
4. (Optional) To enable log correlation, in `OTEL_RESOURCE_ATTRIBUTES`, set an additional environment variable `aws.log.group.names` for the log groups of your application. 
 By doing so, the traces and metrics from your application can be correlated with the relevant log entries from these log groups. For this variable, replace `$YOUR_APPLICATION_LOG_GROUP`
 with the log group names for your application. If you have multiple log groups, you can use an ampersand (`&`) to separate them as in this example: `aws.log.group.names=log-group-1&log-group-2`. 
 To enable metric to log correlation, setting this current environmental variable is enough. For more information, see
 [Enable metric to log correlation](Application-Signals-MetricLogCorrelation.md "Application-Signals-MetricLogCorrelation.md"). To enable trace to log correlation, you'll also need to change the 
 logging
 configuration in your application. For more information, see [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md "Application-Signals-TraceLogCorrelation.md").
 


The following is an example of a starting script that helps enable log correlation. 



```
export OTEL_METRICS_EXPORTER=none \
export OTEL_LOGS_EXPORTER=none \
export OTEL_AWS_APPLICATION_SIGNALS_ENABLED=true \
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
export OTEL_TRACES_SAMPLER=xray \
export OTEL_TRACES_SAMPLER_ARG=endpoint=http://localhost:2000 \
export OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT=http://localhost:4316/v1/metrics \
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4316/v1/traces \
export OTEL_RESOURCE_ATTRIBUTES="aws.log.group.names=`$YOUR_APPLICATION_LOG_GROUP`,service.name=`$SVC_NAME`" \
node --require '@aws/aws-distro-opentelemetry-node-autoinstrumentation/register' `your-application.js`
```

**Setting up a Node.js application with the ESM module format**


We provide limited support for Node.js applications with the ESM module format.
 For details, see [Known limitations about Node.js with ESM](CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations "CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations").


To enable Application Signals for a Node.js application with ESM, you need to modify the steps in the previous 

 procedure.


First, install `@opentelemetry/instrumentation` for your Node.js application:



```
npm install @opentelemetry/instrumentation@0.54.0
```

Then, in steps 3 and 4 in the previous procedure, change the node options from:



```
--require '@aws/aws-distro-opentelemetry-node-autoinstrumentation/register'

```

to the following:



```
--import @aws/aws-distro-opentelemetry-node-autoinstrumentation/register --experimental-loader=@opentelemetry/instrumentation/hook.mjs
```



## (Optional) Step 4: Monitor your application health


Once you have enabled your applications on Amazon EC2, you can monitor your application health. For more information, see [Monitor the operational health of your applications with Application Signals](Services.md "Services.md").
