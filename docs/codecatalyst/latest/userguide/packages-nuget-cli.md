

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Configuring and using the nuget or dotnet CLI
<a name="packages-nuget-cli"></a>

You can use CLI tools such as `NuGet` and `dotnet` to publish and consume packages from CodeCatalyst. This document provides information about configuring the CLI tools and using them to publish or consume packages.

**Contents**
+ [Configuring NuGet with CodeCatalyst](#nuget-configure-cli)
+ [Consuming NuGet packages from a CodeCatalyst repository](#nuget-consume-cli)
+ [Consuming NuGet packages from NuGet.org through CodeCatalyst](#nuget-consume-nuget-gallery)
+ [Publishing NuGet packages to CodeCatalyst](#nuget-publish-cli)

## Configuring NuGet with CodeCatalyst
<a name="nuget-configure-cli"></a>

To configure NuGet with CodeCatalyst, add a repository endpoint and personal access token to your NuGet configuration file to allow `nuget` or `dotnet` to connect to your CodeCatalyst package repository.

**To configure NuGet with your CodeCatalyst package repository**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. On the overview page for your project, choose **Packages**.

1. Choose your package repository from the list of package repositories.

1. Choose **Connect to repository**.

1. In the **Connect to repository** dialog box, choose **NuGet** or **dotnet** from the list of package manager clients. 

1. You will need a personal access token (PAT) to authenticate NuGet with CodeCatalyst. If you already have one, you can use that. If not, you can create one here.

   1. Choose **Create token**.

   1. Choose **Copy** to copy your PAT.
**Warning**  
You will not be able to see or copy your PAT again after you close the dialog box.

1. Configure `nuget` or `dotnet` to use your repository's NuGet endpoint and CodeCatalyst PAT. Replace the following values.
**Note**  
If copying from the console instructions, the following values should be updated for you and should not be changed.
   + Replace {{username}} with your CodeCatalyst user name.
   + Replace {{PAT}} with your CodeCatalyst PAT.
   + Replace {{space\_name}} with your CodeCatalyst space name.
   + Replace {{proj\_name}} with your CodeCatalyst project name.
   + Replace {{repo\_name}} with your CodeCatalyst package repository name.

   1. For `nuget`, use the `nuget sources add` command.

      ```
      nuget sources add -name "{{repo_name}}" -Source "https://packages.{{region}}.codecatalyst.aws/nuget/{{space_name}}/{{proj_name}}/{{repo_name}}/v3/index.json" -username "{{username}}" -password "{{PAT}}"
      ```

   1. For `dotnet`, use the `dotnet nuget add source` command.

      **Linux and macOS users**: Because encryption is not supported on non-Windows platforms, you must add the `--store-password-in-clear-text` flag to the following command. Note that this will store your password as plaintext in your configuration file.

      ```
      dotnet nuget add source "https://packages.{{region}}.codecatalyst.aws/nuget/{{space_name}}/{{proj_name}}/{{repo_name}}/v3/index.json" -n "{{proj_name}}/{{repo_name}}" -u "{{username}}" -p "{{PAT}}" --store-password-in-clear-text
      ```

Once you have configured NuGet with CodeCatalyst, you can [consume NuGet packages](#nuget-consume-cli) that are stored in your CodeCatalyst repository or one of its upstream repositories and [publish NuGet packages](#nuget-publish-cli) to your CodeCatalyst repository.

## Consuming NuGet packages from a CodeCatalyst repository
<a name="nuget-consume-cli"></a>

Once you have [configured NuGet with CodeCatalyst](#nuget-configure-cli), you can consume NuGet packages that are stored in your CodeCatalyst repository or one of its upstream repositories.

To consume a package version from a CodeCatalyst repository or one of its upstream repositories with nuget or dotnet, run the following command. Replace {{packageName}} with the name of the package you want to consume and {{packageSourceName}} with the source name for your CodeCatalyst package repository in your NuGet configuration file, which should be the repository name.

**To install a package with `dotnet`**

```
dotnet add {{packageName}} --source {{packageSourceName}}
```

**To install a package with `nuget`**

```
nuget install {{packageName}} --source {{packageSourceName}}
```

For more information, see [Manage packages using the nuget CLI](https://docs.microsoft.com/en-us/nuget/consume-packages/install-use-packages-nuget-cli) or [Install and manage packages using the dotnet CLI](https://docs.microsoft.com/en-us/nuget/consume-packages/install-use-packages-dotnet-cli) in the *Microsoft Documentation*.

## Consuming NuGet packages from NuGet.org through CodeCatalyst
<a name="nuget-consume-nuget-gallery"></a>

You can consume NuGet packages from [NuGet.org](https://www.nuget.org/) through a CodeCatalyst repository by configuring the repository with an upstream connection to **NuGet.org**. Packages consumed from **NuGet.org** are ingested and stored in your CodeCatalyst repository.

**To consume packages from NuGet.org**

1. If you haven't already, configure your NuGet package manager with your CodeCatalyst package repository by following the steps in [Configuring NuGet with CodeCatalyst](#nuget-configure-cli). 

1. Ensure that your repository has added **NuGet.org** as an upstream connection. You can check which upstream sources are added or add **Nuget.org** as an upstream source by following the instructions in [Adding an upstream repository](packages-upstream-repositories-add.md) and choosing the **NuGet store** repository.

## Publishing NuGet packages to CodeCatalyst
<a name="nuget-publish-cli"></a>

Once you have [configured NuGet with CodeCatalyst](#nuget-configure-cli), you can use `nuget` or `dotnet` to publish package versions to CodeCatalyst repositories.

To push a package version to a CodeCatalyst repository, run the following command with the full path to your `.nupkg` file and the source name for your CodeCatalyst repository in your NuGet configuration file.

**To publish a package with `dotnet`**

```
dotnet nuget push {{path/to/nupkg/SamplePackage.1.0.0.nupkg}} --source {{packageSourceName}}
```

**To publish a package with `nuget`**

```
nuget push {{path/to/nupkg/SamplePackage.1.0.0.nupkg}} --source {{packageSourceName}}
```