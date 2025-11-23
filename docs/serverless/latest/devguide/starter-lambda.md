# Get started with Lambda

All projects need a compute capability to handle processing tasks. Here are some examples:

- Handling web application and API requests
- Transforming batches of data
- Processing messages from a queue
- Resizing images
- Generating dynamic PDFs from customer data
  In traditional applications, you write code to do these tasks. You organize that code into **functions**. You put the function code inside an application framework. Whichever framework you picked will run inside a language dependent runtime environment. Finally, that runtime environment will be hosted on a virtual or physical server.

Setting up, configuring and maintaining the frameworks, runtime environments, and virtual or physical infrastructure slows down your delivery of features, bug fixes, and improvements.

## What is Lambda?

In Lambda, you write function code. Lambda runs the functions. That’s it. There are no servers.

![Image of Werner Vogels on stage in front of a banner.](images/s_lambda/werner-no-server.jpg)

_“No Server Is Easier To Manage Than No Server”_ - Werner Vogels, VP and CTO

The Lambda service runs instances of your function only when needed and scales automatically from zero requests per day to thousands per second. You pay only for the compute time that’s actually used — there is no charge when your code is not running.

## Fundamentals

Serverless solutions are based on _event-driven architecture,_ or EDA,
where services send and receive _events_, which represent an update or
change in state. The primary activity of Lambda functions is to process events.

Within the Lambda service, your function code is stored in a code package, deployed as a .zip or a container image. All interaction with the code occurs through the Lambda API. There is no direct invocation of functions from outside of the Lambda service.

![Diagram showing the Amazon Web Services Cloud as a box, with AWS Lambda service inside it within a grey box. Event text connects with an arrow to the Lambda API inside a blue box in the AWS Lambda service. The Lambda API connects with an arrow to a Lambda function icon labeled with the text: function code.](images/s_lambda/lambda-arch-overview.png)

What you will learn on your journey to building applications with Lambda:

- How the event-driven programming model invokes Lambda functions
- How to create, invoke, test, update, package, and secure functions
- How the execution and runtime environment runs your functions
- How to view logs and monitor your functions
- Where to find hands-on opportunities to learn how to invoke functions

![Image of learning path. Described in detail in the following text.](images/s_lambda/path-lambda-fun.png)

### Fundamentals -

conceptual and practical paths

The following is a text representation of the key concepts in the preceding
diagram.

The Lambda learning path forks into two paths. The conceptual path focuses on the programming model, runtime environment, and security concepts. The other path includes practical steps to build a application while introducing development workflow activities such as how to create and deploy functions, invoke and test, update and package, and monitor the logs and troubleshoot errors.

**Programming Model**

- Event plus Context and Environment variables (ENV) are inputs to a Handler function
- ENV variables
- Runtime environment

**Create & Deploy**

- Management Console
- Infrastructure as Code (IaC) - CloudFormation (CFN), AWS SAM (SAM), AWS Cloud Development Kit (AWS CDK)
- [Deploy .zip file archives](../../../lambda/latest/dg/nodejs-package.md "../../../lambda/latest/dg/nodejs-package.md") — when you need additional libraries, or compiled languages.
- [Versions](../../../lambda/latest/dg/configuration-versions.md "../../../lambda/latest/dg/configuration-versions.md") - by publishing a version of your function, you can store your code and configuration as separate stable resources

**Invoke/Test**

- Synchronous invocation
- Testing locally and in the cloud with the help of AWS SAM templates and AWS SAM CLI

**Update / Package**

- Updating code and dependencies
- Packaging with the help of AWS SAM templates and AWS SAM CLI

**Monitor**

- Logs in CloudWatch
- Errors and tracing in X-Ray
- Metrics

**Secure**

- Execution role
- Policies that grant least privilege to your functions

**Workshop - Intro to Serverless** - Before diving too deep,
you can choose to try out serverless in a workshop or tutorial. Connect to a data source and
create a REST API with your first Lambda function.”

- Services used: AWS Management Console, Lambda, DynamoDB, API Gateway

### Programming Model

The Lambda service provides the same event-based programming model for all languages. The Lambda runtime passes an _invocation event_ and _context_ to your Lambda function _handler_ which does some work and produces a resulting event:

![MISSING](images/s_lambda/lambda-programming-model.png)

The _invocation event_ contains data, as a JSON packet, which varies from service to service. For example, API gateway events include path, HTTP method, query string parameters, headers, cookies, and more. DynamoDB events could contain updated or delete record data. S3 events include the bucket name and object key, among other things.

_The context_ contains information about the environment the function is running inside. Additional contextual information can be set in familiar environment variables (ENV).

The function _handler_ is a method in your function code that processes the inbound event. The handler, which is a standard function in your language of choice, does some work and emits a _result event_.

After the handler finishes processing the first event, the runtime sends it another, and another. Each instance of your function could process thousands of requests.

Unlike traditional servers, Lambda functions do not run constantly. When a function is triggered by an event, this is called an _invocation_. Lambda functions are limited to 15 minutes in duration, but on average, across all AWS customers, most invocations last for less than a second.

There are many types of invocation events. Some examples:

- HTTP request from API Gateway
- Schedule managed by an EventBridge rule
- Message from an IOT device
- Notification that a file was uploaded to an S3 bucket

Even the smallest Lambda-based application uses at least one event that invokes your function.

### How Lambda invokes your function (runtime environment)

Lambda invokes your function in an _execution environment_, which contains a secure and isolated _runtime environment_.

- A _runtime_ provides a language-specific environment which relays invocation events, context information, and responses between the Lambda and your functions.
- An _execution environment_ manages the processes and resources that are required to run the function.

![Runtime environment diagram. Lambda service box on left, Execution Environment box on right with dotted line surrounding a box for API Endpoints and a box for Processes. Lambda service is connected through three connection points to three API endpoints: Runtime API, Extensions API, and Telemetry API. These APIs are connected into the Process block. Runtime API connects to a Runtime + Function block. Extensions API and Telemetry API connect to an Extension.](images/s_lambda/telemetry-api-concept-diagram.png)

You can use runtimes that Lambda provides for JavaScript (Node.js), TypeScript, Python, Java, Go, C#, and PowerShell, or you can build your own custom runtime environment inside of a container.

If you package your code as a .zip file archive, you must configure your function to use a runtime that matches your programming language. For a container image, you include the runtime when you build the image.

### How to process events with a Lambda handler

Conceptually, there are only three steps to processing events with Lambda:

1. Configure the entry point to your function, known as the _handler_, and deploy the function.
2. Lambda service initializes the function, then it invokes the
   _handler_ with an invocation event and context.
3. Your handler function processes the event and returns a response event.

Subsequent events will invoke the handler again, without the initialization delay.
During this cycle, the function stays in memory, so clients and variables declared outside
of the handler method can be reused.

After a period of time, Lambda will eventually tear down the runtime. This can happen for a variety of reasons; some examples: scaling down to conserve resources, updating the function, updating the runtime.

The function **handler** is the essential component of your function code. As noted previously, the handler is the entry point, but it may not be the only function in your code. In fact, a best practice is keeping the handler sparse and doing the actual processing in other functions in your code.

Here are some example **handlers**:

Python

```
# Example handler method in Python
def lambda_handler(event, context):
  message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
  return {
       'message' : message
      }
```

Node.js

```
# Example handler method for Node.js
exports.handler =  async function(event, context) {
  console.log("EVENT: \n" + JSON.stringify(event, null, 2))
  return context.logStreamName
  }
```

Java

```
# Example handler method in Java
package example;
import com.amazonaws.services.lambda.runtime.Context
import com.amazonaws.services.lambda.runtime.RequestHandler
import com.amazonaws.services.lambda.runtime.LambdaLogger

// Handler value: example.Handler
public class Handler implements RequestHandler<Map<String,String>, String>{
  Gson gson = new GsonBuilder().setPrettyPrinting().create();

  @Override
  public String handleRequest(Map<String,String> event, Context context)
  {
    LambdaLogger logger = context.getLogger();
    String response = new String("200 OK");
    logger.log("EVENT: " + gson.toJson(event));
    return response;
  }
}
```

C#

```
// Example handler method in C#
using Amazon.Lambda.Core;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace HelloWorld;

public class Function
{
    public string FunctionHandler(string input, ILambdaContext context)
    {
        context.Logger.LogLine($"Transforming {input} to upper case");

        return input.ToUpper();
    }
}
```

Handlers in interpreted languages can be deployed directly through the web-based AWS Management Console. Compiled languages, such as Java and C#, or functions that use external libraries are deployed using .zip file archives or container images. Because of that additional process, this guide will focus on Python for examples.

Regardless of language, Lambda functions will generally return a _response event_ on successful completion. The following program listing is an example response event to send back to API Gateway so that it can handle a request:

```
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
   },
    "isBase64Encoded": false,
    "multiValueHeaders": {
      "X-Custom-Header": ["My value", "My other value"],
    },
  "body": "{\n  \"TotalCodeSize\": 104330022,\n  \"FunctionCount\": 26\n}"
}
```

### How to write logs with serverless applications

You might have noticed the logging statements in the preceding handler code. Where do those log messages go?

During invocation, the Lambda runtime automatically captures function output to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/").

In addition to logging your function's output, the runtime also logs entries when function invocation starts and ends. This includes a report log with the request ID, billed duration, initialization duration, and other details. If your function throws an error, the runtime returns that error to the invoker.

To help simplify troubleshooting, the [AWS Serverless Application Model CLI](../../../serverless-application-model/latest/developerguide/serverless-sam-reference.md#serverless-sam-cli "../../../serverless-application-model/latest/developerguide/serverless-sam-reference.md#serverless-sam-cli") (AWS SAM CLI) has a command called [sam logs](../../../serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-logs.md "../../../serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-logs.md") which will show you CloudWatch Logs generated by your Lambda function.

For example, the following terminal command would show the live tail of logs generated by the _YourLambdaFunctionName_ Lambda function:

```
sam logs -n YourLambdaFunctionName --tail
```

Logging and debugging go hand in hand. Traces of events are available with Amazon X-Ray for debugging.

### Securing functions

[AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM) is the service used to manage access to AWS services. Lambda is fully integrated with IAM, allowing you to control precisely what each Lambda function can do within the AWS Cloud. There are two important things that define the scope of permissions in Lambda functions:

- _resource policy_: Defines which events are authorized to invoke the function.
- _execution role policy_: Limits what the Lambda function is authorized to do.

![Workflow diagram showing progress from event source to Lambda function, with a Resource-based policy, then Lambda to Other AWS resources, with an Execution role policy.](images/s_lambda/lambda-security-flow.png)

Using IAM roles to describe a Lambda function’s permissions, decouples security
configuration from the code. This helps reduce the complexity of a lambda function, making
it easier to maintain.

A Lambda function’s resource and execution policy should be granted the minimum required permissions for the function to perform it’s task effectively. This is sometimes referred to as the rule of least privilege. As you develop a Lambda function, you expand the scope of this policy to allow access to other resources as required.

## Advanced Topics

You can do a lot by just creating a function and connecting it to an event source like API Gateway or S3 triggers.

As you progress on your journey, you should explore the following more advanced topics.

- Connect services with event source mapping
- Deploy code in containers
- Add additional code with layers
- Augment functions with extensions
- Launch functions faster with SnapStart
- Connect to functions with Function URLs

### Event source mapping

Some services can trigger Lambda functions directly, for example, when an image is added to an S3 bucket, a Lambda can be triggered to resize it. Some services cannot invoke Lambda directly; but you can instead use an _event source mapping_ which is a polling mechanism that reads from an event source and invokes a Lambda function.

You can use event source mappings to process items from a stream or queue in the following services:

- [Amazon DynamoDB](../../../lambda/latest/dg/with-ddb.md "../../../lambda/latest/dg/with-ddb.md")
- [Amazon Kinesis](../../../lambda/latest/dg/with-kinesis.md "../../../lambda/latest/dg/with-kinesis.md")
- [Amazon MQ](../../../lambda/latest/dg/with-mq.md "../../../lambda/latest/dg/with-mq.md")
- [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](../../../lambda/latest/dg/with-msk.md "../../../lambda/latest/dg/with-msk.md")
- [Self-managed Apache Kafka](../../../lambda/latest/dg/with-kafka.md "../../../lambda/latest/dg/with-kafka.md")
- [Amazon Simple Queue Service](../../../lambda/latest/dg/with-sqs.md "../../../lambda/latest/dg/with-sqs.md")

Related resource:

- [Event source mapping](../../../lambda/latest/dg/invocation-eventsourcemapping.md "../../../lambda/latest/dg/invocation-eventsourcemapping.md") official documentation, including the default behavior that batches records together into a single payload that Lambda sends to your function.

### Deploy with containers

If you need a custom runtime that is not provided by AWS, you can create and deploy a custom container image. AWS provides base images preloaded with a language runtime and other components that are required to run the image on Lambda. AWS provides a Dockerfile for each of the base images to help with building your container image.

Custom containers are one way you might experiment with lift and shift of existing code to Lambda runtimes. If you do this, consider the architectural differences between always running containers, versus on demand nature of Lambda functions.

Related resource:

- [Deploy container images](../../../lambda/latest/dg/nodejs-image.md "../../../lambda/latest/dg/nodejs-image.md")

### Add code with Layers

A Lambda _layer_ is a .zip file archive that can contain additional code or other content. A layer can contain libraries, a [custom runtime](../../../lambda/latest/dg/runtimes-custom.md "../../../lambda/latest/dg/runtimes-custom.md"), data, or configuration files. Layers are also necessary if your function .zip archive exceeds the size limit.

Layers provide a convenient way to package libraries and other dependencies that you can use with your Lambda functions. Using layers reduces the size of uploaded deployment archives and makes it faster to deploy your code. Layers also promote code sharing and separation of responsibilities so that you can iterate faster on writing business logic.

Related resource:

- [Creating and sharing Lambda layers](../../../lambda/latest/dg/configuration-layers.md "../../../lambda/latest/dg/configuration-layers.md")

### Extensions

You can use Lambda extensions to augment your Lambda functions. For example, use Lambda Extensions to integrate with your preferred monitoring, observability, security, and governance tools.

Lambda supports internal or external extensions. An internal extension runs as part of the runtime process. An external extension runs as an independent process in the execution environment and continues to run after the function invocation is fully processed.

Related resources:

- [Datadog Lambda Extension](https://docs.datadoghq.com/serverless/libraries_integrations/extension/ "https://docs.datadoghq.com/serverless/libraries_integrations/extension/") - an extension that supports submitting custom metrics, traces, and logs asynchronously while your Lambda function executes.
- [Lambda Extensions - official documentation](../../../lambda/latest/dg/lambda-extensions.md "../../../lambda/latest/dg/lambda-extensions.md")

### Launch functions faster with SnapStart

Lambda SnapStart for Java can improve startup performance by up to 10x at no extra cost, typically with no changes to your function code. The largest contributor to startup latency (often referred to as cold start time) is the time that Lambda spends initializing the function, which includes loading the function's code, starting the runtime, and initializing the function code.

![Lambda logo with checkmark and performance meter indicating optimization.](images/s_lambda/snapstart-logo.png)

With SnapStart, Lambda initializes your function when you publish a function version. Lambda takes a [Firecracker microVM](http://aws.amazon.com/blogs/opensource/firecracker-open-source-secure-fast-microvm-serverless/ "http://aws.amazon.com/blogs/opensource/firecracker-open-source-secure-fast-microvm-serverless/") snapshot of the memory and disk state of the initialized [execution environment](../../../lambda/latest/dg/lambda-runtime-environment.md "../../../lambda/latest/dg/lambda-runtime-environment.md"), encrypts the snapshot, and caches it for low-latency access.

Note: You can use SnapStart only on published function versions and aliases that point to versions. You can't use SnapStart on a function's unpublished version ($LATEST).

Related resources:

- [Accelerate Your Lambda Functions with Lambda SnapStart](https://aws.amazon.com/blogs/aws/new-accelerate-your-lambda-functions-with-lambda-snapstart/ "https://aws.amazon.com/blogs/aws/new-accelerate-your-lambda-functions-with-lambda-snapstart/") - an AWS Compute blog
  article by Jeff Barr from Nov 2022 that shows the configuration change and vast
  difference from roughly six seconds init time to 142 milliseconds of restore time with
  SnapStart

### Connect to functions with Function URLs

A function URL is a dedicated HTTP(S) endpoint for your Lambda function. You can create and configure a function URL through the Lambda console or the Lambda API. When you create a function URL, Lambda automatically generates a unique URL endpoint for you. Once you create a function URL, its URL endpoint never changes. Function URL endpoints have the following format:

```
https://<url-id>.lambda-url.<region>.on.aws
```

After you configure a function URL for your function, you can invoke your function through its HTTP(S) endpoint with a web browser, curl, Postman, or any HTTP client.

Related resources:

- [Function URLs](../../../lambda/latest/dg/lambda-urls.md "../../../lambda/latest/dg/lambda-urls.md") - official documentation

## Additional resources

Official AWS documentation:

- [AWS Lambda Developer Guide](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") - extensive and complete documentation for Lambda

## Next steps

###### Learn serverless techniques in an online workshop

Learn by doing in the **[Serverless Patterns Workshop](https://catalog.workshops.aws/serverless-patterns "https://catalog.workshops.aws/serverless-patterns")**. The first module introduces a serverless microservice to retrieve data from DynamoDB with Lambda and API Gateway. Additional modules provide practical examples of unit and integration testing, using infrastructure as code to deploy resources, and how to build common architectural patterns used in serverless solutions.

![Architecture diagram for a REST microservice. Client icon connects through an arrow to REST API resource icon with API Gateway service icon placed above it. REST API is connected by a double arrow to Lambda function resource icon with Permissions Policy resource icon placed above it, and Lambda service icon placed above both. Lambda function resource is connected through an arrow pointing to Users Table resource with DynamoDB service icon placed above it. Dotted boxes enclose each of the services.](images/workshop-m1-infra-complete.png)
