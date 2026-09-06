

# Git connections
<a name="git-connections"></a>

Git connections enable project members to use Git repositories for source control in Amazon SageMaker Unified Studio. You can create connections to GitHub, GitHub Enterprise Server, GitLab, GitLab Self-Managed, and Bitbucket through the AWS CodeConnections service.

**Important**  
Enabling a Git connection grants all users in the account read and write access to all repositories on that connection. For full details on access implications, see [Enabling a connection for project access](#git-connections-enable).

By default, all Git connections are initially disabled and cannot be accessed by project users. Enabling a Git connection makes it accessible in all domains that you own. Disabling a Git connection removes access to it in all domains that you own.

## Account requirements
<a name="git-account-requirements"></a>

To create and manage Git connections, you must have the following:
+ An AWS account with permissions to manage Amazon SageMaker Unified Studio domains
+ An active account with the Git provider you want to connect (GitHub, GitLab, or Bitbucket)
+ Administrator or owner permissions in your Git provider account to authorize AWS application installations

## Creating a connection
<a name="git-creating-connection"></a>

You can create Git connections from the **Connections** tab on your domain's details page in the Amazon SageMaker Unified Studio console, or from the admin portal if it is configured for your domain. Each provider has a specific setup workflow. For detailed procedures, see the following sections for each supported provider.

By default, all added Git connections are initially disabled and cannot be accessed by project members. Enabling a Git connection makes it accessible in all domains and projects in that account. Disabling a Git connection removes access in all domains and projects in that account.

## Connection tagging
<a name="git-connection-tagging"></a>

You can add AWS tags to your Git connections during creation. Tags are key-value pairs that help you organize and identify your connections. You can use tags to categorize connections by environment, team, or purpose.

## Supported providers
<a name="git-supported-providers"></a>

Amazon SageMaker Unified Studio supports Git connections to the following providers:
+ GitHub
+ GitHub Enterprise Server
+ GitLab
+ GitLab Self-Managed
+ Bitbucket

## Creating a GitHub connection
<a name="git-connections-github"></a>

Complete the following procedure to create a Git connection to GitHub.

**To create a GitHub connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain where you want to add a Git connection to GitHub.

1. On the domain's details page, choose the **Connections** tab.

1. Expand the **Create Git connection** dropdown and then choose **GitHub**.

1. For **Connection name**, enter a name for the connection. Optionally, add any AWS tags you want to associate with the connection. Choose **Connect to GitHub**.

1. Enter your GitHub credentials if you are prompted to provide them.

1. For the app installation, either choose an existing AWS application or install a new application:
   + If you have an existing AWS application, search for and select that application.
   + If you do not have an AWS application, choose **Install a new app**. In the popup window, select the account you want to connect, choose whether to connect to **All repositories** or **Only select repositories**, and then choose **Install**.

1. Choose **Connect**.

Close the popup window and refresh the **Connections** tab. The connection appears in the list with a connection status of **Available**. You must then enable the connection for project access.

## Creating a GitHub Enterprise Server connection
<a name="git-connections-githubes"></a>

Complete the following procedure to create a Git connection to GitHub Enterprise Server.

**To create a GitHub Enterprise Server connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain where you want to add a Git connection to GitHub Enterprise Server.

1. On the domain's details page, choose the **Connections** tab.

1. Expand the **Create Git connection** dropdown and then choose **GitHub Enterprise**.

1. For **Connection name**, enter a name for the connection.

1. For **URL**, enter the URL of your GitHub Enterprise Server instance.

1. If your GitHub Enterprise Server instance is only available in a VPC, choose **Use a VPC** and then specify the VPC ID.

(Optional) Under **TLS certificate**, specify your TLS certificate. Optionally, add any AWS tags. Choose **Connect to GitHub Enterprise Server**.

This takes you to the connection details page with a status of **Pending**. Complete the following procedure to activate the pending connection.

**To update a pending GitHub Enterprise Server connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain with the pending connection.

1. On the domain's details page, choose the **Connections** tab and then choose the Git connection that you want to update.

1. Choose **Update pending connection**. A popup window appears.

1. If you have an existing AWS application, search for and select it, then choose **Connect**. If you do not have an AWS application, choose **Install a new application**.

1. In the popup window, choose **Leave page** to go to the new application installation.

1. Select the organization in which you want to install the application.

Select whether you want the app to connect to **All repositories** or **Only select repositories**, and then choose **Install**. The connection status changes to **Available**. You must then enable the connection for project access.

## Creating a GitLab connection
<a name="git-connections-gitlab"></a>

Complete the following procedure to create a Git connection to GitLab.

**To create a GitLab connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain where you want to add a Git connection to GitLab.

1. On the domain's details page, choose the **Connections** tab.

1. Expand the **Create Git connection** dropdown and then choose **GitLab**.

1. For **Connection name**, enter a name for the connection. Optionally, add any AWS tags. Choose **Connect to GitLab**.

1. Enter your GitLab credentials when prompted. After authentication, choose **Authorize AWS connector for GitLab**.

1. On the **Connect to GitLab** page, choose **Connect**.

Close the popup window and refresh the **Connections** tab. The new GitLab connection appears in the list with a connection status of **Available**. You must then enable this connection for project access.

## Creating a GitLab self-managed connection
<a name="git-connections-gitlabsm"></a>

Complete the following procedure to create a Git connection to GitLab Self-Managed.

**To create a GitLab self-managed connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain where you want to add a Git connection to GitLab Self-Managed.

1. On the domain's details page, choose the **Connections** tab.

1. Expand the **Create Git connection** dropdown and then choose **GitLab self-managed**.

1. For **Connection name**, enter a name for the connection. For **URL**, enter the endpoint of the server to connect to. Choose **Connect to GitLab self-managed**.

This takes you to the connection details page with a status of **Pending**. Complete the following procedure to activate the pending connection.

**To update a pending GitLab self-managed connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain with the pending connection.

1. On the domain's details page, choose the **Connections** tab and then choose the Git connection that you want to update.

1. Choose **Update pending connection**. A popup window appears.

1. If you have an existing AWS application, search for and select it, then choose **Connect**. If you do not have an AWS application, choose **Install a new application**.

1. In the popup window, choose **Leave page** to go to the new application installation.

1. Select the organization in which you want to install the application.

Select whether you want the app to connect to **All repositories** or **Only select repositories**, and then choose **Install**. The connection status changes to **Available**. You must then enable the connection for project access.

## Creating a Bitbucket connection
<a name="git-connections-bitbucket"></a>

Complete the following procedure to create a Git connection to Bitbucket.

**Note**  
You must have an existing Bitbucket workspace before you can complete this procedure. Amazon SageMaker Unified Studio only supports the Bitbucket Cloud hosting option. The Data Center hosting option is not supported. For more information, see [Bitbucket hosting options](https://bitbucket.org/product/guides/getting-started/overview#bitbucket-software-hosting-options).

**To create a Bitbucket connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain where you want to add a Git connection to Bitbucket.

1. On the domain's details page, choose the **Connections** tab.

1. Expand the **Create Git connection** dropdown and then choose **Bitbucket**.

1. For **Connection name**, enter a name for the connection. Choose **Connect to Bitbucket**.

1. For **Bitbucket apps**, specify an existing app or choose **Install a new app**. Choose **Connect**. This redirects you to the Bitbucket website where you can choose your existing Bitbucket workspace and grant access by choosing **Grant access**.

## Enabling a connection for project access
<a name="git-connections-enable"></a>

After a Git connection is created and updated to become available, you can enable it for project members to use in your domain. Complete the following procedure to enable project access for a Git connection.

**To enable a Git connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain where you want to enable a connection.

1. On the domain's details page, choose the **Connections** tab.

1. Choose the connection that you want to enable, and then choose **Enable**. A confirmation window appears.

1. Choose **Enable**. When you refresh the page, the connection appears as **Enabled**.

**Important**  
When you enable a Git connection, all users who can sign in to any domain in the account have read and write access to all repositories on that connection. This access applies regardless of the user's project membership or permission level. There is no repository-level isolation within a single account. To enforce isolation between repositories, use separate AWS accounts. Do not store sensitive information in connected repositories unless all users in the account are authorized to access that information.

## Disabling or deleting a connection
<a name="git-disable-delete"></a>

You can disable a Git connection to temporarily remove project access, or delete a connection to permanently remove it from your domain.

**To disable or delete a Git connection**

1. Open the Amazon SageMaker Unified Studio console and use the Region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and then choose the domain with the connection you want to modify.

1. On the domain's details page, choose the **Connections** tab.

1. Choose the connection that you want to disable or delete.

1. Choose **Disable** to remove project access, or choose **Delete** to permanently remove the connection.

**Note**  
If you disable or delete a connection, the local repository clone remains in the user's IDE. However, users can no longer push or pull changes to or from the remote repository.

When you disable or delete a connection, projects that have repositories using that connection are affected as follows:
+ Existing local clones remain in the project. Project members can continue viewing tracked artifacts.
+ Push, pull, and branch operations fail because the connection is no longer available.
+ Project members cannot add new repositories using that connection.
+ If you re-enable the connection, repository operations resume without requiring project members to re-add repositories.