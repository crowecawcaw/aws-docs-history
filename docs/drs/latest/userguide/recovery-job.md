# Recovery job history

The Recovery launch history page provides an in-depth overview for operations (Jobs)
performed in Elastic Disaster Recovery.

###### Topics

- [Recovery job history](#recovery-job-history "#recovery-job-history")

## Recovery job history

The **Recovery job history** page allows you to track and
manage all operations performed in Elastic Disaster Recovery.

You can access the Recovery job history page by choose **Recovery
job history** on the left-hand navigation menu.

![Recovery job history table showing job details like ID, type, status, and start time.](images/drs-new-job1.png)

###### Topics

- [Overview](#tracking-launch "#tracking-launch")
- [Job Details](#job-history "#job-history")

### Overview

The Recovery job history tab shows all of the operations (referred to as "Jobs") performed
on your account. Each Job corresponds to a single operation (ex. Launch Recovery instance,
Launch Drill instance, etc.) Each Job is composed of one or more servers. The main Recovery job
history view allows you to easily identify all key Job parameters, including:

![Recovery job history table showing job details like ID, type, status, and start time.](images/drs-new-job2.png)

- **Job ID**

* The unique ID of the Job.

- **Job Type**

* The type of Job (Recovery, Failback, or
  Terminate)

- **Initiated By**

* The command or action that initiated the
  Job (ex. Drill, Recovery, Failback)

- **Status**

* The status of the Job (Pending, Completed, or
  Started)

- **Servers**

* The number of servers that are included in the
  Job.

- **Start Time**

* The time the job was started.

- **Completed Time**

* The time the Job was completed (blank
  if the job was not completed)

To sort the Recovery job history by any column (for example, **Job ID**), click the column header.

![Recovery job history table showing Job ID, Job type, Status, and other details for multiple jobs.](images/drs-new-job3.png)

You can search for specific Jobs by any of the available fields within the **Find launch history by property or value** search bar.

![Recovery job history table showing completed diagnostic jobs with start times and server counts.](images/drs-new-job4.png)

Example: Filtered search for the values
**Job type: Recovery**
and **Status: Completed**, only showing completed Recovery Jobs.

![Recovery job history table filtered to show completed Recovery jobs.](images/drs-new-job5.png)

Choose **Clear filters** to clear the search results and
return to the default Job History view.

![Recovery job history interface with applied filters and a Clear filters button highlighted.](images/drs-new-job6.png)

### Job Details

You can view a detailed breakdown of each individual job by choosing the Job ID. Choose the
**Job ID**
of any Job to open the Job details view.

![Table showing job details including Job ID, Job type, Initiator, Status, and Start time.](images/drs-recoveryjob-jobdetails.png)

The Job details view is composed of three sections:

![AWS Elastic Disaster Recovery job details showing completed recovery status and job log.](images/drs-new-job7.png)

###### Topics

- [Details](#job-detials "#job-detials")
- [Job log](#job-joblog "#job-joblog")
- [Jobs - Source servers](#job-sourceservers "#job-sourceservers")

#### Details

The **Details** section shows the same
information as the main Job log page, including the **Type,
Status, Initiated By, Start time,** and **Completed time**.

![Details table showing recovery type, completed status, diagnostic initiation, and start time.](images/drs-recoveryjob-jobdetails3.png)

#### Job log

The Job log section shows a detailed log of all of the operations performed during the
Job.

![Job log table showing events, times, and server details for a conversion process.](images/drs-recoveryjob-jobdetails-joblog.png)

You can use this section to troubleshoot any potential issues and determine in which step
of the launch process they occurred.

You can use the **Filter job log by property or value** search bar to filter the Job log.

![Search bar for filtering job log entries by property or value.](images/drs-recoveryjob-jobdetails-joblog2.png)

You can filter by a variety of properties, including **Time, Event, Source Server Id, Source server hostname, Conversion Server
instance Id, Drill/Recovery instance ID,** and **Error.**

![List of properties for filtering, including Time, Event, Source Server Id, and others.](images/drs-recoveryjob-jobdetails-joblog3.png)

You can filter by multiple values at once (for example, Job log filtered by
**Event: Failed to take snaphot** and a
specific **Source Server Id: 7**).

![Job log filtered by "Failed to take snapshot" event and Source Server Id: 7.](images/drs-recoveryjob-jobdetails-joblog4.png)

#### Jobs - Source servers

The Source servers section shows a list of all source servers involved in the Job and
their status.

You can use the **Filter source servers by property or
value** search bar to filter by **Hostname** or
**Status**.

![Search bar for filtering source servers by property or value, such as Hostname or Status.](images/drs-recoveryjob-jobdetails-joblog5.png)

Choose the Hostname of any of Source server from the list to open the Server Details view
for that server.
[Learn more about the Source Server details
view.](server-details.md "server-details.md")

![List of source servers showing hostnames and statuses, with server1 highlighted.](images/launchhistory-serverdetails.png)
