

# Bundling applications for the .NET Core on Linux Elastic Beanstalk platform
<a name="dotnet-linux-platform-bundle-app"></a>

You can deploy two types of .NET applications to the .NET Core on Linux platform: *runtime-dependent* applications, which use the .NET runtime that the platform provides, and *self-contained* applications, which include their own .NET runtime. The .NET documentation calls runtime-dependent applications *framework-dependent* applications.

Publish your application with the `dotnet publish` command on your computer or in your build pipeline, and then deploy the output in a source bundle. Elastic Beanstalk doesn't build or publish your application during deployment. The type of application that you publish determines which platform branches can run it and how it gets .NET security patches.

## Choosing between runtime-dependent and self-contained applications
<a name="dotnet-linux-platform-bundle-app-compare"></a>

The following table compares runtime-dependent and self-contained applications on the .NET Core on Linux platform.


| Consideration | Runtime-dependent | Self-contained | 
| --- | --- | --- | 
| Source bundle contents | The source bundle contains your application and its dependencies, so it's smaller. | The source bundle contains your application, its dependencies, and the .NET runtime, so it's larger. | 
| .NET runtime that runs your application | Your application uses the runtime that the platform branch provides. Each .NET Core on Linux platform branch provides the ASP.NET Core Runtime, which includes the .NET Runtime, for one .NET major version. | Your application uses the runtime in your source bundle, not the platform's runtime. | 
| Platform branches that can run your application | Only the platform branch for the .NET major version that your application targets can run it, unless you configure roll forward. For details, see [Publishing a runtime-dependent application](#dotnet-linux-platform-bundle-app-runtime-dependent). | Any .NET Core on Linux platform branch can run it. | 
| .NET security patches | Platform updates include new .NET patch releases. After you update your environment's platform version, either manually or with [managed platform updates](environment-platform-update-managed.md), your application uses the newer patch release. You don't need to republish your application. | Platform updates don't change the runtime in your source bundle. To get a newer .NET patch release, republish your application with an updated .NET SDK, and then deploy it again. | 
| Processor architecture | If you publish without a runtime identifier (RID), your application runs on both x86\_64 and arm64 instance types. | Your application runs only on the processor architecture that you publish it for: linux-x64 for x86\_64 or linux-arm64 for arm64. | 

We recommend runtime-dependent applications for most workloads, because platform updates keep the .NET runtime patched for you. Choose a self-contained application when you need a .NET version that no .NET Core on Linux platform branch provides, or when you need to control exactly which .NET patch release your application runs on.

For more information about both types, see [.NET application publishing overview](https://learn.microsoft.com/en-us/dotnet/core/deploying/) in the .NET documentation.

## Publishing a runtime-dependent application
<a name="dotnet-linux-platform-bundle-app-runtime-dependent"></a>

Runtime-dependent is the default publishing mode. To publish a runtime-dependent application that runs on both x86\_64 and arm64 instances, don't specify a runtime identifier (RID).

```
~/myapp$ dotnet publish -c Release
```

By default, the command writes its output to the `bin/Release/{{net10.0}}/publish` folder of your project, where {{net10.0}} is your project's target framework.

Choose the platform branch for the .NET major version that your application targets. For example, if your project targets `net10.0`, choose the *.NET 10 on AL2023* platform branch. For a list of platform branches, see [.NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.dotnetlinux) in the *AWS Elastic Beanstalk Platforms* guide.

When your application starts, the .NET host reads your application's `runtimeconfig.json` file and uses the latest installed patch release of the .NET version that your application targets.

**Important**  
By default, .NET doesn't run an application on a different .NET major version than the one that it targets. If your application targets a different major version than your platform branch provides, your application doesn't start. As a result, the deployment fails. The application's output in the instance logs includes the message `You must install or update .NET to run this application`. To let your application run on a later major version, set the `RollForward` property in your project file, for example `<RollForward>Major</RollForward>`. Before you change this setting, review [Select which .NET version to use](https://learn.microsoft.com/en-us/dotnet/core/versions/selection) in the .NET documentation.

## Publishing a self-contained application
<a name="dotnet-linux-platform-bundle-app-self-contained"></a>

To publish a self-contained application, specify a Linux runtime identifier (RID) and the `--self-contained true` option. The following command publishes an application for instances with x86\_64 processors.

```
~/myapp$ dotnet publish -c Release -r linux-x64 --self-contained true
```

For instances with arm64 (AWS Graviton) processors, specify `-r linux-arm64` instead. The RID must match the processor architecture of your environment's instance types. Otherwise, your application doesn't start.

By default, the command writes its output to the `bin/Release/{{net10.0}}/{{linux-x64}}/publish` folder of your project, where {{net10.0}} is your project's target framework and {{linux-x64}} is the RID.

For a list of RIDs, see [.NET Runtime Identifier (RID) catalog](https://learn.microsoft.com/en-us/dotnet/core/rid-catalog) in the .NET documentation. For information about the processor architectures of instance types, see [Amazon EC2 instance types](using-features.managing.ec2.instance-types.md).

**Important**  
For applications that target .NET 8 or later, specifying a runtime identifier no longer makes an application self-contained. If you omit the `--self-contained true` option (or the `SelfContained` project property), `dotnet publish` creates a runtime-dependent application, and Elastic Beanstalk runs it as one. For more information, see [Breaking change: Runtime-specific apps no longer self-contained](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/runtimespecific-app-default) in the .NET documentation.

Platform updates don't change the .NET runtime in your source bundle. To get .NET security patches, republish your application with an updated .NET SDK, and then deploy it again.

Because your application doesn't use the platform's .NET runtime, you can deploy it to any .NET Core on Linux platform branch. We recommend that you use a .NET version that Microsoft still supports. For more information, see [.NET and .NET Core Support Policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) on the .NET website.

## Source bundle structure
<a name="dotnet-linux-platform-bundle-app-structure"></a>

Create your source bundle from the contents of your publish folder, not from the folder itself. The published files must be at the root of the source bundle. Otherwise, Elastic Beanstalk can't find your application, and the deployment fails. Also place any `Procfile`, `.ebextensions` folder, and `.platform` folder at the root. For instructions on zipping your files, see [Creating a source bundle from the command line](applications-sourcebundle.md#using-features.deployment.source.commandline).
+ **One application** – Place the application's files at the root of the source bundle. Include only one file with the `.runtimeconfig.json` suffix at the root. A `Procfile` is optional.
+ **Multiple applications** – Place each application in its own top-level folder, and include a [Procfile](dotnet-linux-procfile.md) at the root that starts each application.

During deployment, Elastic Beanstalk finds each application by its `{{name}}.runtimeconfig.json` file, where {{name}} is your application's assembly name. Elastic Beanstalk reads the `runtimeOptions` section of the file to determine the application type, as shown in the following table.


| Application type | `runtimeOptions` section | Expected file in the same folder | Command that Elastic Beanstalk runs if there's no `Procfile` | 
| --- | --- | --- | --- | 
| Runtime-dependent | Includes a framework or frameworks entry | {{name}}.dll | dotnet {{name}}.dll | 
| Self-contained | Includes neither entry | The executable file {{name}} | ./{{name}} | 

If the expected file is missing, the deployment fails, even if your source bundle includes a `Procfile`. Elastic Beanstalk sets execute permissions on the expected file, so a self-contained executable that you package on Windows can still run.

Elastic Beanstalk reports whether it found a runtime-dependent or a self-contained application in the [environment's events](using-features.events.md).

## Examples
<a name="dotnet-linux-platform-bundle-app-examples"></a>

The following examples show source bundles for the .NET Core on Linux platform.

The following example file structure defines a single runtime-dependent application.

```
├── appsettings.Development.json
├── appsettings.json
├── dotnetcoreapp.deps.json
├── dotnetcoreapp.dll
├── dotnetcoreapp.pdb
├── dotnetcoreapp.runtimeconfig.json
├── web.config
├── Procfile
├── .ebextensions
├── .platform
```

The following example file structure defines a single self-contained application. `dotnetcoreapp` is the executable file that Elastic Beanstalk runs. The .NET runtime files are also at the root of the source bundle. This example shows only some of them.

```
├── appsettings.Development.json
├── appsettings.json
├── dotnetcoreapp
├── dotnetcoreapp.deps.json
├── dotnetcoreapp.dll
├── dotnetcoreapp.pdb
├── dotnetcoreapp.runtimeconfig.json
├── libclrjit.so
├── libcoreclr.so
├── libhostfxr.so
├── libhostpolicy.so
├── Microsoft.AspNetCore.dll
├── System.Private.CoreLib.dll
├── System.Runtime.dll
├── ...
├── .ebextensions
├── .platform
```

You can include multiple applications in your source bundle. The following example defines two applications to run on the same web server. To run multiple applications, you must include a [Procfile](dotnet-linux-procfile.md) in your source bundle. For a full example application, see [dotnet-core-linux-multiple-apps.zip](samples/dotnet-core-linux-multiple-apps.zip).

```
├── DotnetMultipleApp1
│   ├── Amazon.Extensions.Configuration.SystemsManager.dll
│   ├── appsettings.Development.json
│   ├── appsettings.json
│   ├── AWSSDK.Core.dll
│   ├── AWSSDK.Extensions.NETCore.Setup.dll
│   ├── AWSSDK.SimpleSystemsManagement.dll
│   ├── DotnetMultipleApp1.deps.json
│   ├── DotnetMultipleApp1.dll
│   ├── DotnetMultipleApp1.pdb
│   ├── DotnetMultipleApp1.runtimeconfig.json
│   ├── Microsoft.Extensions.PlatformAbstractions.dll
│   ├── Newtonsoft.Json.dll
│   └── web.config
├── DotnetMultipleApp2
│   ├── Amazon.Extensions.Configuration.SystemsManager.dll
│   ├── appsettings.Development.json
│   ├── appsettings.json
│   ├── AWSSDK.Core.dll
│   ├── AWSSDK.Extensions.NETCore.Setup.dll
│   ├── AWSSDK.SimpleSystemsManagement.dll
│   ├── DotnetMultipleApp2.deps.json
│   ├── DotnetMultipleApp2.dll
│   ├── DotnetMultipleApp2.pdb
│   ├── DotnetMultipleApp2.runtimeconfig.json
│   ├── Microsoft.Extensions.PlatformAbstractions.dll
│   ├── Newtonsoft.Json.dll
│   └── web.config
├── Procfile
├── .ebextensions
├── .platform
```

The applications in this sample target .NET 6 and set `rollForward` to `LatestMajor` in their `runtimeconfig.json` files, so they run on the .NET runtime of any .NET Core on Linux platform branch. For more information, see [Publishing a runtime-dependent application](#dotnet-linux-platform-bundle-app-runtime-dependent).