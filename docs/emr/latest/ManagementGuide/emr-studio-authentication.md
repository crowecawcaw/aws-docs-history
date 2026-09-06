

# Choose an authentication mode for Amazon EMR Studio
<a name="emr-studio-authentication"></a>

EMR Studio supports two authentication modes: IAM authentication mode and IAM Identity Center authentication mode. IAM mode uses AWS Identity and Access Management (IAM), while IAM Identity Center mode uses AWS IAM Identity Center. When you create an EMR Studio, you choose the authentication mode for all users of that Studio. For more information about the different authentication modes, see [Authentication and user login](how-emr-studio-works.md#emr-studio-login).

Use the following table to choose an authentication mode for EMR Studio.



| If you are... | We recommend... | 
| --- | --- | 
| Already familiar with or have previously set up IAM authentication or federation | [IAM authentication mode](#emr-studio-iam-authentication), which offers the following benefits:+  Provides quick setup for EMR Studio if you already manage identities such as users and groups in IAM. <br />+  Works with identity providers that are compatible with OpenID Connect (OIDC) or Security Assertion Markup Language 2.0 (SAML 2.0). <br />+  Supports using multiple identity providers with the same AWS account. <br />+  Available in a wide number of AWS Regions. <br />+  Compliant with SOC 2.  | 
| New to AWS or Amazon EMR | [IAM Identity Center authentication mode](#emr-studio-enable-sso), which provides the following features:+  Supports easy user and group assignment to AWS resources. <br />+  Works with Microsoft Active Directory and SAML 2.0 identity providers. <br />+  Facilitates multi-account federation setup so that you don't have to separately configure federation for each AWS account in your organization.  | 

## Set up IAM authentication mode for Amazon EMR Studio
<a name="emr-studio-iam-authentication"></a>

With IAM authentication mode, you can use either IAM authentication or IAM federation. IAM *authentication* lets you manage IAM identities such as users, groups, and roles in IAM. You grant users access to a Studio with IAM permissions policies and [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html). IAM *federation* lets you establish trust between a third-party identity provider (IdP) and AWS so that you can manage user identities through your IdP.

**Note**  
If you already use IAM to control access to AWS resources, or if you've already configured your identity provider (IdP) for IAM, see [User permissions for IAM authentication mode](how-emr-studio-works.md#emr-studio-iam-authorization) to set user permissions when you use IAM authentication mode for EMR Studio.

### Use IAM federation for Amazon EMR Studio
<a name="emr-studio-iam-federation"></a>

To use IAM federation for EMR Studio, you create a trust relationship between your AWS account and your identity provider (IdP) and enable federated users to access the AWS Management Console. The steps you take to create this trust relationship differ depending on your IdP's federation standard.

In general, you complete the following tasks to configure federation with an external IdP. For complete instructions, see [Enabling SAML 2.0 federated users to access the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html) and [Enabling custom identity broker access to the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html) in the *AWS Identity and Access Management User Guide*.

1. Gather information from your IdP. This usually means generating a metadata document to validate SAML authentication requests from your IdP.

1. Create an identity provider IAM entity to store information about your IdP. For instructions, see [Creating IAM identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create.html).

1. Create one or more IAM roles for your IdP. EMR Studio assigns a role to a federated user when the user logs in. The role permits your IdP to request temporary security credentials for access to AWS. For instructions, see [Creating a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html). The permissions policies that you assign to the role determine what federated users can do in AWS and in an EMR Studio. For more information, see [User permissions for IAM authentication mode](how-emr-studio-works.md#emr-studio-iam-authorization).

1. (For SAML providers) Complete the SAML trust by configuring your IdP with information about AWS and the roles that you want federated users to assume. This configuration process creates *relying party trust* between your IdP and AWS. For more information, see [Configuring your SAML 2.0 IdP with relying party trust and adding claims](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.html).

**To configure an EMR Studio as a SAML application in your IdP portal**

You can configure a particular EMR Studio as a SAML application using a deep link to the Studio. Doing so lets users log in to your IdP portal and launch a specific Studio instead of navigating through the Amazon EMR console.
+ Use the following format to configure a deep link to your EMR Studio as a landing URL after SAML assertion verification. 

  ```
  https://console.aws.amazon.com/emr/home?region={{<aws-region>}}#studio/{{<your-studio-id>}}/start
  ```

## Set up IAM Identity Center authentication mode for Amazon EMR Studio
<a name="emr-studio-enable-sso"></a>

To prepare AWS IAM Identity Center for EMR Studio, you must configure your identity source and provision users and groups. Provisioning is the process of making user and group information available for use by IAM Identity Center and by applications that use IAM Identity Center. For more information, see [User and group provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/users-groups-provisioning.html#user-group-provision). 

EMR Studio supports using the following identity providers for IAM Identity Center:
+ **AWS Managed Microsoft AD and self-managed Active Directory** – For more information, see [Connect to your Microsoft AD directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-ad.html).
+ **SAML-based providers** – For a full list, see [Supported identity providers](https://docs.aws.amazon.com/singlesignon/latest/userguide/supported-idps.html).
+ **The IAM Identity Center directory** – For more information, see [Manage identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html).

**To set up IAM Identity Center for EMR Studio**

1. To set up IAM Identity Center for EMR Studio, you need the following:
   + A management account in your AWS organization if you use multiple accounts in your organization. 
**Note**  
You should only use your management account to enable IAM Identity Center and *provision* users and groups. After you set up IAM Identity Center, use a member account to create an EMR Studio and *assign* users and groups. To learn more about AWS terminology, see [AWS Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html). 
   + If you enabled IAM Identity Center before November 25, 2019, you might have to enable applications that use IAM Identity Center for the accounts in your AWS organization. For more information, see [Enable IAM Identity Center-integrated applications in AWS accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/app-enablement.html#enable-app-enablement).
   + Make sure that you have the prerequisites listed on the [IAM Identity Center prerequisites](https://docs.aws.amazon.com/singlesignon/latest/userguide/prereqs.html) page.

1. Follow the instructions in [Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/step1.html) to enable IAM Identity Center in the AWS Region where you want to create the EMR Studio.

1. Connect IAM Identity Center to your identity provider and provision the users and groups that you want to assign to the Studio.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-authentication.html)

You can now assign users and groups from your Identity Store to an EMR Studio. For instructions, see [Assign a user or group to an EMR Studio](emr-studio-manage-users.md#emr-studio-assign-users-groups).