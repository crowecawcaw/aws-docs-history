

# AssessmentSummary
<a name="API_AssessmentSummary"></a>

Contains summary information about a directory assessment, providing a high-level overview without detailed validation results.

## Contents
<a name="API_AssessmentSummary_Contents"></a>

 ** AssessmentId **   <a name="DirectoryService-Type-AssessmentSummary-AssessmentId"></a>
The unique identifier of the directory assessment.  
Type: String  
Pattern: `^da-[0-9a-f]{18}$`   
Required: No

 ** CustomerDnsIps **   <a name="DirectoryService-Type-AssessmentSummary-CustomerDnsIps"></a>
The IP addresses of the DNS servers or domain controllers in your self-managed AD environment.  
Type: Array of strings  
Array Members: Fixed number of 2 items.  
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`   
Required: No

 ** DirectoryId **   <a name="DirectoryService-Type-AssessmentSummary-DirectoryId"></a>
The identifier of the directory associated with this assessment.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** DnsName **   <a name="DirectoryService-Type-AssessmentSummary-DnsName"></a>
The fully qualified domain name (FQDN) of the Active Directory domain being assessed.  
Type: String  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`   
Required: No

 ** LastUpdateDateTime **   <a name="DirectoryService-Type-AssessmentSummary-LastUpdateDateTime"></a>
The date and time when the assessment status was last updated.  
Type: Timestamp  
Required: No

 ** ReportType **   <a name="DirectoryService-Type-AssessmentSummary-ReportType"></a>
The type of assessment report generated. Valid values include `CUSTOMER` and `SYSTEM`.  
Type: String  
Required: No

 ** StartTime **   <a name="DirectoryService-Type-AssessmentSummary-StartTime"></a>
The date and time when the assessment was initiated.  
Type: Timestamp  
Required: No

 ** Status **   <a name="DirectoryService-Type-AssessmentSummary-Status"></a>
The current status of the assessment. Valid values include `SUCCESS`, `FAILED`, `PENDING`, and `IN_PROGRESS`.  
Type: String  
Required: No

## See Also
<a name="API_AssessmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/AssessmentSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/AssessmentSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/AssessmentSummary) 