

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Tutorial: Creating an Amazon FinSpace environment with AD FS
<a name="tutorial-idp-ADFS-sso"></a>

**Important**  
Amazon FinSpace Dataset Browser will be discontinued on {{March 26, 2025}}. Starting {{November 29, 2023}}, FinSpace will no longer accept the creation of new Dataset Browser environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/) will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/) or contact [AWS Support](https://aws.amazon.com/contact-us/) to assist with your transition.

The following tutorial walks you through how Amazon FinSpace environment can be created using Microsoft Active Directory Federation Services (AD FS) as an Identity provider (IdP).

**Note**  
You need to have appropriate privileges in AD FS to create a SAML application.

## Prerequisites
<a name="prerequisites-4"></a>

Ensure that a user exists in AD FS for each person who will need access to FinSpace. When creating users, make sure to include an email address for each user. Email addresses are required to connect the users in AD FS with their corresponding users in FinSpace.

## Step 1: Access the SAML metadata document or URL from AD FS
<a name="step-1-access-the-saml-metadata-document-or-url-from-ad-fs"></a>

Access the SAML metadata document or URL from your AD FS installation. You will need this document or URL to create the FinSpace environment.

## Step 2: Creating a FinSpace environment
<a name="step-2-creating-a-finspace-environment-3"></a>

**To create a FinSpace environment**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Create Environment**.

1. Enter a name for your FinSpace environment under **Environment name**. For example, enter `finspace-saml-adfs`.

1. (Optional) Add **Environment description**.

1. Select an existing or create a new KMS key to encrypt data in your FinSpace environment. For more information, see [Managing keys](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html).

1. For **Authentication method**, select **Single Sign On (SSO)**.

1. Enter your **Identity provider name**. For example, `AD FS`.

1. For **Metadata document URL**, select **Provide a metadata document URL** and then paste the SAML metadata document URL in the text box.

1. For **Attribute mapping**, enter the attribute set for email in AD FS. It should be `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`.

1. Choose **Create Environment**. The environment creation process starts and it will take 50-60 minutes to finish in the background. You can return to other activities while the environment is being created.

1. After the FinSpace environment is ready, copy and save the **Redirect / Sign-in URL** and **URN**.

## Step 3: Configure AD FS for FinSpace
<a name="step-3-configure-ad-fs-for-finspace"></a>

**To configure ADFS for FinSpace**

1. Sign in to your AD FS console.

1. Go to **Server Manager**.

1. From the top-right drop down menu, choose **Tools**.

1. Choose **AD FS management**.

1. From the left menu, choose **Relying Party Trusts**.

1. Choose **Add Relying Party Trust**.

1. From the dialog box, choose **Claims Aware**.

1. Choose **Enter data about the relying party manually**.

1. For display name, enter `FinSpace` and then choose **Next**.

1. Choose **Enable support for the SAML 2.0 WebSSO protocol**.

1. Paste the **Redirect / Sign-in URL** and then choose **Next**.

1. Paste the **URN** under the **Relying party trust identifier**.

1. Choose **Add** and then choose **Next**.

1. Choose **Close**. You will see **FinSpace** in the list of **Relying Party Trusts**.

1. Right-click on **FinSpace** and choose **Edit Claim Issuance Policy**.

1. On the next page, chose **Add Rule**.

1. Under **Claim Rule Template**, choose **Send LDAP Attributes as Claims**.

1. Choose **Next**.

1. For **Claim rule name**, enter rule name as `emailclaimrule`.

1. Under **Attribute store**, choose **Active Directory**.

1. Under **Mapping of LDAP attributes to outgoing claim types**, set the LDAP attributes as following:

   1. For **LDAP attribute**, enter `E-mail-Addresses` and for **Outgoing Claim Type** , enter `E-mail Address`.

   1. Repeat the above step to set **LDAP attribute**, as `E-mail-Addresses` and **Outgoing Claim Type** as `Name ID`.

1. Choose **Finish** and then choose **OK**.

## Step 4: Assign user in AD FS
<a name="step-4-assign-user-in-ad-fs"></a>

Ensure that any user to be enabled for FinSpace has a valid email in their user record in AD FS.

## Step 5: Create superuser in your FinSpace environment
<a name="step-5-create-superuser-in-your-finspace-environment-3"></a>

**To create a superuser**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose `finspace-saml-adfs` from the list of environments.

1. Under **Superusers**, choose **Add Superuser**.

1. On **Specify Superuser details** page, enter the email that was used when assigning the user in AD FS.

1. Enter the **First name** and the **Last name**.

1. Choose **Create and view credentials**. You will not receive a password as you will use the IAM Identity Center credentials for authentication.

## Step 6: Sign in to FinSpace with AWS SSO credentials
<a name="step-6-sign-in-to-finspace-with-aws-sso-credentials-2"></a>

**To sign in with IAM Identity Center credentials**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose `finspace-saml-adfs` from the list of environments.

1. Copy the link under **Domain** and paste it in your web browser.

   You will be re-directed to your AD FS authentication page.

1. Enter your SSO credentials to sign in to FinSpace.