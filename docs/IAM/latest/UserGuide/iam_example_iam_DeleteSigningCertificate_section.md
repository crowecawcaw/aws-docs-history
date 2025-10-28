# Use `DeleteSigningCertificate` with a CLI

The following code examples show how to use `DeleteSigningCertificate`.

CLI

**AWS CLI**

**To delete a signing certificate for an IAM user**

The following `delete-signing-certificate` command deletes the specified signing certificate for the IAM user named `Bob`.

```
`aws iam delete-signing-certificate \
 --user-name `Bob` \
 --certificate-id `TA7SMP42TDN5Z26OBPJE7EXAMPLE``

```

This command produces no output.

To get the ID for a signing certificate, use the `list-signing-certificates` command.

For more information, see [Manage signing certificates](../../../AWSEC2/latest/UserGuide/set-up-ami-tools.md#ami-tools-managing-certs "../../../AWSEC2/latest/UserGuide/set-up-ami-tools.md#ami-tools-managing-certs") in the _Amazon EC2 User Guide_.

- For API details, see
  [DeleteSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the signing certificate with the ID `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` from the IAM user named `Bob`.**

```
Remove-IAMSigningCertificate -UserName Bob -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU

```

- For API details, see
  [DeleteSigningCertificate](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the signing certificate with the ID `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` from the IAM user named `Bob`.**

```
Remove-IAMSigningCertificate -UserName Bob -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU

```

- For API details, see
  [DeleteSigningCertificate](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
