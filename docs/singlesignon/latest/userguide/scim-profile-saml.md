# SCIM profile and SAML 2.0 implementation

Both SCIM and SAML are important considerations for configuring IAM Identity Center. 


## SAML 2.0 implementation


IAM Identity Center supports identity federation with [SAML (Security Assertion Markup
 Language)](https://wiki.oasis-open.org/security "https://wiki.oasis-open.org/security") 2.0. This allows IAM Identity Center to authenticate identities from external identity
 providers (IdPs). SAML 2.0 is an open standard used for securely exchanging SAML assertions.
 SAML 2.0 passes information about a user between a SAML authority (called an identity
 provider or IdP), and a SAML consumer (called a service provider or SP). The IAM Identity Center service
 uses this information to provide federated single sign-on. Single sign-on allows users to
 access AWS accounts and configured applications based on their existing identity provider
 credentials. 


IAM Identity Center adds SAML IdP capabilities to your IAM Identity Center store, AWS Managed Microsoft AD, or to an external
 identity provider. Users can then single sign-on into services that support SAML, including
 the AWS Management Console and third-party applications such as Microsoft 365,
 Concur, and Salesforce. 


The SAML protocol however doesn't provide a way to query the IdP to learn about users
 and groups. Therefore, you must make IAM Identity Center aware of those users and groups by provisioning
 them into IAM Identity Center. 


## SCIM profile


IAM Identity Center provides support for the System for Cross-domain Identity Management (SCIM) v2.0
 standard. SCIM keeps your IAM Identity Center identities in sync with identities from your IdP. This
 includes any provisioning, updates, and deprovisioning of users between your IdP and
 IAM Identity Center.


For more information about how to implement SCIM, see [Provision users and groups from an external identity provider using SCIM](provision-automatically.md "provision-automatically.md"). For
 additional details about IAM Identity Center’s SCIM implementation, see the [IAM Identity Center SCIM Implementation Developer Guide](../developerguide/what-is-scim.md "../developerguide/what-is-scim.md").


###### Topics

* [Provision users and groups from an external identity provider using SCIM](provision-automatically.md "provision-automatically.md")
* [Rotate SAML 2.0 certificates](managesamlcerts.md "managesamlcerts.md")
