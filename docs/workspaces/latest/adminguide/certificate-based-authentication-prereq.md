

# Prerequisites
<a name="certificate-based-authentication-prereq"></a>

Complete the following steps before you use certificate-based authentication.

1. Configure your WorkSpaces Pools directory with SAML 2.0 integration to use certificate-based authentication. For more information, see [Configure SAML 2.0 and create a WorkSpaces Pools directory](create-directory-pools.md).
**Note**  
Don't enable **Smart card sign in** in your pool directory if you want to use certificate-based authentication. 

1. Configure the `userPrincipalName` attribute in your SAML assertion. For more information, see [Step 7: Create assertions for the SAML authentication response](create-directory-pools.md#saml-directory-create-assertions).

1. Configure the `ObjectSid` attribute in your SAML assertion. You can use this attribute to perform strong mapping with the Active Directory user. Certificate-based authentication fails if the `ObjectSid` attribute doesn't match the Active Directory security identifier (SID) for the user specified in the SAML\_Subject `NameID`. For more information, see [Step 7: Create assertions for the SAML authentication response](create-directory-pools.md#saml-directory-create-assertions). 
**Note**  
According to [Microsoft KB5014754](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16), the `ObjectSid` attribute will become mandatory for certificate-based authentication after September 10, 2025.

1. Add the `sts:TagSession` permission to the IAM role trust policy that you use with your SAML 2.0 configuration. For more information, see [Passing session tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html.html) in the *AWS Identity and Access Management User Guide*. This permission is required to use certificate-based authentication. For more information, see [Step 5: Create a SAML 2.0 federation IAM role](create-directory-pools.md#saml-directory-saml-federation-role-in-iam).

1. Create a private certificate authority (CA) using AWS Private CA, if you don't have one configured with your Active Directory. AWS Private CA is required to use certificate-based authentication. For more information, see [Planning your AWS Private CA deployment](https://docs.aws.amazon.com/privateca/latest/userguide/PcaPlanning.html) in the *AWS Private Certificate Authority User Guide*. The following AWS Private CA settings are common for many certificate-based authentication use cases:
   + **CA type options**
     + **Short-lived certificate CA usage mode** – Recommended if the CA only issues end user certificates for certificate-based authentication.
     + **Single level hierarchy with a Root CA** – Choose a subordinate CA to integrate it with an existing CA hierarchy.
   + **Key algorithm options** – RSA 2048
   + **Subject distinguished name options** – Use the most appropriate options to identify this CA in your Active Directory Trusted Root Certification Authorities store.
   + **Certificate revocation options** – CRL distribution
**Note**  
Certificate-based authentication requires an online CRL distribution point accessible from both the WorkSpaces in WorkSpaces Pools and the domain controller. This requires unauthenticated access to the Amazon S3 bucket configured for AWS Private CA CRL entries, or a CloudFront distribution with access to the Amazon S3 bucket if it blocks public access. For more information about these options, see [Planning a certificate revocation list (CRL)](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html) in the *AWS Private Certificate Authority User Guide*.

1. Tag your private CA with a key entitled `euc-private-ca` to designate the CA for use with WorkSpaces Pools certificate-based authentication. This key doesn't require a value. For more information, see [Managing tags for your private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCaTagging.html) in the *AWS Private Certificate Authority User Guide*..

1. Certificate-based authentication uses virtual smart cards to log on. For more information, see [Guidelines for enabling smart card logon with third-party certification authorities](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities). Follow these steps:

   1. Configure domain controllers with a domain controller certificate to authenticate smart card users. If you have an Active Directory Certificate Services enterprise CA configured in your Active Directory, it automatically enrolls domain controllers with certificates that enable smart card logon. If you don't have Active Directory Certificate Services, see [Requirements for domain controller certificates from a third-party CA](https://learn.microsoft.com/en-US/troubleshoot/windows-server/windows-security/requirements-domain-controller). You can create a domain controller certificate with AWS Private CA. If you do this, don't use a private CA configured for short-lived certificates.
**Note**  
If you use AWS Managed Microsoft AD, you can configure Certificate Services on an Amazon EC2 instance that satisfies the requirement for domain controller certificates. See [Deploy Active Directory to a new Amazon Virtual Private Cloud](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc.html) for example deployments of AWS Managed Microsoft AD configured with Active Directory Certificate Services.  
With AWS Managed Microsoft AD and Active Directory Certificate Services, you must also create outbound rules from the controller's VPC security group to the Amazon EC2 instance running Certificate Services. You must provide the security group access to TCP port 135, and ports 49152 through 65535 to enable certificate auto-enrollment. The Amazon EC2 instance must also allow inbound access on these same ports from domain instances, including domain controllers. For more information on locating the security group for AWS Managed Microsoft AD, see [Configure your VPC subnets and security groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_prepare_mad.html#tutorial_setup_trust_open_vpc).

   1. On the AWS Private CA console, or with the SDK or CLI, export the private CA certificate. For more information, see [Exporting a private certificate](https://docs.aws.amazon.com/acm/latest/userguide/export-private.html).

   1. Publish the private CA to Active Directory. Log on to a domain controller or a domain-joined machine. Copy the private CA certificate to any `{{<path>}}\{{<file>}}` and run the following commands as a domain administrator. You can also use Group Policy and the Microsoft PKI Health Tool (PKIView) to publish the CA. For more information, see [Configuration instructions](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities#configuration-instructions).

      ```
      certutil -dspublish -f {{<path>}}\<file> RootCA
      ```

      ```
      certutil -dspublish -f {{<path>}}\<file> NTAuthCA
      ```

      Make sure that the commands complete successfully, then remove the private CA certificate file. Depending on your Active Directory replication settings, it can take several minutes for the CA to publish to your domain controllers and WorkSpaces in WorkSpaces Pools.
**Note**  
Active Directory must distribute the CA to the Trusted Root Certification Authorities and Enterprise NTAuth stores automatically for WorkSpaces in WorkSpaces Pools when they join the domain.
**Note**  
Active Directory domain controllers must be in Compatibility mode for certificate strong enforcement to support certificate-based authentication. For more information, see [KB5014754—Certificate-based authentication changes on Windows domain controllers](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16) in the Microsoft Support documentation. If you are using AWS Managed Microsoft AD, see [Configure directory security settings](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_settings.html) for more information.