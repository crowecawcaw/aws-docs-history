

# Actions, resources, and condition keys for AWS Private Certificate Authority
<a name="list_acm-pca"></a>

AWS Private Certificate Authority (service prefix: `acm-pca`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/privateca/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/privateca/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/acm-pca/acm-pca.json) for this service.

**Topics**
+ [API operations defined by AWS Private Certificate Authority](#list_acm-pca-operations)
+ [Actions defined by AWS Private Certificate Authority](#list_acm-pca-actions-as-permissions)
+ [Resource types defined by AWS Private Certificate Authority](#list_acm-pca-resources-for-iam-policies)
+ [Condition keys for AWS Private Certificate Authority](#list_acm-pca-policy-keys)

## API operations defined by AWS Private Certificate Authority
<a name="list_acm-pca-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_acm-pca-actions-as-permissions).




- **   CreateCertificateAuthority  **
  - **IAM action:**  [acm-pca:CreateCertificateAuthority](#list_acm-pca-action-CreateCertificateAuthority)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [acm-pca:TagCertificateAuthority](#list_acm-pca-action-TagCertificateAuthority)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCertificateAuthorityAuditReport  **
  - **IAM action:**  [acm-pca:CreateCertificateAuthorityAuditReport](#list_acm-pca-action-CreateCertificateAuthorityAuditReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePermission  **
  - **IAM action:**  [acm-pca:CreatePermission](#list_acm-pca-action-CreatePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteCertificateAuthority  **
  - **IAM action:**  [acm-pca:DeleteCertificateAuthority](#list_acm-pca-action-DeleteCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePermission  **
  - **IAM action:**  [acm-pca:DeletePermission](#list_acm-pca-action-DeletePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeletePolicy  **
  - **IAM action:**  [acm-pca:DeletePolicy](#list_acm-pca-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeCertificateAuthority  **
  - **IAM action:**  [acm-pca:DescribeCertificateAuthority](#list_acm-pca-action-DescribeCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCertificateAuthorityAuditReport  **
  - **IAM action:**  [acm-pca:DescribeCertificateAuthorityAuditReport](#list_acm-pca-action-DescribeCertificateAuthorityAuditReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCertificate  **
  - **IAM action:**  [acm-pca:GetCertificate](#list_acm-pca-action-GetCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCertificateAuthorityCertificate  **
  - **IAM action:**  [acm-pca:GetCertificateAuthorityCertificate](#list_acm-pca-action-GetCertificateAuthorityCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCertificateAuthorityCsr  **
  - **IAM action:**  [acm-pca:GetCertificateAuthorityCsr](#list_acm-pca-action-GetCertificateAuthorityCsr) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **IAM action:**  [acm-pca:GetPolicy](#list_acm-pca-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportCertificateAuthorityCertificate  **
  - **IAM action:**  [acm-pca:ImportCertificateAuthorityCertificate](#list_acm-pca-action-ImportCertificateAuthorityCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   IssueCertificate  **
  - **IAM action:**  [acm-pca:IssueCertificate](#list_acm-pca-action-IssueCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListCertificateAuthorities  **
  - **IAM action:**  [acm-pca:ListCertificateAuthorities](#list_acm-pca-action-ListCertificateAuthorities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPermissions  **
  - **IAM action:**  [acm-pca:ListPermissions](#list_acm-pca-action-ListPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTags  **
  - **IAM action:**  [acm-pca:ListTags](#list_acm-pca-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutPolicy  **
  - **IAM action:**  [acm-pca:PutPolicy](#list_acm-pca-action-PutPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RestoreCertificateAuthority  **
  - **IAM action:**  [acm-pca:RestoreCertificateAuthority](#list_acm-pca-action-RestoreCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeCertificate  **
  - **IAM action:**  [acm-pca:RevokeCertificate](#list_acm-pca-action-RevokeCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagCertificateAuthority  **
  - **IAM action:**  [acm-pca:TagCertificateAuthority](#list_acm-pca-action-TagCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagCertificateAuthority  **
  - **IAM action:**  [acm-pca:UntagCertificateAuthority](#list_acm-pca-action-UntagCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCertificateAuthority  **
  - **IAM action:**  [acm-pca:UpdateCertificateAuthority](#list_acm-pca-action-UpdateCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Private Certificate Authority
<a name="list_acm-pca-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html)  **
  - **Description:** Grants permission to create an AWS Private CA and its associated private key and configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-pca-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-pca-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html)  **
  - **Description:** Grants permission to create an audit report for an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html)  **
  - **Description:** Grants permission to create a permission for an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html)  **
  - **Description:** Grants permission to delete an AWS Private CA and its associated private key and configuration
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html)  **
  - **Description:** Grants permission to delete a permission for an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeletePolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to delete the policy for an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DescribeCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html)  **
  - **Description:** Grants permission to return a list of the configuration and status fields contained in the specified AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthorityAuditReport.html)  **
  - **Description:** Grants permission to return the status and information about an AWS Private CA audit report
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html)  **
  - **Description:** Grants permission to retrieve an AWS Private CA certificate and certificate chain for the certificate authority specified by an ARN
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html)  **
  - **Description:** Grants permission to retrieve an AWS Private CA certificate and certificate chain for the certificate authority specified by an ARN
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCertificateAuthorityCsr](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html)  **
  - **Description:** Grants permission to retrieve an AWS Private CA certificate signing request (CSR) for the certificate-authority specified by an ARN
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html)  **
  - **Description:** Grants permission to retrieve the policy on an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html)  **
  - **Description:** Grants permission to import an SSL/TLS certificate into AWS Private CA for use as the CA certificate of an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html)  **
  - **Description:** Grants permission to issue an AWS Private CA certificate
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [acm-pca:TemplateArn](#list_acm-pca-acm-pca_TemplateArn)<br />[aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html)  **
  - **Description:** Grants permission to retrieve a list of the AWS Private CA certificate authority ARNs, and a summary of the status of each CA in the calling account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPermissions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html)  **
  - **Description:** Grants permission to list the permissions that have been applied to the AWS Private CA certificate authority
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTags](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html)  **
  - **Description:** Grants permission to list the tags that have been applied to the AWS Private CA certificate authority
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html)  **
  - **Description:** Grants permission to put a policy on an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RestoreCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RestoreCertificateAuthority.html)  **
  - **Description:** Grants permission to restore an AWS Private CA from the deleted state to the state it was in when deleted
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html)  **
  - **Description:** Grants permission to revoke a certificate issued by an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html)  **
  - **Description:** Grants permission to add one or more tags to an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-pca-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-pca-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html)  **
  - **Description:** Grants permission to remove one or more tags from an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_acm-pca-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_acm-pca-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html)  **
  - **Description:** Grants permission to update the configuration of an AWS Private CA
  - **Resource types (\*required):** [certificate-authority\*](#list_acm-pca-resource-certificate-authority)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Private Certificate Authority
<a name="list_acm-pca-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [certificate-authority](https://docs.aws.amazon.com/privateca/latest/userguide/api-permissions.html)  | arn:${Partition}:acm-pca:${Region}:${Account}:certificate-authority/${CertificateAuthorityId} | [aws:ResourceTag/${TagKey}](#list_acm-pca-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Private Certificate Authority
<a name="list_acm-pca-policy-keys"></a>

AWS Private Certificate Authority defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [acm-pca:TemplateArn](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-varieties)  | Filters access by the arn of the certificate template used in Issue Certificate request | ARN | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 