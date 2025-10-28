# EcsEnvironmentFile

A list of files containing the environment variables to pass to a container. You can
specify up to ten environment files. The file must have a `.env` file extension.
Each line in an environment file should contain an environment variable in
`VARIABLE=VALUE` format. Lines beginning with `#` are treated as
comments and are ignored. For more information about the environment variable file syntax,
see [Declare default environment
variables in file](https://docs.docker.com/compose/env-file/ "https://docs.docker.com/compose/env-file/").

If there are environment variables specified using the `environment`
parameter in a container definition, they take precedence over the variables contained
within an environment file. If multiple environment files are specified that contain the
same variable, they're processed from the top down. We recommend that you use unique
variable names. For more information, see [Specifying environment
variables](../../../AmazonECS/latest/developerguide/taskdef-envfiles.md "../../../AmazonECS/latest/developerguide/taskdef-envfiles.md") in the _Amazon Elastic Container Service Developer
Guide_.

This parameter is only supported for tasks hosted on Fargate using the
following platform versions:

- Linux platform version `1.4.0` or later.
- Windows platform version `1.0.0` or later.

## Contents

**type**

The file type to use. The only supported value is `s3`.

Type: String

Valid Values: `s3`

Required: Yes

**value**

The Amazon Resource Name (ARN) of the Amazon S3 object containing the
environment variable file.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/EcsEnvironmentFile.md "../../../goto/SdkForCpp/pipes-2015-10-07/EcsEnvironmentFile.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsEnvironmentFile.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsEnvironmentFile.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsEnvironmentFile.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsEnvironmentFile.md")
