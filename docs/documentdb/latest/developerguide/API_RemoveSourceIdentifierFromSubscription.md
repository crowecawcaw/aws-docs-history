# RemoveSourceIdentifierFromSubscription

Removes a source identifier from an existing Amazon DocumentDB event notification
subscription.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**SourceIdentifier**

The source identifier to be removed from the subscription, such as the instance
identifier for an instance, or the name of a security group.

Type: String

Required: Yes

**SubscriptionName**

The name of the Amazon DocumentDB event notification subscription that you want to remove a
source identifier from.

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/cli2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/SdkForCpp/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/SdkForGoV2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/SdkForKotlin/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/boto3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/RemoveSourceIdentifierFromSubscription.md")
