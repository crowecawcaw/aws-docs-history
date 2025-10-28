# Troubleshoot impaired Amazon EC2 Linux instance using EC2Rescue

EC2Rescue for Linux is an easy-to-use, open-source tool that can be run on an Amazon EC2 Linux
instance to diagnose, troubleshoot, and remediate common issues using its library of over 100
_modules_. Modules are YAML files that contain either a BASH or a Python
script and the necessary metadata.

Some generalized use cases for EC2Rescue for Linux instances include:

- Gathering syslog and package manager logs
- Collecting resource utilization data
- Diagnosing and remediating known problematic kernel parameters and common OpenSSH issues

###### Note

The `AWSSupport-TroubleshootSSH` AWS Systems Manager Automation runbook installs
EC2Rescue for Linux and then uses the tool to check or attempt to fix common issues
that prevent an SSH connection to a Linux instance. For more information, see
[AWSSupport-TroubleshootSSH](../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootssh.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootssh.md").

If you are using a Windows instance, see [Troubleshoot impaired Amazon EC2 Windows instance using EC2Rescue](Windows-Server-EC2Rescue.md "Windows-Server-EC2Rescue.md").

###### Topics

- [Install EC2Rescue](ec2rl_install.md "ec2rl_install.md")
- [Run EC2Rescue commands](ec2rl_working.md "ec2rl_working.md")
- [Develop EC2Rescue modules](ec2rl_moduledev.md "ec2rl_moduledev.md")
