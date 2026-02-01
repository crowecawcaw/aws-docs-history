# DescribeEventCategories

Displays a list of categories for all event source types, or, if specified, for a
specified source type.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**Filters.Filter.N**

This parameter is not currently supported.

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

**SourceType**

The type of source that is generating the events.

Valid values: `db-instance`, `db-parameter-group`, `db-security-group`

Type: String

Required: No

## Response Elements

The following element is returned by the service.

**EventCategoriesMapList.EventCategoriesMap.N**

A list of event category maps.

Type: Array of [EventCategoriesMap](API_EventCategoriesMap.md "API_EventCategoriesMap.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/cli2/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/SdkForCpp/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/boto3/docdb-2014-10-31/DescribeEventCategories.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeEventCategories.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeEventCategories.md")
