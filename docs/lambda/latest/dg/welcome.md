# What is AWS Lambda?

AWS Lambda is a compute service that runs code without the need to manage servers. Your code runs, scaling up and down automatically, with pay-per-use pricing.
To get started, see [Create your first function](getting-started.md "getting-started.md").

You can use Lambda for:

- **Stream processing**: Process real-time data streams for analytics and monitoring. See [Kinesis Data Streams](with-kinesis.md "with-kinesis.md") for details.
- **Web applications**: Build scalable web apps that automatically adjust to demand.
- **Mobile backends**: Create secure API backends for mobile and web applications.
- **IoT backends**: Handle web, mobile, IoT, and third-party API requests. See [IoT](services-iot.md "services-iot.md") for details.
- **File processing**: Process files automatically when uploaded to Amazon Simple Storage Service. See [file processing examples](example-apps.md#examples-apps-file "example-apps.md#examples-apps-file") for details.
- **Database operations and integration examples**: Respond to database changes and automate data workflows. See [database examples](example-apps.md#examples-apps-database "example-apps.md#examples-apps-database") for details.
- **Scheduled and periodic tasks**: Run automated operations on a regular schedule using EventBridge. See [scheduled task examples](example-apps.md#examples-apps-scheduled "example-apps.md#examples-apps-scheduled") for details.
  For pricing information, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/").

## How Lambda works

When using Lambda, you are responsible only for your code. Lambda runs your code on a high-availability compute infrastructure and manages all the computing resources,
including server and operating system maintenance, capacity provisioning, automatic scaling, and logging.

Because Lambda is a serverless,
event-driven compute service, it uses a different programming paradigm than traditional web applications. The following model illustrates how Lambda works:

1. You write and organize your code in [Lambda functions](concepts-basics.md#gettingstarted-concepts-function "concepts-basics.md#gettingstarted-concepts-function"), which are the basic building blocks you use to create a Lambda application.
2. You control security and access through [Lambda permissions](lambda-permissions.md "lambda-permissions.md"), using [execution roles](lambda-intro-execution-role.md "lambda-intro-execution-role.md") to manage what AWS services your functions can interact with and what resource policies can interact with your code.
3. Event sources and AWS services [trigger](concepts-event-driven-architectures.md "concepts-event-driven-architectures.md") your Lambda functions, passing event data in JSON format, which your functions process (this includes event source mappings).
4. [Lambda runs your code](concepts-how-lambda-runs-code.md "concepts-how-lambda-runs-code.md") with language-specific runtimes (like Node.js and Python) in execution environments that package your runtime, layers, and extensions.

###### Tip

To learn how to build **serverless solutions**, check out the [Serverless Developer Guide](../../../serverless/latest/devguide.md "../../../serverless/latest/devguide.md").

## Key features

**Configure, control, and deploy secure applications:**

- [Environment variables](configuration-envvars.md "configuration-envvars.md") modify application behavior without new code deployments.
- [Versions](configuration-versions.md "configuration-versions.md") safely test new features while maintaining stable production environments.
- [Lambda layers](chapter-layers.md "chapter-layers.md") optimize code reuse and maintenance by sharing common components across multiple functions.
- [Code signing](configuration-codesigning.md "configuration-codesigning.md") enforce security compliance by ensuring only approved code reaches production systems.

**Scale and perform reliably:**

- [Concurrency and scaling controls](lambda-concurrency.md "lambda-concurrency.md") precisely manage application responsiveness and resource utilization during traffic spikes.
- [Lambda SnapStart](snapstart.md "snapstart.md") significantly reduce cold start times. Lambda SnapStart can provide as low as sub-second startup performance, typically with no changes to your function code.
- [Response streaming](configuration-response-streaming.md "configuration-response-streaming.md") optimize function performance by delivering large payloads incrementally for real-time processing.
- [Container images](images-create.md "images-create.md") package functions with complex dependencies using container workflows.

**Connect and integrate seamlessly:**

- [VPC networks](configuration-vpc.md "configuration-vpc.md") secure sensitive resources and internal services.
- [File system](configuration-filesystem.md "configuration-filesystem.md") integration that shares persistent data and manage stateful operations across function invocations.
- [Function URLs](urls-configuration.md "urls-configuration.md") create public-facing APIs and endpoints without additional services.
- [Lambda extensions](lambda-extensions.md "lambda-extensions.md") augment functions with monitoring, security, and operational tools.

## Related information

- For information on how Lambda works, see [How Lambda works](concepts-basics.md "concepts-basics.md").
- To start using Lambda, see [Create your first Lambda function](getting-started.md "getting-started.md").
- For a list of example applications, see [Getting started with example applications and patterns](example-apps.md "example-apps.md").
