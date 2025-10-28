# Setting up your project on a local machine

While it's recommended that you create a Dev Environment and build your action within a CodeCatalyst-supported IDE,
you can also set up your project and build your action on your local machine. For more information about setting up a
Dev Environment, see [Step 1: Set up your project and Dev Environment](getting-started.md#set-up-workspace-first-action "getting-started.md#set-up-workspace-first-action").

**To set up your project**

1. Create an empty project in CodeCatalyst.

###### Note

Before you create a project, you must have the **Space administrator**
role, and you must create or join the space where you want to create the project.
For more information, see [Creating a space in CodeCatalyst](../userguide/spaces-create.md "../userguide/spaces-create.md").

    1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
    2. Navigate to the space where you want to create a project.
    3. On the space dashboard, choose **Create project**.
    4. Choose **Start from scratch**.
    5. Under **Give a name to your project**, enter the name that you
     want to assign to your project. The name must be unique within your space.
    6. Choose **Create project**.

2. Create an empty repository in your new project.

###### Note

Third-party repositories, such as GitHub repositories, aren't
supported for developing, testing, and publishing actions. The actions must
be developed in a CodeCatalyst repository.

    1. Navigate to your project.
    2. In the navigation pane, choose **Code**, and then choose
     **Source repositories**.
    3. Choose **Add repository**, and then choose **Create
     repository**.
    4. In **Repository name**, provide a name for the repository. Repository
     names must be unique within a project. For more information about the requirements for
     repository names, see [Quotas for source repositories in CodeCatalyst](../userguide/source-quotas.md "../userguide/source-quotas.md").


    The action name defaults to the repository name, but it can be changed in CodeCatalyst.
    5. (Optional) In **Description**, add a description for the
     repository that will help other users in the project understand what the repository is
     used for.
    6. (Optional) Add a `.gitignore` file for the type of code you plan to
     push.
    7. Choose **Create**.


    ###### Note

    CodeCatalyst adds a `README.md` file to your repository when you create it.
     CodeCatalyst also creates an initial commit for the repository in a default branch named
     **main**. You can edit or delete the `README.md` file,
     but you can't change or delete the default branch.

3.  Create a new feature branch and clone the remote repository.

        1. In the navigation pane, choose **Code**, choose **Source
         repositories**, and then choose the empty repository you created.
        2. Choose **Actions**, and then choose **Create
         branch**.
        3. In the **Branch name** text input field, enter a
         ``feature-action-name``.
        4. In the **Create branch from** dropdown menu, ensure
         **main**, the source branch you're creating the new branch from, is
         selected.
        5. Choose **Clone repository** and **Copy** the
         **HTTPS clone URL** for the remote repository.
        6. Choose **Create token** for a personal access token (PAT) needed
         to clone the repository.
        7. Choose **Copy** and save the copied PAT for a later step.
        8. From your working terminal, clone the remote repository in a local folder with the
         following
         git
         command:



        ```
        git clone https://`[CODECATALYST-USER]`@`[GIT-ENDPOINT]`/v1/`[CODECATALYST-SPACE-NAME]`/`[CODECATALYST-PROJECT-NAME]`/`[CODECATALYST-REPO-NAME]`
               # The url should be available when you visit the repository created.
        ```

        When prompted for a password, paste the copied PAT as the password and enter it in
         your working terminal.
        9. Change your directory to the repository you cloned:



        ```
        cd `[CODECATALYST-PROJECT-NAME]`
        ```
        10. Switch to the new branch:



        ```
        git checkout ``feature-action-name``
        ```

    After setting up your project, you can continue on to the next step before you can begin developing your action using the
    CodeCatalyst ADK. For more information, see [Step 2: Install tools and packages](getting-started.md#install-tools-packages "getting-started.md#install-tools-packages").
