# Certificate-based authentication and WorkSpaces Personal

You can use certificate-based authentication with WorkSpaces to remove the user prompt for the
Active Directory domain password. By using certificate-based authentication with your Active
Directory domain, you can:

- Rely on your SAML 2.0 identity provider to authenticate the user and provide SAML
  assertions to match the user in Active Directory.
- Enable a single sign-on logon experience with fewer user prompts.
- Enable passwordless authentication flows using your SAML 2.0 identity
  provider.
  Certificate-based authentication uses AWS Private CA resources in your AWS account. AWS Private CA enables
  creation of private certificate authority (CA) hierarchies, including root and subordinate
  CAs. With AWS Private CA, you can create your own CA hierarchy and issue certificates with it for
  authenticating internal users. For more information, see the [AWS Private Certificate Authority User Guide](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md").

When using AWS Private CA for certificate-based authentication, WorkSpaces will request certificates for
your users automatically during session authentication. Users are authenticated to Active
Directory using a virtual smart card provisioned with the certificates.

Certificate-based authentication is supported with Windows WorkSpaces on DCV bundles
using the latest WorkSpaces Web Access, Windows, and macOS client applications. Open Amazon WorkSpaces
[Client downloads](https://clients.amazonworkspaces.com/ "https://clients.amazonworkspaces.com/") to find the latest versions:

- Windows client version 5.5.0 or later
- macOS client version 5.6.0 or later
  For more information on configuring certificate-based authentication with Amazon WorkSpaces, see
  [How to configure certificate-based authentication for Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/how-to-configure-certificate-based-authentication-for-amazon-workspaces/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/how-to-configure-certificate-based-authentication-for-amazon-workspaces/") and
  [Design considerations in highly regulated environments for Certificate Based Authentication with WorkSpaces Applications and WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/design-considerations-in-highly-regulated-environments-for-certificate-based-authentication-with-appstream-2-0-workspaces/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/design-considerations-in-highly-regulated-environments-for-certificate-based-authentication-with-appstream-2-0-workspaces/") .

## Prerequisites

Complete the following steps before enabling certificate-based authentication.

1. Configure your WorkSpaces directory with SAML 2.0 integration to use
   certificate-based authentication. For more information, see [WorkSpaces
   Integration with SAML 2.0](amazon-workspaces-saml.md "amazon-workspaces-saml.md").
2. Configure the `userPrincipalName` attribute in your SAML assertion.
   For more information, see [Create Assertions for the SAML Authentication Response](setting-up-saml.md#create-assertions-saml-auth "setting-up-saml.md#create-assertions-saml-auth").
3. Configure the `ObjectSid` attribute in your SAML assertion. This is
   required to perform strong mapping to the Active Directory user.
   Certificate-based authentication will fail if the attribute does not match the
   Active Directory security identifier (SID) for user specified in the
   SAML_Subject `NameID`. For more information, see [Create Assertions for the SAML Authentication Response](setting-up-saml.md#create-assertions-saml-auth "setting-up-saml.md#create-assertions-saml-auth").

###### Note

According to [Microsoft KB5014754](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16 "https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16"), the `ObjectSid` attribute will
become mandatory for certificate-based authentication after September 10, 2025. 4. Add the [sts:TagSession](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md")
permission to your IAM role trust policy used with your SAML 2.0 configuration
if it is not already present. This permission is required to use
certificate-based authentication. For more information, see [Create a SAML 2.0 Federation IAM Role](setting-up-saml.md#create-saml-iam-role "setting-up-saml.md#create-saml-iam-role"). 5. Create a private certificate authority (CA) using AWS Private CA if you do not have one
configured with your Active Directory. AWS Private CA is required to use
certificate-based authentication. For more information, see [Planning your AWS Private CA deployment](../../../privateca/latest/userguide/PcaPlanning.md "../../../privateca/latest/userguide/PcaPlanning.md") and follow the guidance to configure
a CA for certificate-based authentication. The following AWS Private CA settings are the
most common for certificate-based authentication use cases:

    1. CA type options:




    	1. Short-lived certificate CA usage mode (recommended if you are
    	 only using the CA to issue end user certificates for
    	 certificate-based authentication)
    	2. Single level hierarchy with a Root CA (alternatively, choose a
    	 subordinate CA if you want to integrate with an existing CA
    	 hierarchy)
    2. Key algorithm options: RSA 2048
    3. Subject distinguished name options: Use any combination of options to
     identify the CA in your Active Directory Trusted Root Certification
     Authorities store.
    4. Certificate revocation options: CRL distribution


    ###### Note

    Certificate-based authentication requires an online CRL
     distribution point accessible from desktops and the domain
     controller. This requires unauthenticated access to the Amazon S3
     bucket configured for Private CA CRL entries, or a CloudFront
     distribution that will have access to the S3 bucket if it is
     blocking public access. For more information on these options, see
     [Planning a certificate revocation list (CRL)](../../../privateca/latest/userguide/crl-planning.md#s3-bpa "../../../privateca/latest/userguide/crl-planning.md#s3-bpa").

6.  Tag your private CA with a key entitled `euc-private-ca` to
    designate the CA for use with EUC certificate-based authentication. The key does
    not require a value. For more information, see [Managing tags for your
    private CA](../../../privateca/latest/userguide/PcaCaTagging.md "../../../privateca/latest/userguide/PcaCaTagging.md").
7.  Certificate-based authentication utilizes virtual smart cards for logon.
    Following the [Guidelines for enabling smart card logon with third-party certification
    authorities](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities "https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities") in Active Directory, perform the following steps:
    - Configure domain controllers with a domain controller certificate to
      authenticate smart card users. If you have an Active Directory
      Certificate Services enterprise CA configured in your Active Directory,
      domain controllers are automatically enrolled with certificates to
      enable smart card logon. If you don't have Active Directory Certificate
      Services, see [Requirements for domain controller certificates from a third-party
      CA](https://learn.microsoft.com/en-US/troubleshoot/windows-server/windows-security/requirements-domain-controller "https://learn.microsoft.com/en-US/troubleshoot/windows-server/windows-security/requirements-domain-controller"). You can create a domain controller certificate with
      AWS Private CA. If you do this, don't use a private CA configured for short-lived
      certificates.

    ###### Note

    If you are using AWS Managed Microsoft AD, you can configure Certificate
    Services on an EC2 instance to satisfy the requirement for domain
    controller certificates. See [AWS Launch Wizard](../../../launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc.md "../../../launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc.md") for example deployments of AWS Managed Microsoft AD
    configured with Active Directory Certificate Services. AWS Private CA can be
    configured as a subordinate to the Active Directory Certificate Services CA,
    or can be configured as its own root when using AWS Managed Microsoft AD.

    An additional configuration task with AWS Managed Microsoft AD and Active
    Directory Certificate Services is to create outbound rules from the
    controllers VPC security group to the EC2 instance running
    Certificate Services allowing TCP ports 135 and 49152-65535 to
    enable certificate autoenrollment. In addition, the EC2 instance
    running must allow inbound access on the same ports from domain
    instances, including domain controllers. For more information on
    locating the security group for AWS Managed Microsoft AD see [Configure your VPC subnets and security groups](../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_prepare_mad.md#tutorial_setup_trust_open_vpc "../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_prepare_mad.md#tutorial_setup_trust_open_vpc").
    - On the AWS Private CA console or using the SDK or CLI, select your CA and under
      the CA certificate, export the CA private certificate. For more
      information, see [Exporting a private
      certificate](../../../acm/latest/userguide/export-private.md "../../../acm/latest/userguide/export-private.md").
    - Publish the CA to Active Directory. Logon to a domain controller or a
      domain-joined machine. Copy the CA private certificate to any
      `<path>\<file>` and run the following
      commands as a domain administrator. Alternatively, you can use Group
      Policy and the Microsoft PKI Health Tool (PKIView) tool to publish the
      CA. For more information, see [Configuration instructions](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities#configuration-instructions "https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities#configuration-instructions").

    ```
    certutil -dspublish -f <path>\<file> RootCA
    certutil -dspublish -f  <path>\<file> NTAuthCA
    ```

    Ensure that the commands complete successfully, and then remove the
    private certificate file. Depending on Active Directory replication
    settings, it can take several minutes for the CA to be published to your
    domain controllers and desktop instances.

    ###### Note

        + It is required that Active Directory distribute the CA to the
         Trusted Root Certification Authorities and Enterprise NTAuth stores
         automatically for WorkSpaces desktops when they are joined to the domain.

## Enable certificate-based authentication

Complete the following steps to enable certificate-based authentication.

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Choose the Directory ID for your WorkSpaces.
4. Under **Authentication**, click
   **Edit**.
5. Click **Edit Certificate-Based Authentication**.
6. Check **Enable Certificate-Based Authentication**.
7. Confirm that your private CA ARN is associated in the list. The private CA
   should be in the same AWS account and AWS Region, and must be tagged with a
   key entitled euc-private-ca to appear in the list.
8. Click **Save Changes**. Certificate-based authentication is
   now enabled.
9. Reboot your Windows WorkSpaces on DCV bundles for the changes to take
   effect. For more information, see [Reboot a
   WorkSpace](reboot-workspaces.md "reboot-workspaces.md").
10. After rebooting, when users authenticate via SAML 2.0 using a supported
    client, they will no longer receive a prompt for the domain password.

###### Note

When certificate-based authentication is enabled to sign in to WorkSpaces, users are
not prompted for multi-factor authentication (MFA) even if enabled on the Directory.
When using certificate-based authentication, MFA can be enabled through your SAML
2.0 identity provider. For more information on AWS Directory Service MFA, see [Multi-factor authentication (AD Connector)](../../../directoryservice/latest/admin-guide/ms_ad_mfa.md "../../../directoryservice/latest/admin-guide/ms_ad_mfa.md") or [Enable multi-factor authentication for AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_mfa.md#supportedamazonapps "../../../directoryservice/latest/admin-guide/ms_ad_mfa.md#supportedamazonapps").

## Manage certificate-based authentication

###### CA Certificate

In a typical configuration, the private CA certificate has a validity period of 10
years. See [Managing the private CA
lifecycle](../../../privateca/latest/userguide/ca-lifecycle.md "../../../privateca/latest/userguide/ca-lifecycle.md") for more information on replacing a CA with an expired
certificate, or reissuing the CA with a new validity period.

###### End User Certificates

End user certificates issued by AWS Private CA for WorkSpaces certificate-based authentication
don't require renewal or revocation. These certificates are short-lived. WorkSpaces
automatically issues a new certificate every 24 hours. These end user certificates
have a shorter validity period than a typical AWS Private CA CRL distribution. As a result,
end user certificates don't need to be revoked and won't appear in a CRL.

###### Audit Reports

You can create an audit report to list all of the certificates that your private
CA has issued or revoked. For more information, see [Using audit reports with
your private CA](../../../privateca/latest/userguide/PcaAuditReport.md "../../../privateca/latest/userguide/PcaAuditReport.md").

###### Logging and Monitoring

You can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") to record API calls to AWS Private CA by WorkSpaces. For more information,
see [Using CloudTrail](../../../privateca/latest/userguide/PcaCtIntro.md "../../../privateca/latest/userguide/PcaCtIntro.md"). In [CloudTrail
Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") you can view `GetCertificate` and
`IssueCertificate` event names from
`acm-pca.amazonaws.com` event source made by the WorkSpaces
`EcmAssumeRoleSession` user name. These events will be recorded for
every EUC certificate-based authentication request.

## Enable cross-account PCA sharing

When you use Private CA cross-account sharing, you can grant other accounts permissions to
use a centralized CA, which removes the needs for a Private CA in every account. The CA can generate and issue certificates by using
[AWS Resource Access Manager](https://aws.amazon.com/ram/ "https://aws.amazon.com/ram/") to manage permissions.
Private CA cross-account sharing can be used with WorkSpaces certificate-based Authentication (CBA) within the same AWS Region.

###### To use a shared Private CA resource with WorkSpaces CBA

1. Configure the Private CA for CBA in a centralized AWS account.
   For more information, see [Certificate-based authentication and WorkSpaces Personal](certificate-based-authentication.md "certificate-based-authentication.md").
2. Share the Private CA with the resource AWS accounts where WorkSpaces resources utilize CBA by
   following the steps in [How to use AWS RAM to share your ACM Private CA cross-account](https://aws.amazon.com/blogs/security/how-to-use-aws-ram-to-share-your-acm-private-ca-cross-account/ "https://aws.amazon.com/blogs/security/how-to-use-aws-ram-to-share-your-acm-private-ca-cross-account/"). You don't need to complete step 3 to create a certificate.
   You can either share the Private CA with individual AWS accounts, or share through AWS Organizations. To share with individual
   accounts, you need to accept the shared Private CA in your resource account by using the Resource Access Manager (RAM) console or APIs.
   When configuring the share, confirm that the RAM resource share for the Private CA in the resource account is using the
   `AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority` managed permission template. This template
   aligns with the PCA template used by the WorkSpaces service role when issuing CBA certificates.
3. After the share is successful, you should be able to view the shared Private CA by using the Private CA console
   in the resource account.
4. Use the API or CLI to associate the Private CA ARN with CBA in your WorkSpaces directory properties.
   At this time, the WorkSpaces console doesn't support selection of shared Private CA ARNs. Example CLI commands:

```
aws workspaces modify-certificate-based-auth-properties —resource-id <value> —certificate-based-auth-properties Status=<value>,CertificateAuthorityArn=<value>

```
