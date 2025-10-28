# IpRouteInfo

Information about one or more IP address blocks.

## Contents

**AddedDateTime**

The date and time the address block was added to the directory.

Type: Timestamp

Required: No

**CidrIp**

IP address block in the [IpRoute](API_IpRoute.md "API_IpRoute.md").

Type: String

Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([1-9]|[1-2][0-9]|3[0-2]))$`

Required: No

**CidrIpv6**

IPv6 address block in the [IpRoute](API_IpRoute.md "API_IpRoute.md").

Type: String

Pattern: `^((([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,7}:)|(([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2})|(([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3})|(([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4})|(([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5})|([0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}))|(:((:[0-9a-fA-F]{1,4}){1,7}|:)))\/(12[0-8]|1[01][0-9]|[1-9]?[0-9])$`

Required: No

**Description**

Description of the [IpRouteInfo](API_IpRouteInfo.md "API_IpRouteInfo.md").

Type: String

Length Constraints: Minimum length of 0. Maximum length of 128.

Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

Required: No

**DirectoryId**

Identifier (ID) of the directory associated with the IP addresses.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**IpRouteStatusMsg**

The status of the IP address block.

Type: String

Valid Values: `Adding | Added | Removing | Removed | AddFailed | RemoveFailed`

Required: No

**IpRouteStatusReason**

The reason for the IpRouteStatusMsg.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/IpRouteInfo.md "../../../goto/SdkForCpp/ds-2015-04-16/IpRouteInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/IpRouteInfo.md "../../../goto/SdkForJavaV2/ds-2015-04-16/IpRouteInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/IpRouteInfo.md "../../../goto/SdkForRubyV3/ds-2015-04-16/IpRouteInfo.md")
