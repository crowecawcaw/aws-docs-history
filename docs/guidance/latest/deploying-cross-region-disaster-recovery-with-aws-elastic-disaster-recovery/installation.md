# Installation

## Ensure Instance Profile Permissions

- Verify that the instances you want to protect have an instance profile with the following policies:
  - AmazonSSMManagedInstanceCore
  - AWSElasticDisasterRecoveryEC2InstancePolicy

- If the instance profile is not present, you can create the default instance profile by following these steps:
  1.  Go to the **Instance profile** role **installation** section.
  2.  Select the **Install default IAM role** button to create the default instance profile.

### Assign Instance Profiles:

- In the **Instance profiles** section, verify that all the instances you want to protect have the required instance profile assigned.
- If any instances do not have an instance profile, you can assign the default instance profile by selecting **Attach profiles to all instances**.

**Set Target Disaster Recovery Region**:

- In the **Target disaster recovery region** section, select the AWS Region where you want to set up the disaster recovery.
- If the selected Region is not initialized for Elastic Disaster Recovery, select **Initialize and configure Elastic Disaster Recovery** to set it up.

_NOTE: As this guide is based on a cross-Region deployment pattern, the Recovery Region you select should be different than the source Region where your source EC2 instances are deployed_

### Protect instances with Elastic Disaster Recovery:

- In the **Add instances** section, select **Add instances**.
- Elastic Disaster Recovery will list all the instances that are currently managed by AWS Systems Manager and will attempt to install the AWS replication agent on them.
- Once the AWS replication agent is successfully installed, the instances will be added as source servers to Elastic Disaster Recovery.

### Monitor the Process:

- In the **Add instances result** page, you can view the progress and status of the AWS replication agent installation on the instances.
- For instances where the installation was successful, you can find a link to the source servers page in the **Details** column.
- For instances where the installation failed, you can find a link to the run log on the AWS Systems Manager console.

### Verify Instance Management by AWS SSM:

- After attaching the instance profile, allow a few minutes for Elastic Disaster Recovery to detect if the instances are managed by AWS Systems Manager.
- The marker near the instance ID will change to indicate if the instance is currently managed by AWS Systems Manager.

Remember, if there are instances that are not managed by AWS Systems Manager, you will need to install the Systems Manager agent on those instances and then attach the appropriate instance profile before adding them to
Elastic Disaster Recovery. Should you not wish to utilize Systems Manager for this process, refer to [Adding Servers](../../../drs/latest/userguide/adding-servers.md "../../../drs/latest/userguide/adding-servers.md") for instructions on how to manually install the AWS Replication agent. If you are using a third-party software deployment process, consult with the team that manages it to find if it can be used to deploy AWS Elastic Disaster Recovery.

- When installing the AWS Replication Agent, you may run into unforeseen installation issues based on multiple factors. Refer to **Advanced topics** in the Resources section of this guide for common issues that can be encountered during the installation process.
- If you are unable to resolve the using the information provided, create an AWS support ticket and include the following:
  - What part of the installation process is failing
  - Confirmation that you have followed the troubleshooting guide
  - Attach the agent log from that specific server. The agent log can be located at the
    [following locations](../../../drs/latest/userguide/agent-logs-location.md "../../../drs/latest/userguide/agent-logs-location.md"):

        1. **Linux**: /var/log/awsdrs-agent/agent.log
        2. **Windows**: C:.log

  - Once the installation has completed, the Elastic Disaster Recovery console will show the following stages:
    - Initiating
      - This shows that the agent has been installed successfully on the source server, and Elastic Disaster Recovery is now moving on to the
        next steps of configuring replication for that server. To see what step the service is currently on, select the server name, and check
        under _Data replication status,_ as shown in the user guide under [Recovery Dashboard](<http://%20(https://docs.aws.amazon.com/drs/latest/userguide/recovery-dashboard.html)> "http://%20(https://docs.aws.amazon.com/drs/latest/userguide/recovery-dashboard.html)").

    - Initial sync | time left
      - This is the amount of the known blocks that will be replicated.
        - Note that you may see the time left for replication fluctuate by large margins. This is due to how reading block storage is accomplished and we are unable to predict how many future blocks may need to be replicated.
        - You can estimate the amount of time required to complete this step
          by analyzing the amount of storage that needs to be replicated and the available bandwidth available to transmit this data.

      - During this initial sync process, you may see _backlog_ in the same line.
        - Backlog is the amount of new data that has been written and waiting to be added after initial sync. Once initial sync has completed, you will see the backlog amount start to reduce as the agent replicates those newer blocks.

    - Initial sync 100% done | Creating Snapshot
      - All blocks have been replicated from the source machine to the staging area and we are now creating the baseline EBS snapshot for that
        volume.

            + **Note**: if the service is stuck in the stage for a long time, confirm the replication server has 443 outbound access to
            regional EC2 endpoint.

    - Healthy
      - All data has been replicated to the staging area, and the replication server has enough bandwidth to replicate the changes being
        generated at the source environment.
        _Should there be an issue with the replication process after you have completed the initial sync phase, you will see an error in the same
        location_.

  - Other states you might see are:
    - Rescan
      - This means that something has interrupted the agents ability to validate the block map, usually caused by an unplanned reboot of the
        source machine (such as a power outage, pulling the plug, or terminating an EC2 instance)

    - Lag
      - Lag is the amount of time since the server was last in continuous data protection (CDP) mode. Lag typically leads to backlog, which is the amount of data that has accumulated and still needs to be replicated. The longer the lag, the larger the backlog that needs to be cleared.
      - This can be caused by many items, and troubleshooting steps can be found in the userguide under [Replication Lag Issues](../../../drs/latest/userguide/Other-Troubleshooting-Topics.md#Replication-Lag-Issues "../../../drs/latest/userguide/Other-Troubleshooting-Topics.md#Replication-Lag-Issues").
      - Potential solutions:
        - Make sure that the source server is up and running.
        - Make sure that AWS Elastic Disaster Recovery services are running on the source server.
        - Make sure that TCP Port 1500 is not blocked outbound from the Source server to the replication server.
        - If the MAC address of the Source had changed, that would require a reinstallation of the AWS Replication Agent.
        - If the source machine had a spike of write operations, the lag will grow until AWS Elastic Disaster Recovery service manages to flush all the written data to the drill or recovery instance replication server.

    - Backlog
      - Backlog is the amount of data that was written to the disk and still needs to be replicated in order to reach CDP mode. backlog can also occur without lag. This can happen due to various reasons, such as:
        - Temporary network interruptions or bandwidth limitations that prevent the data from being replicated in real-time.
        - Spikes in data volume that exceed the processing capacity of the system, leading to a backlog.
        - Scheduled maintenance or other operational activities that temporarily pause the replication process.

      - Even if there is no lag, meaning the server or service is in the desired state, a backlog of data can still build up that needs to be processed. For example, a server generating traffic at a lower rate than the network bandwidth, resulting in no lag, but there could still be a
        backlog of data that needs to be replicated.
        _Once the installation process has been completed across all needed servers, you can move on to the next section, where you will configure monitoring and notifications_.
