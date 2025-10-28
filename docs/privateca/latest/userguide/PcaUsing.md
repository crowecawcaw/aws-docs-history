# Issue and manage certificates in AWS Private CA

After you have created and activated a private certificate authority (CA) and configured
access to it, you or your authorized users can issue and manage certificates. If
you have not yet set up AWS Identity and Access Management (IAM) policies for the CA, you can learn more about
configuring them in the [Identity and Access
Management](security-iam.md "security-iam.md") section of this guide. For information about configuring CA access in
single-account and cross-account scenarios, see [Control access to the private CA](granting-ca-access.md "granting-ca-access.md").

###### Topics

- [Issue private end-entity certificates](PcaIssueCert.md "PcaIssueCert.md")
- [Retrieve a private certificate](PcaGetCert.md "PcaGetCert.md")
- [List private certificates](PcaListCerts.md "PcaListCerts.md")
- [Export a private certificate and its secret key](export-in-acm.md "export-in-acm.md")
- [Revoke a private certificate](PcaRevokeCert.md "PcaRevokeCert.md")
- [Automate export of a renewed certificate](auto-export.md "auto-export.md")
- [Use AWS Private CA certificate templates](UsingTemplates.md "UsingTemplates.md")
