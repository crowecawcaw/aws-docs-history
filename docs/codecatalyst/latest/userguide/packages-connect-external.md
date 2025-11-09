Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Connecting to public external repositories

You can connect CodeCatalyst package repositories to supported public, external repositories by
adding the corresponding gateway repository as an upstream repository. Gateway repositories act as
intermediary repositories that search and store packages pulled from external repositories. This
saves time and data transfer because all package repositories in a project can use stored packages from the
gateway repository.

###### To connect to a public repository using gateway repositories

1. In the navigation pane, choose **Packages**.
2. In **Packages**, choose the **Gateway
   repositories** page. You can view a list of supported gateway repositories and their
   descriptions.
3. To use a gateway repository, first you must create it. If the gateway repository
   has been created, the date and time it was created is shown. If it hasn't, choose
   **Create** to create it.
4. To use packages from the gateway repository, you must set an upstream
   connection to it from a CodeCatalyst repository. Choose **Package repositories** and choose the package repository that
   you want to connect to.
5. To connect to the public repository, choose **Upstreams** and choose
   **Select upstream repositories**.
6. Choose **Gateway repositories** select the gateway repository that corresponds
   to the public repository that you want to connect to as an upstream repository .
7. When you've selected all of the gateway repositories you want to add as upstream
   repositories, choose **Select**.
8. When you're finished ordering upstream repositories, choose
   **Save**.
   For more information about upstream repositories, see
   [Configuring and using upstream repositories](packages-upstream-repositories.md "packages-upstream-repositories.md").

When you've added a gateway repository as an upstream repository, you can use a package
manager that is connected to your local repository to fetch packages from the public, external
package repository that corresponds to it. You do not need to update your package manager
configuration. Packages consumed in this manner are stored in both the gateway repository and your
local package repository. For more information about requesting package versions from an upstream
repository, see [Requesting a package version with upstream repositories](packages-upstream-repositories-request.md "packages-upstream-repositories-request.md").

## Supported external package repositories and their gateway repositories

CodeCatalyst supports adding an upstream connection to the following official package authorities with gateway repositories.

| Repository package type | Description               | Gateway repository name       |
| ----------------------- | ------------------------- | ----------------------------- |
| npm                     | npm public registry       | `npm-public-registry-gateway` |
| Python                  | Python Package Index      | `pypi-gateway`                |
| Maven                   | Maven Central             | `maven-central-gateway`       |
| Maven                   | Google Android repository | `google-android-gateway`      |
| Maven                   | CommonsWare               | `commonsware-gateway`         |
| Maven                   | Gradle plugins repository | `gradle-plugins-gateway`      |
| NuGet                   | NuGet Gallery             | `nuget-gallery-gateway`       |
