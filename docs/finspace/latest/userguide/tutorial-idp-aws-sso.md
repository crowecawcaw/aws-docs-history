

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Tutorial: Creating an Amazon FinSpace environment with IAM Identity Center
<a name="tutorial-idp-aws-sso"></a>

**Important**  
Amazon FinSpace Dataset Browser will be discontinued on {{March 26, 2025}}. Starting {{November 29, 2023}}, FinSpace will no longer accept the creation of new Dataset Browser environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/) will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/) or contact [AWS Support](https://aws.amazon.com/contact-us/) to assist with your transition.

The following tutorial walks you through how FinSpace environment can be created using AWS IAM Identity Center as an Identity provider (IdP).

## Prerequisites
<a name="prerequisites-3"></a>

Ensure that a user exists in IAM Identity Center for each person who will need access to FinSpace. When creating users, make sure to include an email address for each user. Email addresses are required to connect the users in Active Directory Federation Services with their corresponding users in FinSpace.

## Step 1: Creating an application in IAM Identity Center
<a name="step-1-creating-an-application-in-aws-sso"></a>

**Note**  
You need to have appropriate privileges in IAM Identity Center to create a SAML application.

**To create an application in IAM Identity Center**

1. Sign in to AWS Management Console, and open IAM Identity Center.

1. Choose **Settings**.

1. For **Identity source**, choose **IAM Identity Center**.

1. From the left menu, choose **Applications**.

1. Choose **Add application**.

1. Choose **Add a custom SAML 2.0 application**.

1. Choose **Next**.

1. On the **Configure application** page, specify a display name for the application. For example, you can use `FinSpace-SAML-application`.

1. (Optional) Add a description.

1. Copy and save the URL for **IAM Identity Center SAML metadata file** or download it. You will need it when you create a FinSpace environment.

1. For **Application metadata**, choose **Manually type your metadata values**.

1. For **Application ACS URL**, enter `https://finspace.com/saml2/idpresponse`. For **Application SAML audience**, enter `urn:amazon:sp:*`.
**Note**  
These are sample values. Return to application configuration and replace these fields with the actual values after you create an environment. 

1. Choose **Submit**. The page for newly created application opens.

1. On the application page, choose **Actions** and then choose **Edit attribute mappings**.

1. On the attribute mappings page, enter the attribute mappings values as shown in the following screenshot.  
![A screenshot that shows the attribute mappings.](http://docs.aws.amazon.com/finspace/latest/userguide/images/09-security/finspace-security-attribute-mapping.png)

1. Choose **Save changes**.

Now that you have the SAML metadata document or it's URL, create a FinSpace environment next.

## Step 2: Creating a FinSpace environment
<a name="step-2-creating-a-finspace-environment-2"></a>

**To create a FinSpace environment**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Create Environment**.

1. Enter a name for your FinSpace environment under **Environment name**. For example, enter `finspace-saml-aws-sso` 

1. (Optional) Add **Environment description**.

1. Select an existing or create a new KMS key to encrypt data in your FinSpace environment. For more information, see [Managing keys](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html).

1. For **Authentication method**, select **Single Sign On (SSO)**.

1. Enter your **Identity provider name**. For example, **IAM Identity Center**.

1. For **Metadata document URL**, choose **Provide a metadata document URL** and then paste the SAML metadata document URL in the text box. This is the same URL that you copied when [creating an application](#metadata-url).

1. For **Attribute mapping**, enter the attribute set for email in IAM Identity Center. Since you set attribute as `Email` in SSO, set the same in mapping.

1. Choose **Create Environment**. The environment creation process starts and it will take 50-60 minutes to finish in the background. You can return to other activities while the environment is being created.

1. After the FinSpace environment is ready, copy and save the **Redirect / Sign-in URL** and **URN**.

## Step 3: Finish application configuration in IAM Identity Center
<a name="step-3-finish-application-configuration-in-aws-sso"></a>

Finish configuration of IAM Identity Center app with the **Redirect / Sign-in URL** and **URN**.

1. Sign in to AWS Management Console, and open IAM Identity Center.

1. Choose **Applications**.

1. Choose **FinSpace-SAML-application** that you created in step 1 of this tutorial.

1. On the application details page, choose **Actions** and then choose **Edit configuration**.

1. In the **Application metadata** section, paste the following values that you copied in step 2 of this tutorial.

   1. For **Application ACS URL**, paste the **Redirect / Sign-in URL**.

   1. For **Application SAML audience**, paste the **URN**.

1. Choose **Submit**.

## Step 4: Assign user to the FinSpace application in IAM Identity Center
<a name="step-4-assign-user-to-the-finspace-application-in-aws-sso"></a>

After setting up the application, assign at least one user to it in IAM Identity Center. You can create this user as a superuser for FinSpace.

**To assign a user**

1. Sign in to AWS Management Console, and open IAM Identity Center.

1. Choose **Applications**.

1. Choose the `FinSpace-SAML-application` application.

1. Choose **Assign Users**.

1. From the list of users, choose and assign users to the application.

## Step 5: Create superuser in your FinSpace environment
<a name="step-5-create-superuser-in-your-finspace-environment-2"></a>

After assigning a user,you can create them as a superuser in FinSpace.

**To create a superuser**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose `finspace-saml-aws-sso` from the list of environments.

1. Under **Superusers**, choose **Add Superuser**.

1. On the **Specify Superuser details** page, enter the email that was used when assigning the user in IAM Identity Center.

1. Enter the **First name** and the **Last name**.

1. Choose **Next**.

1. Review the details and choose **Create and view credentials**. You will not receive a password as you will use the IAM Identity Center credentials for authentication.

## Step 6: Sign in to FinSpace with IAM Identity Center credentials
<a name="step-6-sign-in-to-finspace-with-aws-sso-credentials"></a>

**To sign in with IAM Identity Center credentials**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose `finspace-saml-aws-sso` from the list of environments.

1. Choose the **Application URL** link.

   The IAM Identity Center authentication page opens.

1. Enter your SSO credentials to sign in to FinSpace.