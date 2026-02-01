• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Install the Session Manager plugin on Amazon Linux 2,

Amazon Linux 2023, and Red Hat Enterprise Linux distributions

Use the following procedure to install the Session Manager plugin on Amazon Linux 2, Amazon Linux 2023
(AL2023), and RHEL distributions.

1. Download and install the Session Manager plugin RPM package.

x86_64
On Amazon Linux 2 and RHEL 7, run the following
command:

```
sudo yum install -y https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm
```

On AL2023 and RHEL 8 and 9, run the following
command:

```
sudo dnf install -y https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm
```

ARM64
On Amazon Linux 2 and RHEL 7, run the following
command:

```
sudo yum install -y https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_arm64/session-manager-plugin.rpm
```

On AL2023 and RHEL 8 and 9, run the following
command:

```
sudo dnf install -y https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_arm64/session-manager-plugin.rpm
```

2. Verify that the installation was successful. For information, see
   [Verify the Session Manager plugin installation](install-plugin-verify.md "install-plugin-verify.md").

###### Note

If you want to uninstall the plugin, run `sudo yum erase
 session-manager-plugin -y`
