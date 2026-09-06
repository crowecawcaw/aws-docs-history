

# Deployment manifest schema reference
<a name="dotnet-manifest-schema"></a>

The deployment manifest is a JSON file that defines how Elastic Beanstalk should deploy and configure your Windows applications. This section provides a comprehensive reference for all supported properties and configuration options in the manifest schema.

## Manifest structure
<a name="dotnet-manifest-schema-structure"></a>

The deployment manifest follows a specific JSON schema with the following top-level structure:

**Example Basic manifest structure**  

```
{
  "manifestVersion": 1,
  "skipIISReset": false,
  "iisConfig": {
    "websites": [...],
    "appPools": [...]
  },
  "deployments": {
    "msDeploy": [...],
    "aspNetCoreWeb": [...],
    "custom": [...]
  }
}
```

### Top-level properties
<a name="dotnet-manifest-schema-top-level"></a>

`manifestVersion` (required)  
*Type:* Number  
*Default:* 1  
*Valid values:* 1  
Specifies the version of the manifest schema. Currently, only version 1 is supported.

`skipIISReset` (optional)  
*Type:* Boolean  
*Default:* false  
Controls whether Elastic Beanstalk resets IIS during application deployments. This flag affects `msDeploy` and `aspNetCoreWeb` deployments. For `custom` deployments, it controls whether Elastic Beanstalk runs your custom restart script during application deployments.  
*Behavior:*  
+ *Not specified or `false` (default):* IIS resets are performed during install, uninstall, and update operations. This is the traditional behavior.
+ *`true`:* IIS resets are skipped during deployment operations.
*Benefits:*  
+ *Reduced downtime* – Applications experience shorter service interruptions during deployments.
+ *Faster deployments* – Eliminates the time required for IIS to fully restart and reinitialize.
When using `skipIISReset`, the [RestartAppServer](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RestartAppServer.html) operation performs an IIS reset regardless of this flag setting.
*Example:*  

```
{
  "manifestVersion": 1,
  "skipIISReset": true,
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

`deployments` (required)  
*Type:* Object  
Contains the deployment configurations for your applications. This object can include `msDeploy`, `aspNetCoreWeb`, and `custom` deployment types.

`iisConfig` (optional)  
*Type:* Object  
Defines IIS configuration settings to apply before deploying applications. Supports both website and application pool configuration.

## IIS configuration
<a name="dotnet-manifest-schema-iis-config"></a>

The `iisConfig` section allows you to configure IIS settings before deploying your applications. This includes setting up application pools with specific configurations and configuring IIS websites with custom bindings.

### IIS websites
<a name="dotnet-manifest-schema-websites"></a>

IIS websites allow you to configure custom website settings including physical paths and network bindings before deploying your applications.

**Important considerations for creating different IIS websites**  
*Website setup order:* Websites are configured sequentially in the order they appear in the `websites` array. The platform processes each website configuration in sequence, so ensure proper ordering if you have dependencies between websites.
*Firewall and port access:* Only port 80 is automatically exposed through the default Elastic Beanstalk Windows firewall configuration. If you configure websites to use non-standard ports, you must define custom firewall rules through ebextensions or custom deployment scripts to allow external access to these ports.

**Example Website configuration**  

```
{
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
          },
          {
            "protocol": "https",
            "port": 8443
          }
        ]
      }
    ]
  }
}
```Website properties

`name` (required)  
*Type:* String  
The name of the IIS website. This name is used to identify the website in IIS Manager and must be unique within the IIS configuration.

`physicalPath` (required)  
*Type:* String  
The physical path on the server where the website files are stored. This path must be accessible to the IIS worker process.

`bindings` (required)  
*Type:* Array  
*Minimum items:* 1  
An array of binding configurations that define how the website responds to network requests. Each binding specifies a protocol, port, and optional host name.

#### Website bindings
<a name="dotnet-manifest-schema-bindings"></a>

Website bindings define the network endpoints where your IIS website will listen for incoming requests.

`protocol` (required)  
*Type:* String  
*Valid values:* "http", "https"  
The protocol used for the binding.

`port` (required)  
*Type:* Integer  
*Valid range:* 1-65535  
The port number on which the website will listen for requests.

`hostName` (optional)  
*Type:* String  
The host name (domain name) for the binding.

### Application pools
<a name="dotnet-manifest-schema-app-pools"></a>

Application pools provide isolation between applications and allow you to configure runtime settings for groups of applications.

**Example Application pool configuration**  

```
{
  "iisConfig": {
    "appPools": [
      {
        "name": "MyAppPool",
        "enable32Bit": false,
        "managedPipelineMode": "Integrated",
        "managedRuntimeVersion": "v4.0",
        "queueLength": 1000,
        "cpu": {
          "limitPercentage": 80,
          "limitAction": "Throttle",
          "limitMonitoringInterval": 5
        },
        "recycling": {
          "regularTimeInterval": 1440,
          "requestLimit": 10000,
          "memory": 1048576,
          "privateMemory": 524288
        }
      }
    ]
  }
}
```Application pool properties

`name` (required)  
*Type:* String  
The name of the application pool. This name is used to reference the pool in deployment configurations.

`enable32Bit` (optional)  
*Type:* Boolean  
Enables a 32-bit application to run on a 64-bit version of Windows. Set to `true` for legacy applications that require 32-bit compatibility.

`managedPipelineMode` (optional)  
*Type:* String  
*Valid values:* "Integrated", "Classic"  
Specifies the request-processing mode for the application pool.

`managedRuntimeVersion` (optional)  
*Type:* String  
*Valid values:* "No Managed Code", "v2.0", "v4.0"  
Specifies the .NET Framework version for the application pool.

`queueLength` (optional)  
*Type:* Integer  
Maximum number of requests that HTTP.sys queues for the application pool before rejecting additional requests.

#### CPU configuration
<a name="dotnet-manifest-schema-cpu-config"></a>

The `cpu` object configures CPU usage limits and monitoring for the application pool.

`limitPercentage` (optional)  
*Type:* Number  
Maximum percentage of CPU time that worker processes in the application pool can consume.

`limitAction` (optional)  
*Type:* String  
*Valid values:* "NoAction", "KillW3wp", "Throttle", "ThrottleUnderLoad"  
Action to take when the CPU limit is reached.

`limitMonitoringInterval` (optional)  
*Type:* Number  
Reset period (in minutes) for CPU monitoring and throttling limits.

#### Recycling configuration
<a name="dotnet-manifest-schema-recycling-config"></a>

The `recycling` object configures when and how application pool worker processes are recycled.

`regularTimeInterval` (optional)  
*Type:* Integer  
Time interval (in minutes) after which the application pool recycles. Set to 0 to disable time-based recycling.

`requestLimit` (optional)  
*Type:* Integer  
Maximum number of requests the application pool processes before recycling.

`memory` (optional)  
*Type:* Integer  
Amount of virtual memory (in kilobytes) that triggers worker process recycling.

`privateMemory` (optional)  
*Type:* Integer  
Amount of private memory (in kilobytes) that triggers worker process recycling.

## Deployment types
<a name="dotnet-manifest-schema-deployments"></a>

The `deployments` object contains arrays of deployment configurations for different application types. Each deployment type has specific properties and use cases.

### MSDeploy deployments
<a name="dotnet-manifest-schema-msdeploy"></a>

MSDeploy deployments are used for traditional .NET Framework applications that can be deployed using Web Deploy (MSDeploy).

**Example MSDeploy deployment configuration**  

```
{
  "deployments": {
    "msDeploy": [
      {
        "name": "WebApp",
        "description": "Main web application",
        "parameters": {
          "appBundle": "webapp.zip",
          "iisPath": "/",
          "appPool": "DefaultAppPool"
        }
      }
    ]
  }
}
```MSDeploy deployment properties

`name` (required)  
*Type:* String  
Unique name for the deployment. This name must be unique across all deployments in the manifest.

`description` (optional)  
*Type:* String  
Human-readable description of the deployment.

`parameters` (required)  
*Type:* Object  
Configuration parameters for the MSDeploy operation.

`scripts` (optional)  
*Type:* Object  
PowerShell scripts to run at various stages of the deployment lifecycle.

#### MSDeploy parameters
<a name="dotnet-manifest-schema-msdeploy-parameters"></a>

`appBundle` (required)  
*Type:* String  
Path to the application bundle (ZIP file) relative to the manifest file. This bundle contains the application files to deploy.

`iisWebSite` (optional)  
*Type:* String  
*Default:* "Default Web Site"  
The IIS website to deploy the application to. By default, applications are deployed to the "Default Web Site". Optionally, you can specify a different website name, such as one configured in the `iisConfig.websites` section.

`iisPath` (optional)  
*Type:* String  
*Default:* "/"  
Virtual directory path in IIS where the application will be deployed. Use "/" for the root path or "/api" for a subdirectory.

`appPool` (optional)  
*Type:* String  
Name of the application pool to run this application.

### ASP.NET Core deployments
<a name="dotnet-manifest-schema-aspnetcore"></a>

ASP.NET Core deployments are specifically designed for .NET Core and .NET 5\+ applications.

**Example ASP.NET Core deployment configuration**  

```
{
  "deployments": {
    "aspNetCoreWeb": [
      {
        "name": "CoreAPI",
        "description": "ASP.NET Core Web API",
        "parameters": {
          "appBundle": "coreapi.zip",
          "iisPath": "/api",
          "appPool": "CoreAppPool"
        }
      }
    ]
  }
}
```

ASP.NET Core deployments use the same property structure as MSDeploy deployments, with the key difference being the runtime environment and hosting model used for the application.ASP.NET Core deployment parameters

`appBundle` (required)  
*Type:* String  
Path to the application bundle relative to the manifest file. This can be either a ZIP archive or a directory path containing the published ASP.NET Core application.

`iisWebSite` (optional)  
*Type:* String  
*Default:* "Default Web Site"  
The IIS website to deploy the ASP.NET Core application to. By default, applications are deployed to the "Default Web Site". Optionally, you can specify a different website name, such as one configured in the `iisConfig.websites` section.

`iisPath` (optional)  
*Type:* String  
*Default:* "/"  
Virtual directory path in IIS for the ASP.NET Core application.

`appPool` (optional)  
*Type:* String  
Application pool for the ASP.NET Core application. The pool will be configured appropriately for ASP.NET Core hosting.

### Custom deployments
<a name="dotnet-manifest-schema-custom"></a>

Custom deployments provide complete control over the deployment process through PowerShell scripts. This deployment type is useful for complex scenarios that require custom installation, configuration, or deployment logic.

**Example Custom deployment configuration**  

```
{
  "deployments": {
    "custom": [
      {
        "name": "CustomService",
        "description": "Custom Windows service deployment",
        "architecture": 32,
        "scripts": {
          "install": {
            "file": "install-service.ps1"
          },
          "restart": {
            "file": "restart-service.ps1"
          },
          "uninstall": {
            "file": "uninstall-service.ps1",
            "ignoreErrors": true
          }
        }
      }
    ]
  }
}
```Custom deployment properties

`name` (required)  
*Type:* String  
Unique name for the custom deployment.

`description` (optional)  
*Type:* String  
Description of the custom deployment.

`architecture` (optional)  
*Type:* Integer  
*Default:* 32  
*Valid values:* 32, 64  
The architecture specification for execution mode of powershell scripts

`scripts` (required)  
*Type:* Object  
PowerShell scripts that define the deployment behavior. Custom deployments support additional script types compared to other deployment types.

## Deployment scripts
<a name="dotnet-manifest-schema-scripts"></a>

Deployment scripts are PowerShell scripts that run at specific points during the deployment lifecycle. Different deployment types support different sets of script events.

### Script events
<a name="dotnet-manifest-schema-script-events"></a>

The following script events are available depending on the deployment type:Standard deployment scripts (msDeploy and aspNetCoreWeb)

`preInstall`  
Runs before the application is installed or updated.

`postInstall`  
Runs after the application is installed or updated.

`preRestart`  
Runs before the application is restarted.

`postRestart`  
Runs after the application is restarted.

`preUninstall`  
Runs before the application is uninstalled.

`postUninstall`  
Runs after the application is uninstalled.Custom deployment scripts (custom deployments only)

`install`  
Primary installation script for a custom deployment. Elastic Beanstalk runs this script during each application deployment. This script deploys the application content, configures IIS or your service, and serves the application at the health check path (`/` by default) so that the health check succeeds. For more information, see [Define custom deployments](dotnet-manifest.md#dotnet-manifest-custom).

`restart`  
Script that restarts the application or service. Elastic Beanstalk runs this script after every application deployment and after every configuration change. Because a custom deployment performs no IIS management on your behalf, this script must restart the application itself—for an IIS-hosted site by running `iisreset`, or for a self-hosted service by restarting the service. Choosing **Restart App Server** performs a platform-level `iisreset` and does not invoke your custom restart script.  
When the top-level `skipIISReset` property is set to `true`, Elastic Beanstalk skips the custom restart script on application deployments. Configuration deployments always run the custom restart script, regardless of the `skipIISReset` setting.

`uninstall`  
Script that removes a previously installed application version. Elastic Beanstalk runs this script before each new application version is installed, that is, before each application deployment. Set `ignoreErrors` to `true` so that the first deployment—when there is nothing to remove—doesn't fail.

### Script properties
<a name="dotnet-manifest-schema-script-properties"></a>

Each script is defined as an object with the following properties:

`file` (required)  
*Type:* String  
Path to the PowerShell script file relative to the manifest file. The script should have a `.ps1` extension.

`ignoreErrors` (optional)  
*Type:* Boolean  
*Default:* false  
When set to `true`, deployment continues even if the script fails. Use this for non-critical scripts or cleanup operations.

**Example Script configuration example**  

```
{
  "scripts": {
    "preInstall": {
      "file": "backup-config.ps1",
      "ignoreErrors": true
    },
    "postInstall": {
      "file": "configure-app.ps1"
    }
  }
}
```