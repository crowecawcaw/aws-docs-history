After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Tutorial: Setup an Identity Provider with your

Amazon FinSpace environment

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

You can integrate any SAML 2.0 compliant IdP when creating a new Amazon FinSpace
environment.

## Prerequisites

Before creating a FinSpace environment with SAML based SSO, do the
following:

Inside your organization's network, configure your identity store, such as
Windows Active Directory, to work with a SAML-based IdP. SAML based IdPs include
Microsoft Windows Active Directory Federation Services, Okta, and so on.

## Step 1: Generate a SAML

metadata document

Using your IdP, generate a metadata document that describes your organization
as an identity provider. You will need the metadata document or the URL to the
metadata document when creating the FinSpace environment.

## Step 2: Determine

the SAML attribute for email

Determine the SAML attribute name that contains the email address in the SAML
assertion. Email address is required to identify the user in FinSpace. For example,
`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`.
Check your IdP documentation for details. You will need the SAML attribute when
creating the FinSpace environment.

## Step 3: Create a

FinSpace environment

Create a [FinSpace
environment](create-an-amazon-finspace-environment.md "create-an-amazon-finspace-environment.md"). Once the FinSpace environment is ready, copy and save the
**Redirect / Sign-in url** and **URN** from
the Summary section of the environment page. You will need the parameters for
configuration in the IdP.

## Step 4: Create an application for FinSpace in your IdP

Once the environment is created, add an application for FinSpace in your IdP and
use the **Redirect / Sign-in url** and **URN**
where appropriate.

## Step 5: Assign users to the newly created FinSpace application in your IdP

Once the application is added, assign users to the application in IdP. A
minimum of one user is required to create a superuser in FinSpace.

## Step 6: Create a superuser in your FinSpace environment

###### Note

In order to create a FinSpace environment, you need to be a user with **AdministratorAccess** role or FinSpace policy.

Now that the users are assigned to your FinSpace application in your IdP, create a
superuser.

After your FinSpace is created, you must create a first superuser to add additional
users and to configure permission groups from within the FinSpace web application. A
superuser has all permissions to take all actions in FinSpace. The first superuser
must be created in the AWS console page. After the superuser is created, the
superuser logs in to the FinSpace web application for the first time.

###### To create a superuser

1. Sign in to your AWS account in which the FinSpace environment was created
   and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing"). Your AWS
   account number is displayed for verification purposes.
2. Choose **Environments** and select the FinSpace environment
   for which a superuser will be created.
3. Under **Superusers**, choose **Add
   Superuser**.
4. On **Specify Superuser details** page, enter the
   **Email address**, **First name**, and
   **Last name**.
5. Choose **Next**.
6. On the next page, review the superuser details.
7. Choose **Create and view credentials** to get a
   temporary password.

###### Note

If you have created an environment with SSO, you will not get a
temporary password as you will be authenticated with your IdP. 8. On the **View Credentials** page, view and copy the
superuser security credentials. You also get a welcome message which you can
use to email users instructions for signing into FinSpace.

Share these credentials with the person designated as the superuser. The
credentials are necessary to sign in to your FinSpace web application. The
**Environment domain** is the sign-in url for your FinSpace
web application.

###### Note

This is the last time these credentials will be available to be
copied. However, you can create new credentials at any time.

You have successfully created a FinSpace environment configured with your SAML 2.0
IdP. Learn more about [managing users in
SSO](managing-user-sso.md "managing-user-sso.md") and [permissions](managing-user-permissions.md "managing-user-permissions.md").
