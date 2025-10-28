# ServerlessV2FeaturesSupport

Specifies any Amazon DocumentDB Serverless properties or limits that differ between Amazon DocumentDB engine versions.
You can test the values of this attribute when deciding which Amazon DocumentDB version to use in a new or upgraded cluster.
You can also retrieve the version of an existing cluster and check whether that version supports certain Amazon DocumentDB Serverless features before you attempt to use those features.

## Contents

###### Note

In the following list, the required parameters are described first.

**MaxCapacity**

The maximum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster.
You can specify DCU values in half-step increments, such as 32, 32.5, 33, and so on.

Type: Double

Required: No

**MinCapacity**

The minimum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster.
You can specify DCU values in half-step increments, such as 8, 8.5, 9, and so on.

Type: Double

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/ServerlessV2FeaturesSupport.md "../../../goto/SdkForCpp/docdb-2014-10-31/ServerlessV2FeaturesSupport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/ServerlessV2FeaturesSupport.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/ServerlessV2FeaturesSupport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/ServerlessV2FeaturesSupport.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/ServerlessV2FeaturesSupport.md")
