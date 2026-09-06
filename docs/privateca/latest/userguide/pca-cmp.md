

# Customer managed permissions in RAM
<a name="pca-cmp"></a>

In addition to the AWS managed permissions available in RAM, AWS Private CA supports RAM customer managed permissions (CMP). Customer managed permissions allow CA owners to define a custom set of actions that cross-account principals can perform on a shared CA, providing finer-grained access control than the default AWS managed permissions.

The following actions are available for customer managed permissions on the `acm-pca:certificate-authority` resource type:

**Read actions**
+ `acm-pca:DescribeCertificateAuthority` – View CA configuration and status.
+ `acm-pca:GetCertificate` – Retrieve an issued certificate.
+ `acm-pca:GetCertificateAuthorityCertificate` – Retrieve the CA certificate and certificate chain.
+ `acm-pca:ListPermissions` – List permissions assigned to the CA.
+ `acm-pca:ListTags` – List tags associated with the CA.

**Write actions**
+ `acm-pca:IssueCertificate` – Issue a certificate from the shared CA.
+ `acm-pca:RevokeCertificate` – Revoke a previously issued certificate.

You can create customer managed permissions that include any combination of these actions. For example, you can create a read-only permission that excludes `IssueCertificate` and `RevokeCertificate`, or a full-access permission that includes all seven actions.

For more information about creating customer managed permissions, see [Creating customer managed permissions](https://docs.aws.amazon.com/ram/latest/userguide/create-customer-managed-permissions.html) in the *AWS RAM User Guide*.