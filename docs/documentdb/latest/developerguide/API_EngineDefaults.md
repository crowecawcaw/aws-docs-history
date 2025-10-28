# EngineDefaults

Contains the result of a successful invocation of the
`DescribeEngineDefaultClusterParameters` operation.

## Contents

###### Note

In the following list, the required parameters are described first.

**DBParameterGroupFamily**

The name of the cluster parameter group family to return the engine parameter information for.

Type: String

Required: No

**Marker**

An optional pagination token provided by a previous request. If this parameter is specified, the response
includes only records beyond the marker, up to the value specified by
`MaxRecords`.

Type: String

Required: No

**Parameters.Parameter.N**

The parameters of a particular cluster parameter group family.

Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/EngineDefaults.md "../../../goto/SdkForCpp/docdb-2014-10-31/EngineDefaults.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/EngineDefaults.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/EngineDefaults.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/EngineDefaults.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/EngineDefaults.md")
