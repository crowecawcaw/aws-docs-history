# Configuring Jira Cloud

Before you can use AWS Glue to transfer data from Jira Cloud to supported destinations, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have an Atlassian account where you use the Jira software product in Jira Cloud. For more information, see [Creating a Jira Cloud account](#jira-cloud-configuring-creating-jira-cloud-account "#jira-cloud-configuring-creating-jira-cloud-account").
- You must have an AWS account created with the service access to AWS Glue.
- This app provides the client credentials that AWS Glue uses to access your data securely when it makes authenticated calls to your account. For more information, see [Enabling OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#enabling-oauth-2-0--3lo- "https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#enabling-oauth-2-0--3lo-") in the Atlassian Developer documentation.

If you meet these requirements, you’re ready to connect AWS Glue to your Jira Cloud account.

## Creating a Jira Cloud account

To create a Jira Cloud account:

1. Navigate to the [Atlassian sign up URL](https://id.atlassian.com/signup "https://id.atlassian.com/signup").
2. Enter your work email and name and choose **Agree**. You receive a verification email.
3. After verifying your email, you can create a password and choose **Sign up**.
4. Enter name and password, and choose **Sign up**.
5. You are redirected to a page where you need to enter your site. Enter a site name and choose **Agree**.

Once your Atlassian Cloud site starts up, you can set up your Jira by answering a few questions as per your project type preferences.

To log in to an existing account:

1. Navigate to the [Atlassian login URL](https://id.atlassian.com/login "https://id.atlassian.com/login") and enter credentials.
2. Enter email and password and click **Log in**. You are redirected to the Jira dashboard.

## Creating an app in your Jira Cloud

To create an app in Jira Cloud and obtain the Client ID and Client Secret from the managed client app:

1. Navigate to the [Jira Cloud URL](https://id.atlassian.com/login "https://id.atlassian.com/login") and enter credentials.
2. Choose **Create** and select the **OAuth 2.0 integration** option.
3. Enter the app name, check **T&C** and choose **Create**.
4. Navigate to the **Distribution** section in the left menu and choose **Edit**.
5. In the **Edit distribution controls** section:
   1. Select **DISTRIBUTION STATUS** as **Sharing**.
   2. Enter the vendor name.
   3. Enter the URL for your **Privacy policy**. For example, https://docs.aws.amazon.com/glue/latest/dg/security-iam-awsmanpol.html
   4. Enter the URL for your **Terms of service** (optional).
   5. Enter the URL for your **Customer support contact** (optional).
   6. Select Yes/No from the **PERSONAL DATA DECLARATION** and choose **Save changes**.

6. Navigate to **Permissions** in the left menu for the respective app.
7. For **Jira API**, choose **Add**. Once added, choose the **Configuration** option.
8. Under the **Classic scopes** > **Jira platform REST API** section choose **Edit Scopes**. and check all scopes. Click **Save**.
9. Under **Granular Scopes** choose **Edit Scopes** and select the following scopes:
10. Scroll down and find scopes. There are two kinds of scopes you must select under headings "CRM" and "Standard".
11. Add the following scopes:

```
read:application-role:jira
read:audit-log:jira
read:avatar:jira
read:field:jira
read:group:jira
read:instance-configuration:jira
read:issue-details:jira
read:issue-event:jira
read:issue-link-type:jira
read:issue-meta:jira
read:issue-security-level:jira
read:issue-security-scheme:jira
read:issue-type-scheme:jira
read:issue-type-screen-scheme:jira
read:issue-type:jira
read:issue.time-tracking:jira
read:label:jira
read:notification-scheme:jira
read:permission:jira
read:priority:jira
read:project:jira
read:project-category:jira
read:project-role:jira
read:project-type:jira
read:project-version:jira
read:project.component:jir
read:project.property:jira
read:resolution:jira
read:screen:jira
read:status:jira
read:user:jira
read:workflow-scheme:jira
read:workflow:jira
read:field-configuration:jira
read:issue-type-hierarchy:jira
read:webhook:jira

```

12. Navigate to **Authentication** in the left menu and choose **Add**.
13. Enter a **Callback URL** such as https://us-east-1.console.aws.amazon.com/gluestudio/oauth
14. Navigate to **Settings** in the left menu and scroll down for **Authentication** details. Note the Client ID and Secret.
