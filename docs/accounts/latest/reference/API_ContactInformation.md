# ContactInformation

Contains the details of the primary contact information associated with an
AWS account.

## Contents

**AddressLine1**

The first line of the primary contact address.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 60.

Required: Yes

**City**

The city of the primary contact address.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: Yes

**CountryCode**

The ISO-3166 two-letter country code for the primary contact address.

Type: String

Length Constraints: Fixed length of 2.

Required: Yes

**FullName**

The full name of the primary contact address.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: Yes

**PhoneNumber**

The phone number of the primary contact information. The number will be validated and,
in some countries, checked for activation.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 20.

Pattern: `[+][\s0-9()-]+`

Required: Yes

**PostalCode**

The postal code of the primary contact address.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 20.

Required: Yes

**AddressLine2**

The second line of the primary contact address, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 60.

Required: No

**AddressLine3**

The third line of the primary contact address, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 60.

Required: No

**CompanyName**

The name of the company associated with the primary contact information, if
any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**DistrictOrCounty**

The district or county of the primary contact address, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**StateOrRegion**

The state or region of the primary contact address. If the mailing address is within the United States (US), the
value in this field can be either a two character state code (for example, `NJ`) or the full state name
(for example, `New Jersey`). This field is required in the following countries: `US`,
`CA`, `GB`, `DE`, `JP`, `IN`,
and `BR`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**WebsiteUrl**

The URL of the website associated with the primary contact information, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/account-2021-02-01/ContactInformation.md "../../../goto/SdkForCpp/account-2021-02-01/ContactInformation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/account-2021-02-01/ContactInformation.md "../../../goto/SdkForJavaV2/account-2021-02-01/ContactInformation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/account-2021-02-01/ContactInformation.md "../../../goto/SdkForRubyV3/account-2021-02-01/ContactInformation.md")
