# Building Lambda functions with Ruby

You can run Ruby code in AWS Lambda. Lambda provides [runtimes](lambda-runtimes.md "lambda-runtimes.md") for Ruby that run your code to process events. Your code runs
in an environment that includes the AWS SDK for Ruby, with credentials from an AWS Identity and Access Management (IAM) role that you manage. To learn more
about the SDK versions included with the Ruby runtimes, see [Runtime-included SDK versions](#ruby-sdk-included "#ruby-sdk-included").

Lambda supports the following Ruby runtimes.

| Name     | Identifier | Operating system  | Deprecation date | Block function create | Block function update |
| -------- | ---------- | ----------------- | ---------------- | --------------------- | --------------------- |
| Ruby 3.4 | `ruby3.4`  | Amazon Linux 2023 | Mar 31, 2028     | Apr 30, 2028          | May 31, 2028          |
| Ruby 3.3 | `ruby3.3`  | Amazon Linux 2023 | Mar 31, 2027     | Apr 30, 2027          | May 31, 2027          |
| Ruby 3.2 | `ruby3.2`  | Amazon Linux 2    | Mar 31, 2026     | Jun 1, 2026           | Jul 1, 2026           |

###### To create a Ruby function

1. Open the [Lambda console](https://console.aws.amazon.com/lambda "https://console.aws.amazon.com/lambda").
2. Choose **Create function**.
3. Configure the following settings:
   - **Function name**: Enter a name for the function.
   - **Runtime**: Choose **Ruby 3.4**.

4. Choose **Create function**.
   The console creates a Lambda function with a single source file named `lambda_function.rb`. You can edit this file and add more files in the built-in code editor. In the **DEPLOY** section, choose **Deploy** to update your function's code. Then, to run your code, choose **Create test event** in the **TEST EVENTS** section.

The `lambda_function.rb` file exports a function named `lambda_handler` that takes an event object and a
context object. This is the [handler function](ruby-handler.md "ruby-handler.md") that Lambda calls when the
function is invoked. The Ruby function runtime gets invocation events from Lambda and passes them to the
handler. In the function configuration, the handler value is `lambda_function.lambda_handler`.

When you save your function code, the Lambda console creates a .zip file archive deployment package.
When you develop your function code outside of the console (using an IDE) you need to [create a
deployment package](ruby-package.md "ruby-package.md") to upload your code to the Lambda function.

The function runtime passes a context object to the handler, in addition to the invocation event. The [context object](ruby-context.md "ruby-context.md") contains additional information about the invocation, the
function, and the execution environment. More information is available from environment variables.

Your Lambda function comes with a CloudWatch Logs log group. The function runtime sends details about each invocation to
CloudWatch Logs. It relays any [logs that your function outputs](ruby-logging.md "ruby-logging.md") during invocation. If
your function returns an error, Lambda formats the error and returns it to the
invoker.

###### Topics

- [Runtime-included SDK versions](#ruby-sdk-included "#ruby-sdk-included")
- [Enabling Yet Another Ruby JIT (YJIT)](#ruby-yjit "#ruby-yjit")
- [Define Lambda function handler in Ruby](ruby-handler.md "ruby-handler.md")
- [Deploy Ruby Lambda functions with .zip file archives](ruby-package.md "ruby-package.md")
- [Deploy Ruby Lambda functions with container images](ruby-image.md "ruby-image.md")
- [Working with layers for Ruby Lambda functions](ruby-layers.md "ruby-layers.md")
- [Using the Lambda context object to retrieve Ruby function information](ruby-context.md "ruby-context.md")
- [Log and monitor Ruby Lambda functions](ruby-logging.md "ruby-logging.md")
- [Instrumenting Ruby code in AWS Lambda](ruby-tracing.md "ruby-tracing.md")

## Runtime-included SDK versions

The version of the AWS SDK included in the Ruby runtime depends on the runtime version and your AWS Region. The AWS SDK for Ruby is designed to be modular and is
separated by AWS service. To find the version number of a particular service gem included in the runtime you're using, create a Lambda function with code in the following
format. Replace `aws-sdk-s3` and `Aws::S3`with the name of the service gems your code uses.

```
require 'aws-sdk-s3'

def lambda_handler(event:, context:)
  puts "Service gem version: #{Aws::S3::GEM_VERSION}"
  puts "Core version: #{Aws::CORE_GEM_VERSION}"
end
```

## Enabling Yet Another Ruby JIT (YJIT)

The Ruby 3.2 runtime supports [YJIT](https://github.com/ruby/ruby/blob/master/doc/yjit/yjit.md "https://github.com/ruby/ruby/blob/master/doc/yjit/yjit.md"), a lightweight, minimalistic Ruby JIT compiler. YJIT provides significantly higher performance, but also uses more memory than the Ruby interpreter. YJIT is recommended for Ruby on Rails workloads.

YJIT is not enabled by default. To enable YJIT for a Ruby 3.2 function, set the `RUBY_YJIT_ENABLE` environment variable to `1`. To confirm that YJIT is enabled, print the result of the `RubyVM::YJIT.enabled?` method.

###### Example — Confirm that YJIT is enabled

```
puts(RubyVM::YJIT.enabled?())
# => true
```
