# Recovery instance details view

The recovery instance details view provides an overview of the recovery instance,
including the instance's reversed direction launch process, post-launch action runs and
data replication status. It allows you to control instance tags and the instance's
failback settings.

You can access the recovery instance details view by choosing the instance ID of a
recovery instance under the **Instance ID** column.

You can also access the recovery instance details view by selecting a recovery
instance and choosing the **View instance details** option
under the **Actions** menu.

The recovery instance information page displays the **Instance
ID** at the top.

The **Overview** panel provides an overview of the failback
process, including:

- **EC2 instance** – the ID of the recovery instance
  in EC2. Choose **View in EC2** to open the AWS EC2
  Console.
- **Pending actions** – information derived from the
  **Pending actions** column (for example,
  **Launch for failback on {region}**).
- **Replicating to source server** – the source
  server to which the recovery instance is replicating. Choose the source server
  ID to open the **Source server details view** page
  for the specific source server.
- **Launched from source server** – the source server
  from which the recovery instance was launched. Choose the source server ID to
  open the **Source server details view** page for
  the specific source server.
- **Post-launch actions status** – displays the
  status of the last post-launch actions run on this instance.
  The recovery instance details page is divided into these sections:

- **Launch dashboard** - see the current status of
  failback or reversed direction replication and launch.
- **Instance information** - view information about the underlying EC2 instance.
- **Tags** - manage the tags of the recovery instance.
- **Failback replication settings** - configure settings for failback to on-premises servers. Not relevant for in-AWS launches.
- **Post-launch actions status** - the progress or result of the last post-launch actions run.

## Launch

dashboard

The **Launch** dashboard provides a detailed overview
of the reversed direction launch process.

### Reversed

direction launch state

The **Reversed direction launch state** panel
provides an overview of the reversed direction launch process, including:

- The current state of the failback.
- **Launch target** – the server into which
  the recovery instance is launching. This indicates whether the recovery
  instance is launching into the original server or to a new server. Note
  that for in-AWS flows this value is always a new server, unless your are using the **Launch into existing instance** capability.
- **Last job ID** – the ID of the last
  failback job started for the recovery instance.
- **Last job started** – the date and time
  the last failback job was started for the recovery instance.
- **Last job finished** – the date and time
  the last failback job was finished for the recovery instance.
- **Last launch results** – the results of
  the most recent launch.

### Data

replication status

The Data replication status panel displays the current data replication status
state for the recovery instance, including:

- **Replication progress** – the progress of
  the replication of the recovery instance in percent completed.
- **Total replicated storage** – the total
  amount of storage replicated in GiB.
- **Lag** – the total Lag time, if any.
- **Backlog** – the total backlog amount and
  time to clear, if any.
- **Elapsed replication time** – time
  elapsed since replication began.
- **AWS replication agent last seen** – the
  date and time connectivity was last established between the recovery
  instance and the AWS Replication Agent.
- **Failback client last seen** – the date
  and time connectivity was last established between the recovery instance
  and the Failback client.
- **Replication start time** – and date and
  time replication was started for the recovery instance.

### Events and

metrics

The Events and metrics section contains external links to monitor your
recovery instance in AWS CloudTrail. [Learn more about monitoring DRS with
CloudTrail](logging-using-cloudtrail.md#logging-using-cloudtrail- "logging-using-cloudtrail.md#logging-using-cloudtrail-").

## Instance information

The **Instance information** tab displays general
server information, hardware, and network information:

- **Last updated**
- **AWS recovery instance ID**
- **Created in recovery job**
- **Hostname**
- **Fully qualified domain name**
- **CPUs**
- **Disks**
- **Primary network interface**
- **Operating system** information

## Tags

The Tags section displays tags that have been assigned to the server. A tag is a
label that you assign to an AWS resource. Each tag consists of a key and an optional
value. You can use tags to search and filter your resources or track your AWS costs.
Learn more about AWS tags in [Tag your Amazon EC2 resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").

Choose **Manage tags** to add or remove tags. On the
**Manage tags** page choose **Add new tag** to add a new tag. Add a tag **Key** and an optional tag **Value**.
**Save** your added tags.

To remove a tag, choose **Remove** to the right of the tag you
want to remove, and then choose **Save**.

## Failback replication

settings

The Failback replication settings tab allows you to edit various failback
replication settings for the recovery instance prior to performing a failback.

Choose **Edit** to edit the settings.

You can configure the failback replication settings for multiple recovery
instances at once. The **Selected recovery instances**
box displays the recovery instances for which you are updating the settings.

### Network

bandwidth throttling

You can control the amount of network bandwidth used for data replication per
server. By default, Elastic Disaster Recovery uses all available network
bandwidth on five concurrent connections. Choose **Throttle
bandwidth** if you want to control the transfer rate over TCP Port
1500 of data sent from your recovery instances to your source servers during
failback. On the the **Throttle network bandwidth (per
instance, in Mbps)** enter the bandwidth in Mbps.

Otherwise, choose **Do not throttle
bandwidth**.

### Use

private IP

By default, data is sent from the recovery instance to the source servers over
the public internet, using the public IP that was automatically assigned to the
replication servers. Transferred data is always encrypted in transit.

Choose the **Use private IP** option if you want
to route the replicated data from your recovery instance to your source servers
through a private network with a VPN, AWS Direct Connect, VPC peering, or
another type of existing private connection. Use this option if you want to:

- Allocate a dedicated bandwidth for replication
- Use another level of encryption
- Add another layer of security by transferring the replicated data from
  one private IP address (source) to another private IP address (on
  AWS)

###### Important

Data replication does not work unless you have already set up the VPN, AWS
Direct Connect, or VPC peering in the AWS Console.

###### Note

- If you selected the default subnet, it is highly unlikely that the
  private IP is activated for that subnet. Ensure that Private IP
  (VPN, AWS Direct Connect, or VPC peering) is activated for
  your chosen subnet to use this option.
- Choosing the **Use Private IP**
  option does not create a new private connection.

### Saving

failback replication settings

Once you have configured your failback replication settings, choose
**Save failback replication settings.**

## Post-launch actions status

The **Post-launch actions** view displays the current
run status of post-launch actions.

The status includes:

- **Order** - the running order of the action.
- **Name** - the name of the action is a link to the detailed run status in the AWS Systems Manager console.
- **Run result** – provides the current action run status.
- **Start time** – the time when the action
  script started to run. This column is empty for actions that have not yet
  started running.
- **End time** – the time when the action script
  run ended. This column is empty for actions that have not yet completed
  running.
- **Details** – error messages are displayed in
  this column.
- **Link** – provides a link to resources created by this action if there are any, or to the action run logs in the AWS Systems Manager console.
