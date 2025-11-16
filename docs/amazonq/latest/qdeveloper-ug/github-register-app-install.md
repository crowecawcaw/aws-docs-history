# Increasing usage limits and configuring details

in Amazon Q Developer console

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

You can use Amazon Q Developer agents in GitHub for free without the need to set up an AWS account
to get started. You're provided with limited invocations per month for the feature development
and code review capabilities, as well as specified number of lines for code transformation per
month. You can increase your free usage at any time by registering your Amazon Q Developer app
installation with your AWS account.

By default, the **Code reviews**, **Feature
development**, and **Code transformation** features are enabled in
GitHub when you install the app. You can disable any of these features when you register.
Registering requires an Amazon Q Developer profile to manage the features from the console. The
profile stores your settings and code recommendation
customization.

###### Important

To register the app installation in the Amazon Q Developer console, you must meet the
requirements for the GitHub organization. For more information, see [Requirements to install a GitHub App](https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app "https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app") and [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations "https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations") in the _GitHub
documentation_.

###### To register your Amazon Q Developer installation

1. Navigate to the [Amazon Q Developer
   console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github "https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github"), and in the navigation pane, choose **Amazon Q Developer in
   GitHub**.
2. Choose **Register installation**, and then choose
   **Authorize** to be directed to GitHub.

If you previously authorized Amazon Q Developer to access your GitHub
organization, you'll be redirected back to the Amazon Q Developer console.
In this case, skip to step 4. 3. Sign in to your GitHub account using your GitHub credentials. If you have multiple
accounts, choose the account where you want to provide access to Amazon Q Developer. 4. Choose **Authorize Amazon Q Developer** to provide access to your GitHub
account. You'll be redirected back to Amazon Q Developer console after the authorization. 5. Enter details for an Amazon Q Developer profile.

If you previously created a profile when getting started with Amazon Q Developer, skip to step 6. To learn more about the profile, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md "subscribe-understanding-profile.md").

    1. Under **Amazon Q Developer profile**, enter your profile details.


    	1. In the **Profile name** text input field, enter a name that
    	 can be recognized and referenced. Consider including the region so the profile
    	 name can be properly identified (example: "QDevProfile\_us-east-1").
    	2. (Optional) Choose **Additional settings**, and in the
    	 **Profile description - optional** text input field, enter a
    	 description for your profile to provide context and identify your profile.

6. Under **Registration details**, enter your GitHub details, optionally
   configure the code reviews feature, and add tags.
   1. In the **Registration name** text input filed, enter a name for
      your app installation.
   2. (Optional) In the **Organization name -
      _optional_** text input field, enter a name for the
      organization associated with the app installation.
   3. (Optional) Under **Features**, configure the **Code
      reviews** feature by choosing the toggle to enable or disable the feature.
      **Feature development** and **Code
      transformation** configuration cannot be
      modified.
      The features are enabled by default.
   4. (Optional) Under **Tags - optional**, choose **Add new
      tag** to add a tag that can help to search and filter your AWS resources
      in GitHub.

7. Choose **Register** to create an Amazon Q Developer profile and register your
   app installation in GitHub with your AWS account.
   After you successfully create an Amazon Q Developer profile and register the app installation in
   GitHub, you can view the registration details. You can still enable or disable features, as well
   as add tags at a later time. You can also delete a GitHub app installation. For more information
   [Configuring registered installation details](github-configuration.md "github-configuration.md").
