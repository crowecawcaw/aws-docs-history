# Setting maintenance windows

You can select the day and time that maintenance events occur. This is called a
_maintenance window_. These windows help minimize
maintenance impact on your production.

A maintenance window is used every time a maintenance event is required. You can set a
maintenance window while creating a flow, or add the window to an existing flow. To
change the day and time of a maintenance window, you can use the MediaConnect console or the
AWS CLI. Also, if maintenance is required, you can set a specific date for the maintenance
to occur. The date you select must be before the required maintenance date.

If you don't set a maintenance window, MediaConnect restarts the flows for you. We recommend
that you set a maintenance window for each flow that requires maintenance.

###### To set a maintenance window (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Flows**. When a flow
   requires maintenance, it will display a **Required by** date
   under the **Maintenance window** column.
3. Select the flow or flows. You can set a unique maintenance window for each
   flow. Alternatively, you can set maintenance windows in bulk by selecting
   multiple flows.
4. Under the **Flow actions** drop-down menu, select
   **Edit flow maintenance window**.
5. - Select the day of the week maintenance will occur in the
     **Start day** field.
   - Select the time maintenance will occur in the **Start
     hour** field. Time is presented in UTC.
   - If maintenance is required, you have the option to select a specific
     date in the **Maintenance window date** field. The
     selected date must occur before the required maintenance date and
     time.
   - Select **Update**.
6. You can verify the window by viewing the **Maintenance
   window** column on the **Flows** dashboard.

###### To set a maintenance window (AWS CLI)

1. In the AWS CLI, use the `update-flow` command with the
   `--maintenance` option. You will also need to use the
   `--flow-arn` option to specify which flow you are working with.

The `--maintenance` option accepts the following arguments:

    * `MaintenanceDay`
    * `MaintenanceStartHour`
    * `MaintenanceScheduleDate` - This argument is only accepted
     when there is a required maintenance date assigned by AWS.

2. Use the following command to update the reoccurring maintenance day and time.
   The maintenance day and time can be configured at any time, regardless of
   required maintenance status.

```
aws mediaconnect update-flow --flow-arn `arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame` --maintenance MaintenanceDay=`'Tuesday'`,MaintenanceStartHour=`'10:00'`
```

The following example shows the return value when only setting the
**MaintenanceDay** and
**MaintenanceStartHour**:

```
{
    "Flows": [
        {
            "AvailabilityZone": "us-west-2d",
            "Description": "Example flow description",
            "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
            "Name": "BasketballGame",
            "SourceType": "OWNED",
            "Status": "STANDBY",
            "Maintenance": {
                "MaintenanceDay": "Tuesday",
                "MaintenanceStartHour": "10:00"}
        }
    ]
}
```

3. Use the following command to set a specific maintenance date, in addition to
   setting the reoccurring maintenance day and time. The maintenance scheduled date
   can only be set when AWS requires maintenance on the flow.

```
aws mediaconnect update-flow --flow-arn `arn:aws:mediaconnect:us-east-1:111122223333:flow:2-3aBC45dEF67hiJ8k-2AbC34DE5fGa6:AwardsShow` --maintenance MaintenanceDay=`'Saturday'`,MaintenanceStartHour=`'23:00'`,MaintenanceScheduledDate=`'2021-10-23'`
```

The following example shows the return value when setting the
**MaintenanceDay**,
**MaintenanceStartHour**, and
**MaintenanceScheduledDate**:

```
{
    "Flows": [
        {
            "AvailabilityZone": "us-west-2b",
            "Description": "Example flow description",
            "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:2-3aBC45dEF67hiJ8k-2AbC34DE5fGa6:AwardsShow",
            "Name": "AwardsShow",
            "SourceType": "OWNED",
            "Status": "ACTIVE",
            "Maintenance": {
                "MaintenanceDay": "Saturday",
                "MaintenanceDeadline": "2021-10-25T22:15:56Z",
                "MaintenanceScheduledDate": "2021-10-23",
                "MaintenanceStartHour": "23:00"}
         }
    ]
}
```

The selected day and time are used for all future recurring maintenance events on that
flow. Repeat these steps to add or edit additional maintenance windows. After
maintenance is complete, the **Maintenance status** column on the
**Flows** dashboard will display **No maintenance
required**.
