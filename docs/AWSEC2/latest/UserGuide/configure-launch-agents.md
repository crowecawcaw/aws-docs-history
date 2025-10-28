# Windows launch agents on Amazon EC2 Windows instances

Each AWS Windows AMI includes a Windows launch agent that's pre-configured with default
settings. Launch agents perform tasks during instance startup and run if an instance is
stopped and later started, or restarted. For information about a specific agent, see the
detail pages in the following list.

For more information about AWS Windows AMIs, see the [AWS
Windows AMI reference](../../../ec2/latest/windows-ami-reference/windows-amis.md "../../../ec2/latest/windows-ami-reference/windows-amis.md").

- [Use the EC2Launch v2 agent to perform tasks during EC2 Windows
  instance launch](ec2launch-v2.md "ec2launch-v2.md")
- [Use the EC2Launch v1 agent to perform tasks during EC2 Windows
  instance launch](ec2launch.md "ec2launch.md")
- [Use the EC2Config service to perform tasks during EC2 legacy Windows
  operating system instance launch](ec2config-service.md "ec2config-service.md")

###### Content

- [Compare Amazon EC2 launch agents](#ec2launch-agent-compare "#ec2launch-agent-compare")
- [Configure DNS Suffix for EC2 Windows launch agents](launch-agents-set-dns.md "launch-agents-set-dns.md")
- [Subscribe to EC2 Windows launch agent notifications](launch-agents-subscribe-notifications.md "launch-agents-subscribe-notifications.md")
- [Windows Service administration for EC2Launch v2 and EC2Config agents](launch-agents-service-admin.md "launch-agents-service-admin.md")

## Compare Amazon EC2 launch agents

The following table shows the major functional differences between EC2Config,
EC2Launch v1, and EC2Launch v2.

| Feature                            | EC2Config       | EC2Launch v1                                                  | EC2Launch v2                                                                        |
| ---------------------------------- | --------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Run as                             | Windows Service | PowerShell Scripts                                            | Windows Service                                                                     |
| Supports                           | Legacy OS only  | Windows Server versions: <br>• 2016 <br>• 2019 (LTSC and SAC) | Windows Server versions: <br>• 2016 <br>• 2019 (LTSC and SAC) <br>• 2022 <br>• 2025 |
| Configuration file                 | XML             | JSON                                                          | JSON/YAML                                                                           |
| Set Administrator username         | No              | No                                                            | Yes                                                                                 |
| Compressed user data               | No              | No                                                            | Yes                                                                                 |
| Local user data baked on AMI       | No              | No                                                            | Yes, configurable                                                                   |
| Task configuration in user data    | No              | No                                                            | Yes                                                                                 |
| Configurable wallpaper             | No              | No                                                            | Yes                                                                                 |
| Customize task run order           | No              | No                                                            | Yes                                                                                 |
| Configurable tasks                 | 15              | 9                                                             | 20 at launch                                                                        |
| Supports Windows Event Viewer      | Yes             | No                                                            | Yes                                                                                 |
| Number of Event Viewer event types | 2               | 0                                                             | 30                                                                                  | ###### Note EC2Config documentation is provided for historical reference only. The operating system versions it runs on are no longer supported by Microsoft. We strongly recommend that you upgrade to the latest launch service. |
