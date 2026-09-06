

# Scheduling data in the Connect Customer analytics data lake
<a name="data-lake-scheduling"></a>

This topic details the content in the Connect Customer data lake scheduling tables. The tables list the column, type, and description of the content.

There are two ways to access the analytics data lake and configure data to be shared: 
+ [Option 1: Use the Connect Customer console](access-datalake.md#option1-configure-data-to-be-shared)
+ [Option 2: Use CLI or CloudShell](access-datalake.md#option2-configure-data-to-be-shared)

If you are unable to access the scheduling tables by using Option 1, try using Option 2.

**Topics**
+ [Staff scheduling profile](#data-lake-staff-scheduling-profile)
+ [Shift activities](#data-lake-shift-activities)
+ [Shift profiles](#data-lake-shift-profiles)
+ [Staffing groups](#data-lake-staffing-groups)
+ [Staffing groups - Forecast groups](#data-lake-staffing-groups-forecast-groups)
+ [Staffing groups - Supervisors](#data-lake-staffing-groups-supervisors)
+ [Staff shifts](#staff-shifts)
+ [Staff shift activities](#data-lake-staff-shift-activities)
+ [Staff timeoff balance changes](#data-lake-staff-timeoff-balance-changes)
+ [Staff timeoffs](#data-lake-staff-timeoffs)
+ [Staff timeoff intervals](#data-lake-staff-timeoff-intervals)
+ [Staff demand group](#data-lake-staff_demand_group)
+ [Staffing groups demand group](#data-lake-staffing-groups-demand-groups)
+ [Staff shift activity allocation](#data-lake-staff-shift-activity-allocation)
+ [Schedule metrics](#data-lake-schedule-metrics)
+ [Schedule goals](#data-lake-schedule-goals)
+ [Shift rotation patterns](#data-lake-shift-rotation-patterns)
+ [Shift rotation steps](#data-lake-shift-rotation-steps)
+ [Data schema](#data-lake-data-schema)
+ [Sample queries](#data-lake-sample-queries)

## Staff scheduling profile
<a name="data-lake-staff-scheduling-profile"></a>

**Table name:** `staff_scheduling_profile`

**Description:** Contains agent scheduling configuration including staffing group assignment, shift profile or rotation pattern assignment, and scheduling validity window.

**Primary key:** `instance_id, agent_arn, staff_scheduling_profile_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `agent_arn` — Joins to Agent Event, Contact Record, staff\_shifts, staff\_timeoffs, users (as `user_arn`)
+ `staffing_group_arn` — Joins to staffing\_groups, staffing\_group\_forecast\_groups, staffing\_group\_supervisors
+ `shift_profile_arn` — Joins to shift\_profiles
+ `shift_rotation_pattern_arn` — Joins to shift\_rotation\_patterns


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance. | 
|  agent\_arn  |  string |  No  |  The ARN of the Agent.  | 
|  staff\_scheduling\_profile\_version  |  bigint  |  No  |  The Staff Scheduling Profile Version.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance. | 
|  staffing\_group\_arn  |  string  |  Yes  |  The ARN of the Staffing Group to which the Agent is assigned.  | 
|  start\_timestamp  |  Timestamp  |  Yes  |  StartTimestamp for the Agent configured in Staff Rules (schedules are generated only after this Timestamp).  | 
|  end\_timestamp  |  Timestamp  |  Yes  |  EndTimestamp for the Agent configured in Staff Rules (schedules are not generated beyond this Timestamp). | 
|  shift\_profile\_arn  |  string  |  Yes  |  The ARN of the Shift Profile assigned to the Agent in Staff Rules. Mutually exclusive with Shift Rotation Pattern.  | 
|  shift\_rotation\_pattern\_arn  |  string  |  Yes  |  The ARN of the Shift Rotation Pattern assigned to the Agent in Staff Rules. Mutually exclusive with Shift Profile.  | 
|  shift\_rotation\_start\_step\_id  |  bigint  |  Yes  |  The step ID where the Agent begins in the assigned Shift Rotation Pattern.  | 
|  timezone  |  string  |  Yes  |  Timezone configured for the Agent.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to True if the Agent is deleted. Else set to False.  | 
|  last\_updated\_by  |  string  |  Yes  |  The ARN of the user who updated the Staff Scheduling Profile.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the Staff Scheduling Profile was created/updated/deleted.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.  | 

## Shift activities
<a name="data-lake-shift-activities"></a>

**Table name:** `shift_activities`

**Description:** Defines the types of activities that can be assigned within shifts, including activity type (productive, non-productive, leave), adherence tracking, and paid status.

**Primary key:** `instance_id, shift_activity_arn, shift_activity_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `shift_activity_arn` — Joins to staff\_shift\_activities, staff\_timeoff\_balance\_changes, staff\_timeoffs


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  shift\_activity\_arn  |  string  |  No  |  The ARN of the Shift Activity.  | 
|  shift\_activity\_version  |  bigint  |  No  |  The Shift Activity Version.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  shift\_activity\_name  |  string  |  Yes  |  Name of the Shift Activity.  | 
|  type  |  string  |  Yes  |  Type of the Shift Activity. The possible values are: PRODUCTIVE, NON\_PRODUCTIVE, and LEAVE.  | 
|  sub\_type  |  string  |  Yes  | The sub-type of the Shift Activity. This is only valid for NON\_PRODUCTIVE type activities. The possible values are: BREAK\_OR\_MEAL and NONE.  | 
|  is\_adherence\_tracked  |  Boolean  |  Yes  |  Set to True if the Shift Activity is configured for Adherence tracking. Else set to False.  | 
|  is\_paid  |  Boolean  |  Yes  |  Set to True if the Shift Activity is configured as Paid. Else set to False.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to True if the Shift Activity is deleted. Else set to False.  | 
|  last\_updated\_by  |  string  |  Yes  |  The ARN of the user who created/updated the Shift Activity.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  | The Timestamp when the Shift Activity was created/updated/deleted.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  | The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Shift profiles
<a name="data-lake-shift-profiles"></a>

**Table name:** `shift_profiles`

**Description:** Defines shift profile templates that can be assigned to agents, specifying the shift pattern for schedule generation.

**Primary key:** `instance_id, shift_profile_arn, shift_profile_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `shift_profile_arn` — Joins to staff\_scheduling\_profile, shift\_rotation\_steps


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  shift\_profile\_arn  |  string  |  No  |  The ARN of the Shift Profile.  | 
|  shift\_profile\_version  |  bigint  |  No  |  The Shift Profile Version.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  shift\_profile\_name  |  string  |  Yes  |  The name of the Shift Profile.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to True if the Shift Profile is deleted. Else set to False.  | 
|  last\_updated\_by  |  string  |  Yes  |  The ARN of the user who created/updated the Shift Profile.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  | The Timestamp when the Shift Profile was created/updated/deleted.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  | The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Staffing groups
<a name="data-lake-staffing-groups"></a>

**Table name:** `staffing_groups`

**Description:** Defines staffing groups that organize agents for scheduling purposes, serving as the primary organizational unit for workforce management.

**Primary key:** `instance_id, staffing_group_arn, staffing_group_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `staffing_group_arn` — Joins to staff\_scheduling\_profile, staffing\_group\_forecast\_groups, staffing\_group\_supervisors, staffing\_group\_demand\_group


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  staffing\_group\_arn  |  string  |  No  |  The ARN of the Staffing Group.  | 
|  staffing\_group\_version  |  bigint  |  No  |  The Staffing Group Version.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  staffing\_group\_name  |  string  |  Yes  |  The name of the Staffing Group.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to True if the Staffing Group is deleted. Else set to False.  | 
|  last\_updated\_by  |  string  |  Yes  |  The ARN of the user who created/updated the Staffing Group.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the Staffing Group was created/updated/deleted.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  | The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Staffing groups - Forecast groups
<a name="data-lake-staffing-groups-forecast-groups"></a>

**Table name:** `staffing_group_forecast_groups`

**Description:** Maps the association between staffing groups and forecast groups, linking workforce capacity to demand forecasting.

**Primary key:** `instance_id, staffing_group_arn, staffing_group_version, forecast_group_arn`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `staffing_group_arn, staffing_group_version` — Joins to staffing\_groups
+ `forecast_group_arn` — Joins to schedule\_metrics, schedule\_goals, staff\_shift\_activity\_allocations


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  staffing\_group\_arn  |  string  |  No  |  The ARN of the Staffing Group.  | 
|  staffing\_group\_version  |  bigint  |  No  |  The Staffing Group Version.  | 
|  forecast\_group\_arn  |  string  |  No  |  The ARN of the Forecast Group associated to the Staffing Group.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to False when the StaffingGroup-ForecastGroup association is valid.  | 
|  last\_updated\_by  |  string  |  Yes  |  The ARN of the user who created/updated the Staffing Group.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the Staffing Group was created/updated.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Staffing groups - Supervisors
<a name="data-lake-staffing-groups-supervisors"></a>

**Table name:** `staffing_group_supervisors`

**Description:** Maps supervisor associations to staffing groups, tracking which supervisors are responsible for each staffing group.

**Primary key:** `instance_id, staffing_group_arn, staffing_group_version, supervisor_arn`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `staffing_group_arn, staffing_group_version` — Joins to staffing\_groups
+ `supervisor_arn` — Joins to Agent Event (as agent\_arn), Contact Record (as agent\_arn)


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  staffing\_group\_arn  |  string  |  No  |  The ARN of the Staffing Group.  | 
|  staffing\_group\_version  |  bigint  |  No  |  The Staffing Group Version.  | 
|  supervisor\_arn  |  string  |  No  |  The Agent ARN of the Supervisor associated to the Staffing Group.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to False when the StaffingGroup-ForecastGroup association is valid.  | 
|  last\_updated\_by  |  string  |  Yes  |  The ARN of the user who created/updated the Staffing Group.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the Staffing Group was created/updated.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Staff shifts
<a name="staff-shifts"></a>

**Table name:** `staff_shifts`

**Description:** Contains individual shift instances assigned to agents, including shift start and end times and creation metadata.

**Primary key:** `instance_id, shift_id, shift_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `shift_id, shift_version` — Joins to staff\_shift\_activities, staff\_shift\_activity\_allocations
+ `agent_arn` — Joins to staff\_scheduling\_profile, Agent Event, Contact Record, users (as `user_arn`)


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  shift\_id  |  string  |  No  |  The ID of the Shift. | 
|  shift\_version  |  bigint  |  No  |  The Shift Version.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  agent\_arn  |  string  |  Yes  |  The ARN of the Agent.  | 
|  shift\_start\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the Shift Starts.  | 
|  shift\_end\_timestamp  |  Timestamp  |  Yes  | The Timestamp when the Shift Ends.  | 
|  created\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the Shift was Created.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to True if the Shift is deleted. Else set to False.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the Shift was created/updated/deleted.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  | The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Staff shift activities
<a name="data-lake-staff-shift-activities"></a>

**Table name:** `staff_shift_activities`

**Description:** Contains individual activity blocks within a shift, including activity start and end times, overtime flags, and activity status.

**Primary key:** `instance_id, shift_id, shift_version, activity_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `shift_id, shift_version` — Joins to staff\_shifts
+ `activity_id` — Joins to staff\_shift\_activity\_allocations
+ `shift_activity_arn` — Joins to shift\_activities


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  shift\_id  |  string  |  No  |  The ID of the Shift. | 
|  shift\_version  |  bigint  |  No  |  The Shift Version.  | 
|  activity\_id  |  string  |  No  |  The ID of the Activity.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  activity\_start\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the activity starts.  | 
|  activity\_end\_timestamp  |  Timestamp  |  Yes  | The Timestamp when the activity ends.  | 
|  shift\_activity\_arn  |  string  |  Yes  |  The ARN of the Shift Activity. If the shift\_activity\_arn is null, then it indicates 'Work' activity.  | 
|  activity\_status  |  string  |  Yes  |  Status of the Activity. This is set to INACTIVE if the activity overlaps with a timeoff.  | 
|  is\_overtime  |  Boolean  |  Yes  |  Set to True if the Activity is part of Overtime. Else set to False.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to False when the Shift Activities are valid.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  | The Timestamp when the Shift was created/updated.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Staff timeoff balance changes
<a name="data-lake-staff-timeoff-balance-changes"></a>

**Table name:** `staff_timeoff_balance_changes`

**Description:** Tracks time-off balance changes for agents, recording credits and deductions from various sources including uploads, requests, and schedule publishing.

**Primary key:** `instance_id, agent_arn, shift_activity_arn, timeoff_balance_version`

**Partition key:** `last_created_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `agent_arn` — Joins to staff\_scheduling\_profile, staff\_shifts, Agent Event, Contact Record
+ `shift_activity_arn` — Joins to shift\_activities
+ `timeoff_id` — Joins to staff\_timeoffs


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  aws\_account\_id  |  string  |  Yes  |  The ID of the AWS account.  | 
|  agent\_arn  |  string  |  No  |  The ARN of the agent.  | 
|  shift\_activity\_arn  |  string  |  No  |  The ARN of the Shift Activity this balance is allocated to.  | 
|  timeoff\_balance\_version  |  bigint  |  No  |  The Time Off balance version, an incrementing number to denote order of changes.  | 
|  balance\_update\_source  |  string  |  Yes  |  Source of the balance update. The possible values are TIME\_OFF\_BALANCE\_UPLOAD, CONNECT\_TIME\_OFF\_REQUEST, SCHEDULE\_PUBLISH, CSV\_TIME\_OFF\_BALANCE\_DELETION, TIME\_OFF\_BALANCE\_BACKFILL, SYSTEM\_UPDATE  | 
|  timeoff\_id  |  string  |  Yes  |  The ID of the Time Off that caused this balance change, if one exists.  | 
|  last\_updated\_by  |  string  |  Yes  |  The ARN of the agent who caused this balance change, if one exists.  | 
|  balance\_change\_in\_hours  |  double  |  Yes  |  Amount of Time Off balance updated through this change in hours. If this value is positive, this change is crediting Time Off balance. If this value is negative, this change is deducting Time Off balance. This value is undefined for any balance upload and deletion events.  | 
|  remaining\_balance\_in\_hours  |  double  |  Yes  |  Remaining Time Off balance hours after this change event. This value is undefined for any balance deletion event.  | 
|  last\_created\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the Time Off balance change record was created.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Staff timeoffs
<a name="data-lake-staff-timeoffs"></a>

**Table name:** `staff_timeoffs`

**Description:** Records time-off requests and approvals for agents, including status tracking through the approval workflow and effective hours.

**Primary key:** `instance_id, timeoff_id, agent_arn, timeoff_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `timeoff_id, timeoff_version` — Joins to staff\_timeoff\_intervals
+ `agent_arn` — Joins to staff\_scheduling\_profile, staff\_shifts, Agent Event, Contact Record
+ `shift_activity_arn` — Joins to shift\_activities


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  timeoff\_id  |  string  |  No  |  The ID of the Time Off.  | 
|  agent\_arn  |  string  |  No  |  The ARN of the Agent.  | 
|  timeoff\_version  |  bigint  |  No  |  The Time Off Version.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  timeoff\_type  |  string  |  Yes  |  Type of Time Off. The possible values are: TIME\_OFF and VOLUNTARY\_TIME\_OFF.  | 
|  timeoff\_start\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the Time Off starts.  | 
|  timeoff\_end\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the Time Off ends.  | 
|  timeoff\_status  |  string  |  Yes  |  Status of the Time Off. The possible values are: PENDING\_CREATE, PENDING\_UPDATE, PENDING\_CANCEL, PENDING\_ACCEPT, PENDING\_APPROVE, PENDING\_DECLINE, APPROVED, ACCEPTED, REJECTED, CANCELLED, WAITING\_ACCEPT, and WAITING\_APPROVE. The WAITING statuses indicate timeoff is waiting on User action. PENDING statuses indicate timeoff is waiting for system processing of a user action.  | 
|  shift\_activity\_arn  |  string  |  Yes  |  The ARN of the Shift Activity used for the Timeoff.  | 
|  effective\_timeoff\_hours  |  double  |  Yes  |  Total effective Time Off hours. Effective timeoff hours are calculated based on [timeoff deduction logic](https://docs.aws.amazon.com/connect/latest/adminguide/upload-timeoff-balance.html#how-system-calculates-time-off-deductions). This is only set for TIME\_OFF type.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the Time Off was created/updated/deleted.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.  | 

## Staff timeoff intervals
<a name="data-lake-staff-timeoff-intervals"></a>

**Table name:** `staff_timeoff_intervals`

**Description:** Contains the individual time intervals within a time-off request, breaking multi-day or multi-period time-off into discrete intervals with effective hours per interval.

**Primary key:** `instance_id, timeoff_id, timeoff_version, interval_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `timeoff_id, timeoff_version` — Joins to staff\_timeoffs


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  timeoff\_id  |  string  |  No  |  The ID of the Time Off.  | 
|  timeoff\_version  |  bigint  |  No  |  The Time Off Version.  | 
|  interval\_id  |  string  |  No  |  The ID of the Time Off Interval.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  timeoff\_interval\_start\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the specific interval of Time Off starts.  | 
|  timeoff\_interval\_end\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the specific interval of Time Off ends.  | 
|  interval\_effective\_timeoff\_hours  |  double  |  Yes  |  Effective Time Off hours for this specific interval of Time Off. Effective timeoff hours are calculated based on [timeoff deduction logic](https://docs.aws.amazon.com/connect/latest/adminguide/upload-timeoff-balance.html#how-system-calculates-time-off-deductions).  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the Time Off was created/updated/deleted.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.  | 

## Staff demand group
<a name="data-lake-staff_demand_group"></a>

**Table name:** `staff_demand_group`

**Description:** Maps agents to demand groups with priority assignments, supporting both staffing group-level defaults and agent-level overrides for demand allocation.

**Primary key:** `instance_id, agent_arn, demand_group_arn, staff_demand_group_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `agent_arn` — Joins to staff\_scheduling\_profile, staff\_shifts, Agent Event, Contact Record
+ `demand_group_arn` — Joins to staffing\_group\_demand\_group, staff\_shift\_activity\_allocations


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
| instance\_id  | string  |  No  | The ID of the Connect Customer instance.  | 
| agent\_arn  | string  |  No  | The ARN of the agent. | 
| demand\_group\_arn  | string  |  No  | The ARN of the demand group.  | 
| staff\_demand\_group\_version  | Long  |  No  | Version for this agent to demand group association  | 
| priority  | string  |  Yes  | Priority of the demand group for this agent. Can be LOW, MEDIUM or HIGH | 
| instance\_arn  | string  |  Yes  | The ARN of the Connect Customer instance. | 
| is\_override  | Boolean  |  Yes  | Set to 'true' if this is Agent to Demand Group association is Agent level override. | 
| is\_deleted  | Boolean  |  Yes  | Set to true if agent to demand group association is deleted. | 
| last\_updated\_by  | string  |  Yes  | The ARN of the user who created/updated the Agent to Demand Group association. | 
| last\_updated\_timestamp  | Timestamp  |  Yes  | The Timestamp when the agent to demand group association was created/updated. | 
| data\_lake\_last\_processed\_timestamp  | Timestamp  |  Yes  | The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness. | 

## Staffing groups demand group
<a name="data-lake-staffing-groups-demand-groups"></a>

**Table name:** `staffing_group_demand_group`

**Description:** Maps the association between staffing groups and demand groups with priority, linking organizational units to demand allocation targets.

**Primary key:** `instance_id, staffing_group_arn, demand_group_arn, staffing_group_demand_group_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `staffing_group_arn` — Joins to staffing\_groups, staff\_scheduling\_profile
+ `demand_group_arn` — Joins to staff\_demand\_group, staff\_shift\_activity\_allocations


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  staffing\_group\_arn  |  string  |  No  |  The ARN of the Staffing Group.  | 
|  demand\_group\_arn  |  string  |  No  |  The ARN of the demand group.  | 
|  staffing\_group\_demand\_group\_version  |  Long  |  No  | Version for this Staffing Group to Demand Group association  | 
|  priority  |  string  |  Yes  |  Priority of the Demand Group for this Staffing Group. Can be LOW, MEDIUM or HIGH | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance. | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to true if the staffing group to demand group association is deleted. | 
|  last\_updated\_by  |  string  |  Yes  |  The ARN of the user who created/updated the Staffing Group to Demand Group association. | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the staffing group to demand group association was created/updated/deleted. | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness. | 

## Staff shift activity allocation
<a name="data-lake-staff-shift-activity-allocation"></a>

**Table name:** `staff_shift_activity_allocations`

**Description:** Records the percentage allocation of shift activities to demand groups, enabling proportional assignment of agent capacity across multiple demand groups within a single activity.

**Primary key:** `instance_id, shift_id, shift_version, activity_id, demand_group_arn`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `shift_id, shift_version` — Joins to staff\_shifts, staff\_shift\_activities
+ `activity_id` — Joins to staff\_shift\_activities
+ `demand_group_arn` — Joins to staff\_demand\_group, staffing\_group\_demand\_group
+ `forecast_group_arn` — Joins to staffing\_group\_forecast\_groups (as forecast\_group\_arn)


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  shift\_id  |  string  |  No  |  The ID of the shift. | 
|  shift\_version  |  Long  |  No  |  The Shift Version. | 
|  activity\_id  |  string  |  No  |  The ID of the activity. | 
|  demand\_group\_arn  |  string  |  No  |  The ARN of the demand group.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  forecast\_group\_arn  |  string  |  Yes  |  The ARN of the forecast group.  | 
|  allocation\_percentage  |  double  |  Yes  |  Percentage allocation of the Activity to the Demand Group. | 
|  is\_deleted  |  Boolean  |  Yes  |  Set to False when the StaffingGroup-ForecastGroupassociation is valid.  | 
|  last\_updated\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when the Staffing Group was created/updated. | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.  | 

## Schedule metrics
<a name="data-lake-schedule-metrics"></a>

**Table name:** `schedule_metrics`

**Description:** Contains schedule performance metrics by interval, including required versus scheduled agent counts, occupancy, service level percentage, and average speed of answer.

**Primary key:** `instance_id, metric_id, interval_start_timestamp`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `entity_arn` — Joins to staffing\_group\_forecast\_groups (as forecast\_group\_arn), staff\_demand\_group (as demand\_group\_arn)


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| instance\_id | string |  No  | The ARN of the Amazon Connect instance. | 
| instance\_arn | string |  Yes  | The ID of the Amazon Connect instance. | 
| metric\_id | string |  No  | Unique identifier for the metric value | 
| aws\_account\_id | string |  Yes  | The ID of the AWS account. | 
| entity\_type | string |  Yes  | Denotes whether the metric is for a forecast group or demand group. | 
| entity\_arn | string |  Yes  | Arn of the forecast group or demand group | 
| channel | string |  Yes  | Denotes the media channel like Voice, chat. If the row contains metrics that are not channel level, then it's populated as ALL | 
| interval\_start\_timestamp | timestamp |  No  | Timestamp denoting the start of the interval | 
| required\_agent\_count | float |  Yes  | Denotes the required agents count | 
| scheduled\_agent\_count | float |  Yes  | Denotes the scheduled agents count | 
| scheduled\_occupancy | float |  Yes  | Denotes the occupancy percentage | 
| scheduled\_service\_level\_percentage | float |  Yes  | Denotes the projected service level percentage based on scheduled headcount | 
| service\_level\_seconds | integer |  Yes  | Denotes the service level seconds | 
| scheduled\_average\_speed\_of\_answer | float |  Yes  | Denotes the projected average speed of answer in seconds based on scheduled headcount | 
| is\_deleted | boolean |  Yes  | Denotes whether the metric is deleted | 
| last\_updated\_timestamp | timestamp |  Yes  | The Timestamp when the metric record was created. | 
| data\_lake\_last\_processed\_timestamp | timestamp |  Yes  | Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 
| projected\_average\_time\_to\_complete | float |  Yes  | Denotes the average time to complete in hours | 
| projected\_backlog | integer |  Yes  | Denotes the backlog items | 

## Schedule goals
<a name="data-lake-schedule-goals"></a>

**Table name:** `schedule_goals`

**Description:** Stores service level goals for scheduling, including target service level percentage, service level seconds, and average speed of answer for forecast or demand groups.

**Primary key:** `instance_id, goal_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `entity_arn` — Joins to staffing\_group\_forecast\_groups (as forecast\_group\_arn), staff\_demand\_group (as demand\_group\_arn)


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| instance\_id | string |  No  | The ARN of the Amazon Connect instance. | 
| instance\_arn | string |  Yes  | The ID of the Amazon Connect instance. | 
| goal\_id | string |  No  | Unique identifier for the goal value | 
| aws\_account\_id | string |  Yes  | The ID of the AWS account. | 
| entity\_type | string |  Yes  | Denotes whether the goal is for a forecast group or demand group. | 
| entity\_arn | string |  Yes  | Arn of the forecast group or demand group | 
| channel | string |  Yes  | Denotes the media channel like Voice, chat. | 
| start\_date\_timestamp | timestamp |  Yes  | Timestamp denoting start of the goal | 
| end\_date\_timestamp | timestamp |  Yes  | Timestamp denoting end of the goal | 
| goal\_service\_level\_percentage | float |  Yes  | Denotes the goal service level percentage | 
| goal\_service\_level\_seconds | integer |  Yes  | Denotes the service level seconds | 
| goal\_average\_speed\_of\_answer | float |  Yes  | Denotes the average speed of answer in seconds | 
| is\_deleted | boolean |  Yes  | Denotes whether the goal is deleted | 
| last\_updated\_timestamp | timestamp |  Yes  | The Timestamp when the goals record was created. | 
| data\_lake\_last\_processed\_timestamp | timestamp |  Yes  | Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 
| goal\_average\_time\_to\_complete | float |  Yes  | Denotes the average time to complete in hours. | 

## Shift rotation patterns
<a name="data-lake-shift-rotation-patterns"></a>

**Table name:** `shift_rotation_patterns`

**Description:** Defines shift rotation pattern configurations that cycle agents through different shift profiles over time, with a configurable start date.

**Primary key:** `instance_id, shift_rotation_pattern_arn, shift_rotation_pattern_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `shift_rotation_pattern_arn, shift_rotation_pattern_version` — Joins to shift\_rotation\_steps
+ `shift_rotation_pattern_arn` — Joins to staff\_scheduling\_profile


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| instance\_id | string |  No  | The ID of the Connect Customer instance. | 
| shift\_rotation\_pattern\_arn | string |  No  | The ARN of the Shift Rotation Pattern. | 
| shift\_rotation\_pattern\_version | bigint |  No  | The Shift Rotation Pattern Version. | 
| instance\_arn | string |  Yes  | The ARN of the Connect Customer instance. | 
| shift\_rotation\_pattern\_name | string |  Yes  | The name of the Shift Rotation Pattern. | 
| start\_date | string |  Yes  | The start date of the Shift Rotation Pattern in yyyy-mm-dd format. | 
| is\_deleted | Boolean |  Yes  | Set to True if the Shift Rotation Pattern is deleted. Else set to False. | 
| last\_updated\_by | string |  Yes  | The ARN of the user who created/updated/deleted the Shift Rotation Pattern. | 
| last\_updated\_timestamp | Timestamp |  Yes  | The Timestamp when the Shift Rotation Pattern was created/updated/deleted. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 

## Shift rotation steps
<a name="data-lake-shift-rotation-steps"></a>

**Table name:** `shift_rotation_steps`

**Description:** Defines the individual steps within a shift rotation pattern, each associating a shift profile with a duration in weeks (up to 52 steps per rotation).

**Primary key:** `instance_id, shift_rotation_pattern_arn, shift_rotation_pattern_version, step_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `shift_rotation_pattern_arn, shift_rotation_pattern_version` — Joins to shift\_rotation\_patterns
+ `shift_profile_arn` — Joins to shift\_profiles


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| instance\_id | string |  No  | The ID of the Connect Customer instance. | 
| shift\_rotation\_pattern\_arn | string |  No  | The ARN of the Shift Rotation Pattern. | 
| shift\_rotation\_pattern\_version | bigint |  No  | The Shift Rotation Pattern Version. | 
| step\_id | bigint |  No  | The ID of the step within the Shift Rotation Pattern. Steps are numbered sequentially (1, 2, 3, ... up to 52). | 
| instance\_arn | string |  Yes  | The ARN of the Connect Customer instance. | 
| shift\_profile\_arn | string |  Yes  | The ARN of the Shift Profile associated with the rotation step. | 
| duration | bigint |  Yes  | The duration of the rotation step in weeks. | 
| is\_deleted | Boolean |  Yes  | Set to False when the Shift Rotation Step is valid. | 
| last\_updated\_by | string |  Yes  | The ARN of the user who created/updated the Shift Rotation Pattern. | 
| last\_updated\_timestamp | Timestamp |  Yes  | The Timestamp when the Shift Rotation Pattern was created/updated. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 

## Data schema
<a name="data-lake-data-schema"></a>

Following is an entity relationship diagram that shows the structure and relationships between scheduling tables in the Connect Customer data lake. 

 Each table displays its primary keys and attributes with their data types. The diagram illustrates how these tables relate to each other through foreign key relationships, providing a comprehensive view of the scheduling data model.

![An entity relationship diagram that shows the structure and relationships between scheduling tables.](http://docs.aws.amazon.com/connect/latest/adminguide/images/data-lake-scheduling-tables-overview-1.png)


## Sample queries
<a name="data-lake-sample-queries"></a>

### 1. Query to get all the Scheduled Shift Activities of the Agents working on a specific Forecast Group
<a name="query1"></a>

`SELECT * FROM agent_scheduled_shift_activities_view where forecast_group_name = 'AnyDepartmentForecastGroup'` 

Complete the following steps to create `agent_scheduled_shift_activities_view` mentioned above.

 **Step 1: Create a view to get supervisor names** 

```
CREATE OR REPLACE VIEW "latest_supervisor_names_view" AS
SELECT
  staffing_group_arn
, array_agg(supervisor_name ORDER BY supervisor_name ASC) supervisor_names
FROM
  (
   SELECT
     s.staffing_group_arn
   , CONCAT(u.first_name, ' ', u.last_name) supervisor_name
   FROM
     ((
      SELECT
        staffing_group_arn
      , supervisor_arn
      FROM
        (
         SELECT
           *
         , RANK() OVER (PARTITION BY staffing_group_arn ORDER BY staffing_group_version DESC) recency
         FROM
           staffing_group_supervisors
         WHERE (instance_id = 'YourAmazonConnectInstanceId')
      )  t
      WHERE (recency = 1)
   )  s
   INNER JOIN USERS u ON (s.supervisor_arn = u.user_arn))
)
GROUP BY staffing_group_arn
```

 **Step 2: Create a view to get the staffing group and forecast group associated with an agent** 

```
CREATE OR REPLACE VIEW "latest_agent_staffing_group_forecast_group_view" AS
WITH
  latest_staff_scheduling_profile AS (
   SELECT
     agent_arn
   , staffing_group_arn
   , last_updated_timestamp
   FROM
     (
      SELECT
        *
      , RANK() OVER (PARTITION BY agent_arn ORDER BY staff_scheduling_profile_version DESC) recency
      FROM
        staff_scheduling_profile
      WHERE ((instance_id = 'YourAmazonConnectInstanceId') AND (is_deleted = false))
   )  t
   WHERE (recency = 1)
)
, latest_staffing_groups AS (
   SELECT
     staffing_group_name
   , staffing_group_arn
   FROM
     (
      SELECT
        *
      , RANK() OVER (PARTITION BY staffing_group_arn ORDER BY staffing_group_version DESC) recency
      FROM
        staffing_groups
      WHERE (instance_id = 'YourAmazonConnectInstanceId')
   )  t
   WHERE (recency = 1)
)
, latest_forecast_groups AS (
   SELECT
     forecast_group_arn
   , forecast_group_name
   FROM
     (
      SELECT
        *
      , RANK() OVER (PARTITION BY forecast_group_arn ORDER BY forecast_group_version DESC) recency
      FROM
        forecast_groups
      WHERE (instance_id = 'YourAmazonConnectInstanceId')
   )  t
   WHERE (recency = 1)
)
, latest_staffing_group_forecast_groups AS (
   SELECT
     staffing_group_arn
   , forecast_group_arn
   FROM
     (
      SELECT
        *
      , RANK() OVER (PARTITION BY staffing_group_arn ORDER BY staffing_group_version DESC) recency
      FROM
        staffing_group_forecast_groups
      WHERE (instance_id = 'YourAmazonConnectInstanceId')
   )  t
   WHERE (recency = 1)
)
SELECT
  ssp.agent_arn
, U.agent_username AS username
, U.agent_routing_profile_id AS routing_profile_id
, CONCAT(u.first_name, ' ', u.last_name) agent_name
, fg.forecast_group_arn
, fg.forecast_group_name
, sg.staffing_group_arn
, sg.staffing_group_name
FROM
 latest_staff_scheduling_profile ssp
INNER JOIN latest_staffing_groups sg ON ssp.staffing_group_arn = sg.staffing_group_arn
INNER JOIN latest_staffing_group_forecast_groups sgfg ON ssp.staffing_group_arn = sgfg.staffing_group_arn
INNER JOIN latest_forecast_groups fg ON fg.forecast_group_arn = sgfg.forecast_group_arn
INNER JOIN USERS u ON ssp.agent_arn = u.user_arn
```

 **Step 3: Get the latest Shift activities ** 

```
CREATE OR REPLACE VIEW "latest_shift_activities_view" AS
SELECT
  shift_activity_arn
, shift_activity_name
, shift_activity_version
, type
, sub_type
, is_adherence_tracked
, is_paid
, last_updated_timestamp
FROM
  (
   SELECT
     *
   , RANK() OVER (PARTITION BY shift_activity_arn ORDER BY shift_activity_version DESC) recency
   FROM
     shift_activities
   WHERE (instance_id = 'YourAmazonConnectInstanceId')
)  t
WHERE (recency = 1)
```

 **Step 4: Create a view to get the agent scheduled shift activities** 

```
CREATE OR REPLACE VIEW "agent_scheduled_shift_activities_view" AS
WITH
  latest_staff_shifts AS (
   SELECT
     agent_arn
   , shift_id
   , shift_version
   , shift_start_timestamp
   , shift_end_timestamp
   , created_timestamp
   , last_updated_timestamp
   , data_lake_last_processed_timestamp
   , recency
   FROM
     (
      SELECT
        RANK() OVER (PARTITION BY shift_id ORDER BY shift_version DESC) recency
      , *
      FROM
        staff_shifts sa
      WHERE (instance_id = 'YourAmazonConnectInstanceId')
   )  t
   WHERE ((recency = 1) AND (is_deleted = false))
)
SELECT
  asgfg.forecast_group_name
, array_join(sn.supervisor_names, ',') supervisor_names
, s.agent_arn
, u.first_name
, u.last_name
, asgfg.staffing_group_name
, ssa.activity_id
, (CASE WHEN (ssa.shift_activity_arn IS NULL) THEN COALESCE(sa.shift_activity_name, 'Work') ELSE sa.shift_activity_name END) shift_activity_name
, s.shift_start_timestamp
, s.shift_end_timestamp
, (CASE WHEN (ssa.shift_activity_arn IS NULL) THEN COALESCE(sa.type, 'PRODUCTIVE') ELSE sa.type END) type
, (CASE WHEN (ssa.shift_activity_arn IS NULL) THEN COALESCE(sa.is_paid, true) ELSE sa.is_paid END) is_paid
, ssa.activity_start_timestamp
, ssa.activity_end_timestamp
, ssa.last_updated_timestamp
, ssa.data_lake_last_processed_timestamp
, u.agent_username as username
, u.agent_routing_profile_id as routing_profile_id
FROM
  staff_shift_activities ssa
INNER JOIN latest_staff_shifts s ON s.shift_id = ssa.shift_id AND s.shift_version = ssa.shift_version
INNER JOIN USERS u ON s.agent_arn = u.user_arn
INNER JOIN latest_agent_staffing_group_forecast_group_view asgfg ON s.agent_arn = asgfg.agent_arn
LEFT JOIN latest_shift_activities_view sa ON sa.shift_activity_arn = ssa.shift_activity_arn
INNER JOIN latest_supervisor_names_view sn ON sn.staffing_group_arn = asgfg.staffing_group_arn
WHERE (ssa.is_deleted = false) AND (COALESCE(ssa.activity_status, ' ') <> 'INACTIVE') AND (ssa.instance_id = 'YourAmazonConnectInstanceId')
```

### 2. Query to get all the time off requests of the Agents in a specific Forecast Group
<a name="query2"></a>

` SELECT * FROM agent_timeoff_report_view where forecast_group_name = 'AnyDepartmentForecastGroup' `

 Use the following query to create `agent_timeoff_report_view` mentioned above.

```
CREATE OR REPLACE VIEW "agent_timeoff_report_view" AS
WITH latest_staff_timeoffs AS (
        SELECT t1.*,
            CAST((t1.effective_timeoff_hours * 60) AS INT) total_effective_timeoff_minutes
        FROM (
                SELECT RANK() OVER (
                        PARTITION BY timeoff_id
                        ORDER BY timeoff_version DESC
                    ) recency,
                    agent_arn,
                    timeoff_id,
                    shift_activity_arn,
                    timeoff_status,
                    timeoff_version,
                    effective_timeoff_hours,
                    timeoff_start_timestamp,
                    timeoff_end_timestamp,
                    last_updated_timestamp,
                    data_lake_last_processed_timestamp
                FROM staff_timeoffs
                WHERE (
                        instance_id = 'YourAmazonConnectInstanceId'
                    )
            ) t1
        WHERE (recency = 1)
    )
SELECT asgfg.forecast_group_name,
    to.agent_arn,
    asgfg.agent_name,
    asgfg.staffing_group_name,
    asgfg.username,
    sa.shift_activity_name,
    to.timeoff_start_timestamp,
    to.timeoff_end_timestamp,
    to.timeoff_status,
    array_join(sn.supervisor_names, ',') AS supervisor_names,
    sa.is_paid,
    to.last_updated_timestamp,
    to.data_lake_last_processed_timestamp,
    u.agent_routing_profile_id AS routing_profile_id,
    to.timeoff_id,

    to.shift_activity_arn,
    to.total_effective_timeoff_minutes
FROM latest_staff_timeoffs to
    INNER JOIN latest_agent_staffing_group_forecast_group_view asgfg ON asgfg.agent_arn = to.agent_arn
    INNER JOIN latest_shift_activities_view sa ON sa.shift_activity_arn = to.shift_activity_arn
    INNER JOIN latest_supervisor_names_view sn ON sn.staffing_group_arn = asgfg.staffing_group_arn
    INNER JOIN users u ON u.user_arn = to.agent_arn
```