# Building Lambda functions with Rust

Because Rust compiles to native code, you don't need a dedicated runtime to run Rust code on Lambda. Instead, use the [Rust runtime client](https://github.com/awslabs/aws-lambda-rust-runtime "https://github.com/awslabs/aws-lambda-rust-runtime") to build your project locally, and then deploy it to Lambda using the `provided.al2023` or `provided.al2` runtime. When you use `provided.al2023` or `provided.al2`, Lambda automatically keeps the operating system up to date with the latest patches.

###### Note

The [Rust runtime client](https://github.com/awslabs/aws-lambda-rust-runtime "https://github.com/awslabs/aws-lambda-rust-runtime") is an experimental package. It is subject to change and intended only for evaluation purposes.

###### Tools and libraries for Rust

- [AWS SDK for Rust](../../../sdk-for-rust/latest/dg/getting-started.md "../../../sdk-for-rust/latest/dg/getting-started.md"): The AWS SDK for Rust
  provides Rust APIs to interact with Amazon Web Services infrastructure services.
- [Rust runtime client for Lambda](https://github.com/awslabs/aws-lambda-rust-runtime "https://github.com/awslabs/aws-lambda-rust-runtime"): The Rust runtime client is an experimental package. It is subject to breaking changes and not recommended for production.
- [Cargo
  Lambda](https://www.cargo-lambda.info/guide/what-is-cargo-lambda.html "https://www.cargo-lambda.info/guide/what-is-cargo-lambda.html"): This library provides a command line application to work with Lambda
  functions built with Rust.
- [Lambda
  HTTP](https://github.com/awslabs/aws-lambda-rust-runtime/tree/main/lambda-http "https://github.com/awslabs/aws-lambda-rust-runtime/tree/main/lambda-http"): This library provides a wrapper to work with HTTP events.
- [Lambda
  Extension](https://github.com/awslabs/aws-lambda-rust-runtime/tree/main/lambda-extension "https://github.com/awslabs/aws-lambda-rust-runtime/tree/main/lambda-extension"): This library provides support to write Lambda Extensions with Rust.
- [AWS Lambda Events](https://crates.io/crates/aws_lambda_events "https://crates.io/crates/aws_lambda_events"):
  This library provides type definitions for common event source integrations.

###### Sample Lambda applications for Rust

- [Basic
  Lambda function](https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/basic-lambda "https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/basic-lambda"): A Rust function that shows how to process basic events.
- [Lambda
  function with error handling](https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/basic-error-handling "https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/basic-error-handling"): A Rust function that shows how to handle custom Rust
  errors in Lambda.
- [Lambda
  function with shared resources](https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/basic-shared-resource "https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/basic-shared-resource"): A Rust project that initializes shared resources
  before creating the Lambda function.
- [Lambda
  HTTP events](https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/http-basic-lambda "https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/http-basic-lambda"): A Rust function that handles HTTP events.
- [Lambda
  HTTP events with CORS headers](https://github.com/awslabs/aws-lambda-rust-runtime/blob/main//examples/http-cors "https://github.com/awslabs/aws-lambda-rust-runtime/blob/main//examples/http-cors"): A Rust function that uses Tower to inject CORS headers.
- [Lambda REST API](https://github.com/awslabs/aws-lambda-rust-runtime/tree/main/examples/http-axum-diesel "https://github.com/awslabs/aws-lambda-rust-runtime/tree/main/examples/http-axum-diesel"): A REST API that uses Axum and Diesel to connect to a PostgreSQL database.
- [Serverless Rust
  demo](https://github.com/aws-samples/serverless-rust-demo/ "https://github.com/aws-samples/serverless-rust-demo/"): A Rust project that shows the use of Lambda's Rust libraries, logging,
  environment variables, and the AWS SDK.
- [Basic
  Lambda Extension](https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/extension-basic "https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/extension-basic"): A Rust extension that shows how to process basic extension events.
- [Lambda
  Logs Amazon Data Firehose Extension](https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/extension-logs-kinesis-firehose "https://github.com/awslabs/aws-lambda-rust-runtime/blob/main/examples/extension-logs-kinesis-firehose"): A Rust extension that shows how to send Lambda logs
  to Firehose.

###### Topics

- [Define Lambda function handlers in Rust](rust-handler.md "rust-handler.md")
- [Using the Lambda context object to retrieve Rust function information](rust-context.md "rust-context.md")
- [Processing HTTP events with Rust](rust-http-events.md "rust-http-events.md")
- [Deploy Rust Lambda functions with .zip file archives](rust-package.md "rust-package.md")
- [Working with layers for Rust Lambda functions](rust-layers.md "rust-layers.md")
- [Log and monitor Rust Lambda functions](rust-logging.md "rust-logging.md")
