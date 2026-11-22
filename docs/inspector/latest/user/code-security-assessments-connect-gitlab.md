

# Creating an integration between Amazon Inspector and GitLab Self-Managed

 This topic describes how to create an integration between Amazon Inspector and your code repository in GitLab Self-Managed. Amazon Inspector supports both public internet connectivity and secure private network connections for GitLab Self-Managed instances. 

**Required information**  
 The following is required when you create a connection: 
+  Integration name – This is the name added to the body of your integration. 
+  Endpoint URL – This is the URL used to access your GitLab Self-Managed instance. 
+  Personal access token – Create the personal access token in your GitLab Self-Managed instance from an administrator account. The token must include the following scopes: `api`, `read_api`, and `read_repository`. For steps to create a personal access token, see the GitLab documentation. 

**Note**  
 Amazon Inspector only scans and monitors your default branch. If you create a new default branch, Amazon Inspector scans and updates the new default branch. 

## Creating an integration between Amazon Inspector and GitLab Self-Managed
<a name="w2aac17c12c19c11"></a>

 The following procedure describes how to create a connection between Amazon Inspector and your code repository in GitLab Self-Managed. 

**Note**  
 If this is your first time creating an integration, you're prompted to create a default scan configuration on Step 2. When you [create a scan configuration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-create-configuration.html), you choose the scan frequency, scan analysis, and repositories to be scanned. Creating a default scan configuration is the same as creating a general scan configuration. However, the default scan configuration is automatically associated with any new and existing projects imported into Amazon Inspector. If you want to create a default scan configuration, choose **Continue with this configuration**. You can only create a default scan configuration once. If you create a default scan configuration, you won't be prompted to create a default scan configuration again. You can only create a default scan configuration once per account and once per organization. If you don't want to configure a default scan configuration, choose **Skip configuration**. However, you will be prompted to create a default scan configuration the next time you create an integration. After you create a default scan configuration or skip creating a default scan configuration, you're directed to Step 3 of the integration workflow where you enter your integration details. 

**Important**  
 Before you finish creating the integration, you're prompted to authorize the connection between Amazon Inspector and GitLab Self-Managed. You must complete this step to finish the procedure. If you close the pop-up, you will not be able to proceed. 

**To create a connection with GitLab Self-Managed**

1.  Sign in using your credentials. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home). 

1.  From the navigation pane, choose **Code Security**. Choose **Connect to** and choose **GitLab Self-Managed**. 

1.  Under **Integration details**, enter the following: 

   1.  For **Integration name**, enter the name added to the body of your integration. 

   1.  For **Endpoint URL**, enter the URL used to access your GitLab Self-Managed instance. 

   1.  For **Personal access token**, enter your personal access token with the required scopes. 

1.  For **Network accessibility**, choose one of the following options: 

   1.  **Public** – If your GitLab Self-Managed instance is accessible via the public internet, choose this option. 

   1.  **Private or behind a firewall** – If your GitLab Self-Managed instance is in a private network, choose this option and then select one of the following configuration methods: 
      +  **VPC Configuration** – Configure VPC settings by selecting from the dropdown lists: 
        +  **VPC ID** – Select the VPC where your GitLab Self-Managed instance is hosted. 
        +  **Subnet ID** – Select the subnet for network access. 
        +  **Security Groups** – Select the appropriate security groups for network access. 
        +  **GitLab Instance URL** – Provide the URL of your GitLab Self-Managed instance. 
      + **Code Connections** – Configure AWS CodeConnections by providing: 
        +  **Code Connections host** – Select an existing AWS CodeConnections host from the dropdown. 
        +  **VPC ID** – Provide the VPC ID where the AWS CodeConnection is hosted. 
        +  **VPC endpoint** – Specify the VPC endpoint for the connection. 

       If you use an interface VPC endpoint with private DNS enabled for Amazon Inspector webhook events, you must allow the Amazon Inspector hostname in GitLab Self-Managed. For more information, see [Allowing Amazon Inspector webhooks when you use an interface VPC endpoint with private DNS](#code-security-assessments-connect-gitlab-private-webhooks). 

1.  Choose **Connect** to GitLab. 

1.  Choose **Authorize** in the pop-up window to finish creating a connection between Amazon Inspector and GitLab. 

 After you create the integration, you can encounter a scenario where Amazon Inspector is unable to refresh the access token. This can occur if the integration host is unavailable or Amazon Inspector experiences other communication issues. To remediate the issue, you can re-authenticate the connection from the **Integrations** tab on the **Code Security** page. Under the **Status** column, the integration shows as **Inactive**, and Amazon Inspector provides the option to re-authenticate. Choose **Re-authenticate**. You're redirected to the integration workflow where you can complete the connection setup. 

 If you delete system settings for your integration, you can lose connection indefinitely. If this occurs, you must [delete the integration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-delete-integrations.html) and create a new integration. When you delete an integration, you lose all projects and scan configurations associated with the integration. 

## Allowing Amazon Inspector webhooks when you use an interface VPC endpoint with private DNS
<a name="code-security-assessments-connect-gitlab-private-webhooks"></a>

 Amazon Inspector registers webhooks on your GitLab Self-Managed instance. When you create the integration, Amazon Inspector adds a system hook to your instance. When you associate a scan configuration that has a merge request scan trigger with a project, Amazon Inspector also adds a webhook to that project. Both webhooks send events to the following Regional endpoint, where {{region}} is the AWS Region of your integration: 

```
https://inspector2-codesecurity-events.{{region}}.amazonaws.com
```

 If your instance reaches this endpoint through an interface VPC endpoint for `com.amazonaws.{{region}}.inspector2-codesecurity-events` with private DNS enabled, you must allow the Amazon Inspector hostname in GitLab Self-Managed. 

**Important**  
 When private DNS is enabled, the Amazon Inspector hostname resolves to private IP addresses in your VPC. By default, GitLab Self-Managed blocks project webhooks that send requests to private IP addresses, so you must allow the Amazon Inspector hostname for Amazon Inspector to add webhooks to your projects. 

 To allow the hostname, add `inspector2-codesecurity-events.{{region}}.amazonaws.com` to the allowlist for outbound requests to local IP addresses and domain names in the administrator settings of your GitLab Self-Managed instance. For more information, see the GitLab documentation about filtering outbound requests. We recommend that you allow only this hostname instead of allowing all webhooks and integrations to send requests to your local network. 

 After you allow the hostname, existing Amazon Inspector project webhooks deliver events again. If a project doesn't have an Amazon Inspector project webhook yet, Amazon Inspector adds it the next time you associate or update a scan configuration for that project. 