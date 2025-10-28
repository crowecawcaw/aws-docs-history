# Conditions for using AWS Private CA to sign ACM private

certificates

You can use AWS Private CA to sign your ACM certificates in either of two
cases:

- **Single account**: The signing CA and the
  AWS Certificate Manager (ACM) certificate that is issued reside in the same AWS
  account.

For single-account issuance and renewals to be enabled, the AWS Private CA
administrator must grant permission to the ACM service principal to
create, retrieve, and list certificates. This is done using the AWS Private CA
API action [CreatePermission](../../../privateca/latest/APIReference/API_CreatePermission.md "../../../privateca/latest/APIReference/API_CreatePermission.md") or the AWS CLI command [create-permission](../../../cli/latest/reference/acm-pca/create-permission.md "../../../cli/latest/reference/acm-pca/create-permission.md"). The account owner assigns these permissions
to an IAM user, group, or role that is responsible for issuing
certificates.

- **Cross-account**: The signing CA and the
  ACM certificate that is issued reside in different AWS accounts, and
  access to the CA has been granted to the account where the certificate
  resides.

To enable cross-account issuance and renewals, the AWS Private CA
administrator must attach a resource-based policy to the CA using the
AWS Private CA API action [PutPolicy](../../../privateca/latest/APIReference/API_PutPolicy.md "../../../privateca/latest/APIReference/API_PutPolicy.md") or the AWS CLI command [put-policy](../../../cli/latest/reference/acm-pca/put-policy.md "../../../cli/latest/reference/acm-pca/put-policy.md"). The policy specifies principals in other accounts
that are allowed limited access to the CA. For more information, see [Using a Resource Based Policy with ACM Private CA](../../../privateca/latest/userguide/pca-rbp.md "../../../privateca/latest/userguide/pca-rbp.md").

The cross-account scenario also requires ACM to set up a service-linked
role (SLR) to interact as a principal with the PCA policy. ACM creates the
SLR automatically while issuing the first certificate.

ACM might alert you that it cannot determine whether an SLR exists on your account. If the
required `iam:GetRole` permission has already been granted to the ACM SLR for your account,
then the alert will not recur after the SLR is created. If it does recur,
then you or your account administrator might need to grant the `iam:GetRole`
permission to ACM, or associate your account with the ACM-managed policy
`AWSCertificateManagerFullAccess`.

For more information, see [Using a Service Linked Role with ACM](acm-slr.md "acm-slr.md").

###### Important

Your ACM certificate must be actively associated with a supported AWS service
before it can be automatically renewed. For information about the resources that ACM
supports, see [Services integrated with ACM](acm-services.md "acm-services.md").
