

# Migrating from X-Ray instrumentation to OpenTelemetry instrumentation
<a name="xray-sdk-migration"></a>

**Note**  
X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see [X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md).

 X-Ray is transitioning to OpenTelemetry (OTel) as its primary instrumentation standard for application tracing and observability. This strategic shift aligns AWS with industry best practices and offers customers a more comprehensive, flexible, and future-ready solution for their observability needs. OpenTelemetry's wide adoption in the industry enables tracing of requests across diverse systems, including those outside AWS that may not directly integrate with X-Ray. 

This chapter provides recommendations for a smooth transition, and emphasizes the importance of migrating to OpenTelemetry-based solutions to ensure continued support and access to the latest features in application instrumentation and observability.

It is recommended to adopt OpenTelemetry as the observability solution for instrumenting your application.

**Topics**
+ [Understanding OpenTelemetry](#migration-to-opentelemetry)
+ [Understanding OpenTelemetry concepts for migration](#opentelemetry-concepts)
+ [Migration overview](#migration-overview)
+ [Migrating from X-Ray Daemon to AWS CloudWatch agent or OpenTelemetry collector](#xray-Daemon-migration)
+ [Migrating to OpenTelemetry Java](xray-migration-opentelemetry.md)
+ [Migrate to OpenTelemetry Go](manual-instrumentation-go.md)
+ [Migrate to OpenTelemetry Node.js](migrate-xray-to-opentelemetry-nodejs.md)
+ [Migrate to OpenTelemetry .NET](introduction-dotnet.md)
+ [Migrate to OpenTelemetry Python](migrate-xray-to-opentelemetry-python.md)
+ [Migrate to OpenTelemetry Ruby](migrate-xray-to-opentelemetry-ruby.md)

## Understanding OpenTelemetry
<a name="migration-to-opentelemetry"></a>

OpenTelemetry is an industry-standard observability framework that provides standardized protocols and tools for collecting telemetry data. It offers a unified approach to instrumenting, generating, collecting, and exporting telemetry data such as metrics, logs, and traces.

When you migrate from X-Ray SDKs to OpenTelemetry, you get the following benefits:
+ Enhanced framework and library instrumentation support
+ Support for additional programming languages
+ Automatic instrumentation capabilities
+ Flexible sampling configuration options
+ Unified collection of metrics, logs, and traces

The OpenTelemetry collector provides more options for data collection formats and export destinations than the X-Ray daemon.

### OpenTelemetry support in AWS
<a name="opentelemetry-support"></a>

AWS provides multiple solutions for working with OpenTelemetry:
+ AWS Distro for OpenTelemetry

  Export OpenTelemetry traces as segments to X-Ray.

  For more information, see [AWS Distro for OpenTelemetry](https://aws-otel.github.io/).
+ CloudWatch Application Signals

  Export customized OpenTelemetry traces and metrics to monitor application health.

  For more information, see [Working with Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html).
+ CloudWatch OTel Endpoint

  Export OpenTelemetry traces to X-Ray using the HTTP OTel endpoint with native OpenTelemetry instrumentation.

  For more information, see [Using OTel endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html).

#### Using OpenTelemetry with AWS CloudWatch
<a name="opentelemetry-with-cloudwatch"></a>

AWS CloudWatch supports OpenTelemetry traces through client-side application instrumentation and native AWS CloudWatch services such as Application Signals, Trace, Map, Metrics, and Logs. For more information, see [OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html).

## Understanding OpenTelemetry concepts for migration
<a name="opentelemetry-concepts"></a>

The following table maps X-Ray concepts to their OpenTelemetry equivalents. Understanding these mappings helps you translate your existing X-Ray instrumentation to OpenTelemetry:


|  X-Ray concept | OpenTelemetry concept | 
| --- | --- | 
| X-Ray Recorder | Tracer Provider and Tracers | 
| Service Plugins | Resource Detector | 
| Segment | (Server) Span | 
| Sub-segment | (non-Server) Span | 
| X-Ray Sampling Rules | OpenTelemetry Sampling (Customizable) | 
| X-Ray Emitter | Span Exporter (Customizable) | 
| Annotations/Metadata | Attributes | 
| Library Instrumentation | Library Instrumentation | 
| X-Ray Trace Context | Span Context | 
| X-Ray Trace Context Propagation | W3C Trace Context Propagation | 
| X-Ray Trace Sampling | OpenTelemetry Trace Sampling | 
| N/A | Span Processing | 
| N/A | Baggage | 
| X-Ray Daemon | OpenTelemetry Collector | 

**Note**  
For more information about OpenTelemetry concepts, see the [OpenTelemetry documentation](https://opentelemetry.io/docs).

### Comparing features
<a name="feature-comparison"></a>

The following table shows which features are supported in both services. Use this information to identify any gaps you need to address during migration:


| Feature | X-Ray instrumentation | OpenTelemetry instrumentation | 
| --- | --- | --- | 
| Library instrumentation | Supported | Supported | 
| X-Ray sampling | Supported | Supported in OTel Java/.NET/Go<br />Supported in ADOT Java/.NET/Python/Node.js | 
| X-Ray trace context propagation | Supported | Supported | 
| Resource detection | Supported | Supported | 
| Segment annotations | Supported | Supported | 
| Segment metadata | Supported | Supported | 
| Zero-code auto-instrumentation | Supported in Java | Supported in OTel Java/.NET/Python/Node.js<br />Supported in ADOT Java/.NET/Python/Node.js | 
| Manually trace creation | Supported | Supported | 

### Setting up and configuring tracing
<a name="tracing-setup-configuration"></a>

To create traces in OpenTelemetry, you need a tracer. You get a tracer by initializing a *Tracer Provider* in your application. This is similar to how you use the X-Ray Recorder to configure X-Ray and create segments and subsegments in an X-Ray trace.

**Note**  
The OpenTelemetry *Tracer Provider* offers more configuration options than the X-Ray Recorder.

#### Understanding trace data structure
<a name="trace-data"></a>

After understanding the basic concepts and feature mappings, you can learn about specific implementation details like trace data structure and sampling.

OpenTelemetry uses *spans* instead of segments and subsegments to structure trace data. Each span includes the following components:
+ Name
+ Unique ID
+ Start and end timestamps
+ Span kind
+ Span context
+ Attributes (key-value metadata)
+ Events (timestamped logs)
+ Links to other spans
+ Status information
+ Parent span references

When you migrate to OpenTelemetry, your spans are automatically converted to X-Ray segments or subsegments. This ensures your existing CloudWatch console experience remains unchanged.

##### Working with span attributes
<a name="span-attributes"></a>

The X-Ray SDK provides two ways to add data to segments and subsegments:

Annotations  
Key-value pairs that are indexed for filtering and searching

Metadata  
Key-value pairs containing complex data that isn't indexed for searching

By default, OpenTelemetry span attributes are converted to metadata in X-Ray raw data. To convert specific attributes to annotations instead, add their keys to the `aws.xray.annotations` attributes list.
+ For more information about OpenTelemetry concepts, see [OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/)
+ For details about how OpenTelemetry data maps to X-Ray data, see [OpenTelemetry to X-Ray data model translation](https://aws-otel.github.io/docs/getting-started/X-Ray#otel-to-X-Ray-data-model-translation-behavior-of-aws-X-Ray-exporter)

### Detecting resources in your environment
<a name="resource-detection"></a>

OpenTelemetry uses *Resource Detectors* to collect metadata about the resources that generate telemetry data. This metadata is stored as *Resource Attributes*. For example, an entity producing telemetry could be an Amazon ECS cluster or an Amazon EC2 instance, and the Resource Attributes that can be recorded from these entities can include the Amazon ECS Cluster ARN or Amazon EC2 Instance ID.
+ For information about supported resource types, see [OpenTelemetry Resource Semantic Conventions](https://opentelemetry.io/docs/reference/specification/resource/semantic_conventions/)
+ For information about X-Ray service plugins, see [Configuring the X-Ray SDK](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-configuration.html)

### Managing sampling strategies
<a name="sampling"></a>

Trace sampling helps you manage costs by collecting data from a representative subset of requests instead of all requests. Both OpenTelemetry and X-Ray support sampling, but implement it differently.

**Note**  
Sampling fewer than 100% of traces reduces your observability costs while maintaining meaningful insights into your application's performance.

OpenTelemetry provides several built-in sampling strategies and lets you create custom ones. You can also configure an X-Ray *Remote Sampler* in some SDK languages to use X-Ray sampling rules with OpenTelemetry.

The additional sampling strategies from OpenTelemetry are:
+ Parent-based Sampling – Respects the parent span's sampling decision before applying additional sampling strategies
+ Trace ID Ratio Based Sampling – >Randomly samples a specified percentage of spans
+ Tail sampling – Applies sampling rules to complete traces in the OpenTelemetry Collector
+ Custom samplers – Implement your own sampling logic using the sampling interface

For information about X-Ray sampling rules, see [Sampling rules in the X-Ray console](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html)

For information about OpenTelemetry tail sampling, see [Tail sampling processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor)

### Managing trace context
<a name="trace-context-management"></a>

X-Ray SDKs manage the Segment Context to correctly handle parent-child relationships between Segments and Subsegments in a trace. OpenTelemetry uses a similar mechanism to ensure that spans have the correct parent span. It stores and propagates tracing data throughout a request context. For example, when your application processes a request and creates a server span to represent that request, OpenTelemetry will store the server span in the OpenTelemetry Context so that when a child span is created, that child span can reference the span in the Context as its parent.

### Propagating trace context
<a name="context-propagation"></a>

Both X-Ray and OpenTelemetry use HTTP headers to propagate trace context across services. This allows you to link trace data generated by different services and maintain sampling decisions.

The X-Ray SDK automatically propagates trace context using the X-Ray trace header. When one service calls another, the trace header contains the context needed to maintain parent-child relationships between traces.

OpenTelemetry supports multiple trace header formats for context propagation, including:
+ W3C Trace Context (default)
+ X-Ray trace header
+ Other custom formats

**Note**  
You can configure OpenTelemetry to use one or more header formats. For example, use the X-Ray Propagator to send trace context to AWS services that support X-Ray tracing.

Configure and use the X-Ray Propagator to enable tracing across AWS services. This allows you to propagate trace context to API Gateway endpoints and other services that support X-Ray.
+ For information about X-Ray trace headers, see [Tracing header](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader) in the X-Ray Developer Guide
+ For information about OpenTelemetry context propagation, see [Context and Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/) in the OpenTelemetry documentation

### Using library instrumentation
<a name="library-instrumentations"></a>

Both X-Ray and OpenTelemetry provide library instrumentation that requires minimal code changes to add tracing to your applications.

X-Ray provides library instrumentation functionalities. This allows you to add pre-built X-Ray instrumentations with minimal application code changes. These instrumentations support specific libraries like the AWS SDK and HTTP Clients, as well as web frameworks like Spring Boot or Express.js.

OpenTelemetry's instrumentation libraries generate detailed spans for your libraries through library hooks or automatic code modification, requiring minimal code changes.

To determine if OpenTelemetry's Library Instrumentations supports your library, search for it in the OpenTelemetry Registry at [OpenTelemetry Registry](https://opentelemetry.io/ecosystem/registry/).

### Exporting traces
<a name="exporting-traces"></a>

X-Ray and OpenTelemetry use different methods to export trace data.

#### X-Ray trace export
<a name="xray-export"></a>

The X-Ray SDKs use an emitter to send trace data:
+ Sends segments and subsegments to the X-Ray Daemon
+ Uses UDP for non-blocking I/O
+ Configured by default in the SDK

#### OpenTelemetry trace export
<a name="opentelemetry-export"></a>

OpenTelemetry uses configurable *Span Exporters* to send trace data:
+ Uses *http/protobuf* or *grpc* protocols
+ Exports spans to endpoints monitored by the OpenTelemetry Collector or CloudWatch Agent
+ Allows for custom exporter configurations

### Processing and forwarding traces
<a name="receiving-processing-exporting"></a>

Both X-Ray and OpenTelemetry provide components to receive, process, and forward trace data.

#### X-Ray trace processing
<a name="xray-processing"></a>

The X-Ray Daemon handles trace processing:
+ Listens for UDP traffic from X-Ray SDKs
+ Batches segments and subsegments
+ Uploads batches to the X-Ray service

#### OpenTelemetry trace processing
<a name="opentelemetry-processing"></a>

The OpenTelemetry Collector handles trace processing:
+ Receives traces from instrumented services
+ Processes and optionally modifies trace data
+ Sends processed traces to various backends, including X-Ray

**Note**  
The AWS CloudWatch Agent can also receive and send OpenTelemetry traces to X-Ray. For more information, see [Collect metrics and traces with OpenTelemetry](AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-OpenTelemetry-metrics.html).

### Span processing (OpenTelemetry-specific concept)
<a name="span-processing"></a>

OpenTelemetry uses Span Processors to modify spans as they're created:
+ Allows reading and modifying spans at creation or completion
+ Enables custom logic for span handling

### Baggage (OpenTelemetry-soecific concept)
<a name="baggage"></a>

OpenTelemetry's Baggage feature allows propagation of key-value data:
+ Enables passing arbitrary data alongside trace context
+ Useful for propagating application-specific information across service boundaries

For information about the OpenTelemetry Collector, see [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)

For information about X-Ray concepts, see [X-Ray concepts](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html) in the X-Ray Developer Guide

## Migration overview
<a name="migration-overview"></a>

This section provides an overview of the code changes required for migration. The list below are language-specific guidance and X-Ray Daemon migration steps.

**Important**  
To fully migrate from X-Ray instrumentation to OpenTelemetry instrumentation, you need to:  
Replace X-Ray SDK usage with an OpenTelemetry solution
Replace the X-Ray Daemon with the CloudWatch Agent or OpenTelemetry Collector (with X-Ray Exporter)
+ [Migrating to OpenTelemetry Java](xray-migration-opentelemetry.md)
+ [Migrate to OpenTelemetry Go](manual-instrumentation-go.md)
+ [Migrate to OpenTelemetry Node.js](migrate-xray-to-opentelemetry-nodejs.md)
+ [Migrate to OpenTelemetry .NET](introduction-dotnet.md)
+ [Migrate to OpenTelemetry Python](migrate-xray-to-opentelemetry-python.md)
+ [Migrate to OpenTelemetry Ruby](migrate-xray-to-opentelemetry-ruby.md)

### Recommendations for new and existing applications
<a name="new-applications"></a>

For new and existing applications, it is recommended to use the following solutions to enable tracing in your applications:

Instrumentation  
+ OpenTelemetry SDKs
+ AWS Distro for OpenTelemetry Instrumentation

Data Collection  
+ OpenTelemetry Collector
+ CloudWatch Agent

After migrating to OpenTelemetry-based solutions, your CloudWatch experience will remain the same. You will still be able to view your traces in the same format in the CloudWatch console’s Traces and Trace Map pages, or retrieve your trace data through the [X-Ray APIs](https://docs.aws.amazon.com/xray/latest/devguide/xray-api.html).

### Tracing setup changes
<a name="tracing-setup-migration"></a>

You need to replace the X-Ray setup with an OpenTelemetry setup.


**Comparison of X-Ray and OpenTelemetry setup**  

| Feature | X-Ray SDK | OpenTelemetry | 
| --- | --- | --- | 
| Default configurations |  + X-Ray Centralized Sampling<br />+ X-Ray Trace Context propagation<br />+ Trace Export to X-Ray Daemon  |  + Exporting traces to OpenTelemetry Collector or CloudWatch Agent (HTTP/gRPC)<br />+ W3C Trace Context propagation  | 
| Manual configurations |  + Local sampling rules<br />+ Resource detection plug-ins  |  + X-Ray Sampling (may not be available for all languages)<br />+ Resource detection<br />+ X-Ray Trace Context propagation  | 

### Library instrumentation changes
<a name="library-instrumentation-migration"></a>

Update your code to use OpenTelemetry Library Instrumentation instead of X-Ray Library Instrumentation for AWS SDK, HTTP Clients, Web Frameworks, and other libraries. This generates OpenTelemetry Traces instead of X-Ray Traces.

**Note**  
Code changes vary by language and library. Refer to the language-specific migration guides for detailed instructions.

### Lambda environment instrumentation changes
<a name="lambda-instrumentation-migration"></a>

To use OpenTelemetry in your Lambda functions, choose one of these setup options:

1. Use an auto-instrumentation Lambda Layer:
   + (Recommended) [AWS Lambda Layer for OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.html)
**Note**  
To use only tracing, set the Lambda environment variable `OTEL_AWS_APPLICATION_SIGNALS_ENABLED=false`.
   + [AWS managed Lambda Layer for ADOT](https://aws-otel.github.io/docs/getting-started/lambda)

1. Manually set up OpenTelemetry for your Lambda function:
   + Configure a Simple Span Processor with an X-Ray UDP Span Exporter
   + Set up an X-Ray Lambda propagator

### Manually creating trace data
<a name="manually-creating-trace-data"></a>

Replace X-Ray segments and sub-segments with OpenTelemetry Spans:
+ Use an OpenTelemetry Tracer to create Spans
+ Add attributes to Spans (equivalent to X-Ray metadata and annotations)

**Important**  
When sent to X-Ray:  
Server Spans convert to X-Ray segments
Other Spans convert to X-Ray sub-segments
Attributes convert to metadata by default

To convert an attribute to an annotation, add its key to the `aws.xray.annotations` attribute list. For more information, see [Enable Customized X-Ray Annotations](https://aws-otel.github.io/docs/getting-started/x-ray#enable-the-customized-x-ray-annotations).

## Migrating from X-Ray Daemon to AWS CloudWatch agent or OpenTelemetry collector
<a name="xray-Daemon-migration"></a>

You can use either the CloudWatch agent or OpenTelemetry collector to receive traces from your instrumented applications and send them to X-Ray.

**Note**  
The CloudWatch agent version 1.300025.0 and later can collect OpenTelemetry traces. Using the CloudWatch agent instead of the X-Ray Daemon reduces the number of agents you need to manage. For more information, see [Collecting metrics, logs, and traces with the CloudWatch agent](AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html).

**Topics**
+ [Migrating on Amazon EC2 or on-premises servers](#ec2-onprem-migration)
+ [Migrating on Amazon ECS](#ecs-migration)
+ [Migrating on Elastic Beanstalk](#beanstalk-migration)

### Migrating on Amazon EC2 or on-premises servers
<a name="ec2-onprem-migration"></a>

**Important**  
Stop the X-Ray Daemon process before using the CloudWatch agent or OpenTelemetry collector to prevent port conflicts.

#### Existing X-Ray Daemon setup
<a name="xray-daemon-setup"></a>

##### Installing the daemon
<a name="install-daemon"></a>

Your existing X-Ray Daemon usage was installed using one of these methods:

Manual installation  
Download and run the executable file from the X-Ray daemon Amazon S3 bucket.

Automatic installation  
Use this script to install the daemon when launching an instance:  

```
#!/bin/bash
curl https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-3.x.rpm \
    -o /home/ec2-user/xray.rpm
yum install -y /home/ec2-user/xray.rpm
```

##### Configuring the daemon
<a name="configure-daemon"></a>

Your existing X-Ray Daemon usage was configured using either:
+ Command line arguments
+ Configuration file (`xray-daemon.yaml`)

**Example Using a configuration file**  

```
./xray -c ~/xray-daemon.yaml
```

##### Running the daemon
<a name="run-daemon"></a>

Your existing X-Ray Daemon usage was started with the following command:

```
~/xray-daemon$ ./xray -o -n us-east-1
```

##### Removing the daemon
<a name="uninstall-daemon"></a>

To remove the X-Ray Daemon from your Amazon EC2 instance:

1. Stop the daemon service:

   ```
   systemctl stop xray
   ```

1. Delete the configuration file:

   ```
   rm ~/{{path}}/{{to}}/xray-daemon.yaml
   ```

1. If configured, remove the log file:
**Note**  
The log file location depends on your configuration:  
Command line configuration: `/var/log/xray-daemon.log`
Configuration file: Check the `LogPath` setting

#### Setting up the CloudWatch agent
<a name="setup-cloudwatch-agent"></a>

##### Installing the agent
<a name="cloudwatch-installation"></a>

For installation instructions, see [Installing the CloudWatch agent on an on-premises server](AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-commandline-fleet.html#install-CloudWatch-Agent-iam_user-first).

##### Configuring the agent
<a name="cloudwatch-configuration"></a>

1. Create a configuration file to enable trace collection. For more information, see [Creating the CloudWatch agent configuration file](AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html).

1. Set up IAM permissions:
   + Attach an IAM role or specify credentials for the agent. For more information, see [Setting up IAM roles](AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-commandline-fleet.html#install-CloudWatch-Agent-iam_permissions-first).
   + Make sure the role or credentials include the `xray:PutTraceSegments` permission.

##### Starting the agent
<a name="cloudwatch-start"></a>

For instructions to start the agent, see [Starting the CloudWatch agent using the command line](AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-commandline-fleet.html#start-CloudWatch-Agent-EC2-commands-fleet).

#### Setting up the OpenTelemetry collector
<a name="setup-otel-collector"></a>

##### Installing the collector
<a name="otel-installation"></a>

Download and install the OpenTelemetry collector for your operating system. For instructions, see [Installing the collector](https://opentelemetry.io/docs/collector/installation/).

##### Configuring the collector
<a name="otel-configuration"></a>

Configure the following components in your collector:
+ awsproxy extension

  Required for X-Ray sampling
+ OTel receivers

  Collects traces from your application
+ xray exporter

  Sends traces to X-Ray

**Example Sample collector configuration — otel-collector-config.yaml**  

```
extensions:
  awsproxy:
    endpoint: 127.0.0.1:2000
  health_check:

receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 127.0.0.1:4317
      http:
        endpoint: 127.0.0.1:4318

processors:
  batch:

exporters:
  awsxray:
    region: 'us-east-1'

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [awsxray]
  extensions: [awsproxy, health_check]
```

**Important**  
Configure AWS credentials with the `xray:PutTraceSegments` permission. For more information, see [Specifying credentials](sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials).

##### Starting the collector
<a name="otel-start"></a>

Run the collector with your configuration file:

```
otelcol --config=otel-collector-config.yaml
```

### Migrating on Amazon ECS
<a name="ecs-migration"></a>

**Important**  
Your task role must have the `xray:PutTraceSegments` permission for any collector you use.  
Stop any existing X-Ray Daemon container before running the CloudWatch agent or OpenTelemetry collector container on the same host to prevent port conflicts.

#### Using the CloudWatch agent
<a name="ecs-cloudwatch"></a>

1. Get the Docker image from [Amazon ECR Public Gallery](https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent).

1. Create a configuration file named `cw-agent-otel.json`:

   ```
   {
     "traces": {
       "traces_collected": {
         "xray": {
           "tcp_proxy": {
             "bind_address": "0.0.0.0:2000"
           }
         },
         "otlp": {
           "grpc_endpoint": "0.0.0.0:4317",
           "http_endpoint": "0.0.0.0:4318"
         }
       }
     }
   }
   ```

1. Store the configuration in Systems Manager Parameter Store:

   1. Open the [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/)

   1. Choose **Create parameter**

   1. Enter the following values:
      + Name: `/ecs/cwagent/otel-config`
      + Tier: Standard
      + Type: String
      + Data type: Text
      + Value: [Paste the cw-agent-otel.json configuration here]

1. Create a task definition using bridge network mode:

   In your task definition, the configuration depends on the networking mode that you use. Bridge networking is the default and can be used in your default VPC. In a bridge network, set the `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`environment variable to tell the OpenTelemetry SDK what the endpoint and port are for the CloudWatch agent. You should also create a link from your application container to the Collector container for traces to be sent from the OpenTelemetry SDK in your application to the Collector container.   
**Example CloudWatch agent task definition**  

   ```
   {
       "containerDefinitions": [
           {
               "name": "cwagent",
               "image": "public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest",
               "portMappings": [
                   {
                       "containerPort": 4318,
                       "hostPort": 4318,
                       "protocol": "tcp"
                   },
                   {
                       "containerPort": 4317,
                       "hostPort": 4317,
                       "protocol": "tcp"
                   },
                   {
                       "containerPort": 2000,
                       "hostPort": 2000,
                       "protocol": "tcp"
                   }
               ],
               "secrets": [
                   {
                       "name": "CW_CONFIG_CONTENT",
                       "valueFrom": "/ecs/cwagent/otel-config"
                   }
               ]
           },
           {
               "name": "application",
               "image": "APPLICATION_IMAGE",
               "links": ["cwagent"],
               "environment": [
                   {
                       "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT",
                       "value": "http://cwagent:4318/v1/traces"
                   }
               ]
           }
       ]
   }
   ```

For more information, see [Deploying the CloudWatch agent to collect Amazon EC2 instance-level metrics on Amazon ECS ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-instancelevel.html).

#### Using the OpenTelemetry collector
<a name="ecs-otel"></a>

1. Get the Docker image `otel/opentelemetry-collector-contrib` from [Docker Hub](https://hub.docker.com/r/otel/opentelemetry-collector-contrib).

1. Create a configuration file called `otel-collector-config.yaml` using the same content as shown in the **Amazon EC2 configuring the collector** section, but update the endpoints to use `0.0.0.0` instead of `127.0.0.1`.

1. To use this configuration in Amazon ECS, you can store the configuration in Systems Manager Parameter Store. First, go to Systems Manager Parameter Store console, and choose **Create new parameter **. Create a new parameter with the following information:
   + Name: /ecs/otel/config (this name will be referenced in the Task Definition for the Collector)
   + Tier: Standard
   + Type: String
   + Data type: Text
   + Value: [Paste the otel-collector-config.yaml configuration here]

1. Create a task definition to deploy the OpenTelemetry collector using the bridge network mode as an example.

   In the task definition, the configuration depends on the networking mode that you use. Bridge networking is the default and can be used in your default VPC. In a bridge network, set the `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` environment variable to tell the OpenTelemetry SDK what the endpoint and port are for the OpenTelemetry Collector. You should also create a link from your application container to the Collector container for traces to be sent from the OpenTelemetry SDK in your application to the Collector container.   
**Example OpenTelemetry collector task definition**  

   ```
   {
       "containerDefinitions": [
           {
               "name": "otel-collector",
               "image": "otel/opentelemetry-collector-contrib",
               "portMappings": [
                   {
                       "containerPort": 2000,
                       "hostPort": 2000
                   },
                   {
                       "containerPort": 4317,
                       "hostPort": 4317
                   },
                   {
                       "containerPort": 4318,
                       "hostPort": 4318
                   }
               ],
               "command": [
                   "--config",
                   "env:SSM_CONFIG"
               ],
               "secrets": [
                   {
                       "name": "SSM_CONFIG",
                       "valueFrom": "/ecs/otel/config"
                   }
               ]
           },
           {
               "name": "application",
               "image": "APPLICATION_IMAGE",
               "links": ["otel-collector"],
               "environment": [
                   {
                       "name": "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT",
                       "value": "http://otel-collector:4318/v1/traces"
                   }
               ]
           }
       ]
   }
   ```

### Migrating on Elastic Beanstalk
<a name="beanstalk-migration"></a>

**Important**  
Stop the X-Ray Daemon process before using the CloudWatch agent to prevent port conflicts.

Your existing X-Ray Daemon integration was turned on by using the Elastic Beanstalk console, or by configuring X-Ray Daemon in your application source code with a configuration file.

#### Using the CloudWatch agent
<a name="beanstalk-cloudwatch"></a>

On the Amazon Linux 2 platform, configure the CloudWatch agent using an `.ebextensions` configuration file:

1. Create a directory named `.ebextensions` in your project root

1. Create a file named `cloudwatch.config` within the `.ebextensions` directory with the following content:

   ```
   files:
     "/opt/aws/amazon-cloudwatch-agent/etc/config.json":
       mode: "0644"
       owner: root
       group: root
       content: |
         {
           "traces": {
             "traces_collected": {
               "otlp": {
                 "grpc_endpoint": "12.0.0.1:4317",
                 "http_endpoint": "12.0.0.1:4318"
               }
             }
           }
         }
   container_commands:
     start_agent:
       command: /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -c file:/opt/aws/amazon-cloudwatch-agent/etc/config.json -s
   ```

1. Include the `.ebextensions` directory in your application source bundle when you deploy

For more information about Elastic Beanstalk configuration files, see [Advanced environment customization with configuration files](elasticbeanstalk/latest/dg/ebextensions.html).