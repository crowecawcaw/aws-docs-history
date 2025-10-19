# Set up emergency access to the AWS Management Console

IAM Identity Center is built from highly available AWS infrastructure and uses an Availability Zone architecture to eliminate single points of failure. 
 For an extra layer of protection in the unlikely event of an IAM Identity Center or AWS Region disruption, we recommend 
 that you set up a configuration that you can use to provide temporary access to the AWS Management Console.

AWS enables you to:


* [Connect your third-party IdP to IAM Identity Center](manage-your-identity-source-idp.md "manage-your-identity-source-idp.md").
* Connect your third-party IdP to individual AWS accounts by using [SAML 2.0-based federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html").
If you use IAM Identity Center, you can use these capabilities to create the emergency access
 configuration described in the following sections. This configuration enables you to use
 IAM Identity Center as the mechanism for AWS account access. If IAM Identity Center is disrupted, your emergency
 operations users can sign in to the AWS Management Console through direct federation, by using the same
 credentials that they use to access their accounts. This configuration works when IAM Identity Center is
 unavailable, but the IAM data plane and your
 external
 identity provider (IdP) are available.

###### Important

We recommend that you deploy this configuration before a disruption occurs because you cannot
 create the configuration if your access to create the required IAM roles is also
 disrupted. Also, test this configuration periodically to ensure that your team
 understands what to do if IAM Identity Center is disrupted.

###### Topics

* [Summary of emergency access configuration](emergency-access-implementation.md "emergency-access-implementation.md")
* [How to
 design
 your critical operations roles](emergency-access-implementation-design.md "emergency-access-implementation-design.md")
* [How to plan your access model](emergency-access-planning.md "emergency-access-planning.md")
* [How to design
 emergency
 role, account, and group mapping](emergency-access-mapping-design.md "emergency-access-mapping-design.md")
* [How to create your emergency access configuration](emergency-access-role-idp-group-creation-mapping-plan.md "emergency-access-role-idp-group-creation-mapping-plan.md")
* [Emergency preparation tasks](emergency-access-prepare-configuration.md "emergency-access-prepare-configuration.md")
* [Emergency failover process](emergency-access-failover-steps.md "emergency-access-failover-steps.md")
* [Return to normal operations](emergency-access-return-to-normal-operations.md "emergency-access-return-to-normal-operations.md")
* [One-time setup of a direct IAM federation application in Okta](emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.md "emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.md")
