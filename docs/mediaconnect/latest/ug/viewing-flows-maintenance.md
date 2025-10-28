# Viewing MediaConnect flows that require maintenance

You can view flows that require maintenance in the MediaConnect console or by using the
AWS CLI.

###### Note

If your flow does not have a **Required by date** (console) or a
**MaintenanceDeadline** (AWS CLI), maintenance is not currently
required for that flow.

###### To view the flows that require maintenance (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Flows**.
3. In the **Maintenance window** column, you can view the
   **Required by date**. Alternatively, you can view the
   **Required by date** on an individual flows
   **Details** page.
4. All listed flows must be restarted by the date shown.

###### To view the flows that require maintenance (AWS CLI)

- In the AWS CLI, you can use the `list-flows` command to view all
  flows and their maintenance statuses. Additionally, you can view a specific
  flows maintenance status by using the `describe-flow` command:

```
aws mediaconnect list-flows
```

or

```
aws mediaconnect describe-flow --flow-arn `arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame`
```

The following example shows the return value of `list-flows`. The
return value for `describe-flow` uses a similar structure.

In this example, the Flow named _BasketballGame_ has a **MaintenanceDay** and
**MaintenanceStartHour** set for recurring maintenance. The
Flow named _AwardsShow_ has the
**MaintenanceDay** and
**MaintenanceStartHour** set, but also a
**MaintenanceDeadline**. The
**MaintenanceDeadline** is the required due date for
maintenance restarts on this flow. The _AwardsShow_ flow has also scheduled a specific date for the
maintenance restarts to occur, seen in the
**MaintenanceScheduledDate** value. The
**MaintenanceScheduledDate** must occur before the
**MaintenanceDeadline**:

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
                "MaintenanceDay": "Monday",
                "MaintenanceStartHour": "08:00"}
        },
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
