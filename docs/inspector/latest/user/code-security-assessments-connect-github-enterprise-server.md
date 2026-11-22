

# Creating an integration between Amazon Inspector and GitHub Enterprise Server

 This topic describes how to create an integration between Amazon Inspector and GitHub Enterprise Server. Amazon Inspector supports integrations with GitHub Enterprise Server through both public and private network connections. 

**Note**  
 If this is your first time creating an integration, you're prompted to create a default scan configuration in Step 2 of the following procedure. When you [create a scan configuration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-create-configuration.html), you choose the scan frequency, scan analysis, and repositories to scan. A default scan configuration works the same as a general one, except that it's automatically associated with any new and existing projects imported into Amazon Inspector. You can create only one default scan configuration per account and per organization. To create one now, choose **Continue with this configuration**. To skip this step, choose **Skip configuration**; you're prompted again the next time you create an integration. After you complete or skip this step, you're directed to Step 3 of the integration workflow, where you enter your integration details. 

 For GitHub Enterprise Server, you can choose between public internet connectivity or secure private network connections using AWS CodeConnections. 

## Private network connectivity for GitHub Enterprise Server
<a name="w2aac17c12c17b9"></a>

 For organizations that host GitHub Enterprise Server in private networks, Amazon Inspector supports secure connections through VPC configurations or AWS CodeConnections. This approach allows you to scan your repositories without opening your firewalls to the entire AWS IP address range. 

**To configure the GitHub Enterprise Server connection**

1.  Sign in using your credentials. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home). 

1.  From the navigation pane, choose **Code Security**. Choose **Connect to**, and choose GitHub Enterprise Server. 

1.  Under **Integration details**, enter the name of your integration. 

1.  For **Network accessibility**, choose one of the following options: 

   1.  **Public** – If your GitHub Enterprise Server instance is accessible via the public internet, choose this option. 

   1.  **Private or behind a firewall** – If your GitHub Enterprise Server instance is in a private network, choose this option and then select one of the following configuration methods: 
      +  **VPC Configuration** – Configure VPC settings by selecting from the dropdown lists: 
        +  **VPC ID** – Select the VPC where your GitHub Enterprise Server instance is hosted. 
        +  **Subnet ID** – Select the subnet for network access. 
        +  **Security Groups** – Select the appropriate security groups for network access. 
        +  **GitHub Enterprise Server URL** – Provide the URL of your GitHub Enterprise Server instance. 
      + **Code Connections** – Configure AWS CodeConnections by providing: 
        +  **Code Connections host** – Select an existing AWS CodeConnections host from the dropdown. 
        +  **VPC ID** – Provide the VPC ID where the AWS CodeConnection is hosted. 
        +  **VPC endpoint** – Specify the VPC endpoint for the connection. 

1.  Choose **Connect**. 

 After you configure the connection, create and install the GitHub Enterprise Server App to finish the integration. 

**To create and install the GitHub Enterprise Server App**

1.  Create the GitHub Enterprise Server App by downloading the provided HTML form file. This file will redirect you to your GitHub Enterprise Server instance to register the application using the App Manifest registration flow. 

1.  Complete the App registration process in your GitHub Enterprise Server instance by following the prompts to create and install the application. 

1.  Return to the Amazon Inspector console to complete the integration setup and review your integration settings. 

1.  Choose **Connect** to finalize the integration. 

**Note**  
 Amazon Inspector only scans and monitors your default branch. If you create a new default branch, Amazon Inspector scans and updates the new default branch. 

**Important**  
 Before you finish creating the integration, you're directed to authorize the connection between Amazon Inspector and GitHub Enterprise Server. You must complete this step to finish the procedure. If you close the pop-up, you will not be able to proceed. 

 After you create the integration, Amazon Inspector might be unable to refresh the access token. This can occur if the integration host is unavailable or Amazon Inspector experiences other communication issues. To remediate the issue, you can re-authenticate the connection from the **Integrations** tab on the **Code Security** page. Under the **Status** column, the integration shows as **Inactive**, and Amazon Inspector provides the option to re-authenticate. Choose **Re-authenticate**. You're redirected to the integration workflow where you can complete the connection setup. 

 If you delete system settings for your integration, you can lose connection indefinitely. If this occurs, you must [delete the integration](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-connect-delete-integrations.html) and create a new integration. When you delete an integration, you lose all projects and scan configurations associated with the integration. 