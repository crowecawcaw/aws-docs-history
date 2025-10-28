# DatasetParameter

Represents a dataset parameter that defines type and conditions for a parameter in the
Amazon S3 path of the dataset.

## Contents

###### Note

In the following list, the required parameters are described first.

**Name**

The name of the parameter that is used in the dataset's Amazon S3 path.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**Type**

The type of the dataset parameter, can be one of a 'String', 'Number' or 'Datetime'.

Type: String

Valid Values: `Datetime | Number | String`

Required: Yes

**CreateColumn**

Optional boolean value that defines whether the captured value of this parameter
should be used to create a new column in a dataset.

Type: Boolean

Required: No

**DatetimeOptions**

Additional parameter options such as a format and a timezone. Required for datetime parameters.

Type: [DatetimeOptions](API_DatetimeOptions.md "API_DatetimeOptions.md") object

Required: No

**Filter**

The optional filter expression structure to apply additional matching criteria to the parameter.

Type: [FilterExpression](API_FilterExpression.md "API_FilterExpression.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DatasetParameter.md "../../../goto/SdkForCpp/databrew-2017-07-25/DatasetParameter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DatasetParameter.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DatasetParameter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DatasetParameter.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DatasetParameter.md")
