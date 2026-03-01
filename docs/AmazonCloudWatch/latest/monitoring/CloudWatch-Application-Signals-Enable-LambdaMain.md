# Enable your applications on Lambda

You can enable Application Signals for your Lambda functions. Application Signals
automatically instruments your Lambda functions using enhanced AWS Distro for OpenTelemetry
(ADOT) libraries, provided through a Lambda layer. This AWS Lambda Layer for OpenTelemetry
packages and deploys the libraries that are required for auto-instrumentation for
Application Signals.

In addition to supporting Application Signals, this Lambda layer is also a component of
Lambda OpenTelemetry support and provides tracing functionality.

You can also enhance Lambda observability by using transaction search, which enables the
capture of trace spans for Lambda function invocation without sampling. This feature allows
you to collect spans for your functions, unaffected by the `sampled` flag in trace context propagation. This ensures
that there is no additional impact to downstream dependent services. By enabling transaction search on Lambda, you gain
complete visibility into your function performance and you can troubleshoot rarely occurring issues. To get started,
see [Transaction Search](CloudWatch-Transaction-Search.md "CloudWatch-Transaction-Search.md")

###### Topics

- [Getting started](#Application-Signals-Enable-Lambda-Methods-Getting-Started "#Application-Signals-Enable-Lambda-Methods-Getting-Started")
- [Use the CloudWatch Application Signals console](#Enable-Lambda-CWConsole "#Enable-Lambda-CWConsole")
- [Use the Lambda console](#Enable-Lambda-LambdaConsole "#Enable-Lambda-LambdaConsole")
- [Enable Application Signals on Lambda using AWS CDK](#CloudWatch-Application-Signals-Lambda-CDK "#CloudWatch-Application-Signals-Lambda-CDK")
- [Enable Application Signals on Lambda using Model Context Protocol (MCP)](#CloudWatch-Application-Signals-Lambda-MCP "#CloudWatch-Application-Signals-Lambda-MCP")
- [(Optional) Monitor your application health](#CloudWatch-Application-Signals-Monitor-Lambda "#CloudWatch-Application-Signals-Monitor-Lambda")
- [Manually enable Application Signals.](#Enable-Lambda-Manually "#Enable-Lambda-Manually")
- [Manually disable Application Signals](#Disable-Lambda-Manually "#Disable-Lambda-Manually")
- [Configuring Application Signals](#Configuring-Lambda-AppSignals "#Configuring-Lambda-AppSignals")
- [AWS Lambda Layer for OpenTelemetry ARNs](#Enable-Lambda-Layers "#Enable-Lambda-Layers")
- [Deploy Lambda functions using Amazon ECR container](#containerized-lambda "#containerized-lambda")

## Getting started

There are three methods for enabling Application Signals for your Lambda
functions.

After you enable Application Signals for a Lambda function, it takes a few minutes for
telemetry from that function to appear in the Application Signals console.

- Use the CloudWatch Application Signals console
- Use the Lambda console
- Manually add the AWS Lambda Layer for OpenTelemetry to your Lambda function
  runtime.

Each of these methods adds the AWS Lambda Layer for OpenTelemetry to your
function.

## Use the CloudWatch Application Signals console

Use these steps to use the Application Signals console to enable Application Signals
for a Lambda function.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**,
   **Services**.
3. In the **Services** list area, choose **Enable
   Application Signals**.
4. Choose the **Lambda** tile.
5. Select each function that you want to enable for Application Signals, and then
   choose **Done**.

## Use the Lambda console

Use these steps to use the Lambda console to enable Application Signals for a Lambda
function.

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. In the navigation pane, choose **Functions** and then choose
   the name of the function that you want to enable.
3. Choose the **Configuration** tab, and then choose
   **Monitoring and operations tools**.
4. Choose **Edit**.
5. In the **CloudWatch Application Signals and X-Ray** section,
   select both **Automatically collect application traces and standard
   application metrics with Application Signals** and
   **Automatically collect Lambda service traces for end to end
   visibility with X-Ray.**.
6. Choose **Save**.

## Enable Application Signals on Lambda using AWS CDK

If you haven't enabled Application Signals in this account yet, you must grant
Application Signals the permissions it needs to discover your services. For more
information, see [Enable Application Signals in your account](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md").

1. Enable Application Signals for your applications

```
import { aws_applicationsignals as applicationsignals } from 'aws-cdk-lib';

const cfnDiscovery = new applicationsignals.CfnDiscovery(this,
  'ApplicationSignalsServiceRole', { }
);
```

The Discovery CloudFormation resource grants Application Signals the following
permissions:

    * `xray:GetServiceGraph`
    * `logs:StartQuery`
    * `logs:GetQueryResults`
    * `cloudwatch:GetMetricData`
    * `cloudwatch:ListMetrics`
    * `tag:GetResources`

For more information about this role, see [Service-linked role permissions for CloudWatch Application Signals](using-service-linked-roles.md#service-linked-role-signals "using-service-linked-roles.md#service-linked-role-signals"). 2. Add the IAM policy
`CloudWatchLambdaApplicationSignalsExecutionRolePolicy` to the
lambda function.

```
const fn = new Function(this, 'DemoFunction', {
    code: Code.fromAsset('$YOUR_LAMBDA.zip'),
    runtime: Runtime.PYTHON_3_12,
    handler: '$YOUR_HANDLER'
})

fn.role?.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName('CloudWatchLambdaApplicationSignalsExecutionRolePolicy'));
```

3. Replace `$AWS_LAMBDA_LAYER_FOR_OTEL_ARN` with the actual
   [AWS Lambda Layer for OpenTelemetry ARN](https://aws-otel.github.io/docs/getting-started/lambda#adot-lambda-layer-arns "https://aws-otel.github.io/docs/getting-started/lambda#adot-lambda-layer-arns") for your Region.

```
fn.addLayers(LayerVersion.fromLayerVersionArn(
    this, 'AwsLambdaLayerForOtel',
    '$AWS_LAMBDA_LAYER_FOR_OTEL_ARN'
))
fn.addEnvironment("AWS_LAMBDA_EXEC_WRAPPER", "/opt/otel-instrument");
```

## Enable Application Signals on Lambda using Model Context Protocol (MCP)

You can use the CloudWatch Application Signals Model Context Protocol (MCP) server to enable Application Signals on your Lambda functions through conversational AI interactions. This provides a natural language interface for setting up Application Signals monitoring.

The MCP server automates the enablement process by understanding your requirements and generating the appropriate configuration. Instead of manually following console steps or writing CDK code, you can simply describe what you want to enable.

### Prerequisites

Before using the MCP server to enable Application Signals, ensure you have:

- A Development Environment that supports MCP (such as Kiro, Claude Desktop, VSCode with MCP extensions, or other MCP-compatible tools)
- The CloudWatch Application Signals MCP server configured in your IDE. For detailed setup instructions, see [CloudWatch Application Signals MCP Server documentation](https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server "https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server").

### Using the MCP server

Once you have configured the CloudWatch Application Signals MCP server in your IDE, you can request enablement guidance using natural language prompts. While the coding assistant can infer context from your project structure, providing specific details in your prompts helps ensure more accurate and relevant guidance. Include information such as your Lambda function's programming language, function name, and absolute paths to your Lambda function code and infrastructure code.

**Best practice prompts (specific and complete):**

```
"Enable Application Signals for my Python Lambda function.
My function code is in /home/user/order-processor/lambda and IaC is in /home/user/order-processor/terraform"

"I want to add observability to my Node.js Lambda function 'checkout-handler'.
The function code is at /Users/dev/checkout-function and
the CDK infrastructure is at /Users/dev/checkout-function/cdk"

"Help me instrument my Java Lambda function with Application Signals.
Function directory: /opt/apps/payment-lambda
CDK infrastructure: /opt/apps/payment-lambda/cdk"
```

**Less effective prompts:**

```
"Enable monitoring for my Lambda"
→ Missing: language, paths

"Enable Application Signals. My code is in ./src and IaC is in ./infrastructure"
→ Problem: Relative paths instead of absolute paths

"Enable Application Signals for my Lambda at /home/user/myfunction"
→ Missing: programming language
```

**Quick template:**

```
"Enable Application Signals for my [LANGUAGE] Lambda function.
Function code: [ABSOLUTE_PATH_TO_FUNCTION]
IaC code: [ABSOLUTE_PATH_TO_IAC]"
```

### Benefits of using the MCP server

Using the CloudWatch Application Signals MCP server offers several advantages:

- **Natural language interface:** Describe what you want to enable without memorizing commands or configuration syntax
- **Context-aware guidance:** The MCP server understands your specific environment and provides tailored recommendations
- **Reduced errors:** Automated configuration generation minimizes manual typing errors
- **Faster setup:** Get from intention to implementation more quickly
- **Learning tool:** See the generated configurations and understand how Application Signals works

For more information about configuring and using the CloudWatch Application Signals MCP server, see the [MCP server documentation](https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server "https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server").

## (Optional) Monitor your application health

Once you have enabled your applications on Lambda, you can monitor your application
health. For more information, see [Monitor the operational health of your applications with Application Signals](Services.md "Services.md").

## Manually enable Application Signals.

Use these steps to manually enable Application Signals for a Lambda function.

1. Add the AWS Lambda Layer for OpenTelemetry to your Lambda runtime. To find
   the layer ARN for your Region, see
   [ADOT Lambda Layer ARNs](https://aws-otel.github.io/docs/getting-started/lambda#adot-lambda-layer-arns "https://aws-otel.github.io/docs/getting-started/lambda#adot-lambda-layer-arns").
2. Add the environment variable
   `AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument`

Add the environment variable
`LAMBDA_APPLICATION_SIGNALS_REMOTE_ENVIRONMENT` to configure
custom Lambda environments. By default, lambda environments are configured to
`lambda:default`. 3. Attach the AWS managed IAM policy
**CloudWatchLambdaApplicationSignalsExecutionRolePolicy**
to the Lambda execution role. 4. (Optional) We recommend that you enable Lambda active tracing to get a better
tracing experience. For more information, see [Visualize Lambda function
invocations using AWS X-Ray](../../../lambda/latest/dg/services-xray.md "../../../lambda/latest/dg/services-xray.md").

## Manually disable Application Signals

To manually disable Application Signals for a Lambda function, remove the AWS Lambda
Layer for OpenTelemetry from your Lambda runtime, and remove the
`AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument` environment
variable.

## Configuring Application Signals

You can use this section to configure Application Signals in Lambda.

**Grouping multiple Lambda functions into one service**

Environment variable `OTEL_SERVICE_NAME` sets the name of the service. This
will be displayed as the service name for your application in Application Signals
dashboards. You can assign the same service name to multiple Lambda functions, and they
will be merged into a single service in Application Signals. When you don't provide a
value for this key, the default Lambda Function name is used.

**Sampling**

By default, the trace sampling strategy is parent based. You can adjust the sampling
strategy by setting environment variables `OTEL_TRACES_SAMPLER`.

For example, set trace sampling rate to 30%.

```
OTEL_TRACES_SAMPLER=traceidratio
OTEL_TRACES_SAMPLER_ARG=0.3
```

For more information , see [OpenTelemetry Environment Variable Specification](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/ "https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/").

**Enabling all library instrumentation’s**

To reduce Lambda cold starts, by default, only AWS SDK and HTTP instrumentation’s
are enabled for Python, Node, and Java. You can set environment variables to enable
instrumentation for other libraries used in your Lambda function.

- Python – `OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=none`
- Node – `OTEL_NODE_DISABLED_INSTRUMENTATIONS=none`
- Java –
  `OTEL_INSTRUMENTATION_COMMON_DEFAULT_ENABLED=true`

## AWS Lambda Layer for OpenTelemetry ARNs

For the complete list of AWS Lambda Layer for OpenTelemetry ARNs by Region and runtime,
see [ADOT Lambda Layer ARNs](https://aws-otel.github.io/docs/getting-started/lambda#adot-lambda-layer-arns "https://aws-otel.github.io/docs/getting-started/lambda#adot-lambda-layer-arns")
in the AWS Distro for OpenTelemetry documentation. The layer is available for Python, Node.js, .NET, and
Java runtimes.

## Deploy Lambda functions using Amazon ECR container

Lambda functions deployed as container images do not support Lambda Layers in the
traditional way. When using container images, you cannot attach a layer as you would
with other Lambda deployment methods. Instead, you must manually incorporate the layer’s
contents into your container image during the build process.

Java
You can learn how to integrate the AWS Lambda Layer for OpenTelemetry
into your containerized Java Lambda function, download the
`layer.zip` artifact, and integrate it into your Java Lambda
function container to enable Application Signals monitoring.

**Prerequisites**

- AWS CLI configured with your credentials
- Docker installed
- These instructions assume you are on x86_64 platform

1. **Set Up Project Structure**

Create a directory for your Lambda function

```
mkdir java-appsignals-container-lambda && \
cd java-appsignals-container-lambda
```

Create a Maven project structure

```
mkdir -p src/main/java/com/example/java/lambda
mkdir -p src/main/resources
```

2. **Create Dockerfile**

Download and integrate the OpenTelemetry Layer with Application
Signals support directly into your Lambda container image. To do
this, the `Dockerfile` file is created.

```
FROM public.ecr.aws/lambda/java:21

# Install utilities
RUN dnf install -y unzip wget maven

# Download the OpenTelemetry Layer with AppSignals Support
RUN wget https://github.com/aws-observability/aws-otel-java-instrumentation/releases/latest/download/layer.zip -O /tmp/layer.zip

# Extract and include Lambda layer contents
RUN mkdir -p /opt && \
    unzip /tmp/layer.zip -d /opt/ && \
    chmod -R 755 /opt/ && \
    rm /tmp/layer.zip

# Copy and build function code
COPY pom.xml ${LAMBDA_TASK_ROOT}
COPY src ${LAMBDA_TASK_ROOT}/src
RUN mvn clean package -DskipTests

# Copy the JAR file to the Lambda runtime directory (from inside the container)
RUN mkdir -p ${LAMBDA_TASK_ROOT}/lib/
RUN cp ${LAMBDA_TASK_ROOT}/target/function.jar ${LAMBDA_TASK_ROOT}/lib/

# Set the handler
CMD ["com.example.java.lambda.App::handleRequest"]
```

###### Note

The `layer.zip` file contains the OpenTelemetry
instrumentation necessary for AWS Application Signals support
to monitor your Lambda function.

The layer extraction steps ensures:

    * The layer.zip contents are properly extracted to the
     `/opt/ directory`
    * The `otel-instrument` script receives
     proper execution permissions
    * The temporary layer.zip file is removed to keep the
     image size smaller

3. **Lambda function code** –
   Create a Java file for your Lambda handler at
   `src/main/java/com/example/lambda/App.java:`

Your project should look something like:

```
.
├── Dockerfile
├── pom.xml
└── src
    └── main
        ├── java
        │   └── com
        │       └── example
        │           └── java
        │               └── lambda
        │                   └── App.java
        └── resources
```

4. **Build and deploy the container
   image**

**Set up environment
variables**

```
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=$(aws configure get region)

# For fish shell users:
# set AWS_ACCOUNT_ID (aws sts get-caller-identity --query Account --output text)
# set AWS_REGION (aws configure get region)
```

**Authenticate with ECR**

First with public ECR (for base image):

```
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
```

Then with your private ECR:

```
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

**Build, tag and push your
image**

```
# Build the Docker image
docker build -t lambda-appsignals-demo .

# Tag the image
docker tag lambda-appsignals-demo:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/lambda-appsignals-demo:latest

# Push the image
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/lambda-appsignals-demo:latest
```

5. **Create and configure the Lambda
   function**

Create a new function using the Lambda console.

Select **Container image** as the deployment
option.

Choose **Browse images** to select your Amazon ECR
image. 6. **Testing and verifications – Test your
Lambda with a simple event. If the layer integration is
successful, your Lambda appears under the Application Signals
service map.**

You will see traces and metrics for your Lambda function in the
CloudWatch console.

**Troubleshooting**

If Application Signals is not working, check the following:

- Check the function logs for any errors related to the
  OpenTelemetry instrumentation
- Verify if the environment variable
  `AWS_LAMBDA_EXEC_WRAPPER` is set correctly
- Make sure the layer extraction in the Docker file completed
  successfully
- Confirm if the IAM permissions are properly attached
- If needed, increase the _Timeout and Memory_ settings in the general configuration of the Lambda
  function

.Net
You can learn how to integrate the OpenTelemetry Layer with Application
Signals support into your containerized .Net Lambda function, download the
`layer.zip` artifact, and integrate it into your .Net Lambda
function to enable Application Signals monitoring.

**Prerequisites**

- AWS CLI configured with your credentials
- Docker installed
- .Net 8 SDK
- These instructions assume you are on x86_64 platform

1. **Set Up Project Structure**

Create a directory for your Lambda function container image

```
mkdir dotnet-appsignals-container-lambda && \
cd dotnet-appsignals-container-lambda
```

2. **Create Dockerfile**

Download and integrate the OpenTelemetry Layer with Application
Signals support directly into your Lambda container image. To do
this, the `Dockerfile` file is created.

```
FROM public.ecr.aws/lambda/dotnet:8

# Install utilities
RUN dnf install -y unzip wget dotnet-sdk-8.0 which

# Add dotnet command to docker container's PATH
ENV PATH="/usr/lib64/dotnet:${PATH}"

# Download the OpenTelemetry Layer with AppSignals Support
RUN wget https://github.com/aws-observability/aws-otel-dotnet-instrumentation/releases/latest/download/layer.zip -O /tmp/layer.zip

# Extract and include Lambda layer contents
RUN mkdir -p /opt && \
    unzip /tmp/layer.zip -d /opt/ && \
    chmod -R 755 /opt/ && \
    rm /tmp/layer.zip

WORKDIR ${LAMBDA_TASK_ROOT}

# Copy the project files
COPY dotnet-lambda-function/src/dotnet-lambda-function/*.csproj ${LAMBDA_TASK_ROOT}/
COPY dotnet-lambda-function/src/dotnet-lambda-function/Function.cs ${LAMBDA_TASK_ROOT}/
COPY dotnet-lambda-function/src/dotnet-lambda-function/aws-lambda-tools-defaults.json ${LAMBDA_TASK_ROOT}/

# Install dependencies and build the application
RUN dotnet restore

# Use specific runtime identifier and disable ReadyToRun optimization
RUN dotnet publish -c Release -o out --self-contained false /p:PublishReadyToRun=false

# Copy the published files to the Lambda runtime directory
RUN cp -r out/* ${LAMBDA_TASK_ROOT}/

CMD ["dotnet-lambda-function::dotnet_lambda_function.Function::FunctionHandler"]
```

###### Note

The `layer.zip` file contains the OpenTelemetry
instrumentation necessary for AWS Application Signals support
to monitor your Lambda function.

The layer extraction steps ensures:

    * The layer.zip contents are properly extracted to the
     `/opt/ directory`
    * The `otel-instrument` script receives
     proper execution permissions
    * The temporary layer.zip file is removed to keep the
     image size smaller

3. **Lambda function code** –
   Initialize your Lambda project using the AWS Lambda .NET
   template:

```
# Install the Lambda templates if you haven't already
dotnet new -i Amazon.Lambda.Templates

# Create a new Lambda project
dotnet new lambda.EmptyFunction -n dotnet-lambda-function
```

Your project should look something like:

```
.
├── Dockerfile
└── dotnet-lambda-function
    ├── src
    │   └── dotnet-lambda-function
    │       ├── Function.cs
    │       ├── Readme.md
    │       ├── aws-lambda-tools-defaults.json
    │       └── dotnet-lambda-function.csproj
    └── test
        └── dotnet-lambda-function.Tests
            ├── FunctionTest.cs
            └── dotnet-lambda-function.Tests.csproj
```

4. **Build and deploy the container
   image**

**Set up environment
variables**

```
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=$(aws configure get region)

# For fish shell users:
# set AWS_ACCOUNT_ID (aws sts get-caller-identity --query Account --output text)
# set AWS_REGION (aws configure get region)
```

Update the `Function.cs` code to:

Update the `dotnet-lambda-function.csproj` code
to:

```
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0>/TargetFramework>
   <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <GenerateRuntimeConfigurationFiles>true</GenerateRuntimeConfigurationFiles>
    <AWSProjectType>Lambda</AWSProjectType>

    <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>

    <PublishReadyToRun>true</PublishReadyToRun>
 </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Amazon.Lambda.Core" Version="2.5.0" />
    <PackageReference Include="Amazon.Lambda.Serialization.SystemTextJson" Version="2.4.4" />
    <PackageReference Include="AWSSDK.S3" Version="3.7.305.23" />
  </ItemGroup>
</Project>
```

5. **Build and deploy the container
   image**

Set up environment variables

```
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=$(aws configure get region)

# For fish shell users:
# set AWS_ACCOUNT_ID (aws sts get-caller-identity --query Account --output text)
# set AWS_REGION (aws configure get region)
```

Authenticate with public Amazon ECR

```
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
```

Authenticate with private Amazon ECR

```
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

Create Amazon ECR repository (if needed)

```
aws ecr create-repository \
    --repository-name lambda-appsignals-demo \
    --region $AWS_REGION
```

Build, tag, and push your image

```
# Build the Docker image
docker build -t lambda-appsignals-demo .

# Tag the image
docker tag lambda-appsignals-demo:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/lambda-appsignals-demo:latest

# Push the image
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/lambda-appsignals-demo:latest

5. Create and Configure the Lambda Function


```

6. **Create and configure the Lambda
   function**

Create a new function using the Lambda console.

Select **Container image** as the deployment
option.

Choose **Browse images** to select your Amazon ECR
image. 7. **Testing and verifications – Test your
Lambda with a simple event. If the layer integration is
successful, your Lambda appears under the Application Signals
service map.**

You will see traces and metrics for your Lambda function in the
CloudWatch console.

**Troubleshooting**

If Application Signals is not working, check the following:

- Check the function logs for any errors related to the
  OpenTelemetry instrumentation
- Verify if the environment variable
  `AWS_LAMBDA_EXEC_WRAPPER` is set correctly
- Make sure the layer extraction in the Docker file completed
  successfully
- Confirm if the IAM permissions are properly attached
- If needed, increase the _Timeout and Memory_ settings in the general configuration of the Lambda
  function

Node.js
You can learn how to integrate the OpenTelemetry Layer with Application
Signals support into your containerized Node.js Lambda function, download
the `layer.zip` artifact, and integrate it into your Node.js
Lambda function to enable Application Signals monitoring.

**Prerequisites**

- AWS CLI configured with your credentials
- Docker installed
- These instructions assume you are on x86_64 platform

1. **Set Up Project Structure**

Create a directory for your Lambda function container image

```
mkdir nodejs-appsignals-container-lambda &&\
cd nodejs-appsignals-container-lambda
```

2. **Create Dockerfile**

Download and integrate the OpenTelemetry Layer with Application
Signals support directly into your Lambda container image. To do
this, the `Dockerfile` file is created.

```
# Dockerfile
FROM public.ecr.aws/lambda/nodejs:22

# Install utilities
RUN dnf install -y unzip wget

# Download the OpenTelemetry Layer with AppSignals Support
RUN wget https://github.com/aws-observability/aws-otel-js-instrumentation/releases/latest/download/layer.zip -O /tmp/layer.zip

# Extract and include Lambda layer contents
RUN mkdir -p /opt && \
    unzip /tmp/layer.zip -d /opt/ && \
    chmod -R 755 /opt/ && \
    rm /tmp/layer.zip

# Install npm dependencies
RUN npm init -y
RUN npm install

# Copy function code
COPY *.js ${LAMBDA_TASK_ROOT}/

# Set the CMD to your handler
CMD [ "index.handler" ]
```

###### Note

The `layer.zip` file contains the OpenTelemetry
instrumentation necessary for AWS Application Signals support
to monitor your Lambda function.

The layer extraction steps ensures:

    * The layer.zip contents are properly extracted to the
     `/opt/ directory`
    * The `otel-instrument` script receives
     proper execution permissions
    * The temporary layer.zip file is removed to keep the
     image size smaller

3. **Lambda function code**

Create an `index.js` file with the following
content:

```
const { S3Client, ListBucketsCommand } = require('@aws-sdk/client-s3');

// Initialize S3 client
const s3Client = new S3Client({ region: process.env.AWS_REGION });

exports.handler = async function(event, context) {
  console.log('Received event:', JSON.stringify(event, null, 2));
  console.log('Handler initializing:', exports.handler.name);

  const response = {
    statusCode: 200,
    body: {}
  };

  try {
    // List S3 buckets
    const command = new ListBucketsCommand({});
    const data = await s3Client.send(command);

    // Extract bucket names
    const bucketNames = data.Buckets.map(bucket => bucket.Name);

    response.body = {
      message: 'Successfully retrieved buckets',
      buckets: bucketNames
    };

  } catch (error) {
    console.error('Error listing buckets:', error);

    response.statusCode = 500;
    response.body = {
      message: `Error listing buckets: ${error.message}`
    };
  }

  return response;
};
```

Your project structure should look something like this:

```
.
├── Dockerfile
└── index.js
```

4. **Build and deploy the container
   image**

**Set up environment
variables**

```
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=$(aws configure get region)

# For fish shell users:
# set AWS_ACCOUNT_ID (aws sts get-caller-identity --query Account --output text)
# set AWS_REGION (aws configure get region)
```

Authenticate with public Amazon ECR

```
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
```

Authenticate with private Amazon ECR

```
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

Create Amazon ECR repository (if needed)

```
aws ecr create-repository \
    --repository-name lambda-appsignals-demo \
    --region $AWS_REGION
```

Build, tag, and push your image

```
# Build the Docker image
docker build -t lambda-appsignals-demo .

# Tag the image
docker tag lambda-appsignals-demo:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/lambda-appsignals-demo:latest

# Push the image
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/lambda-appsignals-demo:latest

5. Create and Configure the Lambda Function


```

5. **Create and configure the Lambda
   function**

Create a new function using the Lambda console.

Select **Container image** as the deployment
option.

Choose **Browse images** to select your Amazon ECR
image. 6. **Testing and verifications – Test your
Lambda with a simple event. If the layer integration is
successful, your Lambda appears under the Application Signals
service map.**

You will see traces and metrics for your Lambda function in the
CloudWatch console.

**Troubleshooting**

If Application Signals is not working, check the following:

- Check the function logs for any errors related to the
  OpenTelemetry instrumentation
- Verify if the environment variable
  `AWS_LAMBDA_EXEC_WRAPPER` is set correctly
- Make sure the layer extraction in the Docker file completed
  successfully
- Confirm if the IAM permissions are properly attached
- If needed, increase the _Timeout and Memory_ settings in the general configuration of the Lambda
  function

Python
You can learn how to integrate the OpenTelemetry Layer with Application
Signals support into your containerized Python Lambda function, download the
`layer.zip` artifact, and integrate it into your Python
Lambda function to enable Application Signals monitoring.

**Prerequisites**

- AWS CLI configured with your credentials
- Docker installed
- These instructions assume you are on x86_64 platform

1. **Set Up Project Structure**

Create a directory for your Lambda function container image

```
mkdir python-appsignals-container-lambda &&\
cd python-appsignals-container-lambda
```

2. **Create Dockerfile**

Download and integrate the OpenTelemetry Layer with Application
Signals support directly into your Lambda container image. To do
this, the `Dockerfile` file is created.

```
# Dockerfile

FROM public.ecr.aws/lambda/python:3.13

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Install unzip and wget utilities
RUN dnf install -y unzip wget

# Download the OpenTelemetry Layer with AppSignals Support
RUN wget https://github.com/aws-observability/aws-otel-python-instrumentation/releases/latest/download/layer.zip -O /tmp/layer.zip

# Extract and include Lambda layer contents
RUN mkdir -p /opt && \
    unzip /tmp/layer.zip -d /opt/ && \
    chmod -R 755 /opt/ && \
    rm /tmp/layer.zip

# Set the CMD to your handler
CMD [ "app.lambda_handler" ]
```

###### Note

The `layer.zip` file contains the OpenTelemetry
instrumentation necessary for AWS Application Signals support
to monitor your Lambda function.

The layer extraction steps ensures:

    * The layer.zip contents are properly extracted to the
     `/opt/ directory`
    * The `otel-instrument` script receives
     proper execution permissions
    * The temporary layer.zip file is removed to keep the
     image size smaller

3. **Lambda function code**

Create your Lambda function in an `app.py` file:

```
import json
import boto3

def lambda_handler(event, context):
    """
    Sample Lambda function that can be used in a container image.

    Parameters:
    -----------
    event: dict
        Input event data
    context: LambdaContext
        Lambda runtime information

    Returns:
    __
    dict
        Response object
    """
    print("Received event:", json.dumps(event, indent=2))

    # Create S3 client
    s3 = boto3.client('s3')

    try:
        # List buckets
        response = s3.list_buckets()

        # Extract bucket names
        buckets = [bucket['Name'] for bucket in response['Buckets']]

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Successfully retrieved buckets',
                'buckets': buckets
            })
        }
    except Exception as e:
        print(f"Error listing buckets: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error listing buckets: {str(e)}'
            })
        }
```

Your project structure should look something like this:

```
.
├── Dockerfile
├── app.py
└── instructions.md
```

4. **Build and deploy the container
   image**

**Set up environment
variables**

```
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=$(aws configure get region)

# For fish shell users:
# set AWS_ACCOUNT_ID (aws sts get-caller-identity --query Account --output text)
# set AWS_REGION (aws configure get region)
```

Authenticate with public Amazon ECR

```
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
```

Authenticate with private Amazon ECR

```
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

Create Amazon ECR repository (if needed)

```
aws ecr create-repository \
    --repository-name lambda-appsignals-demo \
    --region $AWS_REGION
```

Build, tag, and push your image

```
# Build the Docker image
docker build -t lambda-appsignals-demo .

# Tag the image
docker tag lambda-appsignals-demo:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/lambda-appsignals-demo:latest

# Push the image
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/lambda-appsignals-demo:latest

5. Create and Configure the Lambda Function


```

5. **Create and configure the Lambda
   function**

Create a new function using the Lambda console.

Select **Container image** as the deployment
option.

Choose **Browse images** to select your Amazon ECR
image. 6. **Testing and verifications – Test your
Lambda with a simple event. If the layer integration is
successful, your Lambda appears under the Application Signals
service map.**

You will see traces and metrics for your Lambda function in the
CloudWatch console.

**Troubleshooting**

If Application Signals is not working, check the following:

- Check the function logs for any errors related to the
  OpenTelemetry instrumentation
- Verify if the environment variable
  `AWS_LAMBDA_EXEC_WRAPPER` is set correctly
- Make sure the layer extraction in the Docker file completed
  successfully
- Confirm if the IAM permissions are properly attached
- If needed, increase the _Timeout and Memory_ settings in the general configuration of the Lambda
  function
