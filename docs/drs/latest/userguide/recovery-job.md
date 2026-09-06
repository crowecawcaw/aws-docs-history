

# Recovery job history
<a name="recovery-job"></a>

The Recovery launch history page provides an in-depth overview for operations (Jobs) performed in Elastic Disaster Recovery. 

**Topics**
+ [Recovery job history](#recovery-job-history)

## Recovery job history
<a name="recovery-job-history"></a>

The **Recovery job history** page allows you to track and manage all operations performed in Elastic Disaster Recovery. 

You can access the Recovery job history page by choosing **Recovery job history** on the left-hand navigation menu. 

![Recovery job history page showing table with job details such as ID, type, status, and start time.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-job1.png)


**Topics**
+ [Overview](#tracking-launch)
+ [Job Details](#job-history)

### Overview
<a name="tracking-launch"></a>

The Recovery job history tab shows all of the operations (referred to as "Jobs") performed on your account. Each Job corresponds to a single operation (ex. Launch Recovery instance, Launch Drill instance, etc.) Each Job is composed of one or more servers. The main Recovery job history view allows you to easily identify all key Job parameters, including: 

![Recovery job history table showing Job ID, type, initiator, status, server count, and timestamps.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-job2.png)

+  **Job ID** - The unique ID of the Job. 
+  **Job Type** - The type of Job (Recovery, Failback, or Terminate) 
+  **Initiated By** - The command or action that initiated the Job (ex. Drill, Recovery, Failback) 
+  **Status** - The status of the Job (Pending, Completed, or Started) 
+  **Servers** - The number of servers that are included in the Job. 
+  **Start Time** - The time the job was started. 
+  **Completed Time** - The time the Job was completed (blank if the job was not completed) 

To sort the Recovery job history by any column (for example, **Job ID**), click the column header. 

![Recovery job history table with Job ID column header highlighted showing sortable columns.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-job3.png)


You can search for specific Jobs by any of the available fields within the **Find launch history by property or value ** search bar. 

![Recovery job history table with search bar highlighted at top for filtering by property or value.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-job4.png)


Example: Filtered search for the values **Job type: Recovery** and **Status: Completed**, only showing completed Recovery Jobs. 

![Recovery job history table filtered by Job type: Recovery and Status: Completed.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-job5.png)


Choose **Clear filters** to clear the search results and return to the default Job History view. 

![Recovery job history filters showing Job type: Recovery and Status: Completed with Clear filters button.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-job6.png)


### Job Details
<a name="job-history"></a>

You can view a detailed breakdown of each individual job by choosing the Job ID. Choose the **Job ID** of any Job to open the Job details view. 

![Job ID drs-job000000000000014-test highlighted in red box within jobs table.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-recoveryjob-jobdetails.png)


The Job details view is composed of three sections:

![Job details page showing recovery job status, timestamps, and job log with event information.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-new-job7.png)


**Topics**
+ [Details](#job-detials)
+ [Job log](#job-joblog)
+ [Jobs - Source servers](#job-sourceservers)

#### Details
<a name="job-detials"></a>

The **Details** section shows the same information as the main Job log page, including the **Type, Status, Initiated By, Start time,** and **Completed time**. 

![Details section showing Recovery type, Completed status, Diagnostic initiator, and start time.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-recoveryjob-jobdetails3.png)


#### Job log
<a name="job-joblog"></a>

The Job log section shows a detailed log of all of the operations performed during the Job. 

![Job log table showing timestamps, events, and server details for cleanup and snapshot operations.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-recoveryjob-jobdetails-joblog.png)


You can use this section to troubleshoot any potential issues and determine in which step of the launch process they occurred. 

You can use the **Filter job log by property or value **search bar to filter the Job log. 

![Filter job log by property or value search bar with pagination controls showing pages 1, 2, and 3.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-recoveryjob-jobdetails-joblog2.png)


You can filter by a variety of properties, including **Time, Event, Source Server Id, Source server hostname, Conversion Server instance Id, Drill/Recovery instance ID,** and **Error.** 

![Properties panel showing filter options such as Time, Event, Source Server Id, and Error.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-recoveryjob-jobdetails-joblog3.png)


You can filter by multiple values at once (for example, Job log filtered by **Event: Failed to take snapshot** and a specific **Source Server Id: 7**). 

![Job log filtered by Event: Failed to take snapshot and Source Server Id: 7.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-recoveryjob-jobdetails-joblog4.png)


#### Jobs - Source servers
<a name="job-sourceservers"></a>

The Source servers section shows a list of all source servers involved in the Job and their status. 

You can use the **Filter source servers by property or value ** search bar to filter by **Hostname** or **Status**. 

![Filter source servers by property or value search bar with pagination controls.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-recoveryjob-jobdetails-joblog5.png)


Choose the Hostname of any of Source server from the list to open the Server Details view for that server. [Learn more about the Source Server details view. ](server-details.md) 

![Source servers table with server1 hostname highlighted, showing 10 servers with various statuses.](http://docs.aws.amazon.com/drs/latest/userguide/images/launchhistory-serverdetails.png)
