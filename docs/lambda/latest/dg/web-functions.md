

# AWS Lambda Web Functions
<a name="web-functions"></a>

With AWS Lambda Web Functions, you can run web applications and API backends as serverless HTTP servers. Your code listens on a network port and handles requests directly. You can use familiar Node.js web frameworks such as Express, Hono, or React Router with no Lambda-specific adapters or wrappers. You develop and run your server locally like any other Node.js web app.

You deploy your code as a .zip file. Lambda creates an HTTPS endpoint, manages the execution environments, and scales your application with traffic, including to zero when it's idle. To reduce latency for globally distributed users, you can deploy across multiple AWS Regions behind a single endpoint. Lambda uses latency-based routing to send each request to one of those Regions. You pay for requests, active CPU time, memory consumed over the life of each execution environment, and data transfer.

**Topics**
+ [When to use Web Functions](#web-functions-overview-use-cases)
+ [How Web Functions work](#web-functions-overview-how-it-works)
+ [Key benefits](#web-functions-overview-benefits)
+ [Core concepts](web-functions-how-it-works.md)
+ [Creating a Lambda Web Function](web-functions-create.md)
+ [Deploying Web Functions](web-functions-deploying.md)
+ [HTTP requests and responses](web-functions-http.md)
+ [Configuring networking for AWS Lambda Web Functions](web-functions-networking.md)
+ [Scaling behavior for Lambda Web Functions](web-functions-scaling.md)
+ [Execution environment lifecycle](web-functions-env-lifecycle.md)
+ [Lambda Web Function runtimes](web-functions-runtimes.md)
+ [Configuring Lambda Web Functions](web-functions-configuration.md)
+ [Lambda Web Function permissions](web-functions-permissions.md)
+ [Lambda Web Function endpoint access control](web-functions-endpoint-access-control.md)
+ [Encryption at rest for Web Functions](web-functions-encryption.md)
+ [Monitoring Lambda Web Functions](web-functions-monitoring.md)
+ [Web Function sample applications](web-functions-samples.md)
+ [Best practices for Lambda Web Functions](web-functions-best-practices.md)
+ [Testing Lambda Web Functions](web-functions-testing.md)
+ [Troubleshooting Lambda Web Functions](web-functions-troubleshooting.md)

## When to use Web Functions
<a name="web-functions-overview-use-cases"></a>

Use Web Functions for workloads that receive and respond to HTTP traffic directly. Common use cases include:
+ **Web applications** – Deploy full-stack or front-end applications that serve HTML, assets, and API routes from a single deployment.
+ **REST and GraphQL APIs** – Build API backends that serve high request volumes.
+ **Microservices** – Run HTTP services that scale independently with traffic, including to zero when idle.
+ **Server-side rendering (SSR)** – Serve pages that are rendered on the server at request time rather than pre-built. A Web Function runs your framework's production server directly. It handles SSR requests, streaming, and API routes without a separate hosting layer. It also scales with traffic. This suits applications that render personalized or frequently changing content on each request.
+ **Streaming responses** – Stream output to the client as it is produced, such as responses from a large language model.

For event-driven processing, such as handling queue messages or file uploads, use [Lambda Event Functions](lambda-functions-chapter.md#lambda-functions-use-cases) instead.

**Note**  
AWS Lambda Web Functions currently support Node.js runtimes only. If you use Java, Python, .NET, or another language, see [Create your first Lambda function](getting-started.md) for AWS Lambda Event Functions, or [AWS Lambda MicroVMs](lambda-microvms-guide.md) for Lambda MicroVMs.

## How Web Functions work
<a name="web-functions-overview-how-it-works"></a>

A Web Function contains revisions and endpoints. A revision is an immutable snapshot of your code and configuration. An endpoint routes HTTP requests to one or two revisions. Lambda runs your server in execution environments that each handle multiple concurrent requests. Lambda scales these execution environments with traffic. For details, see [Core concepts](web-functions-how-it-works.md).

## Key benefits
<a name="web-functions-overview-benefits"></a>

Web Functions provide the following benefits for web applications and API backends:
+ **Standard web development experience** – Deploy standard Node.js applications that listen on a port. You use familiar web frameworks and your normal application structure.
+ **Adaptive scaling** – Each execution environment serves multiple concurrent requests, like a standard web server. As a result, fewer execution environments handle more traffic. Existing execution environments can absorb small traffic increases, so fewer requests wait for a new execution environment to start.
+ **Usage-based billing** – You pay for requests, CPU time that your application and runtime actively consume, memory over the life of each execution environment, and data transfer. A request that waits on a database query or an external API call consumes little CPU while it waits. However, memory continues to accrue while the execution environment exists, including idle time between requests.
+ **Response streaming** – Stream responses to clients as your application produces them, without additional configuration.
+ **Scale to zero** – Lambda removes idle execution environments when there is no traffic and creates new ones when requests arrive. A request might wait while an execution environment initializes. For details about how scaling and throttling work, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).
+ **Built-in HTTPS endpoint** – Each endpoint provides an HTTPS domain with TLS. You choose IAM authentication or application-managed authentication for each endpoint. For details, see [Lambda Web Function endpoint access control](web-functions-endpoint-access-control.md). To use a custom domain or AWS WAF protection, put an Amazon CloudFront distribution in front of the endpoint.
+ **Endpoint-level traffic controls** – Set a request rate limit (requests per second) on each HTTPS endpoint, which Lambda enforces in each Region, and a maximum number of execution environments (`maxEnvironments`), also enforced in each Region. Together, these let you cap the traffic an endpoint accepts. They also let you limit how much load the endpoint passes to downstream dependencies such as databases and external APIs. For more information, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).