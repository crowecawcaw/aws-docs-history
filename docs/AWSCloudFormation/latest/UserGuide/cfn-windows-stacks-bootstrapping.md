# Bootstrapping Windows-based

CloudFormation stacks

This topic describes how to bootstrap a Windows stack and troubleshoot stack
creation issues.

###### Topics

- [User data in EC2 instances](#cfn-windows-bootstrapping-user-data "#cfn-windows-bootstrapping-user-data")
- [CloudFormation helper
  scripts](#cfn-windows-bootstrapping-helper-scripts "#cfn-windows-bootstrapping-helper-scripts")
- [Example of bootstrapping a
  Windows stack](#cfn-windows-bootstrapping-example "#cfn-windows-bootstrapping-example")
- [Escape backslashes in
  Windows file paths](#cfn-windows-stacks-escape-backslashes "#cfn-windows-stacks-escape-backslashes")
- [Manage Windows
  services](#cfn-windows-stacks-manage-windows-services "#cfn-windows-stacks-manage-windows-services")
- [Troubleshoot stack creation
  issues](#cfn-windows-stacks-troubleshooting "#cfn-windows-stacks-troubleshooting")

## User data in EC2 instances

User data is an Amazon EC2 feature that allows you to pass scripts or configuration
information to an EC2 instance when it launches.

For Windows EC2 instances:

- You can use either batch scripts (using `<script>` tags) or
  PowerShell scripts (using `<powershell>` tags).
- Script execution is handled by EC2Launch.

###### Important

If you are creating your own Windows AMI for use with CloudFormation, make sure
that EC2Launch v2 is properly configured. EC2Launch v2 is required for
CloudFormation bootstrapping tools to properly initialize and configure Windows
instances during stack creation. For more information, see [Use the EC2Launch v2 agent to
perform tasks during EC2 Windows instance launch](../../../AWSEC2/latest/UserGuide/ec2launch-v2.md "../../../AWSEC2/latest/UserGuide/ec2launch-v2.md") in the _Amazon EC2 User
Guide_.

For information about AWS Windows AMIs, see the [AWS Windows
AMI Reference](../../../ec2/latest/windows-ami-reference/windows-amis.md "../../../ec2/latest/windows-ami-reference/windows-amis.md").

## CloudFormation helper

scripts

Helper scripts are utilities for configuring instances during the bootstrapping process.
Used with Amazon EC2 user data, they provide powerful configuration options.

CloudFormation provides the following Python helper scripts that you can use to install
software and start services on an Amazon EC2 instance that you create as part of your
stack:

- `cfn-init` – Use to retrieve and interpret resource metadata,
  install packages, create files, and start services.
- `cfn-signal` – Use to signal with a `CreationPolicy`, so
  you can synchronize other resources in the stack when the prerequisite resource or
  application is ready.
- `cfn-get-metadata` – Use to retrieve metadata for a resource or
  path to a specific key.
- `cfn-hup` – Use to check for updates to metadata and execute custom
  hooks when changes are detected.

You call the scripts directly from your template. The scripts work in conjunction with
resource metadata that's defined in the same template. The scripts run on the Amazon EC2
instance during the stack creation process.

For more information, see the [CloudFormation helper scripts reference](../TemplateReference/cfn-helper-scripts-reference.md "../TemplateReference/cfn-helper-scripts-reference.md") in the _AWS CloudFormation Template
Reference Guide_.

## Example of bootstrapping a

Windows stack

Let's examine example snippets from a Windows Server template that
performs the following actions:

- Launches an EC2 instance named `TestInstance` from a Windows
  Server 2022 AMI.
- Creates a simple test file to verify `cfn-init` is working.
- Configures `cfn-hup` for ongoing configuration management.
- Uses a `CreationPolicy` to ensure the instance signals successful
  completion.

The `cfn-init` helper script is used to perform each of these actions
based on information in the `AWS::CloudFormation::Init` resource in the
template.

The `AWS::CloudFormation::Init` section is named `TestInstance`
and begins with the following declaration.

```
TestInstance:
  Type: AWS::EC2::Instance
  Metadata:
    AWS::CloudFormation::Init:
      configSets:
        default:
          - create_files
          - start_services
```

After this, the `files` section of `AWS::CloudFormation::Init` is
declared.

```
      create_files:
        files:
          c:\cfn\test.txt:
            content: !Sub |
              Hello from ${AWS::StackName}
          c:\cfn\cfn-hup.conf:
            content: !Sub |
              [main]
              stack=${AWS::StackName}
              region=${AWS::Region}
              interval=2
          c:\cfn\hooks.d\cfn-auto-reloader.conf:
            content: !Sub |
              [cfn-auto-reloader-hook]
              triggers=post.update
              path=Resources.TestInstance.Metadata.AWS::CloudFormation::Init
              action=cfn-init.exe -v -s ${AWS::StackName} -r TestInstance -c default --region ${AWS::Region}
```

Three files are created here and placed in the `C:\cfn` directory on
the server instance:

- `test.txt`, a simple test file that verifies
  `cfn-init` is working correctly and can create files with dynamic
  content.
- `cfn-hup.conf`, the configuration file for `cfn-hup`
  with a 2-minute check interval.
- `cfn-auto-reloader.conf`, the configuration file for the hook
  used by `cfn-hup` to initiate an update (calling `cfn-init`)
  when the metadata in `AWS::CloudFormation::Init` changes.

Next is the `start_services` section, which configures Windows
services.

```
      start_services:
        services:
          windows:
            cfn-hup:
              enabled: true
              ensureRunning: true
              files:
                - c:\cfn\cfn-hup.conf
                - c:\cfn\hooks.d\cfn-auto-reloader.conf
```

This section ensures that the `cfn-hup` service is started and will
automatically restart if the configuration files are modified. The service monitors for
changes to the CloudFormation metadata and re-runs `cfn-init` when updates are
detected.

Next is the `Properties` section.

```
TestInstance:
  Type: AWS::EC2::Instance
  CreationPolicy:
    ResourceSignal:
      Timeout: PT20M
  Metadata:
    AWS::CloudFormation::Init:
      # ... metadata configuration ...
  Properties:
    InstanceType: t2.large
    ImageId: '{{resolve:ssm:/aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base}}'
    SecurityGroupIds:
      - !Ref InstanceSecurityGroup
    KeyName: !Ref KeyPairName
    UserData:
      Fn::Base64: !Sub |
        <powershell>
        cfn-init.exe -v -s ${AWS::StackName} -r TestInstance -c default --region ${AWS::Region}
        cfn-signal.exe -e $lastexitcode --stack ${AWS::StackName} --resource TestInstance --region ${AWS::Region}
        </powershell>
```

In this section, the `UserData` property contains a PowerShell script that
will be executed by EC2Launch, surrounded by `<powershell>` tags.
The script runs `cfn-init` with the `default` configSet, then uses
`cfn-signal` to report the exit code back to CloudFormation. The
`CreationPolicy` is used to ensure the instance is properly configured before
the stack creation is considered complete.

The `ImageId` property uses a Systems Manager Parameter Store public parameter to
automatically retrieve the latest Windows Server 2022 AMI ID. This approach
eliminates the need for region-specific AMI mappings and ensures you always get the most
recent AMI. Using Systems Manager parameters for AMI IDs is a best practice for maintaining
current AMI references. If you plan to connect to your instance, make sure that the
`SecurityGroupIds` property references a security group that allows RDP
access.

The `CreationPolicy` is declared as part of the resource properties and
specifies a timeout period. The `cfn-signal` command in the user data
signals when the instance configuration is complete:

```
TestInstance:
  Type: AWS::EC2::Instance
  CreationPolicy:
    ResourceSignal:
      Timeout: PT20M
  Properties:
    # ... other properties ...
```

Because the bootstrapping process is minimal and only creates files and starts services,
the `CreationPolicy` waits 20 minutes (PT20M) before timing out. The timeout is
specified using ISO 8601 duration format. Note that Windows instances generally
take longer to launch than Linux instances, so test thoroughly to determine the best
timeout values for your needs.

If all goes well, the `CreationPolicy` completes successfully and you can
access the Windows Server instance using its public IP address. Once stack
creation is complete, the instance ID and public IP address will be displayed in the
**Outputs** tab of the CloudFormation console.

```
Outputs:
  InstanceId:
    Value: !Ref TestInstance
    Description: Instance ID of the Windows Server
  PublicIP:
    Value: !GetAtt TestInstance.PublicIp
    Description: Public IP address of the Windows Server
```

You can also manually verify that the bootstrapping worked correctly by connecting to the
instance via RDP and checking that the file `C:\cfn\test.txt` exists and
contains the expected content. For more information about connecting to Windows
instances, see [Connect to your
Windows instance using RDP](../../../AWSEC2/latest/UserGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/UserGuide/connecting_to_windows_instance.md") in the
_Amazon EC2 User Guide_.

## Escape backslashes in

Windows file paths

When referencing Windows paths in CloudFormation templates, always remember to properly
escape backslashes (`\`) according to the template format you're using.

- For JSON templates, you must use double backslashes in Windows file paths because JSON treats backslash as
  an escape character. The first backslash escapes the second, resulting in the interpretation of a single, literal backslash.

```
"commands" : {
  "1-extract" : {
    "command" : "C:\\SharePoint\\SharePointFoundation2010.exe /extract:C:\\SharePoint\\SPF2010 /quiet /log:C:\\SharePoint\\SharePointFoundation2010-extract.log"
  }
}
```

- For YAML templates, single backslashes are typically sufficient.

```
commands:
  1-extract:
    command: C:\SharePoint\SharePointFoundation2010.exe /extract:C:\SharePoint\SPF2010 /quiet /log:C:\SharePoint\SharePointFoundation2010-extract.log
```

## Manage Windows

services

You manage Windows services in the same way as Linux services, except that you
use a `windows` key instead of `sysvinit`. The following example
starts the `cfn-hup` service, sets it to Automatic, and restarts the service if
`cfn-init` modifies the `c:\cfn\cfn-hup.conf` or
`c:\cfn\hooks.d\cfn-auto-reloader.conf` configuration files.

```
        services:
          windows:
            cfn-hup:
              enabled: true
              ensureRunning: true
              files:
                - c:\cfn\cfn-hup.conf
                - c:\cfn\hooks.d\cfn-auto-reloader.conf
```

You can manage other Windows services in the same way by using the name, not the
display name, to reference the service.

## Troubleshoot stack creation

issues

If your stack fails during creation, the default behavior is to rollback on failure.
While this is normally a good default because it avoids unnecessary charges, it makes it
difficult to debug why your stack creation is failing.

To turn this behavior off when creating or updating your stack with the CloudFormation
console, choose the **Preserve successfully provisioned resources** option
under **Stack failure options**. For more information, see [Choose how to handle failures when provisioning
resources](stack-failure-options.md "stack-failure-options.md"). This allows you
to log into your instance and view the log files to pinpoint issues encountered when
running your startup scripts.

Important logs to look at are:

- The EC2 configuration log at
  `%ProgramData%\Amazon\EC2Launch\log\agent.log`
- The **cfn-init** log at
  `C:\cfn\log\cfn-init.log` (check exit codes and error messages
  for specific failure points)

For more logs, see the following topics in the _Amazon EC2 User
Guide_:

- [EC2Launch directory structure](../../../AWSEC2/latest/UserGuide/ec2config-service.md#UsingConfigXML_WinAMI "../../../AWSEC2/latest/UserGuide/ec2config-service.md#UsingConfigXML_WinAMI")
- [EC2Launch v2 directory structure](../../../AWSEC2/latest/UserGuide/ec2launch-v2.md#ec2launch-v2-directory "../../../AWSEC2/latest/UserGuide/ec2launch-v2.md#ec2launch-v2-directory")

For more information about troubleshooting bootstrapping issues, see [How do I
troubleshoot helper scripts that won't bootstrap in a CloudFormation stack with
Windows instances?](https://repost.aws/knowledge-center/cloudformation-helper-scripts-windows "https://repost.aws/knowledge-center/cloudformation-helper-scripts-windows").
