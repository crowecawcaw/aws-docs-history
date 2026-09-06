

# Assessment
<a name="API_Assessment"></a>

Contains detailed information about a directory assessment, including configuration parameters, status, and validation results.

## Contents
<a name="API_Assessment_Contents"></a>

 ** AssessmentId **   <a name="DirectoryService-Type-Assessment-AssessmentId"></a>
The unique identifier of the directory assessment.  
Type: String  
Pattern: `^da-[0-9a-f]{18}$`   
Required: No

 ** CustomerDnsIps **   <a name="DirectoryService-Type-Assessment-CustomerDnsIps"></a>
The IP addresses of the DNS servers or domain controllers in your self-managed AD environment.  
Type: Array of strings  
Array Members: Fixed number of 2 items.  
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`   
Required: No

 ** DirectoryId **   <a name="DirectoryService-Type-Assessment-DirectoryId"></a>
The identifier of the directory associated with this assessment.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** DnsName **   <a name="DirectoryService-Type-Assessment-DnsName"></a>
The fully qualified domain name (FQDN) of the Active Directory domain being assessed.  
Type: String  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`   
Required: No

 ** LastUpdateDateTime **   <a name="DirectoryService-Type-Assessment-LastUpdateDateTime"></a>
The date and time when the assessment status was last updated.  
Type: Timestamp  
Required: No

 ** ReportType **   <a name="DirectoryService-Type-Assessment-ReportType"></a>
The type of assessment report generated. Valid values are `CUSTOMER` and `SYSTEM`.  
Type: String  
Required: No

 ** SecurityGroupIds **   <a name="DirectoryService-Type-Assessment-SecurityGroupIds"></a>
The security groups identifiers attached to the network interfaces.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Pattern: `^(sg-[0-9a-f]{8}|sg-[0-9a-f]{17})$`   
Required: No

 ** SelfManagedInstanceIds **   <a name="DirectoryService-Type-Assessment-SelfManagedInstanceIds"></a>
The identifiers of the self-managed AD instances used to perform the assessment.  
Type: Array of strings  
Array Members: Fixed number of 2 items.  
Pattern: `^(i-[0-9a-f]{8}|i-[0-9a-f]{17}|mi-[0-9a-f]{8}|mi-[0-9a-f]{17})$`   
Required: No

 ** StartTime **   <a name="DirectoryService-Type-Assessment-StartTime"></a>
The date and time when the assessment was initiated.  
Type: Timestamp  
Required: No

 ** Status **   <a name="DirectoryService-Type-Assessment-Status"></a>
The current status of the assessment. Valid values include `SUCCESS`, `FAILED`, `PENDING`, and `IN_PROGRESS`.  
Type: String  
Required: No

 ** StatusCode **   <a name="DirectoryService-Type-Assessment-StatusCode"></a>
A detailed status code providing additional information about the assessment state.  
Type: String  
Required: No

 ** StatusReason **   <a name="DirectoryService-Type-Assessment-StatusReason"></a>
A human-readable description of the current assessment status, including any error details or progress information.  
Type: String  
Required: No

 ** SubnetIds **   <a name="DirectoryService-Type-Assessment-SubnetIds"></a>
A list of subnet identifiers in the Amazon VPC in which the hybrid directory is created.  
Type: Array of strings  
Pattern: `^(subnet-[0-9a-f]{8}|subnet-[0-9a-f]{17})$`   
Required: No

 ** Version **   <a name="DirectoryService-Type-Assessment-Version"></a>
The version of the assessment framework used to evaluate your self-managed AD environment.  
Type: String  
Required: No

 ** VpcId **   <a name="DirectoryService-Type-Assessment-VpcId"></a>
Contains Amazon VPC information for the `StartADAssessment` operation.   
Type: String  
Pattern: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`   
Required: No

## See Also
<a name="API_Assessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/Assessment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/Assessment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/Assessment) 