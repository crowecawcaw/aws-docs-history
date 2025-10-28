# Customize builds with AWS SAM

You can customize your build to include specific Lambda functions or Lambda layers. A function is a resource that you can invoke to run your code in Lambda.
A Lambda layer allows you to extract code from a Lambda function that can then be re-used across several Lambda functions.
You may choose to customize your build with specific Lambda functions when you want to focus on developing and deploying
individual serverless functions without the complexity of managing shared dependencies or resources. Additionally, you may choose to build a Lambda layer
to help you reduce the size of your deployment packages, separate core function logic from dependencies, and allow you to share dependencies across multiple functions.

The topics in this section explore some of the different ways you can build Lambda functions with AWS SAM. This includes building Lambda functions with customer runtimes and building Lambda layers.
Custom runtimes let you install and use a language not listed in Lambda runtimes in the AWS Lambda Developer Guide.
This allows you to create a specialized execution environment for running serverless functions and applications.
Building only Lambda layers (instead of building your entire application) can benefit you in a few ways. It can help you reduce the size of your deployment packages, separate core function logic
from dependencies, and allow you to share dependencies across multiple functions.

For more information on functions, see [Lambda concepts](../../../lambda/latest/dg/gettingstarted-concepts.md "../../../lambda/latest/dg/gettingstarted-concepts.md") in the _AWS Lambda Developer Guide_.

###### Topics

- [Building Node.js Lambda functions
  with esbuild in AWS SAM](serverless-sam-cli-using-build-typescript.md "serverless-sam-cli-using-build-typescript.md")
- [Building .NET Lambda functions with Native AOT
  compilation in AWS SAM](build-dotnet7.md "build-dotnet7.md")
- [Building Rust Lambda functions with Cargo Lambda in AWS SAM](building-rust.md "building-rust.md")
- [Building Lambda functions with custom runtimes in AWS SAM](building-custom-runtimes.md "building-custom-runtimes.md")
- [Building Lambda layers in AWS SAM](building-layers.md "building-layers.md")
