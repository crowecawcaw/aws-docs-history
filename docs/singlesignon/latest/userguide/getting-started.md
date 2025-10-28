# Getting started with IAM Identity Center

The following outlines how you can get started with IAM Identity Center.

1. **Enable IAM Identity Center**

When you [enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md"), you choose between
two types of IAM Identity Center instances. These types are: [organization
instances](organization-instances-identity-center.md "organization-instances-identity-center.md") (recommended) and [account instances](account-instances-identity-center.md "account-instances-identity-center.md").
To learn more about the different capabilities of these instance types, see [organization and account instances of
IAM Identity Center](identity-center-instances.md "identity-center-instances.md").

###### Note

After IAM Identity Center is enabled, you can sign in and open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/") by doing either of the following:

    * **Organization instance** - Sign in to AWS using credentials
     with administrative permissions in the management account.
    * **Account instance** - Sign in to AWS using credentials with
     administrative permissions in the AWS account where IAM Identity Center is enabled.

2. **Connect your identity source to IAM Identity Center**

In IAM Identity Center console, confirm the identity source that you want to use. See the following
for identity sources:

    * **External identity provider** - If you have an existing identity
     provider to manage your workforce users, you can connect it to IAM Identity Center. For more
     information about how to configure commonly used identity providers to work with IAM Identity Center,
     see [IAM Identity Center identity source tutorials](tutorials.md "tutorials.md").
    * **Active Directory** - If you are using Active Directory to manage
     your workforce users, you can connect it to IAM Identity Center. For more information, see [Using Active Directory as an identity source](gs-ad.md "gs-ad.md").
    * **IAM Identity Center** - Alternatively, you can [create and manage users and groups directly in
     IAM Identity Center](quick-start-default-idc.md "quick-start-default-idc.md").

3. **Set up user access to AWS accounts (organization instance
   only)**

If you’re using an organization instance of IAM Identity Center, you can [assign user or group access to
AWS accounts](assignusers.md "assignusers.md"), using [permission sets](permissionsetsconcept.md "permissionsetsconcept.md") to
grant your users access to AWS accounts and resources. 4. **Set up user access to applications**

With IAM Identity Center, you can grant users access to two types of applications:

    1. **[AWS managed applications](awsapps.md "awsapps.md")**




    	* You can use IAM Identity Center with AWS managed applications like Amazon Q Business, AWS CLI, and
    	 Amazon Redshift. For more information, see [AWS managed applications](awsapps.md "awsapps.md")
    	 and [Integrating AWS CLI with IAM Identity Center](integrating-aws-cli.md "integrating-aws-cli.md").
    2. **[Customer managed applications](customermanagedapps.md "customermanagedapps.md")**




    	* You can integrate either of the following types of customer managed applications
    	 with IAM Identity Center:




    		+ [Applications listed in IAM Identity Center catalog](saasapps.md "saasapps.md")
    		+ [Your custom
    		 applications](customermanagedapps-set-up-your-own-app-saml2.md "customermanagedapps-set-up-your-own-app-saml2.md")
    	* After configuring your application, you can [assign your users access to the application](assignuserstoapp.md "assignuserstoapp.md").

5. **Provide your users with sign-in instructions for the
   AWS access portal**

The AWS access portal is a web portal that provides your users with seamless access to all
their assigned applications, AWS accounts, or both. New users in IAM Identity Center must activate their
user credentials before they can sign in to the AWS access portal.

For information about how to sign in to the AWS access portal, see [Sign in to the
AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_. To learn
about the sign-in process for the AWS access portal, see [Signing in to the
AWS access portal](howtosignin.md "howtosignin.md").
