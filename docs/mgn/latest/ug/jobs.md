NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Review launch history

The **Launch history** tab allows you to track and manage all
of the operation performed in AWS Application Migration Service.

You can access the Launch History by choose **Launch history**
on the left-hand navigation menu.

## Overview

The Launch History tab shows all of the operations (referred to as "Jobs") performed on
your account. Each Job corresponds to a single operation (for example, Launch cutover instance,
Launch test instance, etc.) Each Job is composed of one or more servers. The main Launch History
view allows you to easily identify all key Job parameters, including:

- **Job ID** – The unique ID of the Job.
- **Job type** – The type of Job (Launch or Terminate)
- **Initiated by** – The command or action that initiated the
  job (for example, Launch cutover instances or Terminate launched instances)
- **Status** – The status of the Job (Pending, Completed, or
  Started)
- **Servers** – The number of servers that are included in the
  Job.
- **Start time** – The time the job was started.
- **Completed time** – The time the Job was completed (blank
  if the job was not completed).

You can sort the launch history by any column by clicking the column header. (for example,
sorting by **Job ID**).

You can search for specific Jobs by any of the available fields within the **Find launch history by property or value** search bar.

## Job details

To view a detailed breakdown of each individual job, choose the **Job
ID** of the specific job.

The **Job details** view is composed of 3 sections:

###### Topics

- [Details](#job-detials "#job-detials")
- [Job log](#job-joblog "#job-joblog")
- [Jobs – Source servers](#job-sourceservers "#job-sourceservers")

### Details

The **Details** section shows the same information as the
main Job log page, including the **Type, Status, Initiated by, Start
time,** and **Completed time**.

### Job log

The Job log section shows a detailed log of all of the operations performed during the
job.

Use this section to troubleshoot any potential issues and determine in which step of the
launch process they occurred.

Use the **Filter job log by property or value** search bar to
filter the job log.

You can filter by a variety of properties, including **Time, Event,
Source server Id, Source server hostname, Conversion server instance IS, Test/cutover instance
ID**, and **Error**.

You can filter by multiple values at once.

### Jobs – Source servers

The **Source servers** section shows a list of all source
servers involved in the job and their status.

You can use the **Filter source servers by property or
value** search bar to filter by **Source server name**
or **Status**.

Choose the **Source server name** of any of source server
from the list to open the Server Details view for that server. [Learn more about server details.](server-details.md "server-details.md")
