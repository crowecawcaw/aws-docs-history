# Debug your serverless

application with AWS SAM

After testing your application, you will be ready to debug any issues you’ve found.
With the AWS SAM command line interface (CLI), you can locally test and debug your serverless
application before uploading it to the AWS Cloud. Debugging your application identifies and
fixes issues or errors in your application.

You can use AWS SAM to perform step-through debugging, which is a method of running code one line or instruction at a time.
When you locally invoke a Lambda function in debug mode within the AWS SAM CLI, you can then attach a debugger to it.
With the debugger, you can step through your code line by line, see the values of different variables, and fix issues
the same way you would for any other application. You can
verify whether your application is behaving as expected, debug what's wrong, and fix any issues,
before going through the steps of packaging and deploying your application.

###### Note

If your application includes one or more layers, when you locally run and debug your
application the layers package is downloaded and cached on your local host. For more
information, see [How layers are cached locally](serverless-sam-cli-layers.md#local-testing-with-layers "serverless-sam-cli-layers.md#local-testing-with-layers").

###### Topics

- [Locally debug functions with AWS SAM](serverless-sam-cli-using-debugging.md "serverless-sam-cli-using-debugging.md")
- [Pass multiple runtime arguments when debugging with AWS SAM](serverless-sam-cli-using-debugging-additional-arguments.md "serverless-sam-cli-using-debugging-additional-arguments.md")
- [Validate your AWS SAM applications with CloudFormation Linter](validate-cfn-lint.md "validate-cfn-lint.md")
