# Specify the AWS CodeBuild endpoint

You can use the AWS Command Line Interface (AWS CLI) or one of the AWS SDKs to specify the endpoint used
by AWS CodeBuild. There is an endpoint for each region in which CodeBuild is available. In addition to a
regional endpoint, four regions also have a Federal Information Processing Standards (FIPS)
endpoint. For more information about FIPS endpoints, see [FIPS 140-2 overview](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

Specifying an endpoint is optional. If you don't explicitly tell CodeBuild which endpoint to
use, the service uses the endpoint associated with the region your AWS account uses. CodeBuild
never defaults to a FIPS endpoint. If you want to use a FIPS endpoint, you must associate
CodeBuild with it using one of the following methods.

###### Note

You can use an alias or region name to specify an endpoint using an AWS SDK. If you
use the AWS CLI, then you must use the full endpoint name.

For endpoints that can be used with CodeBuild, see [CodeBuild regions and endpoints](../../../general/latest/gr/rande.md#codebuild_region "../../../general/latest/gr/rande.md#codebuild_region").

###### Topics

- [Specify the AWS CodeBuild endpoint (AWS CLI)](#endpoint-specify-cli "#endpoint-specify-cli")
- [Specify the AWS CodeBuild endpoint (AWS SDK)](#endpoint-specify-sdk "#endpoint-specify-sdk")

## Specify the AWS CodeBuild endpoint (AWS CLI)

You can use the AWS CLI to specify the endpoint through which AWS CodeBuild is accessed by
using the `--endpoint-url` argument in any CodeBuild command. For example, run
this command to get a list of project build names using the Federal Information
Processing Standards (FIPS) endpoint in the US East (N. Virginia) Region:

```
aws codebuild list-projects --endpoint-url https://codebuild-fips.us-east-1.amazonaws.com
```

Include the `https://` at the begining of the endpoint.

The `--endpoint-url` AWS CLI argument is available to all AWS services. For more information about this and
other AWS CLI arguments, see [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

## Specify the AWS CodeBuild endpoint (AWS SDK)

You can use an AWS SDK to specify the endpoint through which AWS CodeBuild is accessed.
Although this example uses the [AWS
SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/"), you can specify the endpoint with the other AWS SDKs.

Use the `withEndpointConfiguration` method when constructing the
AWSCodeBuild client. Here is format to use:

```

AWSCodeBuild awsCodeBuild = AWSCodeBuildClientBuilder.standard().
    withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("`endpoint`", "`region`")).
    withCredentials(new AWSStaticCredentialsProvider(sessionCredentials)).
    build();

```

For information about `AWSCodeBuildClientBuilder`, see [Class
AWSCodeBuildClientBuilder](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/codebuild/AWSCodeBuildClientBuilder.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/codebuild/AWSCodeBuildClientBuilder.md").

The credentials used in `withCredentials` must be of type `AWSCredentialsProvider`. For more information,
see [Working with AWS credentials](../../../sdk-for-java/latest/developer-guide/credentials.md "../../../sdk-for-java/latest/developer-guide/credentials.md").

Do not include `https://` at the begining of the endpoint.

If you want to specify a non-FIPS endpoint, you can use the region instead of the
actual endpoint. For example, to specify the endpoint in the US East (N. Virginia) region,
you can use `us-east-1` instead of the full endpoint name, `codebuild.us-east-1.amazonaws.com`.

If you want to specify a FIPS endpoint, you can use an alias to simplify your code.
Only FIPS endpoints have an alias. Other endpoints must be specified using their region
or full name.

The following table lists the alias for each of the four available FIPS
endpoints:

| Region name             | Region    | Endpoint                               | Alias          |
| ----------------------- | --------- | -------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| US East (N. Virginia)   | us-east-1 | codebuild-fips.us-east-1.amazonaws.com | us-east-1-fips |
| US East (Ohio)          | us-east-2 | codebuild-fips.us-east-2.amazonaws.com | us-east-2-fips |
| US West (N. California) | us-west-1 | codebuild-fips.us-west-1.amazonaws.com | us-west-1-fips |
| US West (Oregon)        | us-west-2 | codebuild-fips.us-west-2.amazonaws.com | us-west-2-fips | To specify use of the FIPS endpoint in the US West (Oregon) region using an alias: `AWSCodeBuild awsCodeBuild = AWSCodeBuildClientBuilder.standard(). withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("us-west-2-fips", "us-west-2")). withCredentials(new AWSStaticCredentialsProvider(sessionCredentials)). build();` To specify use of the non-FIPS endpoint in the US East (N. Virginia) region: `AWSCodeBuild awsCodeBuild = AWSCodeBuildClientBuilder.standard(). withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("us-east-1", "us-east-1")). withCredentials(new AWSStaticCredentialsProvider(sessionCredentials)). build();` To specify use of the non-FIPS endpoint in the Asia Pacific (Mumbai) region: `AWSCodeBuild awsCodeBuild = AWSCodeBuildClientBuilder.standard(). withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("ap-south-1", "ap-south-1")). withCredentials(new AWSStaticCredentialsProvider(sessionCredentials)). build();` |
