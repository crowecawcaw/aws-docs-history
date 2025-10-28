# Prerequisites

Complete the following steps before you use certificate-based
authentication.

1. Set up a domain-joined fleet and configure SAML 2.0. Ensure that you use
   the `username@domain.com`
   `userPrincipalName` format for the SAML_Subject
   `NameID`. For more information, see [Step 5: Create
   Assertions for the SAML Authentication Response](external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions "external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions").

###### Note

Don't enable **Smart card sign in for Active
Directory** in your stack if you want to use
certificate-based authentication. For more information, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards"). 2. Use AppStream 2.0 agent version 10-13-2022 or later with your image. For more
information, see [Keep Your Amazon AppStream 2.0 Image Up-to-Date](keep-image-updated.md "keep-image-updated.md"). 3. Configure the `ObjectSid` attribute in your SAML assertion. You
can use this attribute to perform strong mapping with the Active Directory
user. Certificate-based authentication fails if the `ObjectSid`
attribute doesn't match the Active Directory security identifier (SID) for
the user specified in the SAML_Subject `NameID`. For more
information, see [Step 5: Create
Assertions for the SAML Authentication Response](external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions "external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions"). The
`ObjectSid` is mandatory for certificate-based authentication
after September 10, 2025. For more information, see [KB5014754: Certificate-based authentication changes on Windows domain
controllers](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16 "https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16"). 4. Add the `sts:TagSession` permission to the IAM role trust
policy that you use with your SAML 2.0 configuration. For more information,
see [Passing session
tags in AWS STS](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md"). This permission is required to use
certificate-based authentication. For more information, see [Step 2: Create a SAML 2.0 Federation IAM
Role](external-identity-providers-setting-up-saml.md#external-identity-providers-grantperms "external-identity-providers-setting-up-saml.md#external-identity-providers-grantperms"). 5. Create a private certificate authority (CA) using AWS Private CA, if you
don't have one configured with your Active Directory. AWS Private CA is
required to use certificate-based authentication. For more information, see
[Planning your AWS Private CA
deployment](../../../privateca/latest/userguide/PcaPlanning.md "../../../privateca/latest/userguide/PcaPlanning.md"). The following AWS Private CA settings
are common for many certificate-based authentication use cases:

    * CA type options




    	+ Short-lived certificate CA usage
    	 mode – Recommended if the CA only issues
    	 end user certificates for certificate-based
    	 authentication.
    	+ Single level hierarchy with a Root
    	 CA – Choose a subordinate CA to
    	 integrate it with an existing CA hierarchy.
    * Key algorithm options – RSA
     2048
    * Subject distinguished name options
     – Use the most appropriate options to identify this CA in
     your Active Directory Trusted Root Certification Authorities
     store.
    * Certificate revocation options
     – CRL distribution


    ###### Note

    Certificate-based authentication requires an online CRL
     distribution point accessible from both the AppStream 2.0 fleet
     instance and the domain controller. This requires
     unauthenticated access to the Amazon S3 bucket configured for AWS
     Private CA CRL entries, or a CloudFront distribution with access to
     the Amazon S3 bucket if it blocks public access. For more information
     about these options, see [Planning a certificate revocation list (CRL)](../../../privateca/latest/userguide/crl-planning.md "../../../privateca/latest/userguide/crl-planning.md").

6.  Tag your private CA with a key entitled `euc-private-ca` to
    designate the CA for use with AppStream 2.0 certificate-based authentication. This
    key doesn't require a value. For more information, see [Managing tags for your private CA](../../../privateca/latest/userguide/PcaCaTagging.md "../../../privateca/latest/userguide/PcaCaTagging.md"). For more information about
    the AWS managed policies used with AppStream 2.0 to grant permissions to
    resources in your AWS account, see [AWS Managed Policies Required to Access AppStream 2.0 Resources](managed-policies-required-to-access-appstream-resources.md "managed-policies-required-to-access-appstream-resources.md").
7.  Certificate-based authentication uses virtual smart cards to log on. For
    more information, see [Guidelines for enabling smart card logon with third-party certification
    authorities](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities "https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities"). Follow these steps:

        1. Configure domain controllers with a domain controller certificate
         to authenticate smart card users. If you have an Active Directory
         Certificate Services enterprise CA configured in your Active
         Directory, it automatically enrolls domain controllers with
         certificates that enable smart card logon. If you don't have Active
         Directory Certificate Services, see [Requirements for domain controller certificates from a
         third-party CA](https://learn.microsoft.com/en-US/troubleshoot/windows-server/windows-security/requirements-domain-controller "https://learn.microsoft.com/en-US/troubleshoot/windows-server/windows-security/requirements-domain-controller"). AWS recommends Active Directory
         enterprise certificate authorities to automatically manage
         enrollment for domain controller certificates.


        ###### Note

        If you use AWS Managed Microsoft AD, you can configure
         Certificate Services on an Amazon EC2 instance that satisfies the
         requirement for domain controller certificates. See [Deploy Active Directory to a new Amazon Virtual Private
         Cloud](../../../launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc.md "../../../launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc.md") for example deployments of AWS Managed
         Microsoft AD configured with Active Directory Certificate
         Services.

        With AWS Managed Microsoft AD and Active Directory
         Certificate Services, you must also create outbound rules from
         the controller's VPC security group to the Amazon EC2 instance
         running Certificate Services. You must provide the security
         group access to TCP port 135, and ports 49152 through 65535 to
         enable certificate auto-enrollment. The Amazon EC2 instance must also
         allow inbound access on these same ports from domain instances,
         including domain controllers. For more information on locating
         the security group for AWS Managed Microsoft AD, see [Configure your VPC subnets and security
         groups](../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_prepare_mad.md#tutorial_setup_trust_open_vpc "../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_prepare_mad.md#tutorial_setup_trust_open_vpc").
        2. On the AWS Private CA console, or with the SDK or CLI, export
         the private CA certificate. For more information, see [Exporting a
         private certificate](../../../acm/latest/userguide/export-private.md "../../../acm/latest/userguide/export-private.md").
        3. Publish the private CA to Active Directory. Log on to a domain
         controller or a domain-joined machine. Copy the private CA
         certificate to any
         ``<path>`\`<file>``
         and run the following commands as a domain administrator. You can
         also use Group Policy and the Microsoft PKI Health Tool (PKIView) to
         publish the CA. For more information, see [Configuration instructions](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities#configuration-instructions "https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities#configuration-instructions").



        ```
        certutil -dspublish -f `<path>`\<file> RootCA
        ```


        ```
        certutil -dspublish -f `<path>`\<file> NTAuthCA
        ```

        Make sure that the commands complete successfully, then remove the
         private CA certificate file. Depending on your Active Directory
         replication settings, it can take several minutes for the CA to
         publish to your domain controllers and AppStream 2.0 fleet
         instances.


        ###### Note

        Active Directory must distribute the CA to the Trusted Root
         Certification Authorities and Enterprise NTAuth stores
         automatically for AppStream 2.0 fleet instances when they join the
         domain.

    For Windows operating systems, the distribution of the CA (Certificate Authority)
    happens automatically. However, for Rocky Linux and Red Hat Enterprise Linux, you
    must download the root CA certificate(s) from the CA used by your AppStream 2.0 Directory
    Config. If your KDC root CA certificate(s) are different, you must also download
    those. Before using certificate-based authentication, it's necessary to import these
    certificates onto an image or snapshot.

On the image, there should be a file named
/`etc/sssd/pki/sssd_auth_ca_db.pem`. It should look like the
following:

```
-----BEGIN CERTIFICATE-----
Base64-encoded certificate chain from ACM Private CA
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
Base64-encoded certificate body from ACM private CA
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
Base64-encoded root CA KDC certificate chain
-----END CERTIFICATE-----
```

###### Note

When copying an image across regions or accounts, or re-associating an image with
a new Active Directory, this file will need to be reconfigured with the relevant
certificates on an image builder and snapshotted again before use.

Below are instructions for downloading the root CA certificates:

1. On the image builder, create a file named
   `/etc/sssd/pki/sssd_auth_ca_db.pem`.
2. Open the [AWS Private CA
   console](https://console.aws.amazon.com/acm-pca/ "https://console.aws.amazon.com/acm-pca/").
3. Choose the private certificate used with your AppStream 2.0 Directory
   Config.
4. Choose the **CA certificate** tab.
5. Copy the certificate chain and certificate body to
   `/etc/sssd/pki/sssd_auth_ca_db.pem` on the image
   builder.
   If the root CA certificates used by the KDCs are different from the root CA
   certificate used by your AppStream 2.0 Directory Config, follow these example steps to download
   them:

6. Connect to a Windows instance joined to the same domain as your image
   builder.
7. Open `certlm.msc`.
8. In the left pane, choose **Trusted Root Certificate
   Authorities**, and then choose
   **Certificates**..
9. For each root CA certificate, open the context (right-click) menu.
10. Choose **All Tasks**, choose **Export**
    to open the Certificate Export Wizard, and then choose
    **Next**.
11. Choose **Base64-encoded X.509 (.CER)**, and choose
    **Next**.
12. Choose **Browse**, enter a file name, and choose
    **Next**.
13. Choose **Finish**.
14. Open the exported certificate in a text editor.
15. Copy the contents of the file to
    `/etc/sssd/pki/sssd_auth_ca_db.pem` on the image
    builder.
