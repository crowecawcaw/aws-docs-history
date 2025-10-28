# AddSourceIdentifierToSubscription

Adds a source identifier to an existing event notification
subscription.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**SourceIdentifier**

The identifier of the event source to be added:

- If the source type is an instance, a
  `DBInstanceIdentifier` must be provided.
- If the source type is a security group, a
  `DBSecurityGroupName` must be provided.
- If the source type is a parameter group, a
  `DBParameterGroupName` must be provided.
- If the source type is a snapshot, a
  `DBSnapshotIdentifier` must be provided.

Type: String

Required: Yes

**SubscriptionName**

The name of the Amazon DocumentDB event notification subscription that you
want to add a source identifier to.

Type: String

Required: Yes

## Response Elements

The following element is returned by the service.

**EventSubscription**

Detailed information about an event to which you have subscribed.

Type: [EventSubscription](API_EventSubscription.md "API_EventSubscription.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**SourceNotFound**

The requested source could not be found.

HTTP Status Code: 404

**SubscriptionNotFound**

The subscription name does not exist.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/cli2/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/SdkForCpp/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/SdkForGoV2/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/SdkForKotlin/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/boto3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/AddSourceIdentifierToSubscription.md")
