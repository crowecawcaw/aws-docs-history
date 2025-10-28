# Understanding the Lambda programming model

Lambda provides a programming model that is common to all of the runtimes. The programming model defines the
interface between your code and the Lambda system. You tell Lambda the entry point to your function by defining a
_handler_ in the function configuration. The runtime passes in objects to the handler that
contain the invocation _event_ and the _context_, such as the function name
and request ID.

When the handler finishes processing the first event, the runtime sends it another. The function's class stays
in memory, so clients and variables that are declared outside of the handler method in _initialization
code_ can be reused. To save processing time on subsequent events, create reusable resources like
AWS SDK clients during initialization. Once initialized, each instance of your function can process thousands of
requests.

Your function also has access to local storage in the `/tmp` directory, a transient cache that can be used for multiple invocations. For more information,
see [Execution environment](lambda-runtime-environment.md "lambda-runtime-environment.md").

When [AWS X-Ray tracing](services-xray.md "services-xray.md") is enabled, the runtime records separate
subsegments for initialization and execution.

The runtime captures logging output from your function and sends it to Amazon CloudWatch Logs. In addition to logging your
function's output, the runtime also logs entries when function invocation starts and ends. This includes a report
log with the request ID, billed duration, initialization duration, and other details. If your function throws an
error, the runtime returns that error to the invoker.

###### Note

Logging is subject to [CloudWatch Logs quotas](../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md "../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md"). Log data can be lost due
to throttling or, in some cases, when an instance of your function is stopped.

Lambda scales your function by running additional instances of it as demand increases, and by stopping
instances as demand decreases. This model leads to variations in application architecture, such as:

- Unless noted otherwise, incoming requests might be processed out of order or concurrently.
- Do not rely on instances of your function being long lived, instead store your application's state elsewhere.
- Use local storage and class-level objects to increase performance, but keep to a minimum the size of your deployment package and the amount of data that you transfer onto the execution environment.
  For a hands-on introduction to the programming model in your preferred programming language, see the following
  chapters.

- [Building Lambda functions with Node.js](lambda-nodejs.md "lambda-nodejs.md")
- [Building Lambda functions with Python](lambda-python.md "lambda-python.md")
- [Building Lambda functions with Ruby](lambda-ruby.md "lambda-ruby.md")
- [Building Lambda functions with Java](lambda-java.md "lambda-java.md")
- [Building Lambda functions with Go](lambda-golang.md "lambda-golang.md")
- [Building Lambda functions with C#](lambda-csharp.md "lambda-csharp.md")
- [Building Lambda functions with PowerShell](lambda-powershell.md "lambda-powershell.md")
