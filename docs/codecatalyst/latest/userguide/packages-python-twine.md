Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring Twine and publishing Python packages

To use `twine` with CodeCatalyst, you must connect `twine` to your package repository and provide a personal access token for authentication. You can view
instructions for connecting `twine` to your package repository in the CodeCatalyst console. After you authenticate and connect `twine` to CodeCatalyst, you can run
`twine` commands.

## Publishing packages to CodeCatalyst with

Twine

The following instructions explain how to authenticate and connect `twine` to your CodeCatalyst package repository.

###### To configure and use `twine` to publish packages to your CodeCatalyst package repository

1.  Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2.  On the overview page for your project, choose **Packages**.
3.  Choose your package repository from the list of package repositories.
4.  Choose **Connect to repository**.
5.  In the **Connect to repository** dialog box, choose
    **Twine** from the list of package manager
    clients.
6.  You will need a personal access token (PAT) to authenticate twine with CodeCatalyst. If you already have one, you can use that. If not, you can create one here.
    1. Choose **Create token**.
    2. Choose **Copy** to copy your PAT.

    ###### Warning

    You will not be able to see or copy your PAT again after you close the dialog box.

7.  You can configure twine with a `.pypirc` file, or with environment variables.
    1. **To configure with a `.pypirc` file.**

    Open `~/.pypirc` in your editor of choice.

    Add an index server for CodeCatalyst, including the repository, user name,
    and PAT that you created and copied in a previous step. Replace the following values.

    ###### Note

    If copying from the console instructions, the following values should be updated for you and should not be changed.

        * Replace `username` with your CodeCatalyst user name.
        * Replace `PAT` with your CodeCatalyst PAT.
        * Replace `space_name` with your CodeCatalyst space name.
        * Replace `proj_name` with your CodeCatalyst project name.
        * Replace `repo_name` with your CodeCatalyst package repository name.

    ```
    [distutils]
    index-servers = `proj-name`/`repo-name`

    [`proj-name`/`repo-name`]
    repository = https://packages.`region`.codecatalyst.aws/pypi/`space_name`/`proj_name`/`repo_name`/
    password = `PAT`
    username = `username`
    ```

    2. **To configure with environment variables.**

    Set the following environment variables. In the `TWINE_REPOSITORY_URL` value, update
    `space_name`, `proj_name`, and
    `repo_name` with your CodeCatalyst space, project, and package repository names.

    ```
    export TWINE_USERNAME=`username`
    ```

    ```
    export TWINE_PASSWORD=`PAT`
    ```

    ```
    export TWINE_REPOSITORY_URL="https://packages.`region`.codecatalyst.aws/pypi/`space_name`/`proj_name`/`repo_name`/"
    ```

8.  Publish a Python distribution with the `twine upload`
    command.
