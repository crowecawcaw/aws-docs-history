# Dataset

Represents a dataset that can be processed by DataBrew.

## Contents

###### Note

In the following list, the required parameters are described first.

**Input**

Information on how DataBrew can find the dataset, in either the AWS Glue Data Catalog
or Amazon S3.

Type: [Input](API_Input.md "API_Input.md") object

Required: Yes

**Name**

The unique name of the dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**AccountId**

The ID of the AWS account that owns the dataset.

Type: String

Length Constraints: Maximum length of 255.

Required: No

**CreateDate**

The date and time that the dataset was created.

Type: Timestamp

Required: No

**CreatedBy**

The Amazon Resource Name (ARN) of the user who created the dataset.

Type: String

Required: No

**Format**

The file format of a dataset that is created from an Amazon S3 file or folder.

Type: String

Valid Values: `CSV | JSON | PARQUET | EXCEL | ORC`

Required: No

**FormatOptions**

A set of options that define how DataBrew interprets the data in the dataset.

Type: [FormatOptions](API_FormatOptions.md "API_FormatOptions.md") object

Required: No

**LastModifiedBy**

The Amazon Resource Name (ARN) of the user who last modified the dataset.

Type: String

Required: No

**LastModifiedDate**

The last modification date and time of the dataset.

Type: Timestamp

Required: No

**PathOptions**

A set of options that defines how DataBrew interprets an Amazon S3
path of the dataset.

Type: [PathOptions](API_PathOptions.md "API_PathOptions.md") object

Required: No

**ResourceArn**

The unique Amazon Resource Name (ARN) for the dataset.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**Source**

The location of the data for the dataset, either Amazon S3 or the AWS Glue Data Catalog.

Type: String

Valid Values: `S3 | DATA-CATALOG | DATABASE`

Required: No

**Tags**

Metadata tags that have been applied to the dataset.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/Dataset.md "../../../goto/SdkForCpp/databrew-2017-07-25/Dataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/Dataset.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/Dataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/Dataset.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/Dataset.md")
