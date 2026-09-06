

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Install SSM Agent on Ubuntu Server 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04
<a name="agent-install-ubuntu-64-snap"></a>

**Before you begin**  
Before you install SSM Agent on an Ubuntu Server 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04, note the following: 

SSM Agent installer files locations  
On Ubuntu Server 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04, SSM Agent installer files, including agent binaries and config files, are stored in the following directory: `/snap/amazon-ssm-agent/current/`. If you make changes to any configuration files in this directory, then you must copy these files from the `/snap` directory to the `/etc/amazon/ssm/` directory. Log and library files haven't changed (`/var/lib/amazon/ssm`, `/var/log/amazon/ssm`).

Using the Snap `candidate` channel  
The *candidate* channel in the Snap store contains the latest version of SSM Agent (including all of the latest bug fixes); not the stable channel. To learn more about the differences between the candidate and stable channels, see **Risk-levels** at [https://snapcraft.io/docs/channels](https://snapcraft.io/docs/channels).  
If you want to track SSM Agent version information on the candidate channel, run the following command on your Ubuntu Server 20.04 and 18.04 LTS 64-bit instances.  

```
sudo snap switch --channel=candidate amazon-ssm-agent
```

Snaps recommended on versions 18.04 and later  
On Ubuntu Server 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04, we recommend you only use Snaps. Also verify that only one instance of the agent is installed and running on your instances.

`Maximum timeout exceeded` error message  
Because of a known issue with Snap, you might see a `Maximum timeout exceeded` error with `snap` commands. If you get this error, run the following commands one at a time to start the agent, stop it, and check its status:   

```
sudo systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service
```

```
sudo systemctl stop snap.amazon-ssm-agent.amazon-ssm-agent.service
```

```
sudo systemctl status snap.amazon-ssm-agent.amazon-ssm-agent.service
```

**To install SSM Agent on Ubuntu Server 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04 (with Snap package)**

1. SSM Agent is installed, by default, on Ubuntu Server 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04 AMIs with an identifier of `20180627` or later.

   You can use the following script if you need to install SSM Agent on an on-premises server or if you need to reinstall the agent. You don't need to specify a URL for the download, because the `snap` command automatically downloads the agent from the [Snap app store](https://snapcraft.io/amazon-ssm-agent) at [https://snapcraft.io](https://snapcraft.io).

   ```
   sudo snap install amazon-ssm-agent --classic
   ```

1. Run the following command to determine if SSM Agent is running. 

   ```
   sudo snap list amazon-ssm-agent
   ```

1. Run the following command to start the service if the previous command returned `amazon-ssm-agent is stopped`, `inactive`, or `disabled`.

   ```
   sudo snap start amazon-ssm-agent
   ```

1. Check the status of the agent.

   ```
   sudo snap services amazon-ssm-agent
   ```