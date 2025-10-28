# Use `UpdateSigningCertificate` with a CLI

The following code examples show how to use `UpdateSigningCertificate`.

CLI

**AWS CLI**

**To activate or deactivate a signing certificate for an IAM user**

The following `update-signing-certificate` command deactivates the specified signing certificate for the IAM user named `Bob`.

```
`aws iam update-signing-certificate \
 --certificate-id `TA7SMP42TDN5Z26OBPJE7EXAMPLE` \
 --status `Inactive` \
 --user-name `Bob``

```

To get the ID for a signing certificate, use the `list-signing-certificates` command.

For more information, see [Manage signing certificates](../../../AWSEC2/latest/UserGuide/set-up-ami-tools.md#ami-tools-managing-certs "../../../AWSEC2/latest/UserGuide/set-up-ami-tools.md#ami-tools-managing-certs") in the _Amazon EC2 User Guide_.

- For API details, see
  [UpdateSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example updates the certificate that is associated with the IAM user named `Bob` and whose certificate ID si `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` to mark it as inactive.**

```
Update-IAMSigningCertificate -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU -UserName Bob -Status Inactive

```

- For API details, see
  [UpdateSigningCertificate](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example updates the certificate that is associated with the IAM user named `Bob` and whose certificate ID si `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` to mark it as inactive.**

```
Update-IAMSigningCertificate -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU -UserName Bob -Status Inactive

```

- For API details, see
  [UpdateSigningCertificate](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
