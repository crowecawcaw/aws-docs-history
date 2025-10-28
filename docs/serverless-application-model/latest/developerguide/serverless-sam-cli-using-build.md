# Default build with AWS SAM

To build your serverless application, use the `sam build` command. This command also
gathers the build artifacts of your application's dependencies and places them in the proper
format and location for next steps, such as locally testing, packaging, and deploying.

You specify your application's dependencies in a manifest file, such as
`requirements.txt` (Python) or `package.json` (Node.js),
or by using the `Layers` property of a function resource. The `Layers`
property contains a list of [AWS Lambda layer](../../../lambda/latest/dg/configuration-layers.md "../../../lambda/latest/dg/configuration-layers.md") resources that the
Lambda function depends on.

The format of your application's build artifacts depends on each function's
`PackageType` property. The options for this property are:

- **`Zip`** – A .zip file archive, which
  contains your application code and its dependencies. If you package your code as a .zip file
  archive, you must specify a Lambda runtime for your function.
- **`Image`** – A container image, which
  includes the base operating system, runtime, and extensions, in addition to your application
  code and its dependencies.
  For more information about Lambda package types, see [Lambda deployment packages](../../../lambda/latest/dg/gettingstarted-package.md "../../../lambda/latest/dg/gettingstarted-package.md") in the
  _AWS Lambda Developer Guide_.

###### Topics

- [Building a .zip file archive](#build-zip-archive "#build-zip-archive")
- [Building a container image](#build-container-image "#build-container-image")
- [Container environment
  variable file](#serverless-sam-cli-using-container-environment-file "#serverless-sam-cli-using-container-environment-file")
- [Speed up build times by building your project in the source folder](#serverless-sam-cli-using-build-in-source "#serverless-sam-cli-using-build-in-source")
- [Examples](#building-applications-examples "#building-applications-examples")
- [Building functions outside of AWS SAM](#building-applications-skip "#building-applications-skip")

## Building a .zip file archive

To build your serverless application as a .zip file archive, declare `PackageType:
 Zip` for your serverless function.

AWS SAM builds your application for the [architecture](sam-resource-function.md#sam-function-architectures "sam-resource-function.md#sam-function-architectures") that you specify. If you don't specify an architecture, AWS SAM uses
`x86_64` by default.

If your Lambda function depends on packages that have natively compiled programs, use the
`--use-container` flag. This flag locally compiles your functions in a
container that behaves like a Lambda environment, so they're in the right format when you
deploy them to the AWS Cloud.

When you use the `--use-container` option, by default AWS SAM pulls the container
image from [Amazon ECR Public](../../../AmazonECR/latest/public/what-is-ecr.md "../../../AmazonECR/latest/public/what-is-ecr.md"). If you would like to pull a container image from another repository or
for a specific version of AWS SAM CLI, you can use the `--build-image` option and provide the URI
of an alternate container image. Following are two example commands for building applications
using container images from a specific version of AWS SAM CLI:

```
# Build a Node.js 20 application using a container image for a specific version of AWS SAM CLI (1.136.0)
sam build --use-container --build-image public.ecr.aws/sam/build-nodejs22.x:1.136.0

# Build a function resource using the Python 3.13 container image from a specific version of AWS SAM CLI (1.136.0)(
sam build --use-container --build-image Function1=public.ecr.aws/sam/build-python3.13:1.136.0
```

For additional examples of building a .zip file archive application, see the Examples
section later in this topic.

## Building a container image

To build your serverless application as a container image, declare `PackageType:
 Image` for your serverless function. You must also declare the `Metadata`
resource attribute with the following entries:

`Dockerfile`

The name of the Dockerfile associated with the Lambda function.

`DockerContext`

The location of the Dockerfile.

`DockerTag`

(Optional) A tag to apply to the built image.

`DockerBuildArgs`

Build arguments for the build.

###### Important

The AWS SAM CLI doesn't redact or obfuscate any information you include in `DockerBuildArgs` arguments. We strongly recommend you don't use this section to store sensitive information, such as passwords or secrets.

The following is an example `Metadata` resource attribute section:

```
    Metadata:
      Dockerfile: Dockerfile
      DockerContext: ./hello_world
      DockerTag: v1
```

To download a sample application that's configured with the `Image` package
type, see [Tutorial: Deploy a Hello World application with AWS SAM](serverless-getting-started-hello-world.md "serverless-getting-started-hello-world.md"). At the prompt asking which
package type you want to install, choose `Image`.

###### Note

If you specify a multi-architecture base image in your Dockerfile, AWS SAM builds your
container image for your host machine's architecture. To build for a different architecture,
specify a base image that uses the specific target architecture.

## Container environment

variable file

To provide a JSON file that contains environment variables for the build container, use
the `--container-env-var-file` argument with the `sam build` command.
You can provide a single environment variable that applies to all serverless resources, or
different environment variables for each resource.

### Format

The format for passing environment variables to a build container depends on how many
environment variables you provide for your resources.

To provide a single environment variable for all resources, specify a
`Parameters` object like the following:

```
{
  "Parameters": {
    "GITHUB_TOKEN": "`TOKEN_GLOBAL`"
  }
}
```

To provide different environment variables for each resource, specify objects for each
resource like the following:

```
{
  "MyFunction1": {
    "GITHUB_TOKEN": "`TOKEN1`"
  },
  "MyFunction2": {
    "GITHUB_TOKEN": "`TOKEN2`"
  }
}
```

Save your environment variables as a file, for example, named
`env.json`. The following command uses this file to pass your
environment variables to the build container:

```
sam build --use-container --container-env-var-file env.json
```

### Precedence

- The environment variables that you provide for specific resources take precedence
  over the single environment variable for all resources.
- Environment variables that you provide on the command line take precedence over
  environment variables in a file.

## Speed up build times by building your project in the source folder

For supported runtimes and build methods, you can use the `--build-in-source` option to build your project directly in the source folder. By default, the
AWS SAM CLI builds in a temporary directory, which involves copying over source code and project files. With `--build-in-source`, the AWS SAM
CLI builds directly in your source folder, which speeds up the build process by removing the need to copy files to a temporary directory.

For a list of supported runtimes and build methods, see `--build-in-source`.

## Examples

### Example 1: .zip file archive

The following `sam build` commands build a .zip file archive:

```
# Build all functions and layers, and their dependencies
sam build

# Run the build process inside a Docker container that functions like a Lambda environment
sam build --use-container

# Build a Node.js 20 application using a container image for a specific version of AWS SAM CLI (1.136.0)
sam build --use-container --build-image public.ecr.aws/sam/build-nodejs22.x:1.136.0

# Build a function resource using the Python 3.13 container image from a specific version of AWS SAM CLI (1.136.0)(
sam build --use-container --build-image Function1=public.ecr.aws/sam/build-python3.13:1.136.0

# Build and run your functions locally
sam build && sam local invoke

# For more options
sam build --help
```

### Example 2: Container image

The following AWS SAM template builds as a container image:

```
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      PackageType: Image
      ImageConfig:
        Command: ["app.lambda_handler"]
    Metadata:
      Dockerfile: Dockerfile
      DockerContext: ./hello_world
      DockerTag: v1
```

The following is an example Dockerfile:

```
FROM public.ecr.aws/lambda/python:3.12

COPY app.py requirements.txt ./

RUN python3.12 -m pip install -r requirements.txt

# Overwrite the command by providing a different command directly in the template.
CMD ["app.lambda_handler"]
```

### Example 3: npm ci

For Node.js applications, you can use `npm ci` instead of `npm
 install` to install dependencies. To use `npm ci`, specify
`UseNpmCi: True` under `BuildProperties` in your Lambda function's
`Metadata` resource attribute. To use `npm ci`, your application
must have a `package-lock.json` or
`npm-shrinkwrap.json` file present in the `CodeUri` for your
Lambda function.

The following example uses `npm ci` to install dependencies when you run
`sam build`:

```
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello-world/
      Handler: app.handler
      Runtime: nodejs20.x
      Architectures:
        - x86_64
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
    Metadata:
      BuildProperties:
        UseNpmCi: True

```

### Python parent packages

For Python applications, you can preserve your package structure during the build process to enable absolute imports. To preserve package structure, specify `parent_python_packages` under `BuildProperties` in your Lambda function's `Metadata` resource attribute.

The following example preserves the `app` package structure when you run `sam build`:

```
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello-world/
      Handler: app.main.handler
      Runtime: python3.12
      Architectures:
        - x86_64
    Metadata:
      BuildProperties:
        parent_python_packages: app

```

With this configuration, your code can use absolute imports like `from app.utils import logger` instead of relative imports like `from .utils import logger`.

## Building functions outside of AWS SAM

By default, when you run **sam build**, AWS SAM builds all of your function resources. Other options
include:

- **Build all function resources outside of AWS SAM** – If you build all of
  your function resources manually or through another tool, **sam build** is not required. You can
  skip **sam build** and move on to the next step in your process, such as performing local testing
  or deploying your application.
- **Build some function resources outside of AWS SAM** – If you want AWS SAM to
  build some of your function resources while having other function resources built outside of AWS SAM, you can
  specify this in your AWS SAM template.

### Build some function resources outside of AWS SAM

To have AWS SAM skip a function when using **sam build**, configure the following in your
AWS SAM template:

1. Add the `SkipBuild: True` metadata property to your function.
2. Specify the path to your built function resources.

Here is an example, with `TestFunction` configured to be skipped. Its built resources are located
at `built-resources/TestFunction.zip`.

```
TestFunction:
  Type: AWS::Serverless::Function
  Properties:
    CodeUri: built-resources/TestFunction.zip
    Handler: TimeHandler::handleRequest
    Runtime: java11
  Metadata:
    SkipBuild: True
```

Now, when you run **sam build**, AWS SAM will do the following:

1. AWS SAM will skip functions configured with `SkipBuild: True`.
2. AWS SAM will build all other function resources and cache them in the `.aws-sam` build
   directory.
3. For skipped functions, their template in the `.aws-sam` build directory will
   automatically be updated to reference the specified path to your built function resources.

Here is an example of the cached template for `TestFunction` in the `.aws-sam`
build directory:

```
TestFunction:
  Type: AWS::Serverless::Function
  Properties:
    CodeUri: ../../built-resources/TestFunction.zip
    Handler: TimeHandler::handleRequest
    Runtime: java11
  Metadata:
    SkipBuild: True
```
