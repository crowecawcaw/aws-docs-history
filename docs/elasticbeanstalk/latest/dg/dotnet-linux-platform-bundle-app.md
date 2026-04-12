# Bundling applications for the .NET Core on Linux Elastic Beanstalk platform

You can run both _runtime-dependent_ and _self-contained_ .NET Core applications on
AWS Elastic Beanstalk.

A runtime-dependent application uses a .NET Core runtime that Elastic Beanstalk provides to run your application. Elastic Beanstalk uses the
`runtimeconfig.json` file in your source bundle to determine the runtime to use for your application. Elastic Beanstalk chooses the latest
compatible runtime available for your application.

A self-contained application includes the .NET Core runtime, your application, and its dependencies. To use a version of the .NET Core runtime that
Elastic Beanstalk doesn't include in its platforms, provide a self-contained application.

## Examples

You can compile both self-contained and runtime-dependent applications with the `dotnet publish` command. To learn more about publishing
.NET Core apps, see [.NET Core application publishing overview](https://docs.microsoft.com/en-us/dotnet/core/deploying "https://docs.microsoft.com/en-us/dotnet/core/deploying") in the .NET
Core documentation.

The following example file structure defines a single application that uses a .NET Core runtime that Elastic Beanstalk provides.

```
тФЬтФАтФА appsettings.Development.json
тФЬтФАтФА appsettings.json
тФЬтФАтФА dotnetcoreapp.deps.json
тФЬтФАтФА dotnetcoreapp.dll
тФЬтФАтФА dotnetcoreapp.pdb
тФЬтФАтФА dotnetcoreapp.runtimeconfig.json
тФЬтФАтФА web.config
тФЬтФАтФА Procfile
тФЬтФАтФА .ebextensions
тФЬтФАтФА .platform
```

You can include multiple applications in your source bundle. The following example defines two applications to run on the same web server. To run
multiple applications, you must include a [Procfile](dotnet-linux-procfile.md "dotnet-linux-procfile.md") in your source bundle. For a full example application,
see [dotnet-core-linux-multiple-apps.zip](samples/dotnet-core-linux-multiple-apps.zip.md "samples/dotnet-core-linux-multiple-apps.zip.md").

```
тФЬтФАтФА DotnetMultipleApp1
тФВ┬а┬а тФЬтФАтФА Amazon.Extensions.Configuration.SystemsManager.dll
тФВ┬а┬а тФЬтФАтФА appsettings.Development.json
тФВ┬а┬а тФЬтФАтФА appsettings.json
тФВ┬а┬а тФЬтФАтФА AWSSDK.Core.dll
тФВ┬а┬а тФЬтФАтФА AWSSDK.Extensions.NETCore.Setup.dll
тФВ┬а┬а тФЬтФАтФА AWSSDK.SimpleSystemsManagement.dll
тФВ┬а┬а тФЬтФАтФА DotnetMultipleApp1.deps.json
тФВ┬а┬а тФЬтФАтФА DotnetMultipleApp1.dll
тФВ┬а┬а тФЬтФАтФА DotnetMultipleApp1.pdb
тФВ┬а┬а тФЬтФАтФА DotnetMultipleApp1.runtimeconfig.json
тФВ┬а┬а тФЬтФАтФА Microsoft.Extensions.PlatformAbstractions.dll
тФВ┬а┬а тФЬтФАтФА Newtonsoft.Json.dll
тФВ┬а┬а тФФтФАтФА web.config
тФЬтФАтФА DotnetMultipleApp2
тФВ┬а┬а тФЬтФАтФА Amazon.Extensions.Configuration.SystemsManager.dll
тФВ┬а┬а тФЬтФАтФА appsettings.Development.json
тФВ┬а┬а тФЬтФАтФА appsettings.json
тФВ┬а┬а тФЬтФАтФА AWSSDK.Core.dll
тФВ┬а┬а тФЬтФАтФА AWSSDK.Extensions.NETCore.Setup.dll
тФВ┬а┬а тФЬтФАтФА AWSSDK.SimpleSystemsManagement.dll
тФВ┬а┬а тФЬтФАтФА DotnetMultipleApp2.deps.json
тФВ┬а┬а тФЬтФАтФА DotnetMultipleApp2.dll
тФВ┬а┬а тФЬтФАтФА DotnetMultipleApp2.pdb
тФВ┬а┬а тФЬтФАтФА DotnetMultipleApp2.runtimeconfig.json
тФВ┬а┬а тФЬтФАтФА Microsoft.Extensions.PlatformAbstractions.dll
тФВ┬а┬а тФЬтФАтФА Newtonsoft.Json.dll
тФВ┬а┬а тФФтФАтФА web.config
тФЬтФАтФА Procfile
тФЬтФАтФА .ebextensions
тФЬтФАтФА .platform
```
