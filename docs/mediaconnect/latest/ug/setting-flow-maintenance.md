

# Setting flow maintenance windows
<a name="setting-flow-maintenance"></a>

You can set or change the maintenance window for a flow, regardless of whether the flow is active or stopped. You specify a preferred day and start hour, and MediaConnect performs maintenance within the two-hour window starting at that time.

**Important**  
You cannot change the maintenance window for a flow within 4 hours of the scheduled maintenance start time, or while maintenance is in progress.

**To set a maintenance window (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Flows**.

1. Select the check box next to one or more flows that you want to update.

1. Choose **Flow actions**, and then choose **Update maintenance window**.

1. For **Start day**, choose the preferred day of the week.

1. For **Start hour**, choose the preferred start time (UTC).

1. (Optional) If maintenance is required for the flow, the **Maintenance window date** field is available. Select a specific date for the next maintenance event. The selected date must be before the required-by deadline.

1. Choose **Update**.

**To set a flow maintenance window (AWS CLI)**  
Use the `update-flow` command with the `--maintenance` parameter to set the preferred maintenance day and start hour.

The following example sets the maintenance window for a flow to Tuesday at 10:00 UTC:

```
aws mediaconnect update-flow \
  --flow-arn arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame \
  --maintenance MaintenanceDay='Tuesday',MaintenanceStartHour='10:00'
```

The following example shows the return value:

```
{
    "Flow": {
        "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
        "Name": "BasketballGame",
        ...
        "Status": "STANDBY",
        "Maintenance": {
            "MaintenanceDay": "Tuesday",
            "MaintenanceStartHour": "10:00"
        }
    }
}
```

**Setting a specific maintenance date**  
If maintenance is required for a flow, you can specify a particular date for maintenance to occur by including the `MaintenanceScheduledDate` parameter. The selected date must be before the required-by deadline.

**Note**  
If you change the preferred day or start hour and a maintenance date is already scheduled, you must also update the scheduled date to match your new preferences.

The following example sets the maintenance window to Friday at 01:00 UTC and schedules maintenance for June 5, 2026:

```
aws mediaconnect update-flow \
  --flow-arn arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame \
  --maintenance MaintenanceDay='Friday',MaintenanceStartHour='01:00',MaintenanceScheduledDate='2026-06-05'
```

The following example shows the return value:

```
{
    "Flow": {
        "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
        "Name": "BasketballGame",
        ...
        "Status": "ACTIVE",
        "Maintenance": {
            "MaintenanceDay": "Friday",
            "MaintenanceDeadline": "2026-06-07T00:00:00Z",
            "MaintenanceScheduledDate": "2026-06-05",
            "MaintenanceStartHour": "01:00"
        }
    }
}
```