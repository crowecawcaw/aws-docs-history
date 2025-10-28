# Retry builds automatically in AWS CodeBuild

You can use the AWS CodeBuild console, AWS CLI, or AWS SDKs to automatically retry your builds in AWS CodeBuild. With auto-retry enabled,
CodeBuild will automatically call `RetryBuild` using the project's service role after a failed build up to a specified limit. For example, if the
auto-retry limit is set to two, CodeBuild will call the `RetryBuild` API to automatically retry your build for up to two additional times.

###### Note

CodeBuild does not support auto-retry for CodePipeline.

###### Topics

- [Retry a build automatically (console)](#auto-retry-build-console "#auto-retry-build-console")
- [Retry a build automatically (AWS CLI)](#auto-retry-build-cli "#auto-retry-build-cli")
- [Automatically retry a build (AWS SDKs)](#auto-retry-build-sdks "#auto-retry-build-sdks")

## Retry a build automatically (console)

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. Choose **Create project**. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console")
   and [Run a build (console)](run-build-console.md "run-build-console.md").
   - In **Environment**:
     - For **Auto-retry limit**, enter the maximum number of
       auto-retries desired after a failed build.

3. In **Environment**, choose **Additional configuration**.
4. Continue with the default values and then choose **Create build project**.

## Retry a build automatically (AWS CLI)

- Run the **create-project** command:

```
aws codebuild create-project \
    --name "`<project-name>`" \
    --auto-retry-limit `<auto-retry-limit>` \
    --source "`<source>`" \
    --artifacts {`<artifacts>`} \
    --environment "{\"type\": \"`environment-type>`\",\"image\": \"`image-type>`\",\"computeType\": \"`compute-type>`\"}" \
    --service-role "`service-role>`"
```

In the preceding command, replace the following placeholders:

    + `<auto-retry-limit>`: Set the auto-retry limit
     to the maximum number of auto-retries desired after a failed build.
    + `<project-name>`, `<source>`,
     `<artifacts>`, `environment-type>`, `image-type>`,
     `compute-type>`, and `service-role>`: Set your desired project configuration settings.

## Automatically retry a build (AWS SDKs)

For more information about using AWS CodeBuild with the AWS SDKs, see the [AWS SDKs and tools reference](sdk-ref.md "sdk-ref.md").
