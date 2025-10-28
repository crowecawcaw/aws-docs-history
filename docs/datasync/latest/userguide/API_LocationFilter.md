# LocationFilter

Narrow down the list of resources returned by `ListLocations`. For example, to
see all your Amazon S3 locations, create a filter using `"Name":
 "LocationType"`, `"Operator": "Equals"`, and `"Values":
 "S3"`.

For more information, see [filtering resources](query-resources.md "query-resources.md").

## Contents

**Name**

The name of the filter being used. Each API call supports a list of filters that are
available for it (for example, `LocationType` for
`ListLocations`).

Type: String

Valid Values: `LocationUri | LocationType | CreationTime`

Required: Yes

**Operator**

The operator that is used to compare filter values (for example, `Equals` or
`Contains`).

Type: String

Valid Values: `Equals | NotEquals | In | LessThanOrEqual | LessThan | GreaterThanOrEqual | GreaterThan | Contains | NotContains | BeginsWith`

Required: Yes

**Values**

The values that you want to filter for. For example, you might want to display only Amazon
S3 locations.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[0-9a-zA-Z_\ \-\:\*\.\\/\?-]*$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/LocationFilter.md "../../../goto/SdkForCpp/datasync-2018-11-09/LocationFilter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/LocationFilter.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/LocationFilter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/LocationFilter.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/LocationFilter.md")
