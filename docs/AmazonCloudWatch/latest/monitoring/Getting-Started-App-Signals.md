# Supported instrumentation setups


 You can enable CloudWatch Application Signals with different instrumentation setups. 
 This topic describes each of the setup methods and recommendations based on the method you choose.
 


## Use AWS Distro for OpenTelemetry with the CloudWatch Agent



 The most integrated application performance monitoring(APM) experience in CloudWatch is delivered through the AWS Distro for OpenTelemetry (ADOT) SDKs and are used with the CloudWatch Agent to collect application metrics and traces. 
 This option works best if you want to get started with APM in CloudWatch quickly and also leverage out-of-the box integrations with features, such as Container Insights and CloudWatch Logs. 
 For more information, see [Enable Application Signals on Amazon EKS Clusters](CloudWatch-Application-Signals-Enable-EKS.md "CloudWatch-Application-Signals-Enable-EKS.md") and [Enable Application Signals on Amazon EC2, Amazon ECS, or Kubernates](CloudWatch-Application-Signals-Enable-Other.md "CloudWatch-Application-Signals-Enable-Other.md").
 


## Use the OpenTelemetry SDK and Collector


 
 This setup works for the following use cases:
 



1. You instrumented your application or plan with OpenTelemetry SDKs and currently are using OpenTelemetry Collector.
2. You're using languages, such as Erlang and Rust, that aren't supported by AWS Distro for OpenTelemetry (ADOT).


 For more information, see [OpenTelemetry with CloudWatch](CloudWatch-OpenTelemetry-Sections.md "CloudWatch-OpenTelemetry-Sections.md").
 


## Use the AWS X-Ray SDK and daemon



 This option is best if you instrumented your application using X-Ray SDKs and haven't migrated ADOT SDKs or OpenTelemetry SDKs.
 



 For more information, see [Transaction Search](CloudWatch-Transaction-Search.md "CloudWatch-Transaction-Search.md").
 


## Feature comparison




| Feature | ADOT SDK + CloudWatch Agent | Open Telemetry SDK + OpenTelemetry Collector | X-Ray SDKs |
| --- | --- | --- | --- |
| AWS Support | Yes | Only for data sent to AWS | Yes |
| Nonstandard language support | No | Yes | No |
| Container Insights integration | Yes | No | No |
| Out of the box logging with CloudWatch Logs | Yes | No | No |
| Out of the box runtime metrics | Yes | Yes | No |
| Always gets metrics on 100% of traffic | Yes | Only at 100% sampling rate | Only at 100% sampling rate |
