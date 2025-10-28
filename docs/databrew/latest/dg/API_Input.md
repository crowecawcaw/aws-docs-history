# Input

Represents information on how DataBrew can find data, in either the AWS Glue Data Catalog or
Amazon S3.

## Contents

###### Note

In the following list, the required parameters are described first.

**DatabaseInputDefinition**

Connection information for dataset input files stored in a database.

Type: [DatabaseInputDefinition](API_DatabaseInputDefinition.md "API_DatabaseInputDefinition.md") object

Required: No

**DataCatalogInputDefinition**

The AWS Glue Data Catalog parameters for the data.

Type: [DataCatalogInputDefinition](API_DataCatalogInputDefinition.md "API_DataCatalogInputDefinition.md") object

Required: No

**Metadata**

Contains additional resource information needed for specific datasets.

Type: [Metadata](API_Metadata.md "API_Metadata.md") object

Required: No

**S3InputDefinition**

The Amazon S3 location where the data is stored.

Type: [S3Location](API_S3Location.md "API_S3Location.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/Input.md "../../../goto/SdkForCpp/databrew-2017-07-25/Input.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/Input.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/Input.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/Input.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/Input.md")
