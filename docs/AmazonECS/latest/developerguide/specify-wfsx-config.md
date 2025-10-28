# Specify an FSx for Windows File Server file system in an Amazon ECS task

definition

To use FSx for Windows File Server file system volumes for your containers, specify the volume and
mount point configurations in your task definition. The following task definition JSON
snippet shows the syntax for the `volumes` and `mountPoints`
objects for a container.

```
{
    "containerDefinitions": [
        {
            "entryPoint": [
                "powershell",
                "-Command"
            ],
            "portMappings": [],
            "command": ["New-Item -Path C:\\fsx-windows-dir\\index.html -ItemType file -Value '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>It Works!</h2> <p>You are using Amazon FSx for Windows File Server file system for persistent container storage.</p>' -Force"],
            "cpu": 512,
            "memory": 256,
            "image": "mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019",
            "essential": false,
            "name": "container1",
            "mountPoints": [
                {
                    "sourceVolume": "fsx-windows-dir",
                    "containerPath": "C:\\fsx-windows-dir",
                    "readOnly": false
                }
            ]
        },
        {
            "entryPoint": [
                "powershell",
                "-Command"
            ],
            "portMappings": [
                {
                    "hostPort": 443,
                    "protocol": "tcp",
                    "containerPort": 80
                }
            ],
            "command": ["Remove-Item -Recurse C:\\inetpub\\wwwroot\\* -Force; Start-Sleep -Seconds 120; Move-Item -Path C:\\fsx-windows-dir\\index.html -Destination C:\\inetpub\\wwwroot\\index.html -Force; C:\\ServiceMonitor.exe w3svc"],
            "mountPoints": [
                {
                    "sourceVolume": "fsx-windows-dir",
                    "containerPath": "C:\\fsx-windows-dir",
                    "readOnly": false
                }
            ],
            "cpu": 512,
            "memory": 256,
            "image": "mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019",
            "essential": true,
            "name": "container2"
        }
    ],
    "family": "fsx-windows",
    "executionRoleArn": "arn:aws:iam::111122223333:role/ecsTaskExecutionRole",
    "volumes": [
        {
            "name": "fsx-windows-dir",
            "fsxWindowsFileServerVolumeConfiguration": {
                "fileSystemId": "fs-0eeb5730b2EXAMPLE",
                "authorizationConfig": {
                    "domain": "example.com",
                    "credentialsParameter": "arn:arn-1234"
                },
                "rootDirectory": "share"
            }
        }
    ]
}
```

`FSxWindowsFileServerVolumeConfiguration`

Type: Object

Required: No

This parameter is specified when you're using [FSx for Windows File Server](../../../fsx/latest/WindowsGuide/what-is.md "../../../fsx/latest/WindowsGuide/what-is.md") file
system for task storage.

`fileSystemId`

Type: String

Required: Yes

The FSx for Windows File Server file system ID to use.

`rootDirectory`

Type: String

Required: Yes

The directory within the FSx for Windows File Server file system to mount as
the root directory inside the host.

`authorizationConfig`

`credentialsParameter`

Type: String

Required: Yes

The authorization credential options:

- Amazon Resource Name (ARN) of an [Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") secret.
- Amazon Resource Name (ARN) of an [Systems Manager](../../../systems-manager/latest/userguide/integration-ps-secretsmanager.md "../../../systems-manager/latest/userguide/integration-ps-secretsmanager.md") parameter.

`domain`

Type: String

Required: Yes

A fully qualified domain name that's hosted by an
[AWS Directory Service for Microsoft Active Directory](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md") (AWS Managed Microsoft AD)
directory or a self-hosted EC2 Active
Directory.

## Methods for storing FSx for Windows File Server volume credentials

There are two different methods of storing credentials for use with the
credentials parameter.

- AWS Secrets Manager secret

This credential can be created in the AWS Secrets Manager console by using the
_Other type of secret_ category. You add a row for
each key/value pair, username/admin and
password/`password`.

- Systems Manager parameter

This credential can be created in the Systems Manager parameter console by entering
text in the form that's in the following example code snippet.

```
{
  "username": "admin",
  "password": `"password"`
}
```

The `credentialsParameter` in the task definition
`FSxWindowsFileServerVolumeConfiguration` parameter holds either the
secret ARN or the Systems Manager parameter ARN. For more information, see [What is
AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _Secrets Manager User Guide_ and
[Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") from the _Systems Manager User
Guide_.
