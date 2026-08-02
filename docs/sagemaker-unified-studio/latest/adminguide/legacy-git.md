# Legacy experience and migration

This section is for administrators managing projects that use the previous storage and
Git connection experience. If you are configuring a new domain or have already migrated,
see [Git connections](git-connections.md "git-connections.md") for the current documentation. Below you will find
the documentation for the previous force-push experience.

## Legacy experience

### Unified storage (Legacy)

###### Note

You can't create new projects with AWS CodeCommit. Existing projects that were
created using CodeCommit will continue to work.

### Configuring project storage options (Legacy)

#### Storage type selection guidelines

Choose S3 storage for teams with limited Git experience, simple projects without complex versioning needs,
quick experimentation and ad-hoc analysis, and scenarios requiring maximum regional availability.

Choose Git-based storage for projects requiring strict version control, collaborative development with code reviews,
integration with existing development workflows, and cross-project code sharing requirements.

#### Amazon S3 storage configuration

S3 storage is the default option and requires minimal configuration. As an administrator, you can
enable [S3 bucket
versioning](../../../AmazonS3/latest/userguide/manage-versioning-examples.md "../../../AmazonS3/latest/userguide/manage-versioning-examples.md") to configure basic versioning capabilities for projects that require file history tracking.

#### Git-based storage configuration

For projects requiring advanced version control, you can configure connections to existing Git repositories during project
creation and set default branches and branching policies for effective branch management. Additionally, you can enable multiple
projects to use the same repository when appropriate, allowing for efficient cross-project sharing of code and resources.
However, it's important to note that Git-based storage availability is limited by the CodeConnections service, which may
impose regional limitations on deployment options. For more information,
see [CodeConnections](../../../general/latest/gr/codeconnections.md "../../../general/latest/gr/codeconnections.md").

For storage organization, refer to [Managing storage resources](../userguide/managing-storage.md "../userguide/managing-storage.md").

### Performance and cost optimization (Legacy)

#### File size limitations

Files over 15 MB cannot be directly uploaded to shared folders through the Amazon SageMaker Unified Studio interface in space-based tools
like JupyterLab and Code Editor. Large files must be uploaded to local folder in JupyterLab first, then copy or move to
the shared folder if needed.

#### Cost management considerations

Heavy file read/write workloads in shared storage can incur additional S3 access costs, while frequent S3 operations may
affect performance for collaborative workflows.

**For space-based tools (like JupyterLab):** Apart from the shared folder, space-based tools
such as JupyterLab and Code Editor also have an EBS-based personal folder per user per project. We recommend using this local
storage for intermediate and temporary files during development work, as it provides superior performance for frequent file
operations. Only move final versions of files that are ready for sharing with other project users to the S3 shared folder.
This approach minimizes S3 operations and associated costs while maintaining optimal performance for iterative development work.

###### Note

This storage strategy applies specifically to space-based tools like JupyterLab and Code Editor that have
access to both local EBS storage and shared storage. For web-based tools like Query Editor, intermediate or
temporary files are generated during normal operation, but since these tools don't have a dedicated personal
folder, all files are saved directly to shared storage. Web-based tools rely entirely on the shared storage
for file operations and don't have the option to use local EBS storage for performance optimization.

### Feature comparison matrix (Legacy)

The following table provides a comprehensive comparison of key features between Git-based and S3 storage
options to help you make informed decisions when configuring storage for your Amazon SageMaker Unified Studio projects.

| Feature               | Git-based projects                                                                                                                                                                                      | S3-based projects                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Audit trail           | Full Git commit history tracks all changes including author information, timestamps, and detailed commit<br>messages. Complete audit trail is maintained in the Git repository.                         | No systematic tracking of file changes or user attribution. Basic file modification timestamps are available,<br>but no detailed change history or commit messages are maintained.                               |
| Version history       | Complete Git versioning with full commit history, branching, and merging capabilities. Version history is<br>accessible through Git commands in JupyterLab or through the Git provider's web interface. | S3 bucket versioning must be enabled from the S3 console by administrators. When enabled, version history<br>will be available from the S3 console, allowing you to view and restore previous versions of files. |
| Shared storage        | All project members work through same Git repository. Files must be "Saved to project" or pushed to the repo                                                                                            | Shared folder (shared\_files/) accessible by all project members. Direct file sharing.                                                                                                                           |
| Cross-project sharing | Multiple SMUS projects can connect to the same Git repository, enabling code and resource sharing across<br>different project teams.                                                                    | Each project has its own dedicated S3 storage location. Files cannot be directly shared between projects<br>without manual copying.                                                                              |
| Regional availability | Limited by availability of CodeConnections service.                                                                                                                                                     | Available in all regions where S3 is available.                                                                                                                                                                  |
| Change documentation  | All changes are documented through Git commit messages that developers write when saving changes.<br>Provides detailed context for each modification.                                                   | No built-in mechanism for documenting changes. File modifications occur without requiring or<br>capturing change descriptions.                                                                                   |
| Setup complexity      | Requires Git repository configuration                                                                                                                                                                   | Minimal configuration required                                                                                                                                                                                   |

### Git connections (Legacy)

Git connections enable you to check in and check out files, and manage your code repository.
When you create an Amazon SageMaker unified domain, a default git connection to CodeCommit is
provided for you to manage your code. You can also create and enable new 3P Git connections to
GitHub, GitHub Enterprise Server, GitLab, and GitLab Self-Managed.

###### Important

When you enable a Git connection, all users who can sign in to any domain in the account
have read and write access to all repositories on that connection. This access applies
regardless of the user's project membership or permission level. To enforce isolation between
repositories, use separate AWS accounts.

###### Note

You can't create new projects with AWS CodeCommit. Existing projects that were
created using CodeCommit will continue to work.

By default, all added Git connections are initially disabled and cannot be accessed by
project users. Enabling a Git connection makes it accessible in all the domains that you own,
and disabling a Git connection removes access to it in all the domains that you own.

You can use the following procedures to create 3P Git connections.

#### Github connections

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

#### Github Enterprise server connections

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

#### GitLab connections

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

#### GitLab self-managed connections

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

#### Bitbucket connections

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

#### Enable connections for project access

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

###### Important

When you enable a Git connection, all users who can sign in to any domain in the account
have read and write access to all repositories on that connection. This access applies
regardless of the user's project membership or permission level. There is no
repository-level isolation within a single account. To enforce isolation between
repositories, use separate AWS accounts. Do not store sensitive information in connected
repositories unless all users in the account are authorized to access that
information.

The following note describes the behavior when a connection is later disabled or
deleted.

###### Note

When you create and enable a connection for Git access and the user accesses this
connection in the JupyterLab in SageMaker Unified Studio in Amazon SageMaker Unified Studio,
the repository is cloned, in other words, a local copy of the repository is created in the
Amazon SageMaker Unified Studio project. If the administrator later disables or deletes this
Git connection, the local repository remains in the user's IDE, but users can no longer push
or pull files to or from it. For more information about Git operations in Amazon SageMaker
Unified Studio, see [Performing Git operations](../userguide/performing-git-operations.md "../userguide/performing-git-operations.md").

## Migrating to the new repository experience

Migrating to the new repository experience requires a project update. The migration
is initiated by the project owner from the Repositories page in their project. As an
administrator, be aware of the following:

- **Cross-account prerequisites**: If your projects
  use cross-account configurations, you must update RAM permissions before projects
  can successfully migrate. Without updated permissions, the repository clone fails
  and the project remains in the previous mode. For details, see
  [Cross-account and cross-region Git configurations](cross-account-git.md "cross-account-git.md").
- **Project updates include the Git transition**:
  Any service-initiated or admin-initiated project update includes the migration to
  the new repository experience. Project owners cannot accept other updates selectively
  while excluding the repository experience change.
- **No forced migration**: The migration is opt-in.
  Projects that are not updated continue with the previous behavior indefinitely.
