# AdapterVersionOverview

Summary info for an adapter version. Contains information on the AdapterId, AdapterVersion, CreationTime, FeatureTypes, and Status.

## Contents

**AdapterId**

A unique identifier for the adapter associated with a given adapter version.

Type: String

Length Constraints: Minimum length of 12. Maximum length of 1011.

Required: No

**AdapterVersion**

An identified for a given adapter version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: No

**CreationTime**

The date and time that a given adapter version was created.

Type: Timestamp

Required: No

**FeatureTypes**

The feature types that the adapter version is operating on.

Type: Array of strings

Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`

Required: No

**Status**

Contains information on the status of a given adapter version.

Type: String

Valid Values: `ACTIVE | AT_RISK | DEPRECATED | CREATION_ERROR | CREATION_IN_PROGRESS`

Required: No

**StatusMessage**

A message explaining the status of a given adapter vesion.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/AdapterVersionOverview.md "../../../goto/SdkForCpp/textract-2018-06-27/AdapterVersionOverview.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionOverview.md "../../../goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionOverview.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionOverview.md "../../../goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionOverview.md")
