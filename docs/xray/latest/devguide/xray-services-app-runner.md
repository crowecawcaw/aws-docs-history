# AWS App Runner and X-Ray

AWS App Runner is an AWS service that provides a fast, simple, and cost-effective way to deploy from source code
or a container image directly to a scalable and secure web application in the AWS Cloud. You don't need to
learn new technologies, decide which compute service to use, or know how to provision and configure AWS resources.
See [What is AWS App Runner](../../../apprunner/latest/dg/what-is-apprunner.md "../../../apprunner/latest/dg/what-is-apprunner.md") for more information.

AWS App Runner sends traces to X-Ray by integrating with the [AWS Distro for OpenTelemetry](xray-services-adot.md "xray-services-adot.md") (ADOT).
Use ADOT SDKs to collect trace data for your containerized applications, and use X-Ray to analyze and gain insights into your instrumented application.
For more information, see [Tracing for your App Runner application with X-Ray](../../../apprunner/latest/dg/monitor-xray.md "../../../apprunner/latest/dg/monitor-xray.md").
