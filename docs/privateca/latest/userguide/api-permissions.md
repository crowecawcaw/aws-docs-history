

# AWS Private CA API operations and permissions
<a name="api-permissions"></a>

When you set up access control and permissions policies that you plan to attach to an IAM identity (identity-based policies), use the following table as a reference. The first column in the table lists each AWS Private CA API operation. You specify actions in a policy's `Action` element. The remaining columns provide the additional information.


| AWS Private CA API operations | Required permissions | Resources | 
| --- | --- | --- | 
| [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) | `acm-pca:CreateCertificateAuthority`<br />`acm-pca:TagCertificateAuthority` (Only required when creating a CA with tags.) | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html) | `acm-pca:CreateCertificateAuthorityAuditReport` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [CreatePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html) | acm-pca:CreatePermission | arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}} | 
| [DeleteCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html) | `acm-pca:DeleteCertificateAuthority` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [DeletePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html) | acm-pca:DeletePermission | arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}} | 
| [DeletePolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html) | acm-pca:DeletePolicy | arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}} | 
| [DescribeCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html) | `acm-pca:DescribeCertificateAuthority` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [DescribeCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthorityAuditReport.html) | `acm-pca:DescribeCertificateAuthorityAuditReport` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [GetCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html) | `acm-pca:GetCertificate` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [GetCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html) | `acm-pca:GetCertificateAuthorityCertificate` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [GetCertificateAuthorityCsr](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html) | `acm-pca:GetCertificateAuthorityCsr` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [GetPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html) | acm-pca:GetPolicy | arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}} | 
| [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html) | `acm-pca:ImportCertificateAuthorityCertificate` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) | `acm-pca:IssueCertificate` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html) | `acm-pca:ListCertificateAuthorities` | N/A | 
| [ListPermissions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html) | acm-pca:ListPermissions | arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}} | 
| [ListTags](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html) | `acm-pca:ListTags` | N/A | 
| [PutPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html) | acm-pca:PutPolicy | arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}} | 
| [RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html) | `acm-pca:RevokeCertificate` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [TagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html) | `acm-pca:TagCertificateAuthority` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html) | `acm-pca:UntagCertificateAuthority` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 
| [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) | `acm-pca:UpdateCertificateAuthority` | `arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}` | 

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.