

# Running multiple applications and ASP.NET core applications with a deployment manifest
<a name="dotnet-manifest"></a>

You can use a deployment manifest to tell Elastic Beanstalk how to deploy your application. By using this method, you don't need to use `MSDeploy` to generate a source bundle for a single ASP.NET application that runs at the root path of your website. Rather, you can use a manifest file to run multiple applications at different paths. Or, alternatively, you can tell Elastic Beanstalk to deploy and run the app with ASP.NET Core. You can also use a deployment manifest to configure an application pool where to run your applications.

Deployment manifests add support for [.NET Core applications](#dotnet-manifest-dotnetcore) to Elastic Beanstalk. You can deploy a .NET Framework application without a deployment manifest. However, .NET Core applications require a deployment manifest to run on Elastic Beanstalk. When you use a deployment manifest, you create a site archive for each application, and then bundle the site archives in a second ZIP archive that contains the deployment manifest.

Deployment manifests also add the ability to [run multiple applications at different paths](#dotnet-manifest-multiapp). A deployment manifest defines an array of deployment targets, each with a site archive and a path at which IIS should run it. For example, you could run a web API at the `/api` path to serve asynchronous requests, and a web app at the root path that consumes the API.

You can use a deployment manifest to [configure IIS websites with custom bindings and physical paths](#dotnet-manifest-websites). This allows you to set up websites that listen on specific ports or host names before deploying your applications.

You can also use a deployment manifest to [run multiple applications using application pools in IIS or Kestrel](#dotnet-manifest-apppool). You can configure an application pool to restart your applications periodically, run 32-bit applications, or use a specific version of the .NET Framework runtime.

For full customization, you can [write your own deployment scripts](#dotnet-manifest-custom) in Windows PowerShell and tell Elastic Beanstalk which scripts to run to install, uninstall, and restart your application.

Deployment manifests and related features require a Windows Server platform [version 1.2.0 or newer](dotnet-v2migration.md).

For detailed information about all available configuration options, properties, and advanced features like skipping IIS resets, see the [deployment manifest schema reference](dotnet-manifest-schema.md).

**Topics**
+ [.NET core apps](#dotnet-manifest-dotnetcore)
+ [Run multiple applications](#dotnet-manifest-multiapp)
+ [Configure IIS websites](#dotnet-manifest-websites)
+ [Using Application Request Routing (ARR)](#dotnet-manifest-arr)
+ [Configure application pools](#dotnet-manifest-apppool)
+ [Define custom deployments](#dotnet-manifest-custom)
+ [Deployment manifest schema reference](dotnet-manifest-schema.md)

## .NET core apps
<a name="dotnet-manifest-dotnetcore"></a>

You can use a deployment manifest to run .NET Core applications on Elastic Beanstalk. .NET Core is a cross-platform version of .NET that comes with a command line tool (`dotnet`). You can use it to generate an application, run it locally, and prepare it for publishing.

To run a .NET Core application on Elastic Beanstalk, you can run `dotnet publish` and package the output in a ZIP archive, not including any containing directories. Place the site archive in a source bundle with a deployment manifest with a deployment target of type `aspNetCoreWeb`.

The following deployment manifest runs a .NET Core application from a site archive named `dotnet-core-app.zip` at the root path.

**Example aws-windows-deployment-manifest.json - .NET core**  

```
{
  "manifestVersion": 1,
  "deployments": {
    "aspNetCoreWeb": [
      {
        "name": "my-dotnet-core-app",
        "parameters": {
          "archive": "dotnet-core-app.zip",
          "iisPath": "/"
        }
      }
    ]
  }
}
```

Bundle the manifest and site archive in a ZIP archive to create a source bundle.

**Example dotnet-core-bundle.zip**  

```
.
|-- aws-windows-deployment-manifest.json
`-- dotnet-core-app.zip
```

The site archive contains the compiled application code, dependencies, and `web.config` file.

**Example dotnet-core-app.zip**  

```
.
|-- Microsoft.AspNetCore.Hosting.Abstractions.dll
|-- Microsoft.AspNetCore.Hosting.Server.Abstractions.dll
|-- Microsoft.AspNetCore.Hosting.dll
|-- Microsoft.AspNetCore.Http.Abstractions.dll
|-- Microsoft.AspNetCore.Http.Extensions.dll
|-- Microsoft.AspNetCore.Http.Features.dll
|-- Microsoft.AspNetCore.Http.dll
|-- Microsoft.AspNetCore.HttpOverrides.dll
|-- Microsoft.AspNetCore.Server.IISIntegration.dll
|-- Microsoft.AspNetCore.Server.Kestrel.dll
|-- Microsoft.AspNetCore.WebUtilities.dll
|-- Microsoft.Extensions.Configuration.Abstractions.dll
|-- Microsoft.Extensions.Configuration.EnvironmentVariables.dll
|-- Microsoft.Extensions.Configuration.dll
|-- Microsoft.Extensions.DependencyInjection.Abstractions.dll
|-- Microsoft.Extensions.DependencyInjection.dll
|-- Microsoft.Extensions.FileProviders.Abstractions.dll
|-- Microsoft.Extensions.FileProviders.Physical.dll
|-- Microsoft.Extensions.FileSystemGlobbing.dll
|-- Microsoft.Extensions.Logging.Abstractions.dll
|-- Microsoft.Extensions.Logging.dll
|-- Microsoft.Extensions.ObjectPool.dll
|-- Microsoft.Extensions.Options.dll
|-- Microsoft.Extensions.PlatformAbstractions.dll
|-- Microsoft.Extensions.Primitives.dll
|-- Microsoft.Net.Http.Headers.dll
|-- System.Diagnostics.Contracts.dll
|-- System.Net.WebSockets.dll
|-- System.Text.Encodings.Web.dll
|-- dotnet-core-app.deps.json
|-- dotnet-core-app.dll
|-- dotnet-core-app.pdb
|-- dotnet-core-app.runtimeconfig.json
`-- web.config
```

## Run multiple applications
<a name="dotnet-manifest-multiapp"></a>

You can run multiple applications with a deployment manifest by defining multiple deployment targets.

The following deployment manifest configures two .NET Core applications. The `WebApiSampleApp` application implements a simple web API and serves asynchronous requests at the `/api` path. The `DotNetSampleApp` application is a web application that serves requests at the root path.

**Example aws-windows-deployment-manifest.json - multiple apps**  

```
{
  "manifestVersion": 1,
  "deployments": {
    "aspNetCoreWeb": [
      {
        "name": "WebAPISample",
        "parameters": {
          "appBundle": "WebApiSampleApp.zip",
          "iisPath": "/api"
        }
      },
      {
        "name": "DotNetSample",
        "parameters": {
          "appBundle": "DotNetSampleApp.zip",
          "iisPath": "/"
        }
      }
    ]
  }
}
```

A sample application with multiple applications is available here:
+ **Deployable source bundle** - [dotnet-multiapp-sample-bundle-v2.zip](samples/dotnet-multiapp-sample-bundle-v2.zip)
+ **Source code** - [dotnet-multiapp-sample-source-v2.zip](samples/dotnet-multiapp-sample-source-v2.zip)

## Configure IIS websites
<a name="dotnet-manifest-websites"></a>

You can configure IIS websites with custom bindings and physical paths using the deployment manifest. This is useful when you need to set up websites that listen on specific ports, use custom host names, or serve content from specific directories.

The following deployment manifest configures a custom IIS website that listens on HTTP with a specific port number and a custom physical path:

**Example aws-windows-deployment-manifest.json - IIS website configuration**  

```
{
  "manifestVersion": 1,
  "iisConfig": {
    "websites": [
      {
        "name": "MyCustomSite",
        "physicalPath": "C:\inetpub\wwwroot\mysite",
        "bindings": [
          {
            "protocol": "http",
            "port": 8080,
            "hostName": "mysite.local"
          }
        ]
      }
    ]
  },
  "deployments": {
    "aspNetCoreWeb": [
      {
        "name": "my-dotnet-core-app",
        "parameters": {
          "appBundle": "dotnet-core-app.zip",
          "iisWebSite": "MyCustomSite",
          "iisPath": "/"
        }
      }
    ]
  }
}
```

In this example:
+ A website named "MyCustomSite" is created with a custom physical path
+ The website has an HTTP binding on port 8080 with a specific host name
+ The ASP.NET Core application is deployed to this custom website using the `iisWebSite` parameter

## Using Application Request Routing (ARR)
<a name="dotnet-manifest-arr"></a>

Application Request Routing (ARR) and URL Rewrite modules are pre-installed and available in Elastic Beanstalk Windows AMIs. These modules enable advanced routing scenarios and URL manipulation through IIS configuration using ebextensions or application configuration.

The following example shows a simple deployment manifest that configures a website with a custom port, combined with an ebextensions configuration that sets up basic ARR routing:

**Example aws-windows-deployment-manifest.json - Simple ARR setup**  

```
{
  "manifestVersion": 1,
  "iisConfig": {
    "websites": [
      {
        "name": "ARRSite",
        "physicalPath": "C:\\inetpub\\wwwroot\\arrsite",
        "bindings": [
          {
            "protocol": "http",
            "port": 8080,
            "hostName": "localhost"
          }
        ]
      }
    ]
  },
  "deployments": {
    "aspNetCoreWeb": [
      {
        "name": "BackendApp",
        "parameters": {
          "appBundle": "backend-app.zip",
          "iisWebSite": "ARRSite",
          "iisPath": "/backend"
        }
      }
    ]
  }
}
```

ARR configuration is done through ebextensions. The following configuration sets up basic ARR routing rules:

**Example .ebextensions/arr-config.config - Basic ARR configuration**  

```
files:
  "C:\\temp\\configure-arr.ps1":
    content: |
      # Enable ARR proxy at server level
      Set-WebConfigurationProperty -PSPath 'MACHINE/WEBROOT/APPHOST' -Filter 'system.webServer/proxy' -Name 'enabled' -Value 'True'
      
      # Clear any existing global rules to avoid conflicts
      Clear-WebConfiguration -PSPath 'MACHINE/WEBROOT/APPHOST' -Filter 'system.webServer/rewrite/globalRules'

      # Add global rule to route all requests to backend
      Add-WebConfigurationProperty -PSPath 'MACHINE/WEBROOT/APPHOST' `
        -Filter 'system.webServer/rewrite/globalRules' `
        -Name '.' `
        -Value @{
          name = 'Route_to_Backend'
          stopProcessing = 'True'
          match = @{ url = '^(?!backend/)(.*)' }
          action = @{
            type = 'Rewrite'
            url = 'http://localhost:8080/backend/{R:1}'
          }
        }

container_commands:
  01_configure_arr:
    command: powershell -ExecutionPolicy Bypass -File "C:\\temp\\configure-arr.ps1"
    waitAfterCompletion: 0
```

This configuration creates a website on port 8080 and sets up ARR to route all incoming requests to the backend application running on that site.

## Configure application pools
<a name="dotnet-manifest-apppool"></a>

You can support multiple applications in your Windows environment. Two approaches are available:
+ You can use the out-of-process hosting model with the Kestrel web server. With this model, you configure multiple applications to run in one application pool.
+ You can use the in-process hosting model. With this model, you use multiple application pools to run multiple applications with only one application in each pool. If you're using IIS server and need to run multiple applications, you must use this approach.

To configure Kestrel to run multiple applications in one application pool, add `hostingModel="OutofProcess"` in the `web.config` file. Consider the following examples.

**Example web.config - for Kestrel out-of-process hosting model**  

```
<configuration>
<location path="." inheritInChildApplications="false">
<system.webServer>
<handlers>
<add 
    name="aspNetCore" 
    path="*" verb="*" 
    modules="AspNetCoreModuleV2" 
    resourceType="Unspecified" />
</handlers>
<aspNetCore 
    processPath="dotnet" 
    arguments=".\CoreWebApp-5-0.dll" 
    stdoutLogEnabled="false" 
    stdoutLogFile=".\logs\stdout" 
    hostingModel="OutofProcess" />
</system.webServer>
</location>
</configuration>
```

**Example aws-windows-deployment-manifest.json - multiple applications**  

```
{
"manifestVersion": 1,
  "deployments": {"msDeploy": [
      {"name": "Web-app1",
        "parameters": {"archive": "site1.zip",
          "iisPath": "/"
        }
      },
      {"name": "Web-app2",
        "parameters": {"archive": "site2.zip",
          "iisPath": "/app2"
        }
      }
    ]
  }
}
```

IIS doesn't support multiple applications in one application pool because it uses the in-process hosting model. Therefore, you need to configure multiple applications by assigning each application to one application pool. In other words, assign only one application to one application pool.

You can configure IIS to use different application pools in the `aws-windows-deployment-manifest.json` file. Make the following updates as you refer to the next example file:
+ Add an `iisConfig` section that includes a subsection called `appPools`.
+ In the `appPools` block, list the application pools. 
+ In the `deployments` section, define a `parameters` section for each application.
+ For each application the `parameters` section specifies an archive, a path to run it, and an `appPool` in which to run.

The following deployment manifest configures two application pools that restart their application every 10 minutes. They also attach their applications to a .NET Framework web application that runs at the path specified.

**Example aws-windows-deployment-manifest.json - one application per application pool**  

```
{
"manifestVersion": 1,
  "iisConfig": {"appPools": [
      {"name": "MyFirstPool",
       "recycling": {"regularTimeInterval": 10}
      },
      {"name": "MySecondPool",
       "recycling": {"regularTimeInterval": 10}
      }
     ]
    },
  "deployments": {"msDeploy": [
      {"name": "Web-app1",
        "parameters": {
           "archive": "site1.zip",
           "iisPath": "/",
           "appPool": "MyFirstPool"
           }
      },
      {"name": "Web-app2",
        "parameters": {
           "archive": "site2.zip",
           "iisPath": "/app2",
           "appPool": "MySecondPool"
          }
      }
     ]
    }
}
```

## Define custom deployments
<a name="dotnet-manifest-custom"></a>

For even more control, you can completely customize an application deployment by defining a *custom deployment*. With a custom deployment, Elastic Beanstalk runs only the PowerShell scripts that you provide—it performs no IIS management on your behalf. This differs from `msDeploy` and `aspNetCoreWeb` deployments, where Elastic Beanstalk automatically stops IIS before installing, starts it afterward, and restarts it when needed. For a custom deployment, your scripts place the application content, configure the environment (for example, IIS), and restart the application.

**Important**  
In a load-balanced web server environment, Elastic Beanstalk checks instance health by requesting the environment's health check path (`/` by default) on port 80. Something must serve that path, or the environment becomes unhealthy even though every deployment script succeeds—a common cause of a custom deployment that completes without errors but leaves the environment in a red state. For a standalone custom deployment, serve your application from the root of the **Default Web Site**. It's valid to place a custom application under a sub-path when another deployment already serves the health check path—for example, in a [multiple-application manifest](#dotnet-manifest-multiapp). For more information about environment health, see [Monitoring environments](environments-health.md).

A custom deployment defines up to three scripts. The following table describes each script, when Elastic Beanstalk runs it, and what your script must do.


| Script | When Elastic Beanstalk runs it | Responsibility | 
| --- | --- | --- | 
| uninstall | Before each new application version is installed, that is, before each application deployment. | Stop the service or remove the previous version's files. | 
| install | During each application deployment. | Deploy files, configure IIS or your service, and serve the application at the health check path. | 
| restart | After every application deployment and after every configuration change. If you set skipIISReset to true, Elastic Beanstalk skips this script on application deployments but still runs it on configuration changes. Choosing Restart App Server performs a platform-level iisreset and does not invoke your custom restart script. | Restart IIS (iisreset) or your service so that the new version is live. | 

These scripts also run whenever Elastic Beanstalk deploys your application to a newly launched instance—for example, during initial environment creation and when Auto Scaling adds an instance (scale-out)—because each new instance installs the application as it bootstraps.

The following deployment manifest instructs Elastic Beanstalk to run PowerShell scripts in 32-bit mode. It specifies an `install` script (`install.ps1`), a `restart` script (`restart.ps1`), and an `uninstall` script (`uninstall.ps1`). The `uninstall` script sets `ignoreErrors` to `true` so that the first deployment—when there is nothing to remove—doesn't fail.

**Example aws-windows-deployment-manifest.json - custom deployment**  

```
{
  "manifestVersion": 1,
  "deployments": {
    "custom": [
      {
        "name": "Custom site",
        "architecture": 32,
        "scripts": {
          "install": {
            "file": "install.ps1"
          },
          "restart": {
            "file": "restart.ps1"
          },
          "uninstall": {
            "file": "uninstall.ps1",
            "ignoreErrors": true
          }
        }
      }
    ]
  }
}
```

Include any artifacts required to run the application in your source bundle with the manifest and scripts. Elastic Beanstalk doesn't extract these artifacts for a custom deployment—your scripts must extract them. In the following example, the application content is packaged as `MyApp.zip`.

**Example Custom-site-bundle.zip**  

```
.
|-- aws-windows-deployment-manifest.json
|-- install.ps1
|-- restart.ps1
|-- uninstall.ps1
`-- MyApp.zip
```

The following scripts show a complete, health-check-correct custom deployment for an IIS-hosted application. The `install.ps1` script extracts the application content and points the Default Web Site's physical path at it, so that the application is served from the root path (`/`) where the health check looks.

**Example install.ps1**  

```
$ErrorActionPreference = "Stop"
$appPath = "C:\inetpub\MyApp"
if (Test-Path $appPath) { Remove-Item $appPath -Recurse -Force }

# Elastic Beanstalk doesn't extract your bundle for custom deployments, so extract it yourself.
# MyApp.zip ships in the bundle, alongside this script. Resolve it relative to the script's
# own location so the path is reliable regardless of the current working directory.
$scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$bundleZip = Join-Path $scriptDir "MyApp.zip"
Add-Type -AssemblyName "System.IO.Compression.FileSystem"
[IO.Compression.ZipFile]::ExtractToDirectory($bundleZip, $appPath)

# Serve from the Default Web Site root ("/"), where the health check looks.
Import-Module WebAdministration
Set-ItemProperty "IIS:\Sites\Default Web Site" -Name physicalPath -Value $appPath

iisreset.exe /restart
if ($LASTEXITCODE -ne 0) { exit 1 }
```

**Example restart.ps1**  

```
$ErrorActionPreference = "Stop"
iisreset.exe /restart
if ($LASTEXITCODE -ne 0) { exit 1 }
```

**Example uninstall.ps1**  

```
# Stop IIS first. While the site is live, w3wp holds locks on files under the app directory,
# which would make the following removal fail.
iisreset.exe /stop | Out-Null
Remove-Item "C:\inetpub\MyApp" -Recurse -Force -ErrorAction SilentlyContinue
```

Keep the following points in mind when you write custom deployment scripts:
+ **Serve the health check path.** Point the Default Web Site's physical path at your application, or otherwise deploy to the health check path, so that the health check succeeds.
+ **Include a default document.** If the site root has no default document, `GET /` returns HTTP 403 and the health check fails. Ship a `web.config` file that sets a `<defaultDocument>` element, or name your landing page to match an IIS default document name, such as `Default.htm` or `index.htm`.
+ **Restart IIS yourself.** Because Elastic Beanstalk performs no IIS management for custom deployments, your scripts must run `iisreset` so that changes take effect.
+ **Locate bundled files relative to the script.** Elastic Beanstalk extracts your scripts and bundled artifacts together into the same directory. Resolve bundled files against `$PSScriptRoot` (the folder that contains the running script) rather than assuming a particular current working directory.
+ **Make failures fail the deployment.** Set `$ErrorActionPreference = "Stop"` and check `$LASTEXITCODE` after external commands. Otherwise, a broken script can exit successfully, and Elastic Beanstalk treats the deployment as successful even though the application isn't running correctly.

### Example: a self-hosted Windows service
<a name="dotnet-manifest-custom-service"></a>

With a custom deployment, you can run a Windows service instead of an IIS-hosted site. Elastic Beanstalk Windows platforms don't support the worker environment tier. In a load-balanced environment, the load balancer checks the health check path on port 80, so a Windows service must answer that request to keep the environment healthy. The following example is a self-hosted service that listens on port 80 itself, so it needs no companion IIS site.

**Note**  
Because Windows platforms have no worker tier, a background-only service still needs to answer the health check in a load-balanced environment. Either have the service also answer the health check path (as shown here) or run the background work alongside a site that serves it.

The manifest runs the scripts in 64-bit mode, matching the 64-bit C\# compiler used to build the service.

**Example aws-windows-deployment-manifest.json - Windows service**  

```
{
  "manifestVersion": 1,
  "deployments": {
    "custom": [
      {
        "name": "EbCustomService",
        "architecture": 64,
        "scripts": {
          "install": {
            "file": "serviceInstall.ps1"
          },
          "restart": {
            "file": "serviceRestart.ps1"
          },
          "uninstall": {
            "file": "serviceUninstall.ps1",
            "ignoreErrors": true
          }
        }
      }
    ]
  }
}
```

The bundle ships the manifest, the three scripts, the service source code, and a `version.txt` file (whose contents are the version string, for example `v1`). The install script compiles the service on the instance, so you don't need a build toolchain in your bundle.

**Example Custom-service-bundle.zip**  

```
.
|-- aws-windows-deployment-manifest.json
|-- EbCustomService.cs
|-- serviceInstall.ps1
|-- serviceRestart.ps1
|-- serviceUninstall.ps1
`-- version.txt
```

The `serviceInstall.ps1` script frees port 80 from IIS, compiles the service from the bundled source with the in-box C\# compiler (`csc.exe`), registers it as a `LocalSystem` service, and starts it. Running as `LocalSystem` lets the service bind `http://+:80/` without a URL ACL reservation, which keeps the example minimal. In production, prefer a least-privilege account such as `NetworkService` and grant it the binding explicitly with `netsh http add urlacl`.

**Example serviceInstall.ps1**  

```
# INSTALL: compile and register a self-hosted HTTP service that owns port 80.
$ErrorActionPreference = "Stop"

$svcName = "EbCustomService"
$appPath = "C:\CustomService"
$scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }

# Free port 80 from IIS and keep it from reclaiming the port on reboot.
Stop-Service W3SVC -Force -ErrorAction SilentlyContinue
Set-Service  W3SVC -StartupType Manual -ErrorAction SilentlyContinue

# Fresh application directory.
if (Test-Path $appPath) { Remove-Item $appPath -Recurse -Force }
New-Item -ItemType Directory -Path $appPath | Out-Null

# Compile the service with the in-box .NET Framework compiler (no build tooling needed).
$csc = Join-Path $env:WINDIR "Microsoft.NET\Framework64\v4.0.30319\csc.exe"
$src = Join-Path $scriptDir "EbCustomService.cs"
$exe = Join-Path $appPath "EbCustomService.exe"
& $csc /nologo /target:exe /out:"$exe" /reference:System.ServiceProcess.dll "$src"
if ($LASTEXITCODE -ne 0) { exit 1 }

# Write the content served at "/". A real service would serve its own responses;
# here the install script writes a simple marker so the health check passes.
$version = (Get-Content (Join-Path $scriptDir "version.txt") -Raw).Trim()
Set-Content -Path (Join-Path $appPath "marker.txt") `
    -Value "Custom service deployment $version succeeded" -NoNewline

# Register as a LocalSystem service so it can bind http://+:80/ without a URL ACL.
if (Get-Service $svcName -ErrorAction SilentlyContinue) {
    Stop-Service $svcName -Force -ErrorAction SilentlyContinue
    sc.exe delete $svcName | Out-Null
    # sc.exe delete is async; poll until gone so New-Service below doesn't hit
    # "service marked for deletion".
    $deadline = (Get-Date).AddSeconds(30)
    while ((Get-Service $svcName -ErrorAction SilentlyContinue) -and (Get-Date) -lt $deadline) {
        Start-Sleep -Milliseconds 500
    }
}
New-Service -Name $svcName -BinaryPathName "`"$exe`"" `
    -DisplayName "EB Custom Service" -StartupType Automatic | Out-Null
Start-Service $svcName
```

The `serviceRestart.ps1` script restarts the service so that the new version becomes live.

**Example serviceRestart.ps1**  

```
# RESTART: restart the service so the new version becomes live.
$ErrorActionPreference = "Stop"

$svcName = "EbCustomService"

Restart-Service $svcName -Force
```

The `serviceUninstall.ps1` script stops and deletes the service and removes the previous version's files. The manifest sets `ignoreErrors` to `true` for this script because the first deployment has no previous version to remove.

**Example serviceUninstall.ps1**  

```
# UNINSTALL: stop and remove the previous version before the new install.
# The manifest sets ignoreErrors:true because the first deploy has nothing to remove.
$ErrorActionPreference = "Stop"

$svcName = "EbCustomService"
$appPath = "C:\CustomService"

if (Get-Service $svcName -ErrorAction SilentlyContinue) {
    Stop-Service $svcName -Force -ErrorAction SilentlyContinue
    sc.exe delete $svcName | Out-Null
    # sc.exe delete is async; poll until the service is really gone so the next
    # deploy's New-Service doesn't hit "service marked for deletion".
    $deadline = (Get-Date).AddSeconds(30)
    while ((Get-Service $svcName -ErrorAction SilentlyContinue) -and (Get-Date) -lt $deadline) {
        Start-Sleep -Milliseconds 500
    }
}
if (Test-Path $appPath) {
    Remove-Item $appPath -Recurse -Force -ErrorAction SilentlyContinue
}
```

The service itself is a small C\# program that hosts an `HttpListener` on `http://+:80/` and returns a text response for `GET /`, which is what satisfies the load balancer health check.

**Example EbCustomService.cs**  

```
// Minimal self-hosted HTTP Windows service. Hosts an HttpListener on http://+:80/
// and answers the load balancer's GET "/" health check with the content that the
// install script wrote to marker.txt.
using System;
using System.IO;
using System.Net;
using System.ServiceProcess;
using System.Text;
using System.Threading;

namespace EbCustomService
{
    public class MarkerService : ServiceBase
    {
        private const string Root = @"C:\CustomService";
        private HttpListener _listener;
        private Thread _worker;
        private volatile bool _running;

        public MarkerService()
        {
            this.ServiceName = "EbCustomService";
        }

        protected override void OnStart(string[] args)
        {
            _running = true;
            _listener = new HttpListener();
            _listener.Prefixes.Add("http://+:80/");
            _listener.Start();
            _worker = new Thread(Loop) { IsBackground = true };
            _worker.Start();
        }

        protected override void OnStop()
        {
            _running = false;
            try { if (_listener != null) _listener.Stop(); } catch { }
        }

        private void Loop()
        {
            while (_running)
            {
                HttpListenerContext ctx;
                try { ctx = _listener.GetContext(); }
                catch { break; }
                try
                {
                    byte[] buf = Encoding.UTF8.GetBytes(ReadFile(Path.Combine(Root, "marker.txt")));
                    ctx.Response.StatusCode = 200;
                    ctx.Response.ContentType = "text/plain";
                    ctx.Response.ContentLength64 = buf.Length;
                    ctx.Response.OutputStream.Write(buf, 0, buf.Length);
                    ctx.Response.OutputStream.Close();
                }
                catch { }
            }
        }

        private static string ReadFile(string p)
        {
            try { return File.Exists(p) ? File.ReadAllText(p) : ""; }
            catch { return ""; }
        }

        public static void Main()
        {
            ServiceBase.Run(new MarkerService());
        }
    }
}
```

**Note**  
In this example, the response served at `/` is a small text marker (`marker.txt`) that stands in for your application's real content. A production service would serve its own responses instead. Everything else in these scripts is the minimum required for a working Windows service custom deployment.