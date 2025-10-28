# IAM Identity Center integration limitations

With AWS IAM Identity Center, you can connect to identity providers (IdPs) and centrally manage access
for users and groups across AWS analytics services. You can configure AWS Lake Formation as an enabled application in IAM Identity Center, and data lake
administrators can grant fine-grained permissions to authorized users and groups on AWS Glue Data Catalog resources.

The following limitations apply to Lake Formation integration with
IAM Identity Center:

- You can't assign IAM Identity Center users and groups as data lake administrators or read-only administrators in Lake Formation.

IAM Identity Center users and groups can query encrypted Data Catalog resources if you are using an IAM
role that AWS Glue can assume on your behalf for encrypting and decrypting the Data Catalog. AWS
managed keys don't support trusted identity propagation.

- IAM Identity Center users and groups can only invoke API operations listed in the `AWSIAMIdentityCenterAllowListForIdentityContext` policy provided by IAM Identity Center.
- Lake Formation permits IAM roles from external accounts to act as carrier roles on behalf of IAM Identity Center users and groups for accessing Data Catalog resources,
  but permissions can only be granted on Data Catalog resources within the owning account.
  If you try to grant permissions to IAM Identity Centerusers and groups on Data Catalog resources in an external account,
  Lake Formation throws the following error - "Cross-account grants are not supported for the principal."
- When using Lake Formation with IAM Identity Center, the application assignment configuration is set to
  `false` by default. If you modify this configuration directly through the
  [IAM Identity Center API](../../../singlesignon/latest/APIReference/API_PutApplicationAssignmentConfiguration.md "../../../singlesignon/latest/APIReference/API_PutApplicationAssignmentConfiguration.md"), you must then manage all application assignments manually using the
  API. Lake Formation does not automatically synchronize or manage assignment changes made
  outside of its standard workflows, which may impact access patterns and authorization
  flows within your data lake environment.
