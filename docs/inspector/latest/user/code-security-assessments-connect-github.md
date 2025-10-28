# Creating an integration between Amazon Inspector and GitHub

This topic describes how to create an integration between Amazon Inspector and GitHub.

###### Note

If this is your first time creating an integration, you're prompted to create a default scan configuration on Step 2.
When you [create a scan configuration](code-security-assessments-create-configuration.md "code-security-assessments-create-configuration.md"), you choose the scan frequency, scan analysis, and repositories to be scanned.
Creating a default scan configuration is the same as creating a general scan configuration.
However, the default scan configuration is automatically associated with any new and existing projects imported into Amazon Inspector.
If you want to create a default scan configuration, choose **Continue with this configuration**.
You can only create a default scan configuration once.
If you create a default scan configuration, you won't be prompted to create a default scan configuration again.
You can only create a default scan configuration once per account and once per organization.
If you don't want to configure a default scan configuration, choose **Skip configuration**.
However, will be prompted to create a default scan configuration the next time you create an integration.
After you create a default scan configuration or skip creating a default scan configuration, you're directed to Step 3 of the integration workflow where you enter your integration details.

Integrations with GitHub SaaS, GitHub Enterprise Cloud, and GitHub Enterprise Server require public internet access.

###### Note

Amazon Inspector only scans and monitors your default branch.
If you create a new default branch, Amazon Inspector scans and updates the new default branch.

###### Important

Before you finish creating the integration, you're directed to authorize the connection between Amazon Inspector and GitHub.
You must complete this step to finish the procedure.
If you close the pop-up, you will not be able to proceed.

###### To create an integration between Amazon Inspector and GitHub

1. Sign in using your credentials.
   Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. From the navigation pane, choose **Code Security**.
   Choose **Connect to**, and choose GitHub.
3. Under **Integration details**, enter the name of your integration, and choose **Connect to GitHub**.
4. Choose **Authorize** in the pop-up to create a connection between Amazon Inspector and GitHub.
5. In the success banner, choose **Go to GitHub connection creation page**.
6. Enter the installation ID for the GitHub application.
   If you installed the GitHub application, you can find the installation ID in GitHub from the **GitHub Apps** page or at the end of the GitHub application URL.
   If you haven't installed the GitHub application, choose **Install a new app**.
   This directs you to GitHub where you select the GitHub organization and specify the repository scope.
7. Choose **Connect to GitHub**.

After you create the integration, you can encounter a scenario where Amazon Inspector is unable to refresh the access token.
This can occur if the integration host is unavailable or Amazon Inspector experiences other communication issues.
To remediate the issue, you can re-authenticate the connection from the **Integrations** tab on the **Code Security** page.
Under the **Status** column, the integration shows as **Inactive**, and Amazon Inspector provides the option to re-authenticate.
Choose **Re-authenticate**.
You're redirected to the integration workflow where you can complete the connection setup.

If you delete system settings for your integration, you can lose connection indefinitely.
If this occurs, you must [delete the integration](code-security-assessments-connect-delete-integrations.md "code-security-assessments-connect-delete-integrations.md") and create a new integration.
When you delete an integration, you lose all projects and scan configurations associated with the integration.
