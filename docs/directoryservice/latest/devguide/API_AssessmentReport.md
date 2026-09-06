

# AssessmentReport
<a name="API_AssessmentReport"></a>

Contains the results of validation tests performed against a specific domain controller during a directory assessment.

## Contents
<a name="API_AssessmentReport_Contents"></a>

 ** DomainControllerIp **   <a name="DirectoryService-Type-AssessmentReport-DomainControllerIp"></a>
The IP address of the domain controller that was tested during the assessment.  
Type: String  
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`   
Required: No

 ** Validations **   <a name="DirectoryService-Type-AssessmentReport-Validations"></a>
A list of validation results for different test categories performed against this domain controller.  
Type: Array of [AssessmentValidation](API_AssessmentValidation.md) objects  
Required: No

## See Also
<a name="API_AssessmentReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/AssessmentReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/AssessmentReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/AssessmentReport) 