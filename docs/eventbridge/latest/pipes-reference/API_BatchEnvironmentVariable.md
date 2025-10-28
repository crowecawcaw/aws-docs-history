# BatchEnvironmentVariable

The environment variables to send to the container. You can add new environment
variables, which are added to the container at launch, or you can override the existing
environment variables from the Docker image or the task definition.

###### Note

Environment variables cannot start with "`AWS Batch` ". This
naming convention is reserved for variables that AWS Batch sets.

## Contents

**Name**

The name of the key-value pair. For environment variables, this is the name of the
environment variable.

Type: String

Required: No

**Value**

The value of the key-value pair. For environment variables, this is the value of the
environment variable.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/BatchEnvironmentVariable.md "../../../goto/SdkForCpp/pipes-2015-10-07/BatchEnvironmentVariable.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/BatchEnvironmentVariable.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/BatchEnvironmentVariable.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/BatchEnvironmentVariable.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/BatchEnvironmentVariable.md")
