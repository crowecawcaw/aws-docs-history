# Region

This is a structure that expresses the Region for a given account, consisting of a
name and opt-in status.

## Contents

**RegionName**

The Region code of a given Region (for example, `us-east-1`).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**RegionOptStatus**

One of potential statuses a Region can undergo (Enabled, Enabling, Disabled,
Disabling, Enabled_By_Default).

Type: String

Valid Values: `ENABLED | ENABLING | DISABLING | DISABLED | ENABLED_BY_DEFAULT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/account-2021-02-01/Region.md "../../../goto/SdkForCpp/account-2021-02-01/Region.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/account-2021-02-01/Region.md "../../../goto/SdkForJavaV2/account-2021-02-01/Region.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/account-2021-02-01/Region.md "../../../goto/SdkForRubyV3/account-2021-02-01/Region.md")
