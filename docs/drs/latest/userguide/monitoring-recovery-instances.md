# Monitoring recovery instances

You can monitor your recovery instances on the **Recovery
instances** page. It displays all of your recovery instances and sorts them
by **Instance ID**, **Reversed
direction launch state**, **Data replication
status**, **Pending actions**, **Replicating to source server**, **Last
launch result**, and **Launched from source
server.**

You can sort your recovery instances alphabetically in descending or ascending order
by choosing the arrow next to the various category headers (with the exception of data
replication status).

You can filter the recovery instances page by the properties in the **Filter by property of value** box.

## Recovery instance categories

Here is a breakdown of each category header:

### Instance ID

The **Instance ID** category displays the ID of
the recovery instance. Choose an Instance ID to open the recovery instance
details view. [Learn more about the
recovery instance details view.](recovery-instances-details.md "recovery-instances-details.md")

### Reversed direction launch state

The **Reversed direction launch state** displays
the current state of the reversed direction launch for the recovery instance.
Possible states include:

- **Not started** – Reversed replication
  has not been started for the recovery instance.
- **Synchronizing** – Reversed replication
  has been started for the recovery instance and is currently in process.
- **Ready** – Reversed replication has
  completed initiation and is ready to be launched.
- **Completed** – Failback process to the
  on-premises server has been successfully completed. This value does not
  appear for in-AWS launch flows.
- **Error** – There was an error during the
  reversed replication process. You can learn more about the cause of the
  error in the **Data replication status**
  and **Pending actions** columns.

### Data replication status

The **Data replication status** category displays
the current data replication status of the recovery instance. Possible states
include:

- **Not started** – Data replication has
  not started for the recovery instance. This indicates that failback has
  not started for the instance.
- **Initiating** – Data replication is
  initiating. This indicates that reversed replication has been initiated
  for the instance.
- **Initial sync** – The recovery instance is
  undergoing the initial sync process after reversed replication has been
  initiated. The Elastic Disaster Recovery Console displays the percentage
  completed and the time left.
- **Rescanning** – The recovery instance is
  undergoing a rescan. The AWS Elastic Disaster Recovery Console displays
  the percentage completed and the time left.
- **Healthy** – The data replication process
  has been completed and the recovery instance is ready for launch.
- **Lag** – The recovery instance is
  currently experiencing lag. Open the recovery instance details view to
  learn more.
- **Stalled** – The recovery instance is
  experiencing a stall. Open the **Recovery instance
  details** view to learn more.
- **Completed** – The failback process has
  been completed and as a result data replication has been successfully
  completed and stopped. This value is only relevant to on-premises
  failback and does not appear in in-AWS flows.
- **Disconnected** – The recovery instance
  has been disconnected from AWS Elastic Disaster Recovery. As a result,
  data replication has stopped.

### Pending actions

The **Pending actions** column provides
additional details, when relevant, about the next actions that should be
performed to progress the current flow or to initiate the reversed replication.
Possible values include:

- **Launch for failback on {region}** – This
  status indicates that reversed replication has reached a healthy state.
  To launch for failback, choose the link under **replicating to source server**.
- **Use failback client** – To start the
  replication back to the on-premises server, use the Failback Client.
  This value is only relevant to on-premises failback.
- **Start reversed replication to {region
  name}** – Choose **start reversed
  replication** to initiate reversed replication to the
  specified region. This value only applies to in-AWS and cross-region
  replications.

### Replicating to

source server

The **Replicating to source server** category
identifies the source server to which the recovery instance is replicating. When
you start reversed replication it is managed through this source server. Launch
operations are performed by navigating to this source server and initiating the
operation from that screen.

These are displayed in order:

- The source server region
- The source server's ID

Choose the source server links to view the source server details of the source
server that is associated with the specific recovery instance. [Learn more about the server details view](server-details.md "server-details.md"). If
the source server is located in another region (marked by an external icon),
choosing the link opens the source server's details page in a different
tab.

### Last launch results

This category indicated the results of the last launch. Possible values include:

- Launch successful
- Failback successful
- Launch failed
- Failback failed

### Launched from

source server

The **Launched from source server** column
identifies the source server from which the recovery instance was
launched.

These are displayed in order:

- The source server hostname
- The source server's ID

Choose the source server links to view the source server details of the source
server that is associated with the specific recovery instance. [Learn more about the server details
view](server-details.md "server-details.md").

## Recovery instances actions

The recovery instances page allows you to perform actions that include viewing
recovery instance details, adding recovery instances, editing the failback
replication settings, terminating recovery instances, and continuing the failback
process.

### Actions menu

Actions available on the **Actions** menu:

#### View instance

details

Select a recovery instance and choose the **View
instance details** option under the **Actions** menu to open the **Recovery
instance details** view. [Learn more about the recovery
instance details view.](recovery-instances-details.md "recovery-instances-details.md")

#### Edit failback replication

settings

Select one or more recovery instances and choose the **Edit failback replication settings** option under the
**Actions** menu to edit the failback
replication settings the selected recovery instances. The failback
replication settings configure the replication to the on-premises servers
during an on-premises failback process. This does not apply to in-AWS
replication, which is managed on the **replicating to
source server** source servers. [Learn
more about Failback replication settings.](recovery-instances-details.md#recovery-instances-details-failback-replication-settings "recovery-instances-details.md#recovery-instances-details-failback-replication-settings")

#### Stop failback

Select one or more recovery instances that are in the **Synchronizing** state and choose the **Stop**option under the **Actions** menu to stop the failback process for the selected
recovery instance or instances. This returns the instances' **Reversed replication launch state** to **Not started** and stops any ongoing failback
process. The Failback client indicates that the failback has been stopped.
To restart failback, reboot the machine in the Failback Client. Note that
the **Stop failback** state is only relevant to
on-premises flows.

On the **Stop failback for recovery
instances** dialog choose **Stop
failback**.

#### Terminate recovery instances

Select one or more recovery instances and choose the **Terminate recovery instances** option under the **Actions** menu to terminate the recovery instance
or instances. This removes all of the resources associated with the selected
recovery instance or instances from Elastic Disaster Recovery and terminates all related EC2
resources. Perform this action if you no longer need the recovery instance,
for example, if it was for a drill.

On the **Terminate recovery instances**
dialog choose **Terminate**.

#### Disconnect from

AWS

Select one or more recovery instances and choose the **Disconnect from AWS** option under the **Actions** menu to disconnect the recovery instance or
instances from AWS. This deletes the AWS Replication Agent from the recovery
instance or instances, but keeps the recovery instance Elastic Disaster
Recovery resources and the EC2 resources intact. You may want to disconnect
from AWS if you do not want to perform a launch for the specific recovery
instance or instances and do not want to accrue additional costs for data
replication, but still want the recovery instance to appear in the Elastic
Disaster Recovery Console.

On the **Disconnect X recovery instances from
service** dialog choose **Disconnect**.

#### Delete

recovery instances

Select one or more recovery instances and choose the **Delete recovery instances** option under the **Actions** menu to delete the recovery instance or
instances. This removes all of resources associated with the selected
recovery instance or instances from Elastic Disaster Recovery but does not
terminate all related EC2 resources and the instance keeps running on
Amazon EC2.

You may want to delete the recovery instance or instances if you
already failed over into AWS, but then decided to permanently keep your workload in AWS
instead of failing back to your original source servers and do not want to
incur any more costs associated with Elastic Disaster Recovery resources.
You may also want to delete the recovery instance or instances if you
performed an in-AWS launch but do not want to start reversed replication
back to the original region. Note that you can only delete recovery
instances that have already been disconnected from AWS.

On the **Delete recovery instance** dialog
choose **Delete**.

###### Note

Launch of a new recovery instance from the same source server cleans up
all the previous recovery instances, regardless if they have been
disconnected and deleted from DRS.

### Failback

Select one or more recovery instances that are in the **Ready** state and choose the **Complete
failback** option to continue the failback process after performing
a failback with the Elastic Disaster Recovery Failback Client. This action stops
data replication and starts the conversion process. This finalizes the failback
process and creates a replica of each recovery instance on the corresponding
source server.

###### Important

Ensure that you complete the [entire failback process with
the Elastic Disaster Recovery Failback Client](failback-performing.md "failback-performing.md") prior to choosing the Failback
option.

On the **Continue with failback for X instances**
dialog choose **Failback.**
