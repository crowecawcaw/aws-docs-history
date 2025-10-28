# Use Case 4: AWS IAM Identity Center to Office 365 and other cloud applications

You can use AWS Managed Microsoft AD to provide AWS IAM Identity Center services for cloud applications. You can use Microsoft Entra Connect (formerly known as Azure Active Directory Connect)
to synchronize your users into Microsoft Entra (formerly known as Azure Active Directory (Azure AD)), and then use Active Directory Federation
Services (AD FS) so that your users can access [Microsoft Office 365](https://aws.amazon.com/blogs/security/how-to-enable-your-users-to-access-office-365-with-aws-microsoft-active-directory-credentials/ "https://aws.amazon.com/blogs/security/how-to-enable-your-users-to-access-office-365-with-aws-microsoft-active-directory-credentials/") and other SAML 2.0 cloud applications by using their Active Directory
credentials.

[Integrating AWS Managed Microsoft AD with IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md "../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md") adds SAML capabilities to your AWS Managed Microsoft AD
and / or your on-premises trusted domains. Once integrated your users can then use IAM Identity Center with
services that support SAML, including the AWS Management Console and third-party cloud applications such as
Office 365, Concur, and Salesforce without having to configure a SAML infrastructure. For a
demonstration on the process of allowing your on-premises users to use IAM Identity Center, see the following
YouTube video.

###### Note

AWS Single Sign-On was renamed to IAM Identity Center.
