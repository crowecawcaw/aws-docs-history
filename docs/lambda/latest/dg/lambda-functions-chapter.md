

# AWS Lambda Event Functions (formerly Lambda functions)
<a name="lambda-functions-chapter"></a>

**Tip**  
Join Serverless experts for free hands-on workshops to learn how to build Serverless applications with best practices. [Sign up for free serverless workshops](https://aws-experience.com/amer/smb/events/series/Get-Hands-On-With-Serverless?trk=188abe3e-9f94-4e84-aefb-398d944ad567%26sc_channel%3del) on the AWS Experience website.

AWS Lambda Event Functions, formerly called Lambda functions, run your code in response to events from sources such as Amazon Simple Storage Service (Amazon S3), Amazon Simple Queue Service (Amazon SQS), and EventBridge, without the need to manage servers. A function receives an event, runs your handler, and returns a response. Functions scale up and down automatically with pay-per-use pricing. To get started, see [Create your first function](getting-started.md). For information about [best practices](best-practices.md), [programming languages](lambda-programming-languages.md), [tenant isolation](tenant-isolation.md), and [tools for development and deployment](tools-to-develop-deploy-manage.md), see the related topics below.

**Note**  
**Event Functions** is the name for the original Lambda function type, and the Lambda console labels it **Event function**. The underlying resource is unchanged: the API operations (such as `CreateFunction` and `Invoke`), the AWS SDKs, the AWS CLI, and the `AWS::Lambda::Function` resource type still use *function*, so you don't need to change any code or configuration.

For pricing information, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

## When to use Event Functions
<a name="lambda-functions-use-cases"></a>

You can use Event Functions for:
+ **File processing**: Process files automatically when uploaded to Amazon Simple Storage Service. See [file processing examples](example-apps.md#examples-apps-file) for details.
+ **Long-running workflows**: Build stateful, multi-step workflows that can run for up to one year. See [durable Lambda functions](durable-functions.md) for details.
+ **Database operations and integration examples**: Respond to database changes and automate data workflows. See [database examples](example-apps.md#examples-apps-database) for details.
+ **Scheduled and periodic tasks**: Run automated operations on a regular schedule using EventBridge. See [scheduled task examples](example-apps.md#examples-apps-scheduled) for details.
+ **Stream processing**: Process real-time data streams for analytics and monitoring. See [Kinesis Data Streams](with-kinesis.md) for details.
+ **Web applications**: Handle web and API requests through Amazon API Gateway, Application Load Balancer, or [Lambda function URLs](urls-configuration.md). By default, each execution environment handles one request at a time. On Lambda Managed Instances, an execution environment handles multiple requests concurrently.
+ **Mobile backends**: Create secure API backends for mobile and web applications.
+ **IoT backends**: Handle web, mobile, IoT, and third-party API requests. See [IoT](services-iot.md) for details.

To serve HTTP traffic directly from a standard web server, use Lambda Web Functions. For more information, see [AWS Lambda Web Functions](web-functions.md).

## Event Functions and durable functions
<a name="whatis-function-types"></a>

[Lambda functions](#lambda-functions-chapter) run for up to 15 minutes per invocation by default and are ideal for event-driven tasks like processing API requests, handling file uploads, or responding to database changes. On Lambda Managed Instances, functions can run for up to 90 minutes for asynchronous and event source mapping (ESM) invocations. [Durable functions](durable-functions.md) extend this model for workloads that need to run longer and survive interruptions. They automatically checkpoint their progress so they resume reliably after failures, and they can run for up to one year when invoked asynchronously. Use durable functions when you need multi-step workflows, human-in-the-loop approvals, or coordination across services over extended periods.

## How Lambda works
<a name="how-lambda-works"></a>

When using Lambda, you are responsible only for your code. Lambda runs your code on a high-availability compute infrastructure and manages all the computing resources, including server and operating system maintenance, capacity provisioning, automatic scaling, and logging.

Because Lambda is a serverless, event-driven compute service, it uses a different programming approach than traditional web applications. The following model illustrates how Lambda works:

1. You write and organize your code in [Lambda functions](concepts-basics.md#gettingstarted-concepts-function), which are the basic building blocks you use to create a Lambda application.

1. You control security and access through [Lambda permissions](lambda-permissions.md), using [execution roles](lambda-intro-execution-role.md) to manage what AWS services your functions can interact with and what resource policies can interact with your code.

1. Event sources and AWS services [trigger](concepts-event-driven-architectures.md) your Lambda functions, passing event data in JSON format, which your functions process (this includes event source mappings).

1. [Lambda runs your code](concepts-how-lambda-runs-code.md) with language-specific runtimes (like Node.js and Python) in execution environments that package your runtime, layers, and extensions.

**Tip**  
To learn how to build **serverless solutions**, check out the [Serverless Developer Guide](https://docs.aws.amazon.com/serverless/latest/devguide/).

## Key features
<a name="features"></a>

**Configure, control, and deploy secure applications:**
+ [Environment variables](configuration-envvars.md) modify application behavior without new code deployments.
+ [Versions](configuration-versions.md) safely test new features while maintaining stable production environments.
+ [Layers](chapter-layers.md) optimize code reuse and maintenance by sharing common components across multiple functions.
+ [Code signing](configuration-codesigning.md) enforce security compliance by ensuring only approved code reaches production systems.

**Scale and perform reliably:**
+ [Concurrency and scaling controls](lambda-concurrency.md) precisely manage application responsiveness and resource utilization during traffic spikes.
+ [SnapStart](snapstart.md) significantly reduce cold start times. Lambda SnapStart can provide as low as sub-second startup performance, typically with no changes to your Event Function code.
+ [Response streaming](configuration-response-streaming.md) optimize function performance by delivering large payloads incrementally for real-time processing.
+ [Container images](images-create.md) package functions with complex dependencies using container workflows.

**Connect and integrate seamlessly:**
+ [VPC networks](configuration-vpc.md) secure sensitive resources and internal services.
+ [File systems](configuration-filesystem.md) integration that shares persistent data and manage stateful operations across function invocations.
+ [Function URLs](urls-configuration.md) create public-facing APIs and endpoints without additional services.
+ [Extensions](lambda-extensions.md) augment functions with monitoring, security, and operational tools.

## Related information
<a name="what-is-lambda-moreinfo"></a>
+ For information on how Lambda works, see [How Lambda works](concepts-basics.md).
+ To start using Lambda, see [Create your first Lambda function](getting-started.md).
+ For a list of example applications, see [Getting started with example applications and patterns](example-apps.md).