

# Connecting to Monday
<a name="connecting-to-monday"></a>

 Monday.com is a versatile work operating system that streamlines project management and team collaboration. It features customizable workflows, visual dashboards, and automation tools to enhance productivity. Users can track tasks, manage resources, and communicate effectively in one integrated platform. 

**Topics**
+ [AWS Glue support for Monday](monday-support.md)
+ [Policies containing the API operations for creating and using connections](monday-configuring-iam-permissions.md)
+ [Configuring Monday](monday-configuring.md)
+ [Configuring Monday connections](monday-configuring-connections.md)
+ [Reading from Monday entities](monday-reading-from-entities.md)
+ [Monday connection option reference](monday-connection-options.md)
+ [Limitations](monday-connector-limitations.md)
+ [Create a new Monday account:](#monday-account-creation)

## Create a new Monday account:
<a name="monday-account-creation"></a>

1.  Navigate to Monday’s homepage, [https://monday.com/](https://monday.com/) and choose **Login**. 

1.  You will be re-directed to the login page. On the bottom of the page, choose **Sign up**. 

1.  Enter your email address and choose **Continue**. Alternately, you can sign in with Google. 

1.  Enter the required details and choose **Continue**. 

1.  Complete the survey questions and follow the steps to complete the account creation process. 

**Register an OAuth application:**

1.  Log into your monday.com account. Click on your avatar (picture icon) in the bottom left corner of your screen. 

1.  Choose **Developer**. 

1.  Choose **Create app**. 

1.  Complete the required fields for name and description. 

1. Navigate to “OAuth” section present on the right side add the scopes and choose “Save Feature”.

1.  Navigate to “Redirect URLS” tab beside the scope and add the redirect URL and choose “Save Feature”. 

1.  Under the **Redirect URLs** tab, provide the URL of your app. This should be https://{region-code}.console.aws.amazon.com/appflow/oauth. For example, if you are using `us-east-1 `you can add `https://us-east-1.console.aws.amazon.com/appflow/oauth`. 

1.  The application is now ready to use. You can find your credentials, in the “Basic Information” section. Note your Client ID and Client secret strings. These strings are used to make a connection with this app using an AppFlow connector. 

**Generate personal access token:**

 Currently, monday.com only offers our V2 API tokens, which are all personal tokens. To access your API tokens, you can use one of two methods depending on your user level. Admin users can utilize both methods to acquire their API tokens. Member users can access their API tokens from their Developer tabs. 

 Admins - If you are an admin user on your monday.com account,you can access your API tokens from the "Admin" tab with the following steps: 

1.  Log into your monday.com account. Click on your avatar (picture icon) in the bottom left corner of your screen. 

1.  Select “Administration” from the resulting menu (this requires you to have admin permissions). 

1.  Navigate to the “API”Section and generate a “API V2 Token”. You can copy your token and use it. 

 Developer - If you are a member user on your monday.com account, you can access your API tokens from the Developer tab with the following steps: 

1.  Log into your monday.com account. Click on your avatar (picture icon) in the bottom left corner of your screen. 

1.  Select “Developers” from the resulting menu. 

1.  In the top menu, choose the "Developer" drop-down menu. Select the first option on the drop-down menu titled "My Access Tokens." 