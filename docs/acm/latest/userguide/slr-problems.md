# Problems with the ACM service-linked role (SLR)

When you issue a certificate signed by a private CA that has been shared with you by
another account, ACM attempts on first use to set up a service-linked role (SLR) to
interact as a principal with an AWS Private CA [resource-based access policy](../../../privateca/latest/userguide/pca-resource-sharing.md#pca-rbp "../../../privateca/latest/userguide/pca-resource-sharing.md#pca-rbp").
If you issue a private certificate from a shared CA and the SLR is not in place, ACM will
be unable to automatically renew that certificate for you.

ACM might alert you that it cannot determine whether an SLR exists on your account. If the
required `iam:GetRole` permission has already been granted to the ACM SLR for your account,
then the alert will not recur after the SLR is created. If it does recur,
then you or your account administrator might need to grant the `iam:GetRole`
permission to ACM, or associate your account with the ACM-managed policy
`AWSCertificateManagerFullAccess`.

For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.
