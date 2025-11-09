Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Using CodeCatalyst with Visual Studio

You can consume packages from CodeCatalyst directly in Visual Studio.

To configure and use NuGet with CLI tools such as `dotnet` or `nuget`, see [Configuring and using the nuget or dotnet
CLI](packages-nuget-cli.md "packages-nuget-cli.md").

###### Contents

- [Configuring Visual Studio with CodeCatalyst](packages-nuget-visual-studio.md#packages-nuget-vs-configure "packages-nuget-visual-studio.md#packages-nuget-vs-configure")
  - [Windows](packages-nuget-visual-studio.md#packages-nuget-vs-configure-windows "packages-nuget-visual-studio.md#packages-nuget-vs-configure-windows")
  - [macOS](packages-nuget-visual-studio.md#packages-nuget-vs-configure-mac "packages-nuget-visual-studio.md#packages-nuget-vs-configure-mac")

## Configuring Visual Studio with CodeCatalyst

### Windows

###### To configure Visual Studio with CodeCatalyst

1. A personal access token (PAT) is required to authenticate with CodeCatalyst.
   If you already have one, you can use that.
   If not, follow the instructions in [Grant users repository access with personal access tokens](ipa-tokens-keys.md "ipa-tokens-keys.md") to create one.
2. Use `nuget` or `dotnet` to configure your package repository and credentials.

dotnet
**Linux and macOS users:**
Because encryption is not supported on non-Windows
platforms, you must add the
`--store-password-in-clear-text` flag to the
following command. Note that this will store your password
as plaintext in your configuration file.

```
dotnet nuget add source https://packages.`region`.codecatalyst.aws/nuget/`space-name`/`proj-name`/`repo-name`/v3/index.json --name `repo_name` --password `PAT` --username `user_name`
```

nuget

```
nuget sources add -name `repo_name` -Source https://packages.`region`.codecatalyst.aws/nuget/`space-name`/`proj-name`/`repo-name`/v3/index.json -password `PAT` --username `user_name`
```

Example output:

```
Package source with Name: `repo_name` added successfully.
```

3. Configure Visual Studio to use your new package source. In Visual Studio, choose **Tools**, and
   then choose **Options**.
4. In the **Options** menu, expand the **NuGet Package
   Manager** section and choose **Package
   Sources**.
5. In the **Available package sources** list, make sure that your
   `repo_name` source is enabled. If you have
   configured your package repository with an upstream connection to the
   NuGet Gallery, disable the **nuget.org** source
   .

### macOS

###### To configure Visual Studio with CodeCatalyst

1. A personal access token (PAT) is required to authenticate with CodeCatalyst.
   If you already have one, you can use that.
   If not, follow the instructions in [Grant users repository access with personal access tokens](ipa-tokens-keys.md "ipa-tokens-keys.md") to create one.
2. Choose **Preferences** from the menu bar.
3. In the **NuGet** section, choose **Sources**.
4. Choose **Add** and add your repository information.
   1. For **Name**, enter your CodeCatalyst package repository name.
   2. For **Location**, enter your CodeCatalyst package repository endpoint. The
      following snippet shows an example endpoint. Replace `space-name`, `proj-name`,
      and `repo-name` with your CodeCatalyst space name, project name, and repository name.

   ```
   https://packages.`region`.codecatalyst.aws/nuget/`space-name`/`proj-name`/`repo-name`/
   ```

   3. For **Username**, enter any valid value.
   4. For **Password**, enter your PAT.

5. Choose **Add source**.
6. If you have configured your package repository with an upstream connection to the NuGet
   Gallery, disable the **nuget.org** source.

After configuration, Visual Studio can consume packages from your CodeCatalyst repository, any of its upstream repositories,
or from [NuGet.org](https://www.nuget.org/ "https://www.nuget.org/") if you have it configured as an upstream source. For more information about
browsing and installing NuGet packages in Visual Studio, see
[Install
and manage packages in Visual Studio using the NuGet Package Manager](https://docs.microsoft.com/en-us/nuget/consume-packages/install-use-packages-visual-studio "https://docs.microsoft.com/en-us/nuget/consume-packages/install-use-packages-visual-studio") in the _NuGet documentation_.
