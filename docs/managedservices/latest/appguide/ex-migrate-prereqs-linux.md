# LINUX Prerequisites

Observe the requirements listed in
[Migrating Workloads: Prerequisites for Linux and Windows](ex-migrate-instance-prereqs.md "ex-migrate-instance-prereqs.md") and ensure the following
before submitting a WIGS RFC:

- The latest enhanced networking drivers are installed; see [Enhanced Networking on Linux](../../../AWSEC2/latest/UserGuide/enhanced-networking.md "../../../AWSEC2/latest/UserGuide/enhanced-networking.md").
- Third-party software components that will conflict with AMS components have been removed:
  - Anti-virus Clients
  - Backup Clients
  - Virtualization software (such as VM Tools or Hyper-V Integration services)
  - Access Management Software (Such as SSSD, Centrify, or PBIS)

- Ensure SSH is properly configured - This temporarily enables private key authentication for SSH. AMS
  uses this with our configuration management tool. Use these commands:

```
sudo grep -q "^PubkeyAuthentication" /etc/ssh/sshd_config && sudo sed "s/^PubkeyAuthentication=.*/PubkeyAuthentication yes/" -i /etc/ssh/sshd_config || sudo sed "$ a\PubkeyAuthentication yes" -i /etc/ssh/sshd_config
```

```
sudo grep -q "^AuthorizedKeysFile" /etc/ssh/sshd_config && sudo sed "s/^AuthorizedKeysFile=.*/AuthorizedKeysFile %h\/.ssh\/authorized_keys/" -i /etc/ssh/sshd_config || sudo sed "$ a\AuthorizedKeysFile %h/.ssh/authorized_keys" -i /etc/ssh/sshd_config
```

- Ensure Yum is properly configured - RedHat requires licensing to use their Yum Repositories. The instance needs to be licensed via a Satellite Server or RedHat Cloud Server.
  Use one of these links if licensing is needed:
  - [Red Hat Satellite](https://www.redhat.com/en/technologies/management/satellite "https://www.redhat.com/en/technologies/management/satellite")
  - [Red Hat Cloud Access](https://www.redhat.com/en/technologies/cloud-computing/cloud-access "https://www.redhat.com/en/technologies/cloud-computing/cloud-access")

- If you use Red Hat Satellite, WIGS requires the addition of Red Hat Software Collections (RHSCL).
  The WIGS system uses RHSCL to add a Python3.6 interpreter alongside whatever is configured on the system. To support this solution, the following repositories must be available:
  - rhel-server-rhscl
  - rhel-server-releases-optional
