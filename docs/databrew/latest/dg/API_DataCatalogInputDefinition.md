# DataCatalogInputDefinition

Represents how metadata stored in the AWS Glue Data Catalog is defined in a DataBrew
dataset.

## Contents

###### Note

In the following list, the required parameters are described first.

**DatabaseName**

The name of a database in the Data Catalog.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**TableName**

The name of a database table in the Data Catalog. This table corresponds to a DataBrew
dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**CatalogId**

The unique identifier of the AWS account that holds the Data Catalog that stores the
data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**TempDirectory**

Represents an Amazon location where DataBrew can store intermediate results.

Type: [S3Location](API_S3Location.md "API_S3Location.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DataCatalogInputDefinition.md "../../../goto/SdkForCpp/databrew-2017-07-25/DataCatalogInputDefinition.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DataCatalogInputDefinition.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DataCatalogInputDefinition.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DataCatalogInputDefinition.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DataCatalogInputDefinition.md")
