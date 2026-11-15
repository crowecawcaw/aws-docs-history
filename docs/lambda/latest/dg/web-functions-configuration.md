

# Configuring Lambda Web Functions
<a name="web-functions-configuration"></a>

You configure most Web Function settings on a revision, which is an immutable snapshot of your application code and configuration. Because a revision is immutable, changing a revision setting means creating a new revision with the updated values. You set tags and the resource-based policy on the Web Function. Its revisions and endpoints inherit its tags, and the resource-based policy controls who can act on the Web Function, its revisions, and its endpoints. Endpoint settings apply to each endpoint, including authentication type, auto-deployment mode, revision weights, scaling, and throttling. You can change these without creating a new revision. The following sections describe the settings you can configure.

## Web Function deployment package
<a name="web-functions-configuration-deployment-package"></a>

You package your Web Function code as a .zip file and store it in a versioned Amazon S3 bucket. The revision's `codeConfig` references the bucket, the key, and optionally an object version. If you omit the version, Lambda uses the latest version at creation time, so each revision points to a specific version of your package. Uploading a new package to the same key doesn't change existing revisions, and you can roll back to an earlier revision as long as its object version remains in the bucket.

The package must include your application's entry file and all of its dependencies (for example, `node_modules`). By default, Lambda loads `index.js` at the package root as the entry file and runs it to start your HTTP server. To use a different name or path (for example, `dist/index.js`), set the `AWS_LAMBDA_NODEJS_ENTRYPOINT` environment variable; see [Environment variables](#web-functions-revisions-env-vars).

For how to build and upload the package to Amazon S3 and create a revision that references it, see [Deploying Web Function code from Amazon S3](web-functions-code-s3.md) and [Creating a Lambda Web Function](web-functions-create.md).

## Instruction set architecture
<a name="web-functions-configuration-architecture"></a>

Web Functions run exclusively on the **Arm64** architecture, powered by AWS Graviton processors. Unlike Lambda Event Functions, you cannot choose the instruction set: there is no architecture setting to configure.

Each Web Function execution environment uses 2 Arm64 vCPUs. A per-Region quota limits the Arm64 vCPU capacity of your account. For the quota, see [Lambda Web Functions](gettingstarted-limits.md#web-functions-quotas). For the usage metrics that show your consumption against it, see [Regional usage and throttling metrics](web-functions-monitoring-metrics.md#web-functions-monitoring-metrics-usage).

Build native dependencies for Linux on arm64 (aarch64). Pure Node.js or JavaScript code needs no change. Any dependency with native binaries must provide a Linux arm64 build. Build the dependency on a Linux arm64 machine or in a Linux arm64 container, or cross-compile it for Linux arm64. For an example that installs dependencies in an Arm64 container, see [Testing the deployment package](web-functions-testing.md#web-functions-testing-package).

## Request timeout
<a name="web-functions-revisions-timeout"></a>

The `timeoutSeconds` setting controls the maximum time that a single HTTP request can run before Lambda terminates it. Valid values are 3–900 seconds (15 minutes). The default is 30 seconds.

Choose a timeout value based on your application's longest expected request. Setting the timeout too low causes long-running requests to fail. Setting it too high lets stuck requests run longer before Lambda terminates them.

When a non-streaming request exceeds the timeout, Lambda returns HTTP 504 with a `lambda-web-error-type` header of `Runtime.RequestTimeout`. For a streaming response, the timeout bounds the whole stream. When the timeout elapses, Lambda ends the stream, and the client receives the status code already sent, typically 200, with a truncated body and no `lambda-web-error-type` header.

## Environment variables
<a name="web-functions-revisions-env-vars"></a>

Environment variables are key-value pairs that are available to your application code at runtime. Use environment variables for non-sensitive configuration that you want to change without modifying code, such as feature flags, log levels, and resource identifiers like a database host name. For sensitive values such as API keys and database credentials, don't store them in environment variables. Instead, use Secrets Manager or AWS Systems Manager Parameter Store and retrieve the values at runtime.

Environment variables are set when you create the revision and are immutable after creation. To change an environment variable, create a new revision. In the new revision, specify every environment variable and every `serviceConfig` setting that you want to keep, not only the values that change. Settings that you omit take their default values, and environment variables that you omit aren't set.

Lambda sets the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable specifically for Web Functions. It contains the host and port that your HTTP server must listen on, in `host:port` format. Lambda sets this variable and routes requests to that address. Read it in your application code and bind exactly that host and port. You can't set this variable in a revision's environment variables. Always bind to the address in this variable, not `localhost` or a hardcoded port. The runtime waits for your server to accept a connection at this address, and initialization fails if it never does. Use a fallback address only for local runs. In a Web Function, Lambda always sets this variable.

Web Functions also receive other Lambda runtime environment variables, such as `AWS_LAMBDA_FUNCTION_MEMORY_SIZE`, `AWS_LAMBDA_METADATA_API`, and `AWS_LAMBDA_METADATA_TOKEN`. For the general list, see [Defined runtime environment variables](configuration-envvars.md#configuration-envvars-runtime). If your code or a library reads a variable from that list, confirm that Lambda sets it in a Web Function before you rely on it. Web Functions don't receive every variable in that list.

The following environment variable names are reserved for Lambda Web Functions and can't be set. If you specify one, Lambda rejects the request to create a Web Function or revision:
+ `AWS_ACCESS_KEY`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, `AWS_SECURITY_TOKEN`, and `AWS_SESSION_TOKEN`
+ `AWS_DEFAULT_REGION` and `AWS_REGION`
+ `AWS_LAMBDA_HTTP_ENDPOINT`, `AWS_LAMBDA_RUNTIME_API`, `AWS_LAMBDA_INITIALIZATION_TYPE`, and `AWS_LAMBDA_FUNCTION_MEMORY_SIZE`
+ `AWS_LAMBDA_METADATA_API` and `AWS_LAMBDA_METADATA_TOKEN`

Some frameworks read their own environment variables for the listen address instead. For example, Next.js standalone mode reads `HOSTNAME` and `PORT`. For such frameworks, use an `index.js` entry file that sets those variables from `AWS_LAMBDA_HTTP_ENDPOINT` before starting the server.

By default, the runtime loads `index.js` at the root of your deployment package as your application's entry file. The runtime does not read the entry point from `package.json`. If your entry file has a different name or path (for example, `dist/index.js`), set the `AWS_LAMBDA_NODEJS_ENTRYPOINT` environment variable to its path, relative to the root of your package.

The following example shows how to read the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable in a Node.js application:

```
// Lambda provides the address to bind in AWS_LAMBDA_HTTP_ENDPOINT ("host:port").
// The fallback applies only when running locally.
const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:3000').split(':');
app.listen(port, host, () => {
  console.log(`Server listening on ${host}:${port}`);
});
```

To set your own environment variables, add an `environmentVariables` map to the `serviceConfig` object when you create a revision, as in the following example. For the full command, see [Creating a revision](web-functions-revisions.md#web-functions-revisions-create).

```
{
  "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}",
  "environmentVariables": {
    "DATABASE_URL": "{{my-database-endpoint}}",
    "LOG_LEVEL": "info",
    "FEATURE_FLAG_NEW_UI": "true"
  }
}
```

If you specify a customer managed key, Lambda encrypts environment variables at rest with that key. For more information, see [Encryption at rest for Web Functions](web-functions-encryption.md).

## Tagging Web Functions
<a name="web-functions-configuration-tags"></a>

Tags are key-value labels that you attach to a Web Function to organize your resources and control access. Tags apply to the Web Function resource.

To add tags when you create a Web Function, use the `tags` parameter of `CreateWebFunction`. To add, remove, or list tags later, use the `TagResource`, `UntagResource`, and `ListTags` operations.

You can use tags in the following ways:
+ **Organization and search** – Group and find Web Functions by attributes such as project, environment, or team. You can find a Web Function by its tags only in its home Region. For more information, see [Replica visibility](web-functions-endpoint-replication.md#web-functions-endpoint-replication-visibility).
+ **Attribute-based access control (ABAC)** – Write AWS Identity and Access Management (IAM) policies that allow or deny actions based on tags. Use `aws:ResourceTag/${TagKey}` for actions on a Web Function and its revisions and endpoints, which inherit the tags of the Web Function. On `CreateWebFunction`, you can also use `aws:RequestTag/${TagKey}` and `aws:TagKeys`. You can't tag revisions or endpoints directly. For more information, see [Lambda Web Function permissions](web-functions-permissions.md) and [Lambda Web Function endpoint access control](web-functions-endpoint-access-control.md).

Tags have the following requirements:
+ Tag keys are 1–128 characters.
+ Tag values are 0–256 characters.
+ Keys and values can contain letters, numbers, spaces, and the characters `_ . : / = + - @`.

## Using the metadata endpoint
<a name="web-functions-configuration-metadata-endpoint"></a>

The Lambda metadata endpoint is a local HTTP API within the execution environment. It returns metadata in a simple JSON format, including the Availability Zone (AZ) ID where the environment is running. Use it to route to same-AZ resources such as Amazon ElastiCache and Amazon RDS for lower latency. You can also use it to implement AZ-aware resilience patterns.

**Note**  
A Web Function runs a persistent web server rather than a per-invocation handler. Read the metadata endpoint once at application startup and cache the value, or read it per request if you need it in request context. Don't assume a fresh per-invocation handler. For a multi-Region Web Function, the endpoint reports the AZ within the AWS Region that is serving the request.

### Getting started with the metadata endpoint
<a name="web-functions-metadata-endpoint-getting-started"></a>

Powertools for AWS Lambda provides a utility for accessing the Lambda metadata endpoint. The utility caches the response after the first call. For more information, see [Metadata](https://docs.aws.amazon.com/powertools/typescript/latest/features/metadata/) in the *Powertools for AWS Lambda (TypeScript)* documentation.

Because Web Functions run on Node.js, the following example uses the Powertools for AWS Lambda metadata utility to read the AZ ID once at server startup and cache it for the life of the process. Run the following npm command to install the Powertools package and Express:

```
npm install @aws-lambda-powertools/commons express
```

The following example uses Express for illustration. The same approach works with any Node.js web framework; see [Supported web frameworks](web-functions-runtimes.md#web-functions-runtimes-frameworks). Read the AZ ID at startup and reuse the cached value when handling requests.

**Example – Retrieving AZ ID with Powertools at startup (TypeScript)**  

```
import express from 'express';
import { getMetadata } from '@aws-lambda-powertools/commons/utils/metadata';

const app = express();

// Read the AZ ID once at startup and cache it for the life of the server.
const { AvailabilityZoneID: azId } = await getMetadata();

// Lambda provides the address to bind in AWS_LAMBDA_HTTP_ENDPOINT ("host:port").
// The fallback applies only when running locally.
const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:3000').split(':');

app.get('/', (req, res) => {
  res.json({ azId });
});

app.listen(port, host, () => {
  console.log(`Server listening on ${host}:${port}, AZ: ${azId}`);
});
```

You can also call the metadata endpoint directly. Lambda automatically sets the `AWS_LAMBDA_METADATA_API` and `AWS_LAMBDA_METADATA_TOKEN` environment variables in every execution environment, and you include the token with the Bearer scheme in the `Authorization` header. For the endpoint URL, request and response formats, and error responses, see [Using the Lambda metadata endpoint](configuration-metadata-endpoint.md).

For example, read the metadata server address from `AWS_LAMBDA_METADATA_API` and send an authenticated GET request:

```
METADATA_ENDPOINT="http://${AWS_LAMBDA_METADATA_API}/2026-01-15/metadata/execution-environment"
RESPONSE=$(curl -s -H "Authorization: Bearer ${AWS_LAMBDA_METADATA_TOKEN}" "$METADATA_ENDPOINT")
AZ_ID=$(echo "$RESPONSE" | jq -r '.AvailabilityZoneID')
```

The endpoint returns `application/json`. For example: `{"AvailabilityZoneID": "use1-az1"}`.