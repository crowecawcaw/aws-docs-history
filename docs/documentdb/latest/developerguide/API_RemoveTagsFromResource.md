# RemoveTagsFromResource

Removes metadata tags from an Amazon DocumentDB resource.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**ResourceName**

The Amazon DocumentDB resource that the tags are removed from. This value is an Amazon Resource
Name (ARN).

Type: String

Required: Yes

**TagKeys.member.N**

The tag key (name) of the tag to be removed.

Type: Array of strings

Required: Yes

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/cli2/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/SdkForCpp/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/SdkForGoV2/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/SdkForKotlin/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/boto3/docdb-2014-10-31/RemoveTagsFromResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/RemoveTagsFromResource.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/RemoveTagsFromResource.md")
