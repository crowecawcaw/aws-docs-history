

# Certificate
<a name="API_Certificate"></a>

Information about the certificate.

## Contents
<a name="API_Certificate_Contents"></a>

 ** CertificateId **   <a name="DirectoryService-Type-Certificate-CertificateId"></a>
The identifier of the certificate.  
Type: String  
Pattern: `^c-[0-9a-f]{10}$`   
Required: No

 ** ClientCertAuthSettings **   <a name="DirectoryService-Type-Certificate-ClientCertAuthSettings"></a>
A `ClientCertAuthSettings` object that contains client certificate authentication settings.  
Type: [ClientCertAuthSettings](API_ClientCertAuthSettings.md) object  
Required: No

 ** CommonName **   <a name="DirectoryService-Type-Certificate-CommonName"></a>
The common name for the certificate.  
Type: String  
Required: No

 ** ExpiryDateTime **   <a name="DirectoryService-Type-Certificate-ExpiryDateTime"></a>
The date and time when the certificate will expire.  
Type: Timestamp  
Required: No

 ** RegisteredDateTime **   <a name="DirectoryService-Type-Certificate-RegisteredDateTime"></a>
The date and time that the certificate was registered.  
Type: Timestamp  
Required: No

 ** State **   <a name="DirectoryService-Type-Certificate-State"></a>
The state of the certificate.  
Type: String  
Valid Values: `Registering | Registered | RegisterFailed | Deregistering | Deregistered | DeregisterFailed`   
Required: No

 ** StateReason **   <a name="DirectoryService-Type-Certificate-StateReason"></a>
Describes a state change for the certificate.  
Type: String  
Required: No

 ** Type **   <a name="DirectoryService-Type-Certificate-Type"></a>
The function that the registered certificate performs. Valid values include `ClientLDAPS` or `ClientCertAuth`. The default value is `ClientLDAPS`.  
Type: String  
Valid Values: `ClientCertAuth | ClientLDAPS`   
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/Certificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/Certificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/Certificate) 