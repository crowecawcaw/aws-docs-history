# Project

Represents all of the attributes of a DataBrew project.

## Contents

###### Note

In the following list, the required parameters are described first.

**Name**

The unique name of a project.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**RecipeName**

The name of a recipe that will be developed during a project session.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**AccountId**

The ID of the AWS account that owns the project.

Type: String

Length Constraints: Maximum length of 255.

Required: No

**CreateDate**

The date and time that the project was created.

Type: Timestamp

Required: No

**CreatedBy**

The Amazon Resource Name (ARN) of the user who crated the project.

Type: String

Required: No

**DatasetName**

The dataset that the project is to act upon.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**LastModifiedBy**

The Amazon Resource Name (ARN) of the user who last modified the project.

Type: String

Required: No

**LastModifiedDate**

The last modification date and time for the project.

Type: Timestamp

Required: No

**OpenDate**

The date and time when the project was opened.

Type: Timestamp

Required: No

**OpenedBy**

The Amazon Resource Name (ARN) of the user that opened the project for use.

Type: String

Required: No

**ResourceArn**

The Amazon Resource Name (ARN) for the project.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**RoleArn**

The Amazon Resource Name (ARN) of the role that will be assumed for this
project.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**Sample**

The sample size and sampling type to apply to the data. If this parameter isn't
specified, then the sample consists of the first 500 rows from the dataset.

Type: [Sample](API_Sample.md "API_Sample.md") object

Required: No

**Tags**

Metadata tags that have been applied to the project.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/Project.md "../../../goto/SdkForCpp/databrew-2017-07-25/Project.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/Project.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/Project.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/Project.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/Project.md")
