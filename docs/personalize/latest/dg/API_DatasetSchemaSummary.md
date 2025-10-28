# DatasetSchemaSummary

Provides a summary of the properties of a dataset schema. For a complete listing, call the
[DescribeSchema](API_DescribeSchema.md "API_DescribeSchema.md") API.

## Contents

**creationDateTime**

The date and time (in Unix time) that the schema was created.

Type: Timestamp

Required: No

**domain**

The domain of a schema that you created for a dataset in a Domain dataset group.

Type: String

Valid Values: `ECOMMERCE | VIDEO_ON_DEMAND`

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the schema was last updated.

Type: Timestamp

Required: No

**name**

The name of the schema.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**schemaArn**

The Amazon Resource Name (ARN) of the schema.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DatasetSchemaSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/DatasetSchemaSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetSchemaSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetSchemaSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetSchemaSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetSchemaSummary.md")
