

# Creating a new Intercom account and configuring the client app
<a name="intercom-new-account-creation"></a>

**Creating a Intercom account**

1. Choose on the [Intercom URL](https://app.intercom.com/) and choose **Start my free trial** on right upper corner of the page.

1. Choose **Try for free button** on right upper corner of the page.

1. Choose the business type you require. 

1. Enter all the information required on the page.

1. After entering all the information, choose **Register**.



**Creating an Intercom developer app**

To get the **Client Id** and **Client Secret**, you create a developer account.

1. Navigate to [https://app.intercom.com/](https://app.intercom.com/).

1. Enter the Email ID and Password/ Sign In Using Google and log in.

1. Choose **user profile** on the left bottom corner and choose settings.

1. Choose **Apps & Integration**.

1. Choose the **Developer Hub** tab under **Apps & Integration**.

1. Choose **New app** and create the app here.

1. Provide the app name and choose **Create** app.

1. Inside the app, navigate to the **Authentication** section.

1. Choose the **edit** and add redirect URIs. Add the your region-specific Redirect URL as `https://<aws-region>.console.aws.amazon.com/gluestudio/oauth`. For example, add `https://us-east-1.console.aws.amazon.com/gluestudio/oauth for the us-east-1 region`.

1. Get the generated **Client Id** and **Client Secret** in the Basic Information Section.