

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# NuGet compatibility
<a name="packages-nuget-compatibility"></a>

 This guide contains information about CodeCatalyst's compatibility with different NuGet tools and versions. 

**Topics**
+ [General NuGet compatibility](#nuget-version-support)
+ [NuGet command line support](#nuget-command-line-support)

## General NuGet compatibility
<a name="nuget-version-support"></a>

CodeCatalyst supports NuGet 4.8 and higher.

CodeCatalyst only supports V3 of the NuGet HTTP protocol. This means that some CLI commands that rely V2 of the protocol are not supported. See the following [nuget command support](#nuget-command-support) section for more information.

CodeCatalyst does not support PowerShellGet 2.x.

## NuGet command line support
<a name="nuget-command-line-support"></a>

CodeCatalyst supports the NuGet (`nuget`) and .NET Core (`dotnet`) CLI tools.

### nuget command support
<a name="nuget-command-support"></a>

Because CodeCatalyst only supports V3 of NuGet's HTTP protocol, the following commands will not work when used against CodeCatalyst resources:
+ `list`: The `nuget list` command displays a list of packages from a given source. To get a list of packages in a CodeCatalyst package repository, navigate to the repository in the CodeCatalyst console.