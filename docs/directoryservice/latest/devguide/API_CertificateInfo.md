

# CertificateInfo
<a name="API_CertificateInfo"></a>

Contains general information about a certificate.

## Contents
<a name="API_CertificateInfo_Contents"></a>

 ** CertificateId **   <a name="DirectoryService-Type-CertificateInfo-CertificateId"></a>
The identifier of the certificate.  
Type: String  
Pattern: `^c-[0-9a-f]{10}$`   
Required: No

 ** CommonName **   <a name="DirectoryService-Type-CertificateInfo-CommonName"></a>
The common name for the certificate.  
Type: String  
Required: No

 ** ExpiryDateTime **   <a name="DirectoryService-Type-CertificateInfo-ExpiryDateTime"></a>
The date and time when the certificate will expire.  
Type: Timestamp  
Required: No

 ** State **   <a name="DirectoryService-Type-CertificateInfo-State"></a>
The state of the certificate.  
Type: String  
Valid Values: `Registering | Registered | RegisterFailed | Deregistering | Deregistered | DeregisterFailed`   
Required: No

 ** Type **   <a name="DirectoryService-Type-CertificateInfo-Type"></a>
The function that the registered certificate performs. Valid values include `ClientLDAPS` or `ClientCertAuth`. The default value is `ClientLDAPS`.  
Type: String  
Valid Values: `ClientCertAuth | ClientLDAPS`   
Required: No

## See Also
<a name="API_CertificateInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/CertificateInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/CertificateInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/CertificateInfo) 