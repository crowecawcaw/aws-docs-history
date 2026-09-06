

# IAM Identity Center identity source tutorials
<a name="tutorials"></a>

You can connect your existing identity source in your AWS Organizations management account to [an organization instance of IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). If you do not have an existing identity provider, you can create and manage users directly in the default IAM Identity Center directory. You can have one identity source per organization. 

The tutorials in this section describe how to set up an organization instance of IAM Identity Center with a commonly used identity source, create an administrative user, and if you are using IAM Identity Center to manage access to AWS accounts, create and configure permission sets. If you’re using IAM Identity Center for application access only, you do not need to use permission sets.

These tutorials do not describe how to set up account instances of IAM Identity Center. You can use account instances to assign users and groups to applications, but you cannot use this instance type to manage user access to AWS accounts. For more information, see [Account instances of IAM Identity Center](account-instances-identity-center.md). 

**Note**  
Before starting any of these tutorials, enable IAM Identity Center. For more information, see [Enable IAM Identity Center](enable-identity-center.md).

**Topics**
+ [Using Active Directory as an identity source](gs-ad.md)
+ [Setting up SCIM provisioning between CyberArk and IAM Identity Center](cyberark-idp.md)
+ [Configure SAML and SCIM with Google Workspace and IAM Identity Center](gs-gwp.md)
+ [Using IAM Identity Center to connect with your JumpCloud Directory Platform](jumpcloud-idp.md)
+ [Configure SAML and SCIM with Microsoft Entra ID and IAM Identity Center](idp-microsoft-entra.md)
+ [Configure SAML and SCIM with Okta and IAM Identity Center](gs-okta.md)
+ [Setting up SCIM provisioning between OneLogin and IAM Identity Center](onelogin-idp.md)
+ [Using Ping Identity products with IAM Identity Center](pingidentity.md)
+ [Configure user access with the default IAM Identity Center directory](quick-start-default-idc.md)
+ [Video tutorials](#w2aac15c31)

## Video tutorials
<a name="w2aac15c31"></a>

As an additional resource, you can use these video tutorials to learn more about setting up external identity providers:
+ [Migrating between external identity providers in AWS IAM Identity Center](https://www.youtube.com/watch?v=A87tSiBdSnU)
+ [Federating your existing AWS IAM Identity Center instance with Microsoft Entra ID](https://www.youtube.com/watch?v=iSCuTJNeN6c)