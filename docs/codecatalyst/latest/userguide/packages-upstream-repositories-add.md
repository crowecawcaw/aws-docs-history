Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding an upstream repository

Adding a public package repository or another CodeCatalyst package repository as an upstream repository to your
downstream repository makes all of the packages in the upstream
repository available to package managers that are connected to the downstream repository.

###### To add an upstream repository

1. In the navigation pane, choose **Packages**.
2. On the **Package repositories** page, choose the package repository that you want to
   add an upstream repository to.
3. Under the package repository's name, choose **Upstreams** and choose **Select upstream repositories**.
4. In **Select upstream type**, choose one of the following:
   - **Gateway repositories**

   You can choose from a list of available gateway repositories.

   ###### Note

   To connect to public external package authorities such as Maven Central, npmjs.com, or Nuget Gallery, CodeCatalyst uses gateway repositories
   as intermediary repositories that search and store packages pulled from external repositories. This saves time and data transfer as all package
   repositories in a project will use packages from the gateway intermediary repository. For more information, see
   [Connecting to public external repositories](packages-connect-external.md "packages-connect-external.md").
   - **CodeCatalyst repositories**

   You can choose from a list of available CodeCatalyst package repositories in your project.

5. When you've selected all of the repositories you want to add as upstream repositories, choose **Select**, and then choose **Save**.

For more information about changing the search order of upstream repositories, see
[Editing the search order of
upstream repositories](packages-upstream-repositories-search-order.md "packages-upstream-repositories-search-order.md").
When you've added an upstream repository, you can use a package manager that is connected
to your local repository to fetch packages from the upstream repository. You do not need to
update your package manager configuration. For more information about requesting package versions
from an upstream repository, see [Requesting a package version with upstream repositories](packages-upstream-repositories-request.md "packages-upstream-repositories-request.md").
