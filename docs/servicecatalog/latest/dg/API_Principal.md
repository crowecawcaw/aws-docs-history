# Principal

Information about a principal.

## Contents

**PrincipalARN**

The ARN of the principal (user, role, or group). This field allows for an ARN with no `accountID`, with or without wildcard characters if the
`PrincipalType` is an `IAM_PATTERN`.

For more information, review [associate-principal-with-portfolio](../../../cli/latest/reference/servicecatalog/associate-principal-with-portfolio.md#options "../../../cli/latest/reference/servicecatalog/associate-principal-with-portfolio.md#options")
in the AWS CLI Command Reference.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000.

Required: No

**PrincipalType**

The principal type. The supported value is `IAM` if you use a fully defined ARN, or
`IAM_PATTERN` if you use an ARN with no `accountID`, with or without wildcard characters.

Type: String

Valid Values: `IAM | IAM_PATTERN`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/Principal.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/Principal.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/Principal.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/Principal.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/Principal.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/Principal.md")
