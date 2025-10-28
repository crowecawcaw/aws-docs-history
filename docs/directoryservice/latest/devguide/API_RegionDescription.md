# RegionDescription

The replicated Region information for a directory.

## Contents

**DesiredNumberOfDomainControllers**

The desired number of domain controllers in the specified Region for the specified
directory.

Type: Integer

Valid Range: Minimum value of 2.

Required: No

**DirectoryId**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**LastUpdatedDateTime**

The date and time that the Region description was last updated.

Type: Timestamp

Required: No

**LaunchTime**

Specifies when the Region replication began.

Type: Timestamp

Required: No

**RegionName**

The name of the Region. For example, `us-east-1`.

Type: String

Length Constraints: Minimum length of 8. Maximum length of 32.

Required: No

**RegionType**

Specifies whether the Region is the primary Region or an additional Region.

Type: String

Valid Values: `Primary | Additional`

Required: No

**Status**

The status of the replication process for the specified Region.

Type: String

Valid Values: `Requested | Creating | Created | Active | Inoperable | Impaired | Restoring | RestoreFailed | Deleting | Deleted | Failed | Updating`

Required: No

**StatusLastUpdatedDateTime**

The date and time that the Region status was last updated.

Type: Timestamp

Required: No

**VpcSettings**

Contains VPC information for the [CreateDirectory](API_CreateDirectory.md "API_CreateDirectory.md"), [CreateMicrosoftAD](API_CreateMicrosoftAD.md "API_CreateMicrosoftAD.md"), or [CreateHybridAD](API_CreateHybridAD.md "API_CreateHybridAD.md") operation.

Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md "API_DirectoryVpcSettings.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/RegionDescription.md "../../../goto/SdkForCpp/ds-2015-04-16/RegionDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/RegionDescription.md "../../../goto/SdkForJavaV2/ds-2015-04-16/RegionDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/RegionDescription.md "../../../goto/SdkForRubyV3/ds-2015-04-16/RegionDescription.md")
