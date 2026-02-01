• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Checking SSM Agent status and starting the

agent

This topic lists the commands to check whether AWS Systems Manager Agent (SSM Agent) is running
on each supported operating system. It also provides the commands to start the agent if
it isn't running.

| Operating system                                                                       | Command to check SSM Agent status                                         | Command to start SSM Agent                                                                                               |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Amazon Linux 2and Amazon Linux 2023                                                    | `sudo systemctl status amazon-ssm-agent`                                  | `sudo systemctl enable amazon-ssm-agent`<br>`sudo systemctl start amazon-ssm-agent`                                      |
| Debian Server11 and 12                                                                 | `sudo systemctl status amazon-ssm-agent`                                  | `sudo systemctl enable amazon-ssm-agent`<br>`sudo systemctl start amazon-ssm-agent`                                      |
| macOS                                                                                  | Check the agent log file at<br>`/var/log/amazon/ssm/amazon-ssm-agent.log` | `sudo launchctl load -w<br>/Library/LaunchDaemons/com.amazon.aws.ssm.plist`<br>`sudo launchctl start com.amazon.aws.ssm` |
| Oracle Linux                                                                           | `sudo systemctl status amazon-ssm-agent`                                  | `sudo systemctl enable amazon-ssm-agent`<br>`sudo systemctl start amazon-ssm-agent`                                      |
| Red Hat Enterprise Linux (RHEL) 7.x, 8.x, 9.x, and 10.x                                | `sudo systemctl status amazon-ssm-agent`                                  | `sudo systemctl enable amazon-ssm-agent`<br>`sudo systemctl start amazon-ssm-agent`                                      |
| SUSE Linux Enterprise Server (SLES)                                                    | `sudo systemctl status amazon-ssm-agent`                                  | `sudo systemctl enable amazon-ssm-agent`<br>`sudo systemctl start amazon-ssm-agent`                                      |
| Ubuntu Server 16.04 (32-bit)                                                           | `sudo status amazon-ssm-agent`                                            | `sudo start amazon-ssm-agent`                                                                                            |
| Ubuntu Server 16.04 64-bit instances (deb package installation)                        | `sudo systemctl status amazon-ssm-agent`                                  | `sudo systemctl enable amazon-ssm-agent`<br>`sudo systemctl start amazon-ssm-agent`                                      |
| Ubuntu Server 16.04 LTS, 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS,<br>24.0, and 25.04 | `sudo systemctl status<br>snap.amazon-ssm-agent.amazon-ssm-agent.service` | `sudo snap start amazon-ssm-agent`                                                                                       |
| Windows Server                                                                         | _Run in PowerShell:_<br>`Get-Service AmazonSSMAgent`                      | _Run in PowerShell Administrator<br>mode:_<br>`Start-Service AmazonSSMAgent`                                             |

**More info**

- [Working with SSM Agent on EC2 instances for
  Linux](ssm-agent-linux.md "ssm-agent-linux.md")
- [Working with SSM Agent on EC2 instances for
  Windows Server](ssm-agent-windows.md "ssm-agent-windows.md")
- [Checking the SSM Agent version number](ssm-agent-get-version.md "ssm-agent-get-version.md")
