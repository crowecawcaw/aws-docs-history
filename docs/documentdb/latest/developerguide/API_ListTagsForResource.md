# ListTagsForResource

Lists all tags on an Amazon DocumentDB resource.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**ResourceName**

The Amazon DocumentDB resource with tags to be listed. This value is an Amazon Resource Name
(ARN).

Type: String

Required: Yes

**Filters.Filter.N**

This parameter is not currently supported.

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

## Response Elements

The following element is returned by the service.

**TagList.Tag.N**

A list of one or more tags.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBClusterNotFoundFault**

`DBClusterIdentifier` doesn't refer to an existing cluster.

HTTP Status Code: 404

**DBInstanceNotFound**

`DBInstanceIdentifier` doesn't refer to an existing instance.

HTTP Status Code: 404

**DBSnapshotNotFound**

`DBSnapshotIdentifier` doesn't refer to an existing snapshot.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/ListTagsForResource.md "../../../goto/cli2/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/ListTagsForResource.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/ListTagsForResource.md "../../../goto/SdkForCpp/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/ListTagsForResource.md "../../../goto/SdkForGoV2/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/ListTagsForResource.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/ListTagsForResource.md "../../../goto/SdkForKotlin/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/ListTagsForResource.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/ListTagsForResource.md "../../../goto/boto3/docdb-2014-10-31/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/ListTagsForResource.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/ListTagsForResource.md")
