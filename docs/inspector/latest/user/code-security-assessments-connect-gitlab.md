

# Creating an integration between Amazon Inspector and GitLab Self Managed
<a name="code-security-assessments-connect-gitlab"></a>

 This topic describes how to create an integration between Amazon Inspector and your code repository in GitLab Self Managed. 

**Required information**  
 The following is required when you create a connection: 
+  Integration name – This is the name added to the body of your integration. 
+  Endpoint URL – This is the URL used to access your GitLab Self Managed instance. 
+  Personal access token – The personal access token is [created in GitLab Self Managed](https://docs.gitlab.com/user/profile/personal_access_tokens/) from an administrator account and must include the following scopes: `api`, `read_api`, and `read_repository`. 

**Note**  
 Amazon Inspector only scans and monitors your default branch. If you create a new default branch, Amazon Inspector scans and updates the new default branch. 

## Creating an integration between Amazon Inspector and GitLab Self Managed
<a name="w2aac17c10c17c11"></a>

 The following procedure describes how to create a connection between Amazon Inspector and your code repository in GitLab Self Managed. 

**Note**  
 If this is your first time creating an integration, you're prompted to create a default scan configuration on Step 2. When you [create a scan configuration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-create-configuration.html), you choose the scan frequency, scan analysis, and repositories to be scanned. Creating a default scan configuration is the same as creating a general scan configuration. However, the default scan configuration is automatically associated with any new and existing projects imported into Amazon Inspector. If you want to create a default scan configuration, choose **Continue with this configuration**. You can only create a default scan configuration once. If you create a default scan configuration, you won't be prompted to create a default scan configuration again. You can only create a default scan configuration once per account and once per organization. If you don't want to configure a default scan configuration, choose **Skip configuration**. However, you will be prompted to create a default scan configuration the next time you create an integration. After you create a default scan configuration or skip creating a default scan configuration, you're directed to Step 3 of the integration workflow where you enter your integration details. 

**Important**  
 Before you finish creating the integration, you're prompted to authorize the connection between Amazon Inspector and GitLab Self Managed. You must complete this step to finish the procedure. If you close the pop-up, you will not be able to proceed. 

**To create a connection with GitLab Self Managed**

1.  Sign in using your credentials. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home). 

1.  From the navigation pane, choose **Code Security**. Choose **Connect to** and choose **GitLab Self Managed**. 

1.  Under **Integration details**, enter the following: 

   1.  For **Integration name**, enter the name added to the body of your integration. 

   1.  For **Endpoint URL**, enter the URL used to access your GitLab self-managed instance. 

   1.  For **Personal access token**, enter your personal access token with the required scopes. 

1.  Choose connect to GitLab. 

1.  Choose **Authorize** in the pop-up window to finish creating a connection between Amazon Inspector and GitLab. 

 After you create the integration, you can encounter a scenario where Amazon Inspector is unable to refresh the access token. This can occur if the integration host is unavailable or Amazon Inspector experiences other communication issues. To remediate the issue, you can re-authenticate the connection from the **Integrations** tab on the **Code Security** page. Under the **Status** column, the integration shows as **Inactive**, and Amazon Inspector provides the option to re-authenticate. Choose **Re-authenticate**. You're redirected to the integration workflow where you can complete the connection setup. 

 If you delete system settings for your integration, you can lose connection indefinitely. If this occurs, you must [delete the integration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-delete-integrations.html) and create a new integration. When you delete an integration, you lose all projects and scan configurations associated with the integration. 