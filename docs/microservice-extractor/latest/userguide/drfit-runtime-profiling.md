AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Runtime profiling

The AWS Microservice Extractor for .NET tool includes an application runtime profiler to provide call count
data with dependency details in the visualization of the application. The output of the
profiler is processed by the assessment tool to create the graph. The visualization
shows class level call counts to help you understand the traffic patterns of your
application. This visual representation helps you to focus resources during the
extraction process and to isolate areas of high value. The runtime profiler is a .dll
file that must be included when you run your application in a test or integration
environment with data that is representative of the production environment. CLR
profiling is supported. For steps to run the profiler, see the [Runtime profiling
prerequisites](microservice-extractor-install.md#microservice-extractor-install-runtime-profiling "microservice-extractor-install.md#microservice-extractor-install-runtime-profiling").
