# Building .NET Lambda functions with Native AOT

compilation in AWS SAM

Build and package your .NET 8 AWS Lambda functions with the AWS Serverless Application Model (AWS SAM), utilizing
Native Ahead-of-Time (AOT) compilation to improve AWS Lambda cold-start times.

###### Topics

- [.NET 8 Native AOT overview](#build-dotnet7-overview "#build-dotnet7-overview")
- [Using AWS SAM with your .NET 8 Lambda functions](#build-dotnet7-sam "#build-dotnet7-sam")
- [Install prerequisites](#build-dotnet7-prerequisites "#build-dotnet7-prerequisites")
- [Define .NET 8 Lambda functions in your AWS SAM
  template](#build-dotnet7-sam-define "#build-dotnet7-sam-define")
- [Build your application with the AWS SAM CLI](#build-dotnet7-sam-build "#build-dotnet7-sam-build")
- [Learn more](#build-dotnet7-learn-more "#build-dotnet7-learn-more")

## .NET 8 Native AOT overview

Historically, .NET Lambda functions have cold-start times which impact user experience,
system latency, and usage costs of your serverless applications. With .NET Native AOT compilation,
you can improve cold-start times of your Lambda functions. To learn more about Native AOT for .NET 8, see [Using Native
AOT](https://github.com/dotnet/runtime/tree/main/src/coreclr/nativeaot#readme "https://github.com/dotnet/runtime/tree/main/src/coreclr/nativeaot#readme") in the _Dotnet GitHub repository_.

## Using AWS SAM with your .NET 8 Lambda functions

Do the following to configure your .NET 8 Lambda functions with the AWS Serverless Application Model
(AWS SAM):

- Install prerequisites on your development machine.
- Define .NET 8 Lambda functions in your AWS SAM template.
- Build your application with the AWS SAM CLI.

## Install prerequisites

The following are required prerequisites:

- The AWS SAM CLI
- The .NET Core CLI
- The Amazon.Lambda.Tools .NET Core Global Tool
- Docker

###### Install the AWS SAM CLI

1. To check if you already have the AWS SAM CLI installed, run the following:

```
sam --version
```

2. To install the AWS SAM CLI, see [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").
3. To upgrade an installed version of the AWS SAM CLI, see [Upgrading the AWS SAM CLI](manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade "manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade").

###### Install the .NET Core CLI

1. To download and install the .NET Core CLI, see [Download .NET](https://dotnet.microsoft.com/download "https://dotnet.microsoft.com/download") from Microsoft's
   website.
2. For more information on the .NET Core CLI, see [.NET Core CLI](../../../lambda/latest/dg/csharp-package-cli.md "../../../lambda/latest/dg/csharp-package-cli.md") in the
   _AWS Lambda Developer Guide_.

###### Install the Amazon.Lambda.Tools .NET Core Global Tool

1. Run the following command:

```
dotnet tool install -g Amazon.Lambda.Tools
```

2. If you already have the tool installed, you can make sure that it is the latest
   version using the following command:

```
dotnet tool update -g Amazon.Lambda.Tools
```

3. For more information about the Amazon.Lambda.Tools .NET Core Global Tool, see the
   [AWS Extensions for
   .NET CLI](https://github.com/aws/aws-extensions-for-dotnet-cli "https://github.com/aws/aws-extensions-for-dotnet-cli") repository on GitHub.

###### Install Docker

- Building with Native AOT, requires Docker to be installed. For
  installation instructions, see [Installing Docker to use with the AWS SAM CLI](install-docker.md "install-docker.md").

## Define .NET 8 Lambda functions in your AWS SAM

template

To define a .NET8 Lambda function in your AWS SAM template, do the following:

1. Run the following command from a starting directory of your choice::

```
sam init
```

2. Select `AWS Quick Start Templates` to choose a starting template.
3. Choose the `Hello World Example` template.
4. Choose to not use the most popular runtime and package type by entering `n`.
5. For runtime, choose `dotnet8`.
6. For package type, choose `Zip`.
7. For your starter template, choose `Hello World Example using native AOT`.

###### Install Docker

- Building with Native AOT, requires Docker to be installed. For
  installation instructions, see [Installing Docker to use with the AWS SAM CLI](install-docker.md "install-docker.md").

```
Resources:
HelloWorldFunction:
  Type: AWS::Serverless::Function
  Properties:
    CodeUri: ./src/HelloWorldAot/
    Handler: bootstrap
    Runtime: dotnet8
    Architectures:
      - x86_64
    Events:
      HelloWorldAot:
        Type: Api
        Properties:
          Path: /hello
          Method: get
```

###### Note

When the `Event` property of an `AWS::Serverless::Function` is set to `Api`,
but the `RestApiId` property is not specified, AWS SAM generates the `AWS::ApiGateway::RestApi` CloudFormation resource.

## Build your application with the AWS SAM CLI

From your project's root directory, run the `sam build` command to begin building your
application. If the `PublishAot` property has been defined in your .NET 8 project
file, the AWS SAM CLI will build with Native AOT compilation. To learn more about the
`PublishAot` property, see [Native AOT
Deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/ "https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/") in Microsoft's _.NET documentation_.

To build your function, the AWS SAM CLI invokes the .NET Core CLI which uses the
Amazon.Lambda.Tools .NET Core Global Tool.

###### Note

When building, if a `.sln` file exists in the same or parent
directory of your project, the directory containing the `.sln` file will
be mounted to the container. If a `.sln` file is not found, only the
project folder is mounted. Therefore, if you are building a multi-project application,
ensure the `.sln` file is property located.

## Learn more

For more information on building .NET 8 Lambda functions, see [Introducing the .NET 8 runtime for AWS Lambda](https://aws.amazon.com/blogs/compute/introducing-the-net-8-runtime-for-aws-lambda/ "https://aws.amazon.com/blogs/compute/introducing-the-net-8-runtime-for-aws-lambda/").

For a reference of the **sam build** command, see [sam build](sam-cli-command-reference-sam-build.md "sam-cli-command-reference-sam-build.md").
