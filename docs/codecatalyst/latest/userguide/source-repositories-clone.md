Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Cloning a source repository

To work effectively with multiple files, branches, and commits in source repositories,
clone the source repository to your local computer and use a Git client or an integrated
development environment (IDE) to make changes. Commit and push your changes to the
source repository in order to work with CodeCatalyst features such as issues and pull
requests. You can also choose to create a Dev Environment to work on code. Creating a
Dev Environment automatically clones the repository and branch you specify into the
Dev Environment.

###### Note

You cannot clone linked repositories in the CodeCatalyst console or create Dev Environments
for them. To clone a linked repository locally, choose the link in the list of
repositories to open that repository in the service that hosts it, and then clone
it. For more information, see the documentation for the service that hosts the
linked repository.

###### To create a Dev Environment from a source repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **Code**, and then choose
   **Source repositories**.
3. Choose the source repository where you want to work on code.
4. Choose **Create Dev Environment**.
5. Choose a supported IDE from the drop-down menu. See [Supported integrated development environments
   for Dev Environments](devenvironment-create.md#devenvironment-supported-ide "devenvironment-create.md#devenvironment-supported-ide") for more information.
6. Do one of the following:
   - Choose **Work in existing branch**, and then choose a branch from the
     **Existing branch** drop-down menu.
   - Choose **Work in new branch**, enter a branch name into the **Branch
     name** field, and choose a branch off of which to create the new
     branch from the **Create branch from** drop-down menu.

7. Optionally add a name for the Dev Environment or edit its configuration.
8. Choose **Create**.

###### To clone a source repository

1. Navigate to your project.
2. On
   the summary page for your project, choose the repository you want from the list, and then
   choose **View repository**. Alternatively, in the
   navigation pane, choose **Code**, and then choose **Source
   repositories**.
   Choose the name of the repository from the list of source repositories for the project. You
   can filter the list of repositories by typing part of the repository name in the filter
   bar.
3.
4. Choose **Clone repository**. Copy the clone URL for the
   repository.

###### Note

If you do not have a personal access token (PAT), choose **Create
token**. Copy the token and save it in a secure location. You will use this PAT
when prompted for a password by your Git client or integrated development environment
(IDE). 5. Do one of the following:

    * To clone a repository to your local computer, open a terminal or command line and run
     the **git clone** command with the clone URL after the command. For
     example:



    ```
    git clone https://`LiJuan`@git.us-west-2.codecatalyst.aws/v1/`ExampleCorp`/`MyExampleProject`/`MyExampleRepo`
    ```

    When prompted for a password, paste the PAT you saved earlier.


    ###### Note

    If your operating system provides credential management or you have installed a
     credential management system, you only need to provide the PAT once. If not, you might
     have to provide the PAT for every Git operation. As a best practice, make sure that your
     credential management system securely stores your PAT. Do not include the PAT as part of
     the clone URL string.
    * To clone a repository using an IDE, follow the documentation for your IDE. Choose the
     option to clone a Git repository and provide the URL. When prompted for a password,
     provide the PAT.
