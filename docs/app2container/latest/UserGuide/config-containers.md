AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Configuring application containers

When you run the **[analyze](cmd-analyze.md "cmd-analyze.md")** command, an
`analysis.json` file is created for the application that is
specified in the `--application-id` parameter. The
**containerize** command uses this file to build the application
container image and to generate artifacts.

You can configure the fields in the `containerParameters` section
before running the **containerize** command to customize your
application container. For configurable key/value pairs that do not apply to
your container, set string values to an empty string, numeric values to zero,
and Boolean values to false.

For applications running on Linux, the application `analysis.json`
file includes the following content:

###### Read-only data

- Control fields – Fields having to do with
  file creation, such as template version, and the file creation timestamp.
- analysisInfo – System
  dependencies for the application.

###### Configurable data

The `containerParameters` section contains the following fields:

- imageRepository (string, required) – The name of the
  repository where the application container image is stored.
- imageTag (string, required) – A
  tag for the build version of the application container image.
- containerBaseImage (string)
  – The base operating system (OS) image for the container build.
  By default, App2Container uses the operating system from the application server
  or worker machine where containerization runs.

###### Note

If specified, this must be an image name from your registry in the
format <image name>[:<tag>], and it must match
the operating system platform and version that runs on the
application server or worker machine where containerization runs.
The tag is optional if the repository supports "latest".

- appExcludedFiles (array of strings)
  – Specific files and directories to exclude from the container
  build.
- appSpecificFiles (array of strings)
  – Specific files and directories to include in the container
  build.
- applicationPort (number)
  – The application port exposed inside of the container. This port
  is tested for a successful HTTP response during pre-validation when the
  **containerize** command runs. App2Container assigns this as the
  default exposed port when creating a load balancer during deployment.
- applicationMode (Boolean, required)
  – The approach that App2Container uses to determine which files to
  include in your container image. App2Container uses application mode
  (value=true) for supported application frameworks, and process mode
  (value=false) for all other configurations.

You can override this value if necessary. For example, if your
application is running on a supported framework, but App2Container did not
recognize it and therefore assigned process mode, you can override the
setting to use application mode instead.

###### Application mode settings

    + *`true`* (application mode):
     For supported application frameworks, App2Container targets only the
     application files and dependencies that are needed for containerization, thereby minimizing
     the size of the resulting container image. This is known as *application mode*. Supported application frameworks include:
     Tomcat, TomEE, and JBoss (standalone mode).
    + *`false`* (process mode): If App2Container does not find a supported framework running on your application
     server, or if you have other dependent processes running on your server, App2Container takes a conservative
     approach to identifying dependencies. This is known as *process mode*. For process
     mode, all non-system files on the application server are included in the container image.

###### Tip

If your application container image includes unnecessary files, or is missing files that
should be included, use the following parameters to make corrections:

    + To specify files to exclude from your application container image, use
     the `appExcludedFiles` parameter.
    + To add files that were missed, use the `appSpecificFiles`
     parameter.

- logLocations (array of strings)
  – Specific log files or log directories to be routed to
  `stdout`. This enables applications that write to log
  files on the host to be integrated with AWS services such as CloudWatch and
  Firehose.
- enableDynamicLogging (Boolean,
  required) – Maps application logs to `stdout` as they
  are created. _If set to true, requires log directories to be
  entered in `logLocations`._
- dependencies (array of strings)
  – A listing of all dependent processes or applications found for
  the application ID by the **analyze** command. You can
  remove specific dependencies to exclude them from the container.

###### Examples

The following examples show an `analysis.json` file for an
application running on Linux. Choose the tab that matches your application.

Java
This example shows an `analysis.json` file for a
Java application running on Linux.

```
{
	"a2CTemplateVersion": "",
       "createdTime": "",
       "containerParameters": {
              "_comment1": "*** EDITABLE: The below section can be edited according to the application requirements. Please see the analysisInfo section below for details discovered regarding the application. ***",
              "imageRepository": "java-tomcat-6e6f3a87",
              "imageTag": "latest",
              "containerBaseImage": "ubuntu:18.04",
              "appExcludedFiles": [],
              "appSpecificFiles": [],
              "applicationPort": 5000,
              "applicationMode": true,
              "logLocations": [],
              "enableDynamicLogging": false,
              "dependencies": []
       },
       "analysisInfo": {
              "_comment2": "*** NON-EDITABLE: Analysis Results ***",
              "processId": 2065,
              "appId": "java-tomcat-6e6f3a87",
              "userId": "1000",
              "groupId": "1000",
              "cmdline": [
                     "/usr/bin/java",
                     "... list of commands",
                     "start"
              ],
              "osData": {
                     "BUG_REPORT_URL": "",
                     "HOME_URL": "",
                     "ID": "ubuntu",
                     "ID_LIKE": "debian",
                     "NAME": "Ubuntu",
                     "PRETTY_NAME": "Ubuntu 18.04.2 LTS",
                     "PRIVACY_POLICY_URL": "",
                     "SUPPORT_URL": "",
                     "UBUNTU_CODENAME": "",
                     "VERSION": "",
                     "VERSION_CODENAME": "",
                     "VERSION_ID": "18.04"
              },
              "osName": "ubuntu",
              "ports": [
                     {
                            "localPort": 8080,
                            "protocol": "tcp6"
                     },
                     {
                            "localPort": 8009,
                            "protocol": "tcp6"
                     },
                     {
                            "localPort": 8005,
                            "protocol": "tcp6"
                     }
              ],
              "Properties": {
                     "catalina.base": "<application directory>",
                     "catalina.home": "<application directory>",
                     "classpath": "<application directory>/bin/bootstrap.jar:... etc.",
                     "ignore.endorsed.dirs": "",
                     "java.io.tmpdir": "<application directory>/temp",
                     "java.protocol.handler.pkgs": "org.apache.catalina.webresources",
                     "java.util.logging.config.file": "<application directory>/conf/logging.properties",
                     "java.util.logging.manager": "org.apache.juli.ClassLoaderLogManager",
                     "jdk.tls.ephemeralDHKeySize": "2048",
                     "jdkVersion": "11.0.7",
                     "org.apache.catalina.security.SecurityListener.UMASK": ""
              },
              "AdvancedAppInfo": {
                     "Directories": {
                            "base": "<application directory>",
                            "bin": "<application directory>/bin",
                            "conf": "<application directory>/conf",
                            "home": "<application directory>",
                            "lib": "<application directory>/lib",
                            "logConfig": "<application directory>/conf/logging.properties",
                            "logs": "<application directory>/logs",
                            "tempDir": "<application directory>/temp",
                            "webapps": "<application directory>/webapps",
                            "work": "<application directory>/work"
                     },
                     "distro": "java-tomee",
                     "flavor": "plume",
                     "jdkVersion": "11.0.7",
                     "version": "8.0.0"
              },
              "env": {
                     "HOME": "... Java Home directory",
                     "JDK_JAVA_OPTIONS": "",
                     "LANG": "C.UTF-8",
                     "LC_TERMINAL": "iTerm2",
                     "LC_TERMINAL_VERSION": "3.3.11",
                     "LESSCLOSE": "/usr/bin/lesspipe %s %s",
                     "LESSOPEN": "| /usr/bin/lesspipe %s",
                     "LOGNAME": "ubuntu",
                     "LS_COLORS": "",
                     "MAIL": "",
                     "OLDPWD": "",
                     "PATH": "... server PATH",
                     "PWD": "",
                     "SHELL": "/bin/bash",
                     "SHLVL": "1",
                     "SSH_CLIENT": "",
                     "SSH_CONNECTION": "",
                     "SSH_TTY": "",
                     "TERM": "",
                     "USER": "ubuntu",
                     "XDG_DATA_DIRS": "",
                     "XDG_RUNTIME_DIR": "",
                     "XDG_SESSION_ID": "1",
                     "_": "bin/startup.sh"
              },
              "cwd": "",
              "procUID": {
                     "euid": "1000",
                     "suid": "1000",
                     "fsuid": "1000",
                     "ruid": "1000"
              },
              "procGID": {
                     "egid": "1000",
                     "sgid": "1000",
                     "fsgid": "1000",
                     "rgid": "1000"
              },
              "userNames": {
                     "1000": "ubuntu"
              },
              "groupNames": {
                     "1000": "ubuntu"
              },
              "fileDescriptors": [
                     "<application directory>/logs/... log files",
                     "<application directory>/lib/... jar files",
                     "... etc.",
                     "/usr/lib/jvm/.../lib/modules"
              ],
              "dependencies": {}
          }
}
```

ASP.NET generic
This example shows an `analysis.json` file for an
ASP.NET generic application running on Linux.

```
{
	"a2CTemplateVersion": "1.0",
       "createdTime": "2021-11-24 18:49:1224",
       "containerParameters": {
              "_comment1": "*** EDITABLE: The below section can be edited according to the application requirements. Please see the analysisInfo section below for details discovered regarding the application. ***",
              "imageRepository": "dotnet-generic-a27b2829",
              "imageTag": "latest",
              "containerBaseImage": "mcr.microsoft.com/dotnet/sdk:5.0",
              "appExcludedFiles": [
              	"/root/.aws"
              ],
              "appSpecificFiles": [],
              "applicationPort": 5000,
              "applicationMode": true,
              "logLocations": [],
              "enableDynamicLogging": false,
              "dependencies": []
       },
       "analysisInfo": {
              "_comment2": "*** NON-EDITABLE: Analysis Results ***",
              "processId": 1,
              "appId": "dotnet-generic-a27b2829",
              "userId": "0",
              "groupId": "0",
              "cmdline": [
                     "/usr/bin/dotnet",
				     "/root/nopCommerce440/Nop.Web.dll"
              ],
              "webApp": "",
              "osData": {
                     "BUG_REPORT_URL": "https://bugs.launchpad.net/ubuntu/",
                     "HOME_URL": "https://www.ubuntu.com/",
                     "ID": "ubuntu",
                     "ID_LIKE": "debian",
                     "NAME": "Ubuntu",
                     "PRETTY_NAME": "Ubuntu 20.04.3 LTS",
                     "PRIVACY_POLICY_URL": "https://www.ubuntu.com/legal/terms-and-policies/privacy-policy",
                     "SUPPORT_URL": "https://help.ubuntu.com/",
                     "UBUNTU_CODENAME": "focal",
                     "VERSION": "20.04.3 LTS (Focal Fossa)",
                     "VERSION_CODENAME": "focal",
                     "VERSION_ID": "20.04"
              },
              "osName": "ubuntu",
              "ports": [
                     {
                            "localPort": 5000,
                            "protocol": "tcp"
                     }
              ],
              "Properties": null,
              "applicationType": "dotnet-generic",
              "AdvancedAppInfo": {
                     "Directories": {
                            "dotnetApp": "/root/nopCommerce440"
                     },
                     "dotnetVersion": "5.0"
              },
              "env": {
                     "HOME": "/root",
                     "HOSTNAME": "678f90a12bc3",
				     "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
				     "TERM": "xterm",
				     "TZ": "Etc/UTC"
              },
              "cwd": "",
              "exe": "/usr/share/dotnet/dotnet",
              "procUID": {
                     "euid": "0",
                     "suid": "0",
                     "fsuid": "0",
                     "ruid": "0"
              },
              "procGID": {
                     "egid": "0",
                     "sgid": "0",
                     "fsgid": "0",
                     "rgid": "0"
              },
              "userNames": {
                     "0": "root"
              },
              "groupNames": {
                     "0": "root"
              },
              "fileDescriptors": [
                     "/dev/pts/0",
				     "/root/nopCommerce440/AdvancedStringBuilder.dll",
 				    "/root/nopCommerce440/AutoMapper.dll",
                     "... etc.",
                     "/root/nopCommerce440/netstandard.dll"
              ],
              "dependencies": {}
          }
}
```

ASP.NET single file
This example shows an `analysis.json` file for an
ASP.NET single file application running on Linux.

```
{
	"a2CTemplateVersion": "1.0",
       "createdTime": "2021-11-29 07:08:2929",
       "containerParameters": {
              "_comment1": "*** EDITABLE: The below section can be edited according to the application requirements. Please see the analysisInfo section below for details discovered regarding the application. ***",
              "imageRepository": "dotnet-single-c2930d3132",
              "imageTag": "latest",
              "containerBaseImage": "mcr.microsoft.com/dotnet/sdk:latest",
              "appExcludedFiles": [
              	"/root/.aws"
              ],
              "appSpecificFiles": [],
              "applicationPort": 5000,
              "applicationMode": true,
              "logLocations": [],
              "enableDynamicLogging": false,
              "dependencies": []
       },
       "analysisInfo": {
              "_comment2": "*** NON-EDITABLE: Analysis Results ***",
              "processId": 1,
              "appId": "dotnet-single-c2930d3132",
              "userId": "0",
              "groupId": "0",
              "cmdline": [
                     "./MyCoreWebApp.5"
              ],
              "webApp": "",
              "osData": {
                     "BUG_REPORT_URL": "https://bugs.launchpad.net/ubuntu/",
                     "HOME_URL": "https://www.ubuntu.com/",
                     "ID": "ubuntu",
                     "ID_LIKE": "debian",
                     "NAME": "Ubuntu",
                     "PRETTY_NAME": "Ubuntu 20.04.3 LTS",
                     "PRIVACY_POLICY_URL": "https://www.ubuntu.com/legal/terms-and-policies/privacy-policy",
                     "SUPPORT_URL": "https://help.ubuntu.com/",
                     "UBUNTU_CODENAME": "focal",
                     "VERSION": "20.04.3 LTS (Focal Fossa)",
                     "VERSION_CODENAME": "focal",
                     "VERSION_ID": "20.04"
              },
              "osName": "ubuntu",
              "ports": [
                     {
                            "localPort": 5000,
                            "protocol": "tcp"
                     }
              ],
              "Properties": null,
              "applicationType": "dotnet-single",
              "AdvancedAppInfo": {
                     "Directories": {
                            "dotnetApp": "/root/mycorewebapp"
                     },
                     "dotnetVersion": "latest"
              },
              "env": {
                     "HOME": "/root",
                     "HOSTNAME": "a1bc23d4567e",
				     "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
				     "TERM": "xterm",
				     "TZ": "Etc/UTC"
              },
              "cwd": "/root/mycorewebapp",
              "exe": "/root/mycorewebapp/MyCoreWebApp.5",
              "procUID": {
                     "euid": "0",
                     "suid": "0",
                     "fsuid": "0",
                     "ruid": "0"
              },
              "procGID": {
                     "egid": "0",
                     "sgid": "0",
                     "fsgid": "0",
                     "rgid": "0"
              },
              "userNames": {
                     "0": "root"
              },
              "groupNames": {
                     "0": "root"
              },
              "fileDescriptors": [
                     "/dev/pts/0",
     				"/root/mycorewebapp/MyCoreWebApp.5"
              ],
              "dependencies": {}
          }
}
```

For applications running on Windows, the application `analysis.json`
file includes the following content:

###### Read-only data

- Control fields – Fields having to do with file creation,
  such as template version, and the file creation timestamp.
- analysisInfo – System
  dependencies for the application.

###### Configurable data

The `containerParameters` section contains the following fields:

- containerBaseImage (string)
  – The base operating system (OS) image for the container build.
  By default, App2Container uses the operating system from the application server
  or worker machine where containerization runs.

###### Note

If specified, this must be an image name from your registry in the
format <image name>[:<tag>], and it must match
the operating system platform and version that runs on the
application server or worker machine where containerization runs.
The tag is optional if the repository supports "latest".

- enableServerConfigurationUpdates
  (Boolean, required) – Provides an option in the Dockerfile to
  restore the application configuration of the source server.
- imageRepositoryName (string, required) – The name
  of the repository where the application container image is stored.
- imageTag (string, required) – A
  tag for the build version of the application container image.
- additionalExposedPorts (array of
  numbers) – Additional port numbers that should be exposed inside
  of the application container.
- appIncludedFiles (array of strings)
  – Specific files and directories to include in the container
  build.
- appExcludedFiles (array of strings)
  – Specific files and directories to exclude from the container
  build.
- enableLogging (Boolean, required)
  – Enables dynamic logging, redirecting application logs to
  container `stdout`.
- includedWebApps (array of strings)
  – The application IDs for web applications running under the IIS
  site that should be included in the container image.
  _Applications must have been running in IIS during
  inventory and analysis._
- additionalApps (array of strings)
  – For the `analysis.json` file that describes
  the root application in a complex Windows .NET application, these
  are the additional application or service components to include in
  the application container. You can include up to five additional
  application components in the array.

###### Examples

The following examples show an `analysis.json` file for a
.NET application running on Windows. Your `analysis.json` file
configuration can vary by the type of .NET application you are migrating, its
dependencies, and whether you want it to run in a single container or in multiple
containers. Choose the tab that matches your .NET configuration.

Simple
The following example shows an `analysis.json` file for a
simple .NET application running on Windows.

```
{
  "a2CTemplateVersion": "3.1",
  "createdTime": "",
  "containerParameters": {
    "_comment": "*** EDITABLE: The below section can be edited according to the application requirements. Please see the Analysis Results section further below for details discovered regarding the application. ***",
    "containerBaseImage": "mcr.microsoft.com/dotnet/framework/aspnet:4.7.2-windowsservercore-ltsc2019",
    "enableServerConfigurationUpdates": true,
    "imageRepositoryName": "iis-smarts-51d2dbf8",
    "imageTag": "latest",
    "additionalExposedPorts": [
    ],
    "appIncludedFiles": [

    ],
    "appExcludedFiles": [
    ],
    "enableLogging": false,
    "additionalApps": [
    ]
  },
  "analysisInfo": {
    "_comment": "*** NON-EDITABLE: Analysis Results ***",
    "hostInfo": {
      "os": "...",
      "osVersion": "...",
      "osWindowsDirectory": "...",
      "arch": "..."
    },
    "appId": "iis-smarts-51d2dbf8",
    "appServerIp": "localhost",
    "appType": "IIS",
    "appName": "smarts",
    "ports": [
      {
        "localPort": 90,
        "protocol": "http"
      }
    ],
    "features": [
      "File-Services",
      "FS-FileServer",
      "Web-Http-Tracing",
      "Web-Basic-Auth",
      "Web-Digest-Auth",
      "Web-Url-Auth",
      "Web-Windows-Auth",
      "Web-ASP",
      "Web-CGI",
      "Web-Mgmt-Tools",
      "Web-Mgmt-Console",
      "Web-Scripting-Tools",
      "FS-SMB1",
      "User-Interfaces-Infra",
      "Server-Gui-Mgmt-Infra",
      "Server-Gui-Shell",
      "PowerShell-ISE"
    ],
    "appPoolName": "smarts",
    "poolIdentityType": "ApplicationPoolIdentity",
    "dotnetVersion": "v4.0",
    "iisVersion": "IIS 10.0",
    "sitePhysicalPath": "<IIS web root directory>\\smarts",
    "discoveredWebApps": [
    ],
    "reportPath": "<application output directory>\\iis-smarts-51d2dbf8\\report.txt",
    "isSiteUsingWindowsAuth": false,
    "serverBackupFile": "<application directory>\\Web Deploy Backups\\... backup zip file"
  }
}
```

Complex – one container
In this scenario, each application or service has its own
`analysis.json` file, but the root application
references the application ID for the service in the
`additionalApps` array. This results in a single container
that includes both the root application and the service when you run the
**containerize** command.

- ###### Root application

The following example shows the `analysis.json`
file for the root application.

```
 {
  "a2CTemplateVersion": "1.0",
  "createdTime": "2021-06-25-05:18:24",
  "containerParameters": {
    "_comment": "*** EDITABLE: The below section can be edited according to the application requirements. Please see the Analysis Results section further below for details discovered regarding the application. ***",
    "containerBaseImage": "",
    "enableServerConfigurationUpdates": true,
    "imageRepositoryName": "iis-colormvciis-b69c09ab",
    "imageTag": "latest",
    "additionalExposedPorts": [
    ],
    "appIncludedFiles": [
    ],
    "appExcludedFiles": [
    ],
    "enableLogging": false,
    "includedWebApps": [
    ],
    "additionalApps": [
     	"service-colorwindowsservice-69f90194"
    ]
  },
  "analysisInfo": {
    "_comment": "*** NON-EDITABLE: Analysis Results ***",
    "hostInfo": {
      "os": "Microsoft Windows Server 2019 Datacenter",
      "osVersion": "10.0.17763",
      "osWindowsDirectory": "C:\\Windows",
      "arch": "64-bit"
    },
    "appId": "iis-colormvciis-b69c09ab",
    "appServerIp": "localhost",
    "appType": "IIS",
    "appName": "colorMvcIIs",
    "ports": [
      {
        "localPort": 82,
        "protocol": "http"
      }
    ],
    "features": [
      "Web-Http-Redirect",
      "Web-Custom-Logging",
      "... etc."
    ],
    "appPoolName": "colorMVC",
    "poolIdentityType": "ApplicationPoolIdentity",
    "dotNetVersion": "v4.0",
    "iisVersion": "IIS 10.0",
    "sitePhysicalPath": "C:\\colorMvcIis",
    "discoveredWebApps": [
     ],
    "siteUsesWindowsAuth": false,
    "serverBackupFile": "<application directory>\\Web Deploy Backups\\... backup zip file",
    "reportPath": "<application output directory>\\iis-colormvciis-b69c09ab\\report.txt"
  }
}
```

- ###### Windows service

The following example shows the `analysis.json`
file for the Windows service that is included in the application container.

```
{
  "a2CTemplateVersion": "1.0",
  "createdTime": "2021-07-09-04:16:58",
  "containerParameters": {
    "_comment": "*** EDITABLE: The below section can be edited according to the application requirements. Please see the Analysis Results section further below for details discovered regarding the application. ***",
    "containerBaseImage": "",
    "enableServerConfigurationUpdates": true,
    "imageRepositoryName": "service-colorwindowsservice-69f90194",
    "imageTag": "latest",
    "additionalExposedPorts": [
    ],
    "appIncludedFiles": [
    ],
    "appExcludedFiles": [
    ],
    "enableLogging": false,
    "additionalApps": [
    ]
  },
  "analysisInfo": {
    "_comment": "*** NON-EDITABLE: Analysis Results ***",
    "hostInfo": {
      "os": "Microsoft Windows Server 2019 Datacenter",
      "osVersion": "10.0.17763",
      "osWindowsDirectory": "C:\\Windows",
      "arch": "64-bit"
    },
    "appId": "service-colorwindowsservice-69f90194",
    "appServerIp": "localhost",
    "appType": "service",
    "appName": "colorwindowsservice",
    "ports": [
      {
        "localPort": 33335,
        "protocol": "TCP"
      }
    ],
    "features": [
      "Web-Http-Redirect",
      "Web-Custom-Logging",
      "... etc."
    ],
    "serviceName": "colorwindowsservice",
    "serviceBinary": "ColorWindowsService.exe",
    "serviceDir": "C:\\COLORCODE\\colorservice-master\\ColorWindowsService\\bin\\Release\\",
    "cmdline": [
          "C:\\COLORCODE\\colorservice-master\\ColorWindowsService\\bin\\Release\\ColorWindowsService.exe"
    ]
  }
}
```

Complex – multiple containers
In this scenario, each application or service has its own
`analysis.json` file, and the
`additionalApps` array is empty. To create two containers,
run the **containerize** command twice – once for the
root application and once for the service. For container orchestration,
specify the service as a dependent application when you configure the
`deployment.json` file for the root application.

- ###### Root application

The following example shows the `analysis.json`
file for the root application.

```
 {
  "a2CTemplateVersion": "1.0",
  "createdTime": "2021-06-25-05:18:24",
  "containerParameters": {
    "_comment": "*** EDITABLE: The below section can be edited according to the application requirements. Please see the Analysis Results section further below for details discovered regarding the application. ***",
    "containerBaseImage": "",
    "enableServerConfigurationUpdates": true,
    "imageRepositoryName": "iis-colormvciis-b69c09ab",
    "imageTag": "latest",
    "additionalExposedPorts": [
    ],
    "appIncludedFiles": [
    ],
    "appExcludedFiles": [
    ],
    "enableLogging": false,
    "includedWebApps": [
    ],
    "additionalApps": [
    ]
  },
  "analysisInfo": {
    "_comment": "*** NON-EDITABLE: Analysis Results ***",
    "hostInfo": {
      "os": "Microsoft Windows Server 2019 Datacenter",
      "osVersion": "10.0.17763",
      "osWindowsDirectory": "C:\\Windows",
      "arch": "64-bit"
    },
    "appId": "iis-colormvciis-b69c09ab",
    "appServerIp": "localhost",
    "appType": "IIS",
    "appName": "colorMvcIIs",
    "ports": [
      {
        "localPort": 82,
        "protocol": "http"
      }
    ],
    "features": [
      "Web-Http-Redirect",
      "Web-Custom-Logging",
      "... etc."
    ],
    "appPoolName": "colorMVC",
    "poolIdentityType": "ApplicationPoolIdentity",
    "dotNetVersion": "v4.0",
    "iisVersion": "IIS 10.0",
    "sitePhysicalPath": "C:\\colorMvcIis",
    "discoveredWebApps": [
     ],
    "siteUsesWindowsAuth": false,
    "serverBackupFile": "<application directory>\\Web Deploy Backups\\... backup zip file",
    "reportPath": "<application output directory>\\iis-colormvciis-b69c09ab\\report.txt"
  }
}
```

- ###### Windows service

The following example shows the `analysis.json`
file for the Windows service that runs in a separate container.

```
{
  "a2CTemplateVersion": "1.0",
  "createdTime": "2021-07-09-04:16:58",
  "containerParameters": {
    "_comment": "*** EDITABLE: The below section can be edited according to the application requirements. Please see the Analysis Results section further below for details discovered regarding the application. ***",
    "containerBaseImage": "",
    "enableServerConfigurationUpdates": true,
    "imageRepositoryName": "service-colorwindowsservice-69f90194",
    "imageTag": "latest",
    "additionalExposedPorts": [
    ],
    "appIncludedFiles": [
    ],
    "appExcludedFiles": [
    ],
    "enableLogging": false,
    "additionalApps": [
    ]
  },
  "analysisInfo": {
    "_comment": "*** NON-EDITABLE: Analysis Results ***",
    "hostInfo": {
      "os": "Microsoft Windows Server 2019 Datacenter",
      "osVersion": "10.0.17763",
      "osWindowsDirectory": "C:\\Windows",
      "arch": "64-bit"
    },
    "appId": "service-colorwindowsservice-69f90194",
    "appServerIp": "localhost",
    "appType": "service",
    "appName": "colorwindowsservice",
    "ports": [
      {
        "localPort": 33335,
        "protocol": "TCP"
      }
    ],
    "features": [
      "Web-Http-Redirect",
      "Web-Custom-Logging",
      "... etc."
    ],
    "serviceName": "colorwindowsservice",
    "serviceBinary": "ColorWindowsService.exe",
    "serviceDir": "C:\\COLORCODE\\colorservice-master\\ColorWindowsService\\bin\\Release\\",
    "cmdline": [
          "C:\\COLORCODE\\colorservice-master\\ColorWindowsService\\bin\\Release\\ColorWindowsService.exe"
    ]
  }
}
```

###### Note

For complex Windows .NET applications, you can also use a hybrid approach, with some
components running together in a single container and other components running in separate
containers.
