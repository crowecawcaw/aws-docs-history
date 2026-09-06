

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Federation process example
<a name="fed-example"></a>

This example uses Active Directory Federation Services (ADFS). However, any technology that supports AWS IAM Federation is supported. For more information about AWS-supported IAM federation, see [IAM Partners](https://aws.amazon.com/iam/partners/) and [Identity Providers and Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html). Your CSDM will help you through this process, which involves a joint effort with your AD team and AMS.

For detailed information about integrating SAML for API access, refer to this AWS blog, [ How to Implement Federated API and CLI Access Using SAML 2.0 and AD FS.](https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/)

For an example that installs the AMS CLI and SAML, see [ Appendix: AD FS claim rule and SAML settings ](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/apx-adfs-claim-rule-saml.html) in the AMS User Guide. 