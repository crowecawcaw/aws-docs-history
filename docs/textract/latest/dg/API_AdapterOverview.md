# AdapterOverview

Contains information on the adapter, including the adapter ID, Name, Creation time, and feature types.

## Contents

**AdapterId**

A unique identifier for the adapter resource.

Type: String

Length Constraints: Minimum length of 12. Maximum length of 1011.

Required: No

**AdapterName**

A string naming the adapter resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9-_]+`

Required: No

**CreationTime**

The date and time that the adapter was created.

Type: Timestamp

Required: No

**FeatureTypes**

The feature types that the adapter is operating on.

Type: Array of strings

Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/AdapterOverview.md "../../../goto/SdkForCpp/textract-2018-06-27/AdapterOverview.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/AdapterOverview.md "../../../goto/SdkForJavaV2/textract-2018-06-27/AdapterOverview.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/AdapterOverview.md "../../../goto/SdkForRubyV3/textract-2018-06-27/AdapterOverview.md")
