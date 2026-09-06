

# Manage starting backlog projections in Connect Customer
<a name="capacity-planning-backlog-projections"></a>

When you set an **Average time to complete** target for the Task or Email channel, capacity planning treats that channel as asynchronous. Contacts can accumulate in a backlog instead of agents handling them immediately. To accurately estimate staffing for an asynchronous channel, capacity planning needs to know the backlog size and age at the start of the plan. Capacity planning calls this input a starting backlog projection.

Connect Customer automatically generates a starting backlog projection for each queue in your Connect Customer instance. You don't need to provide anything to use this feature. The system-generated projection estimates the backlog by weekday, queue, and channel, and Connect Customer refreshes it daily. You can upload your own values to override the system-generated projection for specific combinations of weekday, queue, and channel.

## Starting backlog projection file format
<a name="backlog-projections-file-format"></a>

Starting backlog projection files are .csv files with the following columns:
+ **Weekday**: The day of the week, for example `MONDAY`.
+ **QueueName**: The name of the queue.
+ **Channel**: The channel, either `TASK` or `EMAIL`.
+ **AgeInIntervals**: The age of the backlogged contacts, measured in 15-minute intervals.
+ **BacklogSize**: The number of backlogged contacts of that age.

When you download a merged view of the system-generated projection and your overrides, the file includes an additional **Source** column that indicates whether each row comes from the system-generated projection (`SYSTEM`) or from your override (`USER`).

## How overrides work
<a name="how-backlog-overrides-work"></a>

Overrides are tracked by a combination of weekday, queue, and channel. A single combination can have multiple rows, one for each **AgeInIntervals** value. When you work with overrides, Connect Customer treats all of the rows that share the same weekday, queue, and channel as a single group.

### How uploads merge with existing overrides
<a name="backlog-overrides-merge"></a>

Each upload merges with your existing overrides at the weekday, queue, and channel level. When an upload contains rows for a weekday, queue, and channel combination, those rows replace all previously uploaded rows for that combination. Combinations that you don't include in the upload are left unchanged.

For example, suppose you have already uploaded the following overrides.


| Weekday | QueueName | Channel | AgeInIntervals | BacklogSize | 
| --- | --- | --- | --- | --- | 
| MONDAY | SalesQueue | EMAIL | 1 | 20 | 
| MONDAY | SalesQueue | EMAIL | 2 | 15 | 
| TUESDAY | SalesQueue | TASK | 1 | 5 | 

You then upload the following file.


| Weekday | QueueName | Channel | AgeInIntervals | BacklogSize | 
| --- | --- | --- | --- | --- | 
| MONDAY | SalesQueue | EMAIL | 1 | 30 | 
| MONDAY | SalesQueue | EMAIL | 3 | 10 | 

After the upload, your overrides are as follows. The `MONDAY`, `SalesQueue`, `EMAIL` combination is replaced entirely by the rows in the new upload. The previous row for **AgeInIntervals** `2` is removed because the upload didn't include it. The `TUESDAY`, `SalesQueue`, `TASK` combination is unchanged because the upload didn't include it.


| Weekday | QueueName | Channel | AgeInIntervals | BacklogSize | 
| --- | --- | --- | --- | --- | 
| MONDAY | SalesQueue | EMAIL | 1 | 30 | 
| MONDAY | SalesQueue | EMAIL | 3 | 10 | 
| TUESDAY | SalesQueue | TASK | 1 | 5 | 

#### Clear an override
<a name="clear-backlog-override"></a>

To clear your override for a specific weekday, queue, and channel, upload a row for that combination with a blank **AgeInIntervals** value and a blank **BacklogSize** value. After you clear an override, capacity planning uses the system-generated projection for that combination when you generate a plan.

For example, to clear your override for the `MONDAY`, `SalesQueue`, `EMAIL` combination, upload the following row.


| Weekday | QueueName | Channel | AgeInIntervals | BacklogSize | 
| --- | --- | --- | --- | --- | 
| MONDAY | SalesQueue | EMAIL |  |  | 

The blank **AgeInIntervals** and **BacklogSize** values remove all of your override rows for the `MONDAY`, `SalesQueue`, `EMAIL` combination.

### How overrides replace the system-generated projection
<a name="backlog-overrides-replace-system"></a>

When you generate a plan, Connect Customer selects projections for the queues in your forecast group and the plan's start weekday. It then merges your overrides with the system-generated projection, grouped by weekday, queue, and channel. If an override exists for a combination, Connect Customer uses those override rows. If no override exists, Connect Customer uses the system-generated rows. If neither exists, Connect Customer uses a starting backlog of 0.

For example, suppose the system-generated projection for `MONDAY`, `SalesQueue`, `EMAIL` is as follows.


| Weekday | QueueName | Channel | AgeInIntervals | BacklogSize | 
| --- | --- | --- | --- | --- | 
| MONDAY | SalesQueue | EMAIL | 1 | 100 | 
| MONDAY | SalesQueue | EMAIL | 2 | 80 | 
| MONDAY | SalesQueue | EMAIL | 4 | 40 | 

And you have uploaded the following override for the same combination.


| Weekday | QueueName | Channel | AgeInIntervals | BacklogSize | 
| --- | --- | --- | --- | --- | 
| MONDAY | SalesQueue | EMAIL | 1 | 30 | 
| MONDAY | SalesQueue | EMAIL | 3 | 10 | 

When you generate the plan, Connect Customer uses only the override rows for `MONDAY`, `SalesQueue`, `EMAIL`. It ignores the system-generated rows for that combination, including the rows for **AgeInIntervals** `2` and `4`.


| Weekday | QueueName | Channel | AgeInIntervals | BacklogSize | 
| --- | --- | --- | --- | --- | 
| MONDAY | SalesQueue | EMAIL | 1 | 30 | 
| MONDAY | SalesQueue | EMAIL | 3 | 10 | 

For any weekday, queue, and channel combination that you have not overridden, Connect Customer uses the system-generated projection.

## Download or override projections
<a name="how-to-manage-backlog-projections"></a>

You download and upload starting backlog projections on the **Import Data** tab.

1. Sign in to the Connect Customer admin website using an account that has security profile permissions for **Analytics** and **Capacity planning - Edit**.

   For more information, see [Assign permissions](required-optimization-permissions.md). 

1. On the Connect Customer navigation menu, choose **Analytics and optimization**, **Capacity Planning**.

1. Choose the **Import Data** tab.

1. To download projections, choose **Download data**, and then choose one of the following:

   1. **Starting backlog projections (system)**: The latest system-generated projection.

   1. **Starting backlog projections (merged system and overrides)**: A merged view of the system-generated projection and your overrides, including the **Source** column.

   1. **Starting backlog projections (overrides)**: Your current overrides.

   The following image shows the **Download data** menu with the starting backlog projection options.  
![Download data options for starting backlog projections: system, merged system and overrides, and overrides only.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-backlog-download.png)

1. To override projections, enter your values in a .csv file, using the columns described in [Starting backlog projection file format](#backlog-projections-file-format). Choose **Upload data**, **Starting backlog projections**, and then upload the file.

   The following image shows the **Upload data** menu with the **Starting backlog projections** option.  
![Upload data option for Starting backlog projections.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-backlog-upload.png)

   Each upload merges with your existing overrides at the weekday, queue, and channel level. For more information, see [How overrides work](#how-backlog-overrides-work).