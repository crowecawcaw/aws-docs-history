

# Building Lambda Event Functions with customer-managed runtimes in AWS SAM

A Lambda Event Function that uses a customer-managed runtime sets `Runtime` to `custom` and specifies the ARN of the runtime and the name of the runtime alias in its [RuntimeConfig](sam-resource-function.md#sam-function-runtimeconfig) property. To learn more about customer-managed runtimes, see [Using a customer-managed runtime](https://docs.aws.amazon.com/lambda/latest/dg/cmr-using.html) in the *AWS Lambda Developer Guide*.

Because `custom` doesn't name a language, `sam build` uses the `BuildMethod` in the `Metadata` resource attribute of the function to choose how to build the code. Set `BuildMethod` to the Lambda runtime that matches your code, such as `python3.12`, or to `makefile`. **sam build** then builds your code the same way as for that runtime, or with your makefile. For more information about makefiles, see [Building Lambda Event Functions with custom runtimes in AWS SAM](building-custom-runtimes.md).

Note the following when you build a function that uses a customer-managed runtime:
+ If you don't set `BuildMethod`, or set it to a value that isn't a Lambda runtime or `makefile`, such as `esbuild`, the build fails.
+ With `--use-container`, **sam build** uses the build image for the `BuildMethod` runtime. With `BuildMethod: makefile`, there's no default build image, so also pass `--build-image`.
+ **sam build** doesn't look up the runtime, so you don't need access to the runtime to build the function.

## Example: Python function that uses a customer-managed runtime
<a name="building-customer-managed-runtimes-example"></a>

The following template builds a Python function that uses the `prod` alias of a customer-managed runtime.

```yaml
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: {{src/}}
      Handler: {{app.handler}}
      Runtime: custom
      RuntimeConfig:
        RuntimeArn: {{arn:aws:lambda:us-east-1:111122223333:runtime/my-python-runtime}}
        RuntimeAlias: {{prod}}
    Metadata:
      BuildMethod: {{python3.12}}
```

To test the function locally, see [Testing and debugging functions that use customer-managed runtimes](test-and-debug-customer-managed-runtimes.md).