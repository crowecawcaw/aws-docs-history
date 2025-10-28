# Enable Cross-account PCA Sharing

Private CA (PCA) cross-account sharing offers the ability to grant permissions for
other accounts to use a centralized CA. The CA can generate and issue certificates
by using [AWS Resource Access
Manager](https://aws.amazon.com/ram/ "https://aws.amazon.com/ram/") (RAM) to manage the permissions. This removes the need for a
Private CA in every account. Private CA cross-account sharing can be used with
AppStream 2.0 certificate-based Authentication (CBA) within the same AWS Region.

To use a shared Private CA resource with AppStream 2.0 CBA, complete the following
steps:

1. Configure the Private CA for CBA in a centralized AWS account. For more
   information, see [Certificate-Based
   Authentication](certificate-based-authentication.md "certificate-based-authentication.md").
2. Share the Private CA with the resource AWS accounts where AppStream 2.0
   resources utilize CBA. To do this, follow the steps in [How to use AWS RAM to share your ACM Private CA cross-account](https://aws.amazon.com/blogs/security/how-to-use-aws-ram-to-share-your-acm-private-ca-cross-account/ "https://aws.amazon.com/blogs/security/how-to-use-aws-ram-to-share-your-acm-private-ca-cross-account/").
   You do not need to complete step 3 to create a certificate. You can either
   share the Private CA with individual AWS accounts, or share through
   AWS Organizations. If you share with individual accounts, you need to accept the
   shared Private CA in your resource account by using the AWS Resource Access Manager console or
   APIs.

When configuring the share, confirm that the AWS Resource Access Manager resource share for
the Private CA in the resource account is using the
`AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority`
managed permission template. This template aligns with the PCA template used
by the AppStream 2.0 service role when issuing CBA certificates. 3. After the share is successful, view the shared Private CA by using the
Private CA console in the resource account. 4. Use the API or CLI to associate the Private CA ARN with CBA in your AppStream 2.0
Directory Config. At this time, the AppStream 2.0 console does not support
selection of shared Private CA ARNs. The following are example CLI
commands:

`aws appstream update-directory-config --directory-name <value>
 --certificate-based-auth-properties
 Status=<value>,CertificateAuthorityArn=<value>`
