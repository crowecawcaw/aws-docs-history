

# Log in and log out of the Connect Customer CCP
<a name="ccp-login"></a>

Before you can log in to the Contact Control Panel (CCP), your administrator must give you the following information: 
+ The URL to launch the CCP:
  + https://{{instance name}}.my.connect.aws/ccp-v2/

  Where {{instance name}} is provided by your IT department or whoever set up Connect Customer for your business.
+ Your agent ID.
+ Your agent password.

**To log in**

After you have that information, here's how to log in and get started.

1. Make sure that your USB headset is securely connected to your computer.

1. Using Chrome or Firefox, open the CCP by using the URL that you received from your administrator.

1. Enter your agent ID and password, and then choose **Sign In**.  
![The login page for Connect Customer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/ccp-login.png)

1. If you're prompted to **Allow access to cookies**, choose **Grant access**, and then choose **Allow**.  
![A Grant access banner.](http://docs.aws.amazon.com/connect/latest/adminguide/images/3pcookies-default-grant-access.png)

   OR  
![A Grant access banner.](http://docs.aws.amazon.com/connect/latest/adminguide/images/3pcookies-custom-grant-access.png)

   Connect Customer uses cookies for authentication. Google Chrome requires you to authorize the use of Connect Customer cookies.
**Tip**  
**IT admins**: For more information, see [Using Connect Customer with third-party cookies](admin-3pcookies.md).

1. If you are prompted to allow access to your microphone and speaker, choose **Allow**.   
![The browser prompt to allow Connect Customer access to your microphone.](http://docs.aws.amazon.com/connect/latest/adminguide/images/ccp-allow-microphone.png)

You're all set to go\!

## Problems logging in?
<a name="problems-logging-in-CCP"></a>

If you have problems logging in to the CCP, contact your manager for help, or the IT Department for your organization.

**Note**  
If you see the **Session expired** message while logging in, you probably just need to refresh the session token. Go to your identity provider and log in. Refresh the Connect Customer page. If you still get this message, contact your IT team.

## Log out of the Connect Customer CCP
<a name="ccp-logout"></a>

**Important**  
Closing the CCP window or agent workspace doesn't automatically log out an agent. Agents must choose **Log out**. 

1. At the top of the CCP, choose **Settings**. 

1. Choose **Log out**.  
![The CCP, the settings icon in upper right corner.](http://docs.aws.amazon.com/connect/latest/adminguide/images/ccp-logout.png)