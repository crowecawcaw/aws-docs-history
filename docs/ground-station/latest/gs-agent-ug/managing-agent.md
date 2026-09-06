

# Manage the agent
<a name="managing-agent"></a>

 The AWS Ground Station Agent provides the following capabilities for configuring, starting, stopping, upgrading, downgrading and uninstalling the agent using built-in Linux command tooling. 

**Topics**
+ [AWS Ground Station Agent configuration](#gs-agent-configuration)
+ [AWS Ground Station Agent start](#gs-agent-start)
+ [AWS Ground Station Agent stop](#gs-agent-stop)
+ [AWS Ground Station Agent upgrade](#gs-agent-upgrade)
+ [AWS Ground Station Agent downgrade](#gs-agent-downgrade)
+ [AWS Ground Station Agent uninstall](#gs-agent-uninstall)
+ [AWS Ground Station Agent status](#gs-agent-status)
+ [AWS Ground Station Agent RPM info](#gs-agent-rpm-info)

## AWS Ground Station Agent configuration
<a name="gs-agent-configuration"></a>

 Navigate to `/opt/aws/groundstation/etc`, which should contain a single file named aws-gs-agent-config.json. See [Agent config file](configuring-agent.md#agent-config-file) 

## AWS Ground Station Agent start
<a name="gs-agent-start"></a>

```
#start
sudo systemctl start aws-groundstation-agent

#check status
systemctl status aws-groundstation-agent
```

Should produce output showing agent is **active**.

```
aws-groundstation-agent.service - aws-groundstation-agent
Loaded: loaded (/usr/lib/systemd/system/aws-groundstation-agent.service; enabled; vendor preset: disabled)
Active: active (running) since Tue 2023-03-14 00:39:08 UTC; 1 day 13h ago
Docs: https://aws.amazon.com/ground-station/
Main PID: 8811 (aws-gs-agent)
CGroup: /system.slice/aws-groundstation-agent.service
└─8811 /opt/aws/groundstation/bin/aws-gs-agent production
```

## AWS Ground Station Agent stop
<a name="gs-agent-stop"></a>

```
#stop
sudo systemctl stop aws-groundstation-agent

#check status
systemctl status aws-groundstation-agent
```

 Should produce output showing agent is **inactive** (stopped). 

```
aws-groundstation-agent.service - aws-groundstation-agent
Loaded: loaded (/usr/lib/systemd/system/aws-groundstation-agent.service; enabled; vendor preset: disabled)
Active: inactive (dead) since Thu 2023-03-09 15:35:08 UTC; 6min ago
Docs: https://aws.amazon.com/ground-station/
Process: 84182 ExecStart=/opt/aws/groundstation/bin/launch-aws-gs-agent (code=exited, status=0/SUCCESS)
Main PID: 84182 (code=exited, status=0/SUCCESS)
```

## AWS Ground Station Agent upgrade
<a name="gs-agent-upgrade"></a>

1. Download the latest version of the agent. See [Download agent](installing-the-agent.md#download-agent).

1. Stop the agent.

   ```
   #stop
   sudo systemctl stop aws-groundstation-agent
   
   #confirm inactive (stopped) state
   systemctl status aws-groundstation-agent
   ```

1. Update the agent.

   ```
   sudo yum update ${MY_RPM_FILE_PATH}
   
   # check the new version has been installed correctly by comparing the agent version with the starting agent version
   yum info aws-groundstation-agent
   
   # reload the systemd configuration
   sudo systemctl daemon-reload
   
   # restart the agent
   sudo systemctl restart aws-groundstation-agent
   
   # check agent status
   systemctl status aws-groundstation-agent
   ```

## AWS Ground Station Agent downgrade
<a name="gs-agent-downgrade"></a>

1. Download the agent version you need. See [Download agent](installing-the-agent.md#download-agent).

1. Downgrade the agent.

   ```
   # get the starting agent version
   yum info aws-groundstation-agent
   
   # stop the agent service
   sudo systemctl stop aws-groundstation-agent
   
   # downgrade the rpm
   sudo yum downgrade ${MY_RPM_FILE_PATH}
   
   # check the new version has been installed correctly by comparing the agent version with the starting agent version
   yum info aws-groundstation-agent
   
   # reload the systemd configuration
   sudo systemctl daemon-reload
   
   # restart the agent
   sudo systemctl restart aws-groundstation-agent
   
   # check agent status
   systemctl status aws-groundstation-agent
   ```

## AWS Ground Station Agent uninstall
<a name="gs-agent-uninstall"></a>

 Uninstalling the agent will rename /opt/aws/groundstation/etc/aws-gs-agent-config.json to /opt/aws/groundstation/etc/aws-gs-agent-config.json.rpmsave. Installing the agent again on the same instance again will write default values for aws-gs-agent-config.json and will need to be updated with the correct values corresponding to your AWS resources. See [Agent config file](configuring-agent.md#agent-config-file). 

```
sudo yum remove aws-groundstation-agent
```

## AWS Ground Station Agent status
<a name="gs-agent-status"></a>

 The agent status is either **active** (agent is running) or **inactive** (agent is stopped). 

```
systemctl status aws-groundstation-agent
```

 An example output shows that the agent is installed, **inactive** state (stopped) and **enabled** (start service on boot). 

```
aws-groundstation-agent.service - aws-groundstation-agent
Loaded: loaded (/usr/lib/systemd/system/aws-groundstation-agent.service; enabled; vendor preset: disabled)
Active: inactive (dead) since Thu 2023-03-09 15:35:08 UTC; 6min ago
Docs: https://aws.amazon.com/ground-station/
Process: 84182 ExecStart=/opt/aws/groundstation/bin/launch-aws-gs-agent (code=exited, status=0/SUCCESS)
Main PID: 84182 (code=exited, status=0/SUCCESS)
```

## AWS Ground Station Agent RPM info
<a name="gs-agent-rpm-info"></a>

```
yum info aws-groundstation-agent
```

 The output is as follows: 

**Note**  
“Version” might be different based on latest agent published version.

```
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Installed Packages
Name        : aws-groundstation-agent
Arch        : x86_64
Version     : 1.0.5953.0
Release     : 1
Size        : XX M
Repo        : installed
Summary     : Client software for AWS Ground Station
URL         : https://aws.amazon.com/ground-station/
License     : Proprietary
Description : This package provides client applications for use with AWS Ground Station
```