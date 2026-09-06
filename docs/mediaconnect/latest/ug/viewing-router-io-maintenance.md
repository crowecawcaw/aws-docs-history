

# Viewing router I/O maintenance status
<a name="viewing-router-io-maintenance"></a>

You can view the maintenance status of your router I/Os in the MediaConnect console or by using the AWS CLI.

**To view router I/O maintenance status (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Global routing**, choose **Router inputs** or **Router outputs**.

1. The **Time until maintenance** column shows the number of days remaining until the next scheduled maintenance, or "No maintenance scheduled" if no maintenance is pending.

1. Choose the number of days remaining to view additional details, including the window start time, window end time, and scheduled maintenance time.

**To view router I/O maintenance status (AWS CLI)**  
Use the `list-router-inputs` or `list-router-outputs` command to see maintenance status across all router I/Os. You can also use the `get-router-input` or `get-router-output` command for a specific router I/O.

The response includes maintenance details in the `Maintenance`-related fields. Active I/Os with scheduled maintenance include `MaintenanceScheduleType` and `MaintenanceSchedule`:

```
{
    "RouterInputs": [
        {
            "Name": "StudioCam1",
            "Arn": "arn:aws:mediaconnect:us-east-1:111122223333:routerInput:a1b2c3d4e5f6",
            "State": "ACTIVE",
            ...
            "MaintenanceScheduleType": "WINDOW",
            "MaintenanceSchedule": {
                "Window": {
                    "Start": "2026-07-20T04:00:00+00:00",
                    "End": "2026-07-20T06:00:00+00:00",
                    "ScheduledTime": "2026-07-20T04:30:00+00:00"
                }
            }
        },
        {
            "Name": "StudioCam2",
            "Arn": "arn:aws:mediaconnect:us-east-1:111122223333:routerInput:g7h8i9j0k1l2",
            "State": "STANDBY",
            ...
        }
    ]
}
```