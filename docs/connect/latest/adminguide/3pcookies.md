

# Allow the Connect Customer Contact Control Panel (CCP) to access cookies
<a name="3pcookies"></a>

When logging into the CCP you might see one of these banners:

![A Grant access banner.](http://docs.aws.amazon.com/connect/latest/adminguide/images/3pcookies-default-grant-access.png)


OR

![A Grant access banner.](http://docs.aws.amazon.com/connect/latest/adminguide/images/3pcookies-custom-grant-access.png)


Connect Customer uses cookies for authentication. Google Chrome requires you to authorize the use of Connect Customer cookies.

1. When you log in to the CCP, on the **Allow access to cookies** banner choose **Grant access**.

1. At the next prompt, choose **Allow**.

You might need to repeat these steps periodically, for example, if your organization requires it every 30 days.

## What happens if you don't choose Grant access when prompted?
<a name="deny"></a>

If you don't choose **Grant access** when prompted, you won't be able to log into the CCP. To enable access outside of the login workflow, perform the following steps: 

1. Navigate to `chrome://settings/content/storageAccess`.

1. In the left navigation menu, choose **Privacy and security**.

1. Choose **Third-party cookies**.

1. Under **You blocked these sites from using info they've saved about you**, delete any entries associated with `awsapps.com` or `connect.aws` as shown in the following image.  
![A Grant access banner.](http://docs.aws.amazon.com/connect/latest/adminguide/images/3pcookies-delete.png)

1. You can close that instance of your browser.

1. Open your CCP. When prompted, choose **Grant access**, and then choose **Allow**.