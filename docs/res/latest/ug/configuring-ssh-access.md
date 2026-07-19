# Configuring SSH access

Administrators can enable or disable SSH for the RES environment from the
**Environment boundaries** section. SSH Access to VDIs is
facilitated through a bastion host. When you activate this toggle, RES deploys
a bastion host and makes the SSH Access Instructions page visible for users.
When you deactivate the toggle, RES disables SSH access, terminates the bastion
host and removes the SSH access instructions page for users. This toggle is
deactivated by default.

###### Note

When RES deploys a bastion host it adds a `t3.medium` Amazon EC2
instance in your AWS account. You are responsible for all charges associated with
this instance. See the [Amazon EC2 pricing page](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/") for more information.

###### To enable SSH access

1. In the RES console, on the left navigation pane, choose **Environment
   Management**, then **Permission Policy**. Under
   **Environment boundaries** select the **SSH access**
   toggle.

![Permission policy page under environment management in the admin console](images/permission-policy-ssh-disabled.png) 2. Wait for SSH access to be enabled.

![Advisory banner appears on the permission policy page under environment management in the admin console](images/permission-policy-enable-ssh.png) 3. Once the Bastion host is added, SSH access is enabled.

![Permission policy page under environment management in the admin console](images/permission-policy-ssh-enabled.png)

The **SSH Access Instructions** page is visible to users
from their left navigation pane.

![SSH access instructions page showing steps for Linux and Windows](images/permission-policy-ssh-enabled2.png)

###### To disable SSH access

1. In the RES console, on the left navigation pane, choose **Environment
   Management**, then **Permission Policy**. Under
   **Environment boundaries** select the **SSH access**
   toggle.

![Permission policy page under environment management in the admin console](images/permission-policy-ssh-enabled.png) 2. Wait for SSH access to be disabled.

![A banner shows SSH access is being disabled on the Permission policy page](images/permission-policy-disable-ssh.png) 3. Once the process is complete, SSH access is disabled.

![Permission policy page showing SSH access disabled](images/permission-policy-ssh-disabled.png)
