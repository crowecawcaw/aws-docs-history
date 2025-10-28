# AssessmentReport

Contains the results of validation tests performed against a specific domain
controller during a directory assessment.

## Contents

**DomainControllerIp**

The IP address of the domain controller that was tested during the assessment.

Type: String

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**Validations**

A list of validation results for different test categories performed against this
domain controller.

Type: Array of [AssessmentValidation](API_AssessmentValidation.md "API_AssessmentValidation.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/AssessmentReport.md "../../../goto/SdkForCpp/ds-2015-04-16/AssessmentReport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/AssessmentReport.md "../../../goto/SdkForJavaV2/ds-2015-04-16/AssessmentReport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/AssessmentReport.md "../../../goto/SdkForRubyV3/ds-2015-04-16/AssessmentReport.md")
