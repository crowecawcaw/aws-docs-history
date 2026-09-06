

# Log in to the AWS Security Agent web application
<a name="login-web-app"></a>

You should log in to the AWS Security Agent web application to complete tasks such as:
+ Perform a design review
+ Perform a penetration test

## Access methods
<a name="_access_methods"></a>

AWS Security Agent provides different methods to access the web application, depending on how your organization configured access during initial setup and whether you have AWS Console access.

 **IAM Identity Center (SSO)** - If your organization enabled IAM Identity Center, you can log in using your SSO credentials. You must be assigned to at least one Agent Space in IAM Identity Center before you can access the web application.

 **Admin access (IAM)** - If you have AWS Console access with appropriate permissions, you can launch the web application through the admin access link on any Agent Space page. This method provides authentication through your existing Console session.

**Note**  
The primary access method your organization uses was determined during initial AWS Security Agent setup. For information on configuring user access and assignments, see [Grant users access to the AWS Security Agent web application](grant-user-access.md).

## Log in with IAM Identity Center (SSO)
<a name="_log_in_with_iam_identity_center_sso"></a>

If your organization configured IAM Identity Center access, you can log in to the web application using your SSO credentials through multiple entry points.

### Prerequisites
<a name="_prerequisites"></a>
+ You have been assigned to at least one Agent Space in IAM Identity Center
+ You have your IAM Identity Center SSO credentials

### Access the web application
<a name="_access_the_web_application"></a>

Choose one of the following methods based on your needs:

 **To view all Agent Spaces you’re assigned to:** 

1. In the AWS Security Agent console, navigate to **Settings**.

1. Locate the **Web application domain** and copy the URL.
**Tip**  
Bookmark this URL for easy access. This is the universal entry point to view all Agent Spaces you’re assigned to.

1. Navigate to the web application URL.

1. Enter your IAM Identity Center credentials when prompted.

1. After authentication, you’ll see a list of all Agent Spaces you’re assigned to.

1. Select the Agent Space you want to work in.

 **To access a specific Agent Space directly (requires AWS Console access):** 

1. Log into the AWS Management Console.

1. Navigate to the AWS Security Agent console.

1. Navigate to the Agent Space you want to access.

1. Choose one of the following:
   +  **Launch web application** button on the Agent Space overview page
   +  **Launch web app** button in the Code review section
   +  **Launch web app** button in the Penetration testing section

1. Enter your IAM Identity Center credentials when prompted.

1. After authentication, you’ll be taken directly to that Agent Space in the web application.

**Note**  
If you don’t have AWS Console access, use the web application domain from the Settings page to access all your assigned Agent Spaces.

## Log in with admin access (IAM)
<a name="_log_in_with_admin_access_iam"></a>

If you have AWS Console access with appropriate AWS Security Agent permissions, you can launch the web application through the admin access link with automatic authentication.

### Prerequisites
<a name="_prerequisites_2"></a>
+ You are logged into the AWS Management Console
+ You have appropriate permissions to access AWS Security Agent resources

### Access the web application
<a name="_access_the_web_application_2"></a>

Choose one of the following methods:

 **To access a specific Agent Space:** 

1. Log into the AWS Management Console.

1. Navigate to the AWS Security Agent console.

1. Navigate to the Agent Space you want to access.

1. Choose the **Admin access** button on the Agent Space overview page.

1. The web application opens in a new tab with automatic authentication for that Agent Space.

**Note**  
The admin access button is always available to users with AWS Console access, regardless of whether your organization uses IAM Identity Center as the primary access method.