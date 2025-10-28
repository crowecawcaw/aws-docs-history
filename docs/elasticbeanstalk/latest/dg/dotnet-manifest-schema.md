# Deployment manifest schema reference

The deployment manifest is a JSON file that defines how Elastic Beanstalk should deploy and configure your Windows applications. This section provides a comprehensive reference for all supported properties and configuration options in the manifest schema.

## Manifest structure

The deployment manifest follows a specific JSON schema with the following top-level structure:

###### Example Basic manifest structure

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

`manifestVersion` (required)

_Type:_ Number

_Default:_ 1

_Valid values:_ 1

Specifies the version of the manifest schema. Currently, only version 1 is supported.

`skipIISReset` (optional)

_Type:_ Boolean

_Default:_ false

Controls whether IIS is reset during application deployments. This flag affects both `msDeploy` and `aspNetCoreWeb` deployment types.

_Behavior:_

- _Not specified or `false` (default):_ IIS resets are performed during install, uninstall, and update operations. This is the traditional behavior.
- _`true`:_ IIS resets are skipped during deployment operations.

_Benefits:_

- _Reduced downtime_ – Applications experience shorter service interruptions during deployments.
- _Faster deployments_ – Eliminates the time required for IIS to fully restart and reinitialize.

###### Note

When using `skipIISReset`, the [RestartAppServer](../api/API_RestartAppServer.md "../api/API_RestartAppServer.md") operation performs an IIS reset regardless of this flag setting.

_Example:_

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

_Type:_ Object

Contains the deployment configurations for your applications. This object can include `msDeploy`, `aspNetCoreWeb`, and `custom` deployment types.

`iisConfig` (optional)

_Type:_ Object

Defines IIS configuration settings to apply before deploying applications. Supports both website and application pool configuration.

## IIS configuration

The `iisConfig` section allows you to configure IIS settings before deploying your applications. This includes setting up application pools with specific configurations and configuring IIS websites with custom bindings.

### IIS websites

IIS websites allow you to configure custom website settings including physical paths and network bindings before deploying your applications.

###### Important considerations for creating different IIS websites

- _Website setup order:_ Websites are configured sequentially in the order they appear in the `websites` array. The platform processes each website configuration in sequence, so ensure proper ordering if you have dependencies between websites.
- _Firewall and port access:_ Only port 80 is automatically exposed through the default Elastic Beanstalk Windows firewall configuration. If you configure websites to use non-standard ports, you must define custom firewall rules through ebextensions or custom deployment scripts to allow external access to these ports.

###### Example Website configuration

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
```

###### Website properties

`name` (required)

_Type:_ String

The name of the IIS website. This name is used to identify the website in IIS Manager and must be unique within the IIS configuration.

`physicalPath` (required)

_Type:_ String

The physical path on the server where the website files are stored. This path must be accessible to the IIS worker process.

`bindings` (required)

_Type:_ Array

_Minimum items:_ 1

An array of binding configurations that define how the website responds to network requests. Each binding specifies a protocol, port, and optional host name.

#### Website bindings

Website bindings define the network endpoints where your IIS website will listen for incoming requests.

`protocol` (required)

_Type:_ String

_Valid values:_ "http", "https"

The protocol used for the binding.

`port` (required)

_Type:_ Integer

_Valid range:_ 1-65535

The port number on which the website will listen for requests.

`hostName` (optional)

_Type:_ String

The host name (domain name) for the binding.

### Application pools

Application pools provide isolation between applications and allow you to configure runtime settings for groups of applications.

###### Example Application pool configuration

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
```

###### Application pool properties

`name` (required)

_Type:_ String

The name of the application pool. This name is used to reference the pool in deployment configurations.

`enable32Bit` (optional)

_Type:_ Boolean

Enables a 32-bit application to run on a 64-bit version of Windows. Set to `true` for legacy applications that require 32-bit compatibility.

`managedPipelineMode` (optional)

_Type:_ String

_Valid values:_ "Integrated", "Classic"

Specifies the request-processing mode for the application pool.

`managedRuntimeVersion` (optional)

_Type:_ String

_Valid values:_ "No Managed Code", "v2.0", "v4.0"

Specifies the .NET Framework version for the application pool.

`queueLength` (optional)

_Type:_ Integer

Maximum number of requests that HTTP.sys queues for the application pool before rejecting additional requests.

#### CPU configuration

The `cpu` object configures CPU usage limits and monitoring for the application pool.

`limitPercentage` (optional)

_Type:_ Number

Maximum percentage of CPU time that worker processes in the application pool can consume.

`limitAction` (optional)

_Type:_ String

_Valid values:_ "NoAction", "KillW3wp", "Throttle", "ThrottleUnderLoad"

Action to take when the CPU limit is reached.

`limitMonitoringInterval` (optional)

_Type:_ Number

Reset period (in minutes) for CPU monitoring and throttling limits.

#### Recycling configuration

The `recycling` object configures when and how application pool worker processes are recycled.

`regularTimeInterval` (optional)

_Type:_ Integer

Time interval (in minutes) after which the application pool recycles. Set to 0 to disable time-based recycling.

`requestLimit` (optional)

_Type:_ Integer

Maximum number of requests the application pool processes before recycling.

`memory` (optional)

_Type:_ Integer

Amount of virtual memory (in kilobytes) that triggers worker process recycling.

`privateMemory` (optional)

_Type:_ Integer

Amount of private memory (in kilobytes) that triggers worker process recycling.

## Deployment types

The `deployments` object contains arrays of deployment configurations for different application types. Each deployment type has specific properties and use cases.

### MSDeploy deployments

MSDeploy deployments are used for traditional .NET Framework applications that can be deployed using Web Deploy (MSDeploy).

###### Example MSDeploy deployment configuration

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
```

###### MSDeploy deployment properties

`name` (required)

_Type:_ String

Unique name for the deployment. This name must be unique across all deployments in the manifest.

`description` (optional)

_Type:_ String

Human-readable description of the deployment.

`parameters` (required)

_Type:_ Object

Configuration parameters for the MSDeploy operation.

`scripts` (optional)

_Type:_ Object

PowerShell scripts to run at various stages of the deployment lifecycle.

#### MSDeploy parameters

`appBundle` (required)

_Type:_ String

Path to the application bundle (ZIP file) relative to the manifest file. This bundle contains the application files to deploy.

`iisWebSite` (optional)

_Type:_ String

_Default:_ "Default Web Site"

The IIS website to deploy the application to. By default, applications are deployed to the "Default Web Site". Optionally, you can specify a different website name, such as one configured in the `iisConfig.websites` section.

`iisPath` (optional)

_Type:_ String

_Default:_ "/"

Virtual directory path in IIS where the application will be deployed. Use "/" for the root path or "/api" for a subdirectory.

`appPool` (optional)

_Type:_ String

Name of the application pool to run this application.

### ASP.NET Core deployments

ASP.NET Core deployments are specifically designed for .NET Core and .NET 5+ applications.

###### Example ASP.NET Core deployment configuration

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

ASP.NET Core deployments use the same property structure as MSDeploy deployments, with the key difference being the runtime environment and hosting model used for the application.

###### ASP.NET Core deployment parameters

`appBundle` (required)

_Type:_ String

Path to the application bundle relative to the manifest file. This can be either a ZIP archive or a directory path containing the published ASP.NET Core application.

`iisWebSite` (optional)

_Type:_ String

_Default:_ "Default Web Site"

The IIS website to deploy the ASP.NET Core application to. By default, applications are deployed to the "Default Web Site". Optionally, you can specify a different website name, such as one configured in the `iisConfig.websites` section.

`iisPath` (optional)

_Type:_ String

_Default:_ "/"

Virtual directory path in IIS for the ASP.NET Core application.

`appPool` (optional)

_Type:_ String

Application pool for the ASP.NET Core application. The pool will be configured appropriately for ASP.NET Core hosting.

### Custom deployments

Custom deployments provide complete control over the deployment process through PowerShell scripts. This deployment type is useful for complex scenarios that require custom installation, configuration, or deployment logic.

###### Example Custom deployment configuration

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
```

###### Custom deployment properties

`name` (required)

_Type:_ String

Unique name for the custom deployment.

`description` (optional)

_Type:_ String

Description of the custom deployment.

`architecture` (optional)

_Type:_ Integer

_Default:_ 32

_Valid values:_ 32, 64

The architecture specification for execution mode of powershell scripts

`scripts` (required)

_Type:_ Object

PowerShell scripts that define the deployment behavior. Custom deployments support additional script types compared to other deployment types.

## Deployment scripts

Deployment scripts are PowerShell scripts that run at specific points during the deployment lifecycle. Different deployment types support different sets of script events.

### Script events

The following script events are available depending on the deployment type:

###### Standard deployment scripts (msDeploy and aspNetCoreWeb)

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

Runs after the application is uninstalled.

###### Custom deployment scripts (custom deployments only)

`install`

Primary installation script for custom deployments. This script is responsible for installing the application or service.

`restart`

Script to restart the application or service. Called when the environment is restarted.

`uninstall`

Script to uninstall the application or service. Called during environment termination or application removal.

### Script properties

Each script is defined as an object with the following properties:

`file` (required)

_Type:_ String

Path to the PowerShell script file relative to the manifest file. The script should have a `.ps1` extension.

`ignoreErrors` (optional)

_Type:_ Boolean

_Default:_ false

When set to `true`, deployment continues even if the script fails. Use this for non-critical scripts or cleanup operations.

###### Example Script configuration example

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
