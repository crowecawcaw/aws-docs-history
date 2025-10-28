# AlternateContact

A structure that contains the details of an alternate contact associated with an AWS
account

## Contents

**AlternateContactType**

The type of alternate contact.

Type: String

Valid Values: `BILLING | OPERATIONS | SECURITY`

Required: No

**EmailAddress**

The email address associated with this alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 254.

Pattern: `[\s]*[\w+=.#|!&-]+@[\w.-]+\.[\w]+[\s]*`

Required: No

**Name**

The name associated with this alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Required: No

**PhoneNumber**

The phone number associated with this alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 25.

Pattern: `[\s0-9()+-]+`

Required: No

**Title**

The title associated with this alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/account-2021-02-01/AlternateContact.md "../../../goto/SdkForCpp/account-2021-02-01/AlternateContact.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/account-2021-02-01/AlternateContact.md "../../../goto/SdkForJavaV2/account-2021-02-01/AlternateContact.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/account-2021-02-01/AlternateContact.md "../../../goto/SdkForRubyV3/account-2021-02-01/AlternateContact.md")
