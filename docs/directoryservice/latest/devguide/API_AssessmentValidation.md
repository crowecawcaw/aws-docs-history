

# AssessmentValidation
<a name="API_AssessmentValidation"></a>

Contains information about a specific validation test performed during a directory assessment.

## Contents
<a name="API_AssessmentValidation_Contents"></a>

 ** Category **   <a name="DirectoryService-Type-AssessmentValidation-Category"></a>
The category of the validation test.  
Type: String  
Required: No

 ** LastUpdateDateTime **   <a name="DirectoryService-Type-AssessmentValidation-LastUpdateDateTime"></a>
The date and time when the validation test was completed or last updated.  
Type: Timestamp  
Required: No

 ** Name **   <a name="DirectoryService-Type-AssessmentValidation-Name"></a>
The name of the specific validation test performed within the category.  
Type: String  
Required: No

 ** StartTime **   <a name="DirectoryService-Type-AssessmentValidation-StartTime"></a>
The date and time when the validation test was started.  
Type: Timestamp  
Required: No

 ** Status **   <a name="DirectoryService-Type-AssessmentValidation-Status"></a>
The result status of the validation test. Valid values include `SUCCESS`, `FAILED`, `PENDING`, and `IN_PROGRESS`.  
Type: String  
Required: No

 ** StatusCode **   <a name="DirectoryService-Type-AssessmentValidation-StatusCode"></a>
A detailed status code providing additional information about the validation result.  
Type: String  
Required: No

 ** StatusReason **   <a name="DirectoryService-Type-AssessmentValidation-StatusReason"></a>
A human-readable description of the validation result, including any error details or recommendations.  
Type: String  
Required: No

## See Also
<a name="API_AssessmentValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/AssessmentValidation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/AssessmentValidation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/AssessmentValidation) 