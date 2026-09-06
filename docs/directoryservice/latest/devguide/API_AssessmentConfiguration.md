

# AssessmentConfiguration
<a name="API_AssessmentConfiguration"></a>

Contains configuration parameters required to perform a directory assessment.

## Contents
<a name="API_AssessmentConfiguration_Contents"></a>

 ** CustomerDnsIps **   <a name="DirectoryService-Type-AssessmentConfiguration-CustomerDnsIps"></a>
A list of IP addresses for the DNS servers or domain controllers in your self-managed AD that are tested during the assessment.  
Type: Array of strings  
Array Members: Fixed number of 2 items.  
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`   
Required: Yes

 ** DnsName **   <a name="DirectoryService-Type-AssessmentConfiguration-DnsName"></a>
The fully qualified domain name (FQDN) of the self-managed AD domain to assess.  
Type: String  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`   
Required: Yes

 ** InstanceIds **   <a name="DirectoryService-Type-AssessmentConfiguration-InstanceIds"></a>
The identifiers of the self-managed instances with SSM that are used to perform connectivity and validation tests.  
Type: Array of strings  
Array Members: Fixed number of 2 items.  
Pattern: `^(i-[0-9a-f]{8}|i-[0-9a-f]{17}|mi-[0-9a-f]{8}|mi-[0-9a-f]{17})$`   
Required: Yes

 ** VpcSettings **   <a name="DirectoryService-Type-AssessmentConfiguration-VpcSettings"></a>
Contains VPC information for the [CreateDirectory](API_CreateDirectory.md), [CreateMicrosoftAD](API_CreateMicrosoftAD.md), or [CreateHybridAD](API_CreateHybridAD.md) operation.  
Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md) object  
Required: Yes

 ** SecurityGroupIds **   <a name="DirectoryService-Type-AssessmentConfiguration-SecurityGroupIds"></a>
By default, the service attaches a security group to allow network access to the self-managed nodes in your Amazon VPC. You can optionally supply your own security group that allows network traffic to and from your self-managed domain controllers outside of your Amazon VPC.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Pattern: `^(sg-[0-9a-f]{8}|sg-[0-9a-f]{17})$`   
Required: No

## See Also
<a name="API_AssessmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/AssessmentConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/AssessmentConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/AssessmentConfiguration) 