# Install the CodeDeploy agent for

Windows Server

On Windows Server instances, you can use one of these methods to download and install the
CodeDeploy agent:

- Use AWS Systems Manager (recommended)
- Run a series of Windows PowerShell commands.
- Choose a direct download link.
- Run an Amazon S3 copy command.

###### Note

The folder that the CodeDeploy agent is installed to is `C:\Program
 Data\Amazon\CodeDeploy`. Make sure there are no directory junctions or
symlinks on this path.

###### Topics

- [Use Systems Manager](#codedeploy-agent-operations-install-system-manager "#codedeploy-agent-operations-install-system-manager")
- [Use Windows
  PowerShell](#codedeploy-agent-operations-install-windows-powershell "#codedeploy-agent-operations-install-windows-powershell")
- [Use a direct
  link](#codedeploy-agent-operations-install-windows-direct-link "#codedeploy-agent-operations-install-windows-direct-link")
- [Use an Amazon S3 copy
  command](#codedeploy-agent-operations-install-windows-s3-copy "#codedeploy-agent-operations-install-windows-s3-copy")

## Use Systems Manager

Follow the instructions in [Install the CodeDeploy agent using
AWS Systems Manager](codedeploy-agent-operations-install-ssm.md "codedeploy-agent-operations-install-ssm.md") to install the CodeDeploy
agent.

## Use Windows

PowerShell

Sign in to the instance, and run the following commands in Windows
PowerShell:

1. Require that all scripts and configuration files downloaded from the Internet
   be signed by a trusted publisher. If you are prompted to change the execution
   policy, type "`Y`."

```
 Set-ExecutionPolicy RemoteSigned
```

2. Load the AWS Tools for Windows PowerShell.

```
Import-Module AWSPowerShell
```

3. Create a directory into where the CodeDeploy agent installation file is downloaded.

```
New-Item -Path "c:\temp" -ItemType "directory" -Force
```

4. Configure AWS credentials using the `Set-AWSCredential` and
   `Initialize-AWSDefaultConfiguration` commands. For more information,
   see [Using AWS
   credentials](../../../powershell/latest/userguide/specifying-your-aws-credentials.md "../../../powershell/latest/userguide/specifying-your-aws-credentials.md") in the _AWS tools for PowerShell User
   Guide_.
5. Download the CodeDeploy agent installation file.

###### Note

AWS supports the latest minor version of the CodeDeploy agent. Currently the latest minor version is 1.7.x.

To install the latest version of the CodeDeploy
agent:

    * ```
    powershell.exe -Command Read-S3Object -BucketName `bucket-name` -Key latest/codedeploy-agent.msi -File c:\temp\codedeploy-agent.msi
    ```

To install a specific version of the CodeDeploy
agent:

    * ```
    powershell.exe -Command Read-S3Object -BucketName `bucket-name` -Key releases/codedeploy-agent-`###`.msi -File c:\temp\codedeploy-agent.msi
    ```

`bucket-name` is the name of the Amazon S3
bucket that contains the CodeDeploy Resource Kit files for your region. For example, for the
US East (Ohio) Region, replace `bucket-name` with
`aws-codedeploy-us-east-2`. For a list of bucket names, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names"). 6. Run the CodeDeploy agent installation file.

```
c:\temp\codedeploy-agent.msi /quiet /l c:\temp\host-agent-install-log.txt
```

To check that the service is running, run the following command:

```
powershell.exe -Command Get-Service -Name codedeployagent
```

If the CodeDeploy agent was just installed and has not been started, then after running
the **Get-Service** command, under **Status**, you
should see `Start...`:

```

Status     Name                DisplayName
------     ----                -----------
Start...   codedeployagent    CodeDeploy Host Agent Service
```

If the CodeDeploy agent is already running, after running the
**Get-Service** command, under **Status**, you should
see `Running`:

```

Status     Name                DisplayName
------     ----                -----------
Running    codedeployagent    CodeDeploy Host Agent Service
```

## Use a direct

link

If the browser security settings on the Windows Server instance
provide the permissions (for example, to `https://s3.*.amazonaws.com`), you
can use a direct link for your Region to download the CodeDeploy agent and then run the
installer manually.

The link is:

```
https://s3.`region`.amazonaws.com/aws-codedeploy-`region`/latest/codedeploy-agent.msi
```

...where `region` is the AWS
Region where you're deploying your application.

For example:

```
https://s3.af-south-1.amazonaws.com/aws-codedeploy-af-south-1/latest/codedeploy-agent.msi
```

###### Important

Obtain the `.msi` file from the same Region as your CodeDeploy
application. Choosing a different Region may cause `inconsistent region`
failures in the `codedeploy-agent-log` file when you run the
`.msi` file.

## Use an Amazon S3 copy

command

If the AWS CLI is installed on the instance, you can use the Amazon S3 [cp](../../../cli/latest/reference/s3/cp.md "../../../cli/latest/reference/s3/cp.md") command to download the CodeDeploy agent and then
run the installer manually. For information, see [Install the AWS Command Line Interface on Microsoft
Windows](../../../cli/latest/userguide/awscli-install-windows.md "../../../cli/latest/userguide/awscli-install-windows.md").

The Amazon S3 command is:

```
aws s3 cp s3://aws-codedeploy-`region`/latest/codedeploy-agent.msi codedeploy-agent.msi --region `region`
```

...where `region` is the AWS
Region where you're deploying your application.

For example:

```
aws s3 cp s3://aws-codedeploy-af-south-1/latest/codedeploy-agent.msi codedeploy-agent.msi --region af-south-1
```
