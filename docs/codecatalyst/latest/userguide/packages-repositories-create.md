Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating a package repository

Perform the following steps to create a package repository in CodeCatalyst.

###### To create a package repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project in which you want to create a package repository.
3. From the navigation pane, choose **Packages**.
4. On the **Package repositories** page, choose **Create package repository**.
5. In the **Package repository details** section, add the following:
   1. **Repository name**. Consider using a descriptive name with details such as your project or team name, or how the repository will be used.
   2. (Optional) **Description**.
      A repository description is especially helpful when you have multiple repositories across multiple teams in a project.

6. In the **Upstream repositories** section, choose **Select upstream repositories** to add any package repositories that you want to access through your
   CodeCatalyst package repository. You can add **Gateway repositories** to connect to external package repositories or other **CodeCatalyst repositories**.
   1. When a package is requested from a package repository, upstream repositories will be searched in the order they appear in this list. Once a package is found, CodeCatalyst will stop
      searching. To change the order of the upstream repositories, you can drag and drop the repositories in the list.

7. Choose **Create** to create your package repository.
