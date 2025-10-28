# Creating a new Intercom account and configuring the client app

######

Creating a Intercom account

1. Choose on the [Intercom URL](https://app.intercom.com/ "https://app.intercom.com/") and choose
   **Start my free trial** on right upper corner of the page.
2. Choose **Try for free button** on right upper corner of the page.
3. Choose the business type you require.
4. Enter all the information required on the page.
5. After entering all the information, choose **Register**.

######

Creating an Intercom developer app

To get the **Client Id** and **Client Secret**, you create a developer account.

1. Navigate to [https://app.intercom.com/](https://app.intercom.com/ "https://app.intercom.com/").
2. Enter the Email ID and Password/ Sign In Using Google and log in.
3. Choose **user profile** on the left bottom corner and choose settings.
4. Choose **Apps & Integration**.
5. Choose the **Developer Hub** tab under **Apps & Integration**.
6. Choose **New app** and create the app here.
7. Provide the app name and choose **Create** app.
8. Inside the app, navigate to the **Authentication** section.
9. Choose the **edit** and add redirect URIs. Add the your region-specific Redirect URL as
   `https://<aws-region>.console.aws.amazon.com/gluestudio/oauth`. For example, add
   `https://us-east-1.console.aws.amazon.com/gluestudio/oauth for the us-east-1 region`.
10. Get the generated **Client Id** and **Client Secret** in the Basic
    Information Section.
