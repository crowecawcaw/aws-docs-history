# Enable Public Key Cryptography for Initial

Authentication (PKINIT) for your AWS Managed Microsoft AD users

AWS Managed Microsoft AD directories use strong certificate binding by default, which requires
explicit mapping between certificates and AD objects. The following mappings are considered
strong for AWS Managed Microsoft AD:

- `altSecurityIdentities` Issuer and Serial Number
- `altSecurityIdentities` Subject Key Identifier
- `altSecurityIdentities` SHA1 Hash of Public Key
  These attributes enable strong certificate mapping, which provides better security for
  certificate based authentication by requiring explicit certificate-to-user relationships
  defined in Active Directory. This helps prevent certificate-based privilege escalation
  attacks

You can use this procedure to configure strong certificate bindings to help you prevent
privilege escalation attacks while maintaining certificate authentication
functionality.

For more information, see [Microsoft KB5014754: Certificate-based authentication changes on Windows domain
controllers](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16 "https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16")

## Prerequisites

- An AWS Managed Microsoft AD directory with certificate authority configured
- Administrative access to your Active Directory environment
- PowerShell with Active Directory module installed
- The certificate you want to map to the AD object

## Map AltSecurityIdentity

attribute

1. Choose one of the following `AltSecurityIdentity` mapping methods
   based on your certificate information:
   - **SHA1 hash** – Uses the SHA1 hash
     of the certificate's public key

   For SHA1 hash mapping, extract the certificate hash and apply it to
   the user object:

   ```
   $Username = 'YourUsername'
   $cert = certutil -dump "YourCertificate.cer"
   $certHash = ($cert | Select-String -Pattern "(sha1):*" |
       Select-String -Pattern "Cert").ToString().TrimStart('Cert Hash(sha1): ').Replace(' ','')
   Set-ADUser -Identity $Username -Add @{'altSecurityIdentities'="X509:<SHA1-PUKEY>$CertHash"}
   ```

   - **Issuer and Serial Number** –
     Uses the certificate's issuer name and serial number

   For Issuer and Serial Number mapping, use the certificate's issuer and
   serial number:

   ```
   $Username = 'YourUsername'
   $IssuerName = 'YourCertificateIssuer'
   $SerialNumber = 'YourCertificateSerialNumber'
   Set-ADUser -Identity $Username -Add @{'altSecurityIdentities'="X509:<I>$IssuerName<SR>$SerialNumber"}
   ```

   - **Subject Key Identifier** – Uses
     the certificate's subject key identifier extension

   For Subject Key Identifier mapping, use the certificate's subject key
   identifier:

   ```
   $Username = 'YourUsername'
   $SubjectKeyIdentifier = 'YourSubjectKeyIdentifier'
   Set-ADUser -Identity $Username -Add @{'altSecurityIdentities'="X509:<SKI>$SubjectKeyIdentifier"}
   ```

2. Verify the mapping was applied successfully:

```
Get-ADUser -Identity $Username -Properties altSecurityIdentities |
    Select-Object -ExpandProperty altSecurityIdentities
```

3. Wait for Active Directory replication to complete (typically 15-30 seconds)
   before testing certificate authentication.

## Example: Bulk certificate

mapping the AltSecurityIdentity attribute

The following example demonstrates how to map `AltSecurityIdentity`
attribute for multiple user certificates from a certificate authority:

```
$CertificateTemplateName = 'User'
$Now = $((Get-Date).ToString($(Get-culture).DateTimeFormat.ShortDatePattern))
$Restrict = "Disposition=20,NotAfter>=$Now,Certificate Template=$CertificateTemplateName"
$Out = "SerialNumber,Certificate Hash,User Principal Name,RequesterName,CommonName,CertificateTemplate,NotBefore,NotAfter"
$Certs = certutil -view -restrict $Restrict -out $Out csv | ConvertFrom-CSV
$UserSha1HashMapping = @{}

ForEach ($Cert in $Certs) {
    $UPN = $Cert.'User Principal Name'
    $Username, $Domain = $UPN.Split('@')
    $CertificateThumbprint = ($Cert.'Certificate Hash').Replace(' ','')
    $AdUserObject = Get-ADUser -Identity $Username
    If ($AdUserObject -And $AdUserObject.Count -gt 1) {
        Write-Output "Unable to map user: $Username, multiple user objects found"
        Continue
    }
    If ($AdUserObject) {
        If ($UserSha1HashMapping.Keys -Contains $Username) {
            $UserSha1HashMapping[$Username] += $CertificateThumbprint
        } Else {
            $UserSha1HashMapping[$Username] = @($CertificateThumbprint)
        }
    }
}

ForEach ($User in $UserSha1HashMapping.Keys) {
    Write-Output "Mapping altSecurityIdentity for $User"
    $UserObject = Get-ADUser -Identity $User | Get-ADObject -Properties 'altSecurityIdentities'
    $altSecurityIdentities = $UserObject.altSecurityIdentities
    ForEach ($thumbprint in $UserSha1HashMapping[$User]) {
        $SHA1PUKEY = "X509:<SHA1-PUKEY>$thumbprint"
        If ($altSecurityIdentities -Contains $SHA1PUKEY) {
            Write-Output "Skipping $thumbprint, already mapped."
            Continue
        }
        Write-Output "Adding $thumbprint to $User as altSecurityIdentity"
        Set-ADUser -Identity $User -Add @{'altSecurityIdentities'=$SHA1PUKEY}
    }
}
```

## Next steps

- Test certificate-based authentication with your mapped certificates
- Configure your applications to use the mapped certificates for
  authentication
- [Monitor your AWS Managed Microsoft AD](ms_ad_monitor.md "ms_ad_monitor.md") for
  authentication events
