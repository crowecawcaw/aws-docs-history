# Computer

Contains information about a computer account in a directory.

## Contents

**ComputerAttributes**

An array of [Attribute](API_Attribute.md "API_Attribute.md") objects containing the LDAP attributes that belong to the
computer account.

Type: Array of [Attribute](API_Attribute.md "API_Attribute.md") objects

Required: No

**ComputerId**

The identifier of the computer.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[&\w+-.@]+`

Required: No

**ComputerName**

The computer name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 15.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/Computer.md "../../../goto/SdkForCpp/ds-2015-04-16/Computer.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/Computer.md "../../../goto/SdkForJavaV2/ds-2015-04-16/Computer.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/Computer.md "../../../goto/SdkForRubyV3/ds-2015-04-16/Computer.md")
