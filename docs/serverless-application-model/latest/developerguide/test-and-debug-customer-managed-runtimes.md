

# Testing and debugging functions that use customer-managed runtimes

A function that uses a customer-managed runtime sets `Runtime` to `custom`. Its [RuntimeConfig](sam-resource-function.md#sam-function-runtimeconfig) property specifies the ARN of the runtime and the name of the runtime alias.

**sam local invoke**, **sam local start-api**, and **sam local start-lambda** run the function on the container image of that runtime.

To learn more about customer-managed runtimes, see [Using a customer-managed runtime](https://docs.aws.amazon.com/lambda/latest/dg/cmr-using.html) in the *AWS Lambda Developer Guide*. To build the function, see [Building Lambda Event Functions with customer-managed runtimes in AWS SAM](building-customer-managed-runtimes.md).

## Local testing
<a name="test-and-debug-customer-managed-runtimes-local"></a>

By default, the AWS SAM CLI looks up the runtime image from `RuntimeConfig`, and then pulls the image:
+ It asks Lambda which runtime version `RuntimeAlias` points to, and which image that version uses.
+ It uses your AWS credentials and the Region in `RuntimeArn`.
+ It always uses the runtime version that the alias points to. It ignores [RuntimeManagementConfig](sam-resource-function.md#sam-function-runtimemanagementconfig), including a runtime version that you pinned with `Manual` mode.

Local testing needs access that deploying the function doesn't need:
+ The `lambda:GetRuntimeAlias` and `lambda:GetRuntimeVersion` permissions on the runtime.
+ Permission to pull the image from its Amazon ECR repository.
+ Docker signed in to that registry. For more information, see [Private registry authentication in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html).

If the runtime is in another AWS account, the runtime publisher must also grant the `lambda:GetRuntimeAlias` and `lambda:GetRuntimeVersion` permissions to your account in the resource-based policy of the runtime. For more information, see [Sharing and controlling access to customer-managed runtimes](https://docs.aws.amazon.com/lambda/latest/dg/cmr-permissions.html) in the *AWS Lambda Developer Guide*.

A function that you deploy doesn't need access to the image, because Lambda reads the image itself.

To use a different runtime image, pass it with `--invoke-image`. The AWS SAM CLI then doesn't look up `RuntimeConfig`. The following is an example:

```
$ sam local invoke {{MyFunction}} --invoke-image {{111122223333.dkr.ecr.us-east-1.amazonaws.com/my-python-runtime:v2}}
```

The AWS SAM CLI can look up the runtime only when `RuntimeArn` and `RuntimeAlias` are literal values or template parameters. If a value comes from an intrinsic function that the AWS SAM CLI can't resolve locally, such as `Fn::ImportValue`, pass the runtime image with `--invoke-image`.

## Debugging
<a name="test-and-debug-customer-managed-runtimes-debug"></a>

When you debug, the AWS SAM CLI uses the debug settings of the runtime that `Metadata.BuildMethod` names. Debugging works with the following runtime images:
+ Java – Any runtime image.
+ Python, Node.js, and .NET – Only a runtime image built from a Lambda base image for that language, such as `public.ecr.aws/lambda/python:3.12`.

## Troubleshooting
<a name="test-and-debug-customer-managed-runtimes-troubleshooting"></a>

### Not allowed to look up runtime
<a name="test-and-debug-customer-managed-runtimes-troubleshooting-lookup"></a>

**Problem:** A **sam local** command fails with `Not allowed to look up runtime`. Your AWS credentials can't call `lambda:GetRuntimeAlias` or `lambda:GetRuntimeVersion` for the runtime in `RuntimeConfig`.

**Solutions:**
+ Get these permissions. If another AWS account owns the runtime, ask the runtime publisher to grant them to your account in the resource-based policy of the runtime.
+ Pass the runtime image with `--invoke-image`.

### Runtime image can't be pulled
<a name="test-and-debug-customer-managed-runtimes-troubleshooting-pull"></a>

**Problem:** A **sam local** command finds the runtime image, and then fails with an error from Docker, such as `no basic auth credentials` or `denied`.

**Solutions:**
+ Sign in Docker to the Amazon ECR registry of the runtime image. The following is an example:

  ```
  $ aws ecr get-login-password --region {{us-east-1}} | docker login --username AWS --password-stdin {{111122223333.dkr.ecr.us-east-1.amazonaws.com}}
  ```

  For more information, see [Private registry authentication in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html).
+ If another AWS account owns the repository, ask the runtime publisher to grant your account `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` in the repository policy.
+ Pass a runtime image that you can pull with `--invoke-image`.