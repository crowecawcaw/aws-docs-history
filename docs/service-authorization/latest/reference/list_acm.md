

# Actions, resources, and condition keys for AWS Certificate Manager
<a name="list_acm"></a>

AWS Certificate Manager (service prefix: `acm`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/acm/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/acm/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/acm/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/acm/acm.json) for this service.

**Topics**
+ [API operations defined by AWS Certificate Manager](#list_acm-operations)
+ [Actions defined by AWS Certificate Manager](#list_acm-actions-as-permissions)
+ [Resource types defined by AWS Certificate Manager](#list_acm-resources-for-iam-policies)
+ [Condition keys for AWS Certificate Manager](#list_acm-policy-keys)

## API operations defined by AWS Certificate Manager
<a name="list_acm-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_acm-actions-as-permissions).




- **   AddTagsToCertificate  **
  - **IAM action:**  [acm:AddTagsToCertificate](#list_acm-action-AddTagsToCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteCertificate  **
  - **IAM action:**  [acm:DeleteCertificate](#list_acm-action-DeleteCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCertificate  **
  - **IAM action:**  [acm:DescribeCertificate](#list_acm-action-DescribeCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ExportCertificate  **
  - **IAM action:**  [acm:ExportCertificate](#list_acm-action-ExportCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountConfiguration  **
  - **IAM action:**  [acm:GetAccountConfiguration](#list_acm-action-GetAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCertificate  **
  - **IAM action:**  [acm:GetCertificate](#list_acm-action-GetCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportCertificate  **
  - **IAM action:**  [acm:AddTagsToCertificate](#list_acm-action-AddTagsToCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [acm:ImportCertificate](#list_acm-action-ImportCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ListCertificateDomainValidations  **
  - **IAM action:**  [acm:ListCertificateDomainValidations](#list_acm-action-ListCertificateDomainValidations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCertificates  **
  - **IAM action:**  [acm:ListCertificates](#list_acm-action-ListCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForCertificate  **
  - **IAM action:**  [acm:ListTagsForCertificate](#list_acm-action-ListTagsForCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [acm:ListTagsForResource](#list_acm-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutAccountConfiguration  **
  - **IAM action:**  [acm:PutAccountConfiguration](#list_acm-action-PutAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromCertificate  **
  - **IAM action:**  [acm:RemoveTagsFromCertificate](#list_acm-action-RemoveTagsFromCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   RenewCertificate  **
  - **IAM action:**  [acm:RenewCertificate](#list_acm-action-RenewCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RequestCertificate  **
  - **IAM action:**  [acm:AddTagsToCertificate](#list_acm-action-AddTagsToCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [acm:RequestCertificate](#list_acm-action-RequestCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ResendValidationEmail  **
  - **IAM action:**  [acm:ResendValidationEmail](#list_acm-action-ResendValidationEmail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeCertificate  **
  - **IAM action:**  [acm:RevokeCertificate](#list_acm-action-RevokeCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchCertificates  **
  - **IAM action:**  [acm:SearchCertificates](#list_acm-action-SearchCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [acm:TagResource](#list_acm-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [acm:UntagResource](#list_acm-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCertificateOptions  **
  - **IAM action:**  [acm:UpdateCertificateOptions](#list_acm-action-UpdateCertificateOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Certificate Manager
<a name="list_acm-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTagsToCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_AddTagsToCertificate.html)  **
  - **Description:** Grants permission to add one or more tags to a certificate
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [acm:CertificateKeyPairOrigin](#list_acm-acm_CertificateKeyPairOrigin)<br />[aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [CreateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeDomainValidation.html)  **
  - **Description:** Grants permission to create an ACME domain validation
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeEndpoint.html)  **
  - **Description:** Grants permission to create an ACME endpoint
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeExternalAccountBinding.html)  **
  - **Description:** Grants permission to create an ACME external account binding
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeDomainValidation.html)  **
  - **Description:** Grants permission to delete an ACME domain validation
  - **Resource types (\*required):** [acme-domain-validation\*](#list_acm-resource-acme-domain-validation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeEndpoint.html)  **
  - **Description:** Grants permission to delete an ACME endpoint
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeExternalAccountBinding.html)  **
  - **Description:** Grants permission to delete an ACME external account binding
  - **Resource types (\*required):** [acme-external-account-binding\*](#list_acm-resource-acme-external-account-binding)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteCertificate.html)  **
  - **Description:** Grants permission to delete a certificate and its associated private key
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [acm:CertificateKeyPairOrigin](#list_acm-acm_CertificateKeyPairOrigin)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAcmeAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeAccount.html)  **
  - **Description:** Grants permission to retrieve details of an ACME account
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeDomainValidation.html)  **
  - **Description:** Grants permission to retrieve details of an ACME domain validation
  - **Resource types (\*required):** [acme-domain-validation\*](#list_acm-resource-acme-domain-validation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeEndpoint.html)  **
  - **Description:** Grants permission to retrieve details of an ACME endpoint
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeExternalAccountBinding.html)  **
  - **Description:** Grants permission to retrieve details of an ACME external account binding
  - **Resource types (\*required):** [acme-external-account-binding\*](#list_acm-resource-acme-external-account-binding)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html)  **
  - **Description:** Grants permission to retreive a certificates and its metadata
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ExportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExportCertificate.html)  **
  - **Description:** Grants permission to export an exportable certificate for use anywhere
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [acm:DomainNames](#list_acm-acm_DomainNames)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAccountConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetAccountConfiguration.html)  **
  - **Description:** Grants permission to retrieve account level configuration from AWS Certificate Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAcmeExternalAccountBindingCredentials](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetAcmeExternalAccountBindingCredentials.html)  **
  - **Description:** Grants permission to retrieve credentials for an ACME external account binding
  - **Resource types (\*required):** [acme-external-account-binding\*](#list_acm-resource-acme-external-account-binding)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetCertificate.html)  **
  - **Description:** Grants permission to retrieve a certificate and certificate chain for a certificate ARN
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ImportCertificate.html)  **
  - **Description:** Grants permission to import a 3rd party certificate into AWS Certificate Manager (ACM)
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Write

- **   [ListAcmeAccounts](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeAccounts.html)  **
  - **Description:** Grants permission to list ACME accounts
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAcmeDomainValidations](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeDomainValidations.html)  **
  - **Description:** Grants permission to list ACME domain validations
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAcmeEndpoints](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeEndpoints.html)  **
  - **Description:** Grants permission to list ACME endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAcmeExternalAccountBindings](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeExternalAccountBindings.html)  **
  - **Description:** Grants permission to list ACME external account bindings
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCertificateDomainValidations](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificateDomainValidations.html)  **
  - **Description:** Grants permission to list domain validation methods for a certificate
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html)  **
  - **Description:** Grants permission to retrieve a list of certificates for specific certificate parameters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html)  **
  - **Description:** Grants permission to lists the tags that have been associated with a certificate
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [acme-domain-validation](#list_acm-resource-acme-domain-validation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [acme-endpoint](#list_acm-resource-acme-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [acme-external-account-binding](#list_acm-resource-acme-external-account-binding) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutAccountConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_PutAccountConfiguration.html)  **
  - **Description:** Grants permission to update account level configuration in AWS Certificate Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveTagsFromCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RemoveTagsFromCertificate.html)  **
  - **Description:** Grants permission to remove one or more tags from a certificate
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [RenewCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RenewCertificate.html)  **
  - **Description:** Grants permission to renew an eligible private certificate
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html)  **
  - **Description:** Grants permission to requests a public or private certificate
  - **Resource types (\*required):** 
  - **Condition keys:** [acm:CertificateAuthority](#list_acm-acm_CertificateAuthority)<br />[acm:CertificateKeyPairOrigin](#list_acm-acm_CertificateKeyPairOrigin)<br />[acm:CertificateTransparencyLogging](#list_acm-acm_CertificateTransparencyLogging)<br />[acm:DomainNames](#list_acm-acm_DomainNames)<br />[acm:Export](#list_acm-acm_Export)<br />[acm:KeyAlgorithm](#list_acm-acm_KeyAlgorithm)<br />[acm:ValidationMethod](#list_acm-acm_ValidationMethod)<br />[aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Write

- **   [ResendValidationEmail](https://docs.aws.amazon.com/acm/latest/APIReference/API_ResendValidationEmail.html)  **
  - **Description:** Grants permission to resend an email to request domain ownership validation
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeAcmeAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeAccount.html)  **
  - **Description:** Grants permission to revoke an ACME account
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeExternalAccountBinding.html)  **
  - **Description:** Grants permission to revoke an ACME external account binding
  - **Resource types (\*required):** [acme-external-account-binding\*](#list_acm-resource-acme-external-account-binding)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeCertificate.html)  **
  - **Description:** Grants permission to revoke an exportable certificate
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [acm:CertificateKeyPairOrigin](#list_acm-acm_CertificateKeyPairOrigin)<br />[acm:DomainNames](#list_acm-acm_DomainNames)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_SearchCertificates.html)  **
  - **Description:** Grants permission to retrieve a list of certificates matching search criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [acme-domain-validation](#list_acm-resource-acme-domain-validation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Resource types (\*required):** [acme-endpoint](#list_acm-resource-acme-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Resource types (\*required):** [acme-external-account-binding](#list_acm-resource-acme-external-account-binding) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [acme-domain-validation](#list_acm-resource-acme-domain-validation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Resource types (\*required):** [acme-endpoint](#list_acm-resource-acme-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Resource types (\*required):** [acme-external-account-binding](#list_acm-resource-acme-external-account-binding) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeDomainValidation.html)  **
  - **Description:** Grants permission to update an ACME domain validation
  - **Resource types (\*required):** [acme-domain-validation\*](#list_acm-resource-acme-domain-validation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeEndpoint.html)  **
  - **Description:** Grants permission to update an ACME endpoint
  - **Resource types (\*required):** [acme-endpoint\*](#list_acm-resource-acme-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateCertificate.html)  **
  - **Description:** Grants permission to update a certificate
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [acm:CertificateKeyPairOrigin](#list_acm-acm_CertificateKeyPairOrigin)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCertificateOptions](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateCertificateOptions.html)  **
  - **Description:** Grants permission to update a certificate configuration. Use this to specify whether to opt in to or out of certificate transparency logging or to update the certificate domain validation method
  - **Resource types (\*required):** [certificate\*](#list_acm-resource-certificate)
  - **Condition keys:** [acm:ValidationMethod](#list_acm-acm_ValidationMethod)<br />[aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Certificate Manager
<a name="list_acm-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [acme-domain-validation](https://docs.aws.amazon.com/acm/latest/userguide/acm-acme-domain-validation.html)  | arn:${Partition}:acm:${Region}:${Account}:acme-endpoint/${AcmeEndpointId}/acme-domain-validation/${AcmeDomainValidationId} | [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_) | 
|  [acme-endpoint](https://docs.aws.amazon.com/acm/latest/userguide/acm-acme-endpoints.html)  | arn:${Partition}:acm:${Region}:${Account}:acme-endpoint/${AcmeEndpointId} | [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_) | 
|  [acme-external-account-binding](https://docs.aws.amazon.com/acm/latest/userguide/acm-acme-eab.html)  | arn:${Partition}:acm:${Region}:${Account}:acme-endpoint/${AcmeEndpointId}/acme-external-account-binding/${ExternalAccountBindingId} | [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_) | 
|  [certificate](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-acm-cert)  | arn:${Partition}:acm:${Region}:${Account}:certificate/${CertificateId} | [aws:ResourceTag/${TagKey}](#list_acm-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Certificate Manager
<a name="list_acm-policy-keys"></a>

AWS Certificate Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [acm:CertificateAuthority](https://docs.aws.amazon.com/acm/latest/userguide/security-iam.html)  | Filters access by certificateAuthority in the request. Can be used to restrict which Certificate Authorites certificates can be issued from | String | 
|   [acm:CertificateKeyPairOrigin](https://docs.aws.amazon.com/acm/latest/userguide/security-iam.html)  | Filters access by certificateKeyPairOrigin in the request. Can be used to restrict which certificate provisioning paths are permitted | String | 
|   [acm:CertificateTransparencyLogging](https://docs.aws.amazon.com/acm/latest/userguide/security-iam.html)  | Filters access by certificateTransparencyLogging option in the request. Default 'ENABLED' if no key is present in the request | String | 
|   [acm:DomainNames](https://docs.aws.amazon.com/acm/latest/userguide/security-iam.html)  | Filters access by domainNames in the request. This key can be used to restrict which domains can be in certificate requests | ArrayOfString | 
|   [acm:Export](https://docs.aws.amazon.com/acm/latest/userguide/security-iam.html)  | Filters access by the export option in the request. Can be used to restrict creation of certificates that can be exported | String | 
|   [acm:KeyAlgorithm](https://docs.aws.amazon.com/acm/latest/userguide/security-iam.html)  | Filters access by keyAlgorithm in the request | String | 
|   [acm:ValidationMethod](https://docs.aws.amazon.com/acm/latest/userguide/security-iam.html)  | Filters access by validationMethod in the request. Default 'EMAIL' if no key is present in the request | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 