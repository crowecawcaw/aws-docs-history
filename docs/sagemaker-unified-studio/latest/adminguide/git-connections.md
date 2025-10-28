# Git connections in Amazon SageMaker Unified Studio

Git connections enable you to check in and check out files, and manage your code repository.
When you create an Amazon SageMaker unified domain, a default git connection to CodeCommit is
provided for you to manage your code. You can also create and enable new 3P Git connections to
GitHub, GitHub Enterprise Server, GitLab, and GitLab Self-Managed.

###### Note

You can't create new projects with AWS CodeCommit. Existing projects that were
created using CodeCommit will continue to work.

By default, all added Git connections are initially disabled and cannot be accessed by
project users. Enabling a Git connection makes it accessible in all the domains that you own,
and disabling a Git connection removes access to it in all the domains that you own.

You can use the following procedures to create 3P Git connections.

###### Topics

- [Github connections](#git-connections-github "#git-connections-github")
- [Github Enterprise server connections](#git-connections-githubes "#git-connections-githubes")
- [GitLab connections](#git-connections-gitlab "#git-connections-gitlab")
- [GitLab self-managed connections](#git-connections-gitlabsm "#git-connections-gitlabsm")
- [Bitbucket connections](#git-connections-bitbucket "#git-connections-bitbucket")
- [Enable connections for project access](#git-connections-enable "#git-connections-enable")

## Github connections

Complete the following procedure to create a 3P Git connection to GitHub:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   add a 3P Git connection to GitHub.
3. On the domain's details page, choose the **Connections** tab.
4. Expand the **Create Git connection** drop-down menu and then choose
   **Github**.
5. In the **Create a connection** window, in the **Connection
   name** field, specify the name of the connection. (Optional - enter in any
   AWS tags you want to add to the connection and then choose **Connect to
   Github**.
6. Enter in your GitHub credentials if you are prompted to provide them.
7. Optional - for the app installation, either choose an AWS application to connect to
   Amazon SageMaker Unified Studio that you previously installed, or install a new application.
   - If you have installed an AWS application, search for and select that
     application.
   - If you do not have an AWS application, choose **Install a new
     app**. A popup window appears.
     - Select the account you want to install the application and establish a
       connection to.
     - Select whether you want the app to connect to **All
       repositories** or **Only select repositories**.
     - Choose **Install**.

8. Choose **Connect**.
9. Close the popup window and refresh the **Connections** tab. The
   connection appears in the list with a connection status of **Available**.
   You then need to enable the connection for project access in the Amazon SageMaker Unified Studio.

## Github Enterprise server connections

Complete the following procedure to create a 3P Git connection to GitHub Enterprise
Server:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   add a 3P Git connection to GitHub Enterprise Server.
3. On the domain's details page, choose the **Connections** tab.
4. Expand the **Create Git connection** drop-down menu and then choose
   **GitHub Enterprise**.
5. In **Connection name**, provide a name for the connection.
6. In **URL**, specify the URL of your GitHub Enterprise Server
   instance.
7. If your GitHub Enterprise Server instance is only available in a VPC, choose
   **Use a VPC** and then specify the VPC ID.
8. (Optional) Under **TLS certificate**, specify your TLS certificate.
9. (Optional) Specify any AWS tags you want to add to the connection.
10. Choose **Connect to GitHub Enterprise Server**. This brings you to
    the connection details page, and the status of the connection is
    **Pending**. You then need to update the pending connection to make it
    active.

Complete the following procedure to update a pending 3P Git connection to GitHub
Enterprise Server:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   add a 3P Git connection to GitHub.
3. On the domain's details page, choose the **Connections** tab and then
   choose the Git connection that you want to update.
4. Choose **Update pending connection**. A new popup window appears
   inviting you to enter information for your GitHub Enterprise Server.
5. If you have installed an AWS application to connect to Amazon SageMaker Unified Studio, search for it and
   select that application and choose **Connect**. If you do not have an
   AWS application to connect to Amazon SageMaker Unified Studio, choose **Install a new
   application**.
6. In the pop up window, choose **Leave page**. This takes you to the
   new application installation.
7. Select the organization in which you want to install the application and establish a
   connection.
8. Select whether you want the app to connect to **All repositories** or
   **Only select repositories**.
9. Choose **Install**.

This brings you to the connection details page, and the status of the connection changes
to **Available**. You then need to enable the connection for project access
in the Amazon SageMaker Unified Studio.

## GitLab connections

Complete the following procedure to create a 3P Git connection to GitLab:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   add a 3P Git connection to GitLab.
3. On the domain's details page, choose the **Connections** tab.
4. Expand the **Create Git connection** drop-down menu and then choose
   **GitLab**.
5. In **Connection name**, provide a name for the connection,
   optionally, enter in any AWS tags you want to add to the connection, and then choose
   **Connect to GitLab**.
6. Enter in your GitLab credentials when you are prompted to provide them. Once
   authenticated, choose **Authorize AWS connector for GitLab**.
7. On the **Connect to GitLab** page, choose
   **Connect**.
8. Close the popup window and refresh the **Connections** tab. The new
   GitLab connection appears in the list with a connection status of
   **Available**. You must then enable this connection for project access
   in the Amazon SageMaker Unified Studio.

## GitLab self-managed connections

Complete the following procedure to create a 3P Git connection to GitLab
Self-Managed:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   add a 3P Git connection to GitLab self-managed.
3. On the domain's details page, choose the **Connections** tab.
4. Expand the **Create Git connection** drop-down menu and then choose
   **GitLab self-managed**.
5. On the **Connect to GitLab self-managed** page, in
   **Connection name**, specify the name for the connection, and in the
   **URL**, specify the endpoint of the server to connect to, and then
   choose **Connect to GitLab self-managed**. This brings you to the
   connection details page, and the status of the connection is **Pending**.
   You then need to update the pending connection to make it active.

Complete the following procedure to update a pending 3P Git connection to GitLab
self-managed:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   update your pending connection.
3. On the domain's details page, choose the **Connections** tab and then
   choose the Git connection that you want to update.
4. Choose **Update pending connection**. A new popup window appears
   inviting you to enter information for your GitLab self-managed.
5. If you have installed an AWS application to connect to Amazon SageMaker Unified Studio, search for it and
   select that application and choose **Connect**. If you do not have an
   AWS application to connect to Amazon SageMaker Unified Studio, choose **Install a new
   application**.
6. In the pop up window, choose **Leave page**. This takes you to the
   new application installation.
7. Select the organization in which you want to install the application and establish a
   connection.
8. Select whether you want the app to connect to **All repositories** or
   **Only select repositories**.
9. Choose **Install**.

## Bitbucket connections

Complete the following procedure to create a 3P Git connection to Bitbucket:

###### Note

You must have an existing Bitbucket workspace before you can complete this
procedure.

Currently, Amazon SageMaker Unified Studio only supports the BitBucket Cloud hosting option. The Data Center
hosting option is not supported in the currect release of Amazon SageMaker Unified Studio. For more information,
see [Bitbucket hosting options](https://bitbucket.org/product/guides/getting-started/overview#bitbucket-software-hosting-options "https://bitbucket.org/product/guides/getting-started/overview#bitbucket-software-hosting-options").

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   add a 3P Git connection to Bitbucket.
3. On the domain's details page, choose the **Connections** tab.
4. Expand the **Create Git connection** drop-down menu and then choose
   **Bitbucket**.
5. On the **Create a connection** page, in **Connection
   name**, specify the name for the connection, and then choose **Connect
   to Bitbucket**.
6. On the **Connect to Bitbucket** page, in **Bitbucket
   apps**, specify an existing app or choose **Install a new
   app** and then choose **Connect**. This redirects you to the
   bitbucket website where you can choose your existing **Bitbucket
   workspace** and grant Amazon SageMaker Unified Studio access to it by choosing **Grant
   access**.

## Enable connections for project access

After a 3P Git connection is created and updated to become available, you can enable it
for project members to use in your domain. Complete the following procedure to enable project
access for a 3P Git connection:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   enable your connections for project members to use.
3. On the domain's details page, choose the **Connections** tab.
4. Choose the connection that you want to enable, and then choose
   **Enable**. A popup window appears so that you can confirm the
   decision.
5. Choose **Enable**. When you refresh the page, the connection then
   appears as **Enabled**. This means that project members have access to
   the connection and can use it in projects within that domain.

###### Note

All tagged connections will be accessible from all domains in the account and all
projects in the associated accounts.

###### Note

When you create and enable a connection for Git access and the user accesses this
connection in the JupyterLab in SageMaker Unified Studio in Amazon SageMaker Unified Studio,
the repository is cloned, in other words, a local copy of the repository is created in the
Amazon SageMaker Unified Studio project. If the administrator later disables or deletes this
Git connection, the local repository remains in the user's IDE, but users can no longer push
or pull files to or from it. For more information about Git operations in Amazon SageMaker
Unified Studio, see [Performing Git operations](../userguide/performing-git-operations.md "../userguide/performing-git-operations.md").
