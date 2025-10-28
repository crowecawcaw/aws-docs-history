# Recovery planning

In order to launch your recovery instances quickly, you should pre-configure how those instances are to be launched. Also, perform drills in order to make sure that all of your network and application settings are properly configured. You can configure how your instances will be launched by editing the Launch settings for each source server. Launch settings can be configured immediately when a source server has been added to Elastic Disaster Recovery, there is no need to wait for the initial sync process to finalize. Performing frequent drills is key for failover preparedness. Elastic Disaster Recovery makes it easy for you to launch drill instances as frequently as you want. Drills are non-disruptive and do not impact the source server or ongoing data replication. If you experience a disaster in the middle of a drill, you can launch a new recovery instance from the source server’s current state or keep the instance you launched during the drill.

## Preparing for recovery

1. Configure your [launch templates](../../../drs/latest/userguide/launching-target-servers.md "../../../drs/latest/userguide/launching-target-servers.md") for each server you want to protect.
2. Under the **Ready for recovery** column, the server should show **Ready**. This means that the initial sync has been completed and all data from the source server has been replicated to AWS.
3. Under the **Data replication status** column, the server should show the **Healthy** status, but you can also launch the source server if the system is undergoing **Lag** or even **Stall**, but in that case the data may not be up to date. You can still launch a drill instance from a previous Point In Time.
4. Under the **Pending actions** column, the server should show **Initiative recovery drill** if no drill instances have ever been launched for the server. Otherwise, the column will be blank. This helps you identify whether the server has had a recent drill or recovery launch.

## Performing recovery

Prior to launching a Recovery instance, ensure that your source servers are ready for a Recovery by looking for the following indicators on the **Source Servers** page:

1. Under the **Ready for recovery** column, the server should show **Ready**.
2. Under the **Data replication status** column, the server should show **Healthy** status.
3. Under the **Last recovery result** column, there should be an indication of a successful drill or recovery instance launch sometime in the past. The column should state **Successful** and show when the last successful
   launch occurred. This column may be empty if a significant amount of time passed since your last drill instance launch.

To launch a recovery instance for a single source server or multiple source servers, go to the **Source servers** page and check the box to the left of each server for which you want to launch a recovery instance.

1. Open the **Initiate recovery job** menu and select **Initiate recovery**.
2. Select the Point in time snapshot from which to launch the recovery instance for the selected source server. You can either select the **Use most recent data** option to use the latest snapshot available or select an earlier specific Point-in-time snapshot. You may opt to select an
   earlier snapshot in case you wish to return to a specific server configuration before a disaster occurred. After you have selected the Point in Time snapshot, choose **Initiate recovery**. [Learn more about Point in Time snapshots.](../../../drs/latest/userguide/failback-overview.md#point-in-time-faq "../../../drs/latest/userguide/failback-overview.md#point-in-time-faq") in the userguide.
3. The Elastic Disaster Recovery Console will indicate **Recovery job is creating recovery instance for X source servers** when the drill has started.
4. Select **View job details** on the dialog to view the specific Job for the test launch in the **Recovery job history** tab.

_Note Elastic Disaster Recovery is only one part of your disaster recovery plan. There are likely to be many other dependencies and services that will play a role in recovering from a disaster, and this should be factored in when conducting a drill or actual failover._

### Group Launch Templates

Amazon EC2 launch templates control how instances are launched in AWS and each source server has its own launch template. You can edit the launch templates for multiple source servers at once by selecting the relevant servers on the Source servers page, then choosing **Edit EC2 launch
template** from the **Actions** dropdown menu.

**Important** - to edit the launch template, automated launch settings, or to conduct
[Instance type right-sizing](../../../drs/latest/userguide/launch-general-settings.md#server-launch-settings-parameters "../../../drs/latest/userguide/launch-general-settings.md#server-launch-settings-parameters"), the DRS launch settings must first be set to **Inactive** else you will receive an error.

**Note**:
The [DRS Template Manager](https://github.com/aws-samples/drs-tools/tree/main/drs-template-manager "https://github.com/aws-samples/drs-tools/tree/main/drs-template-manager") is an open source solution available on GitHub that can automate management of launch templates with the use of a single
JSON file as a baseline template. This file can be replicated, edited, and used for each source server tagged with a corresponding key in the DRS console.
