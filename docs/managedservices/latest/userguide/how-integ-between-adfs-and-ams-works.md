

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# How integration between AD FS and AMS works
<a name="how-integ-between-adfs-and-ams-works"></a>

A one-way trust between your on-premises network and the AMS domain is the default means for access to stacks and VPCs. When a VPC and stack are created, access is granted via pre-configured Active Directory security groups. In addition, access to the AWS Management Console can be configured using Active Directory Federation Service (AD FS), or any federation software that supports SAML, for a single sign-on (SSO) to the AWS Management Console.

**Note**  
AMS can federate to many federation services, Ping, Okta, and so on. You aren't limited to AD FS; we provide here an example of one federation technology available to you.

Information here is duplicated from this blog post: [ Enabling Federation to AWS Using Windows Active Directory, AD FS, and SAML 2.0](https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/).

![There are several steps involved in secure authentication within your enterprise and between your enterprise and the AWS cloud.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/AD1.png)


1. The flow is initiated when a user (let’s call him Bob) browses to the AD FS sample site (https://Fully.Qualified.Domain.Name.Here/adfs/ls/IdpInitiatedSignOn.aspx) inside his domain. When you install AD FS, you get a new virtual directory named **adfs** for your default website, which includes this page.

1. The sign-on page authenticates Bob against AD. Depending on the browser Bob is using, he might be prompted for his AD username and password.

1. Bob’s browser receives a SAML assertion in the form of an authentication response from AD FS.

1. Bob’s browser posts the SAML assertion to the AWS sign-in endpoint for SAML (https://signin.aws.amazon.com/saml). Behind the scenes, sign-in uses the [AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html) API to request temporary security credentials and then constructs a sign-in URL for the AWS Management Console.

1. Bob’s browser receives the sign-in URL and is redirected to the console.

From Bob’s perspective, the process happens transparently. He starts at an internal website and ends up at the AWS Management Console, without ever having to supply any AWS credentials.

**Note**  
More information on configuring federation to the AMS console is provided in:  
**Multi-Account Landing Zone**: [Configuring Federation to the AMS Console](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate-console.html)
**Single-Account Landing Zone**: [Configuring Federation to the AMS Console](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/fed-with-console.html)
Additionally, see [Appendix: AD FS claim rule and SAML settings](https://docs.aws.amazon.com/managedservices/latest/userguide/apx-adfs-claim-rule-saml.html). For information about using AWS Microsoft AD to support your Active Directory–aware applications, in the AWS Cloud, that are subject to compliance requirements, see [Manage Microsoft AD Compliance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_compliance.html).