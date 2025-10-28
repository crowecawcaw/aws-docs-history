# DatabaseInputDefinition

Connection information for dataset input files stored in a database.

## Contents

###### Note

In the following list, the required parameters are described first.

**GlueConnectionName**

The AWS Glue Connection that stores the connection information for the target
database.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**DatabaseTableName**

The table within the target database.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**QueryString**

Custom SQL to run against the provided AWS Glue connection. This SQL will be used as
the input for DataBrew projects and jobs.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 10000.

Required: No

**TempDirectory**

Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read
input data, or write output from a job.

Type: [S3Location](API_S3Location.md "API_S3Location.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DatabaseInputDefinition.md "../../../goto/SdkForCpp/databrew-2017-07-25/DatabaseInputDefinition.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DatabaseInputDefinition.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DatabaseInputDefinition.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DatabaseInputDefinition.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DatabaseInputDefinition.md")
