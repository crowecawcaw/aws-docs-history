

# Use `DeleteSigningCertificate` with a CLI
<a name="iam_example_iam_DeleteSigningCertificate_section"></a>

The following code examples show how to use `DeleteSigningCertificate`.

------
#### [ CLI ]

**AWS CLI**  
**To delete a signing certificate for an IAM user**  
The following `delete-signing-certificate` command deletes the specified signing certificate for the IAM user named `Bob`.  

```
aws iam delete-signing-certificate \
    --user-name {{Bob}} \
    --certificate-id {{TA7SMP42TDN5Z26OBPJE7EXAMPLE}}
```
This command produces no output.  
To get the ID for a signing certificate, use the `list-signing-certificates` command.  
For more information, see [Manage signing certificates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-up-ami-tools.html#ami-tools-managing-certs) in the *Amazon EC2 User Guide*.  
+  For API details, see [DeleteSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the signing certificate with the ID `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` from the IAM user named `Bob`.**  

```
Remove-IAMSigningCertificate -UserName Bob -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU
```
+  For API details, see [DeleteSigningCertificate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the signing certificate with the ID `Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU` from the IAM user named `Bob`.**  

```
Remove-IAMSigningCertificate -UserName Bob -CertificateId Y3EK7RMEXAMPLESV33FCREXAMPLEMJLU
```
+  For API details, see [DeleteSigningCertificate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.